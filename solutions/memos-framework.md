# MemOS — MemTensor

**项目：** MemOS (MemTensor)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Memory Framework — Memory Operating System

---

## 概述

Memory Operating System for AI Agents。MemOS是一个将操作系统范式应用于AI agent记忆管理的开源框架，提供统一的记忆调度和管理接口。

## 核心机制

- **MemScheduler** — 动态调度器，根据任务需求自动选择最优的记忆类型：parametric memory（参数化记忆）、activation memory（激活记忆）、plaintext memory（明文记忆）
- **树形记忆结构** — 使用树状层次化结构组织记忆，支持多粒度的记忆存储和检索
- **MemCube** — 记忆管理的核心数据结构，封装记忆的存储、索引和访问操作
- **上下文切换** — 支持用户级、任务级、组织级的上下文切换，实现多租户和多任务的记忆隔离与共享

## 评估

- LoCoMo
- PrefEval
- LongMemEval
- PersonaMem

## 备注

开源框架。注意与MemoryOS（百家/BAI-LAB）为不同项目。
