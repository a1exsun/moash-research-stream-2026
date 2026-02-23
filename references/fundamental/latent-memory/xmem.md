# XMem — Cheng et al. 2022

- **Paper**: Cheng et al. (2022)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Multimodal
- **Task**: Video Segmentation

## Core Mechanism

XMem is used for long video object segmentation, encoding each frame into key-value latent embeddings and organizing them into multi-stage memory.

- Encodes each video frame into key-value latent embeddings, serving as basic memory units.
- Organized into a multi-stage memory hierarchy:
  - **Perceptual memory**: Stores high-fidelity representations of the most recent frames.
  - **Working memory**: Maintains active information at an intermediate granularity.
  - **Long-term memory**: Stores critical information across long time spans.
- Uses the LFU (Least Frequently Used) strategy to remove low-frequency entries, controlling memory capacity.
- Achieves efficient object tracking and segmentation in long videos through multi-stage memory management.
