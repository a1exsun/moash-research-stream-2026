# MemAgent — Yu et al. 2025

**论文：** Yu et al. (2025)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Working Memory — Multi-turn — State Consolidation

---

## 问题

长文档问答中，agent需要在固定预算的记忆空间内处理大量输入信息，简单截断会丢失关键内容，而保留全部信息又超出context限制。

## 方法

使用循环机制（recurrent mechanism）在固定预算记忆空间内更新记忆，主动丢弃冗余信息。核心设计：
- **固定预算记忆** — 维护固定大小的记忆缓冲区，确保记忆占用始终在预算范围内
- **循环更新机制** — 以循环方式不断将新信息整合到记忆中，同时淘汰冗余或过时内容
- **RL优化的摘要（GRPO）** — 使用Group Relative Policy Optimization训练摘要策略，学习在固定预算下最优地保留和丢弃信息

## 影响

MemAgent展示了在严格记忆预算约束下，通过RL优化实现高效记忆管理的方法。GRPO优化策略为固定预算场景下的记忆摘要提供了新的优化范式。

## 任务

- Long-term Document QA
