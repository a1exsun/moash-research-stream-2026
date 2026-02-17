# 基于数据重放的 LLM 持续预训练架构设计

## 1. 问题与动机

当前 LLM 训练采用分阶段范式：预训练 → SFT → RLHF，每个阶段是独立的。模型部署后无法持续吸收新知识。如果需要更新模型知识（如新领域文档、用户交互记录），通常需要重新训练或在新数据上 fine-tune，后者容易导致**灾难性遗忘**——模型在学习新知识时遗忘旧能力。

**本方案的目标**：设计一种统一的持续预训练架构，支持将模型推理时的上下文数据（in-context learning 获取的知识）固化为模型权重，同时通过新旧数据混合采样避免灾难性遗忘。

### 适用场景

- **新知识吸收**：将比训练数据更新的技术文档、新闻等固化为权重
- **长期记忆**：将用户对话历史写入模型，使模型"永远记住"
- **领域适配**：持续引入特定领域数据，逐步增强模型在该领域的能力

### 类比

类似人脑的**海马体-新皮层巩固机制**：白天（推理时）海马体快速编码新经验，夜间（巩固时）通过重放将新记忆与已有记忆交叉整合，写入新皮层的长期存储。

---

## 2. 架构总览

```
┌─────────────────────────────────────────────────────────────────┐
│                         推理阶段                                 │
│  用户交互 / 新文档处理 → 上下文数据 → Memory Buffer (持久化存储)    │
└──────────────────────────────┬──────────────────────────────────┘
                               │ 手动触发
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                        巩固阶段 (Consolidation)                  │
│                                                                  │
│   Memory Buffer (新数据)  ──┐                                    │
│                             ├→ 混合采样器 → BOS-aligned Packing   │
│   原始训练集 (旧数据)    ──┘   (new:old               → Batch     │
│                               可配置,                             │
│                               默认 1:9)                          │
│                                      │                           │
│                                      ▼                           │
│                              持续预训练 N steps                   │
│                              (从 checkpoint 续训)                 │
│                                      │                           │
│                                      ▼                           │
│                              新 checkpoint                       │
│                              + 遗忘检测 (eval)                   │
└─────────────────────────────────────────────────────────────────┘
```

系统由三个核心组件构成：
1. **Memory Buffer** — 捕获并存储推理时上下文数据
2. **混合数据加载器** — 从多个数据源按权重采样并打包
3. **巩固训练器** — 从已有 checkpoint 出发，混合数据短周期续训

---

## 3. Memory Buffer — 记忆缓冲区

### 功能

在模型推理过程中，将有价值的上下文数据（用户对话、新文档、新知识）捕获并持久化存储，供后续巩固训练使用。

### 设计

**存储格式**：Parquet 文件（列式存储，高压缩比，与主流训练数据格式一致）

**Schema**：
```
text: string     # 原始文本（与预训练数据格式一致）
```

只存储原始文本而非 token ID，原因：
- tokenizer 可能在后续版本中变化
- 文本格式通用性更强，可被任何 tokenizer 处理
- 便于人工检查和筛选

**存储结构**：
```
memory_buffers/
  buffer_20240301_143022.parquet    # 按时间戳命名
  buffer_20240301_183045.parquet
  ...
```

**接口**：
```python
class MemoryBuffer:
    def __init__(self, buffer_dir: str, flush_size: int = 1000):
        """
        buffer_dir:  缓冲区存储目录
        flush_size:  累积多少条记录后自动写入磁盘
        """

    def add(self, text: str):
        """添加一条文本记录到内存缓冲区"""

    def flush(self):
        """将内存中累积的记录写入新的 parquet 文件"""

    def list_buffers(self) -> list[str]:
        """列出所有 parquet 缓冲文件路径"""

    def total_sequences(self) -> int:
        """统计总记录数"""
```

**捕获时机**：在推理引擎中可选启用，每次对话/文档处理完成后将文本存入 buffer。MVP 阶段由用户手动触发 flush，后续可自动化。

---

## 4. 混合数据加载器 (Mixed Dataloader)

### 功能

从多个数据源按指定权重采样文档，统一送入 packing 算法生成训练 batch。

### 核心思路

现有 LLM 预训练通常使用单一数据源的 dataloader。本组件将其扩展为**多数据流加权采样**：

```
数据流 A (原始训练集, weight=0.9) ──┐
                                     ├→ 加权采样 → 文档缓冲区 → Packing → Batch
数据流 B (Memory Buffer, weight=0.1)┘
```

### 设计

```python
def mixed_data_loader(
    tokenizer,
    batch_size: int,          # 每个 batch 的序列数 B
    seq_len: int,             # 每个序列的 token 长度 T
    sources: list[tuple[dict, float]],  # [(数据源配置, 采样权重), ...]
    device: str = "cuda",
    buffer_size: int = 1000,  # 文档缓冲区大小
):
    """
    sources 示例:
    [
        ({"type": "pretrain_corpus", "path": "/data/fineweb"}, 0.9),
        ({"type": "memory_buffer",   "path": "/data/memory_buffers"}, 0.1),
    ]
    """
```

