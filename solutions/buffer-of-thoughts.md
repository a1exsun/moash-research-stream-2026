# Buffer of Thoughts — Yang et al. 2024

**论文：** Yang et al. (2024)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Experiential Memory — Strategy-based (Pattern / Thought-Template)

---

## 问题

LLM在面对复杂推理任务时，缺乏对高层思维模式的系统化积累与复用机制，每次解题都需要从头构建推理链。

## 方法

维护一个meta-buffer，用于存储高层思维模板（thought-templates）。核心流程：
- **模板积累** — 从成功的推理过程中提取和抽象出通用的思维模板，存入meta-buffer
- **模板检索** — 面对新问题时，从meta-buffer中检索语义最相关的thought-template
- **模板实例化** — 将检索到的抽象模板根据当前问题的具体参数进行实例化，生成针对性的推理路径

## 特点

代表了Strategy-based Memory中Pattern类型的典型方法——记忆的是抽象的解题模式而非具体的解题步骤，通过模板化实现经验的高效迁移。

## 任务

- Game
- Reasoning
- Coding
