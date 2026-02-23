# Retroformer — Yao et al. 2024

**Paper:** Yao et al. (2024) — Retroformer
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Auxiliary LM

---

## Problem

Agents lack a systematic mechanism to learn from the successes and failures of past tasks during execution, resulting in repeated mistakes and an inability to accumulate experience.

## Method

Retroformer proposes a learning paradigm specifically designed to memorize experiences of success and failure from past task executions. By using an auxiliary language model (auxiliary LM) to record and learn from historical task execution trajectories, Retroformer can utilize these experiences to improve decisions in subsequent tasks.

Unlike prompt-based reflection methods, Retroformer stores and refines experience through a parameterized auxiliary model, making experience learning more systematic and persistent.

## Core Mechanism

- **Experience Memory**: Records success and failure experiences from past task executions.
- **Auxiliary LM**: Stores and refines experience through a parameterized auxiliary model.
- **Learning Paradigm**: Systematically learns improvement strategies from historical execution trajectories.
- **Cross-task Transfer**: Applies past experience to decision-making in new tasks.

## Task

- QA
- Web Navigation
