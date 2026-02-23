# Scissorhands — Liu et al. 2023

- **Paper**: Liu et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Pruned KV
- **Task**: Image Classification & Generation

## Core Mechanism

Scissorhands prunes tokens based on attention scores when the KV cache capacity is exceeded, achieving selective memory retention.

- Triggers token pruning based on attention scores whenever the KV cache capacity exceeds a preset threshold.
- Evaluates the importance of each token by assessing its attention score.
- Removes low-importance tokens to free up KV cache space.
- Implements dynamic capacity management for the KV cache, retaining the most critical information within limited memory.
- Transforms latent memory into a more compact representation through pruning strategies.
