# MAC — Amortize Context

**Paper:** MAC (Amortize Context)
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — External — Auxiliary LM

---

## Problem

How can volumes of document information be efficiently encoded into reusable compact representations, avoiding the need to process the full context for every inference?

## Method

MAC uses an amortization network to compress information from new documents into compact modulations, which are stored in a memory bank. During inference, the model adjusts its behavior by retrieving relevant modulations without re-processing the original documents.

This method amortizes the computational cost of context processing into an offline encoding phase, allowing the model to load only compact modulation parameters during inference, significantly improving efficiency.

## Core Mechanism

- **Amortization network**: Compresses document information into compact modulation representations.
- **Memory bank**: Stores all encoded modulations and supports efficient retrieval.
- **Context Compression**: Compresses long documents into parameterized compact representations.
- **Inference Acceleration**: Loads modulations during inference instead of processing full documents.

## Task

- QA
