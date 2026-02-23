# Research References

This directory serves as the project's "External Knowledge Base," containing all relevant academic papers, technical surveys, evaluation benchmarks, and specific technical solutions.

## Core Principles

1.  **Separation of Raw Data and Secondary Processing**: The `surveys/` directory and various raw paper folders store original materials in a read-only capacity.
2.  **First-Principles Classification**: All technical solutions must be distilled into atomic notes and integrated into the technical classification system within this directory.

## Directory Structure

- **[surveys/](./surveys/)** — Surveys & Foundations
  - Stores panoramic field surveys (PDFs, LaTeX, and corresponding full-text translations/excerpts).
- **[fundamental/](./fundamental/)** — Parameter and Latent State Solutions (Fundamental)
  - Stores models and algorithmic implementations that directly address the forgetting problem.
- **[engineering/](./engineering/)** — Context and Multi-Agent Solutions (Engineering)
  - Stores system solutions that bypass the forgetting problem through external architectures.
- **[eval/](./eval/)** — Evaluation Benchmarks
  - Stores benchmark designs for evaluating model continual learning and memory retention capabilities.

---

# Technical Solutions Index

A categorized index of all compiled technical solutions (Methods) based on first principles and technical essence.

---

## Surveys & Theory

| Document                                                                                                   | Source             | Focus                                                                    |
| :--------------------------------------------------------------------------------------------------------- | :----------------- | :----------------------------------------------------------------------- |
| [Memory in the Age of AI Agents](surveys/Memory%20in%20the%20Age%20of%20AI%20Agents/)                                                                                         | arXiv 2512.13564v2 | Three-dimensional framework for Agent Memory: Forms/Functions/Dynamics    |
| [LLM's memory problem will no longer be a problem "soon"?](surveys/LLM's%20memory%20problem%20will%20no%20longer%20be%20a%20problem%20%22soon%22%3F/)                          | Jiqizhixin Pro W07 | 4W classification system, three-layer AI Memory partition                 |
| [From Human Memory to AI Memory](surveys/From%20Human%20Memory%20to%20AI%20Memory%3A%20A%20Survey%20on%20Memory%20Mechanisms%20in%20the%20Era%20of%20LLMs/)                     | Jiqizhixin Pro W07 | Memory analogy framework from a cognitive science perspective             |
| [AI Meets Brain](surveys/AI%20Meets%20Brain%3A%20Memory%20Systems%20from%20Cognitive%20Neuroscience%20to%20Autonomous%20Agents/)                                                | Jiqizhixin Pro W07 | Unified perspective on human brain and Agent Memory                       |
| [Continual Learning of Large Language Model (Monash Slide)](surveys/Continual%20Learning%20of%20Large%20Language%20Model%20(Monash%20Slide)/)                                   | Tutorial Share     | Vertical/Horizontal CL tutorials and introduction to Continual Alignment |
| [Continual Learning of Large Language Models: A Comprehensive Survey](surveys/Continual%20Learning%20of%20Large%20Language%20Models%3A%20A%20Comprehensive%20Survey/)            | Survey Share       | LLM survey distinguishing between Vertical and Horizontal CL             |

---

# I. Engineering: Engineering Extensions and Workflow Architectures

These solutions attempt to bypass catastrophic forgetting through system-level scheduling, such as long contexts, external databases, and multi-agent workflows, achieving "pseudo-learning" (essentially information retrieval or external storage).

## Token-level Memory

### Flat (1D) — Topology-less

| Document                                                         | Core Mechanism                                                     |
| :--------------------------------------------------------------- | :----------------------------------------------------------------- |
| [memgpt](engineering/token-level-memory/memgpt.md)                   | OS metaphor, Main/External Context virtual memory hierarchy        |
| [mem0](engineering/token-level-memory/mem0.md)                       | Standardized memory CRUD operations, hybrid Graph + Vector storage |
| [think-in-memory](engineering/token-level-memory/think-in-memory.md) | Hash table storage for inductive thoughts, cluster-level fusion    |
| [comedy](engineering/token-level-memory/comedy.md)                   | Single model for memory generation, compression, and reuse         |
| [openclaw](engineering/token-level-memory/openclaw.md)               | Engineering solution for cross-session personalized memory         |

### Planar (2D) — Single-layer Structured

| Document                                         | Core Mechanism                                                       |
| :----------------------------------------------- | :------------------------------------------------------------------- |
| [hat](engineering/token-level-memory/hat.md)         | Hierarchical Aggregation Tree, coarse-to-fine retrieval              |
| [memtree](engineering/token-level-memory/memtree.md) | Dynamic hierarchical schema, bottom-up summary updates               |
| [a-mem](engineering/token-level-memory/a-mem.md)     | Card-based memory units, semantic links constructing memory networks |
| [d-smart](engineering/token-level-memory/d-smart.md) | KG + Reasoning Tree hybrid, neuro-symbolic pipeline                  |

