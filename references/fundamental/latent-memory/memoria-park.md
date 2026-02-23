# Memoria — Park et al. 2024

**Paper:** Park et al. (2024)
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Latent Memory — Generate

---

## Problem

Existing memory mechanisms in language models are limited by explicit token sequence representations and lack the capability for implicit memory representation similar to latent memory traces (engrams) in the human brain, making it difficult to efficiently model long-range dependencies.

## Method

Constructs a three-layer memory structure and introduces biologically inspired engrams as latent memory representations. Core design:

- **Three-layer Memory Architecture** — Designs a multi-layered memory storage structure, where different layers are responsible for memories of various time scales and levels of abstraction.
- **Engrams (Memory Traces)** — Inspired by the concept of engrams in neuroscience, it introduces latent memory representation units, analogous to clusters of neurons that encode memory in biological neural systems.
- **Latent Memory Generation** — Creates and updates latent memory representations through generative methods rather than relying solely on explicit token storage.
- **Biologically Inspired Design** — The processes of memory formation, consolidation, and retrieval draw on memory theories from cognitive neuroscience.

## Impact

Memoria introduces the concept of engrams from cognitive neuroscience into the memory design of language models, opening a new direction for latent memory. The combination of three-layer memory and engrams provides a theoretical and practical reference for building AI systems that closer resemble biological memory mechanisms.

## Task

- Language Modeling