### 采样算法

```
初始化:
  为每个数据源创建独立的文档迭代器 (infinite iterator)
  归一化权重向量

循环:
  while 文档缓冲区大小 < buffer_size:
      按权重随机选择一个数据源
      从该数据源获取下一批文档
      tokenize 后放入缓冲区

  从缓冲区中用 bestfit packing 打包 B 个序列
  yield batch(inputs, targets)
```

**关于 Packing 算法**：

推荐使用 **BOS-aligned Best-Fit Packing**：
- 每个序列以 BOS token 开头
- 将不同长度的文档用 best-fit 算法紧凑地拼接进固定长度的序列
- 当剩余空间无法放下任何完整文档时，从最短文档裁剪填满
- 100% token 利用率（无 padding）

这种 packing 方式确保每个 token 都能 attend 到自己文档开头的 BOS，比简单拼接（concatenation）产生更少的跨文档 attention 噪声。

### 数据源类型

| 类型 | 描述 | 实现 |
|------|------|------|
| `pretrain_corpus` | 原始预训练语料（如 FineWeb, CommonCrawl） | 从 parquet 分片中 round-robin 读取 |
| `memory_buffer` | Memory Buffer 中的新数据 | 遍历 buffer parquet 文件 |
| `curated_dataset` | 手动策展的高质量数据集 | 从指定目录读取（扩展用） |

每种数据源都是一个返回文本字符串的无限迭代器。如果数据量不足则循环（multi-epoch）。

---

## 5. 巩固训练器 (Consolidation Trainer)

### 功能

从已有 checkpoint 出发，使用混合数据进行短周期持续预训练，将 Memory Buffer 中的新知识固化为权重。

### 输入参数

```
必需参数:
  --checkpoint         已有模型 checkpoint 路径
  --memory-buffer-dir  Memory Buffer 目录

训练参数:
  --num-iterations     巩固步数 (默认 1000)
  --new-data-ratio     新数据采样比例 (默认 0.1，即 new:old = 1:9)
  --total-batch-size   总 batch size in tokens (默认 524288 ≈ 0.5M)
  --device-batch-size  每设备 batch size

学习率参数:
  --lr-scale           峰值 LR 相对于原始预训练 LR 的缩放因子 (默认 0.1)
  --warmup-ratio       LR warmup 比例 (默认 0.1)
  --warmdown-ratio     LR warmdown 比例 (默认 0.5)

评估参数:
  --eval-after         巩固后是否运行评估检测遗忘
```

### 训练流程

```
1. 加载 checkpoint (模型权重 + 优化器状态)
2. 构建混合 dataloader:
     sources = [
         (原始训练集, 1 - new_data_ratio),
         (Memory Buffer, new_data_ratio),
     ]
3. 设置 LR schedule:
     峰值 LR = 原始 LR × lr_scale  (默认为原始的 1/10)
     schedule = warmup → constant → cosine warmdown
4. 训练循环 (num_iterations 步):
     - 从混合 dataloader 获取 batch
     - 前向传播 + 计算 loss (标准 cross-entropy)
     - 反向传播 + 梯度更新
     - 日志记录 (loss, LR, ...)
5. 保存新 checkpoint
6. (可选) 运行评估:
     - 在原始验证集上计算 BPB (bits per byte)
     - 在 Memory Buffer 的 held-out 集上计算 BPB
     - 运行标准化评估基准 (如 CORE metric)
     - 对比巩固前后的指标，检测遗忘
```

### 学习率策略

巩固训练使用**更低的峰值学习率**，避免大幅修改已学到的权重：

```
LR
│
│  peak_lr = original_lr × 0.1
│  ┌──────────────┐
│ /                \
│/                  \
│                    \________  final_lr = peak_lr × 0.1
└─────────────────────────────→ steps
  warmup  constant   warmdown
  (10%)    (40%)      (50%)
```

**为什么使用较低 LR**：
- 巩固的目标是"微调式整合"而非"从头学习"
- 高 LR 会破坏已有权重分布，加速遗忘
- 类似生物学中睡眠巩固的低频、反复重放特征

### Checkpoint 兼容性

巩固产生的 checkpoint 与原始预训练 checkpoint **格式完全一致**：
- 可以在巩固后继续巩固（迭代巩固）
- 可以在巩固后进行 SFT / RLHF
- 可以直接用于推理
- 记录 metadata：`parent_checkpoint`, `consolidation_config`, `memory_buffer_stats`

---

## 6. 抗灾难性遗忘策略

### 核心方法：经验重放 (Experience Replay)

本方案采用最简单有效的抗遗忘策略——**新旧数据混合训练**：

