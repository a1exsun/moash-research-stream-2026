# R3Mem — Wang et al. 2025

- **Paper**: Wang et al. (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform
- **Task**: QA, Language Modeling

## Core Mechanism

R3Mem uses virtual memory tokens to achieve reversible compression, balancing compression and information retention.

- Introduces virtual memory tokens as an intermediate compressed representation.
- Employs a reversible compression mechanism, allowing compressed memory to recover more details when needed.
- Guarantees minimized information loss during the compression process through reversible transformations.
- Achieves a better trade-off between the compression efficiency of the KV cache and the quality of information retention.
