# Hippocampal Sparse Transformer (HST) — 持续学习架构设计

## 1. 动机与核心洞察

### 问题

标准 dense transformer 在每次梯度更新时修改所有参数，导致新知识学习不可避免地干扰旧知识——灾难性遗忘。这是架构层面的根本缺陷。

**为什么简单的稀疏化不够？**

```
Dense Network = 一本巨大的笔记本
  所有知识写在同一页上 → 写新内容必然覆盖旧内容

Sparse Network = 一本稀疏的笔记本
  只有 5% 的格子能写字 → 但所有知识仍在同一批格子里 → 仍然覆盖

我们需要的 = 图书馆
  不同书架存不同主题
  查"物理"→ 只去物理书架
  更新"物理"→ 只改物理书架的书
  化学书架完全不受影响
```

**核心洞察**：避免灾难性遗忘需要三个条件同时满足：
1. **路由隔离** — 不同知识被路由到不同的参数子集（"不同书架"）
2. **局部更新** — 更新一个子集不影响其他子集（"改物理书不动化学书"）
3. **动态扩展** — 遇到全新领域时可以"新建书架"

### 生物学启示

- **新皮层的功能分区**：视觉皮层、听觉皮层、语言区等功能分区处理不同类型的信息 → 对应 Expert 隔离
- **86B 神经元，~7000 突触/神经元，10⁻⁵% 全局连接密度** → 每个分区内部也是极度稀疏的
- **突触可塑性**：连接持续生长和消亡 → 对应 Expert 内部的动态稀疏拓扑（可选优化）

### 关键文献

