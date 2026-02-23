# XMem — Cheng et al. 2022

- **Paper**: Cheng et al. (2022)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Multimodal
- **Task**: Video Segmentation

## Core Mechanism

XMem 用于长视频对象分割，将每帧编码为key-value潜在嵌入并组织为多阶段记忆。

- 将视频每帧编码为key-value潜在嵌入（latent embeddings），作为基本记忆单元
- 组织为多阶段记忆层次结构：
  - **Perceptual memory**：感知记忆，存储最近帧的高保真表示
  - **Working memory**：工作记忆，维护中间粒度的活跃信息
  - **Long-term memory**：长期记忆，存储跨长时间跨度的关键信息
- 使用LFU（Least Frequently Used）策略移除低频条目，控制记忆容量
- 通过多阶段记忆管理实现长视频的高效对象跟踪与分割
