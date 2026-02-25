# Proposal 06: 基于 DeepSeek 原生动态稀疏注意力 (DSA) 的免遗忘持续微调系统

## 核心洞察 (Core Insight)

学术界在传统 Dense 架构（如 LLaMA / GPT-2）上修修补补设计持续学习系统，必然撞上“稳定性-可塑性”的容量天花板。然而，DeepSeek (尤其是引入原生动态稀疏注意力 DSA / Native Sparse Attention 机制后)，原本是为了解决超长文本（Long-Context）的算力与显存瓶颈。

但从第一性原理来看，这种将注意力强制切分为 **“压缩流（Compressed Attention）”** 和 **“聚焦流（Selected/Sparse Attention）”** 的架构，**在物理拓扑上完美地复刻了大脑“新皮层（慢速泛化） + 海马体（快速记忆）”的双基制系统**。
这意味着，新型的 Native Sparse 架构天然就是一台免疫灾难性遗忘的机器。我们**不需要向外乞求算力挂载庞大的记忆库，也不需要破坏底层架构去修改激活函数，只需要基于其多流结构设计一套非对称的持续微调（Continual FT）方案**，就能达成极高容量的持续学习。

## 一句话研究问题

在不使用任何传统 CL 补丁（如 EWC、庞大 Replay Buffer）的前提下，基于 DeepSeek DSA 架构执行非对称持续微调，能否在长程开放式用例（如 TRPG 陪伴）中彻底终结灾难性遗忘，并碾压所有基于 Dense 架构的最优持续学习策略？

## 研究假设 (Hypotheses)

### H1：空间隔离即时间隔离（干扰天然免疫）

在增量微调时，新知识产生的巨大突发梯度会自然流向并更新 **Selected Attention**（高稀疏子空间）的特定路由节点。而 **Compressed Attention**（全局常识空间）因为极少针对当前特定细颗粒任务被高频激活，天然避免了剧烈的梯度重叠（Gradient Overlap）和权重相互擦除。

### H2：非对称可塑性可解锁无限长微调（Asymmetric Plasticity）

如果对 DSA 的不同通路施加非对称的学习率策略：对 Selected 通路保留甚至放大局部可塑性（快速拟合新知识），对 Compressed 通路实施强正则或极端动量 EMA 冻结（维系世界常识）。系统可以无限期地吸收新特征，而基本不覆盖骨干规律。

### H3：天然对齐长程交互用例（TRPG 环境）

在长程 AI 陪伴场景下，极度个性化的细粒度特定属性（如五十次对话前赠送的、具有特殊附魔的剑）将能够仅被 Selected 稀疏路由“微观刻录”和精确召回；而宏观世界观（如魔法体系的基本语法和物理定律）则不受损地沉淀在 Compressed 节点中。

---

## 方法与实验设计

### 1. 非对称持续微调机制 (Asymmetric Continual Fine-Tuning - ACFT)

不修改 DeepSeek 算子，直接利用其预训练完成的拓扑结构，执行一种极度廉价的持续训练法则：

- **快速写入区（Fast Weight）**：释放 Selected Attention 相关的 Query/Key 路由矩阵、局部 Sliding Window 权重的学习率（或采用局部 LoRA 微调）。使其像海马体一样高频闪烁，专项吸收增量剧本中的新人物、新剧情、新法则。
- **慢速压舱石（Slow Weight）**：对 Compressed Attention（以及全局 Shared Expert MLP）施加极小的恒定学习率、强权衰减，或完全冻结。它们纯粹依赖 DeepSeek 预训练时注入的庞大通用常识兜底。
- _(可选) 离线睡眠梦境（Offline Dream）_：仅在长周期闲置下，利用轻量化生成的轨迹缓冲，将 Selected 层的频繁共现知识以极低学习率蒸馏（Consolidate）回 Compressed 层。

### 2. 对账验证体系 (Alignment Validation)

选用**「长程 AI 陪伴 / TRPG Human Feedback Arena」**（提案评测基准）进行长程注入验证。
**基线网络 (Baseline) 对比**：

- `Model-Dense-SOTA`：同等参数量的 LLaMA 系列架构 + 顶会最优的 Replay / Reg CL 法则。
- `Model-DSA-Naive`：直接对模型进行标准的增量全参数 Vanilla SGD 微调（测试是否原生防患遗忘）。
- `Model-DSA-ACFT`：应用本提议方法，冻结/阻抗压缩流，火力全开放行聚焦流的实验组。

验证核心指标不仅仅评估对话困惑度（Perplexity），而是聚焦在：**在跨度数千次连续微调迭代后，它是否依然没有遭受灾难性遗忘，并能在极低查询算力下答对极大概率会被 Dense 网络遗忘的超早期细粒度知识（Retrieval Accuracy in Infinite FT Streams）**。

---

## 预期贡献及顶会定位 (Expected Contributions)

1.  **范式转移（Paradigm Shift）**：首次提出「**为长文本内存压缩所设计的原生稀疏化注意力算子，是终结时间序列持续微调灾难性遗忘的究极解法**」。用结构化物理拓扑，降维打击当前领域为了抵抗遗忘而生造的各色损失函数。
2.  **工业界立即拿来可用的 SOTA 方案**：直接依托 DeepSeek 开源生态验证，这套非对称持续微调方案（ACFT）训练极快、无需任何非标准算子、零硬件阻抗，可以直接部署服务于真实世界的 AI 陪伴型初创公司。
3.  **完美闭环**：该实验提供了证实 **提案 05（基于双系统假说的压缩-可写性理论容量上限）** 取必然突破的最直接、最具震撼力的大模型验证论据。

---
