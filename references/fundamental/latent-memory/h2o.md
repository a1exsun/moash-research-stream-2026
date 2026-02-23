# H2O (Heavy-Hitter Oracle) — Zhang et al. 2023

- **Paper**: Zhang et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Heavy Hitter Tokens
- **Task**: QA, Language Modeling

## Core Mechanism

H2O (Heavy-Hitter Oracle) reduces the memory footprint through a simple eviction policy that retains only recent tokens and special H2 tokens.

- Identifies and retains Heavy Hitter (H2) tokens: key tokens that frequently receive high attention scores in attention calculations.
- Combines recent tokens (local recent window) and H2 tokens to form a streamlined KV cache.
- Employs a simple and efficient eviction strategy: only these two types of tokens are kept, and others are discarded.
- Significantly reduces the memory footprint of the KV cache while maintaining the quality of model generation.
- Achieves effective cache management at extremely low cost by observing the heavy hitter phenomenon in attention patterns.
