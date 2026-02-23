# RazorAttention — Tang et al. 2025

- **Paper**: Tang et al. (2025), ICLR
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Compensated Window
- **Task**: Language Modeling

## Core Mechanism

RazorAttention 计算每个head的effective attention span，只保留有限local window并使用compensation tokens保存被丢弃条目的信息。

- 计算每个attention head的effective attention span，量化各head实际需要的上下文范围
- 对每个head只保留有限的local window，丢弃超出范围的远程KV对
- 引入compensation tokens：将被丢弃的远程KV条目的关键信息压缩到补偿token中
- compensation tokens注入attention计算，弥补因窗口截断导致的信息损失
- 实现了per-head自适应的KV cache管理，不同head根据其attention span获得不同的cache策略
