# Proposal 05: Compression-Writability Bound — 持续学习的容量天花板与突破条件

## 目标

从第一性原理出发，形式化参数化系统中 compression 与 writability 的根本对抗关系，证明 single-regime 系统存在不可逾越的容量天花板，并展示 dual-regime architecture 可以突破该天花板。通过最小实验在 deep network 中验证理论预测。

核心定位：
- **不是提出新的 CL 方法**——而是建立 capacity bound
- Single-regime 系统（包括 EWC/GPM/replay 等）有 **provable 的容量天花板**——这解释了它们在长序列上的退化
- Dual-regime architecture 是突破该天花板的 **充分条件**（sufficient condition）
- 理论在 restricted model class 上严格证明，在 deep network 上通过实验验证为 empirical conjecture

---

## 起源与动机

### 从 P01-P04 的教训出发

P01-P04 共享一个根本缺陷：**缺少理论根基**。

- P01 (ablation) 和 P02 (SOTA sparse conversion)：围绕 weight sparsity 假说设计，但该假说在固定架构下 trivially true（详见 `20260224-0007.md`）
- P03 (nanoGPT pretrain)：控制变量最干净，但外推性受限于规模
- P04 (CDCL)：不改架构仅改 update rule，本质上是在 dense 全局参数空间做约束——根据本提议的理论，这类方法有 provable 的容量天花板
- P03-2 (interference phase diagram)：理论野心最大但操作化困难

**核心问题**：这些提议都在回答"哪种方法更好"，而没有回答"持续学习的容量极限在哪里、能否被突破"。

### 从 processing doc (20260224-0249) 的理论演进

本提议直接构建在以下已确立的论证链上：

1. **三个本质问题**：定位（where to write）、容量（how much room）、检索（how to recall）
2. **Superposition 是问题根源**：高压缩（重度 superposition）提供容量但摧毁可写性
3. **CLS 的正确类比**：海马体 ≠ RAG，而是第二参数化系统——整个 CLS 过程纯参数化
4. **Activation sparsity 是关键**：海马体通过极端 activation sparsity（DG ~2-5%）实现 pattern separation，而非 weight sparsity
5. **研究问题转向**：从"是否需要 weight sparsity"到"activation sparsity 如何决定持续学习的容量极限"

本提议的目标是将第 5 点**形式化为可证明的 capacity bound**，并通过实验验证。

---

## 研究问题

1. Activation sparsity 与 write interference 之间是否存在可证明的单调关系？
2. 在固定 activation sparsity 的 single-regime 系统中，bounded forgetting 下的 capacity 是否存在 provable 上界（$C \cdot B$ bound）？
3. Dual-regime architecture 是否能 provably 突破该上界？

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

**Per-task richness**：
$$B(s) = \mathbb{E}_t \left[ L_t(\theta_{t-1}) - L_t(\theta_t^*) \right]$$
学习一个任务带来的 loss reduction（即单任务可达到的学习效果）。

注：此前版本使用 mutual information 增量定义 $B(s)$，但该定义的可操作性差（$I(f_{\theta}; \mathcal{D}_t)$ 的计算在 deep network 中不 tractable）。改用 loss reduction 作为 proxy，与实验中的 task-specific evaluation accuracy 直接对应，且在 Hopfield network 上可精确关联到 pattern 容量。

### 证明策略：分层次建立

本提议的理论结果按模型类分三个层次。**核心贡献是 Layer 1 的严格证明**，Layer 2 和 3 通过实验验证。

#### Layer 1: Hopfield Network 上的严格证明（主定理）

选择 Hopfield network 作为理论基础，原因：
1. 稀疏编码容量理论已有严格结果可直接利用（Tsodyks & Feigelman, 1988）
2. 存储与检索有精确数学描述，$C$ 和 $B$ 均可 closed-form 定义
3. Sequential pattern storage 是 CL 的自然简化模型

**已有基础**：Tsodyks & Feigelman (1988) 证明了稀疏 Hopfield network 的最大存储容量：

$$p_{\max} \propto \frac{a}{\ln(1/a)} \cdot N$$

其中 $a$ 为 activity level（$a = 1 - s$），$N$ 为 neuron 数。该结果意味着：
- 当 $a \to 0$（极端稀疏），$p_{\max}$ 增长但每个 pattern 的信息量 $\propto a \log(1/a) \cdot N$ bits 减小
- 存在 total information throughput 的 bound

