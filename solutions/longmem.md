# LONGMEM — Wang et al. 2023

- **Paper**: Wang et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Reuse — Residual SideNet KV
- **Task**: Language Modeling and Understanding

## Core Mechanism

LONGMEM 使用轻量级residual SideNet将历史KV嵌入作为持久化记忆存储，增强长距离检索。

- 使用轻量级的residual SideNet辅助网络处理历史KV嵌入
- 将历史处理过的KV对作为持久化记忆（persistent memory）存储
- SideNet通过残差连接将检索到的历史KV信息融入主模型的计算
- 增强长距离依赖的检索能力，使模型能够高效访问远距离的历史信息
- 主网络参数冻结，仅训练SideNet，降低训练成本
