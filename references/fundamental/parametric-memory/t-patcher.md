# T-Patcher — Huang et al. 2023

**论文：** Huang et al. (2023) — Transformer Patcher
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Adapter

---

## 问题

如何高效地修补Transformer模型中的错误预测，而不影响模型在其他输入上的正常行为？

## 方法

T-Patcher（Transformer Patcher）通过识别"值得修补的神经元"（patch-worthy neurons）来实现知识编辑。对于每个需要修正的错误，T-Patcher定位相关的神经元并添加小规模的补丁（patch）模块，精准修正模型行为。

这种方法将知识编辑转化为神经元级别的修补问题，通过外部补丁模块实现精确的行为修正。

## 核心机制

- **神经元定位**：识别与错误预测相关的"值得修补的神经元"
- **外部补丁模块**：为目标神经元添加小规模的修补参数
- **精准修正**：仅修改与错误相关的行为，不影响其他输入
- **增量式编辑**：每次编辑添加新补丁，不修改原始参数

## 任务

- QA