**本提议在此基础上需要证明的新结果**：

**Theorem 1 (H1, Interference-Sparsity Monotonicity)**：

在 Hopfield network 中，sequential pattern storage 的 write interference（定义为新 pattern 对已存 pattern 的 overlap corruption）是 activity level $a$ 的严格递增函数（即 sparsity $s$ 的严格递减函数）。

证明路径：Hopfield 的 Hebbian 更新 $\Delta W = \frac{1}{N} \xi^t (\xi^t)^T$ 对已存 pattern $\xi^{t'}$ 的干扰为 $\frac{1}{N} \xi^{t'} \cdot \xi^t$。对于 activity level $a$ 的稀疏 binary pattern：

$$\mathbb{E}[\xi_i^t \xi_i^{t'}] = a^2, \quad \text{Var}[\xi_i^t \xi_i^{t'}] = a^2(1-a^2)$$

干扰 noise 的方差 $\propto p \cdot a^2(1-a^2) / N$，在 $a \ll 1$ 时 $\approx p \cdot a^2 / N$，关于 $a$ 严格递增。$\square$

**Theorem 2 (H2, Single-Regime Capacity Bound)**：

在 Hopfield network 中，activity level 固定为 $a$ 时，bounded retrieval error（$\leq \epsilon$）下的最大 pattern 数 $C(a, \epsilon)$ 与每 pattern 信息量 $B(a)$ 满足：

$$C(a, \epsilon) \cdot B(a) \leq \Phi(N)$$

其中 $\Phi(N)$ 独立于 $a$。

证明路径：
1. 由 Tsodyks & Feigelman, $C(a, \epsilon) \leq \frac{\alpha(\epsilon) \cdot a}{\ln(1/a)} \cdot N$，其中 $\alpha(\epsilon)$ 仅依赖于 error tolerance
2. 每 pattern 信息量 $B(a) = N \cdot [a \log(1/a) + (1-a)\log(1/(1-a))]$（binary pattern 的 entropy）
3. 当 $a \ll 1$，$B(a) \approx N \cdot a \log(1/a)$
4. 因此 $C \cdot B \leq \alpha(\epsilon) \cdot a / \ln(1/a) \cdot N \cdot N \cdot a \ln(1/a) = \alpha(\epsilon) \cdot a^2 \cdot N^2$

注：上述推导表明 $C \cdot B$ 在 Hopfield 中不是严格 constant，而是关于 $a$ 有弱依赖（$\propto a^2$）。这意味着**极端稀疏并非最优**——存在一个最大化 $C \cdot B$ 的 optimal $a^*$。但关键点不变：**给定任何固定 $a$，$C$ 和 $B$ 之间存在 tradeoff，且 $C \cdot B$ 有上界 $\Phi(N)$**。

需要进一步精确化的地方：
- $\alpha(\epsilon)$ 的具体形式
- Bound 的 tightness（是否可达？）
- 从 binary Hopfield 到 continuous-valued modern Hopfield 的推广

**Proposition 1 (H3, Dual-Regime Capacity Advantage)**：

存在一个双 regime Hopfield 系统，其 effective capacity 超过任何 single-regime 系统。

证明思路（constructive）：
- 快速区：activity level $a_1$（高稀疏），容量 $C_1$，用于 sequential 暂存
- 慢速区：activity level $a_2 > a_1$，per-pattern 信息量 $B(a_2) > B(a_1)$
- 巩固：每 $C_1$ 个 pattern 后，用 pseudo-rehearsal 将快速区 pattern 同时写入慢速区（joint storage，非 sequential）
- Joint storage 的干扰可控：$C_1$ 个 pattern 同时写入等价于 batch Hebbian update，不受 sequential interference 约束
- 快速区 reset 后释放容量，重复循环
- Total capacity = $\lfloor T / C_1 \rfloor \cdot C_1$ 个 patterns stored in slow region with bounded error

关键假设：巩固过程中 joint storage 的 forgetting 可 bounded。这在 Hopfield network 中对应于经典的 batch 容量结果（$p_{\max} \propto N$ for standard Hopfield），因此成立。

注：此处证明的是 **sufficiency**（dual regime 能 exceed single regime bound），不是 necessity（dual regime 是唯一方式）。

#### Layer 2: Linear Network 上的推广（扩展定理）

将 Layer 1 的结果推广到 linear network，利用 activation pattern 的 subspace 结构。

