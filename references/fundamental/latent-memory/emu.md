# EMU — Na et al. 2024

- **Paper**: Na et al. (2024), ICLR
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Embeddings w/ Returns
- **Task**: Game

## Core Mechanism

EMU trains a state encoder to generate latent embeddings labeled with returns, associating memory with expected rewards.

- Trains a dedicated state encoder to encode game states into latent embeddings.
- Each embedding is labeled with desirability (expected return), representing the value assessment of that state.
- Implements return-conditioned embeddings to enable gain-based memory retrieval.
- Integrates value signals from reinforcement learning into memory representations, allowing the agent to make decisions based on successful patterns in historical experience.
