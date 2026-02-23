# AlphaEdit — Fang et al. 2025

**Paper:** Fang et al. (2025) — Null-space Constrained Knowledge Editing
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Post-Train

---

## Problem

Existing knowledge editing methods may disrupt the model's established knowledge structure when editing new information, with cumulative errors becoming significant after repeated consecutive edits.

## Method

AlphaEdit proposes a Null-space Constrained Knowledge Editing method. The core idea is to project parameter updates for knowledge editing into the null space of the model's existing knowledge representation, ensuring that new edits do not interfere with the expression of previously acquired knowledge.

Through this constraint, AlphaEdit strictly preserves the model's existing knowledge while injecting new information, enhancing stability and reliability in continuous editing scenarios.

## Core Mechanism

- **Null-space Projection**: Constraints parameter updates within the null space of existing knowledge representations.
- **Knowledge Preservation**: Ensures that editing operations do not interfere with the expression of existing knowledge.
- **Continuous Editing Stability**: Maintains model performance even after multiple successive edits.

## Task

- QA
