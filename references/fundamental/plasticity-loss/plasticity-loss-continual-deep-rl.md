# Loss of Plasticity in Continual Deep Reinforcement Learning — Abbas et al. 2023

**Paper:** Abbas, Zhao, Modayil, White, Sutton (2023)
**Title:** Loss of Plasticity in Continual Deep Reinforcement Learning
**Source:** CoLLAs 2023; arXiv 2303.07507 (March 2023)
**Category:** Fundamental — Plasticity Loss — RL-specific Empirical Study

---

## Problem

Do deep RL agents lose their ability to learn when faced with a sequence of tasks, even when catastrophic forgetting is not a concern (i.e., we only care about performance on the current task)?

## Key Findings

- Deep RL algorithms perform **progressively worse** over time when trained on sequences of tasks
- This is distinct from catastrophic forgetting — the agents fail to learn NEW tasks, not just forget old ones
- **Dead ReLU units** accumulate across tasks: the activation footprint becomes sparser, diminishing gradient flow
- Standard regularization techniques (L2, dropout) provide only partial mitigation

## Empirical Evidence

- Tested on sequences of RL tasks in both tabular and function approximation settings
- Performance degradation is consistent and progressive
- Networks trained on later tasks in a sequence perform significantly worse than networks trained from scratch on the same tasks

## Mechanisms Identified

1. **Dead ReLU accumulation**: Units that never activate lose gradient signal permanently
2. **Sparse activation patterns**: Effective network capacity shrinks as fewer units remain active
3. **Weight distribution shift**: Weights drift from initialization, creating initialization-dependent learning dynamics

## Proposed Mitigations (explored)

- **CReLU (Concatenated ReLU)**: Ensures non-zero gradients for all units, partially mitigates dead neuron problem
- **L2 regularization**: Helps prevent weight magnitude explosion but insufficient alone
- **Shrink-and-perturb**: Partially reinitializes weights, shows promise

## Critical Insight for Sparse Topology Research

This paper (from Sutton's group) provides direct empirical evidence that **network connectivity patterns degrade during continual learning**. The dead ReLU / sparse activation analysis is particularly relevant:
- In a dense network, dead neurons waste capacity
- In a sparse network with dynamic topology, dead connections could be pruned and replaced — naturally maintaining plasticity
- This supports the hypothesis that **dynamic sparse topology is a natural solution to plasticity loss**

## Relation to Other Work

- Same group as: Dohare et al. 2021/2024 (Continual Backprop / Nature paper)
- Complementary to: Lyle et al. 2023 (offers curvature perspective beyond dead neurons)
- RL focus vs: Dohare et al. 2024 (supervised learning focus)
