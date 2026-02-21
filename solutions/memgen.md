# MemGen — Zhang et al. 2025

- **Paper**: Zhang et al. (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — LoRA Fragments
- **Task**: QA, Math, Code, Embodied Task, Reasoning
- **Optimization**: RL, SFT

## Core Mechanism

MemGen 在解码过程中动态生成潜在记忆，通过两个专用模块实现记忆的触发和编织。

- **Memory Trigger**：监控agent推理状态，判断何时需要显式调用记忆，决定在解码的哪个位置插入记忆片段
- **Memory Weaver**：利用agent当前状态构建潜在token序列，决定插入什么记忆内容
- 使用两个LoRA adapter分别实现Memory Trigger和Memory Weaver的功能
- 在解码过程中动态生成潜在记忆（latent memory），而非依赖预先存储的静态表示
- 通过RL和SFT联合优化记忆的触发时机和内容质量
