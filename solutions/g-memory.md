# G-Memory (Zhang et al. 2025)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Hierarchical (3D) — Pyramid
- **Task**: QA, Game, Embodied Task

## Core Mechanism

G-Memory 采用查询中心的三层图结构，支持多智能体共享经验，并通过垂直遍历实现跨层次的知识整合。

### 三层图结构

- **Interaction graph**：记录具体的智能体交互轨迹和协作细节
- **Query graph**：组织与特定查询相关的经验片段
- **Insight graph**：从多次试验中提炼出的高层跨试验洞见（cross-trial insights）

### 关键特性

- 多智能体共享经验（multi-agent experience sharing），不同智能体的经验可以汇聚到共同的记忆图中
- 支持垂直遍历（vertical traversal）：从高层跨试验洞见向下追溯到具体协作轨迹，或从底层经验向上归纳出通用策略
- LLM 根据 agent 角色定制精简经验（role-customized experience distillation），不同角色的智能体从共享记忆中提取与自身职责最相关的信息
- 金字塔（Pyramid）架构实现了从具体经验到抽象洞见的层次化组织，适用于需要多智能体协作的复杂任务
