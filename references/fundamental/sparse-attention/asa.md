# ASA — Alternating Sparse Attention — 2025

**Paper:** (2025)
**Title:** Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies
**Source:** arXiv 2511.00819 (November 2025)
**Category:** Fundamental — Sparse Attention — Architectural Refinement

---

## Problem

NSA 在每一层都使用固定的三分支结构（compression + selection + sliding window），是否所有层都需要同样的注意力模式？

## Method: 层间交替 + MLA 集成

### 1. Local-Global Alternating Strategy

将注意力层分为两类，严格交替：

- **Local layers（奇数层）**: 仅使用 sliding window attention，建模局部上下文
- **Global layers（偶数层）**: 使用 compression + selective attention，捕获长程依赖

关键发现：**交替使用比每层都用固定三分支效果更好**。原因可能是：
- 不同层的功能自然分化（局部特征提取 vs 全局信息聚合）
- 减少冗余计算
- 类似 Transformer 中早期层关注局部、后期层关注全局的自然模式

### 2. MLA 替换 GQA

- Sliding window branch 使用 Multi-head Latent Attention (MLA)
- Compression/selective branches 使用 Group-head Latent Attention (GLA)
- **KV-cache 内存降低 50%**，性能不降反升

## Key Results

- 匹配或超越 full attention baseline
- 优于 NSA 的固定三分支结构
- KV-cache 内存减半

## 对 Sparse Topology 研究的意义

ASA 的交替策略触及了一个深层问题：**不同层应该有不同的稀疏模式**。

对 weight-level sparse topology 的直接启发：
- **Layer-wise topology differentiation**: 不同层的最优稀疏拓扑可能不同，早期层可能需要更密集的局部连接，后期层需要更稀疏但更长程的连接
- **Alternating patterns**: 在 continual learning 中，交替使用不同类型的稀疏模式（如固定 vs 可塑层）可能比统一策略更有效
- **MLA 作为 KV compression**: MLA 本质上是一种隐式的稀疏化 — 将 KV 投射到低秩空间，这与 weight matrix 的 low-rank sparsity 有概念上的联系
