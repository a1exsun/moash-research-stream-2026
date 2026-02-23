# Proposal 05: Compression-Writability Bound 与 Representational Regime Differentiation 的必要性

## 目标

从第一性原理出发，形式化参数化系统中 compression 与 writability 的根本对抗关系，证明 multi-regime architecture（即参数化 CLS）是持续学习的**必要架构条件**，并通过最小实验验证理论预测。

核心定位：
- **不是提出新的 CL 方法**——而是建立一个 necessary condition
- 任何不满足此条件的 CL 系统都有一个**理论上可证明的容量天花板**
- 为后续所有 CL 架构设计提供可证伪的理论约束

---

## 起源与动机

### 从 P01-P04 的教训出发

P01-P04 共享一个根本缺陷：**缺少理论根基**。

- P01 (ablation) 和 P02 (SOTA sparse conversion)：围绕 weight sparsity 假说设计，但该假说在固定架构下 trivially true（详见 `20260224-0007.md`）
- P03 (nanoGPT pretrain)：控制变量最干净，但外推性受限于规模
- P04 (CDCL)：不改架构仅改 update rule，本质上是在 dense 全局参数空间做约束——根据本提议的理论，这类方法有 provable 的容量天花板
- P03-2 (interference phase diagram)：理论野心最大但操作化困难

**核心问题**：这些提议都在回答"哪种方法更好"，而没有回答"什么是持续学习的结构性必要条件"。

### 从 processing doc (20260224-0249) 的理论演进

本提议直接构建在以下已确立的论证链上：

1. **三个本质问题**：定位（where to write）、容量（how much room）、检索（how to recall）
2. **Superposition 是问题根源**：高压缩（重度 superposition）提供容量但摧毁可写性
3. **CLS 的正确类比**：海马体 ≠ RAG，而是第二参数化系统——整个 CLS 过程纯参数化
4. **Activation sparsity 是关键**：海马体通过极端 activation sparsity（DG ~2-5%）实现 pattern separation，而非 weight sparsity
5. **研究问题转向**：从"是否需要 weight sparsity"到"什么样的 representational regime differentiation 是必要的"

本提议的目标是将第 5 点**形式化为可证明的定理**。

---

## 研究问题

1. Compression-writability tradeoff 能否被形式化为一个 information-theoretic bound？
2. 在单一 activation sparsity regime 下，bounded forgetting 的 capacity 是否存在 provable 的上界？
3. Dual-regime architecture（两个不同 activation sparsity 水平 + 巩固机制）是否能 provably 突破该上界？

---

## 假设

### H1 (Interference-Sparsity Monotonicity)

不同任务间的 write interference 是 activation sparsity 的单调递减函数。

形式化：设 $I(s)$ 为 activation sparsity 为 $s$ 时的 expected gradient inner product between tasks，则：

$$\frac{\partial I}{\partial s} < 0$$

**直觉**：如果两个任务激活几乎不重叠的神经元子集（高 activation sparsity → pattern separation），更新一个任务的参数几乎不影响另一个任务的表征。

**生物对应**：海马体 Dentate Gyrus 的 ~2-5% activation rate 实现 pattern separation，使得不同记忆间低干扰。

### H2 (Single-Regime Capacity Bound)

对于 activation sparsity 均匀为 $s$ 的单一 regime 系统，存在 fundamental capacity bound：

$$C(s, \epsilon) \cdot B(s) \leq \Phi(d)$$

其中：
- $C(s, \epsilon)$：bounded forgetting ($\leq \epsilon$) 下的最大可学任务数
- $B(s)$：每任务可编码信息量（随 $s$ 增大而减小，因为更少 neuron 参与编码）
- $\Phi(d)$：仅依赖参数总量 $d$ 的上界函数

**含义**：单一 regime 面临不可调和的 tradeoff——
- 高 $s$（极端稀疏）：低 interference → 大 $C$ 但小 $B$（每任务信息少）
- 低 $s$（分布式编码）：高 interference → 小 $C$ 但大 $B$（每任务信息多）
- 总 information throughput $C \cdot B$ 被 $\Phi(d)$ 硬约束

### H3 (Dual-Regime Breaks the Bound)

一个具有两个不同 activation sparsity 水平 $s_1 > s_2$ 和巩固机制 $\mathcal{C}$ 的双 regime 系统，可以突破单一 regime 的容量上界：

$$C_{\text{dual}}(\epsilon) > \max_s C_{\text{single}}(s, \epsilon)$$

