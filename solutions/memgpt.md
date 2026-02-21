# MemGPT — Packer et al. 2023

**论文：** Packer et al. (2023)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Token-level Flat Memory — OS-inspired Memory Management

---

## 问题

LLM受限于固定长度的context window，无法处理超长对话或大规模文档，记忆容量与任务需求之间存在根本矛盾。

## 方法

引入操作系统隐喻管理LLM记忆，借鉴传统OS中虚拟内存的分层设计。将记忆分为两层：
- **Main Context**（工作区）— 类比物理内存，对应当前LLM context window中的活跃内容
- **External Context**（外部存储）— 类比磁盘，存储超出context window的历史对话和文档

LLM自主调用retrieval函数访问外部记忆，实现在有限context window下对无界信息的透明管理。

## 影响

MemGPT是将操作系统范式引入LLM记忆管理的开创性工作，启发了后续大量OS-inspired系统，包括MemOS、MemoryOS等操作系统范式的记忆管理框架。

## 任务

- Long-conversation QA
- Document QA
