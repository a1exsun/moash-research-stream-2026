# M+ (2025)

- **Paper**: (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Cross-layer Token Pools
- **Task**: QA, Document Reasoning

## Core Mechanism

M+ proposes a cross-layer long-term memory token pool architecture, extending the MemoryLLM concept to cross-layer design.

- Constructs a cross-layer long-term memory token pool, where different Transformer layers share and interact with memory representations.
- Extends the single-layer memory token concept of MemoryLLM, introducing a cross-layer architecture to achieve deeper memory integration.
- Employs a dual-level memory design: short-term memory and long-term memory.
- Discards outdated short-term memory entries and compresses key information into long-term storage.
- Uses a hierarchical compression strategy to balance memory capacity with information retention.
