# H2O (Heavy-Hitter Oracle) — Zhang et al. 2023

- **Paper**: Zhang et al. (2023), NeurIPS
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Heavy Hitter Tokens
- **Task**: QA, Language Modeling

## Core Mechanism

H2O（Heavy-Hitter Oracle）通过保留最近tokens和特殊H2 tokens的简单淘汰策略，减少memory footprint。

- 识别并保留Heavy Hitter (H2) tokens：即在attention计算中频繁获得高注意力分数的关键tokens
- 结合最近tokens（local recent window）和H2 tokens构成精简的KV cache
- 采用简单高效的淘汰策略：仅保留这两类tokens，丢弃其余
- 大幅减少KV cache的memory footprint，同时保持模型生成质量
- 通过观察attention模式中的heavy hitter现象，以极低开销实现有效的cache管理
