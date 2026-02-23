# MemTree (Rezazadeh et al. 2025)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Planar (2D) — Tree
- **Task**: Long-conv QA, Document Reasoning

## Core Mechanism

MemTree 是一种动态层次化表示方法，能够从孤立的对话日志中自动推断出层次化 schema，并随着新信息的加入持续演化。

- 动态层次化表示，从孤立对话日志推断层次 schema（hierarchical schema）
- 新文本片段到来时，检索最相似节点并作为子节点插入树中
- 自底向上触发所有父节点的摘要更新（bottom-up summary propagation），确保树的每一层都反映最新信息
- 逐步将具体事件总结为更高层概念，实现从细粒度事实到抽象主题的自然过渡
- 通过动态增长的树结构，避免了固定 schema 的僵化，同时保持了信息的可组织性和可检索性
