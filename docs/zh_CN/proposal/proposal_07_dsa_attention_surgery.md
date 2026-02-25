# Proposal 07: 基于开源小模型的非对称注意力拓扑手术 (Asymmetric Attention Topology Surgery)

## 核心洞察 (Core Insight)

为了验证“物理隔离的稀疏注意力通道（压缩流与聚焦流）配合非对称微调能够终结灾难性遗忘”的前沿假说（参考 Proposal 06），我们无需被动等待开源界发布微缩版的原生 DSA 模型，也不必承担动辄百亿参数级别的训练成本。

从第一性原理来看，只需将**现有的成熟稠密模型（Dense Model）在注意力计算拓扑上做“外科手术式”的阻断改写**，人为切分出代表宏观常识的「强压舱石（压缩流）」与负责动态局部特征拾取的「高频更新区（聚焦流）」，就能以极低成本逼近原生 DSA 架构的动态隔离效果。

## 一句话研究问题

在消费级算力约束下，通过对基础小模型（如 Qwen2.5-1.5B）执行人为的“注意力切割与非对称冻结”，能否在长程序列数据（如 TRPG 设定）的持续微调中，展现出显著优于传统全参数微调（Vanilla FT）和微调缓解算法（如 EWC/Replay）的抗遗忘特性？

## 研究假设 (Hypotheses)

### H1：人为注意力分离（Attention Splitting）可实现等效隔离

强制将基础模型的 Attention Heads 进行 1:1 分割：一半 Heads 被限制只作为通用的、冻结的表征抽取器；另一半 Heads 被迫加上强制的 Top-K 稀疏遮罩（Mask）。这种后天的结构重塑能够有效阻断增量数据更新引发的交叉梯度污染。

### H2：基于后天魔改（Pseudo-DSA）即可复现非对称微调优势

对于拥有高质量预训练常识的底座模型，即便“压缩流”被彻底冻结（显存和算力开销大幅下降），只要对“稀疏流”释放自由的、高频率的局部可塑性，模型依然可以极速记忆新领域知识，且完美保留预训练分布。

## 方法与实验设计

### 1. 网络手术流程 (Topology Surgery Protocol)

使用极其轻量化的干预代码，在主流的基础设施上（例如 Huggingface Transformers 中文或 LLaMA-Factory 库）直接修改模型 `forward` 逻辑：

- **基座选择**：Qwen2.5-1.5B 或 Llama-3.2-1B（参数量合适且推理能力出色的小基座）。
- **注意力通道一分为二 (Head Splitting)**：单层 Transformer 的 $N$ 个 Heads 中：
  - **Group A (压缩流)**：保留原始的全稠密计算（Dense Query-Key interaction）。在微调时，**全局锁定**其 Query / Key / Value / Output 矩阵参数以及对应的 MLP 模块（设置 `requires_grad=False`）。
  - **Group B (聚焦流)**：强行介入 `Attention Score = Q * K^T`。对其注意力分数矩阵增加 **Top-K Sparse Mask** 处理（例如只保留 Top 5%-10% 的高相关性 token 权重，其余置 `-inf`）。在微调中，只针对这部分 Heads 释放学习率或施加低秩适配（LoRA）。

### 2. 对账验证体系与沙盒对比

选用 **「连续式微型知识注入环境（如多轮 TRPG 规则设定注入环境）」**。

实验设置对比组：

1.  **Baseline 1 (Dense Vanilla FT)**：原生 Qwen2.5-1.5B，不切割注意力，标准全参数或普通 LoRA 微调。
2.  **Baseline 2 (Dense CL-SOTA)**：使用目前最先进的 Replay / EWC 持续学习正则对原生 Dense Qwen2.5-1.5B 训练。
3.  **实验组 (Surgically-Adapted DSA)**：应用我们的注意力拓扑手术，仅微调 Group B（聚焦流）和最终 Classifier 层的实验组。

### 3. SOTA 考核指标 (Metrics)

监控模型在连续 50-100 次不同领域/设定的微调迭代后：

- **旧知识存留率（Retention Score）**：针对最早期（如第一次迭代）注入极细微长尾设定的提问召回率。
- **训练成本折算（TFLOPS & Memory Offset）**：因为砍掉了 Group A（占模型总参数 80% 左右的特征权重）的计算梯度图，记录该干预带来的极低显存/算力消耗。

## 预期贡献

1.  **极高性价比的机制证明**：将验证 Native DSA 防止遗忘的实验成本砍掉两个数量级（使得单人单 4090 卡实验室即可完成原本需要百亿参数级集群才能验证的机制论据）。
2.  **即插即用的代码库**：不仅证明假说，还向社区开源这套基于 PyTorch 前向挂钩（Hook）和算子重载的 `Topology-Continual-Learning` 包，可以使得所有的现有小大模型通过微调变相获得一定的内存物理隔离能力。
