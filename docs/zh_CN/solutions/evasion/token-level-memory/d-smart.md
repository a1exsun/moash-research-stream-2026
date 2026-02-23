# D-SMART (Lei et al. 2025)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Planar (2D) — Hybrid
- **Task**: Long-conv QA, Reasoning

## Core Mechanism

D-SMART 结合结构化事实记忆与基于遍历的推理树，通过 neuro-symbolic pipeline 实现对长对话中知识的持续积累与推理。

- 结合结构化事实记忆（持续更新的知识图谱）和基于遍历的推理树（traversal-based reasoning tree）
- 先用 LLM 提炼核心语义为简洁断言（concise assertions），将冗长的对话内容压缩为可操作的事实
- 再通过 neuro-symbolic pipeline 提取 OWL 规范的知识图谱片段（OWL-compliant KG fragments），实现形式化的知识表示
- LLM 作为 planner 在知识图谱上进行 beam search，动态规划推理路径，兼顾搜索效率与推理深度
- Hybrid 架构将符号推理的精确性与神经网络的灵活性相结合，适用于需要多步推理的复杂问答场景
