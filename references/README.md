# Research References

This directory serves as the project's "External Knowledge Base," containing all relevant academic papers, technical surveys, evaluation benchmarks, and specific technical solutions.

## Core Principles

1.  **Separation of Raw Data and Secondary Processing**: The `surveys/` directory and various raw paper folders store original materials in a read-only capacity.
2.  **First-Principles Classification**: All technical solutions must be distilled into atomic notes and integrated into the technical classification system within this directory.

## Directory Structure

- **[surveys/](./surveys/)** — Surveys & Foundations
  - Stores panoramic field surveys (PDFs, LaTeX, and corresponding full-text translations/excerpts).
- **[direct-facing/](./direct-facing/)** — Parameter and Latent State Solutions (Direct-Facing)
  - Stores models and algorithmic implementations that directly address the forgetting problem.
- **[evasion/](./evasion/)** — Context and Multi-Agent Solutions (Evasion)
  - Stores system solutions that bypass the forgetting problem through external architectures.
- **[eval/](./eval/)** — Evaluation Benchmarks
  - Stores benchmark designs for evaluating model continual learning and memory retention capabilities.
- **[pending/](./pending/)** — Pending Materials
  - Solutions or papers awaiting subsequent intensive reading and decomposition.

---

# Technical Solutions Index

A categorized index of all compiled technical solutions (Methods) based on first principles and technical essence.

---

## Surveys & Theory

| Document                                                                                                   | Source             | Focus                                                                    |
| :--------------------------------------------------------------------------------------------------------- | :----------------- | :----------------------------------------------------------------------- |
| [survey-memory-age-of-agents](surveys/survey-memory-age-of-agents.md)                                      | arXiv 2512.13564v2 | Three-dimensional framework for Agent Memory: Forms/Functions/Dynamics   |
| [survey-ai-memory-baijia](surveys/survey-ai-memory-baijia.md)                                              | Jiqizhixin Pro W07 | 4W classification system, three-layer AI Memory partition                |
| [survey-human-to-ai-memory](surveys/survey-human-to-ai-memory.md)                                          | Jiqizhixin Pro W07 | Memory analogy framework from a cognitive science perspective            |
| [AI Meets Brain](surveys/AI Meets Brain: Memory Systems from Cognitive Neuroscience to Autonomous Agents/) | Jiqizhixin Pro W07 | Unified perspective on human brain and Agent Memory                      |
| [tutorial-cl-of-llm](surveys/tutorial-cl-of-llm.md)                                                        | Tutorial Share     | Vertical/Horizontal CL tutorials and introduction to Continual Alignment |
| [survey-cl-of-llm](surveys/survey-cl-of-llm.md)                                                            | Survey Share       | LLM survey distinguishing between Vertical and Horizontal CL             |

---

# I. Evasion: Engineering Extensions and Workflow Architectures

These solutions attempt to bypass catastrophic forgetting through system-level scheduling, such as long contexts, external databases, and multi-agent workflows, achieving "pseudo-learning" (essentially information retrieval or external storage).

## Token-level Memory

### Flat (1D) — Topology-less

| Document                                                         | Core Mechanism                                                     |
| :--------------------------------------------------------------- | :----------------------------------------------------------------- |
| [memgpt](evasion/token-level-memory/memgpt.md)                   | OS metaphor, Main/External Context virtual memory hierarchy        |
| [mem0](evasion/token-level-memory/mem0.md)                       | Standardized memory CRUD operations, hybrid Graph + Vector storage |
| [think-in-memory](evasion/token-level-memory/think-in-memory.md) | Hash table storage for inductive thoughts, cluster-level fusion    |
| [comedy](evasion/token-level-memory/comedy.md)                   | Single model for memory generation, compression, and reuse         |
| [openclaw](evasion/token-level-memory/openclaw.md)               | Engineering solution for cross-session personalized memory         |

### Planar (2D) — Single-layer Structured

