# Retroformer — Yao et al. 2024

**论文：** Yao et al. (2024) — Retroformer
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Auxiliary LM

---

## 问题

Agent在执行任务时缺乏从过往任务的成功和失败中系统性学习的机制，导致重复犯错、无法积累经验。

## 方法

Retroformer提出了一种学习范式（learning paradigm），专门用于记忆过去任务执行的成败经验。通过辅助语言模型（auxiliary LM）记录和学习历史任务的执行轨迹，Retroformer能够在后续任务中利用这些经验改进决策。

与基于prompt的反思方法不同，Retroformer通过参数化的辅助模型来存储和提炼经验，使经验学习更加系统化和持久化。

## 核心机制

- **经验记忆**：记录过去任务执行的成功和失败经验
- **辅助LM**：通过参数化的辅助模型存储和提炼经验
- **学习范式**：从历史执行轨迹中系统性地学习改进策略
- **跨任务迁移**：将过往经验应用到新任务的决策中

## 任务

- QA
- Web Navigation
