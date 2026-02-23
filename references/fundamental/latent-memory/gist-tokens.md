# Gist Tokens — Mu et al. 2023

- **Paper**: Mu et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Single Modal
- **Task**: Long-context Compression, Working Memory

## Core Mechanism

Gist Tokens 训练语言模型在处理长prompt后生成一组gist tokens，将长序列压缩为少量内部token用于后续推理复用。

- 在长prompt处理完成后，模型生成一组紧凑的gist tokens作为原始序列的压缩表示
- 这些gist tokens可以在后续推理中替代原始长序列，大幅减少context length
- 实现了prompt级别的隐式压缩，无需额外外部存储
- 压缩后的表示保留了原始序列的关键语义信息，支持下游任务的高效推理
