# MAC — Amortize Context

**论文：** MAC (Amortize Context)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Auxiliary LM

---

## 问题

如何将大量文档信息高效地编码为可复用的紧凑表示，避免每次推理都需要处理完整的上下文？

## 方法

MAC通过amortization network将新文档的信息压缩为紧凑的modulation（调制参数），并存储在memory bank中。在推理时，模型通过检索相关的modulation来调整自身行为，而无需重新处理原始文档。

这种方法将上下文处理的计算成本分摊（amortize）到离线编码阶段，使得推理时只需加载紧凑的调制参数，大幅提升效率。

## 核心机制

- **Amortization network**：将文档信息压缩为紧凑的modulation表示
- **Memory bank**：存储所有编码后的modulation，支持高效检索
- **上下文压缩**：将长文档压缩为参数化的紧凑表示
- **推理加速**：推理时加载modulation而非处理完整文档

## 任务

- QA
