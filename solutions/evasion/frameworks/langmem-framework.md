# LangMem — LangChain

**项目：** LangMem (LangChain)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Memory Framework — API-driven Memory Management

---

## 概述

LangChain生态中的记忆管理组件，采用Core API + Manager的设计模式，为LangChain agent提供标准化的记忆接口。

## 核心机制

- **Core API** — 提供底层的记忆存储、检索、更新等原子操作接口
- **Manager设计** — 在Core API之上提供高层的记忆管理器，封装常见的记忆管理模式和策略
- **LangChain生态集成** — 与LangChain的chain、agent、tool等组件无缝集成，共享统一的数据流和调用接口

## 备注

开源框架，作为LangChain生态的一部分，受益于LangChain社区的广泛使用和持续迭代。
