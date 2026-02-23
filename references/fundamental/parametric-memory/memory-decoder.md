# Memory Decoder — Cao et al. 2025

**Paper:** Cao et al. (2025) — Memory Decoder
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Adapter

---

## Problem

External RAG methods introduce real-time retrieval overhead, affecting inference speed; on the other hand, editing knowledge directly into model parameters can disrupt existing knowledge. How can we achieve both the inference speed of parameterization and the plug-and-play flexibility of RAG?

## Method

Memory Decoder is a plug-and-play method that does not modify the parameters of the base model, similar in philosophy to external RAG designs. However, unlike traditional RAG, Memory Decoder encodes knowledge into an external decoder module, eliminating the need for real-time retrieval from an external knowledge base during inference. This allows it to achieve the inference speed of parameterized internalization.

This design eliminates external retrieval overhead while maintaining the integrity of the base model and the swappability of the external knowledge module.

## Core Mechanism

- **Plug-and-play**: Does not modify base model parameters; external modules can be freely attached.
- **Eliminate Retrieval Overhead**: Knowledge is encoded into the decoder module, requiring no external retrieval during inference.
- **Base Model Integrity**: Keeps the original model parameters unchanged.
- **Speed and Flexibility**: Combines the flexibility of RAG with the inference efficiency of parameterized methods.

## Task

- QA
- Language Modeling
