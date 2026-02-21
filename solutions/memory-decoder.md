# Memory Decoder — Cao et al. 2025

**论文：** Cao et al. (2025) — Memory Decoder
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — External — Adapter

---

## 问题

外部RAG方法需要实时检索开销，影响推理速度；而直接将知识编辑进模型参数又可能破坏原有知识。如何兼得参数内化的推理速度和即插即用的灵活性？

## 方法

Memory Decoder是一种即插即用（plug-and-play）的方法，不修改基座模型的参数，在这一点上类似外部RAG的设计理念。但与传统RAG不同的是，Memory Decoder通过将知识编码进外部decoder模块，在推理时无需实时检索外部知识库，从而同时达到参数内化的推理速度。

这种设计消除了外部检索开销，同时保持了基座模型的完整性和外部知识模块的可插拔性。

## 核心机制

- **即插即用**：不修改基座模型参数，外部模块可自由挂载
- **消除检索开销**：知识编码进decoder模块，推理时无需外部检索
- **基座模型完整性**：保持原始模型参数不变
- **兼顾速度与灵活性**：融合RAG的灵活性和参数化方法的推理效率

## 任务

- QA
- Language Modeling
