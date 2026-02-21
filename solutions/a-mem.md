# A-MEM (Xu et al. 2025)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Planar (2D) — Graph
- **Task**: QA, Reasoning

## Core Mechanism

A-MEM 是 chunk-level 动态构建记忆图的代表方法，将知识标准化为卡片式单元并按语义关联组织成网络化笔记系统。

- 将知识标准化为卡片式单元（card-like units），每张卡片包含结构化的知识片段
- 按相关性组织记忆，相关的记忆卡片放入同一 box 中，形成逻辑分组
- 构建完整的记忆网络（networked notes with semantic links），卡片之间通过语义链接相互关联
- 作为 chunk-level 动态构建记忆图的代表方法，A-MEM 在记忆的组织和检索上实现了灵活的图结构，既保留了局部知识的精确性，又支持通过语义关联进行跨记忆的推理
