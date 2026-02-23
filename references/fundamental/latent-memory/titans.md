# Titans (2025)

- **Paper**: (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Neural Weights (MLP)
- **Task**: QA, Language Modeling

## Core Mechanism

Titans 将长程信息压缩为在线更新的MLP权重，使用神经权重本身作为记忆形式。

- 将长程上下文信息压缩编码为MLP的权重参数，实现以神经网络权重作为记忆载体
- MLP权重在推理过程中在线更新（online update），动态吸收新信息
- 推理时通过MLP产生潜在向量（latent vectors），将记忆内容注入当前计算
- 将传统的显式KV存储转化为隐式的参数化记忆，在权重空间中编码长距离依赖
