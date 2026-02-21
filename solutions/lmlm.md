# LMLM — Zhao et al. 2025

**论文：** Zhao et al. (2025) — Limited Memory Language Model
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Pre-Train

---

## 问题

传统LLM将事实知识与模型权重紧密耦合，导致知识更新需要重训模型，且无法追溯知识来源。

## 方法

LMLM（Limited Memory Language Model）在预训练阶段就将知识检索的记忆存储在模型中，但知识本身存储在外部知识库中。这一设计显式地将事实知识与模型权重解耦：模型学习的是"如何检索和使用知识"的能力，而非知识本身。

通过这种架构，LMLM支持直接的知识编辑和来源验证，无需重新训练模型。当外部知识库更新时，模型的行为自动反映最新知识。

## 核心机制

- **知识-权重解耦**：模型参数存储检索能力，事实知识存储在外部
- **预训练阶段集成**：在预训练时就设计知识检索机制，而非后训补丁
- **无需重训的知识编辑**：通过更新外部知识库直接修改模型输出
- **来源验证**：知识来源可追溯，支持事实核查

## 任务

- QA
- Factual Generation
