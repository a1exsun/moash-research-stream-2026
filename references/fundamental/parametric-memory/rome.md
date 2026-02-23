# ROME — Meng et al. 2022

**Paper:** Meng et al. (2022) — Rank-One Model Editing
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Post-Train — Knowledge Editing

---

## Problem

How can specific factual knowledge stored in an LLM be precisely modified without retraining the entire model?

## Method

ROME (Rank-One Model Editing) precisely locates the MLP layer storing a specific fact through causal tracing technology, then applies rank-one updates to inject new information into that layer. The core idea is to treat the MLP in a Transformer as a key-value store and update or correct facts in the model's memory by modifying the weight matrix of a specific layer.

Compared to earlier editing methods, ROME achieves higher editing precision and better generalization, enabling modification of target facts while minimizing impact on other knowledge.

## Core Mechanism

- **Causal Tracing**: Locates the specific MLP layer for fact storage through causal intervention experiments.
- **Rank-One Update**: Applies a rank-one update to the target layer's weight matrix to precisely inject new knowledge.
- **Locality**: Editing only affects the target fact and does not interfere with other model behaviors.

## Task

- QA
- Fact Checking
