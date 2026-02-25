# DSA — DeepSeek Sparse Attention — DeepSeek V3.2

**Paper:** DeepSeek-AI (2025)
**Title:** DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
**Source:** arXiv 2512.02556 (December 2025)
**Category:** Fundamental — Sparse Attention — Production-Scale
**Code:** https://github.com/deepseek-ai/DeepSeek-V3.2-Exp

---

## Problem

NSA 的 selection branch 在 **block 级别**操作，粒度不够细。如何实现 **token 级别**的细粒度稀疏选择，同时保持可部署性？

## Method: Lightning Indexer + Token-Level Selection

DSA 由两个核心组件构成：

### 1. Lightning Indexer（轻量级索引器）
- 一个极小的评分网络，为所有历史 token 相对于当前 query token 计算相关性分数
- 计算开销极低，实现近线性复杂度

### 2. Fine-Grained Token Selection
- 基于 indexer 分数选择 top-k 个最相关 token（如从 128k context 中选 2048 个）
- **token 级别**粒度，而非 NSA 的 block 级别
- 选中的 token 送入 MLA（Multi-head Latent Attention）做完整计算

## Key Results

- 将注意力从 O(n²) 实际降为 ~O(n)
- 685B 参数生产模型中部署
- 输出质量与 full attention 几乎无差异
- DeepSeek-V3.2 性能与 GPT-5 相当

## NSA → DSA 演进

| 维度 | NSA | DSA |
|------|-----|-----|
| 选择粒度 | block-level | **token-level** |
| 索引机制 | top-k block scoring | lightning indexer |
| 分支结构 | 三分支（compress/select/window）| indexer + token selector |
| 部署规模 | 研究验证 | **685B 生产模型** |

## 对 Sparse Topology 研究的意义

DSA 的 lightning indexer 本质上是一个**学习到的稀疏连接决策器** — 给定 query，动态决定与哪些 KV 建立"连接"。这与 dynamic sparse topology 高度类似：
- DSA：动态决定 attention 连接（哪些 token 对之间有连接）
- Dynamic sparse networks：动态决定 weight 连接（哪些参数是活跃的）
- 两者都用 learned criteria 做 top-k selection

DSA 证明了 **token-level fine-grained sparsity 在超大规模下是可行的**。
