# MemoryLLM — Wang et al. 2024

- **Paper**: Wang et al. (2024)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Persistent Tokens
- **Task**: Long-conv QA, Model Editing

## Core Mechanism

MemoryLLM 在模型潜在空间内嵌入一组专用memory tokens，实现自更新的潜在嵌入。

- 在模型的潜在空间（latent space）中嵌入一组专用的memory tokens
- 采用self-updatable latent embeddings机制，记忆tokens可随新信息自动更新
- 在Transformer层间注入推理过程，使记忆与模型计算深度耦合
- 实现了持久化的token级记忆，无需外部存储即可维护跨对话的知识状态
