# LLMLingua / LongLLMLingua — Jiang et al. 2023/2024

**论文：** Jiang et al. (2023, 2024)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Working Memory — Single-turn — Input Condensation

---

## 问题

单轮推理场景中，过长的输入prompt包含大量可预测或任务无关的内容，浪费context window容量并增加推理延迟，但简单截断会丢失关键信息。

## 方法

基于token perplexity估计，识别并丢弃可预测或任务无关的内容（hard condensation）。核心设计：
- **Token-level Perplexity评估** — 使用小型语言模型计算每个token的perplexity，量化其信息密度
- **选择性丢弃** — 移除低perplexity（高可预测性）的token，保留高信息密度的内容
- **Hard Condensation** — 直接丢弃token而非软压缩，属于硬性压缩方法
- **LongLLMLingua扩展** — 2024年的扩展版本针对长文档场景进行了优化，引入文档级和段落级的粗粒度筛选

## 影响

LLMLingua系列是prompt压缩领域的代表性工作，证明了基于perplexity的token级筛选可以在大幅压缩输入的同时保持任务性能。作为input condensation方法，它为working memory的单轮优化提供了高效工具。

## 任务

- Reasoning
- Conversation
- Summarization
- Multi-document QA
