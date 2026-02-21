# Generative Agents — Park et al. 2023 (Stanford)

**论文：** Park et al. (2023)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Multi-Agent Shared Memory — Social Simulation

---

## 问题

社交模拟环境中，多个Agent需要具备可信的人类行为模式，包括记忆、反思、规划和社交互动能力，且信息需要能在Agent群体间自然流动。

## 方法

提出社交模拟中的生成式Agent架构，核心记忆机制：
- **三因素检索评分** — 记忆通过recency（时间近因）、importance（重要性）、relevance（与当前查询的相关性）三个维度综合评分，决定检索优先级
- **共享记忆基底** — 全局环境状态和公共交互日志作为所有Agent可访问的共享记忆层
- **自然信息扩散** — 通过Agent间的对话和交互，信息在群体中自然传播，无需显式的记忆同步机制

## 特点

Generative Agents是将LLM记忆机制应用于多Agent社交模拟的标志性工作。其三因素记忆检索机制被后续大量工作采纳，成为Agent记忆检索的经典设计模式。共享记忆+自然扩散的设计使得集体行为涌现成为可能。

## 任务

- Social Simulation
