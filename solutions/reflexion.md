# Reflexion — Shinn et al. 2023

**论文：** Shinn et al. (2023)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Experiential Memory — Strategy-based (Insight)

---

## 问题

Agent在执行任务时缺乏从过往交互经验中学习的机制，无法将失败教训转化为可复用的策略指导。

## 方法

最早且最具影响力的经验记忆方法之一。明确区分两类记忆：
- **短期记忆** — trajectory history，当前episode内的交互轨迹
- **长期记忆** — self-reflection model生成的feedback，跨episode持久化的自我反思结论

核心机制是通过自我反思（self-reflection）将交互经验转化为可复用的文本洞见（insights），这些洞见在后续任务中作为额外上下文注入prompt，指导Agent避免重复错误、改进策略。

## 影响

Reflexion开创了"反思即记忆"的范式，启发了大量后续反思类工作，包括ExpeL、Generative Agents中的reflection机制等。其将经验转化为自然语言洞见的思路，成为Strategy-based Experiential Memory的核心设计模式。

## 任务

- QA
- Reasoning
- Coding
