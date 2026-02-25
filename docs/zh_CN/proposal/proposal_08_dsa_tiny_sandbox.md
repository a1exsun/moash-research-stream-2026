# Proposal 08: 面向持续学习的 Tiny-DSA 沙盒预训练验证 (Tiny-DSA Sandbox Pre-training)

## 核心洞察 (Core Insight)

如果我们认为“后天修改（如 Proposal 07 提到的）既有模型的注意力结构”会面临预训练分布和新机制在微结构上的耦合阻抗（Impedance Mismatch），从而缺乏“原汁原味”的说服力；那么，从零开始（From-Scratch）构建一个基于 DeepSeek 原生动态稀疏注意力（DSA: Dynamic Sparse Attention）架构的极小沙盒模型（Toy Model / Sandbox），将是最纯粹的机制验证路径。

由于仅需证明“分离的注意力通路天然免疫遗忘现象”这一**网络拓扑的物理假说**，我们在顶会级别的理论论证中，可以脱离生产级的大参数模型，转而在极小尺度（~100M 参数）的语料集（如 TinyStories）上进行全链路、端到端（End-to-End）的首创验证。

## 一句话研究问题

在沙盒规模（~100M 参数量级别）的环境下，完全复刻并预训练一套自带“压缩流与聚焦流”的 DeepSeek DSA 核心算子网络，对比同等规模、同样数据分布下的标准 Dense 稠密网络，在遭受百次量级的持续微调轰炸后，谁能彻底终结灾难性遗忘的发生？

## 研究假设 (Hypotheses)

### H1：DSA 拓扑在极小尺度上同构有效（Isomorphism at Toy Scale）

我们假设 DeepSeek 的 DSA（Indexer + Top-K Selection）和 MoE，这种针对长文本优化的机制，尽管诞生于超大规模语料和百亿级别的底座模型中，但当将其缩减到 4~8 层、几百万到上亿个参数的规模后，基于 TinyStories 这种极其干净的“婴幼儿级别”短小故事数据集上依旧能完成流畅的自回归生成收敛。即，**双流通路不会因为模型变小而丧失提取常识的能力**。

### H2：基于第一性原理的极简对比将彻底胜出（First Principles Sweep）

同样的连续微调任务流注入到同样 100M 级的模型中：

- 原生 Dense 架构：在几十个 epochs 后，因为全局注意力和 MLP 权重的严重涂抹，原本能讲出“狼与兔子做朋友”常识的能力完全丧失（Catastrophic Forgetting）。
- Tiny-DSA（伴随非对称微调策略）：即使仅凭单卡 4090 的算力，因为新注入知识的梯度流精准走专门预留的**Selected Attention (聚焦流) 和特定 Routings**，无论微调多久跨度，它都能在生成带有最新设定的对话时保留极佳的故事连贯性。

## 方法与实验设计

### 1. 极小原生沙盒架构组建（Tiny-DSA Architecture Build）

剥离冗杂的非关注组件，仅借用 DeepSeek 开源代码中具有核心创新力的算子段：

- **模型骨干 (Backbone)**：4 - 8 个 Transformer Layer，隐藏维 `d_model = 512` 或 `768`（总参数极小）。
- **DSA 算子注入**：植入带有“Index 筛选与 Top-K 重启”的路由流模块并直接嵌入到 self-attention 层。明确切分宏观共享头（Shared Head / Compressed Flow）与特定匹配头（Selected / Routed Flow）。
- **对照组模型 (Dense Control Base)**：具备一模一样层级和神经元总数，但使用标准 `nn.MultiheadAttention`和标准全连接 FFN 层的传统架构。

### 2. 毫秒级预训练阶段 (Lightning Pre-training)

利用单张或双张消费级 GPU 完成全量常识内化。

- **语料选取**：`roneneldan/TinyStories`（仅数百万级合成童话故事数据词元），或使用极简语法数据集。
- **收敛目标**：通过 24 - 48 小时的单卡训练，使得具有 DSA 拓扑结构的沙盒模型和 Dense Baseline 都在测试集上能够生成流畅并且合逻辑的低龄短篇故事（例如掌握“苹果是红色的”以及基本代词语法关系）。

### 3. 多点连续破窗测试 (Continual "Window-Breaking" Test)

在两个模型同时具备了等位基础生成能力之后，引入“规则破坏级”的长程增量测试集（比如：人为设计 50 种设定矛盾的故事——“在世界 A 中水往高处流”，作为 Continuous Task Stream）。

- **对 Tiny-DSA 采取非对称微调 (ACFT)**：冻结 Shared / Compressed Layers。放任 Selected 层跟随这 50 种奇异新故事疯狂迭代拟合。
- **对 Dense 模型**：采取同样强度、同样周期的 EWC 约束微调、甚至直接基于 Vanilla SGD。
- **遗忘曲线对账（Forgetting Charting）**：追踪这两个底层微观结构的 Perplexity 与 Exact-Match Acc 衰退比，在持续数天的实验流程中勾勒出“遗忘发散图”，证明拓扑硬件物理隔离是最致命的“抗遗忘外挂”。

## 预期贡献及顶会定位

1.  **极度纯粹的学术贡献**：将“解决灾难性遗忘”的理论视阈拉扯回**最原初的网络结构图论**，摒弃近年来过度内卷的各种算力惩罚、梯度投影算法与外部记忆回溯黑盒（Replay Buffer）。
2.  **极简验证复现性**：这套 Tiny-DSA 沙盒代码总额可以压缩在 500 行 PyTorch 文件以内（纯白盒）。所有后继研究人员甚至只需一块便宜的矿卡半天内便能复现结果。
3.  **大厂算力溢出效应向下兼容（Democratization）**：让最穷的学术实验室，能够凭借前沿公司的超级架构思想，打败依然基于 Dense 底层用巨型算力训出的百亿参数闭源持续学习系统。
