# MEND — Mitchell et al. 2022

**论文：** Mitchell et al. (2022) — Model Editor Networks with Gradient Decomposition
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Post-Train

---

## 问题

直接fine-tuning来编辑模型知识会导致对无关知识的灾难性干扰，且效率低下。如何实现快速、精准的单步知识编辑？

## 方法

MEND（Model Editor Networks with Gradient Decomposition）引入辅助网络（editor network），通过分解fine-tuning梯度来实现快速的单步编辑。辅助网络学习将标准梯度转换为局部化的参数更新，使得编辑只影响目标知识而最小化对无关知识的干扰。

关键创新在于梯度分解：将高维梯度分解为低秩因子，辅助网络在低秩空间中学习如何生成精确的编辑方向，从而实现高效且局部化的参数修改。

## 核心机制

- **辅助编辑网络**：专门训练的网络，学习将梯度转换为精确的参数更新
- **梯度分解**：将fine-tuning梯度分解为低秩因子，降低计算成本
- **单步编辑**：无需多轮迭代，一步完成知识修改
- **局部性保障**：最小化对无关知识的干扰

## 任务

- QA
- Fact Checking
- Model Editing
