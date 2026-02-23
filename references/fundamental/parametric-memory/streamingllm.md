# StreamingLLM (2023)

**Paper:** (2023)
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Pre-Train

---

## Problem

When processing ultra-long sequences, standard Transformers face memory and time overhead for attention calculations that grow with sequence length. Furthermore, model performance drops sharply once the sequence exceeds the training length, making it unable to support streaming scenarios.

## Method

The Attention Sink mechanism is discovered and utilized to optimize attention calculation efficiency and enhance long-window memory capability. Core design:

- **Attention Sink Discovery** — Discovers that models tend to assign a large amount of attention weight to the first few tokens of a sequence (i.e., attention sinks), even if these tokens are not semantically important.
- **Sink Token Retention** — Always retains the first few sink tokens in sliding window attention, ensuring the stability of the attention distribution.
- **Sliding Window + Sink** — Combines a fixed-size sliding window with sink tokens to achieve efficient processing of infinitely long sequences within limited memory.
- **No Fine-tuning Required** — This method can be directly applied to pre-trained models without additional training.

## Impact

StreamingLLM reveals the important phenomenon of attention sinks in Transformers, providing a simple and effective engineering solution for long-sequence processing. This discovery is instrumental for understanding Transformer attention behavior and designing more efficient methods for handling long sequences.

## Task

- QA
- Reasoning
