# Proposal 03: Compression-Writability Bound

## 研究动机

我想检验一个工作假设：**只使用单一激活模式（single-regime）的持续学习系统，可能存在学习能力边界；而引入两套不同稀疏度的子系统（类比海马体 + 新皮层）或许能缓解这一边界。**

初步的思路是先在 Hopfield 网络上尝试推导可检验的理论结果，再到 Transformer 上做定性验证，看结论是否仍大体成立。

### 研究背景与关键假设

据我目前的理解，持续学习的核心挑战可以从三个角度来看：**写到哪**（定位）、**放得下多少**（容量）、**怎么找回来**（检索）。以下是我初步形成的几个判断，还需要进一步文献验证：

1. **Superposition 可能是灾难性遗忘的重要机制之一**：模型把多个概念压缩编码到同一组参数里（superposition），压缩率越高，塞得越多但也越难安全写入新东西
2. CLS（互补学习系统）里的海马体不是 RAG 那种外挂存储，而是**第二套参数化系统**——整个过程都在参数空间里完成
3. **本 proposal 聚焦于 activation sparsity**：海马体通过极端的 activation sparsity（DG 只激活 2-5% 的神经元）实现 pattern separation。这促使我思考：activation sparsity 是否以及如何影响持续学习的容量上限？

### 三个研究问题

1. Activation sparsity 和写入干扰之间是不是单调关系？（越稀疏干扰越小？）
2. 如果一个系统只用一种固定的 activation sparsity（single-regime），它能学的任务数有没有上限？
3. 两套不同稀疏度的系统（dual-regime）加上巩固机制，能不能提升这个上限？

## 假设

### H1: 越稀疏，干扰越小

**大白话**：如果两个任务激活的神经元几乎不重叠（高 activation sparsity → pattern separation），学新任务几乎不会破坏旧任务的表征。

形式化：$I(s)$ 是 sparsity 为 $s$ 时，不同任务梯度的 expected inner product：

$$\frac{\partial I}{\partial s} < 0$$

**生物依据**：海马体 DG 只激活 2-5% 的神经元，就是为了把不同记忆隔开。

### H2: 单系统可能存在容量边界

用一种固定的 activation sparsity，能学的任务数 $C$ 和每个任务学到的信息量 $B$ 之间有个 tradeoff，两者之积有上界：

$$C(s, \epsilon) \cdot B(s) \leq \Phi(d)$$

**白话解释**——这是一个两难困境：

- 稀疏度拉到极高 → 干扰小，能学很多任务，但每个任务学到的东西很少（因为参与编码的神经元太少）
- 稀疏度拉低 → 每个任务学得很好，但任务一多就互相覆盖
- **在本文设定下，预计总信息吞吐量 $C \cdot B$ 受一个边界 $\Phi(d)$ 约束**

### H3: 双系统有望缓解该边界

一个系统有两套不同 sparsity 的子系统（$s_1 > s_2$），加上一个巩固机制 $\mathcal{C}$，理论上可能超过单系统的上限：

$$C_{\text{dual}}(\epsilon) > \max_s C_{\text{single}}(s, \epsilon)$$

**工作原理**：

1. **快速区**（高稀疏 $s_1$）：低干扰，快速接收新任务，但容量有限
2. **巩固**：定期把快速区的知识"搬"到慢速区（低稀疏 $s_2$），后者压缩效率高，单位参数存得更多
3. **释放**：搬完后快速区 reset，腾出空间接新任务
4. **关键**：巩固是 batch 操作（interleaved replay），不是 online learning，所以干扰可控
5. **效果**：整个系统用慢速区的高容量存储，用快速区的低干扰接收，两者取长补短

注意：这里将 dual-regime 作为**候选充分条件**讨论，不主张其为**必要条件**（并非唯一可行路径）。

## 方案

### 理论框架

#### 核心定义

