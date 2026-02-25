## Continual Learning Architectures in the Human Brain

My thoughts start by comparing the human brain and current LLM architectures.

## Ablation Experiments

My guess is that the dense nature of the Transformer architecture might physically limit the continual learning ability of LLMs. If a weight parameter inherits many different bits of knowledge (superposition), then any fine-tuning change will inevitably destroy some of the old knowledge.

Also, the most important continual learning mechanism in the brain comes from the separation of the neocortex and the hippocampus. The brain replays short-term memories from the hippocampus to the neocortex during sleep to save them. Although I have seen some papers trying to simulate this process (e.g., mixing old and new data during fine-tuning to simulate experience replay), I find it hard to find a clear, quantitative conclusion on how much these processes actually help a model's continual learning.

So I think maybe we can design an ablation experiment, based on a small-scale model like nanochat, to systematically study these issues and give quantitative results. I think this has value because nanochat and SOTA models share similar architecture features, and we can use scaling to guess how SOTA models will perform.

Based on this hypothesis, I prepared Proposal 01.

## Cross-over Hypothesis

While thinking about the design for the ablation experiments, I had an idea: many researchers are focused on SOTA models, trying to build complex mechanisms to slow down catastrophic forgetting. But is it possible that human brain's continual learning is also not perfect? Humans actually forget a lot of old knowledge every day, and as we grow and learn, we tend to become domain experts (or a person who knows a bit of everything but masters nothing).

So the goal should change: in an ideal continual learning system, a model would still evolve from a general-purpose model into a domain expert. It still needs to keep its general intelligence (e.g., logic, language skills, etc.), but we allow it to forget knowledge outside its target field. We only care if it keeps all the skills for its target area—like having all the memories of a conversation or knowing a specific company's data—and we stop checking its coding or literature skills.

Further, I propose a core cross-over hypothesis: a continual learning model's initial capability is often inferior to that of a baseline model (because building a continual learning architecture might require sacrificing some of the Transformer's natural capacity for data compression and generalization, as global attention and dense updates provide strong initial power but limit continual learning performance). However, if this new continual learning architecture, after multiple rounds of continuous fine-tuning in the target domain, can not only surpass the baseline Transformer model of the same size, but also break through the baseline model's own fine-tuning limit, achieving a clear cross-over, then this sacrifice of "initial capability" is highly valuable.

This is not domain fine-tuning or a domain-specific model, but a model that can keep learning. Compared to traditional domain models, it can keep absorbing new knowledge in its field, but we don't ask it to learn completely different fields every day. I think this is just like humans. For example, my first job was Java development, but since I haven't written Java in years, I've forgotten most of its syntax and frameworks. If I stop doing research or development for many years, I would probably forget most of this field too.

Based on this hypothesis, I prepared Proposal 02.

## Compression-Writability Bound

While exploring the cross-over hypothesis, I realized a deeper problem: the stability-plasticity dilemma is often mentioned in continual learning, but it has always been a vague idea. It has never been turned into a math problem that we can prove or disprove.

I am trying to look at this from the angle of "activation sparsity." The core logic is: models squeeze multiple concepts into the same set of parameters (superposition). Activation sparsity determines how much writing new knowledge interferes with old knowledge. For any system that uses only one fixed activation mode (single-regime), there should be a math "capacity ceiling" for "number of tasks × depth of learning per task." To break this ceiling, you need at least two subsystems with different sparsity levels working together—this matches how the brain uses the hippocampus (extremely sparse, fast recording) and the neocortex (moderate density, deep compression).

If this theory is true, it explains why current methods like EWC and GPM eventually fail on long sequences—they are always working under the ceiling of a single system. Even if the theory is wrong, it is still a useful result.

Based on this hypothesis, I prepared Proposal 03.

## Hidden Sparsity in Scaled Dense Models

While learning about current LLM architectures, I realized: maybe scale itself is the core issue?

Under scaling laws, maybe LLMs naturally develop hidden sparsity? Maybe different skills and knowledge are naturally separate (orthogonal), so fine-tuning one doesn't hurt the others.

I think this is worth studying. But instead of just making experiments, I think the best strategy for SOTA models is to design a fine-tuning change specifically for continual learning and see if this sparsity actually exists during the process.

Based on this hypothesis, I prepared Proposal 04.

## Benchmark

While reading papers, I found that current testing for continual learning is very limited. Whether it's for continual pre-training, fine-tuning, or memory, most of them just use datasets to get scores (e.g., TiC-LM, EvoWiki). Even the newest result, MemoryBench, uses 11 datasets and "LLM-as-User-Simulator" to test.

My thought is: as a software developer, I never care about static CodeBench scores (and I think many others are the same). We only care about real user feedback like LLM Arena or Reddit/X discussions. Continual learning doesn't have a system like that, so I want to build one. I have a structured narrative AI companion app, and maybe I can build a system on top of it that uses human feedback (users naturally care which LLM follows the story and history best, and they can clearly feel the difference).

Based on this hypothesis, I prepared Proposal 05.

## NSA (Native Sparse Attention)

Looking at the latest LLM trends, I noticed that NSA is becoming the core trend for 2025-2026. Almost all SOTA open-source LLMs use NSA/DSA/MLA mechanisms:

- **DeepSeek v3.2**: Uses DSA (DeepSeek Sparse Attention) for native sub-quadratic sparse attention.
- **Qwen v3.5**: Uses a 3:1 mix of Gated DeltaNet and Full Attention.
- **Kimi K2.5**: Uses a 3:1 mix of KDA and MLA.
- **GLM-5**: Keeps the traditional Transformer but adds DSA and MLA.
- **MiniMax M2.5**: Uses the Lightning Attention linear framework.

I noticed that DSA's design—decoupling attention into a "compressed global flow" and a "selective fine-grained flow"—might be the key to solving catastrophic forgetting. If we use this asymmetrically during fine-tuning (only update the selective flow and freeze or slow down the compressed flow), large models might become very resistant to forgetting.

However, I found that the compute budget requirements for this direction are too high. All open-source sparse attention models are too big, so I haven't found a good way to move forward yet.

## Small-scale Validation

Open-source DSA models are all tens of billions of parameters, which is way over my compute budget. On the other hand, current small "sparse" models (around 100M) are usually just FFN-level MoE, which can't prove if decoupling the Attention layer works.

So I think we can use open-source DSA/Indexer operators to pre-train a small DSA model (e.g., ~0.1B level) from scratch on small datasets, and then compare it directly with a traditional Transformer.

Based on this hypothesis, I prepared Proposal 06.
