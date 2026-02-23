# Proposal 04: 曲率分解驱动的持续学习（CDCL）

## 目标

在不改变模型架构、不引入外部工程记忆系统的前提下，仅通过训练规则改造，验证是否可以在长期任务序列中显著降低灾难性遗忘。

核心思想：
- 将参数更新分解为“旧知识敏感子空间”与“可塑性子空间”两部分
- 对前者施加强约束，对后者保持高学习率
- 以此提升 stability-plasticity tradeoff

---

## 研究问题

1. 历史任务对应的高曲率子空间是否稳定承载主要旧知识？
2. 在新任务训练中抑制该子空间更新，是否能显著降低 forgetting？
3. 相比对角近似约束（如 EWC diagonal），低秩子空间约束是否在长任务序列下更有效？

---

## 假设

### H1
旧任务的 Fisher/Hessian 主子空间（top eigenspace）与遗忘风险强相关。

### H2
将梯度分解后对平行分量降权（而非完全冻结），可在较小学习速度损失下显著降低遗忘。

### H3
低秩子空间约束（CDCL）在长期序列中优于 diagonal Fisher 方法，因为它显式建模参数耦合方向。

---

## 方法定义（训练层）

设历史保护子空间基为 `U_t in R^{d x k}`（列正交，`k << d`），当前梯度为 `g`。

梯度分解：
- `g_parallel = U_t (U_t^T g)`
- `g_perp = g - g_parallel`

更新规则：
- `Delta theta = -eta * (alpha * g_parallel + g_perp)`
- 其中 `alpha in [0, 1)`，`alpha` 越小表示保护越强

子空间更新：
- 每完成一个阶段任务后，用该阶段梯度统计/Fisher 近似更新 `U_t`
- 采用 streaming PCA / Oja 风格低秩更新，避免全量二阶矩阵存储

说明：
- 不引入 replay/RAG/外部 memory
- 不改 Transformer 结构，仅改 optimizer/update rule

---

## 实验设计

## 1. 对照组

- `B0`：标准 AdamW（dense baseline）
- `B1`：EWC-diagonal（经典对照）
- `C1`：CDCL（low-rank subspace constraint）

可选扩展：
- `C2`：CDCL + 自适应 `alpha`（随阶段动态调节）

## 2. 公平性约束

- 同一 backbone、同一初始化策略
- 同一 token budget / step budget / batch / optimizer超参基线
- 同一数据流与域顺序协议
- 报告 `same-shape` 与 `matched-FLOPs`
- 每组 >= 3 seeds，报告 95% CI

## 3. 任务协议

- 连续域序列：代码 -> 数学 -> 医疗 -> 法律 -> 对话
- 至少两种域顺序扰动用于稳健性检查
- 长序列版本：>= 20 阶段切换（允许重复回访域）

---

## 指标体系

主指标：
1. Average Forgetting
2. BWT
3. Retention@k

次指标：
1. FWT
2. 新域收敛步数/速度
3. 单位 FLOPs 收益

机制指标：
1. `||g_parallel|| / ||g||` 与 forgetting 的相关性
2. 保护子空间漂移率（`subspace distance`）
3. 不同层的干扰能量分布

---

## 统计与可证伪性

1. 预注册主假设与主指标，避免后验挑指标。
2. 用 mixed-effects model 或两因素 ANOVA（方法 x 阶段）分析长期趋势。
3. 关键可证伪标准：
- 若 `C1` 相比 `B0` 无显著 forgetting 改善，H2 被削弱
- 若 `C1` 不优于 `B1`，H3 不成立
- 若机制指标与 forgetting 弱相关，H1 不成立

---

## Go/No-Go 决策门槛

Go（继续投入）：
- `C1` 在 matched-FLOPs 下相对 `B0` forgetting 降低 >= 15%
- 新域学习速度下降 <= 10%
- 相对 `B1` 至少在一个长期设置中有显著优势

No-Go（降级或终止）：
- 多设置下无统计显著收益
- 额外计算/实现复杂度超过收益（性价比不成立）

---

## 风险与应对

### 风险1：低秩子空间估计不稳定
应对：先固定较小 `k` 和层级范围（如只作用于 attention/MLP 关键层），再扩展。

### 风险2：约束过强导致 plasticity 严重下降
应对：使用 `alpha` 网格搜索（如 0.1/0.3/0.5）并加入阶段自适应策略。

### 风险3：计算开销偏高
应对：采用分层采样更新子空间，减少更新频率（按阶段而非按step刷新）。

---

## 预期输出

1. 一套纯训练层、无架构改造的持续学习基线方法（CDCL）
2. 干扰几何指标与遗忘之间的实证关系
3. 对“参数耦合是否是遗忘主因”的直接证据或反证

---

## 里程碑

1. Week 1：实现 CDCL 核心更新规则与单阶段 sanity check
2. Week 2：`B0/B1/C1` 四到六阶段实验 + 初步统计
3. Week 3：长序列实验（>=20阶段）与稳健性分析
4. Week 4：总结 Go/No-Go 与论文级图表产出