- **模型**：$f_\theta: \mathcal{X} \to \mathcal{Y}$，$d$ 个参数，隐层表征 $h(x;\theta) \in \mathbb{R}^m$
- **Activation sparsity**：$s(\theta) = 1 - \mathbb{E}_x[\|h(x;\theta)\|_0 / m]$（直觉：$s=0.95$ 表示平均只有 5% 的神经元被激活）
- **任务序列**：$\{(\mathcal{D}_t, L_t)\}_{t=1}^T$
- **遗忘**：$F_t(\theta_T) = L_t(\theta_T) - L_t(\theta_t^*)$（学完所有任务后，任务 $t$ 的 loss 比刚学完时涨了多少）
- **Bounded forgetting**：所有任务的遗忘都不超过 $\epsilon$
- **写入干扰**：$I(s) = \mathbb{E}_{t \neq t'}[|\nabla L_t \cdot \nabla L_{t'}|]$（不同任务梯度的内积——越大说明互相干扰越严重）
- **容量**：$C(s, \epsilon)$ = 在 sparsity $s$、遗忘上界 $\epsilon$ 下能学的最大任务数
- **每任务丰富度**：$B(s) = \mathbb{E}_t[L_t(\theta_{t-1}) - L_t(\theta_t^*)]$（学一个任务能降多少 loss）

注：$B(s)$ 之前用互信息定义，但那玩意儿在深度网络上算不出来。改用 loss reduction 更好操作，而且在 Hopfield 上可以精确关联到 pattern 容量。

#### 证明分三层

**本文优先聚焦第一层（Hopfield 上的理论推导），后两层以实验验证为主。**

##### 第一层：在 Hopfield 网络上进行理论推导

为什么选 Hopfield：

1. 稀疏编码容量有现成的严格结果可以用（Tsodyks & Feigelman 1988）
2. 存储和检索有精确数学描述，$C$ 和 $B$ 都能算 closed-form
3. 顺序存 pattern 天然就是持续学习的简化版

**已有结论**（Tsodyks & Feigelman 1988）：稀疏 Hopfield 最大存储容量：

$$p_{\max} \propto \frac{a}{\ln(1/a)} \cdot N$$

其中 $a = 1 - s$ 是 activity level，$N$ 是神经元数。也就是说：$a$ 越小（越稀疏），能存的 pattern 越多，但每个 pattern 携带的信息越少。

**在此基础上，我想尝试检验以下命题**：

**命题 1（待证，对应 H1）**：写入干扰关于 $a$ 严格递增（sparsity 越高干扰越小）。

初步分析表明证明路径可能可行：Hebbian 更新 $\Delta W = \frac{1}{N}\xi^t(\xi^t)^T$ 对已有 pattern $\xi^{t'}$ 的干扰就是 $\frac{1}{N}\xi^{t'} \cdot \xi^t$。对 activity level 为 $a$ 的稀疏 binary pattern：

$$\mathbb{E}[\xi_i^t \xi_i^{t'}] = a^2, \quad \text{Var}[\xi_i^t \xi_i^{t'}] = a^2(1-a^2)$$

干扰 noise 的方差 $\propto p \cdot a^2 / N$（$a \ll 1$ 时），关于 $a$ 严格递增（待严格证明）。

**命题 2（待证，对应 H2）**：单系统的 $C \cdot B$ 存在上界。

证明路径：

1. 已知 $C(a, \epsilon) \leq \frac{\alpha(\epsilon) \cdot a}{\ln(1/a)} \cdot N$
2. 每 pattern 信息量 $B(a) = N \cdot [a \log(1/a) + (1-a)\log(1/(1-a))]$
3. $a \ll 1$ 时 $B(a) \approx N \cdot a \log(1/a)$
4. 所以 $C \cdot B \leq \alpha(\epsilon) \cdot a^2 \cdot N^2$

**当前推导显示**：$C \cdot B$ 在 Hopfield 里不是严格常数，对 $a$ 有弱依赖（$\propto a^2$）。也就是说极端稀疏未必最优——可能存在一个最优 $a^*$。因此更稳妥的说法是：**对给定设定，$C$ 和 $B$ 之间存在 tradeoff，且 $C \cdot B$ 受上界约束**。