| Document                                         | Core Mechanism                                                       |
| :----------------------------------------------- | :------------------------------------------------------------------- |
| [hat](evasion/token-level-memory/hat.md)         | Hierarchical Aggregation Tree, coarse-to-fine retrieval              |
| [memtree](evasion/token-level-memory/memtree.md) | Dynamic hierarchical schema, bottom-up summary updates               |
| [a-mem](evasion/token-level-memory/a-mem.md)     | Card-based memory units, semantic links constructing memory networks |
| [d-smart](evasion/token-level-memory/d-smart.md) | KG + Reasoning Tree hybrid, neuro-symbolic pipeline                  |

### Hierarchical (3D) — Multi-layer Interconnected

| Document                                                                       | Core Mechanism                                                                          |
| :----------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| [graphrag](evasion/token-level-memory/graphrag.md)                             | Recursive aggregation via community detection, multi-layer graph indexing               |
| [hipporag](evasion/token-level-memory/hipporag.md)                             | Neurobiologically inspired, dual-layer graph + PageRank retrieval                       |
| [arigraph](evasion/token-level-memory/arigraph.md)                             | Unified semantic KG + episodic component within a graph                                 |
| [zep](evasion/token-level-memory/zep.md)                                       | Three-layer temporal KG (Episodic/Semantic/Community)                                   |
| [g-memory](evasion/token-level-memory/g-memory.md)                             | Three-layer graph (interaction/query/insight), shared across multi-agents               |
| [lyfe-agents](evasion/token-level-memory/lyfe-agents.md)                       | Working/Short-term/Long-term three-layer social simulation                              |
| [inside-out-personatree](evasion/token-level-memory/inside-out-personatree.md) | Hierarchical persona memory schema and operational updates                              |
| [hipporag-2](evasion/token-level-memory/hipporag-2.md)                         | Evolution from RAG to hippocampus-like multi-hop retrieval and long-term memory systems |

---

## Experiential Memory

### Case-based — Raw Trajectories/Solutions

| Document                                          | Core Mechanism                                            |
| :------------------------------------------------ | :-------------------------------------------------------- |
| [expel](evasion/experiential-memory/expel.md)     | Trial-and-error accumulation, hybrid trajectory + insight |
| [synapse](evasion/experiential-memory/synapse.md) | Abstracted state-action episodes as in-context examples   |

### Strategy-based — Insights/Workflows/Patterns

| Document                                                                | Core Mechanism                                                |
| :---------------------------------------------------------------------- | :------------------------------------------------------------ |
| [reflexion](evasion/experiential-memory/reflexion.md)                   | Short-term trajectory + long-term self-reflection feedback    |
| [buffer-of-thoughts](evasion/experiential-memory/buffer-of-thoughts.md) | Meta-buffer thought template retrieval and instantiation      |
| [awm](evasion/experiential-memory/awm.md)                               | Extraction of reusable workflows from successful trajectories |

### Skill-based — Executable Code/Functions/APIs

| Document                                                                    | Core Mechanism                                                  |
| :-------------------------------------------------------------------------- | :-------------------------------------------------------------- |
| [voyager](evasion/experiential-memory/voyager.md)                           | Continuously growing executable skill code library in Minecraft |
| [darwin-godel-machine](evasion/experiential-memory/darwin-godel-machine.md) | Secure self-rewriting code, recursive self-modification         |

### Meta-evolution

| Document                                              | Core Mechanism                                                            |
| :---------------------------------------------------- | :------------------------------------------------------------------------ |
| [memevolve](evasion/experiential-memory/memevolve.md) | Co-evolution of experiential knowledge and underlying memory architecture |

---

## Working Memory

### Single-turn — Input Compression

| Document                                         | Core Mechanism                                                 |
| :----------------------------------------------- | :------------------------------------------------------------- |
| [llmlingua](evasion/working-memory/llmlingua.md) | Token perplexity estimation for discarding predictable content |

### Multi-turn — State Maintenance

