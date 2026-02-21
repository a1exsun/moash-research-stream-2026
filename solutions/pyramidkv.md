# PyramidKV (2024)

- **Paper**: (2024)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Layer-wise Budget
- **Task**: Language Modeling

## Core Mechanism

PyramidKV 跨层重新分配KV预算，实现层级感知的KV cache管理。

- 跨Transformer层重新分配KV cache预算（layer-wise budget allocation）
- 不同层根据其信息需求分配不同数量的KV cache容量
- 形成金字塔式的KV分配结构，底层保留更多KV对，高层逐步减少
- 通过层级间的差异化预算分配，在总预算不变的情况下优化整体性能
- 避免了uniform allocation导致的资源浪费，使每层的KV cache利用率最大化
