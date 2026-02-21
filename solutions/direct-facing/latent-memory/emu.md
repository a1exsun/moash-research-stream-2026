# EMU — Na et al. 2024

- **Paper**: Na et al. (2024), ICLR
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Embeddings w/ Returns
- **Task**: Game

## Core Mechanism

EMU 训练state encoder生成带return标注的潜在嵌入，将记忆与期望收益关联。

- 训练专用的state encoder将游戏状态编码为潜在嵌入（latent embeddings）
- 每个嵌入标注了desirability（期望回报），表示该状态的价值评估
- 通过return-conditioned embeddings实现基于收益的记忆检索
- 将强化学习中的价值信号融入记忆表示，使agent能基于历史经验中的成功模式进行决策
