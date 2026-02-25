# FSA — Flash Sparse Attention — 2025

**Paper:** Yang et al. (Relaxed System Lab, 2025)
**Title:** FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel
**Source:** arXiv 2508.18224 (August 2025)
**Category:** Fundamental — Sparse Attention — System Optimization
**Code:** https://github.com/Relaxed-System-Lab/Flash-Sparse-Attention

---

## Problem

NSA kernel 的循环顺序设计限制了其适用性：

- NSA 的 kernel 外层循环遍历 query head groups，内层遍历 KV blocks
- 这种顺序只在 GQA 组内 **query head 数量较多** 时高效（需要足够的并行度）
- 但许多主流 LLM（如 Llama 系列）的 GQA 配置中每组 query head 数较少
- 结果：NSA 的 kernel 在这些模型上效率严重受限

## Method: 反转循环顺序

FSA 的核心创新极其简洁 — **反转两层循环**：

- **NSA**: outer loop = query heads → inner loop = KV blocks
- **FSA**: outer loop = **KV blocks** → inner loop = **query tokens**

### 为什么有效？

- 对于一个给定的 KV block，attend to 它的 query token 数量通常远大于硬件要求的最小并行度
- 因此外层遍历 KV blocks 不会遇到并行度不足的问题
- 不引入 padding，减少无效内存访问和 FLOPs

## Key Results

- Kernel 级延迟降低最高 **3.5x**（平均 1.6x）
- 端到端训练加速最高 1.25x
- Prefill 推理加速最高 1.36x
- 适用于各种 GQA 配置的主流 LLM

## 对 Sparse Topology 研究的意义

FSA 是一个纯 systems 优化的工作，但它揭示了一个对 sparse topology 同样重要的问题：

- **循环顺序 = 数据访问模式 = 性能瓶颈**：sparse topology 的实际部署也面临类似挑战 — 稀疏连接的不规则访问模式导致 GPU 利用率低
- **Hardware alignment 是 sparsity 落地的必要条件**：即使算法上最优的 sparse topology，如果不能高效实现也毫无意义
- **启示**：sparse topology 研究不能只关注"哪些连接应该存在"，还必须考虑"这种连接模式能否在硬件上高效执行"
