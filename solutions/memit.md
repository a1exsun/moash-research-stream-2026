# MEMIT — Mitchell et al. 2023

**论文：** Mitchell et al. (2023) — Mass-Editing Memory in a Transformer
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Post-Train

---

## 问题

现有knowledge editing方法（如ROME）一次只能编辑单个事实，无法高效地批量更新大量知识，限制了实际应用中的可扩展性。

## 方法

MEMIT（Mass-Editing Memory in a Transformer）在ROME的基础上进一步扩展，支持批量编辑。通过多层残差分布（multi-layer residual distribution）和batch公式，MEMIT能够同时更新数千条事实，大幅提升了knowledge editing的可扩展性。

核心思路是将编辑目标分布到多个相关的MLP层上，而非集中在单一层，从而在保持编辑质量的同时支持大规模并行编辑。

## 核心机制

- **多层残差分布**：将编辑信号分散到多个Transformer层的MLP中
- **Batch编辑公式**：支持同时处理大量事实更新请求
- **可扩展性**：从单条编辑扩展到数千条事实的批量编辑

## 任务

- QA
- Model Editing
