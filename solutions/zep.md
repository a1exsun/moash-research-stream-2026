# Zep (Rasmussen et al. 2025)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Hierarchical (3D)
- **Task**: Long-conv QA, Document Analysis
- **Note**: 开源框架

## Core Mechanism

Zep 将 Agent 记忆形式化为时序知识图谱（Temporal Knowledge Graph），采用三层图架构，通过时序注释实现记忆的优雅演化。

### 三层图架构

- **Episodic subgraph (G_e)**：双时间模型（bi-temporal model），分别记录消息的发生时间（event time）和处理时间（processing time），精确追踪事件的时序关系
- **Semantic subgraph (G_s)**：存储实体（entities）和有时间约束的事实（time-bounded facts），表示从对话中提取的结构化知识
- **Community subgraph (G_c)**：高层聚类（high-level clustering）和实体摘要（entity summaries），提供全局视角的知识概览

### 关键特性

- 时序注释（temporal annotations）实现 soft deletion 而非破坏性替换（destructive replacement），旧事实不会被直接删除，而是通过时间标记标注其有效期
- 这种设计使系统能够回答"某一时刻的事实是什么"这类时序敏感的问题
- 作为开源框架，Zep 为 Agent 记忆的工程实践提供了可复用的基础设施