### Hierarchical (3D) — Multi-layer Interconnected

| Document                                                                       | Core Mechanism                                                                          |
| :----------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| [graphrag](engineering/token-level-memory/graphrag.md)                             | Recursive aggregation via community detection, multi-layer graph indexing               |
| [hipporag](engineering/token-level-memory/hipporag.md)                             | Neurobiologically inspired, dual-layer graph + PageRank retrieval                       |
| [arigraph](engineering/token-level-memory/arigraph.md)                             | Unified semantic KG + episodic component within a graph                                 |
| [zep](engineering/token-level-memory/zep.md)                                       | Three-layer temporal KG (Episodic/Semantic/Community)                                   |
| [g-memory](engineering/token-level-memory/g-memory.md)                             | Three-layer graph (interaction/query/insight), shared across multi-agents               |
| [lyfe-agents](engineering/token-level-memory/lyfe-agents.md)                       | Working/Short-term/Long-term three-layer social simulation                              |
| [inside-out-personatree](engineering/token-level-memory/inside-out-personatree.md) | Hierarchical persona memory schema and operational updates                              |
| [hipporag-2](engineering/token-level-memory/hipporag-2.md)                         | Evolution from RAG to hippocampus-like multi-hop retrieval and long-term memory systems |

---

## Experiential Memory

### Case-based — Raw Trajectories/Solutions

| Document                                          | Core Mechanism                                            |
| :------------------------------------------------ | :-------------------------------------------------------- |
| [expel](engineering/experiential-memory/expel.md)     | Trial-and-error accumulation, hybrid trajectory + insight |
| [synapse](engineering/experiential-memory/synapse.md) | Abstracted state-action episodes as in-context examples   |

### Strategy-based — Insights/Workflows/Patterns

| Document                                                                | Core Mechanism                                                |
| :---------------------------------------------------------------------- | :------------------------------------------------------------ |
| [reflexion](engineering/experiential-memory/reflexion.md)                   | Short-term trajectory + long-term self-reflection feedback    |
| [buffer-of-thoughts](engineering/experiential-memory/buffer-of-thoughts.md) | Meta-buffer thought template retrieval and instantiation      |
| [awm](engineering/experiential-memory/awm.md)                               | Extraction of reusable workflows from successful trajectories |

### Skill-based — Executable Code/Functions/APIs

| Document                                                                    | Core Mechanism                                                  |
| :-------------------------------------------------------------------------- | :-------------------------------------------------------------- |
| [voyager](engineering/experiential-memory/voyager.md)                           | Continuously growing executable skill code library in Minecraft |
| [darwin-godel-machine](engineering/experiential-memory/darwin-godel-machine.md) | Secure self-rewriting code, recursive self-modification         |

### Meta-evolution

| Document                                              | Core Mechanism                                                            |
| :---------------------------------------------------- | :------------------------------------------------------------------------ |
| [memevolve](engineering/experiential-memory/memevolve.md) | Co-evolution of experiential knowledge and underlying memory architecture |

---

## Working Memory

### Single-turn — Input Compression

| Document                                         | Core Mechanism                                                 |
| :----------------------------------------------- | :------------------------------------------------------------- |
| [llmlingua](engineering/working-memory/llmlingua.md) | Token perplexity estimation for discarding predictable content |

### Multi-turn — State Maintenance

| Document                                                     | Core Mechanism                                                                  |
| :----------------------------------------------------------- | :------------------------------------------------------------------------------ |
| [mem1](engineering/working-memory/mem1.md)                       | Shared internal state + PPO optimized summarization                             |
| [memagent](engineering/working-memory/memagent.md)               | Fixed-budget cyclical memory + GRPO optimization                                |
| [resum](engineering/working-memory/resum.md)                     | Periodic history distillation into reasoning states                             |
| [hiagent](engineering/working-memory/hiagent.md)                 | Subgoal-centric hierarchical working memory                                     |
| [context-folding](engineering/working-memory/context-folding.md) | Learnable folding strategy, autonomous branching and abstraction                |
| [lightmem](engineering/working-memory/lightmem.md)               | Construction of efficient short-term and long-term memory mechanisms for agents |

---

## Multi-Agent Memory

| Document                                                             | Core Mechanism                                                          |
| :------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| [generative-agents](engineering/multi-agent-memory/generative-agents.md) | Social simulation, recency/importance/relevance three-factor retrieval  |
| [bmam](engineering/multi-agent-memory/bmam.md)                           | Hippocampal-neocortical dual-system multi-agent memory framework        |
| [g-designer](engineering/multi-agent-memory/g-designer.md)               | Adaptive multi-agent communication topology using Graph Neural Networks |
| [masrouter](engineering/multi-agent-memory/masrouter.md)                 | Dynamic proxy conditional search mechanism based on routing resources   |

