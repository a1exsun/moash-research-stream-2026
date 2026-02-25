# MoBA — Mixture of Block Attention — Moonshot AI / Kimi

**Paper:** Lu, An, Han, et al. (Moonshot AI)
**Title:** MoBA: Mixture of Block Attention for Long-Context LLMs
**Source:** NeurIPS 2025 **Spotlight**; arXiv 2502.13189 (February 2025)
**Category:** Fundamental — Sparse Attention — MoE-Inspired
**Code:** https://github.com/MoonshotAI/MoBA

---

## Problem

NSA 的三分支设计引入了预定义的结构偏置（compression + selection + sliding window）。能否设计一种更简洁的 sparse attention，遵循 "less structure" 原则，让模型自主学习关注什么？

## Method: MoE 原理迁移到 Attention

MoBA 将 Mixture of Experts (MoE) 的路由思想应用到注意力机制上：

1. **Block 划分**: 将 KV 序列划分为固定大小的 block
2. **Router Network**: 对每个 query，用一个门控网络计算各 block 的相关性分数
3. **Top-k Block Selection**: 只将 query 路由到分数最高的 k 个 block
4. **Block 内 Full Attention**: 选中 block 内做标准注意力计算

## 核心设计哲学

- **Less structure**: 不预设 compression / selection / window 等结构，让 router 自主决定
- **Seamless switching**: 可以在 full attention 和 sparse attention 之间无缝切换
  - top-k = all blocks → full attention
  - top-k = few blocks → sparse attention
- **Training-inference consistency**: 训练和推理使用同一套路由机制

## Key Results

- 10M token 序列上最高 16x 加速
- 已部署在 Kimi 的长上下文服务中
- Routing 学到的 pattern 具有可解释性

## 与 NSA 的对比

| 维度 | NSA | MoBA |
|------|-----|------|
| 设计哲学 | 多分支显式结构 | 最小结构，router 自主决定 |
| 稀疏决策 | 三分支固定模式 | MoE-style 路由 |
| 灵活性 | 分支结构固定 | full ↔ sparse 无缝切换 |
| 粒度 | block-level | block-level |

## 对 Sparse Topology 研究的意义

MoBA 的 MoE-to-attention 迁移提供了一个重要范式：**用路由机制让网络自己决定稀疏连接模式**。

对 weight-level sparse topology 的启发：
- 能否用类似 MoE routing 的机制来决定哪些 weight connections 是活跃的？
- "Less structure" 原则是否适用于 sparse topology？即不预设固定的稀疏模式，而是让网络学习最优拓扑？
- MoBA 证明了 MoE routing 可以超越其原始应用（expert routing → attention routing），这种泛化是否可以继续延伸到 topology routing？
