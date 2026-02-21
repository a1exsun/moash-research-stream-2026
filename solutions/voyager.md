# Voyager — Wang et al. 2024

**论文：** Wang et al. (2024)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Experiential Memory — Skill-based (Code Library)

---

## 问题

开放世界游戏环境中，Agent需要不断学习和积累新技能，但缺乏有效机制将成功经验沉淀为可复用的行为能力。

## 方法

Minecraft中的自主探索Agent，核心是构建不断增长的可执行技能库（code library）。设计流程：
- Agent在Minecraft世界中自主探索、尝试完成各类子任务
- 将成功的子轨迹蒸馏为可复用的代码片段（executable skills）
- 技能库持续扩展，新技能可以组合调用已有技能
- 面对新任务时，从技能库中检索相关技能进行组合执行

## 特点

- 代表了Skill-based Memory的典型范式——以可执行代码而非自然语言文本作为记忆载体
- 支持多模态输入（视觉观察 + 文本指令）
- 技能库的增长使Agent的能力边界不断扩展，体现了持续学习的核心理念

## 任务

- Game (Minecraft)
