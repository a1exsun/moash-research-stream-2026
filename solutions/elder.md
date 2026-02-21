# ELDER — 2025, AAAI

**论文：** ELDER (2025, AAAI)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Adapter

---

## 问题

在长期编辑场景中，单一adapter难以承载大量编辑且容易产生知识冲突，如何提升长期编辑的鲁棒性和可扩展性？

## 方法

ELDER维护多个LoRA模块，每个模块存储不同的编辑知识。关键创新在于学习一个路由函数（routing function），能够基于输入语义自适应地选择或混合相关的LoRA模块。

这种多LoRA + 路由的架构设计，类似于MoE（Mixture of Experts）的思路应用于知识编辑场景，通过分散存储和智能路由提升了长期编辑场景下的鲁棒性和可扩展性。

## 核心机制

- **多LoRA模块**：维护多个独立的LoRA模块存储不同编辑知识
- **语义路由**：基于输入语义自适应选择或混合相关LoRA
- **长期编辑鲁棒性**：通过分布式存储缓解单模块的容量瓶颈
- **可扩展架构**：可通过增加LoRA模块扩展编辑容量

## 任务

- Model Editing
