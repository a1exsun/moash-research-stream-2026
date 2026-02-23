# AutoCompressor — Chevalier et al. 2023

- **Paper**: Chevalier et al. (2023), EMNLP
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Single Modal
- **Task**: QA, Compression, Working Memory

## Core Mechanism

AutoCompressor 将整个长文档编码为少量summary vectors，作为soft prompts供后续推理使用。

- 将长文档通过模型自身编码为一组紧凑的summary vectors
- 这些summary vectors作为soft prompts注入模型，替代原始长文本
- 实现端到端的文档压缩与表示学习，保留全局语义
- 压缩后的soft prompts可复用于多轮问答和推理任务