状态：待完成。预期可通过 gradient subspace overlap 分析获得类似的 $C \cdot B$ bound。

#### Layer 3: Deep Nonlinear Network 上的经验验证（Conjecture）

**Conjecture**：Layer 1 和 2 的 qualitative 结论——single-regime $C \cdot B$ bound 存在且 dual-regime 可突破——在 deep Transformer 中仍然成立。

验证方式：Exp 1 和 Exp 2（见实验设计节）。

注：不声称 Hopfield 的 quantitative bound 直接适用于 Transformer。Claim 的范围是 **qualitative structure**（tradeoff 的存在性和 dual-regime 的优越性），不是 exact scaling。

---

## 与现有工作的关系

### 关键区分

| 现有工作 | 本提议的区别 |
|---------|------------|
| **Knoblauch et al. 2020** (Optimal CL is NP-hard) | 证明**计算复杂度**障碍；我们证明**容量/表征**层面的 bound。二者互补：即使算力无限，single-regime 仍有容量天花板 |
| **Tsodyks & Feigelman 1988** (Sparse Hopfield capacity) | 证明了稀疏编码提升 Hopfield 存储容量。**本提议直接建立在此结果上**，将其重新 frame 为 CL 语境下的 $C \cdot B$ tradeoff bound |
| **EWC / GPM / OGD 等正则化方法** | 在单一 regime 内操作。Theorem 2 解释为什么它们必然在足够长任务序列后失效——受 single-regime capacity ceiling 约束 |
| **Shin et al. 2017** (Generative Replay) | CLS 灵感但 generator 与 learner 使用相同的 activation regime。本质上是 single-regime + 数据增强，不具备 regime differentiation |
| **Stability-Plasticity Dilemma** (非形式化概念) | 我们将这个非形式化 dilemma 形式化为可证明的 capacity bound |
| **CLS-inspired 双系统方法** (各类 dual-memory CL) | 大多使用非参数化 buffer（episodic memory），不是真正的参数化 CLS。本提议要求两个系统都是参数化的，且 activation sparsity 是关键分化维度 |

### 需要讨论的重要相关工作

**Mixture of Experts (MoE)**：MoE 通过 routing 实现 **conditional activation sparsity**——不同输入激活不同 expert subsets。这是否已经构成了一种 regime differentiation？

初步分析：
- MoE 的 sparsity 是 **input-conditional** 的（不同输入激活不同 experts），而本提议的 dual-regime 是 **function-conditional** 的（快速区 vs 慢速区有不同的 sparsity level 和学习动力学）
- MoE 缺少 consolidation 机制——没有从 sparse experts 到 dense shared representation 的知识转移
- 但如果 MoE 在 CL 中展现出 capacity 优势，这将支持 activation sparsity 理论的核心预测
- **实验建议**：在 Exp 2 中加入 MoE baseline，检查其 $C \cdot B$ 是否超过 single-regime ceiling

**Progressive Neural Networks (Rusu et al. 2016)**：通过增长架构避免遗忘。
- 有效 capacity 随参数量线性增长——绕过而非突破 $C \cdot B$ bound（因为 $\Phi(d)$ 随 $d$ 增长）
- 本提议的 bound 假设 $d$ 固定。Progressive Networks 属于 "增加 $\Phi$" 的路线，与 "在固定 $\Phi$ 下突破 single-regime ceiling" 是不同的问题

### 与原始 CLS 理论的对应

| 本提议概念 | 生物 CLS 对应 | 参考文献 |
|-----------|-------------|---------|
| 快速区（高 activation sparsity） | 海马体 DG（~2-5% activation rate） | Leutgeb et al. 2007 |
| 慢速区（低 activation sparsity） | 新皮层（~10-20% activation rate） | — |
| 巩固机制 $\mathcal{C}$ | 睡眠期 hippocampal replay → neocortical plasticity | McClelland et al. 1995 |
| Pattern separation via sparsity | DG granule cell sparse coding | Chawla et al. 2005 |
| Capacity-interference tradeoff | 海马体有限容量 vs 新皮层高容量 | Kumaran et al. 2016 |

**关于 convergent evidence 的诚实声明**：本提议的理论构建过程受 CLS 理论启发（见 `20260224-0249.md`）。因此，理论结论与 CLS 的对应**不能被视为独立的 convergent evidence**。但理论的核心结果（$C \cdot B$ bound）不依赖于 CLS 类比——它从 activation sparsity 与 interference 的数学关系直接推导，CLS 对应只是事后的 interpretive framework。

