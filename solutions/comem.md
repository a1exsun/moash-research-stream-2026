# CoMem — Wu et al. 2025

- **Paper**: Wu et al. (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Multimodal
- **Task**: Multimodal QA

## Core Mechanism

CoMem 通过Q-Former压缩vision-language输入为固定长度token，实现密集连续记忆。

- 使用Q-Former架构将多模态（vision-language）输入压缩为固定长度的token序列
- 生成密集连续记忆（dense continuous memory），保留视觉和语言的联合语义
- 支持即插即用的无限上下文长度（plug-and-play unlimited context length）
- 压缩后的固定长度表示使得记忆容量不受原始输入长度限制
