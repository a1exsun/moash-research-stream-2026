# MEMIT — Mitchell et al. 2023

**Paper:** Mitchell et al. (2023) — Mass-Editing Memory in a Transformer
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Post-Train

---

## Problem

Existing knowledge editing methods (such as ROME) can only edit a single fact at a time and cannot efficiently perform bulk updates on large amounts of knowledge, limiting scalability in practical applications.

## Method

MEMIT (Mass-Editing Memory in a Transformer) further extends ROME to support batch editing. Through multi-layer residual distribution and batch formulas, MEMIT can simultaneously update thousands of facts, significantly improving the scalability of knowledge editing.

The core idea is to distribute editing targets across multiple relevant MLP layers rather than concentrating them on a single layer, thereby supporting large-scale parallel editing while maintaining edit quality.

## Core Mechanism

- **Multi-layer Residual Distribution**: Distributes editing signals into MLPs across multiple Transformer layers.
- **Batch Editing Formula**: Supports simultaneous processing of a large number of fact update requests.
- **Scalability**: Extends from single-fact editing to batch editing of thousands of facts.

## Task

- QA
- Model Editing
