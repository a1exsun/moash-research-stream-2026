# FOT (Focused Transformer) — Tworkowski et al. 2023

- **Paper**: Tworkowski et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Reuse — Memory-Attention KV
- **Task**: QA, Few-shot Learning, Language Modeling

## Core Mechanism

Focused Transformer 引入memory-attention layers，在推理时对额外KV记忆执行KNN检索。

- 引入专用的memory-attention layers，专门负责与外部KV记忆的交互
- 在推理时对存储的额外KV记忆执行KNN检索，获取最相关的历史信息
- 通过memory-attention机制使模型聚焦于最相关的历史KV对
- 相比Memorizing Transformers，FOT通过专用attention层实现更精准的记忆检索与融合
