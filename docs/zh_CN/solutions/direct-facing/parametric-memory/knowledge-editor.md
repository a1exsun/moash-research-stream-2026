# KnowledgeEditor

**论文：** KnowledgeEditor
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Post-Train

---

## 问题

如何在修改模型内部参数时，精准地只改变需要编辑的知识，而不影响其他已学习的知识？

## 方法

KnowledgeEditor通过修改模型内部参数来实现知识编辑，其设计目标是将编辑影响严格限制在需要修改的知识范围内。与直接fine-tuning不同，KnowledgeEditor学习生成精确的参数更新，确保编辑的局部性和可控性。

## 核心机制

- **内部参数修改**：直接修改模型权重以更新特定知识
- **编辑局部性**：目标只改变需要编辑的知识，保持其他知识不变
- **可控编辑**：学习精确的参数更新策略

## 任务

- QA
- Fact Checking
