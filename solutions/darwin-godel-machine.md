# Darwin Godel Machine — Zhang et al. 2025

**论文：** Zhang et al. (2025)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Experiential Memory — Skill-based (Code Snippet)

---

## 问题

Agent的技能库在固定代码框架下难以持续演化，现有skill-based方法仅累积新技能而不修改已有技能的实现，无法实现真正的自我改进。

## 方法

安全地重写自身代码（recursive self-modification），在经验验证下逐步增强技能集。核心设计：
- **递归自修改代码库** — agent可以修改自身的代码实现，包括核心逻辑和技能函数
- **经验验证机制** — 每次代码修改都通过经验验证（empirical verification），确保修改后的表现不低于修改前
- **自引用技能增强** — 产生自引用的（self-referential）、逐步增强的技能集，技能之间可以相互调用和改进
- **安全修改保障** — 在沙箱环境中执行修改，验证通过后才应用到主代码库

## 影响

Darwin Godel Machine将经验记忆从"技能累积"推进到"技能进化"，实现了agent代码层面的持续自我改进。这种递归自修改范式为构建真正自适应的agent系统提供了新方向。

## 任务

- Coding
