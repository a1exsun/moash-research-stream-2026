# K-Adapter — Wang et al. 2021

**Paper:** Wang et al. (2021) — K-Adapter
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Adapter

---

## Problem

When injecting new knowledge into a pre-trained model, fine-tuning can disrupt existing pre-trained representations, leading to catastrophic forgetting. How can knowledge be continuously expanded without interfering with the original model?

## Method

K-Adapter injects new knowledge by training task-specific adapter modules while keeping the original backbone completely unchanged. Each adapter module specifically learns one type of knowledge (e.g., factual knowledge, linguistic knowledge, etc.) and is trained and updated independently of the main model.

This design supports continuous knowledge expansion: new types of knowledge can be injected by adding new adapters without interfering with pre-trained representations or knowledge in existing adapters.

## Core Mechanism

- **Task-specific Adapter**: Each knowledge type corresponds to an independent adapter module.
- **Backbone Frozen**: Parameters of the original pre-trained model remain unchanged.
- **Continuous Expansion**: Supports continuous injection of new knowledge by adding new adapters.
- **Knowledge Isolation**: Different types of knowledge are stored in independent modules, avoiding mutual interference.

## Task

- QA
- Entity Typing
- Classification
