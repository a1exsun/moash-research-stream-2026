# K-Adapter — Wang et al. 2021

**论文：** Wang et al. (2021) — K-Adapter
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Adapter

---

## 问题

向预训练模型注入新知识时，fine-tuning会破坏已有的预训练表示，导致灾难性遗忘。如何在不干扰原始模型的前提下持续扩展知识？

## 方法

K-Adapter通过训练任务特定的adapter模块来注入新知识，保持原始backbone完全不变。每个adapter模块专门学习一种类型的知识（如事实知识、语言知识等），独立于主模型进行训练和更新。

这种设计支持持续知识扩展：新类型的知识可以通过添加新的adapter来注入，而不干扰预训练表示或已有adapter中的知识。

## 核心机制

- **任务特定adapter**：每种知识类型对应一个独立的adapter模块
- **Backbone冻结**：原始预训练模型参数保持不变
- **持续扩展**：通过添加新adapter支持新知识的持续注入
- **知识隔离**：不同类型的知识存储在独立模块中，互不干扰

## 任务

- QA
- Entity Typing
- Classification
