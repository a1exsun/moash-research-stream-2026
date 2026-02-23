# Meta SMF (Sparse Memory Finetuning) — Jessy Lin et al.

**Paper:** Jessy Lin et al. (2025)
**Source:** Machine Heart Pro Week 07 (Mentioned, see Pro 2025 Week 46 for details)
**Category:** LLM Memory — Sparse Memory Pool

---

## Problem

Full fine-tuning leads to catastrophic forgetting (forgetting rate of 89%).

## Method

An additional 1B-parameter sparse memory pool is attached to a 1.3B base model, where only highly activated memory slots are updated each time. All dense layers are frozen, and only the memory pool is updated.

## Results

The forgetting rate dropped from 89% in full fine-tuning to 11%.

## Limitations

- By freezing all dense layers, the model's core reasoning ability cannot be improved.
- Tests were only conducted on factual memory (TriviaQA) and did not involve continual learning at the ability/skill level.
- Essentially an external learnable vector attachment, similar to trainable RAG.
