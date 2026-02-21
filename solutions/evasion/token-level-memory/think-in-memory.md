# Think-in-Memory (TiM)

**论文：** Think-in-Memory
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Token-level Flat Memory — Inductive Thought Storage with Consolidation

---

## 问题

长对话场景中，记忆条目随时间大量积累，语义冗余严重，检索效率和质量下降。

## 方法

将对话内容抽象为归纳性"thoughts"，存储在hash table结构中。核心机制：
- **归纳性抽象** — 不直接存储原始对话，而是将对话提炼为高层归纳性thoughts
- **Hash table存储** — 利用哈希桶组织记忆条目，支持高效定位
- **桶内LLM审查** — 在同一哈希桶内，由LLM审查并合并语义冗余的条目，实现细粒度去重
- **Cluster-level fusion** — 进行聚类级别的记忆整合，跨条目融合相关信息
- **主动遗忘** — LLM评估记忆条目的重要性，主动丢弃低价值信息，控制记忆规模

## 特点

TiM将记忆的压缩与整合提升到结构化层面，不仅做语义摘要，还通过哈希分桶和聚类融合实现系统化的记忆管理，兼顾存储效率与信息保真。

## 任务

- Long-conversation QA
