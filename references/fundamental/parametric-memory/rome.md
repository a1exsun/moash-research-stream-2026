# ROME — Meng et al. 2022

**论文：** Meng et al. (2022) — Rank-One Model Editing
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Post-Train — Knowledge Editing

---

## 问题

如何在不重训整个模型的前提下，精确修改LLM中存储的特定事实知识？

## 方法

ROME（Rank-One Model Editing）通过causal tracing技术精确定位存储特定事实的MLP层，然后对该层应用rank-one updates注入新信息。核心思路是将Transformer中的MLP视为key-value存储，通过修改特定层的权重矩阵来更新或纠正模型记忆的事实。

与早期的editing方法相比，ROME实现了更高的编辑精度和更好的泛化能力，能够在修改目标事实的同时最小化对其他知识的影响。

## 核心机制

- **Causal tracing**：通过因果介入实验定位事实存储的具体MLP层
- **Rank-one update**：对目标层的权重矩阵施加秩一更新，精准注入新知识
- **局部性**：编辑仅影响目标事实，不干扰模型的其他行为

## 任务

- QA
- Fact Checking
