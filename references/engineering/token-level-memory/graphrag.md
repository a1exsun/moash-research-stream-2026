# GraphRAG (Edge et al. 2025)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Hierarchical (3D) — Pyramid
- **Task**: QA, Summarization

## Core Mechanism

GraphRAG 从源文档构建实体知识图谱，并通过社区检测算法递归聚合形成多层金字塔式索引，支持不同粒度的灵活检索。

- 从源文档构建实体知识图谱（entity knowledge graph），抽取实体及其关系作为图的节点和边
- 通过社区检测（community detection）递归聚合实体子图为社区摘要（community summaries），形成从具体实体到抽象主题的层次结构
- 多层图索引（multi-level graph index）支持不同粒度的灵活检索：底层提供精确的实体级信息，高层提供主题级的全局概览
- 金字塔（Pyramid）架构使得系统既能回答细粒度的事实性问题，也能处理需要全局理解的摘要性查询
- 该方法在 QA 和 Summarization 任务中展现了对传统 flat RAG 的显著优势
