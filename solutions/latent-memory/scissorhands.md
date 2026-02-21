# Scissorhands — Liu et al. 2023

- **Paper**: Liu et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Pruned KV
- **Task**: Image Classification & Generation

## Core Mechanism

Scissorhands 在KV cache容量超出时基于attention scores修剪tokens，实现记忆的选择性保留。

- 当KV cache容量超出预设阈值时，触发基于attention scores的token修剪
- 通过评估每个token的attention得分来判断其重要性
- 低重要性的tokens被移除，释放KV cache空间
- 实现了KV cache的动态容量管理，在有限内存下保留最关键的信息
- 通过修剪（pruning）策略将latent memory转化为更紧凑的表示
