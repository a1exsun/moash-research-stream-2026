# Titans (2025)

- **Paper**: (2025)
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate — Neural Weights (MLP)
- **Task**: QA, Language Modeling

## Core Mechanism

Titans compress long-range information into online-updated MLP weights, using neural weights themselves as a form of memory.

- Encodes long-range context information into the weight parameters of an MLP, utilizing neural network weights as memory carriers.
- MLP weights are updated online during the inference process, dynamically absorbing new information.
- Produces latent vectors through the MLP during inference to inject memory content into current computations.
- Transforms traditional explicit KV storage into implicit parametric memory, encoding long-distance dependencies within the weight space.
