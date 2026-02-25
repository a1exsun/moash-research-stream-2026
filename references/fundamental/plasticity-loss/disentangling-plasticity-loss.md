# Disentangling the Causes of Plasticity Loss in Neural Networks — Lyle et al. 2024

**Paper:** Lyle, Zheng, Khetarpal, van Hasselt, Pascanu, Martens, Dabney (2024)
**Title:** Disentangling the Causes of Plasticity Loss in Neural Networks
**Source:** ICML 2025 (proceedings.mlr.press/v274/lyle25a); arXiv 2402.18762 (February 2024)
**Category:** Fundamental — Plasticity Loss — Mechanistic Decomposition

---

## Problem

Previous work identified plasticity loss but treated it as a monolithic phenomenon. This paper asks: can plasticity loss be **decomposed into multiple independent mechanisms**, and can we intervene on them separately?

## Key Findings

- Loss of plasticity decomposes into **multiple independent mechanisms**
- Intervening on any **single** mechanism is **insufficient** to avoid plasticity loss in all cases
- Intervening on **multiple mechanisms in conjunction** produces highly robust learning algorithms
- **Layer normalization + weight decay** is a highly effective combination for maintaining plasticity

## Independent Mechanisms Identified

1. **Weight magnitude growth**: Parameters grow large, reducing effective learning rate
2. **Feature rank collapse**: Internal representations lose diversity/dimensionality
3. **Dead/saturated units**: Units that no longer respond to gradient updates
4. **Loss landscape curvature degradation**: Hessian becomes ill-conditioned
5. **Optimizer state bias**: Momentum/adaptive learning rate states become biased toward previous tasks

## Practical Recipe

The paper validates a simple, practical combination:
- **Layer Normalization** → addresses feature rank collapse, weight magnitude growth
- **Weight Decay** → controls weight magnitude, provides implicit regularization
- Together, these maintain plasticity across both synthetic nonstationary tasks and RL in Arcade Learning Environment

## Critical Insight for Sparse Topology Research

This decomposition is crucial for understanding what sparse topology might (and might not) address:
- Sparse topology likely helps with: feature rank collapse (forces diverse pathways), dead unit problem (fewer parameters to "die")
- Sparse topology likely does NOT help with: optimizer state bias, weight magnitude growth (these need optimization-level interventions)
- **Implication**: sparse topology alone may be necessary but not sufficient — it likely needs to be combined with appropriate optimization techniques (LayerNorm + weight decay) for robust continual learning

## Relation to Other Work

- Directly extends: Lyle et al. 2023 (Understanding Plasticity)
- Connects to: Spectral Collapse (2025) — Hessian analysis of curvature mechanism
- Practical overlap: Dohare et al. 2024 (Continual Backprop addresses dead units specifically)
