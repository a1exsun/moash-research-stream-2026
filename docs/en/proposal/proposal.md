## Research Proposals

This note briefly documents my research process and introduces several research proposals that emerged along the way. I hope to get your feedback to select the most suitable proposal as the direction for my minor thesis, or to derive other valuable research directions based on my current progress.

## Ablation Experiments

My thinking starts with comparing the continual learning mechanisms of the human brain with LLMs. I believe that structural sparsity in the human brain (rather than merely MoE or activation sparsity) and the neocortex-hippocampus separation mechanism are particularly critical.

I hypothesize that the dense nature of the standard Transformer architecture physically constrains the continual learning capability of LLMs. If a weight simultaneously encodes multiple concepts (superposition), any fine-tuning update is likely to disrupt existing knowledge.

Furthermore, the most crucial continual learning mechanism in the human brain stems from the separation of the neocortex and hippocampus. During sleep, the brain replays short-term memories from the hippocampus to the neocortex for consolidation. Although I have seen papers attempting to simulate this process (such as mixing old and new data during fine-tuning to simulate experience replay), I have struggled to find quantitative conclusions on how significantly these processes improve continual learning in models.

Therefore, I think we could design an ablation study based on a small-scale model like nanochat to systematically investigate these questions and gather initial quantitative evidence. I believe this has value because nanochat shares similar architectural characteristics with SOTA models, which could optionally provide insights for subsequent scaling research.

Based on this hypothesis, I formulated **[Proposal 01](proposal_01_ablation_experiments.md)**.

## The Cross-over Hypothesis

While designing the ablation study, an idea occurred to me: many researchers focus on SOTA models, attempting to mitigate catastrophic forgetting through complex mechanisms. But is it possible that even human continual learning is not omnipotent? Humans actually forget large amounts of old knowledge daily. As we age and accumulate knowledge, we tend to become domain experts (or generalists without deep expertise).

Perhaps we could adjust our objective: under an ideal continual learning architecture, a model might gradually evolve from a general-purpose model into a domain expert. It must retain general intelligence (e.g., logical reasoning, language abilities), but we could allow it to forget knowledge outside the target domain, focusing mainly on evaluating its capabilities within that domain. For instance, we may care more about whether it retains conversational history with a user or masters specific enterprise knowledge, rather than emphasizing irrelevant dimensions like coding or literature.

Extrapolating further, I propose a central "cross-over hypothesis": A continual learning model might initially underperform a baseline model (because constructing a continual learning architecture might require sacrificing some of the Transformer’s natural information compression and generalization capabilities. Its global attention and dense updates grant strong initial capacities but might constrain continual learning performance). However, if this new continual learning model can surpass the equivalent-scale Transformer baseline after multiple rounds of continual fine-tuning in target domains—or even approach the inherent fine-tuning ceiling of the baseline—then this architectural trade-off of "initial capability" warrants further investigation.

This is not standard domain fine-tuning, nor is it merely a domain-specific model; it is a model equipped with true continual learning capabilities. Compared to traditional domain fine-tuning or domain models, it can continuously absorb new knowledge within the target domain without being forced to learn entirely disparate fields every day. I think this resembles human learning. For example, my first job was in Java development, but after years without writing Java code, I have forgotten most of its syntax and frameworks. I can assume that if I step away from development or research for years, I would continue to forget most knowledge in this domain.

Based on this hypothesis, I formulated **[Proposal 02](proposal_02_nanogpt_pretrain_dense_vs_sparse.md)**.

## Potential Sparsity in Scaled Dense Models

As I gained deeper insight into current LLM architectures, I realized that scale itself might be a critical factor.

Under the ongoing expansion of scaling laws, could implicit sparsity emerge within dense LLM models? Perhaps the overlap in activation pathways between entirely different skills or distinct pieces of knowledge becomes lower, thereby minimizing interference during fine-tuning.

I think this is also worth investigating deeply. However, rather than simply constructing an experiment, I believe a viable strategy for dealing with SOTA models is to directly design a fine-tuning architectural modification oriented around the continual learning problem, and to verify whether this sparsity actually exists in the process.

Based on this hypothesis, I formulated **[Proposal 03](proposal_03_sota_sparse_conversion.md)**.

## Benchmark

In my broad review of relevant papers, I found that evaluation frameworks for continual learning are relatively concentrated. Whether evaluating continual pre-training, continual fine-tuning, or engineering-based memory, the benchmarking relies mainly on constructing static datasets (such as TiC-LM, EvoWiki, etc.). To date, tools like MemoryBench also combine public datasets with an LLM-as-User-Simulator to perform simulated evaluations.

My thought is that, in applied scenarios, static benchmark scores are often insufficient. We typically refer to real user feedback, such as LLM Arena or Reddit/X discussions. Currently, such evaluation systems are rare in the continual learning field. I think it might be worth attempting to build one. Coincidentally, I have developed an AI companionship application centered on structured narratives. It might be possible to build an evaluation system relying on Human Feedback upon this foundation (since users inherently care about which LLM best aligns with plot frameworks and retains historical memory during long-range narratives, making their perception highly accurate).

Based on this hypothesis, I formulated **[Proposal 04](proposal_04_benchmark.md)**.

## NSA (Native Sparse Attention)

In exploring the latest LLM evolution trends, I noticed that NSA / DSA / MLA appear frequently in some open-source models from 2025–2026. Below are a few examples I've been following:

- DeepSeek v3.2: Uses DSA (DeepSeek Sparse Attention) to achieve native sub-quadratic sparse attention.
- Qwen v3.5: Uses Gated DeltaNet in a 3:1 hybrid architecture with full attention.
- Kimi K2.5: Uses a 3:1 hybrid architecture with KDA and MLA.
- GLM-5: Retains the traditional Transformer structure but introduces DSA and MLA.
- MiniMax M2.5: Adopts the Lightning Attention fully linear framework.

I noted that DSA’s native design—which decouples attention computation topology into a "compressed common sense stream" and an "exclusively focused fine-grained stream"—might offer a compelling direction to test. If used asymmetrically during continual fine-tuning (e.g., updating only the focused stream while freezing or slowing down the compressed stream), large models might exhibit superior resistance to forgetting.

However, I found that the computational budget required for this direction is quite high, as existing open-source sparse attention models are generally quite large. Thus, I haven't yet identified a safer way to proceed.

## Small-scale Validation

Native DSA open-source models are typically large, meaning the experimental compute required for exploratory validation would significantly exceed my current budget. Meanwhile, current 100M-parameter-scale "small sparse models" are generally only MoE at the FFN layer, making it difficult to directly validate the effectiveness of Attention layer decoupling.

Therefore, I think we could potentially leverage open-source DSA / Indexer operators to pre-train a small-scale DSA architecture (e.g., ~0.1B scale) from scratch on a small dataset, and then run a controlled experiment against a conventional Transformer.

Based on this hypothesis, I formulated **[Proposal 05](proposal_05_dsa_tiny_sandbox.md)**.