还需要进一步弄清楚的：$\alpha(\epsilon)$ 的具体形式、bound 能不能达到、怎么从 binary Hopfield 推广到 continuous-valued 版本。

**命题 3（待证，对应 H3）**：存在一个双系统 Hopfield 方案，其容量可超过对应单系统方案。

构造性证明：

- 快速区：高稀疏（$a_1$ 小），用于顺序暂存
- 慢速区：低稀疏（$a_2 > a_1$），每 pattern 信息量更大
- 每 $C_1$ 个 pattern 后，用 pseudo-rehearsal 把快速区内容 batch 写入慢速区
- Batch 写入 = 一次性 Hebbian update，不受顺序干扰约束
- 快速区 reset，继续接新任务
- 总容量 = 循环次数 × $C_1$，全部存在慢速区里

##### 第二层：Linear Network（待做）

把第一层的结论推广到线性网络。预期通过分析梯度子空间的重叠能得到类似的 $C \cdot B$ bound。

##### 第三层：Deep Nonlinear Network（猜想 + 实验验证）

**猜想**：第一层和第二层的定性结论（单系统可能存在边界、双系统可能缓解该边界）在深度 Transformer 里仍然成立。

需要强调的是，这里不主张 Hopfield 的具体数值 bound 能直接用到 Transformer 上，而是更谨慎地关注**定性结构**（tradeoff 是否存在、dual-regime 是否可能有优势）。

### 跟现有工作的关系

| 已有工作                                                | 本 proposal 想做的有什么不同                                                                                                     |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------- |
| **Knoblauch et al. 2020** 证明最优持续学习是 NP-hard 的 | 他们讨论的是**算力**限制，这里关注的是**容量/表征**限制；两者可能互补                                                              |
| **Tsodyks & Feigelman 1988** 稀疏 Hopfield 容量理论     | 想尝试在该结果基础上，将其重述为持续学习语境下的 $C \cdot B$ tradeoff                                                            |
| **EWC / GPM / OGD 这些正则化方法**                      | 都是在一套系统内操作。若命题 2 成立，可能为它们在长任务序列中退化提供一种解释                                                     |
| **Shin et al. 2017 生成式 replay**                      | 虽然受 CLS 启发，但 generator 和 learner 用的是同一种 activation regime，本质还是 single-regime + 数据增强                       |
| **Stability-Plasticity Dilemma**                        | 以前这更多是 informal 的说法，这里想尝试把它表述为可检验的 capacity bound                                                        |
| **各种 dual-memory CL 方法**                            | 据我了解大多用非参数化的 episodic memory buffer，不是真正的参数化双系统。这里要求两个子系统都是参数化的，靠 activation sparsity 来区分 |

#### 需要认真讨论的：MoE

MoE 通过 routing 实现了 **conditional activation sparsity**（不同输入激活不同 expert）。问题是：这算不算 regime differentiation？

初步分析：

- MoE 的稀疏是 **input-conditional** 的（按输入选 expert），这里讨论的 dual-regime 是 **function-conditional** 的（快速区 vs 慢速区有不同的 sparsity 和学习规则）
- MoE 没有巩固机制——没有从 sparse experts 到 dense shared representation 的知识转移
- 但如果 MoE 在持续学习中确实表现更好，那可能支持关于 activation sparsity 的假说
- **实验里可考虑加入 MoE baseline**，看看它的 $C \cdot B$ 表现

#### Progressive Neural Networks（Rusu et al. 2016）

通过不断增加新模块来避免遗忘。本质上是在**增加 $\Phi(d)$**（参数量增大通常会抬高可用容量上限），与这里关注的"固定参数量下的 single-regime 边界"是不同问题。

#### 跟 CLS 的对应

| 本 proposal 中的概念              | 大脑里对应什么                             |
| :------------------------------- | :----------------------------------------- |
| 快速区（高 activation sparsity） | 海马体 DG（~2-5% 激活率）                  |
| 慢速区（低 activation sparsity） | 新皮层（~10-20% 激活率）                   |
| 巩固机制 $\mathcal{C}$           | 睡眠期的 hippocampal replay → 新皮层可塑性 |
| Sparsity 实现 pattern separation | DG granule cell 稀疏编码                   |
| 容量-干扰 tradeoff               | 海马体有限容量 vs 新皮层高容量             |

