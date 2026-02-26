# Proposal 01: Ablation Experiments on Continual Learning Mechanisms

## Motivation

Based on existing literature, strategies for mitigating catastrophic forgetting can be broadly categorized into two types. I aim to quantitatively separate their respective contributions and potential interaction effects while controlling for model scale and baseline capability:

1. **Sparse Topology**: One hypothesis suggests that sparse connections may help reduce cross-interference among parameters.
2. **Experience Replay**: Often considered analogous to the memory consolidation process during sleep in the brain, it maintains old knowledge by integrating historical data.

The two research questions to explore:

- What is the individual impact of each mechanism on continual learning?
- Is there a positive synergistic effect when both are combined?

## Hypotheses

### H1 (Role of Sparse Topology)

Replacing a dense architecture with a sparse one may provide parameter isolation that helps mitigate weight cross-interference, thereby reducing the extent to which old knowledge is overwritten during fine-tuning.

### H2 (Role of Experience Replay)

Experience replay via mixing historical data may help consolidate old knowledge within the network, improving the overall retention rate in continual learning.

### H3 (Interaction Effect)

If sparse topology and experience replay are complementary—where sparse topology reduces physical structural conflicts and experience replay consolidates feature representations—their combined effect on mitigating forgetting may surpass the simple sum of their individual contributions.

## Experimental Design

### Baseline Configuration

- **Backbone**: nanochat official recommended weight scale (depth=20, approx. 561M parameters)
  - 20-layer Transformer, model dimension 1280, 10 attention heads (128 dimensions per head)
  - Vocabulary size 65,536 (2^16), context length 2,048
  - BFloat16 precision, Muon optimizer (for matrix parameters) + AdamW (for embedding parameters)
- **Data**: Fixed sequential multi-domain tasks (e.g., Code -> Math -> Medical -> Legal -> Dialogue)
- **Training**: Identical hyperparameters including token count, steps, optimizer, and batch size.

### Ablation Groups (2x2)

Four ablation groups constructed using a dual-mechanism toggle:

- `T0 R0`: Dense baseline (no sparsity, no replay)
- `T1 R0`: Sparse topology only (e.g., MoE or 2:4 block sparsity, no replay)
- `T0 R1`: Experience replay only (dense baseline + mixed data replay)
- `T1 R1`: Sparse topology + experience replay

Where:

- `T` = Topology mechanism
- `R` = Replay mechanism

**Fairness Principle:** Report comparisons under both matched-FLOPs and same-shape settings. Execute ≥3 different random seeds per experimental group to eliminate variance.

## Compute Cost Evaluation

Estimated computational cost based on the nanochat (561M) scale:

### Basic Assumptions and Validation

- **Model Parameters**: 561M parameters (nanochat depth=20 official recommended configuration).
- **Training Data Volume**: Total training data across 5 domains is capped at 5B tokens, approx. 1B tokens per domain.
- **Theoretical Compute**: `6 × 561M × 5B = 1.68e19 FLOPs`.
- **Hardware Efficiency**: Effective compute of a single Nvidia A100 (80GB) is conservatively estimated at 150 TFLOPs (`1.5e14 FLOPs/s`).

### Duration per Run

- **Single Run Duration**: `1.68e19 / 1.5e14 ≈ 112,000 seconds` ≈ **31 GPU hours (Single A100)**.
- If using an 8×H100 cluster (nanochat official recommended configuration), a single training run can be compressed to roughly **4-5 hours**.

### Total Experiment Cost

- **Total Training Runs**: 4 ablation groups × 3 different random seeds = **12 independent runs**.
- **Total Compute Time**: `12 × 31 ≈ 373 A100 GPU hours`.
- **Financial and Time Cost**:
  - Renting cloud A100s ($2/h) costs approximately **$750 USD**.
  - Using an 8×H100 cluster node ($24/h), `12 × 5h = 60 node hours`, costs approximately **$1,440 USD**, but all experiments can be completed in **roughly 3 days**.
  - Serial execution on a single A100 card requires roughly **16 days**.
  - Factoring in extra debugging and friction costs, the full suite can be completed within **3-4 weeks**.

## Expected Outcomes

1. Quantitative mechanism contribution mapping (main effect and interaction effect analysis).
2. Preliminary empirical data at the nanochat 561M scale, providing a reference for whether it is worth scaling up to larger parameters.