---

## 实验设计

### 原则

实验的目的不是与 SOTA 方法竞争分数，而是**验证理论预测**。因此采用最小化设计，控制变量优先于规模。

### 实验平台

- 模型：小型 Transformer（~50-100M 参数级别，如 nanoGPT 规模）
- 理由：理论验证不需要大规模，控制变量需要大量 runs（≥3 seeds × 多个 sparsity levels × 多个 task sequence lengths）

### Exp 1: Activation Sparsity → Interference 曲线（验证 Theorem 1 在 deep network 中的成立性）

**目标**：在 Transformer 中建立 activation sparsity 与 write interference 的定量关系，验证 Hopfield 上证明的单调性是否推广到 deep network。

**设计**：
- 固定模型架构和训练预算
- Activation sparsity 控制：主方案使用 k-Winners-Take-All (k-WTA)；辅助方案使用 L1 regularization on activations 作为 robustness check（排除 k-WTA artifact）
- 扫描 $k/m \in \{0.02, 0.05, 0.10, 0.20, 0.50, 1.0\}$（$s$ 从 0.98 到 0.0）
- 固定 5-task sequence
- 报告：
  - 直接度量 $I(s) = \mathbb{E}_{t \neq t'}[|\nabla L_t \cdot \nabla L_{t'}|]$（梯度 inner product）
  - Average Forgetting $\bar{F}(s)$
  - 两者关于 $s$ 的关系曲线
  - k-WTA 与 L1 两种实现的一致性

**预测**：$I(s)$ 和 $\bar{F}(s)$ 关于 $s$ 单调递减，且 $\bar{F} \propto I$ 近似线性。

**可证伪条件**：如果 $I(s)$ 非单调（存在中间 sparsity 反而 interference 更高），则 Theorem 1 不推广到 deep network。

### Exp 2: 单一 Regime 容量天花板（验证 Theorem 2 在 deep network 中的成立性）

**目标**：对每个 sparsity level 找到 bounded forgetting 下的最大任务数，验证 $C \cdot B$ tradeoff 在 Transformer 中存在。

**设计**：
- 对 Exp 1 的每个 sparsity level，逐步增加任务数（$T = 5, 10, 20, 50$）
- 对每个 $(s, T)$ 组合，记录：
  - 是否所有任务 $F_t \leq \epsilon$（$\epsilon$ 预设为 baseline performance 的 10%）
  - 如果否，$C(s, \epsilon) = \max T$ s.t. 条件满足
- Per-task richness $B(s)$：用 task-specific evaluation loss reduction（$L_t(\theta_{t-1}) - L_t(\theta_t^*)$）度量
- 绘制 Pareto frontier: $C(s, \epsilon)$ vs $B(s)$
- 计算 $C \cdot B$ 作为 $s$ 的函数，检查是否存在上界

**预测**：
1. 高 $s$：大 $C$ 但小 $B$（能学很多任务但每个任务学习效果差）
2. 低 $s$：小 $C$ 但大 $B$（每个任务学习效果好但很快遗忘）
3. $C \cdot B$ 存在上界（可能在某个 $s^*$ 取最大值），改变 $s$ 无法突破该上界

**可证伪条件**：如果 $C \cdot B$ 随 $s$ 单调递增或递减（无 tradeoff），或不同 sparsity level 的 $C \cdot B$ 差异极大且无收敛趋势，则 Theorem 2 的 qualitative 结论不推广到 deep network。

### Exp 3: 双 Regime Sanity Check（初步验证 H3）

**目标**：最小化验证 dual-regime 能否在 deep network 中展示出超越 single-regime 的容量优势。本实验**不追求最优实现**，仅验证理论预测的方向性。

**设计**：
- **快速区**：模型的一部分层使用 k-WTA（$k/m = 0.05$，即 $s_1 = 0.95$）
- **慢速区**：其余层使用标准 activation（$s_2 \approx 0.0$）
- **巩固机制**：简单的 interleaved replay（从快速区缓存的 logits 进行知识蒸馏到慢速区）
- **对照**：
  - B0: 标准 dense baseline
  - B1: 最优单一 regime（从 Exp 2 中选 $C \cdot B$ 最大的 $s^*$）
  - B1-same: 同参数量但两个区域使用**相同** sparsity level（排除"参数量分配"混淆）

