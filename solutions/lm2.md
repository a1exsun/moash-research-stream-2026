# LM2 (2025)

- **Paper**: (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Matrix Slots
- **Task**: QA, Reasoning

## Core Mechanism

LM2 在每层引入矩阵形状的潜在记忆slot（matrix-shaped latent memory slots），实现结构化的层内记忆存储。

- 在Transformer的每一层引入matrix-shaped latent memory slots
- 记忆以矩阵形式组织，提供比向量更丰富的表示能力
- 与Titans等方法方向相关但结构不同：LM2强调矩阵slot的结构化存储
- 每层的记忆slot独立维护，支持层级间的信息传递与整合
