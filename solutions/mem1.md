# MEM1 — Zhou et al. 2025

**论文：** Zhou et al. (2025)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Working Memory — Multi-turn — State Consolidation

---

## 问题

多轮对话中，agent需要在有限context window内维持跨轮次的连贯记忆，但简单拼接历史会导致context溢出，而固定规则的摘要又无法保留任务关键信息。

## 方法

维护共享内部状态（shared internal state），将新观察与先前记忆合并为统一的记忆表示。核心设计：
- **State Consolidation** — 每轮将新的观察信息与已有记忆状态进行合并，持续更新内部状态
- **RL优化的摘要策略（PPO）** — 使用Proximal Policy Optimization训练摘要策略，学习如何在压缩与保留之间取得最优平衡
- **协同记忆操作** — 学习多个记忆操作之间的协同配合，而非孤立地执行单一操作

## 影响

MEM1展示了用强化学习优化记忆摘要策略的可行性，证明了学习型记忆管理优于规则型方法。PPO优化的摘要策略为后续RL-based记忆系统提供了参考范式。

## 任务

- Retrieval
- Open-domain QA
- Shopping