| Document                                                     | Core Mechanism                                                                  |
| :----------------------------------------------------------- | :------------------------------------------------------------------------------ |
| [mem1](evasion/working-memory/mem1.md)                       | Shared internal state + PPO optimized summarization                             |
| [memagent](evasion/working-memory/memagent.md)               | Fixed-budget cyclical memory + GRPO optimization                                |
| [resum](evasion/working-memory/resum.md)                     | Periodic history distillation into reasoning states                             |
| [hiagent](evasion/working-memory/hiagent.md)                 | Subgoal-centric hierarchical working memory                                     |
| [context-folding](evasion/working-memory/context-folding.md) | Learnable folding strategy, autonomous branching and abstraction                |
| [lightmem](evasion/working-memory/lightmem.md)               | Construction of efficient short-term and long-term memory mechanisms for agents |

---

## Multi-Agent Memory

| Document                                                             | Core Mechanism                                                          |
| :------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| [generative-agents](evasion/multi-agent-memory/generative-agents.md) | Social simulation, recency/importance/relevance three-factor retrieval  |
| [bmam](evasion/multi-agent-memory/bmam.md)                           | Hippocampal-neocortical dual-system multi-agent memory framework        |
| [g-designer](evasion/multi-agent-memory/g-designer.md)               | Adaptive multi-agent communication topology using Graph Neural Networks |
| [masrouter](evasion/multi-agent-memory/masrouter.md)                 | Dynamic proxy conditional search mechanism based on routing resources   |

---

## Frameworks — Open Source Memory Frameworks

| Document                                                       | Core Abstraction                                       |
| :------------------------------------------------------------- | :----------------------------------------------------- |
| [memos-framework](evasion/frameworks/memos-framework.md)       | MemOS — MemScheduler for dynamic memory type selection |
| [memoryos-framework](evasion/frameworks/memoryos-framework.md) | MemoryOS — Hierarchical S/M/LTM architecture           |
| [memobase-framework](evasion/frameworks/memobase-framework.md) | Memobase — Structured profiles                         |
| [langmem-framework](evasion/frameworks/langmem-framework.md)   | LangMem — Core API + manager                           |
| [cognee-framework](evasion/frameworks/cognee-framework.md)     | Cognee — Knowledge graph-based                         |

---

# II. Direct-Facing: Parameter Updates and Latent State Representations

These solutions directly confront catastrophic forgetting. By explicitly modifying weights (internal parameters, adapters), optimizing latent space representation structures, or innovating gradient update mechanisms during the training phase, they attempt to achieve long-term learning objectives at the network parameter level, analogous to neurobiological processes.

## Parametric Memory

### Internal — Direct Model Weight Modification

**Pre-Train / Mid-Train:**

| Document                                                        | Core Mechanism                                                                                     |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [lmlm](direct-facing/parametric-memory/lmlm.md)                 | Stores knowledge retrieval memory within the model, while knowledge remains in an external library |
| [streamingllm](direct-facing/parametric-memory/streamingllm.md) | Attention Sink mechanism for optimizing long-window memory                                         |

**Post-Train — Knowledge Editing:**

| Document                                                                | Core Mechanism                                                                    |
| :---------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| [rome](direct-facing/parametric-memory/rome.md)                         | Causal tracing localization + Rank-One Update injection                           |
| [memit](direct-facing/parametric-memory/memit.md)                       | Batch editing of thousands of facts using multi-layer residual distribution       |
| [mend](direct-facing/parametric-memory/mend.md)                         | Auxiliary network for gradient decomposition to achieve rapid single-step editing |
| [alphaedit](direct-facing/parametric-memory/alphaedit.md)               | Knowledge editing with null-space constraints                                     |
| [knowledge-editor](direct-facing/parametric-memory/knowledge-editor.md) | Targeted internal parameter modification                                          |

**Post-Train — Other:**

| Document                                                        | Core Mechanism                                                              |
| :-------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| [self-param](direct-facing/parametric-memory/self-param.md)     | KL divergence distillation for knowledge injection without extra parameters |
| [character-lm](direct-facing/parametric-memory/character-lm.md) | SFT fine-tuning for injecting character traits/persona                      |

