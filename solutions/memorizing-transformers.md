# Memorizing Transformers — Wu et al. 2022

- **Paper**: Wu et al. (2022), ICLR
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Reuse — External KV Cache
- **Task**: Language Modeling

## Core Mechanism

Memorizing Transformers 显式存储过去的KV对，推理时通过KNN搜索检索相关记忆。

- 将过去处理过的token的key-value对显式存储到外部记忆中
- 推理时通过KNN（k-nearest neighbors）搜索在存储的KV对中检索最相关的条目
- 检索到的KV对被注入attention计算，扩展模型的有效上下文范围
- 实现了latent memory的直接复用（reuse），无需重新编码或压缩历史信息
