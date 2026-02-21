# AriGraph (Anokhin et al. 2024)

- **Paper**: [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)
- **Source**: arXiv 2512.13564v2
- **Category**: Token-level Memory — Hierarchical (3D)
- **Task**: Game

## Core Mechanism

AriGraph 在统一图中按信息类型进行分层，将语义知识与情景经验整合在同一图结构中，为游戏环境中的智能体提供结构化的世界模型。

- 在统一图（unified graph）中按信息类型分层，不同层承载不同粒度和性质的信息
- Semantic knowledge-graph 层：编码环境结构的世界模型（world model），表示环境中物体、位置、属性之间的通用关系
- Episodic component 层：将具体观察（specific observations）链接回语义主干（semantic backbone），记录智能体在特定时刻的具体经验
- 通过将语义层和情景层整合在同一图中，AriGraph 使智能体既能利用通用的环境知识进行规划，又能回忆具体的历史经验来指导决策
- 该方法特别适用于游戏场景，智能体需要在探索中不断积累对环境的理解