**需要指出的一个限制**：这个理论的构建过程就是受 CLS 启发的，所以结论跟 CLS 对应上**不能**算独立的 convergent evidence。但核心结果（$C \cdot B$ bound）是从 activation sparsity 与 interference 的数学关系直接推出来的，不依赖 CLS 类比。CLS 只是事后的解读框架。

### 实验设计

#### 实验的原则

实验不是为了刷分，是为了**验证理论预测**。所以用最小化设计，控制变量优先。

#### 实验平台

Transformer（约 561M 参数，nanochat 规模）。理论验证不需要大模型，但需要大量 runs（≥3 seeds × 多个 sparsity levels × 多个任务序列长度）。

#### Exp 1: Activation Sparsity → 干扰曲线

**要回答的问题**：Hopfield 上的理论预期"越稀疏干扰越小"，在 Transformer 里定性上是否仍成立？

**做法**：

- 固定架构和训练预算
- 控制 activation sparsity：主方案用 k-Winners-Take-All（k-WTA），辅助用 L1 正则化（排除 k-WTA 的 artifact）
- 扫 $k/m \in \{0.02, 0.05, 0.10, 0.20, 0.50, 1.0\}$（对应 $s$ 从 0.98 到 0.0）
- 固定 5 个任务的序列
- 报告：梯度内积 $I(s)$、平均遗忘 $\bar{F}(s)$、两者关于 $s$ 的曲线、k-WTA 和 L1 两种实现是否一致

**预测**：$I(s)$ 和 $\bar{F}(s)$ 随 $s$ 单调递减，且 $\bar{F} \propto I$ 近似线性。

**什么情况算推翻**：如果 $I(s)$ 非单调（比如某个中间 sparsity 的干扰反而更高），说明命题 1 在深度网络上的外推需要修正。

#### Exp 2: 单系统容量边界检验

**要回答的问题**：不同 sparsity level 下，能学的任务数和每任务学习效果之间是不是真的有 tradeoff？$C \cdot B$ 有没有上界？

**做法**：

- 对 Exp 1 的每个 sparsity level，逐步增加任务数（$T = 5, 10, 20, 50$）
- 对每个 $(s, T)$ 组合记录：所有任务遗忘是否 $\leq \epsilon$？如果不是，$C(s, \epsilon)$ 等于满足条件的最大 $T$
- 用 task-specific loss reduction 度量 $B(s)$
- 画 Pareto frontier：$C(s, \epsilon)$ vs $B(s)$
- 画 $C \cdot B$ vs $s$ 的曲线

**预测**：

1. 高 sparsity → 能学很多任务但每个都学得浅
2. 低 sparsity → 每个任务学得好但很快就忘
3. $C \cdot B$ 受上界约束（可能在某个 $s^*$ 取最大值），仅调 sparsity 难以无限提升

**什么情况算推翻**：$C \cdot B$ 随 $s$ 单调变化且缺乏 tradeoff，或者不同 sparsity 的 $C \cdot B$ 差异极大且无收敛趋势。

#### Exp 3: 双系统初步验证

**要回答的问题**：双系统在 Transformer 上能否展示出相对单系统的容量优势？

**注意：这只是 proof-of-concept，不追求最优实现，不跟 CL SOTA 比分。**

**做法**：

- **快速区**：部分层用 k-WTA（$k/m = 0.05$，$s_1 = 0.95$）
- **慢速区**：其余层用标准 activation（$s_2 \approx 0.0$）
- **巩固**：简单的 interleaved replay（从快速区缓存的 logits 做知识蒸馏到慢速区）
- **对照基线**：
  - B0: 标准 dense baseline
  - B1: Exp 2 里 $C \cdot B$ 最大的那个 single-regime
  - B1-same: 总参数量一样，但两个区域用**相同**的 sparsity（排除"参数分配"的混淆）

