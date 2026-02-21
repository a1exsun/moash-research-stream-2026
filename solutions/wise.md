# WISE — 2024, NeurIPS

**论文：** WISE (2024, NeurIPS)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Adapter

---

## 问题

在终身编辑（lifelong editing）场景中，持续向模型注入新知识会导致新旧知识之间的冲突，影响模型整体性能。

## 方法

WISE采用双参数记忆设置（dual parametric memory），将预训练知识和编辑知识分离存储在两套独立的参数中。在推理时，路由机制（routing mechanism）根据输入动态选择使用哪个参数记忆——原始预训练参数或编辑后的参数。

这种分离存储和动态路由的设计有效缓解了终身编辑过程中新旧知识的冲突问题。

## 核心机制

- **双参数记忆**：预训练知识和编辑知识分别存储在独立参数集中
- **动态路由**：推理时根据输入语义自动选择使用哪套参数
- **知识冲突缓解**：通过物理隔离避免新旧知识的互相干扰
- **终身编辑支持**：设计面向持续、长期的知识更新场景

## 任务

- QA
- Hallucination Detection
