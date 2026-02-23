# FOT (Focused Transformer) — Tworkowski et al. 2023

- **Paper**: Tworkowski et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Reuse — Memory-Attention KV
- **Task**: QA, Few-shot Learning, Language Modeling

## Core Mechanism

Focused Transformer introduces memory-attention layers and performs KNN retrieval on additional KV memory during inference.

- Introduces dedicated memory-attention layers responsible for interacting with external KV memory.
- Performs KNN retrieval on stored additional KV memory during inference to obtain the most relevant historical information.
- Uses the memory-attention mechanism to focus the model on the most relevant historical KV pairs.
- Compared to Memorizing Transformers, FOT achieves more precise memory retrieval and fusion through dedicated attention layers.
