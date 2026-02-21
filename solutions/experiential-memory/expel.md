# ExpeL — Zhao et al. 2024

**论文：** Zhao et al. (2024)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Experiential Memory — Case + Strategy Hybrid

---

## 问题

Agent在任务执行中的经验积累通常只保留单一形式（要么是具体案例，要么是抽象策略），缺乏同时利用两类经验的互补优势。

## 方法

通过trial-and-error自主积累经验，同时维护两类互补的经验记忆：
- **Case-based Memory** — 存储成功的完整轨迹（successful trajectories），作为具体的参考案例
- **Strategy-based Memory** — 从经验中提取文本洞见（textual insights），作为高层策略指导

核心机制是对比成功与失败经验，提取整体规划层面的洞见。Agent不仅记住"做了什么成功了"，还总结出"为什么成功/失败"的抽象规律。

## 特点

ExpeL代表了Case + Strategy混合经验记忆的设计范式。具体案例提供细节参考，抽象洞见提供方向指导，两者互补使Agent的经验利用更加全面和鲁棒。

## 任务

- Reasoning