**证明思路**：
1. **快速区**（$s_1$，高稀疏）：以低 interference 吸收新任务，容量受限于 $C(s_1) \cdot B(s_1)$
2. **巩固** $\mathcal{C}$：将快速区知识转移到慢速区（$s_2$，低稀疏），后者有更高的 per-parameter capacity
3. **容量释放**：巩固后快速区参数部分 reset，释放容量给下一批新任务
4. **关键**：巩固是受控过程（interleaved replay，非 online learning），因此可以在不引发灾难性遗忘的条件下完成知识转移
5. **总效果**：系统的 effective capacity = 慢速区的高容量 $C(s_2) \cdot B(s_2)$，且全过程 forgetting bounded

---

## 理论框架

### 形式化定义

**模型**：$f_\theta: \mathcal{X} \to \mathcal{Y}$，参数 $\theta \in \mathbb{R}^d$，隐层表征 $h(x;\theta) \in \mathbb{R}^m$

**Activation sparsity**：$s(\theta) = 1 - \mathbb{E}_{x \sim \mathcal{D}} \left[ \frac{\|h(x;\theta)\|_0}{m} \right]$

**任务序列**：$\{(\mathcal{D}_t, L_t)\}_{t=1}^T$，其中 $\mathcal{D}_t$ 是数据分布，$L_t$ 是损失函数

**Forgetting 定义**：$F_t(\theta_T) = L_t(\theta_T) - L_t(\theta_t^*)$，其中 $\theta_t^*$ 是学完任务 $t$ 后的参数

**Bounded forgetting**：$\forall t \leq T, \, F_t(\theta_T) \leq \epsilon$

**Write interference**：
$$I(s) = \mathbb{E}_{t \neq t'} \left[ \left| \nabla_\theta L_t(\theta) \cdot \nabla_\theta L_{t'}(\theta) \right| \right]$$
不同任务梯度的 expected inner product，是 activation sparsity $s$ 的函数。

**Effective capacity**：
$$C(s, \epsilon) = \max\left\{ T \in \mathbb{N} : \exists \text{ update rule } \mathcal{U} \text{ s.t. } \forall t \leq T, \, F_t(\theta_T) \leq \epsilon \right\}$$
在给定 sparsity $s$ 和 forgetting bound $\epsilon$ 下的最大可学任务数。

**Per-task information**：
$$B(s) = \mathbb{E}_t \left[ I(f_{\theta_t^*}; \mathcal{D}_t) - I(f_{\theta_{t-1}}; \mathcal{D}_t) \right]$$
学习一个任务带来的 mutual information 增量。

### 证明策略

**P1 (H1) 的证明路径**：

利用 activation pattern 的 overlap 与梯度 inner product 的关系。设任务 $t$ 的激活 pattern 为 $a_t(x) \in \{0,1\}^m$。

在一类模型中（如 ReLU 网络），梯度关于参数 $\theta_j$ 的非零分量仅出现在 $j$ 所连接的 neuron 处于激活状态时。因此：

$$\nabla_\theta L_t \cdot \nabla_\theta L_{t'} \propto \mathbb{E}_{x_t, x_{t'}} \left[ a_t(x_t)^T a_{t'}(x_{t'}) \right]$$

