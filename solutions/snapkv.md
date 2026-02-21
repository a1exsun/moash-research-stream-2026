# SnapKV — Li et al. 2024

- **Paper**: Li et al. (2024), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Aggregated Prefix KV
- **Task**: Language Modeling

## Core Mechanism

SnapKV 通过head-wise voting机制聚合高重要性前缀KV表示，实现KV cache的智能压缩。

- 采用head-wise voting机制，在每个attention head独立评估prefix tokens的重要性
- 聚合各head的投票结果，选出全局高重要性的前缀KV表示
- 将选中的高重要性KV对作为压缩后的prefix cache保留
- 通过跨head的投票聚合实现比单head选择更鲁棒的重要性评估
- 在保持模型性能的前提下大幅减少KV cache的存储需求