### External — Additional Parameter Modules

**Adapter-based:**

| Document                                                              | Core Mechanism                                                                    |
| :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| [k-adapter](direct-facing/parametric-memory/k-adapter.md)             | Task-specific adapters with a frozen backbone                                     |
| [wise](direct-facing/parametric-memory/wise.md)                       | Dual-parameter memory + dynamic routing selection                                 |
| [elder](direct-facing/parametric-memory/elder.md)                     | Multi-LoRA modules + semantic routing function                                    |
| [t-patcher](direct-facing/parametric-memory/t-patcher.md)             | Identifying and patching "neurons worth patching"                                 |
| [memory-decoder](direct-facing/parametric-memory/memory-decoder.md)   | Plug-and-play, combining external RAG flexibility with parametric inference speed |
| [memlora](direct-facing/parametric-memory/memlora.md)                 | Distillation of expert adapters for memory enhancement                            |
| [meta-smf](direct-facing/parametric-memory/meta-smf.md)               | Sparse memory pool, 1.3B+1B params, reduction of forgetting from 89% to 11%       |
| [engram-deepseek](direct-facing/parametric-memory/engram-deepseek.md) | Conditional memory O(1) lookup module                                             |

**Auxiliary LM-based:**

| Document                                                      | Core Mechanism                                                     |
| :------------------------------------------------------------ | :----------------------------------------------------------------- |
| [mac](direct-facing/parametric-memory/mac.md)                 | Amortization network compressing documents into compact modulation |
| [retroformer](direct-facing/parametric-memory/retroformer.md) | Learning from successes and failures of past task executions       |

---

## Latent Memory

### Generate — Auxiliary Model Generated Embeddings

**Single Modal:**

| Document                                                                                  | Core Mechanism                                                                      |
| :---------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- |
| [gist-tokens](direct-facing/latent-memory/gist-tokens.md)                                 | Long prompt compression into gist tokens                                            |
| [autocompressor](direct-facing/latent-memory/autocompressor.md)                           | Encoding long documents into summary vectors as soft prompts                        |
| [memorag](direct-facing/latent-memory/memorag.md)                                         | LLM-generated global semantic latent states + hypothetical document query rewriting |
| [memoryllm](direct-facing/latent-memory/memoryllm.md)                                     | Self-updating memory tokens embedded within latent space                            |
| [m-plus](direct-facing/latent-memory/m-plus.md)                                           | Long-term memory token pool across layers                                           |
| [lm2](direct-facing/latent-memory/lm2.md)                                                 | Latent memory slots with per-layer matrix shapes                                    |
| [titans](direct-facing/latent-memory/titans.md)                                           | Long-range information compression into online-updated MLP weights                  |
| [memgen](direct-facing/latent-memory/memgen.md)                                           | Dynamic generation of latent memory during decoding (Memory Trigger + Weaver)       |
| [emu](direct-facing/latent-memory/emu.md)                                                 | State encoder embeddings with return annotations                                    |
| [memoria-park](direct-facing/latent-memory/memoria-park.md)                               | Three-layer memory with engrams (biologically inspired)                             |
| [google-nested-learning-hope](direct-facing/latent-memory/google-nested-learning-hope.md) | Nested Optimization                                                                 |

**Multimodal:**

| Document                                      | Core Mechanism                                                |
| :-------------------------------------------- | :------------------------------------------------------------ |
| [comem](direct-facing/latent-memory/comem.md) | Q-Former compressing vision-language into fixed-length tokens |
| [xmem](direct-facing/latent-memory/xmem.md)   | Multi-stage KV embedding memory for video object segmentation |

### Reuse — Direct Reuse of Computation States

| Document                                                                          | Core Mechanism                                           |
| :-------------------------------------------------------------------------------- | :------------------------------------------------------- |
| [memorizing-transformers](direct-facing/latent-memory/memorizing-transformers.md) | Storing past KV pairs, retrieved via KNN search          |
| [fot](direct-facing/latent-memory/fot.md)                                         | Memory-attention layers + KNN retrieval of additional KV |
| [longmem](direct-facing/latent-memory/longmem.md)                                 | Residual SideNet for persistent historical KV embeddings |

