# KnowledgeEditor

**Paper:** KnowledgeEditor
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Post-Train

---

## Problem

How can internal model parameters be modified to precisely change only the knowledge that needs editing without affecting other learned information?

## Method

KnowledgeEditor implements knowledge editing by modifying internal model parameters, with the design goal of strictly limiting the editing impact to the specific knowledge range that requires modification. Unlike direct fine-tuning, KnowledgeEditor learns to generate precise parameter updates, ensuring the locality and controllability of edits.

## Core Mechanism

- **Internal Parameter Modification**: Directly modifies model weights to update specific knowledge.
- **Editing Locality**: Aims to change only the required knowledge while keeping other knowledge intact.
- **Controllable Editing**: Learns a strategy for precise parameter updates.

## Task

- QA
- Fact Checking