**预测**：在部分设定下可能出现 $C_{\text{dual}} > C_{\text{B1}}$

**什么情况算推翻**：若稳定观察到 $C_{\text{dual}} \leq C_{\text{B1}}$，则 H3 在深度网络上的支持证据不足，或实现方案存在关键问题。

### 风险和对策

#### 风险 1: Hopfield 的结论跟 Transformer 有什么关系？

审稿人很可能会关注这一点。

**对策**：

- Exp 1 和 Exp 2 直接在 Transformer 上验证定性预测
- 论文结构讲清楚：Hopfield 上可验证推导 + 深度网络上 empirical conjecture，不混为一谈
- 有先例：Hopfield 网络的容量理论（Cover 1965, Tsodyks & Feigelman 1988）到今天还是理解联想记忆的基础工具，虽然现代网络比 Hopfield 复杂得多

#### 风险 2: $C \cdot B$ bound 不够 tight

$C \cdot B$ 对 $a$ 有弱依赖（$\propto a^2$），不是严格常数。这可能让"tradeoff"的故事没那么漂亮。

**对策**：

- 如实报告 bound 的形式，不将其表述为常数
- 核心 claim 调整为：**存在最优 $a^*$，且 $C(a^*) \cdot B(a^*)$ 有上界**——调 $a$ 不能无限提升 throughput
- 实验里直接画 $C \cdot B$ vs $s$ 曲线

#### 风险 3: k-WTA 引入 artifact

k-WTA 的硬约束可能导致训练不稳定，实验结果反映的是 k-WTA 的毛病而不是 activation sparsity 的本质。

**对策**：

- 同时用 L1 正则化做 soft enforcement
- 两种实现的 $I(s)$ 曲线定性一致 → artifact 风险低
- 不一致 → 分析原因，可能需要第三种实现

#### 风险 4: 双系统的优势来自参数量更多而不是 regime 分化

**对策**：

- 控制总参数量相同
- B1-same 基线：同参数量但两个区域用相同 sparsity
- 如果 B1-same ≈ dual-regime，那优势来自参数分配而不是 differentiation，H3 要重新审视

### 时间线

#### Phase 1: 理论（优先项）

- Hopfield 上命题 1 和命题 2 的理论推导
- 命题 3 的构造性推导
- 跟 Tsodyks & Feigelman (1988) 的结果对接
- 搞清楚 bound 的 tightness 和适用范围

#### Phase 2: 实验

- Exp 1: $I(s)$ 曲线
- Exp 2: Single-regime Pareto frontier
- Exp 3: Dual-regime sanity check

#### Go/No-Go 判定

**继续做的条件**：

- Hopfield 上的推导能够闭合且自洽
- Exp 1 和 Exp 2 定性上支持理论预测（单调性成立、tradeoff 存在）

**不做了的条件**：

- Hopfield 推导需要太强的假设，结果变得 trivial
- Exp 1 里 $I(s)$ 非单调，或 Exp 2 里 $C \cdot B$ 没有收敛趋势

### 论文结构（到时候写的话）

```
1. Introduction: stability-plasticity dilemma 缺形式化 → 尝试给出 capacity bound
2. Preliminaries: activation sparsity / write interference / forgetting 的定义
3. Theory (核心):
   3.1 Proposition 1: I(s) 单调递减（Hopfield, 待证）
   3.2 Proposition 2: Single-regime C·B bound（Hopfield, 待证）
   3.3 Proposition 3: Dual-regime 是否可超过 single-regime bound（constructive）
   3.4 Conjecture: 定性结论推广到深度网络
4. Experiments:
   4.1 Exp 1: I(s) curve in Transformer → 检验命题 1
   4.2 Exp 2: Pareto frontier → 检验命题 2
   4.3 Exp 3: Dual-regime sanity check → 支持命题 3
5. Discussion: CLS 对应、现有方法的边界解释、局限性
6. Future Work
```

### 将来可以做但这次不做的事

