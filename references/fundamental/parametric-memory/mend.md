# MEND — Mitchell et al. 2022

**Paper:** Mitchell et al. (2022) — Model Editor Networks with Gradient Decomposition
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Post-Train

---

## Problem

Direct fine-tuning to edit model knowledge leads to catastrophic interference with unrelated knowledge and is inefficient. How can fast, precise, single-step knowledge editing be achieved?

## Method

MEND (Model Editor Networks with Gradient Decomposition) introduces an auxiliary editor network to achieve fast single-step editing by decomposing fine-tuning gradients. The editor network learns to transform standard gradients into localized parameter updates, ensuring that editing only affects targeted knowledge while minimizing interference with unrelated knowledge.

The key innovation is gradient decomposition: high-dimensional gradients are decomposed into low-rank factors. The editor network learns how to generate precise editing directions in this low-rank space, resulting in efficient and localized parameter modification.

## Core Mechanism

- **Auxiliary Editor Network**: A specially trained network that learns to transform gradients into precise parameter updates.
- **Gradient Decomposition**: Decomposes fine-tuning gradients into low-rank factors to reduce computational costs.
- **Single-step Editing**: Completes knowledge modification in one step without multiple rounds of iteration.
- **Locality Guarantee**: Minimizes interference with unrelated knowledge.

## Task

- QA
- Fact Checking
- Model Editing
