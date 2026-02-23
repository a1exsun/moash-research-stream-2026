# Context Folding (2025)

**论文：** (2025)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Working Memory — Multi-turn — Hierarchical Folding

---

## 问题

层次化记忆折叠中，何时将轨迹分支为子轨迹、如何将子轨迹抽象为高层状态，这些决策依赖人工启发式规则，难以泛化到多样化任务场景。

## 方法

将折叠操作变为可学习的策略（learnable policy），用强化学习训练agent自主做出折叠决策。核心设计：
- **可学习的折叠策略** — 不再依赖固定规则，而是训练agent学习何时触发分支（branching）与折叠（folding）
- **自主分支决策** — agent自主决定何时将当前轨迹分支为子轨迹
- **自主抽象决策** — agent自主决定如何将子轨迹抽象为高层状态表示
- **RL优化** — 使用强化学习优化折叠策略，以下游任务表现为奖励信号

## 影响

Context Folding将HiAgent等工作中的启发式折叠规则提升为可学习的策略，代表了从"规则驱动"到"学习驱动"的记忆管理范式转变。

## 任务

- Deep Research
- SWE (Software Engineering)
