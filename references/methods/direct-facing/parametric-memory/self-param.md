# SELF-PARAM

**论文：** SELF-PARAM
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Post-Train

---

## 问题

如何在不引入额外参数的前提下，将外部知识注入到模型的参数化记忆中？

## 方法

SELF-PARAM通过KL divergence蒸馏的方式将额外知识注入模型，核心特点是不需要引入额外参数。通过自蒸馏（self-distillation）机制，模型在保持原有能力的同时吸收新知识，实现了轻量级的参数化记忆更新。

这种方法避免了adapter或额外模块带来的计算开销，直接在模型现有参数空间中完成知识注入。

## 核心机制

- **KL divergence蒸馏**：通过最小化分布差异将新知识注入模型
- **无额外参数**：不需要引入新的可训练参数
- **自蒸馏**：模型自身作为教师和学生，实现知识内化

## 任务

- QA
- Recommendation
