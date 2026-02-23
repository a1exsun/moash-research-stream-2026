# MemoryLLM — Wang et al. 2024

- **Paper**: Wang et al. (2024)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Persistent Tokens
- **Task**: Long-conv QA, Model Editing

## Core Mechanism

MemoryLLM embeds a set of dedicated memory tokens within the model's latent space, achieving self-updating latent embeddings.

- Embeds a set of dedicated memory tokens within the model's latent space.
- Employs a self-updatable latent embeddings mechanism, where memory tokens can automatically update with new information.
- Injects a reasoning process between Transformer layers, deeply coupling memory with model computation.
- Achieves persistent token-level memory, maintaining knowledge states across dialogues without external storage.
