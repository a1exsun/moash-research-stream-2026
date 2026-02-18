# Research Log

研究进展与关键决策记录。按时间倒序排列。

---

## 2026-02-18

### 项目初始化
- 建立项目结构：`proposal/`, `refs/`, `docs/`
- 完成研究提议初稿 (`proposal/research_proposal_draft.md`)
- 核心方向确定：结构性稀疏拓扑对灾难性遗忘的消融研究

### 关键决策
- **从HST多机制方案简化到单一变量消融**：早期设计了Hippocampal Sparse Transformer（见 `refs/nanochat/HST_ARCHITECTURE.md`），包含路由隔离、局部更新、动态扩展等多机制。后反思认为：如果需要3-4种机制才能解决问题，说明还没找到问题本质。最终收敛到单一假说——稀疏拓扑本身对遗忘的影响。
- **排除工程化方案**：明确不研究RAG、Agentic Search、File-based Memory等非参数化方案。

### 待办
- [ ] 与教授沟通研究提议
- [ ] 确定实验框架选型（nanochat改造 vs PyTorch从零搭建 vs 其他）
- [ ] 系统性阅读refs/中的参考材料并整理批判性笔记
