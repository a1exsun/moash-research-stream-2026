# ELDER — 2025, AAAI

**Paper:** ELDER (2025, AAAI)
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Adapter

---

## Problem

In long-term editing scenarios, a single adapter struggles to carry a large number of edits and is prone to knowledge conflicts. How can the robustness and scalability of long-term editing be improved?

## Method

ELDER maintains multiple LoRA modules, each storing different editing knowledge. A key innovation is learning a routing function that can adaptively select or mix relevant LoRA modules based on input semantics.

This multi-LoRA + routing architecture design, which applies a concept similar to MoE (Mixture of Experts) to knowledge editing scenarios, enhances robustness and scalability in long-term editing situations through decentralized storage and intelligent routing.

## Core Mechanism

- **Multi-LoRA Modules**: Maintains multiple independent LoRA modules to store different editing knowledge.
- **Semantic Routing**: Adaptively selects or mixes relevant LoRAs based on input semantics.
- **Long-term Editing Robustness**: Alleviates the capacity bottleneck of a single module through distributed storage.
- **Scalable Architecture**: Editing capacity can be expanded by adding more LoRA modules.

## Task

- Model Editing
