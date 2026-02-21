# Synapse — Zheng et al. 2024

**论文：** Zheng et al. (2024)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Experiential Memory — Case-based (Solution) + Working Memory

---

## 问题

Web导航和计算机控制任务中，agent面对复杂的非结构化HTML DOM树，难以从原始状态中提取任务相关信息，且缺乏从过去经验中学习的能力。

## 方法

注入抽象的state-action episodes作为上下文示例（in-context examples），同时将原始状态重写为任务相关的摘要。核心设计：
- **State-Action Episode注入** — 将过去成功的交互经验抽象为state-action对，作为上下文示例提供给agent
- **DOM树重写** — 将非结构化的HTML DOM树重写为任务相关的状态摘要（task-relevant state summary），过滤无关元素
- **经验记忆与工作记忆结合** — 同时优化经验记忆（past episodes）和工作记忆（current state representation），实现双重增强

## 影响

Synapse展示了经验记忆与工作记忆协同工作的设计范式。其DOM树重写方法为Web agent的状态表示优化提供了有效方案，state-action episode的抽象为case-based经验记忆建立了实用模式。

## 任务

- Computer Control
- Web Navigation
