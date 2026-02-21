# R3Mem — Wang et al. 2025

- **Paper**: Wang et al. (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform
- **Task**: QA, Language Modeling

## Core Mechanism

R3Mem 使用虚拟记忆tokens实现可逆压缩（reversible compression），在压缩与信息保留之间取得平衡。

- 引入虚拟记忆tokens（virtual memory tokens）作为中间压缩表示
- 采用可逆压缩机制（reversible compression），使压缩后的记忆可以在需要时恢复更多细节
- 通过可逆变换保证压缩过程中的信息损失最小化
- 在KV cache的压缩效率和信息保留质量之间实现更优的折中
