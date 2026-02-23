# SELF-PARAM

**Paper:** SELF-PARAM
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Post-Train

---

## Problem

How can external knowledge be injected into a model's parameterized memory without introducing additional parameters?

## Method

SELF-PARAM injects additional knowledge into the model through KL divergence distillation, with the core feature being that no additional parameters are required. Through a self-distillation mechanism, the model absorbs new knowledge while maintaining its original capabilities, achieving lightweight parameterized memory updates.

This method avoids the computational overhead associated with adapters or additional modules, completing knowledge injection directly within the model's existing parameter space.

## Core Mechanism

- **KL Divergence Distillation**: Injects new knowledge into the model by minimizing distribution differences.
- **No Additional Parameters**: Does not require introducing new trainable parameters.
- **Self-distillation**: The model itself serves as both teacher and student to achieve knowledge internalization.

## Task

- QA
- Recommendation
