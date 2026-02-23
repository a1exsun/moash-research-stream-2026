# AlphaEdit — Fang et al. 2025

**论文：** Fang et al. (2025) — Null-space Constrained Knowledge Editing
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Post-Train

---

## 问题

现有knowledge editing方法在编辑新知识时可能破坏模型已有的知识结构，尤其在连续多次编辑后累积误差显著。

## 方法

AlphaEdit提出零空间约束的知识编辑（Null-space Constrained Knowledge Editing）方法。核心思路是将知识编辑的参数更新投影到模型现有知识表示的零空间（null space）中，确保新编辑不会干扰已有知识的表达。

通过这种约束，AlphaEdit在注入新知识的同时严格保持模型对原有知识的保留，提升了连续编辑场景下的稳定性和可靠性。

## 核心机制

- **零空间投影**：将参数更新约束在现有知识表示的零空间中
- **知识保留**：确保编辑操作不干扰已有知识的表达
- **连续编辑稳定性**：在多次编辑后仍能保持模型性能

## 任务

- QA