**预测**：$C_{\text{dual}} > C_{\text{B1}}$

**可证伪条件**：如果 $C_{\text{dual}} \leq C_{\text{B1}}$，则 H3 在 deep network 中不成立，或实现方案需根本性改进。

**scope 限制**：Exp 3 是 proof-of-concept，不追求与 CL SOTA 竞争。完整的 dual-regime 系统（最优巩固调度、自适应 sparsity、scaling 分析）留给 future work。

---

## 预期贡献

### 理论贡献

1. **Compression-writability bound**：首次将 stability-plasticity dilemma 形式化为 provable capacity bound（Hopfield 上 exact，deep network 上 empirically validated conjecture）
2. **Single-regime capacity ceiling**：证明在固定 activation sparsity 的系统中，$C$ 和 $B$ 之间存在不可逾越的 tradeoff
3. **Dual-regime capacity advantage**：证明 dual-regime 是突破 single-regime ceiling 的**充分条件**

注：本提议**不 claim necessity**——即不声称 dual-regime 是突破 ceiling 的唯一方式。其他可能的路径（如 MoE 的 conditional sparsity、参数增长型方法）需要另行分析。

### 实验贡献

1. **Activation sparsity-interference 定量关系**：首次系统性地建立 $I(s)$ 曲线
2. **单一 regime Pareto frontier**：展示 capacity-richness tradeoff 的具体形态
3. **双 regime sanity check**：最小化实现初步验证理论预测的方向性

### 对 CL 领域的影响

如果 Theorem 2 和 Proposition 1 成立：
- 提供了 **定量解释** 为什么 EWC/GPM/replay 等 single-regime 方法在长序列上退化——它们受 $C \cdot B$ bound 约束
- 指出一个被忽视的研究方向：**activation sparsity 的 regime differentiation**（而非仅在单一 regime 内优化 update rule）
- 提供 **可证伪的预测**：对任何 single-regime CL 方法，可以通过测量其 activation sparsity 预测其 capacity ceiling

---

## 风险与缓解

### 风险 1: Hopfield 证明的 relevance

Reviewer 可能质疑 Hopfield network 上的结果对 modern Transformer 的 relevance。

**缓解**：
- Exp 1 和 Exp 2 直接在 Transformer 上验证 qualitative 预测
- 明确论文的 claim 结构：Hopfield 上 exact theorem + deep network 上 empirical conjecture
- 类比先例：Hopfield network 的容量理论（Cover 1965, Tsodyks & Feigelman 1988）至今仍是理解联想记忆的基础工具，尽管现代网络远比 Hopfield 复杂

### 风险 2: Theorem 2 中 $C \cdot B$ bound 的 tightness

$C \cdot B$ 在 Hopfield 中对 $a$ 有弱依赖（$\propto a^2$），不是严格 constant。这可能削弱 "tradeoff" 的叙事力度。

**缓解**：
- 诚实报告 bound 的具体形式，不假装它是 constant
- 核心 claim 调整为：**存在 optimal $a^*$，且 $C(a^*) \cdot B(a^*)$ 有上界**——即无法通过调 $a$ 无限提升 throughput
- 在实验中直接画 $C \cdot B$ vs $s$ 曲线，展示其形态

### 风险 3: k-WTA artifact

k-WTA 的 hard constraint 可能引入训练不稳定，使实验结果反映 k-WTA 的 artifact 而非 activation sparsity 的本质。

**缓解**：
- 并行使用 L1 regularization on activations 作为 soft enforcement
- 如果两种实现的 $I(s)$ 曲线 qualitatively 一致，则 artifact 风险低
- 如果不一致，需要分析不一致的来源，可能需要第三种实现方式

### 风险 4: Exp 3 的 dual-regime 优势来自更多参数而非 regime differentiation

**缓解**：
- 控制总参数量相同（same-shape baseline）
- 加入 B1-same 对照：同参数量但两个区域使用**相同** sparsity level
- 如果 B1-same ≈ dual-regime，则优势来自参数分配而非 differentiation，H3 需重新审视

---

## 时间线与里程碑

### Phase 1: 理论建立（核心，决定论文成败）

- Hopfield network 上 Theorem 1 和 Theorem 2 的严格证明
- Proposition 1 的 constructive proof
- 与 Tsodyks & Feigelman (1988) 结果的精确对接
- 明确 bound 的 tightness 和适用范围

### Phase 2: 实验验证

