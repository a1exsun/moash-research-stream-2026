# WISE — 2024, NeurIPS

**Paper:** WISE (2024, NeurIPS)
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Adapter

---

## Problem

In lifelong editing scenarios, continuously injecting new knowledge into a model leads to conflicts between new and old knowledge, affecting overall model performance.

## Method

WISE employs a dual parametric memory setting, separate storing pre-trained knowledge and editing knowledge in two independent sets of parameters. During inference, a routing mechanism dynamically selects which parameter memory to use—the original pre-trained parameters or the edited parameters—based on the input.

This design of separate storage and dynamic routing effectively alleviates the problem of knowledge conflict during the lifelong editing process.

## Core Mechanism

- **Dual Parametric Memory**: Pre-trained and editing knowledge are stored respectively in independent parameter sets.
- **Dynamic Routing**: Automatically selects which set of parameters to use based on input semantics during inference.
- **Knowledge Conflict Alleviation**: Avoids mutual interference between new and old knowledge through physical isolation.
- **Lifelong Editing Support**: Designed for continuous, long-term knowledge update scenarios.

## Task

- QA
- Hallucination Detection
