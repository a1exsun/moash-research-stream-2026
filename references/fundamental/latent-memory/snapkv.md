# SnapKV — Li et al. 2024

- **Paper**: Li et al. (2024), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Aggregated Prefix KV
- **Task**: Language Modeling

## Core Mechanism

SnapKV aggregates high-importance prefix KV representations through a head-wise voting mechanism, achieving intelligent KV cache compression.

- Employs a head-wise voting mechanism to independently evaluate the importance of prefix tokens within each attention head.
- Aggregates the voting results from all heads to select globally high-importance prefix KV representations.
- Retains the selected high-importance KV pairs as a compressed prefix cache.
- Achieves more robust importance evaluation through voting aggregation across heads compared to single-head selection.
- Significantly reduces KV cache storage requirements while maintaining model performance.
