# FlashMoBA — Optimizing Mixture of Block Attention — MIT Han Lab

**Paper:** (MIT Han Lab, 2025)
**Title:** Optimizing Mixture of Block Attention
**Source:** arXiv 2511.11571 (November 2025)
**Category:** Fundamental — Sparse Attention — Theoretical Analysis + System Optimization
**Code:** https://github.com/mit-han-lab/flash-moba

---

## Problem

MoBA 的理论最优配置（小 block size）在 GPU 上计算不高效。如何在理论最优性和硬件效率之间架桥？

## Contribution 1: 信噪比（SNR）理论分析

首次对 MoBA 的路由准确率做严格理论推导：

### SNR 公式
- 推导出影响 routing 准确率的**信噪比公式**
- SNR 取决于：block size、key 的统计分布、query-key 亲和力
- **关键发现**：
  1. **更小的 block size → 更高的 SNR → 更准确的路由**（因为 block 内的 key 更同质）
  2. **对 key 施加短卷积 → 增强局部信号聚类 → 提升路由精度**

### 理论指导实践
- 小 block 理论上最优，但 GPU 上因为 memory access 和 parallelism 问题效率低
- 需要专门的 kernel 来弥合理论-实践的鸿沟

## Contribution 2: FlashMoBA Kernel

- 硬件感知的 CUDA kernel 实现
- 使小 block 配置在 GPU 上变得实用
- 比 FlashAttention-2 最高 **14.7x 加速**
- 改进后的 MoBA 从头训练即可匹配 dense attention baseline

## 对 Sparse Topology 研究的意义

这篇论文的方法论对 sparse topology 极其相关：

1. **SNR 理论框架**：为"稀疏粒度的选择"提供了严格的分析工具。类比到 weight-level sparsity：unstructured sparsity（单个权重）vs structured sparsity（整个 channel/head）的选择也应该有类似的 SNR 分析
2. **理论最优 vs 硬件可行**的张力在 sparse topology 中同样存在：fine-grained unstructured sparsity 理论上最优，但 hardware 更偏好 structured sparsity
3. **系统协同设计**：算法和 kernel 必须一起优化，这是 sparse topology 部署的核心挑战