当 activation sparsity 增加时，$\|a_t\|_0$ 和 $\|a_{t'}\|_0$ 均减小。如果 active neurons 是从 $m$ 个 neurons 中均匀采样的（pattern separation 的理想情形），则：

$$\mathbb{E}[a_t^T a_{t'}] = m \cdot (1-s)^2$$

因此 $I(s) \propto (1-s)^2$，关于 $s$ 严格递减。$\square$

注：真实网络中激活 pattern 非均匀，但单调性在 mild conditions 下仍然成立。

**P2 (H2) 的证明路径**：

两个 competing constraints：

1. **Forgetting constraint**：要使 $F_t \leq \epsilon$，需要 $I(s) \leq g(\epsilon, T)$，其中 $g$ 是关于 $\epsilon$ 和 $T$ 的递减函数。由 P1，这要求 $s \geq s_{\min}(\epsilon, T)$。
2. **Capacity constraint**：每个 neuron 在 sparsity $s$ 下只有 $(1-s)$ 的概率被激活。可编码的独立 pattern 数上界为 $\binom{m}{\lfloor(1-s)m\rfloor}$，每个 pattern 承载 $O((1-s)m \log m)$ bits。

在高 $s$（满足 forgetting bound）下，$B(s)$ 被 $(1-s)$ 压缩。因此：

$$C(s, \epsilon) \cdot B(s) \leq \Phi(d, m)$$

其中 $\Phi$ 独立于 $s$。**这是一个 constant——改变 $s$ 只是在 $C$ 和 $B$ 之间重新分配，无法增加乘积。**

**P3 (H3) 的证明路径**：

双 regime 系统的关键 insight：巩固过程不受 online learning 的 interference constraint 限制。

设：
- 快速区 sparsity $s_1$，容量 $C_1 = C(s_1, \epsilon)$（小但够用于短期缓冲）
- 慢速区 sparsity $s_2 < s_1$，per-task capacity $B(s_2) > B(s_1)$
- 巩固过程 $\mathcal{C}$：replay-based，从快速区生成 synthetic data → interleaved training 到慢速区

巩固过程中的 forgetting 可控，因为：
- Replay 同时包含新旧知识的 synthetic examples
- 相当于 multi-task joint training（已知 forgetting 可 bounded）

因此慢速区的 effective capacity 不受 sequential 的 interference bound 限制，其容量由 $C(s_2, \epsilon') \cdot B(s_2)$ 决定（$\epsilon'$ 为巩固阶段的 forgetting tolerance）。

只要 $s_2 < s_1$，慢速区的 $B(s_2) > B(s_1)$，且其容量不被 online sequential learning 的 interference 约束，总 capacity 超过任何单一 regime。$\square$

---

## 与现有工作的关系

### 关键区分

| 现有工作 | 本提议的区别 |
|---------|------------|
| **Knoblauch et al. 2020** (Optimal CL is NP-hard) | 证明**计算复杂度**障碍；我们证明**架构/表征**的必要条件。即使有无限算力，单一 regime 仍有容量天花板 |
| **EWC / GPM / OGD 等正则化方法** | 在单一 regime 内操作。P2 解释为什么它们必然在足够长任务序列后失效 |
| **Shin et al. 2017** (Generative Replay) | CLS 灵感但缺少关键机制：生成器不具备 extreme activation sparsity / pattern separation。本质上是 single-regime + 数据增强 |
| **Stability-Plasticity Dilemma** (非形式化概念) | 我们将这个非形式化 dilemma 形式化为可证明的 capacity bound |
| **CLS-inspired 双系统方法** (各类 dual-memory CL) | 大多使用非参数化 buffer（episodic memory），不是真正的参数化 CLS。本提议要求两个系统都是参数化的，且 activation sparsity 是关键分化维度 |

### 与原始 CLS 理论的对应

| 本提议概念 | 生物 CLS 对应 | 参考文献 |
|-----------|-------------|---------|
| 快速区（高 activation sparsity） | 海马体 DG（~2-5% activation rate） | Leutgeb et al. 2007 |
| 慢速区（低 activation sparsity） | 新皮层（~10-20% activation rate） | — |
| 巩固机制 $\mathcal{C}$ | 睡眠期 hippocampal replay → neocortical plasticity | McClelland et al. 1995 |
| Pattern separation via sparsity | DG granule cell sparse coding | Chawla et al. 2005 |
| Capacity-interference tradeoff | 海马体有限容量 vs 新皮层高容量 | Kumaran et al. 2016 |

关键点：这个对应不是我们选择的设计灵感，而是**从 information-theoretic bound 推导出的唯一结构解**恰好与生物系统同构。这提供了 convergent evidence——进化在生物基质上找到了相同的最优解。

---

## 实验设计

### 原则

实验的目的不是与 SOTA 方法竞争分数，而是**验证理论预测**。因此采用最小化设计，控制变量优先于规模。

### 实验平台

- 模型：小型 Transformer（~50-100M 参数级别，如 nanoGPT 规模）
- 理由：理论验证不需要大规模，控制变量需要大量 runs（≥3 seeds × 多个 sparsity levels × 多个 task sequence lengths）

### Exp 1: Activation Sparsity → Interference 曲线（验证 H1）

**目标**：建立 activation sparsity 与 write interference 的定量关系。

**设计**：
- 固定模型架构和训练预算
- 通过 k-Winners-Take-All (k-WTA) 激活函数控制 activation sparsity：$s = 1 - k/m$
- 扫描 $k/m \in \{0.02, 0.05, 0.10, 0.20, 0.50, 1.0\}$（$s$ 从 0.98 到 0.0）
- 固定 5-task sequence
- 报告：
  - 直接度量 $I(s) = \mathbb{E}_{t \neq t'}[|\nabla L_t \cdot \nabla L_{t'}|]$（梯度 inner product）
  - Average Forgetting $\bar{F}(s)$
  - 两者关于 $s$ 的关系曲线

**预测**：$I(s)$ 和 $\bar{F}(s)$ 关于 $s$ 单调递减，且 $\bar{F} \propto I$ 近似线性。

**可证伪条件**：如果 $I(s)$ 非单调（存在中间 sparsity 反而 interference 更高），则 H1 不成立。

### Exp 2: 单一 Regime 容量天花板（验证 H2）

**目标**：对每个 sparsity level 找到 bounded forgetting 下的最大任务数，验证 $C \cdot B$ 存在不可逾越的上界。

**设计**：
- 对 Exp 1 的每个 sparsity level，逐步增加任务数（$T = 5, 10, 20, 50$）
- 对每个 $(s, T)$ 组合，记录：
  - 是否所有任务 $F_t \leq \epsilon$（$\epsilon$ 预设为 baseline performance 的 10%）
  - 如果否，$C(s, \epsilon) = \max T$ s.t. 条件满足
- Per-task information $B(s)$：用 task-specific evaluation accuracy 作为 proxy
- 绘制 Pareto frontier: $C(s, \epsilon)$ vs $B(s)$

**预测**：
1. 高 $s$：大 $C$ 但小 $B$（能学很多任务但每个任务性能低）
2. 低 $s$：小 $C$ 但大 $B$（每个任务性能高但很快遗忘）
3. $C \cdot B$ 存在上界 $\Phi$，改变 $s$ 只是沿 Pareto frontier 移动

**可证伪条件**：如果存在某个 $s^*$ 使得 $C(s^*) \cdot B(s^*)$ 显著超过其他 sparsity levels（即不存在 tradeoff），则 H2 不成立。

### Exp 3: 双 Regime 突破天花板（验证 H3）

**目标**：最小双 regime 实现，证明其 $C_{\text{dual}}$ 超过任何 $C_{\text{single}}$。

**设计**：
- **快速区**：模型的一部分层使用 k-WTA（$k/m = 0.05$，即 $s_1 = 0.95$）
- **慢速区**：其余层使用标准 activation（$s_2 \approx 0.0$）
- **巩固机制**：每学完 $C_1$ 个任务（快速区容量）后执行巩固——
  1. 用快速区参数为所有已学任务生成 synthetic activations
  2. 以 interleaved training 更新慢速区参数
  3. 快速区参数部分 reset（释放容量）
- **对照**：
  - B0: 标准 dense model，sequential fine-tuning（worst case baseline）
  - B1: 最优单一 regime（从 Exp 2 中选 $C \cdot B$ 最大的 $s^*$）
  - B2: EWC（代表 regularization-based 方法的上界）
  - D1: 双 regime + consolidation（本提议）

**预测**：$C_{\text{D1}} > C_{\text{B1}} \geq C_{\text{B2}} > C_{\text{B0}}$

**可证伪条件**：如果 $C_{\text{D1}} \leq C_{\text{B1}}$（双 regime 不优于最优单一 regime），则 H3 不成立。

---

## 预期贡献

### 理论贡献

1. **Compression-writability bound**：首次将 stability-plasticity dilemma 形式化为 information-theoretic capacity bound
2. **Regime differentiation 必要性**：证明 multi-regime 不是一种设计选择，而是突破 single-regime capacity ceiling 的**唯一结构解**
3. **CLS 的数学基础**：将 CLS 从生物学类比提升为 information-theoretic 必然——进化和数学收敛到相同的解

### 实验贡献

1. **Activation sparsity-interference 定量关系**：首次系统性地建立 $I(s)$ 曲线
2. **单一 regime Pareto frontier**：展示 capacity-richness tradeoff 的具体形态
3. **双 regime 概念验证**：最小化实现证明理论预测的可验证性

### 对 CL 领域的影响

如果 H2 和 H3 成立：
- **所有**不包含 regime differentiation 的 CL 方法都有一个 provable 的容量天花板——这解释了为什么 EWC/replay/GPM 等方法在长序列上逐步退化
- 后续研究的正确方向：不是在单一 regime 内叠加补丁（正则化、replay 调度等），而是设计 regime differentiation + consolidation 机制
- 提供可证伪的 **necessary condition 检验**：一个 CL 方法如果不满足 dual-regime 条件，可以直接预测其长期 capacity ceiling

---

## 风险与缓解

### 风险 1: 形式化证明需要过强假设

P2 的 clean 证明可能需要对模型类（如线性网络、特定激活函数）做强假设。

**缓解**：
- 分层次证明：先在简化模型（线性网络/Hopfield network）上获得 exact result，再通过实验验证 non-linear 模型的 empirical consistency
- 明确区分 "proven bound" 和 "empirically validated conjecture"
- 即使 full generality 的证明未完成，$I(s)$ 曲线和 Pareto frontier 的实验结果本身有独立价值

### 风险 2: 双 regime 优势来自更多参数而非 regime differentiation

双 regime 系统可能因为有效参数更多而表现更好，而非因为 differentiation。

**缓解**：
- 控制总参数量相同（same-shape baseline）
- 额外对照：同参数量但两个区域使用**相同** sparsity level（验证 differentiation 而非 quantity 是关键因素）

### 风险 3: k-WTA 是否是 activation sparsity 的正确实现

k-WTA 是人工约束，真实网络的 activation sparsity 是 emergent property。

**缓解**：
- k-WTA 用于控制实验，建立 causal 关系
- 额外探索 L1 regularization on activations 作为 soft enforcement
- 理论结果不依赖于 k-WTA 的具体实现——依赖于 activation sparsity 的数值

---

## 时间线与里程碑

### Phase 1: 理论建立（核心）

- 形式化 compression-writability bound 的 problem setup
- 在简化模型上证明 P1 和 P2
- 建立 P3 的 proof sketch

### Phase 2: 最小实验验证

- Exp 1: $I(s)$ 曲线
- Exp 2: Single-regime Pareto frontier
- Exp 3: Dual-regime 概念验证

### Phase 3: 推广与完善

- 探索 P2 在更一般模型类上的成立条件
- 分析 optimal $s_1, s_2$ 的理论关系
- 与 scaling laws 的连接：$\Phi(d)$ 如何随 $d$ 增长？

---

## 参考文献

### 持续学习基础
- Kirkpatrick, J., et al. (2017). Overcoming catastrophic forgetting in neural networks. *PNAS*, 114(13), 3521-3526. [EWC]
- Farajtabar, M., et al. (2020). Orthogonal gradient descent for continual learning. *AISTATS 2020*. [OGD]
- Saha, G., et al. (2021). Gradient projection memory for continual learning. *ICLR 2021*. [GPM]
- Knoblauch, J., Husain, H., & Diethe, T. (2020). Optimal continual learning has perfect memory and is NP-hard. *ICML 2020*.
- Shin, H., et al. (2017). Continual learning with deep generative replay. *NeurIPS 2017*.

### CLS 理论
- McClelland, J.L., McNaughton, B.L., & O'Reilly, R.C. (1995). Why there are complementary learning systems in the hippocampus and neocortex. *Psychological Review*, 102(3), 419-457.
- Kumaran, D., Hassabis, D., & McClelland, J.L. (2016). What learning systems do intelligent agents need? Complementary learning systems theory updated. *Trends in Cognitive Sciences*, 20(7), 512-534.

### 海马体神经科学
- Leutgeb, J.K., et al. (2007). Pattern separation in the dentate gyrus and CA3 of the hippocampus. *Science*, 315(5814), 961-966.
- Chawla, M.K., et al. (2005). Sparse, environmentally selective expression of Arc RNA in the upper blade of the rodent fascia dentata. *Hippocampus*, 15(5), 579-586.
- Amaral, D.G., Ishizuka, N., & Claiborne, B. (1990). Neurons, numbers and the hippocampal network. *Progress in Brain Research*, 83, 1-11.

### 稀疏性与表征理论
- Frankle, J., & Carlin, M. (2019). The lottery ticket hypothesis. *ICLR 2019*.
- Elhage, N., et al. (2022). Toy models of superposition. *Anthropic research*.
- Tsodyks, M.V., & Feigelman, M.V. (1988). The enhanced storage capacity in neural networks with low activity level. *Europhysics Letters*, 6(2), 101-105.

### 信息论基础
- Cover, T.M., & Thomas, J.A. (2006). *Elements of Information Theory*. Wiley.

---

## 文档元信息

- **创建时间**：2026-02-24
- **前序文档**：`docs/zh_CN/processing/20260224-0249.md`（第一性原理讨论记录）
- **关联提议**：P01-P04（本提议解释为什么它们有 fundamental limitations）
- **状态**：初稿
