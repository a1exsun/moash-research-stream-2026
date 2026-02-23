# MemGen — Zhang et al. 2025

- **Paper**: Zhang et al. (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — LoRA Fragments
- **Task**: QA, Math, Code, Embodied Task, Reasoning
- **Optimization**: RL, SFT

## Core Mechanism

MemGen dynamically generates latent memory during the decoding process, implementing memory triggering and weaving through two specialized modules.

- **Memory Trigger**: Monitors the agent's reasoning state to judge when explicit memory invocation is needed and determines where in the decoding process to insert memory fragments.
- **Memory Weaver**: Utilizes the agent's current state to construct latent token sequences, deciding what memory content to insert.
- Uses two LoRA adapters to separately implement the functions of the Memory Trigger and Memory Weaver.
- Dynamically generates latent memory during decoding instead of relying on pre-stored static representations.
- Jointly optimizes memory invocation timing and content quality through RL and SFT.