---

## Frameworks — Open Source Memory Frameworks

| Document                                                       | Core Abstraction                                       |
| :------------------------------------------------------------- | :----------------------------------------------------- |
| [memos-framework](engineering/frameworks/memos-framework.md)       | MemOS — MemScheduler for dynamic memory type selection |
| [memoryos-framework](engineering/frameworks/memoryos-framework.md) | MemoryOS — Hierarchical S/M/LTM architecture           |
| [memobase-framework](engineering/frameworks/memobase-framework.md) | Memobase — Structured profiles                         |
| [langmem-framework](engineering/frameworks/langmem-framework.md)   | LangMem — Core API + manager                           |
| [cognee-framework](engineering/frameworks/cognee-framework.md)     | Cognee — Knowledge graph-based                         |

---

# II. Fundamental: Parameter Updates and Latent State Representations

These solutions directly confront catastrophic forgetting. By explicitly modifying weights (internal parameters, adapters), optimizing latent space representation structures, or innovating gradient update mechanisms during the training phase, they attempt to achieve long-term learning objectives at the network parameter level, analogous to neurobiological processes.

## Parametric Memory

### Internal — Direct Model Weight Modification

**Pre-Train / Mid-Train:**

| Document                                                        | Core Mechanism                                                                                     |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [lmlm](fundamental/parametric-memory/lmlm.md)                 | Stores knowledge retrieval memory within the model, while knowledge remains in an external library |
| [streamingllm](fundamental/parametric-memory/streamingllm.md) | Attention Sink mechanism for optimizing long-window memory                                         |

**Post-Train — Knowledge Editing:**

| Document                                                                | Core Mechanism                                                                    |
| :---------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| [rome](fundamental/parametric-memory/rome.md)                         | Causal tracing localization + Rank-One Update injection                           |
| [memit](fundamental/parametric-memory/memit.md)                       | Batch editing of thousands of facts using multi-layer residual distribution       |
| [mend](fundamental/parametric-memory/mend.md)                         | Auxiliary network for gradient decomposition to achieve rapid single-step editing |
| [alphaedit](fundamental/parametric-memory/alphaedit.md)               | Knowledge editing with null-space constraints                                     |
| [knowledge-editor](fundamental/parametric-memory/knowledge-editor.md) | Targeted internal parameter modification                                          |

**Post-Train — Other:**

| Document                                                        | Core Mechanism                                                              |
| :-------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| [self-param](fundamental/parametric-memory/self-param.md)     | KL divergence distillation for knowledge injection without extra parameters |
| [character-lm](fundamental/parametric-memory/character-lm.md) | SFT fine-tuning for injecting character traits/persona                      |

### External — Additional Parameter Modules

**Adapter-based:**

| Document                                                              | Core Mechanism                                                                    |
| :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| [k-adapter](fundamental/parametric-memory/k-adapter.md)             | Task-specific adapters with a frozen backbone                                     |
| [wise](fundamental/parametric-memory/wise.md)                       | Dual-parameter memory + dynamic routing selection                                 |
| [elder](fundamental/parametric-memory/elder.md)                     | Multi-LoRA modules + semantic routing function                                    |
| [t-patcher](fundamental/parametric-memory/t-patcher.md)             | Identifying and patching "neurons worth patching"                                 |
| [memory-decoder](fundamental/parametric-memory/memory-decoder.md)   | Plug-and-play, combining external RAG flexibility with parametric inference speed |
| [memlora](fundamental/parametric-memory/memlora.md)                 | Distillation of expert adapters for memory enhancement                            |
| [meta-smf](fundamental/parametric-memory/meta-smf.md)               | Sparse memory pool, 1.3B+1B params, reduction of forgetting from 89% to 11%       |
| [engram-deepseek](fundamental/parametric-memory/engram-deepseek.md) | Conditional memory O(1) lookup module                                             |

**Auxiliary LM-based:**

| Document                                                      | Core Mechanism                                                     |
| :------------------------------------------------------------ | :----------------------------------------------------------------- |
| [mac](fundamental/parametric-memory/mac.md)                 | Amortization network compressing documents into compact modulation |
| [retroformer](fundamental/parametric-memory/retroformer.md) | Learning from successes and failures of past task executions       |

---

## Latent Memory

### Generate — Auxiliary Model Generated Embeddings

**Single Modal:**

