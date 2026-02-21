# Agent Workflow Memory (AWM) — Wang et al. 2024

**论文：** Wang et al. (2024)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Experiential Memory — Strategy-based (Workflow)

---

## 问题

Web交互任务中，Agent需要反复执行相似的操作序列，但每次都从零开始规划，既低效又容易出错。

## 方法

从成功的交互轨迹中提取可复用的工作流（workflows），作为高层脚手架指导后续任务生成。核心设计：
- **工作流提取** — 分析成功轨迹，识别并抽象出通用的操作流程模板
- **工作流复用** — 面对新任务时，检索相关workflow作为高层规划框架，在其指导下生成具体操作
- **无需权重更新** — 工作流存储为外部记忆，无需更新基座模型权重即可提升任务成功率

## 特点

AWM是Strategy-based Memory中Workflow类型的代表性工作。与Insight类型（如Reflexion）关注"做什么"不同，Workflow类型关注"怎么做"——以结构化的操作流程而非抽象洞见作为记忆载体，更适合程序化、步骤明确的交互任务。

## 任务

- Web Interaction
