# HAT (Hierarchical Aggregate Tree)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Planar (2D) — Tree
- **Task**: Long-conv QA

## Core Mechanism

HAT 对长交互进行分段并逐步聚合，构建层次化聚合树（Hierarchical Aggregate Tree）。该方法的核心思想是将冗长的对话或文档按段落切分后，自底向上地进行摘要聚合，形成一棵树状结构。

- 对长交互进行分段并逐步聚合，构建层次化聚合树
- 支持从粗到细的检索（coarse-to-fine retrieval）：查询时先匹配树的高层节点确定相关区域，再逐层深入到具体段落，实现高效的多粒度检索
- 在长上下文 QA 任务上优于平面向量索引（flat vector index），因为层次化结构能更好地捕捉文档的全局语义组织
