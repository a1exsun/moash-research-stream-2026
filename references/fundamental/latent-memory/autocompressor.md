# AutoCompressor — Chevalier et al. 2023

- **Paper**: Chevalier et al. (2023), EMNLP
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Single Modal
- **Task**: QA, Compression, Working Memory

## Core Mechanism

AutoCompressor encodes an entire long document into a small number of summary vectors, which serve as soft prompts for subsequent reasoning.

- Encodes long documents through the model itself into a compact set of summary vectors.
- These summary vectors are injected into the model as soft prompts, replacing the original long text.
- Achieves end-to-end document compression and representation learning, preserving global semantics.
- Compressed soft prompts can be reused for multi-turn QA and reasoning tasks.
