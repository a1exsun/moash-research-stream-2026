# Proposal 06: Tiny-DSA Sandbox Pre-training Validation for Continual Learning

## Research Motivation

If "retrofitting attention structures onto existing models" (as discussed in Proposal 04) faces incompatibility between the pre-trained distribution and new mechanisms—thereby lacking the persuasiveness of controlled experiments—then building a minimal sandbox model from scratch based on DeepSeek's native Dynamic Sparse Attention (DSA) architecture may offer a cleaner path for mechanism validation.

Since the core objective is to test the hypothesis that "separated attention pathways help mitigate forgetting," we can decouple from production-scale large models and conduct end-to-end preliminary validation at a minimal scale (~100M parameters) on compact corpora such as TinyStories.

### Research Question in One Sentence

At sandbox scale (~100M parameters), can we replicate and pre-train a network built around DeepSeek DSA's core operators—featuring "compression flow and focused flow"—and, when compared against a standard dense network of equal size and data distribution, demonstrate that conditional sparse routing architectures exhibit better forgetting mitigation under certain settings after multiple rounds of continual fine-tuning?

## Hypotheses

### H1: DSA Topology Remains Functionally Valid at Toy Scale (Isomorphism at Toy Scale)

We hypothesize that DeepSeek's DSA (Indexer + Top-K Selection) and MoE-style mechanisms, despite originating in ultra-large-scale settings, can still achieve basic autoregressive generation convergence when scaled down to 4–8 layers and ~100M parameters on clean small-scale datasets like TinyStories. That is, **the dual-stream pathway may retain partial functionality at toy scale**. This hypothesis itself also requires experimental verification.

### H2: Conditional Sparse Routing Mitigates Forgetting During Continual Fine-tuning (Sparse Routing Mitigates Forgetting)

When the same continual fine-tuning task stream is injected into models of the same ~100M scale:

- **Native Dense architecture**: After multiple rounds of fine-tuning, mutual overwriting of global attention and MLP weights may cause notable degradation of base generation capabilities (Catastrophic Forgetting).
- **Tiny-DSA (with asymmetric fine-tuning strategy)**: Because the gradient flow of newly injected knowledge is confined to **Selected Attention (focused flow) and specific routings**, performance degradation on old tasks under the same fine-tuning intensity may be lower than that of the Dense control group.

## Approach

### Minimal Native Sandbox Architecture Build (Tiny-DSA Architecture Build)

Strip away redundant components and borrow core operators from DeepSeek's open-source codebase:

- **Backbone**: 4–8 Transformer layers with hidden dimension `d_model = 512` or `768` (minimal total parameters).
- **DSA Operator Injection**: Integrate routing-flow modules with "Index selection and Top-K restart" directly into the self-attention layers. Explicitly separate shared heads (Shared Head / Compressed Flow) from task-specific matching heads (Selected / Routed Flow).
- **Dense Control Base**: An architecture with identical layer count and total neuron count, but using standard `nn.MultiheadAttention` and standard fully-connected FFN layers.

### Pre-training Phase (Lightning Pre-training)

Complete base language capability convergence on one or two consumer-grade GPUs.

- **Corpus**: `roneneldan/TinyStories` (only a few million synthetic fairy-tale tokens), or a minimalist grammar dataset.
- **Convergence Target**: Through 24–48 hours of single-GPU training, bring both the DSA-topology sandbox model and the Dense baseline to usable base generation quality on the test set (e.g., mastering "apples are red" and basic pronoun-grammar relationships).

### Multi-point Continual "Window-Breaking" Test

After both models have achieved equivalent base generation capabilities, introduce "rule-breaking" long-range incremental test sets (e.g., 50 artificially designed contradictory stories—"In World A, water flows upward"—as a Continuous Task Stream).

- **Asymmetric Continual Fine-tuning (ACFT) for Tiny-DSA**: Freeze Shared / Compressed Layers; only allow Selected layers to undergo iterative fine-tuning on these 50 new stories.
- **For the Dense model**: Apply EWC-constrained fine-tuning at the same intensity and duration, or even plain Vanilla SGD.
- **Forgetting Charting**: Track the Perplexity and Exact-Match Accuracy degradation ratios of both architectures, plot forgetting curve comparisons, and observe whether topology-level pathway isolation makes a meaningful contribution to forgetting mitigation.

## Compute Cost Estimate

- Pre-training (~100M model × TinyStories): ~24–48 hours on a single RTX 4090 × 2 models
- Continual fine-tuning (50 incremental tasks × multiple epochs): ~1–2 days on a single GPU × 2 models
- Total: ~1 week on a single RTX 4090, or ~3–4 days on an A100
- Codebase can be kept under 500 lines of PyTorch, with a relatively low reproduction barrier

## Expected Outcomes

1. **A network-topology perspective on forgetting**: Provide a complementary viewpoint for catastrophic forgetting research—beyond regularization methods (EWC, etc.), gradient projection (GPM/OGD), and experience replay—by exploring how network connectivity structure itself affects forgetting.
2. **High reproducibility**: The sandbox code can be kept under 500 lines of PyTorch, with main experiments reproducible on a single consumer-grade GPU, facilitating verification and extension by future researchers.
3. **Low-cost preliminary validation**: Leverage the core design principles of a frontier architecture (DSA) for proof-of-concept at small scale, providing directional evidence for whether larger-scale investment is warranted.
