# Proposal 05: 面向持续学习的 Tiny-DSA 沙盒预训练验证

## 研究动机

如果"后天修改既有模型的注意力结构"（如 Proposal 03 讨论的方向）会面临预训练分布与新机制之间的不兼容问题，从而缺乏控制变量的说服力；那么，从零开始构建一个基于 DeepSeek 原生动态稀疏注意力（DSA: Dynamic Sparse Attention）架构的极小沙盒模型，可能是一条更干净的机制验证路径。

**为什么不能直接用现成的模型？** 截至 2026 年 2 月，具备原生条件性稀疏路由架构（MoE + Gated Delta Networks）的最小公开模型是刚发布的 **Qwen3.5-35B-A3B**（35B 总参数 / 3B 激活参数）。即便是这一"最小"规模，算力资源要求仍然很高（参考提议03中的评估）。而其他模型，比如deepseek-v3.2, Kimi-K2.5等，参数规模更大得多，无法推进相关研究。

### 一句话研究问题

在沙盒规模（~100M 参数量级别）的环境下，复刻并预训练一套自带"压缩流与聚焦流"的 DeepSeek DSA 核心算子网络，对比同等规模、同样数据分布下的标准 Dense 稠密网络，在经历多轮持续微调后，条件性稀疏路由架构是否能在部分设定下展现出更好的遗忘缓解表现？

## 假设

### H1：DSA 拓扑在极小尺度上同构有效（Isomorphism at Toy Scale）

这里假设 DeepSeek 的 DSA（Indexer + Top-K Selection）和 MoE 这类机制，尽管诞生于超大规模环境中，但缩减到 4~8 层、~100M 参数的规模后，在 TinyStories 这种干净的小规模数据集上仍能完成基本的自回归生成收敛。即，**双流通路在 toy 规模下可能仍保留部分功能**。这个假设本身也需要实验验证。

### H2：条件性稀疏路由有助于缓解持续微调中的遗忘（Sparse Routing Mitigates Forgetting）

同样的连续微调任务流注入到同样 100M 级的模型中：

- 原生 Dense 架构：在多轮微调后，因全局注意力和 MLP 权重的相互覆写，基础生成能力可能出现较明显退化（Catastrophic Forgetting）。
- Tiny-DSA（伴随非对称微调策略）：由于新注入知识的梯度流被限制在 **Selected Attention（聚焦流）和特定 Routings** 内，在相同微调强度下，旧任务的性能退化可能低于 Dense 对照组。

## 方案

### 极小原生沙盒架构组建（Tiny-DSA Architecture Build）

剥离冗余组件，借用 DeepSeek 开源代码中的核心算子：

- **模型骨干 (Backbone)**：4 - 8 个 Transformer Layer，隐藏维 `d_model = 512` 或 `768`（总参数极小）。
- **DSA 算子注入**：植入带有"Index 筛选与 Top-K 重启"的路由流模块并直接嵌入到 self-attention 层。明确切分宏观共享头（Shared Head / Compressed Flow）与特定匹配头（Selected / Routed Flow）。
- **对照组模型 (Dense Control Base)**：具备一模一样层级和神经元总数，但使用标准 `nn.MultiheadAttention`和标准全连接 FFN 层的传统架构。

### 预训练阶段 (Lightning Pre-training)

利用单张或双张消费级 GPU 完成基础语言能力收敛。

- **语料选取**：`roneneldan/TinyStories`（仅数百万级合成童话故事数据词元），或使用极简语法数据集。
- **收敛目标**：通过 24 - 48 小时的单卡训练，使得具有 DSA 拓扑结构的沙盒模型和 Dense Baseline 都在测试集上达到可用的基础生成质量（例如掌握"苹果是红色的"以及基本代词语法关系）。

### 多点连续破窗测试 (Continual "Window-Breaking" Test)

在两个模型同时具备了等位基础生成能力之后，引入"规则破坏级"的长程增量测试集（比如：人为设计 50 种设定矛盾的故事——"在世界 A 中水往高处流"，作为 Continuous Task Stream）。

- **对 Tiny-DSA 采取非对称微调 (ACFT)**：冻结 Shared / Compressed Layers，仅允许 Selected 层在这 50 种新故事上进行迭代微调。
- **对 Dense 模型**：采取同样强度、同样周期的 EWC 约束微调、甚至直接基于 Vanilla SGD。
- **遗忘曲线对账（Forgetting Charting）**：追踪两个架构的 Perplexity 与 Exact-Match Acc 衰退比，绘制遗忘曲线对比图，观察拓扑层面的路径隔离是否对遗忘缓解有可观贡献。

## 算力成本评估

- 预训练（~100M 模型 × TinyStories）：单卡 RTX 4090 约 24-48 小时 × 2 个模型
- 持续微调（50 个增量任务 × 多 epoch）：单卡约 1-2 天 × 2 个模型
- 总计：单卡 RTX 4090 约 1 周，或 A100 约 3-4 天
- 代码量可压缩在 500 行 PyTorch 以内，复现门槛相对较低

## 预期产出

1. **从网络拓扑视角切入遗忘问题**：为灾难性遗忘的研究提供一个互补视角——除了正则化方法（EWC 等）、梯度投影（GPM/OGD）和经验重放之外，探索网络连接结构本身对遗忘的影响。
2. **较高复现性**：沙盒代码可压缩在 500 行 PyTorch 以内，单卡消费级 GPU 有机会复现主要实验，便于后续研究者验证和扩展。
3. **低成本初步验证**：利用前沿架构（DSA）的核心设计思想在小规模上进行概念验证，为后续是否值得在更大规模上投入提供方向性依据。
