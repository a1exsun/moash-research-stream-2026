# Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning — 2025

**Paper:** (Authors TBD from full paper)
**Title:** Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning
**Source:** NeurIPS 2025 (accepted); arXiv 2509.22335 (September 2025)
**Category:** Fundamental — Plasticity Loss — Theoretical Analysis

---

## Problem

Why exactly does loss of plasticity occur at the optimization level? Previous work identified curvature changes but lacked a precise theoretical characterization.

## Key Contributions

### 1. Hessian Spectral Collapse
- At new-task initialization, **meaningful curvature directions in the Hessian vanish**
- Gradient descent becomes ineffective because the loss landscape becomes "flat" in most directions
- This is a **necessary precursor** to plasticity loss — it occurs before performance degradation becomes visible

### 2. τ-trainability Framework
- Introduces **τ-trainability** as a formal necessary condition for successful training
- A network is τ-trainable if gradient descent can reduce the loss to below τ within a reasonable number of steps
- Current plasticity-preserving algorithms (continual backprop, resets, LayerNorm+WD) can be **unified** under this framework — they all maintain τ-trainability

### 3. Regularization via Hessian Structure
- Uses **Kronecker-factored approximation of the Hessian** to motivate practical regularizers
- Two key regularizations:
  1. **Maintaining high effective feature rank** → prevents representation collapse
  2. **L2 penalties** → prevents weight magnitude explosion
- Combining these two regularizers effectively preserves plasticity

## Core Mechanism

```
Prolonged training → Weight growth + Feature homogenization
    → Hessian eigenvalue spectrum collapses (most eigenvalues → 0)
    → Gradient descent has no "useful directions" to update
    → Network cannot learn new tasks
    → Loss of plasticity
```

## Critical Insight for Sparse Topology Research

This is arguably the most theoretically rigorous plasticity loss paper. For sparse topology:
- **Sparse connectivity inherently maintains higher effective feature rank** because different sparse pathways are forced to learn different features
- **The Kronecker factored Hessian decomposition** could be applied to analyze how topology affects curvature — sparse topology may naturally prevent spectral collapse
- **τ-trainability** provides a formal framework for evaluating whether a given sparse topology preserves plasticity
- Key research question: does sparse topology provably maintain non-degenerate Hessian spectrum?

## Relation to Other Work

- Theoretical foundation for: Dohare et al. 2024 (explains WHY continual backprop works)
- Extends: Lyle et al. 2023/2024 (formalizes the curvature perspective)
- Unifies: All existing plasticity-preserving methods under τ-trainability
