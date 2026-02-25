# The Primacy Bias in Deep Reinforcement Learning — Nikishin et al. 2022

**Paper:** Nikishin, Schwarzer, D'Oro, Bacon, Courville (2022)
**Title:** The Primacy Bias in Deep Reinforcement Learning
**Source:** ICML 2022; arXiv 2205.07802 (May 2022)
**Category:** Fundamental — Plasticity Loss — RL-specific
**Code:** https://github.com/evgenii-nikishin/rl_with_resets

---

## Problem

Deep RL agents exhibit a **primacy bias**: they over-rely on early interactions and fail to incorporate useful evidence encountered later in training. This is a specific manifestation of plasticity loss in the RL setting — the agent's network becomes "locked in" to patterns from initial experiences.

## Key Findings

- Training on progressively growing datasets causes deep RL agents to **overfit to earlier experiences**
- This overfitting negatively affects the rest of the learning process
- The effect is analogous to the **primacy effect** in cognitive psychology (first impressions dominate)
- Observed across both discrete (Atari 100k) and continuous (DeepMind Control Suite) action domains

## Method: Periodic Network Resets

- **Periodically reset** a portion of the agent's network parameters while retaining the replay buffer
- Simple and generally applicable across different RL algorithms
- Consistent performance improvement in both Atari 100k and DMC benchmarks

## Core Mechanism

- Early training data disproportionately shapes network features
- As the network trains longer, these early features become increasingly difficult to override
- The loss landscape "hardens" around early solutions, preventing adaptation to later, potentially better data
- Periodic resets break this cycle by restoring the network's capacity to learn

## Critical Insight for Sparse Topology Research

This is essentially a **brute-force plasticity restoration** — reset and re-learn. The question for sparse topology research: can architectural sparsity provide a more graceful mechanism for preventing primacy bias? If sparse topology maintains more independent/modular pathways, early experiences might be less likely to dominate the entire network's representation.

## Relation to Other Work

- Directly inspired: Nikishin et al. 2023 (Plasticity Injection — more refined version)
- Parallel discovery: Dohare et al. 2024 (Continual Backprop — unit-level reinitialization vs network-level resets)
- Mechanistic analysis: Lyle et al. 2023 (Understanding Plasticity — curvature perspective)
