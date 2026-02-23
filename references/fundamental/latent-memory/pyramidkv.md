# PyramidKV (2024)

- **Paper**: (2024)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Layer-wise Budget
- **Task**: Language Modeling

## Core Mechanism

PyramidKV reallocates KV budgets across layers, implementing layer-aware KV cache management.

- Reallocates KV cache budget across Transformer layers (layer-wise budget allocation).
- Assigns different amounts of KV cache capacity to various layers based on their specific information requirements.
- Forms a pyramid-like KV allocation structure, where lower layers retain more KV pairs and higher layers gradually reduce them.
- Optimizes overall performance under a fixed total budget through differentiated budget allocation across layers.
- Avoids resource wastage caused by uniform allocation, maximizing the KV cache utilization of each layer.
