# LMLM — Zhao et al. 2025

**Paper:** Zhao et al. (2025) — Limited Memory Language Model
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Pre-Train

---

## Problem

Traditional LLMs tightly couple factual knowledge with model weights, which makes knowledge updates require model retraining and prevents tracing knowledge sources.

## Method

LMLM (Limited Memory Language Model) stores memory for knowledge retrieval within the model during the pre-training phase, but the knowledge itself is stored in an external knowledge base. This design explicitly decouples factual knowledge from model weights: the model learns the capability of "how to retrieve and use knowledge" rather than the knowledge itself.

Through this architecture, LMLM supports direct knowledge editing and source verification without requiring model retraining. When the external knowledge base is updated, the model's behavior automatically reflects the latest knowledge.

## Core Mechanism

- **Knowledge-Weight Decoupling**: Model parameters store retrieval capabilities, while factual knowledge is stored externally.
- **Pre-training Integration**: Knowledge retrieval mechanisms are designed during pre-training rather than as post-training patches.
- **Knowledge Editing Without Retraining**: Directly modifies model output by updating the external knowledge base.
- **Source Verification**: Knowledge sources are traceable, supporting fact-checking.

## Task

- QA
- Factual Generation
