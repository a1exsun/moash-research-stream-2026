# MemLoRA — Bini et al. 2025

**论文：** Bini et al. (2025) — MemLoRA: Distilling Expert Adapters
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Adapter

---

## 问题

如何将多个专家adapter中的知识高效地压缩和整合，实现记忆增强的知识编辑？

## 方法

MemLoRA通过蒸馏专家adapter（Distilling Expert Adapters）实现记忆增强。核心思路是将多个专门训练的专家adapter中的知识通过蒸馏（distillation）压缩到统一的LoRA模块中，既保留了专家知识的精度，又降低了推理时的计算和存储开销。

## 核心机制

- **专家adapter蒸馏**：将多个专家adapter的知识蒸馏到统一模块
- **记忆增强**：通过蒸馏过程实现知识的压缩和整合
- **LoRA架构**：使用低秩adapter作为知识载体，参数高效
- **知识压缩**：将分散的专家知识统一到紧凑的参数空间

## 任务

- QA
