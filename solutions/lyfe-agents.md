# Lyfe Agents (Kaiya et al. 2023)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Hierarchical (3D) — Multi-Layer
- **Task**: Social Simulation

## Core Mechanism

Lyfe Agents 在社交模拟（social simulation）中将记忆分为三层，模拟人类认知中的记忆层次，分离重要的长期记录与低价值的瞬时细节。

### 三层记忆架构

- **Working Memory**：当前活跃的信息，对应正在进行的对话或任务的即时上下文
- **Short-term Memory**：近期的交互记录，保留一定时间窗口内的信息，用于维持对话的连贯性
- **Long-term Memory**：经过筛选和巩固的重要记忆，长期保存对智能体行为和社交关系有重要影响的信息

### 关键特性

- 分离重要的长期记录与低价值的瞬时细节，通过记忆的重要性评估机制决定信息在各层之间的流动
- 模拟人类记忆的自然衰减和巩固过程，使智能体在社交模拟中表现出更接近人类的记忆行为
- 该架构特别适用于社交模拟场景，智能体需要在长期的社交互动中积累和运用关于其他角色的知识
