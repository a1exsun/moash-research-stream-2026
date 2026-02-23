# LONGMEM — Wang et al. 2023

- **Paper**: Wang et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Reuse — Residual SideNet KV
- **Task**: Language Modeling and Understanding

## Core Mechanism

LONGMEM uses a lightweight residual SideNet to store historical KV embeddings as persistent memory, enhancing long-range retrieval.

- Uses a lightweight residual SideNet auxiliary network to process historical KV embeddings.
- Stores historically processed KV pairs as persistent memory.
- SideNet integrates retrieved historical KV information into the main model's computation through residual connections.
- Enhances retrieval of long-range dependencies, allowing the model to efficiently access distant historical information.
- The parameters of the main network are frozen, and only the SideNet is trained, reducing training costs.