- 每个 batch 中，约 90% 的 token 来自原始预训练语料，10% 来自新数据
- 通过持续暴露旧数据，模型在学习新知识的同时被迫"复习"旧知识
- 比例可配置，根据新数据量和重要程度调整

**为什么选择这种方法而非其他**：

| 方法 | 优点 | 缺点 | 选择理由 |
|------|------|------|----------|
| **数据混合重放** ✓ | 简单、直观、有效 | 需要访问旧数据 | 适合有原始训练集的场景 |
| EWC (弹性权重巩固) | 不需要旧数据 | 需计算 Fisher 矩阵，超参敏感 | 过于复杂 |
| 知识蒸馏 | 理论上更优 | 需维护 teacher 模型，计算翻倍 | 工程负担大 |
| LoRA/Adapter | 不修改原始权重 | 知识未真正整合到主网络 | 不符合"固化"目标 |

### 关键超参建议

- **new_data_ratio = 0.05 ~ 0.2**：新数据量少时用更低比例，数据量大时可适当提高
- **num_iterations**：通常 500 ~ 5000 步，取决于新数据量。经验法则：确保新数据被看到 3~10 次
- **lr_scale = 0.05 ~ 0.2**：峰值 LR 为原始预训练的 5% ~ 20%

### 遗忘检测

每次巩固后运行标准评估，检查：
- 原始验证集 BPB 是否上升（上升 = 遗忘）
- 标准化基准分数是否下降
- 若检测到显著遗忘（如 BPB 上升 > 2%），可：降低 new_data_ratio、降低 lr_scale、增加 num_iterations

---

## 7. 端到端工作流

### 日常使用模式

```
第一天 (推理):
  用户与模型交互，讨论量子计算话题
  系统自动将对话存入 Memory Buffer
  用户阅读新技术文档，系统将文档存入 Memory Buffer

夜间 (巩固):
  用户手动触发巩固训练
  系统混合 Memory Buffer 中的新数据 (10%) 与原始训练集 (90%)
  运行 1000 步持续预训练
  保存新 checkpoint，运行评估确认无遗忘

第二天 (推理):
  加载巩固后的模型
  模型现在"记住了"昨天的量子计算讨论和技术文档内容
  无需在 prompt 中重复这些上下文
```

### 迭代巩固

支持多次巩固：

```
Checkpoint v0 (原始预训练)
    │
    ├── 巩固 #1：学习用户偏好 → Checkpoint v1
    │
    ├── 巩固 #2：学习新技术文档 → Checkpoint v2
    │
    └── 巩固 #3：学习领域知识 → Checkpoint v3
```

每次巩固都从上一次的 checkpoint 继续，Memory Buffer 可以累积或清空。

---

## 8. 局限性与开放问题

### 已知局限

1. **需要访问原始训练数据**：数据混合重放要求能采样原始预训练语料。如果原始数据不可获得，需要替代方案（如使用公开的通用语料替代）。

2. **新数据质量敏感**：低质量的新数据（噪声、错误信息）会直接被学习。MVP 阶段不做自动质量过滤，依赖用户判断。

3. **遗忘的度量**：BPB 和标准基准只能检测粗粒度遗忘。特定知识点的遗忘可能无法被这些指标捕捉。

4. **规模限制**：本方案面向中小规模模型（<10B 参数）。超大规模模型的巩固训练计算成本可能过高。

### 待讨论的开放问题

1. **Memory Buffer 中的数据应该如何预处理？** 推理时的上下文包含 system prompt、特殊标记等，是否需要清洗？还是保持原样让模型学习完整的对话格式？

2. **巩固的粒度**：应该频繁小量巩固（每天 100 步）还是低频大量巩固（每周 1000 步）？两者对遗忘-学习平衡的影响？

3. **旧数据采样策略**：从原始训练集中均匀随机采样，还是加权采样（如偏向与新数据领域相关的旧数据）？

4. **优化器状态处理**：巩固时是否应该继承原始训练的优化器状态（动量、二阶矩）？还是重新初始化？继承可能有利于稳定性，重新初始化可能有利于适应新数据分布。

5. **何时该用持续预训练 vs. RAG？** 对于快速变化的事实性知识，RAG 可能更合适。持续预训练更适合"技能型"知识和长期偏好。两者的分界线在哪里？

---

## 9. MVP 实现范围

MVP 聚焦于跑通核心流程，不做工程化优化：

- [x] Memory Buffer：简单的 parquet 存储
- [x] 混合 Dataloader：双源加权采样
- [x] 巩固训练脚本：从 checkpoint 续训
- [x] 推理端集成：可选保存对话到 buffer
- [x] 遗忘检测：巩固后运行 eval
- [ ] ~~自动化触发机制~~（后续）
- [ ] ~~数据质量过滤~~（后续）
- [ ] ~~自适应采样比例~~（后续）
- [ ] ~~分布式巩固训练~~（后续）
