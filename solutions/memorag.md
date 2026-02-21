# MemoRAG — Qian et al. 2025

- **Paper**: Qian et al. (2025), WWW
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate + Query Rewriting
- **Task**: QA, Summary

## Core Mechanism

MemoRAG 使用LLM生成紧凑隐状态记忆捕获全局语义结构，并通过生成hypothetical document实现查询重写。

- 利用LLM生成紧凑的隐状态记忆（compact latent state memory），捕获输入文档的全局语义结构
- 生成hypothetical document用于查询重写，将模糊查询转化为更精准的检索请求
- 将全局记忆融入假设文档生成过程，使检索更好地匹配全局上下文
- 结合了latent memory的压缩能力与query rewriting的检索增强策略