1. **完整的参数化 CLS 系统**：最优巩固调度、自适应 sparsity、快速区容量管理——独立的系统工程问题
2. **$\Phi(d)$ 的 scaling 分析**：capacity bound 怎么随模型规模变？有没有 scaling law？
3. **MoE 跟 conditional sparsity 的关系**
4. **第二层推导**：线性网络上的进一步理论化
5. **快速区和慢速区最优 activity level 的理论分析**

## 算力成本评估

nanochat 规模（约 561M 参数），核心开销集中在 Exp 2 的大量组合实验上。

- Exp 1: 6 sparsity levels × 2 实现方式 × 3 seeds = 36 runs
- Exp 2: 6 sparsity levels × 4 任务序列长度 × 2 实现方式 × 3 seeds = 144 runs
- Exp 3: 4 配置（dual + 3 baselines）× 3 seeds = 12 runs
- 单次 run 在 A100 上约 8-12 小时
- 总计约 ~1500-2300 A100 GPU 小时，8×H100 集群约 2-3 周
- 云端成本约 $3000-4500

## 预期产出

### 理论

1. **Compression-writability bound**：尝试把 stability-plasticity dilemma 形式化为容量上界（Hopfield 上做理论推导，深度网络上以实验方式检验）
2. **单系统容量边界**：检验固定 activation sparsity 下 $C$ 和 $B$ 之间是否存在受上界约束的 tradeoff
3. **双系统容量优势**：评估 dual-regime 作为缓解该边界的候选充分条件是否成立

需要强调的是，这里不主张 necessity——不是说 dual-regime 是唯一的突破方式。MoE 的 conditional sparsity、参数增长等其他路径需要另行分析。

### 实验

1. Activation sparsity 和 interference 的定量关系曲线
2. 单系统的 Pareto frontier（capacity vs richness）
3. 双系统的初步方向性验证

### 对 CL 领域的影响（如果结论成立的话）

- 可能为 EWC/GPM/replay 等方法在长序列上退化提供一种可检验的定量解释
- 指出一个可能被忽视的方向：**activation sparsity 的 regime 分化**（而不是只在一套 regime 里优化更新规则）
- 提供可证伪的预测：测量 single-regime CL 方法的 activation sparsity，评估其容量边界是否可被提前估计

## 参考文献

### 持续学习基础

- Kirkpatrick et al. (2017). Overcoming catastrophic forgetting in neural networks. _PNAS_. [EWC]
- Farajtabar et al. (2020). Orthogonal gradient descent for continual learning. _AISTATS_. [OGD]
- Saha et al. (2021). Gradient projection memory for continual learning. _ICLR_. [GPM]
- Knoblauch et al. (2020). Optimal continual learning has perfect memory and is NP-hard. _ICML_.
- Shin et al. (2017). Continual learning with deep generative replay. _NeurIPS_.

### CLS 理论

- McClelland, McNaughton, & O'Reilly (1995). Why there are complementary learning systems. _Psychological Review_.
- Kumaran, Hassabis, & McClelland (2016). What learning systems do intelligent agents need? _Trends in Cognitive Sciences_.

### 海马体神经科学

- Leutgeb et al. (2007). Pattern separation in the dentate gyrus and CA3. _Science_.
- Chawla et al. (2005). Sparse expression of Arc RNA in the rodent fascia dentata. _Hippocampus_.
- Amaral, Ishizuka, & Claiborne (1990). Neurons, numbers and the hippocampal network. _Progress in Brain Research_.

### 稀疏性与表征理论

- Tsodyks & Feigelman (1988). Enhanced storage capacity with low activity level. _Europhysics Letters_. [**本研究的直接基础**]
- Frankle & Carlin (2019). The lottery ticket hypothesis. _ICLR_.
- Elhage et al. (2022). Toy models of superposition. _Anthropic_.

### 架构相关

- Rusu et al. (2016). Progressive neural networks.
- Shazeer et al. (2017). Outrageously large neural networks: MoE. _ICLR_.
- Fedus, Zoph, & Shazeer (2022). Switch Transformers. _JMLR_.

### 信息论基础

- Cover & Thomas (2006). _Elements of Information Theory_. Wiley.
