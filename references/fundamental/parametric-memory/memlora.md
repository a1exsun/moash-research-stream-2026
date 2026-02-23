# MemLoRA — Bini et al. 2025

**Paper:** Bini et al. (2025) — MemLoRA: Distilling Expert Adapters
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Adapter

---

## Problem

How can knowledge from multiple expert adapters be efficiently compressed and integrated to achieve memory-enhanced knowledge editing?

## Method

MemLoRA achieves memory enhancement by distilling expert adapters. The core idea is to compress knowledge from multiple specialized expert adapters into a unified LoRA module through distillation. This preserves the precision of expert knowledge while reducing computational and storage overhead during inference.

## Core Mechanism

- **Expert Adapter Distillation**: Distills knowledge from multiple expert adapters into a unified module.
- **Memory Enhancement**: Achieves knowledge compression and integration through the distillation process.
- **LoRA Architecture**: Uses low-rank adapters as knowledge carriers, ensuring parameter efficiency.
- **Knowledge Compression**: Unifies decentralized expert knowledge into a compact parameter space.

## Task

- QA