- Exp 1: $I(s)$ 曲线（验证 Theorem 1 推广性）
- Exp 2: Single-regime Pareto frontier（验证 Theorem 2 推广性）
- Exp 3: Dual-regime sanity check（验证 Proposition 1 方向性）

### Go/No-Go 决策门槛

**Go（继续投入）**：
- Hopfield 上的 Theorem 1 和 2 证明 clean
- Exp 1 和 2 的结果 qualitatively 支持理论预测（单调性成立、tradeoff 存在）

**No-Go（降级或转向）**：
- Hopfield 证明需要过强假设导致结果 trivial
- Exp 1 中 $I(s)$ 非单调，或 Exp 2 中 $C \cdot B$ 无收敛趋势

---

## Future Work

以下方向在本提议中**不涉及**，但由理论结果自然引出：

1. **完整的参数化 CLS 系统构建**：最优巩固调度（何时触发、replay 多少）、自适应 sparsity level、快速区容量管理。这是一个独立的系统工程问题。

2. **$\Phi(d)$ 的 scaling analysis**：capacity bound 如何随模型规模 $d$ 增长？是否存在 scaling law $\Phi(d) \propto d^\alpha$？这连接到 LLM scaling laws 的研究。

3. **MoE 作为 conditional sparsity 的分析**：MoE 的 routing 机制是否等价于某种 regime differentiation？其 $C \cdot B$ 行为如何？

4. **Layer 2 推广**：在 linear network 上的严格证明，bridging Hopfield 和 deep network。

5. **Optimal $a_1, a_2$ 的理论分析**：快速区和慢速区的最优 activity level 关系。

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
- Tsodyks, M.V., & Feigelman, M.V. (1988). The enhanced storage capacity in neural networks with low activity level. *Europhysics Letters*, 6(2), 101-105. [**本提议 Theorem 1-2 的直接基础**]
- Frankle, J., & Carlin, M. (2019). The lottery ticket hypothesis. *ICLR 2019*.
- Elhage, N., et al. (2022). Toy models of superposition. *Anthropic research*.

### 架构相关
- Rusu, A.A., et al. (2016). Progressive neural networks. *arXiv:1606.04671*. [参数增长型 CL]
- Shazeer, N., et al. (2017). Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. *ICLR 2017*. [MoE / conditional sparsity]
- Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch Transformers: Scaling to trillion parameter models with simple and efficient sparsity. *JMLR*. [Sparse MoE in Transformers]

### 信息论基础
- Cover, T.M., & Thomas, J.A. (2006). *Elements of Information Theory*. Wiley.

---

## 论文结构概览

```
1. Introduction: stability-plasticity dilemma 缺乏形式化 → 我们提供 capacity bound
2. Preliminaries: activation sparsity, write interference, forgetting 的形式化定义
3. Theory (核心贡献):
   3.1 Theorem 1: I(s) monotonically decreasing (Hopfield, exact)
   3.2 Theorem 2: Single-regime C·B bound (Hopfield, exact)
   3.3 Proposition 1: Dual-regime exceeds bound (constructive)
   3.4 Conjecture: qualitative structure extends to deep networks
4. Experiments (验证):
   4.1 Exp 1: I(s) curve in Transformers → validates Theorem 1
   4.2 Exp 2: Pareto frontier → validates Theorem 2
   4.3 Exp 3: Dual-regime sanity check → supports Proposition 1
5. Discussion: CLS 对应、现有方法的 ceiling 解释、limitations
6. Future Work: 完整 dual-regime 系统、scaling analysis、MoE 分析
```

---

## 文档元信息

- **创建时间**：2026-02-24
- **最后修改**：2026-02-24（基于第一性原理评审的重大修订）
- **前序文档**：`docs/zh_CN/processing/20260224-0249.md`（第一性原理讨论记录）
- **关联提议**：P01-P04（本提议解释为什么它们有 fundamental limitations）
- **状态**：修订稿（v2）
- **主要修订内容**：
  1. 放弃 "必要条件" 措辞 → 改为 capacity ceiling + sufficiency
  2. 理论框架改为分层证明（Hopfield exact → deep network conjecture）
  3. $B(s)$ 定义从 mutual information 改为 loss reduction（可操作性）
  4. Exp 3 从完整系统构建缩减为 minimal sanity check
  5. 补充 MoE、Progressive Networks 的讨论
  6. 移除 convergent evidence 的过度声明
  7. 加入论文结构概览
