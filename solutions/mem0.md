# Mem0 — Chhikara et al. 2025

**论文：** Chhikara et al. (2025)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Token-level Flat Memory — Standardized Memory Maintenance

---

## 问题

Agent记忆缺乏标准化的维护操作接口，记忆的增删改查、摘要与整合流程碎片化，不利于大规模部署和后续优化。

## 方法

建立标准化的记忆维护操作框架（增删改查），为Agent记忆管理提供统一接口。核心设计：
- **双层存储结构** — 同时保存summary（摘要层）和original dialogue（原始对话层），兼顾检索效率与信息完整性
- **LLM驱动的语义摘要** — 利用LLM对对话进行语义级别的压缩与总结
- **混合存储后端** — Mem0^g版本支持Graph + Vector的混合存储，引入Knowledge Graph增强语义关联

## 影响

Mem0作为开源框架，为后续工作提供了标准化基础。其记忆操作接口为Memory-R1等基于RL的记忆优化方法奠定了基础，使得记忆维护操作可以作为RL的action space进行策略优化。

## 任务

- Long-conversation QA

## 备注

开源框架，社区广泛采用。
