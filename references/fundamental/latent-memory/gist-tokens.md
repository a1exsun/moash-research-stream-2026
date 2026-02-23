# Gist Tokens — Mu et al. 2023

- **Paper**: Mu et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Single Modal
- **Task**: Long-context Compression, Working Memory

## Core Mechanism

Gist Tokens train a language model to generate a set of gist tokens after processing a long prompt, compressing the long sequence into a small number of internal tokens for subsequent inference reuse.

- After processing a long prompt, the model generates a set of compact gist tokens as a compressed representation of the original sequence.
- These gist tokens can replace the original long sequence in subsequent inference, significantly reducing context length.
- Achieves prompt-level implicit compression without the need for additional external storage.
- The compressed representation retains the key semantic information of the original sequence, supporting efficient inference for downstream tasks.
