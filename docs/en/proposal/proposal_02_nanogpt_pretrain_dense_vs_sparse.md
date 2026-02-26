# Proposal 02: The Cross-over Effect in Continual Learning based on nanochat

## Motivation

Based on my current reading, most continual learning research focuses on mitigating catastrophic forgetting, aiming to retain as much prior knowledge as possible. However, human learning appears different—we naturally forget early or low-value facts as we grow, ultimately tending toward becoming **domain experts** (while retaining fundamental logic and general language skills).

This leads to a testable hypothesis (tentatively named the **Cross-over Hypothesis**): **A continual learning model might initially underperform a baseline model, but after multiple rounds of fine-tuning, it may surpass the baseline at a certain point and, under specific settings, approach or exceed the baseline's fine-tuning limit.**

If this hypothesis holds, exploring more sustainable continual learning architectures may require sacrificing some of the initial compression and generalization advantages of Dense Transformers. If a novel architecture (e.g., native sparsity) demonstrates better long-term evolutionary potential after extensive target domain fine-tuning, then this trade-off in "initial capacity" is worth investigating.

## Hypotheses

### H1 (Initial Capability Gap)

Given identical pre-training compute and data, traditional Dense Transformers, due to their global attention and dense backpropagation, may exhibit stronger initial general knowledge and lower perplexity compared to "novel architectures with independent isolation mechanisms (e.g., native sparsity)".

### H2 (The Cross-over Effect)

During multiple rounds of continuous fine-tuning on a specific target domain:

- **Baseline Model (Dense):** Constrained by cross-inherited weights, it may encounter a bottleneck in absorbing the target domain earlier. Its target performance gains may decelerate, accompanied by a risk of degraded general capabilities.
- **Continual Learning Architecture Model (Sparse, etc.):** Per the Cross-over Hypothesis, its **initial capability may be lower than the baseline** (a lower starting point). However, if mutual overwriting is reduced, it could maintain steady improvement over longer fine-tuning sequences, eventually crossing over the baseline to form an observable intersection curve.

## Methodology

### Baseline Configuration

- **Base Scale:** nanochat (~561M parameters, depth=20 as officially recommended), ensuring high efficiency and feasibility when validating such fundamental pre-training hypotheses.
- **Decoupled Evaluation System:**
  - **General Intelligence Baseline:** Tests only fundamental language fluency and basic logical inference (allows forgetting specific encyclopedic facts but prohibits losing underlying "reasoning fluency").
  - **Target Domain (Complex Domains):** E.g., in-depth medical long contexts, complex codebases, or proprietary enterprise knowledge.

### Phase A: Pre-training

Pre-train both architectures from scratch using the same general corpus (e.g., a subset of FineWeb-Edu):

1. `Model-Dense`: Standard nanochat structure.
2. `Model-CL`: nanochat with specialized continual learning mechanisms (e.g., incorporating the structured sparsity design from Proposal 01 to limit cross-inheritance).
   _Checkpoint: Verify on the general knowledge test set whether `Model-Dense` holds an initial performance advantage._

### Phase B: Continual Domain Evolution

Deploy both pre-trained models simultaneously into the target domain (Domain X) for continuous, streaming, long-sequence fine-tuning.

- At each data injection milestone (e.g., every 10M Tokens) acting as an Epoch node, simultaneously evaluate both models on the Domain X specialized test and the general baseline test.
- Plot two comparative capability evolution curves against training time/data volume.

## Compute Cost Evaluation

Given the moderate scale of nanochat (561M), the end-to-end compute for "pre-training + continual fine-tuning" is highly manageable (about a week on a single A100, or a few days on an 8×H100 cluster for Phases A and B). This enables preliminary exploration of whether "fundamental architectural adjustments are worthwhile" without relying on massive models.

## Expected Outcomes

### Core Observation: Domain Cross-over Curve

Plot a line chart with the X-axis as "Token injection volume during continuous fine-tuning" and the Y-axis as "Domain X Performance". If the Cross-over Hypothesis holds, we expect: on the left (initial phase), `Model-CL` underperforms `Model-Dense`; in later phases, `Model-CL` intersects with `Model-Dense` and may reach a higher peak under certain settings. Naturally, it is also possible that no cross-over is observed, which itself would be a valuable finding.

### Auxiliary Observation: General Baseline Maintenance

Observe the difference in forgetting rates between the models on the general intelligence baseline. Evaluate whether `Model-CL` acts more like "selectively forgetting non-essential facts" rather than suffering significant degradation in fundamental language capabilities.
