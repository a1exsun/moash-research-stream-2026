# Understanding Plasticity in Neural Networks — Lyle et al. 2023

**Paper:** Lyle, Zheng, Nikishin, Pires, Pascanu, Dabney (2023)
**Title:** Understanding Plasticity in Neural Networks
**Source:** ICML 2023; arXiv 2303.01486 (March 2023)
**Category:** Fundamental — Plasticity Loss — Mechanistic Analysis

---

## Problem

Why do neural networks lose plasticity — the ability to quickly change predictions in response to new information? This paper provides a **systematic empirical analysis** of the mechanisms underlying plasticity loss.

## Key Findings

- Loss of plasticity is **deeply connected to changes in the curvature of the loss landscape**
- Plasticity loss often occurs **in the absence of saturated units** — contradicting the common belief that dead ReLU units are the sole cause
- The effective rank of the network's feature representations decreases over training
- Changes in the loss landscape geometry (Hessian structure) make gradient-based optimization increasingly ineffective

## Core Mechanisms Identified

1. **Loss landscape curvature changes**: The Hessian of the loss becomes increasingly ill-conditioned, making gradient descent less effective
2. **Feature rank collapse**: Network representations lose diversity, reducing the effective dimensionality of the feature space
3. **Weight norm growth**: Parameter magnitudes increase over training, making the network less responsive to gradient updates (effective learning rate decreases)

## Design Choices That Preserve Plasticity

- **Layer normalization**: Helps maintain feature diversity and prevents weight norm explosion
- **Weight decay / L2 regularization**: Controls weight magnitude growth
- **Careful initialization schemes**: Maintain diversity at the start of each new task
- **Spectral normalization**: Controls the spectral properties of weight matrices

## Critical Insight for Sparse Topology Research

This paper reveals that plasticity loss is NOT just about dead neurons — it's about **geometric changes in the optimization landscape**. For sparse topology research, this means:
- Simply having a sparse network (fewer dead neurons) may not suffice
- The topology must also maintain favorable **curvature properties** in the loss landscape
- Sparse topology could potentially help by maintaining higher effective feature rank through forced diversity of pathways

## Relation to Other Work

- Preceded by: Nikishin et al. 2022 (Primacy Bias — observed the phenomenon)
- Followed up by: Lyle et al. 2024 (Disentangling Causes — decomposed into independent mechanisms)
- Complementary to: Dohare et al. 2024 (focused more on dead units; this paper shows curvature matters too)
