# Continual Learning Research Proposals

## Proposal 1: Mechanism Ablation Study

**Goal:** Systematically decompose the independent and interaction contributions of three key CL mechanisms under a unified training budget.

**Mechanisms under study:**

- Structural sparse topology
- Selective write gating
- Offline consolidation / replay

**Method:** A 2×2×2 factorial design that isolates each mechanism's marginal contribution and their pairwise/three-way interactions.

---

## Proposal 2: Post-hoc Sparse Conversion for CL

**Goal:** Test whether converting a pretrained dense LLM to structured sparsity (e.g., 2:4) directly reduces catastrophic forgetting during sequential fine-tuning.

---

## Proposal 3: Native Sparse Pretraining and Interference Phase Boundaries

**Goal:** Investigate whether natively sparse-pretrained models shift the critical boundary between "high-forgetting" and "low-forgetting" phases.

**Core claim:** Continual learning forgetting exhibits reproducible **phase transitions**, and native sparsity systematically moves these boundaries. This is framed not as "method X scores higher" but as a mechanistic finding.

**Framework:** A risk ratio $R_t = I_t / C_t$ (interference over plasticity capacity) that characterises when forgetting accelerates.

---

## Proposal 4: Curvature-Decomposed Continual Learning (CDCL)

**Goal:** A pure training-rule modification (no architecture change, no external memory) for continual learning.

**Method:** Decompose gradients into:

- A **knowledge-sensitive subspace** component → apply strong constraints (preserve old knowledge)
- A **plasticity subspace** component → maintain high learning rates (enable new learning)

This is essentially a low-rank subspace generalisation of EWC/GPM.

---

## Proposal 5: Compression-Writability Capacity Bound

**Goal:** Formalise the stability-plasticity dilemma as a provable capacity bound from first principles.

**Core idea:** In any single-regime system with fixed activation sparsity, there exists a fundamental ceiling:

$$C(s, \epsilon) \cdot B(s) \leq \Phi(d)$$

where $C$ = number of tasks learnable without forgetting, $B$ = per-task learning quality, and $\Phi(d)$ is a function of model dimensionality.

**Approach:**

1. Prove the bound exactly on Hopfield networks (building on Tsodyks & Feigelman, 1988)
2. Validate as an empirical conjecture on Transformers
3. Show that a **dual-regime architecture** (analogous to hippocampal–neocortical complementary learning systems, but fully parametric) is a sufficient condition to break through the single-regime ceiling
