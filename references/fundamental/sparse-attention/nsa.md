# NSA — Native Sparse Attention — DeepSeek 2025

**Paper:** Jingyang Yuan, Huazuo Gao, Damai Dai, et al. (DeepSeek-AI)
**Title:** Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention
**Source:** ACL 2025 **Best Paper**; arXiv 2502.11089 (February 2025)
**Category:** Fundamental — Sparse Attention — Architecture Design
**Code:** https://github.com/deepseek-ai/Native-Sparse-Attention

---

## Problem

传统 sparse attention 方案（post-hoc pruning、learned gating）在推理时有效但训练时用 full attention，导致训练-推理 mismatch。如何设计一种**训练阶段就原生稀疏**的注意力机制？

## Method: 三分支层级稀疏策略

NSA 在每层注意力中同时使用三个互补分支：

1. **Compression Branch（粗粒度）**: 将 KV 序列按 block 压缩为 summary tokens，捕获全局上下文
2. **Selection Branch（细粒度）**: 基于 top-k 选择最相关的 KV blocks，保留局部精度
3. **Sliding Window Branch**: 固定的局部窗口，确保最近上下文始终可见

三个分支的输出通过 learned gating 加权融合。

## Hardware-Aligned 设计

- 算法设计与 GPU 的 memory hierarchy 对齐（SRAM/HBM 边界）
- Block-level 操作匹配 GPU tensor core 的最优粒度
- 通过 arithmetic intensity 平衡最大化硬件利用率

## Key Results

- 在 64k 序列上，decode / forward / backward 均大幅加速
- 预训练模型在 general benchmarks、long-context tasks、instruction-following 上匹配或超越 full attention
- **端到端原生训练**：训练和推理使用同一套稀疏模式，无 mismatch

## 对 Sparse Topology 研究的意义

NSA 证明了一个关键命题：**稀疏结构可以在训练中原生习得，而非仅在推理时剪枝**。这与你的 sparse topology 假说高度一致 — 结构性稀疏不是后处理工具，而是学习过程的一部分。

但 NSA 的稀疏是 **attention-level**（决定看哪些 token），你的研究关注 **weight-level** 的稀疏拓扑。两者可能互补：weight-level 稀疏决定"用哪些参数计算"，attention-level 稀疏决定"看哪些输入"。

## 后续工作

- → DSA (DeepSeek V3.2): 从 block-level 进化到 token-level 细粒度
- → ASA: 层间交替策略优化
- → FSA: kernel 实现优化
- → SSA: 解决 native sparse 训练的 sparsity 悖论