- [Brain-inspired sparse training (NeurIPS 2025)](https://arxiv.org/abs/2501.19107)：1%-5% 密度可匹配全连接性能
- [Sparse Memory Finetuning (2025)](https://arxiv.org/abs/2510.15103)：稀疏记忆层 + 选择性更新，遗忘率从 89% 降至 11%
- [Split-on-Share: MoE for Task-Agnostic CL (2025)](https://arxiv.org/html/2601.17616v1)：稀疏专家混合实现持续学习
- [Mixtures of SubExperts for LLM CL (2025)](https://arxiv.org/html/2511.06237)：子专家混合用于大语言模型持续学习
- [Dynamic Sparse Training (ICLR 2024)](https://arxiv.org/abs/2305.02299)：结构化稀疏训练可获得真实硬件加速

---

## 2. 架构总览

```
                    Hippocampal Sparse Transformer (HST)
    ┌──────────────────────────────────────────────────────────────┐
    │                                                              │
    │   Token Embedding                                            │
    │       │                                                      │
    │       ▼                                                      │
    │   ┌──────────────────────────────────────────────────────┐   │
    │   │            HST Block ×N (repeated)                    │   │
    │   │                                                       │   │
    │   │   ┌─────────────────────────────────────────────┐    │   │
    │   │   │  Attention (standard, dense)                  │    │   │
    │   │   │  - RoPE, Flash Attention, QK-norm             │    │   │
    │   │   └─────────────────────────────────────────────┘    │   │
    │   │       │                                               │   │
    │   │       ▼                                               │   │
    │   │   ┌─────────────────────────────────────────────┐    │   │
    │   │   │  Key-Routed Sparse MoE FFN                   │    │   │
    │   │   │                                              │    │   │
    │   │   │  Key Router (non-learnable):                 │    │   │
    │   │   │    x → cosine match against expert keys      │    │   │
    │   │   │    → top-k experts activated                 │    │   │
    │   │   │    → novelty detection                       │    │   │
    │   │   │                                              │    │   │
    │   │   │  Expert Pool (dynamically growable):         │    │   │
    │   │   │  ┌─────┐ ┌─────┐ ┌─────┐     ┌─────┐      │    │   │
    │   │   │  │ E_0 │ │ E_1 │ │ E_2 │ ... │ E_n │      │    │   │
    │   │   │  └─────┘ └─────┘ └─────┘     └─────┘      │    │   │
    │   │   │  (each: FFN, optionally sparse ~5%)         │    │   │
    │   │   └─────────────────────────────────────────────┘    │   │
    │   └──────────────────────────────────────────────────────┘   │
    │       │                                                      │
    │       ▼                                                      │
    │   Output Head                                                │
    │                                                              │
    │   ═══════════════════════════════════════════════════════    │
    │   训练侧 (不在模型计算图中):                                   │
    │                                                              │
    │   Smart Sampler                                              │
    │   ┌─────────────────────────────────────────────────────┐   │
    │   │  推理时记录: (text, expert_routing_log)              │   │
    │   │  巩固时构建: per-expert coreset + 旧数据采样          │   │
    │   │  → 定向微调对应 expert, 冻结其他                      │   │
    │   └─────────────────────────────────────────────────────┘   │
    └──────────────────────────────────────────────────────────────┘
```

### 系统组成

| 组件 | 类型 | 功能 |
|------|------|------|
| **Key-Routed MoE** | 模型架构 | 知识隔离存储，不可遗忘的路由 |
| **Sparse Expert Internals** | 模型架构（可选） | Expert 内部稀疏化，进一步减少更新干扰 |
| **动态 Expert 增长** | 模型架构 | 遇新领域时扩展知识容量 |
| **Smart Sampler** | 训练算法 | 推理时收集数据+路由日志，巩固时构建 per-expert coreset |
| **Coreset 微调** | 训练算法 | 按需对特定 expert 做定向微调 |

**关键简化**：上一版的"海马体神经网络层"（模型中的额外 KV 记忆模块）被替换为训练侧的 **Smart Sampler**（纯算法模块，不改变模型前向传播）。模型本身更干净——只有 Attention + MoE FFN，没有额外的记忆层。

---

## 3. Key-Routed Sparse MoE — 基于 Key 匹配的路由

### 3.1 为什么不用可学习路由器？

标准 MoE 的路由器是一个小型可学习网络（通常是 `Linear(d, num_experts)`）。在持续学习场景下，这个路由器本身会遗忘：

```
Step 1: 路由器学会 "物理 token → Expert 3"
Step 2: 学习化学，路由器参数更新
Step 3: 路由器可能忘记 "物理 → Expert 3" 的映射
→ 物理 token 被路由到错误的 expert → 旧知识不可访问 → 等效于遗忘
```

### 3.2 Key-Based Routing（键匹配路由）

每个 expert 维护一个 **key 向量**（不参与梯度更新），路由通过余弦相似度匹配完成：

```python
class KeyRouter(nn.Module):
    def __init__(self, dim, num_initial_experts, top_k=2, novelty_threshold=0.3):
        super().__init__()
        # Expert keys: buffer, 不参与梯度更新
        self.register_buffer('expert_keys', torch.randn(num_initial_experts, dim))
        self.top_k = top_k
        self.novelty_threshold = novelty_threshold
        self.key_momentum = 0.99  # EMA 更新动量

    def forward(self, x):
        # x: (B, T, d)
        x_norm = F.normalize(x, dim=-1)
        k_norm = F.normalize(self.expert_keys, dim=-1)
        sim = x_norm @ k_norm.T  # (B, T, num_experts)

        top_sim, top_idx = sim.topk(self.top_k, dim=-1)
        weights = F.softmax(top_sim, dim=-1)

        # 新颖性检测
        max_sim = top_sim[..., 0]
        needs_new = (max_sim < self.novelty_threshold)

        return top_idx, weights, needs_new

    @torch.no_grad()
    def update_key_ema(self, expert_id, hidden_states):
        """预训练时通过 EMA 缓慢更新 expert key"""
        mean_h = hidden_states.mean(dim=0)
        self.expert_keys[expert_id] = (
            self.key_momentum * self.expert_keys[expert_id] +
            (1 - self.key_momentum) * F.normalize(mean_h, dim=-1)
        )
```

**Expert Key 的来源**：
- 预训练阶段：expert key = 该 expert 处理过的 token 的 hidden state 的 EMA 均值
- 新 expert 创建时：key = 触发创建的那批新数据的 hidden state 均值
- Key 是 expert 的"身份标识"，描述"这个 expert 擅长什么"

**为什么这避免了遗忘？**
- Expert key 是 buffer，不参与梯度更新 → 不会被新数据修改
- Key 匹配是纯计算操作（余弦相似度）→ 没有可学习参数 → 没有遗忘的可能
- 物理 expert 的 key 永远是"物理方向"的向量 → 物理 token 永远被路由到物理 expert

### 3.3 动态 Expert 增长

当路由器检测到新知识与所有现有 expert 都不匹配时（`max_sim < threshold`），系统创建新 expert：

```
新 Expert 创建流程:

1. 检测触发: 连续 M 个 batch 中，有 >p% 的 token 满足 max_sim < threshold
2. 收集这些"无归属" token 的 hidden states
3. 对这些 hidden states 取均值 → 新 expert 的 key
4. 初始化新 expert 的 FFN 权重:
   Option A: 随机初始化
   Option B: 从最相似的现有 expert 复制 (迁移学习)
5. 将新 expert 加入 expert pool
6. 路由器自动包含新 expert (因为 key 匹配是动态的)
```

**知识容量随学习增长**：
```
初始预训练: 8 experts/layer  → 基础知识
学习物理:   +1 expert/layer  → 物理知识隔离存储
学习化学:   +1 expert/layer  → 化学知识隔离存储
...
模型容量: 8 + n_new_domains experts/layer
```

### 3.4 计算成本控制

每个 token 只激活 top-k 个 expert（如 k=2）：
- 推理 FLOPs 恒定 = k × single_expert_flops，与 expert 总数无关
- 只有参数量增长，计算量不变
- 这正是 MoE 的核心优势

---

## 4. Sparse Expert Internals — Expert 内部稀疏化（可选优化）

### 4.1 动机

MoE 实现了 expert 之间的路由隔离（"不同书架"）。稀疏化进一步实现 expert 内部的局部性——在同一个书架上更新一本书，不影响旁边的书。

**这是可选优化**：MVP 可以用 dense expert，后续再引入稀疏化。

### 4.2 每个 Expert 是一个稀疏 FFN

```
Standard FFN:  x → W_up(x) → activation → W_down(x)
               W_up: (d, 4d), W_down: (4d, d)  — 全连接

Sparse Expert: x → S_up(x) → activation → S_down(x)
               S_up: (d, 4d) at ~5% density, S_down: (4d, d) at ~5% density
```

**双重隔离**：
- Expert 之间：路由隔离（不同 token 去不同 expert）
- Expert 内部：稀疏隔离（5% 连接 → 每次更新只影响局部）

### 4.3 Expert 内拓扑演化

每个 expert 独立维护自己的稀疏拓扑，训练中动态演化：

```
每 ΔT 步，对每个活跃的 expert:
  1. 剪枝: 移除重要性最低的 p% 连接
     importance(w) = |w| × |∂L/∂w|
  2. 重生长: 在高潜力位置长出 p% 新连接
     基于拓扑启发式 (共同邻居分数) 或梯度信号
  3. 总连接数保持不变
```

**对持续学习的意义**：
- Expert 内编码新的细粒度知识时（如物理 expert 学习量子力学）
- 不需要修改现有的强连接（承载经典力学知识）
- 而是在空闲位置长出新连接来编码新知识

---

## 5. Smart Sampler — 智能数据采样器

替代上一版方案中的"海马体神经网络层"。核心区别：**Smart Sampler 不是模型的一部分，不参与前向传播，而是一个纯算法模块**，负责在推理时收集数据并在巩固时构建训练集。

### 5.1 推理时：数据收集 + 路由日志

```python
class SmartSampler:
    def __init__(self, buffer_dir):
        self.buffer = []  # 待写入的记录

    def record(self, text: str, routing_log: dict):
        """
        推理时调用，记录每次交互。

        text:        原始文本 (对话/文档)
        routing_log: 路由日志，记录每个 token 被路由到哪个 expert
                     格式: {expert_id: token_count} 的统计
                     例: {3: 450, 7: 120, 2: 30} 表示这段文本主要激活了 Expert 3
        """
        self.buffer.append({
            'text': text,
            'primary_expert': max(routing_log, key=routing_log.get),
            'expert_distribution': routing_log,
            'timestamp': time.time(),
        })

    def flush(self):
        """写入磁盘 (parquet 格式)"""
        # 写入 buffer_dir/buffer_{timestamp}.parquet
        ...
```

**与海马体层的关键区别**：
| | 海马体神经网络层（上一版） | Smart Sampler（本版） |
|---|---|---|
| 位置 | 模型计算图内 | 模型外，训练侧 |
| 参数 | 有可学习参数 (keys, values) | 无参数 |
| 推理开销 | 增加 ~10% FLOPs | 几乎为零（只记录日志） |
| 复杂度 | 需要训练 memory slot | 只需要文件 I/O |
| Expert 关联 | 通过 affinity 统计推断 | 直接记录路由日志，精确 |

### 5.2 巩固时：Per-Expert Coreset 构建

```python
class SmartSampler:
    ...
    def build_coreset(self, expert_id, old_data_source, new_old_ratio=0.2):
        """
        为特定 expert 构建巩固训练集。

        1. 从 buffer 中筛选 primary_expert == expert_id 的新数据
        2. 从 old_data_source 中采样路由到该 expert 的旧数据
        3. 按 new_old_ratio 混合
        """
        # 新数据: 从 buffer 中筛选
        new_data = [r['text'] for r in self.all_records()
                    if r['primary_expert'] == expert_id]

        # 旧数据: 从原始训练集采样
        # (需要预先建立 "expert_id → 旧数据子集" 的索引)
        old_data = old_data_source.sample_for_expert(expert_id,
                    n=len(new_data) * int((1 - new_old_ratio) / new_old_ratio))

        return new_data, old_data
```

**Coreset 的含义**：不是用全部旧数据，而是只用路由到该 expert 的旧数据子集。这确保旧数据与 expert 的知识领域匹配，微调效率更高。

---

## 6. Coreset 微调 — 按需定向巩固

替代上一版的"睡眠巩固"。核心简化：**不需要复杂的多阶段巩固流程，直接对特定 expert 做标准微调**。

### 6.1 流程

```
按需 Coreset 微调:

输入:
  - 当前模型 checkpoint
  - Smart Sampler 中累积的新数据 + 路由日志
  - 原始训练集 (采样用)

═══════════════════════════════════════════════════

Step 1: 确定需要更新的 expert

  统计 Smart Sampler 中每个 expert 的新数据量:
    expert_3: 2000 条新数据 → 需要巩固
    expert_7: 500 条新数据  → 需要巩固
    expert_1: 3 条新数据    → 跳过 (太少)

═══════════════════════════════════════════════════

Step 2: 逐 Expert 微调

  对每个需要更新的 expert (可并行):

    a) 构建 coreset:
       new_data = sampler.get_new_data(expert_id)
       old_data = sampler.sample_old_data(expert_id, ratio=4:1)
       coreset = shuffle(new_data + old_data)

    b) 冻结模型其他部分，只解冻当前 expert:
       for param in model.parameters():
           param.requires_grad = False
       for param in model.experts[expert_id].parameters():
           param.requires_grad = True

    c) 标准微调:
       for step in range(num_steps):
           batch = next(coreset_loader)
           loss = model(batch)  # 正常前向（所有 expert 参与路由）
           loss.backward()      # 只有当前 expert 有梯度
           optimizer.step()

    d) (可选) Expert 内拓扑演化:
       if sparse_experts:
           current_expert.topology_update()

═══════════════════════════════════════════════════

Step 3: Expert Key 更新

  对更新过的 expert，用 EMA 微调其 key:
    expert.key = 0.99 * expert.key + 0.01 * mean(新数据的 hidden states)

═══════════════════════════════════════════════════

Step 4: (可选) 创建新 Expert

  如果 Smart Sampler 中有大量 primary_expert = None 的数据
  (路由时 max_sim < threshold):
    → 按 §3.3 的流程创建新 expert
    → 用这些数据做初始微调

═══════════════════════════════════════════════════

Step 5: 评估

  运行标准评估 (BPB, CORE metric)
  对比巩固前后指标，检测遗忘
```

### 6.2 为什么这比"睡眠巩固"更好？

| | 睡眠巩固（上一版） | Coreset 微调（本版） |
|---|---|---|
| 复杂度 | 4 个 phase，涉及海马体迁移判定 | 标准微调 + 冻结/解冻 |
| 新数据来源 | 海马体 KV slot（需要从 slot 反推原始数据） | 直接来自 Smart Sampler（原始文本） |
| Expert 定位 | 通过 affinity 统计间接推断 | 通过路由日志直接确定 |
| 可调试性 | 海马体状态难以人工检查 | coreset 是纯文本，完全可检查 |
| 实现难度 | 高（记忆迁移判定、slot 衰减等） | 低（标准微调 + 数据筛选） |

### 6.3 三重抗遗忘保护

1. **Expert 路由隔离**：更新物理 expert 时，化学 expert 完全冻结 → 化学知识零遗忘
2. **Key 匹配路由不可遗忘**：路由机制无可学习参数 → 路由映射永远稳定
3. **Coreset 中的旧数据混合**：微调时混合该 expert 的旧数据，维护 expert 内的旧知识

（如果启用 Expert 内稀疏化，则额外获得第四重保护：稀疏局部更新）

---

## 7. 完整生命周期

### 7.1 预训练

```
1. 初始化:
   - 每层 8 个 expert (可配置)
   - Expert key: 随机初始化，预训练中通过 EMA 更新
   - Expert 内部: dense FFN (MVP) 或 sparse FFN (优化)

2. 预训练 (标准流程):
   - 所有组件同时训练
   - Key Router 通过 EMA 自然分化 (不同 expert 特化到不同领域)
   - 固定 expert 数量，不触发新建

3. 输出: 预训练好的 HST checkpoint
```

### 7.2 持续学习

```
推理阶段:
  模型处理新数据 (对话/新文档)
  → Key Router 将 token 路由到匹配的 expert
  → Smart Sampler 记录 (text, routing_log)
  → 如果 max_sim < threshold → 标记为"无归属"

巩固阶段 (手动触发):
  → Step 1: 统计每个 expert 的新数据量
  → Step 2: 逐 expert coreset 微调 (冻结其他 expert)
  → Step 3: 更新 expert key (EMA)
  → Step 4: (可选) 创建新 expert
  → Step 5: 评估，检测遗忘

持续循环:
  推理 → 巩固 → 推理 → 巩固 → ...
  Expert 数量随知识增长
  旧 expert 的知识保持稳定
```

---

## 8. 与标准架构的对比

| 维度 | Dense Transformer | Standard MoE | HST |
|------|------------------|--------------|-----|
| 连接密度 | 100% | 100% (per expert) | 100% 或 ~5% (per expert) |
| 路由 | N/A | 可学习 router | Key 匹配 (不可遗忘) |
| Expert 数量 | N/A | 固定 | 动态增长 |
| 新知识编码 | 覆盖全局权重 | 覆盖 expert 权重 | 定向更新特定 expert |
| 持续学习 | 灾难性遗忘 | Router 遗忘 + Expert 内遗忘 | 三重抗遗忘保护 |
| 记忆系统 | 单一 | 单一 | 模型 (MoE) + 训练侧 (Smart Sampler) |
| 巩固 | 无 | 无 | Coreset 微调到对应 expert |
| 推理 FLOPs | O(d²) | O(k × d²/E) | O(k × d²/E) 或更低 |
| 推理额外开销 | N/A | N/A | 仅路由日志记录 (~0) |

---

## 9. 实现参考

### 9.1 Key-Based Router

```python
class KeyRouter(nn.Module):
    def __init__(self, dim, num_initial_experts, top_k=2, novelty_threshold=0.3):
        super().__init__()
        self.register_buffer('expert_keys', torch.randn(num_initial_experts, dim))
        self.top_k = top_k
        self.novelty_threshold = novelty_threshold
        self.key_momentum = 0.99

    def forward(self, x):
        x_norm = F.normalize(x, dim=-1)
        k_norm = F.normalize(self.expert_keys, dim=-1)
        sim = x_norm @ k_norm.T

        top_sim, top_idx = sim.topk(self.top_k, dim=-1)
        weights = F.softmax(top_sim, dim=-1)
        needs_new = (top_sim[..., 0] < self.novelty_threshold)

        return top_idx, weights, needs_new

    @torch.no_grad()
    def update_key_ema(self, expert_id, hidden_states):
        mean_h = F.normalize(hidden_states.mean(dim=0), dim=-1)
        self.expert_keys[expert_id] = (
            self.key_momentum * self.expert_keys[expert_id] +
            (1 - self.key_momentum) * mean_h
        )
```

### 9.2 Expert (Dense MVP / Sparse Optional)

```python
class Expert(nn.Module):
    def __init__(self, dim, hidden_dim):
        super().__init__()
        self.up = nn.Linear(dim, hidden_dim, bias=False)
        self.down = nn.Linear(hidden_dim, dim, bias=False)

    def forward(self, x):
        return self.down(F.relu(self.up(x)) ** 2)  # ReLU²
```

### 9.3 HST Block

```python
class HSTBlock(nn.Module):
    def __init__(self, dim, n_heads, num_experts, expert_hidden_dim):
        super().__init__()
        self.attn = Attention(dim, n_heads)
        self.router = KeyRouter(dim, num_experts)
        self.experts = nn.ModuleList([
            Expert(dim, expert_hidden_dim) for _ in range(num_experts)
        ])

    def forward(self, x):
        x = x + self.attn(x)

        expert_idx, expert_weights, needs_new = self.router(x)
        moe_out = self._moe_forward(x, expert_idx, expert_weights)
        x = x + moe_out

        return x, expert_idx  # 返回路由信息供 Smart Sampler 使用

    def _moe_forward(self, x, expert_idx, expert_weights):
        # 标准 MoE 分发: 按 expert_idx 分组 token, 送入对应 expert, 加权合并
        ...
```

### 9.4 Smart Sampler

```python
class SmartSampler:
    def __init__(self, buffer_dir: str):
        self.buffer_dir = Path(buffer_dir)
        self.buffer_dir.mkdir(parents=True, exist_ok=True)
        self.pending = []

    def record(self, text: str, expert_routing: dict[int, int]):
        """
        text: 原始文本
        expert_routing: {expert_id: token_count} 统计
        """
        self.pending.append({
            'text': text,
            'primary_expert': max(expert_routing, key=expert_routing.get),
            'routing': expert_routing,
            'timestamp': int(time.time()),
        })

    def flush(self):
        if not self.pending:
            return
        df = pd.DataFrame(self.pending)
        path = self.buffer_dir / f"buffer_{int(time.time())}.parquet"
        df.to_parquet(path)
        self.pending = []

    def build_coreset(self, expert_id, old_data_sampler, new_old_ratio=0.2):
        """构建特定 expert 的巩固训练集"""
        all_records = self._load_all_records()
        new_texts = [r['text'] for r in all_records
                     if r['primary_expert'] == expert_id]

        num_old = int(len(new_texts) * (1 - new_old_ratio) / new_old_ratio)
        old_texts = old_data_sampler.sample(expert_id, n=num_old)

        return new_texts, old_texts
```

### 9.5 Consolidation Script (概要)

```python
# scripts/consolidate.py

def consolidate(model, sampler, old_data_source, args):
    """按需 coreset 微调"""

    # Step 1: 确定需要更新的 expert
    expert_stats = sampler.get_per_expert_stats()
    experts_to_update = [eid for eid, count in expert_stats.items()
                         if count >= args.min_new_data]

    for expert_id in experts_to_update:
        # Step 2: 构建 coreset
        new_data, old_data = sampler.build_coreset(
            expert_id, old_data_source, args.new_old_ratio)

        # Step 3: 冻结其他 expert, 只训练当前 expert
        freeze_all(model)
        unfreeze_expert(model, expert_id)

        # Step 4: 标准微调
        loader = make_dataloader(new_data + old_data, ...)
        optimizer = make_optimizer(model.get_expert_params(expert_id), lr=args.lr)

        for step in range(args.num_steps):
            batch = next(loader)
            loss = model(batch).loss
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

        # Step 5: 更新 expert key
        model.update_expert_key_ema(expert_id, new_data)

    # Step 6: (可选) 创建新 expert
    unrouted = sampler.get_unrouted_data()
    if len(unrouted) >= args.new_expert_threshold:
        model.add_expert(unrouted)

    # Step 7: 评估
    evaluate(model)
```

---

## 10. 评估框架

### 10.1 遗忘检测

```
巩固后运行:
  1. 原始验证集 BPB → 检测全局遗忘
  2. 分 expert 数据的 BPB → 检测特定领域遗忘
  3. 标准基准 (CORE / few-shot) → 检测通用能力退化

Forgetting = (metric_after - metric_before) / metric_before
  < 2%:  无显著遗忘
  2-5%:  轻微遗忘
  > 5%:  需要调整参数
```

### 10.2 知识吸收

```
Absorption = BPB_new_before - BPB_new_after
在新数据 held-out 集上测量。
正值 = 成功学到新知识。
```

### 10.3 路由稳定性

```
巩固前后，在相同数据上运行推理:
  计算路由一致性 = 路由结果相同的 token 比例
  > 95%: 路由稳定
  < 90%: 路由漂移，需检查
```

---

## 11. 局限性与开放问题

1. **Expert 专化是否会自然发生？** 预训练时，仅通过 key EMA 更新，expert 是否会自然特化到不同领域？还是需要辅助损失（如负载均衡、diversity loss）来鼓励专化？

2. **Expert key 的稳定性**：EMA 更新导致 key 缓慢漂移。持续学习中长期累积后是否影响路由一致性？可能需要定期"冻结"key。

3. **新 Expert 创建的阈值**：`novelty_threshold` 如何设定？太低 → 新知识被塞进旧 expert；太高 → expert 数量爆炸。

4. **Expert 间知识共享**：完全隔离可能阻碍跨领域知识迁移（如物理+数学）。可能方案：共享 "foundation expert" 始终被激活 + 领域特定 expert top-k 选择。

5. **旧数据的 expert 归属索引**：Coreset 构建需要知道旧训练集中哪些数据路由到哪个 expert。需要预先建立索引，或在巩固时动态路由旧数据。

6. **Attention 层的持续学习**：本方案只隔离了 FFN (MoE)，但 Attention 的 QKV 投影仍是全局共享的。Attention 层是否也需要隔离？MoA (Mixture of Attention) 是一个可能方向。

7. **预训练成本**：MoE 架构的预训练比同等参数的 dense 模型需要更多工程优化（负载均衡、通信等）。

---

## 12. MVP 路线图

| Phase | 内容 | 验证目标 |
|-------|------|----------|
| 1 | 基础 MoE + Key Router (dense experts) | Key 路由可训练，expert 出现初步专化 |
| 2 | Smart Sampler | 推理时正确记录路由日志 |
| 3 | Coreset 微调 | 定向微调特定 expert，旧 expert 无遗忘 |
| 4 | 动态 Expert 增长 | 新领域数据触发新 expert 创建 |
| 5 | (可选) Expert 内稀疏化 | 稀疏 expert 性能接近 dense expert |
| 6 | 端到端验证 | 预训练→学新知识→巩固→无遗忘→重复 |
