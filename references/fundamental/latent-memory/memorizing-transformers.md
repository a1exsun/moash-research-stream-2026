# Memorizing Transformers — Wu et al. 2022

- **Paper**: Wu et al. (2022), ICLR
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Reuse — External KV Cache
- **Task**: Language Modeling

## Core Mechanism

Memorizing Transformers explicitly store past KV pairs and retrieve relevant memories through KNN search during inference.

- Explicitly stores the key-value pairs of past processed tokens in external memory.
- Performs KNN (k-nearest neighbors) search during inference to retrieve the most relevant entries from the stored KV pairs.
- The retrieved KV pairs are injected into the attention calculation, extending the model's effective context range.
- Achieves direct reuse of latent memory without the need to re-encode or compress historical information.