### Transform — Compression/Reorganization of Existing States

| Document                                                        | Core Mechanism                                          |
| :-------------------------------------------------------------- | :------------------------------------------------------ |
| [scissorhands](direct-facing/latent-memory/scissorhands.md)     | Pruning KV cache based on attention scores              |
| [snapkv](direct-facing/latent-memory/snapkv.md)                 | Head-wise voting to aggregate high-importance prefix KV |
| [pyramidkv](direct-facing/latent-memory/pyramidkv.md)           | Reallocating KV budget across layers                    |
| [h2o](direct-facing/latent-memory/h2o.md)                       | Heavy-Hitter Oracle eviction strategy                   |
| [razorattention](direct-facing/latent-memory/razorattention.md) | Effective attention span + compensation tokens          |
| [r3mem](direct-facing/latent-memory/r3mem.md)                   | Virtual memory tokens + reversible compression          |

---

## Continual Pre-Training (CPT)

### Domain / Cross-Lingual & Mixture

| Document                                                       | Core Mechanism                                                                 |
| :------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| [finpythia](direct-facing/continual-pre-training/finpythia.md) | Strictly selected corpora for domain-specific (finance) CPT                    |
| [swallow](direct-facing/continual-pre-training/swallow.md)     | Cross-lingual CPT via vocabulary expansion and high-quality Japanese corpora   |
| [doremi](direct-facing/continual-pre-training/doremi.md)       | Proxy model estimating domain weights to optimize massive data mixture         |
| [rho-1](direct-facing/continual-pre-training/rho-1.md)         | Selective Language Modeling (SLM), pre-training token selection based on value |

---

## Continual Instruction Tuning (CIT)

| Document                                                         | Core Mechanism                                                                                     |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [sapt](direct-facing/continual-instruction-tuning/sapt.md)       | Isolated fine-tuning using multi-expert LLMs / Adapters for new tasks                              |
| [toolllm](direct-facing/continual-instruction-tuning/toolllm.md) | Incremental adaptation learning for tool-use capabilities (Tools/APIs)                             |
| [moelora](direct-facing/continual-instruction-tuning/moelora.md) | Interference-free incremental fine-tuning architecture for multimodal tasks combining MoE and LoRA |

---

## Continual Alignment (CA)

| Document                                          | Core Mechanism                                                                     |
| :------------------------------------------------ | :--------------------------------------------------------------------------------- |
| [cppo](direct-facing/continual-alignment/cppo.md) | Preventing RLHF forgetting by combining score probability and retention            |
| [rlvf](direct-facing/continual-alignment/rlvf.md) | Using DPO+SCD to avoid preference over-generalization caused by prompt fine-tuning |
| [ama](direct-facing/continual-alignment/ama.md)   | Adaptive model smoothing/averaging to mitigate Alignment Tax                       |

---

# III. Evaluation and Pending

## Eval — Evaluation Benchmarks

| Document                             | Core Mechanism                                                                      |
| :----------------------------------- | :---------------------------------------------------------------------------------- |
| [evermembench](eval/evermembench.md) | Three-dimensional evaluation: fine-grained recall / memory awareness / user persona |
| [freshqa](eval/freshqa.md)           | Evaluation of temporal knowledge acquisition and retention                          |
| [unseentimeqa](eval/unseentimeqa.md) | Long-span and diversified QA testing for unseen temporal information                |
| [ckl](eval/ckl.md)                   | Invariant, New, and Updated LAMA knowledge testing                                  |

---

## Pending

| Document                                                          | Status                                          |
| :---------------------------------------------------------------- | :---------------------------------------------- |
| [mit-beyond-context-limits](pending/mit-beyond-context-limits.md) | Mentioned only; awaiting original paper reading |

---

_Back to [Root](../docs/zh_CN/CLAUDE.md)_
