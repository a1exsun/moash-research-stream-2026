# M+ (2025)

- **Paper**: (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Cross-layer Token Pools
- **Task**: QA, Document Reasoning

## Core Mechanism

M+ 提出跨层长期记忆token池架构（cross-layer long-term memory architecture），扩展MemoryLLM的思路到跨层设计。

- 构建跨层的长期记忆token池，不同Transformer层共享和交互记忆表示
- 扩展MemoryLLM的单层memory token思路，引入跨层架构实现更深层的记忆整合
- 采用双层记忆设计：短期记忆和长期记忆
- 丢弃过时的短期记忆条目，将关键信息压缩到长期存储中
- 通过分层压缩策略平衡记忆容量和信息保留
