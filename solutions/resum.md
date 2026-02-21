# ReSum — Wu et al. 2025

**论文：** Wu et al. (2025)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Working Memory — Multi-turn — State Consolidation

---

## 问题

长期Web搜索等开放式探索任务中，agent的交互历史持续增长，需要在不丧失关键推理状态的前提下支持无限期的探索。

## 方法

周期性将历史蒸馏为推理状态（reasoning state），利用RL优化摘要条件下的行为表现。核心设计：
- **周期性历史蒸馏** — 定期将累积的交互历史压缩蒸馏为精炼的推理状态表示
- **推理状态维护** — 蒸馏后的推理状态作为agent的工作记忆，驱动后续决策
- **RL优化摘要行为** — 以下游任务表现为奖励信号，优化摘要策略使其生成的推理状态最有利于后续行为
- **无限期探索支持** — 通过周期性蒸馏，打破context window对探索时长的限制，支持无限期的搜索与推理

## 影响

ReSum证明了周期性状态蒸馏结合RL优化可以有效支持无限期探索任务，为开放式agent任务的记忆管理提供了可扩展的解决方案。

## 任务

- Long-horizon Web Search
