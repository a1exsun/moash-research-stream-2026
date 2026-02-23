# Engram — DeepSeek & Peking University

**Paper:** [arXiv 2601.07372](https://arxiv.org/pdf/2601.07372)
**Source:** Machine Heart Pro Week 07
**Category:** LLM Memory — Architecture Extension (Scalable Lookup Module)

---

## Problem

Transformers lack native knowledge lookup primitives and must simulate retrieval through inefficient deep computation.

## Method

Proposes a sparsity dimension of "conditional memory" as a supplement to the conditional computation paradigm of MoE. Designs the Engram scalable lookup module, drawing on classic N-gram embedding ideas, to achieve knowledge lookup with O(1) time complexity, allowing the model to quickly invoke static knowledge based on local input patterns.

## Mechanism Analysis

Shallow layers are liberated from static knowledge reconstruction tasks, while deep layers focus on complex reasoning, equivalently increasing the model's effective depth. The deterministic retrieval characteristic supports the decoupling of storage and computation; the memory table can be deployed on CPU/SSD, reducing dependency on GPU video memory.

## Results

At 27B scale, under equivalent parameter and FLOPs conditions:

- Knowledge Category: MMLU +3.4, CMMLU +4.0 (vs MoE baseline)
- General Reasoning: BBH +5.0, ARC-Challenge +3.7
- Code & Math: HumanEval +3.0, MATH +2.4
- Long Context: Multi-Query NIAH 84.2% → 97.0%
