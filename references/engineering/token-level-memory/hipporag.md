# HippoRAG / HippoRAG 2 (Gutierrez et al. 2025)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Hierarchical (3D) — Multi-Layer
- **Task**: QA

## Core Mechanism

HippoRAG 是受神经生物学启发的长期记忆系统，模拟海马体的记忆整合机制，采用多层图结构实现高效的知识存储与检索。HippoRAG 2 进一步扩展到 non-parametric continual learning 设置。

### HippoRAG

- 受神经生物学启发的长期记忆系统，模拟海马体（hippocampus）在记忆巩固中的角色
- 双层结构：semantic graph（语义图，编码概念间的通用关系）+ episodic graph（情景图，记录具体的段落级经验）
- 采用 personalized PageRank 进行检索，通过图上的随机游走发现与查询相关的多跳信息

### HippoRAG 2

- 扩展到 non-parametric continual learning 设置，支持在不断增长的知识库上持续学习
- 丰富索引层的深度段落集成（deep passage integration），将段落内容更充分地融入图结构
- 在线 LLM 过滤（online LLM filtering），在检索阶段利用 LLM 动态筛选最相关的信息，提高检索精度