| Document                                                                                  | Core Mechanism                                                                      |
| :---------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- |
| [gist-tokens](fundamental/latent-memory/gist-tokens.md)                                 | Long prompt compression into gist tokens                                            |
| [autocompressor](fundamental/latent-memory/autocompressor.md)                           | Encoding long documents into summary vectors as soft prompts                        |
| [memorag](fundamental/latent-memory/memorag.md)                                         | LLM-generated global semantic latent states + hypothetical document query rewriting |
| [memoryllm](fundamental/latent-memory/memoryllm.md)                                     | Self-updating memory tokens embedded within latent space                            |
| [m-plus](fundamental/latent-memory/m-plus.md)                                           | Long-term memory token pool across layers                                           |
| [lm2](fundamental/latent-memory/lm2.md)                                                 | Latent memory slots with per-layer matrix shapes                                    |
| [titans](fundamental/latent-memory/titans.md)                                           | Long-range information compression into online-updated MLP weights                  |
| [memgen](fundamental/latent-memory/memgen.md)                                           | Dynamic generation of latent memory during decoding (Memory Trigger + Weaver)       |
| [emu](fundamental/latent-memory/emu.md)                                                 | State encoder embeddings with return annotations                                    |
| [memoria-park](fundamental/latent-memory/memoria-park.md)                               | Three-layer memory with engrams (biologically inspired)                             |
| [google-nested-learning-hope](fundamental/latent-memory/google-nested-learning-hope.md) | Nested Optimization                                                                 |

**Multimodal:**

| Document                                      | Core Mechanism                                                |
| :-------------------------------------------- | :------------------------------------------------------------ |
| [comem](fundamental/latent-memory/comem.md) | Q-Former compressing vision-language into fixed-length tokens |
| [xmem](fundamental/latent-memory/xmem.md)   | Multi-stage KV embedding memory for video object segmentation |

### Reuse — Direct Reuse of Computation States

| Document                                                                          | Core Mechanism                                           |
| :-------------------------------------------------------------------------------- | :------------------------------------------------------- |
| [memorizing-transformers](fundamental/latent-memory/memorizing-transformers.md) | Storing past KV pairs, retrieved via KNN search          |
| [fot](fundamental/latent-memory/fot.md)                                         | Memory-attention layers + KNN retrieval of additional KV |
| [longmem](fundamental/latent-memory/longmem.md)                                 | Residual SideNet for persistent historical KV embeddings |

### Transform — Compression/Reorganization of Existing States

| Document                                                        | Core Mechanism                                          |
| :-------------------------------------------------------------- | :------------------------------------------------------ |
| [scissorhands](fundamental/latent-memory/scissorhands.md)     | Pruning KV cache based on attention scores              |
| [snapkv](fundamental/latent-memory/snapkv.md)                 | Head-wise voting to aggregate high-importance prefix KV |
| [pyramidkv](fundamental/latent-memory/pyramidkv.md)           | Reallocating KV budget across layers                    |
| [h2o](fundamental/latent-memory/h2o.md)                       | Heavy-Hitter Oracle eviction strategy                   |
| [razorattention](fundamental/latent-memory/razorattention.md) | Effective attention span + compensation tokens          |
| [r3mem](fundamental/latent-memory/r3mem.md)                   | Virtual memory tokens + reversible compression          |

---

## Continual Pre-Training (CPT)

### Domain / Cross-Lingual & Mixture

| Document                                                       | Core Mechanism                                                                 |
| :------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| [finpythia](fundamental/continual-pre-training/finpythia.md) | Strictly selected corpora for domain-specific (finance) CPT                    |
| [swallow](fundamental/continual-pre-training/swallow.md)     | Cross-lingual CPT via vocabulary expansion and high-quality Japanese corpora   |
| [doremi](fundamental/continual-pre-training/doremi.md)       | Proxy model estimating domain weights to optimize massive data mixture         |
| [rho-1](fundamental/continual-pre-training/rho-1.md)         | Selective Language Modeling (SLM), pre-training token selection based on value |

---

## Continual Instruction Tuning (CIT)

| Document                                                         | Core Mechanism                                                                                     |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [sapt](fundamental/continual-instruction-tuning/sapt.md)       | Isolated fine-tuning using multi-expert LLMs / Adapters for new tasks                              |
| [toolllm](fundamental/continual-instruction-tuning/toolllm.md) | Incremental adaptation learning for tool-use capabilities (Tools/APIs)                             |
| [moelora](fundamental/continual-instruction-tuning/moelora.md) | Interference-free incremental fine-tuning architecture for multimodal tasks combining MoE and LoRA |

---

## Continual Alignment (CA)

| Document                                          | Core Mechanism                                                                     |
| :------------------------------------------------ | :--------------------------------------------------------------------------------- |
| [cppo](fundamental/continual-alignment/cppo.md) | Preventing RLHF forgetting by combining score probability and retention            |
| [rlvf](fundamental/continual-alignment/rlvf.md) | Using DPO+SCD to avoid preference over-generalization caused by prompt fine-tuning |
| [ama](fundamental/continual-alignment/ama.md)   | Adaptive model smoothing/averaging to mitigate Alignment Tax                       |

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

_Back to [Root](../README.md)_
