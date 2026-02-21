# HiAgent — Hu et al. 2025

**论文：** Hu et al. (2025)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Working Memory — Multi-turn — Hierarchical Folding

---

## 问题

长期任务中agent的执行轨迹不断增长，导致context window溢出。平坦的轨迹记录缺乏层次结构，难以在保留全局规划信息的同时聚焦当前子任务。

## 方法

构建子目标中心的层次化工作记忆（subgoal-centric hierarchical working memory）。核心设计：
- **子目标分层管理** — 仅保留当前活跃子目标（active subgoal）的详细执行轨迹在工作记忆中
- **轨迹折叠（Trajectory Folding）** — 已完成的子目标自动折叠为简洁摘要，大幅压缩历史信息
- **按需检索** — 折叠后的子目标摘要仍可按需展开检索，在需要时恢复完整细节

## 影响

HiAgent将层次化规划与记忆管理结合，证明了"折叠-展开"机制在长期任务中的有效性。这种层次化折叠范式启发了Context Folding等后续工作将折叠操作变为可学习策略。

## 任务

- Long-horizon Agent Task
