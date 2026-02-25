# Deep Reinforcement Learning with Plasticity Injection — Nikishin et al. 2023

**Paper:** Nikishin, Oh, Ostrovski, Lyle, Pascanu, Dabney, Barreto (2023)
**Title:** Deep Reinforcement Learning with Plasticity Injection
**Source:** NeurIPS 2023; arXiv 2305.15555 (May 2023)
**Category:** Fundamental — Plasticity Loss — Mitigation (RL)

---

## Problem

Neural networks in deep RL gradually lose plasticity, and existing solutions (full network resets) are computationally wasteful and discard learned features.

## Method: Plasticity Injection

A minimalistic intervention that **increases network plasticity without changing the number of trainable parameters** or biasing predictions:
- Adds new randomly initialized neurons to existing layers
- Simultaneously removes neurons with lowest utility
- Net effect: refreshes a small fraction of the network without changing architecture size

## Key Contributions

### 1. Diagnostic Tool
- If plasticity injection improves performance → the agent's network was losing plasticity
- Identified a subset of **Atari environments where plasticity loss causes performance plateaus**
- Provides empirical evidence that plasticity loss is environment-dependent

### 2. Computational Efficiency
- More efficient than full network resets (Nikishin et al. 2022)
- Can be used to dynamically grow the network if needed
- Stronger performance on Atari than alternative methods

## Core Mechanism

- Utility-based selection identifies which neurons contribute least to current learning
- Replacing low-utility neurons with fresh random ones restores local plasticity
- Conceptually similar to continual backpropagation (Dohare et al.) but applied at the neuron level in RL context

## Critical Insight for Sparse Topology Research

Plasticity injection is essentially **dynamic topology modification** — adding/removing neurons based on utility. This is closely related to sparse topology evolution (e.g., SET, RigL). The key difference:
- Plasticity injection: swaps neurons (columns in weight matrix)
- Sparse topology evolution: swaps connections (individual weights)
- Both maintain network capacity while refreshing structure
- Sparse topology evolution operates at a finer granularity

## Relation to Other Work

- Extends: Nikishin et al. 2022 (Primacy Bias — from full resets to targeted injection)
- Parallel to: Dohare et al. 2024 (Continual Backprop — similar utility-based reinitialization)
- Mechanism explained by: Lyle et al. 2023 (curvature-based analysis)
