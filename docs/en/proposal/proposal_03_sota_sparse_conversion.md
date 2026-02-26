# Proposal 03: Exploring Implicit Sparsity in SOTA Models and Sparse-Aware Fine-Tuning for Continual Learning

## Research Motivation

A question I find worth exploring: **Does model scale itself already mitigate interference in continual learning to some extent?**

As parameter counts and feature dimensions grow, SOTA-level large language models may naturally exhibit "implicit sparsity" — in high-dimensional semantic spaces, activation pathways for different domains may inherently have low overlap, thereby reducing the risk of mutual overwriting.

If this conjecture holds, then for existing large models, a viable research direction is: **introducing sparse-aware architectural modifications during fine-tuning to both probe the actual degree of implicit sparsity and leverage this property to mitigate forgetting in continual fine-tuning.**

## Hypotheses

### H1 (Implicit Sparsity Emerging from Scale)

As model feature dimensions increase, the neuron activation clusters and gradient distributions within a dense model when processing different tasks (e.g., coding vs. medical domains) may exhibit low overlap and near-orthogonal tendencies. Even if the base model is architecturally dense, it may possess a degree of logical sparsity in its feature pathways — though this still requires probing-based verification.

### H2 (Sparse-Aligned Fine-Tuning Modifications)

While preserving the dense architecture, introducing **"sparse-aware / orthogonality-preserving" modification layers during fine-tuning (e.g., activation-sparse-routed PEFT or orthogonal subspace low-rank parameter updates)** may help isolate gradient interference during fine-tuning. If large models do possess natural local sparse characteristics, such methods could leverage this property to reduce knowledge overwriting risk during sequential domain fine-tuning.

## Approach

### Base Configuration

- **Base model selection**: Select open-source SOTA models with "emergent-capability-level" scale and frontier architectures. Two specific candidates are under consideration:
  - **Qwen3.5-27B (Dense)**: A 27B fully dense architecture where all parameters are activated during every forward pass, yielding the highest inference density. Suitable as a dense baseline for probing implicit sparsity.
  - **Qwen3.5-35B-A3B (MoE)**: 35B total parameters / 3B active parameters, employing a Gated Delta Networks + MoE hybrid architecture. Its built-in conditional sparse routing allows direct observation of the correspondence between expert routing and tasks, providing a more natural entry point for sparse-aware fine-tuning.
- **Task sequence**: Multi-domain sequential setup (Code -> Math -> Medical -> General conversational reasoning).

### Fine-Tuning Architecture Modification Design

Beyond full fine-tuning and standard LoRA, explore a fine-tuning strategy that exploits "implicit task boundaries":

- **Approach A — Activation-Mask Tuning**: Freeze the main model body. Probe neuron activation patterns during forward passes on new-task samples, then selectively unfreeze or create side-branch updates only along high-activation pathways for the current task (constraining unrelated neurons from being affected by fine-tuning gradients via sparse masking).
- **Approach B — Implicit Orthogonal Subspace Mapping**: When introducing Adapters/LoRA, compute the orthogonal direction of the new-domain parameter delta relative to the historical gradients of old-domain parameters, attempting to grow new representations within the task's idle subspace.

### Visualization and Probing Verification

Beyond standard task-score evaluation across domains, dedicated probes should be designed to verify whether "implicit sparsity" actually exists:

- **Activation Overlap Analysis**: Compute the Intersection over Union (IoU) of Top-K activated neuron clusters across layers for two entirely different tasks.
- **Parameter Perturbation Tracking**: Compare the subspace representation drift — the displacement of core general-knowledge latent vectors in key subspaces — after absorbing target new knowledge, with and without the sparse fine-tuning architecture enabled.

## Compute Cost Estimate

Fine-tuning uses PEFT (LoRA/Adapter); inference requires forward passes for activation probing. Below are resource estimates for each candidate base model:

### Option A: Qwen3.5-27B (Dense)

- **Memory footprint**: BF16 weights ~54 GB; LoRA fine-tuning + activation cache ~70–90 GB; feasible on 1×A100-80GB (with gradient checkpointing enabled)
- Activation probing (per domain): single forward pass ~4–8 A100 GPU hours
- Fine-tuning (per domain): LoRA fine-tuning ~16–32 A100 GPU hours
- Full experiment across 4 domains + probing analysis: ~160–320 A100 GPU hours
- Cloud cost: ~$400–800

### Option B: Qwen3.5-35B-A3B (MoE)

- **Memory footprint**: Although only 3B parameters are activated, all 35B parameters must be loaded into GPU memory (BF16 ~70 GB); LoRA fine-tuning ~80–100 GB, requiring 1×A100-80GB (tight) or 2×A100-40GB
- Activation probing (per domain): Since only 3B parameters are activated per token, forward inference is significantly faster than the 27B Dense model, ~3–6 A100 GPU hours
- Fine-tuning (per domain): Gradients flow only through activated experts; LoRA fine-tuning ~12–24 A100 GPU hours
- Full experiment across 4 domains + probing analysis: ~120–240 A100 GPU hours
- Cloud cost: ~$300–600
- **Additional advantage**: MoE inherently provides expert routing logs, enabling direct analysis of expert selection patterns across different domain data without the need for custom-designed activation probes

## Expected Outcomes

1. **Empirical observations on implicit sparsity**: Through neuron- and subspace-level probing analysis, provide initial quantitative observations on the degree of activation pathway overlap across domains in SOTA-level large models, building evidence toward understanding the encoding relationship between "general capabilities" and "domain-specific skills" in large models.
2. **Exploration of continual-learning-oriented fine-tuning strategies**: Given observed implicit sparse characteristics (if they exist), provide a preliminary feasibility assessment of sparse-aware fine-tuning approaches for mitigating continual fine-tuning forgetting, offering directional guidance for more systematic method design in follow-up work.
