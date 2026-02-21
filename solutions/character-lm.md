# Character-LM / CharacterGLM

**论文：** Character-LM / CharacterGLM
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Post-Train

---

## 问题

如何让LLM在交互中稳定地表现出特定角色的个性、知识背景和行为模式？

## 方法

Character-LM和CharacterGLM将LLM微调为具有不同角色特征的模型。在后训练阶段（post-training）通过SFT（Supervised Fine-Tuning）将个性化记忆注入模型参数中，使模型能够持续、一致地扮演特定角色。

这一方法代表了参数化角色/人格注入（parametric character/persona injection）的典型范式：通过将角色知识、说话风格、价值观等信息编码进模型权重，实现比prompt-based方法更稳定、更深层的角色扮演能力。

## 核心机制

- **SFT角色注入**：通过监督微调将角色特征编码进模型参数
- **个性化记忆**：角色的知识背景、语言风格、价值观等被参数化存储
- **参数化人格**：角色信息深度融入模型权重，而非仅通过prompt提供

## 任务

- Role Playing
