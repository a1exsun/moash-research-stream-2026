# Character-LM / CharacterGLM

**Paper:** Character-LM / CharacterGLM
**Source:** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**Category:** Parametric Memory — Internal — Post-Train

---

## Problem

How can an LLM be made to stably exhibit a specific character's personality, knowledge background, and behavioral patterns during interaction?

## Method

Character-LM and CharacterGLM fine-tune LLMs to become models with distinct character traits. During the post-training phase, personalized memory is injected into the model parameters through SFT (Supervised Fine-Tuning), enabling the model to consistently and continuously play a specific role.

This approach represents a typical paradigm of parametric character/persona injection: by encoding character knowledge, speaking style, values, and other information into the model weights, it achieves more stable and deep role-playing capabilities than prompt-based methods.

## Core Mechanism

- **SFT Character Injection**: Encodes character traits into model parameters through supervised fine-tuning.
- **Personalized Memory**: The character's knowledge background, language style, values, etc., are parametrically stored.
- **Parametric Personality**: Character information is deeply integrated into model weights rather than being provided solely through prompts.

## Task

- Role Playing
