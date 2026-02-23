# T-Patcher — Huang et al. 2023

**Paper:** Huang et al. (2023) — Transformer Patcher
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Adapter

---

## Problem

How can incorrect predictions in a Transformer model be efficiently patched without affecting the model's normal behavior on other inputs?

## Method

T-Patcher (Transformer Patcher) implements knowledge editing by identifying "patch-worthy neurons." For each error that needs correction, T-Patcher locates relevant neurons and adds small-scale patch modules to precisely correct the model's behavior.

This method transforms knowledge editing into a neuron-level patching problem, achieving precise behavioral correction through external patch modules.

## Core Mechanism

- **Neuron Localization**: Identifies "patch-worthy neurons" associated with incorrect predictions.
- **External Patch Modules**: Adds small-scale patching parameters for target neurons.
- **Precise Correction**: Modifies only behaviors related to the error, without affecting other inputs.
- **Incremental Editing**: Adds a new patch for each edit without modifying original parameters.

## Task

- QA
