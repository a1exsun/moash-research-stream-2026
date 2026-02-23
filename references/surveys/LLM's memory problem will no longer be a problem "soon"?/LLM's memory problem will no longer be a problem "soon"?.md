# Week 07 · Will the LLM Memory Problem "Soon" No Longer Be a Problem?

2026.02.15

### ① Will the LLM Memory Problem "Soon" No Longer Be a Problem?

**Introduction:** Currently, intelligent agents are undergoing a paradigm shift from efficient single-task execution to a mode of continuous self-adaptation, capability evolution, and experience accumulation in dynamic environments. In this context, AI Memory serves as a core cornerstone, enabling agents to maintain behavioral consistency, make rational decisions, and achieve efficient collaboration. Through long-term exploration, AI Memory has branched into two distinct evolutionary paths: "Agent Memory" and "LLM Memory."

**Why OpenClaw's "Long-term Memory" Does Not Represent "AI Possessing Persistent Memory"**

1. The open-source project OpenClaw (formerly known as Clawdbot and Moltbot) became virally popular in early 2026. In related discussions, the core competitiveness of OpenClaw is regarded as being a "Claude with hands," capable of maintaining persistent memory across weeks or even months of sessions. By learning user preferences, tone, and specific workflows, it transforms the AI from a "dialogue window" into a truly "knowledgeable" digital employee.
   ① Since its release at the end of 2025, the OpenClaw project has surged in popularity on GitHub, exceeding 190,000 stars by February 2026. [1-1]

2. Against this backdrop, the core of the AI community's discussion on the OpenClaw project is not only its ability to perform complex cross-platform operations but also whether its demonstrated "long-term memory" capability signifies the imminent arrival of a future where "AI possesses persistent memory."
   ① With breakthroughs and the widespread adoption of LLMs and Agent applications, the AI Memory problem is regarded as the core bottleneck hindering the evolution of higher-order intelligence. Research aimed at improving AI memory has become one of the most watched frontier directions in LLM-related studies.
   ② In 2025, numerous explorations aimed at improving AI Memory emerged, such as the "SMF" work by the Meta team, the "Nested Learning" paradigm and the HOPE model proposed by Google, and the "BEYOND CONTEXT LIMITS" work by MIT (for details, see Pro Membership Newsletter 2025 Week 46 & Week 50).
   ③ Academic interest in AI Memory is also continuously rising. Using top-tier conference research themes as an example, ICLR 2026 specially established the "MemAgents" workshop, aiming to build an underlying memory substrate for agents that supports few-shot learning and long-range consistency. [1-11]

3. Accompanied by the continuous exploration of memory architectures and mechanisms in academia, and the "huge success" of OpenClaw in engineering, the long-discussed AI memory problem has begun to form boundaries and differentiate into two evolutionary paths: "LLM Memory" and "Agent Memory." [1-4]
   ① LLM Memory constitutes the underlying computational mechanism for prediction, existing in two specific forms: parametric memory embedded in pre-trained model weights, and runtime memory managed through the context window. LLM Memory is the foundational computational carrier; its priority lies in ensuring the accuracy of immediate generation within a limited window, rather than maintaining coherent autonomous behavior.
   ② Agent Memory extends upon the former into a functional process that systematically supports autonomous behavior. It no longer merely generates isolated text but coordinates the cyclic process of perception, planning, and action, enabling the system to decompose and execute complex tasks.

4. In the field of Agents, or in the context of relatively vertical "Vertical Agents," memory (Agent Memory) is no longer a scientific mystery but an engineering problem that can be solved through scenario decomposition and targeted construction. [1-2] [1-3]
   ① By organizing data into different formats—such as procedural, declarative, and metacognitive—Agent Memory allows the system to learn from historical experience. This layer facilitates the transformation of data from static records to dynamic "experience" by implementing reflection and strategy optimization, enabling the Agent to evolve its behavior based on past outcomes. [1-4]

5. Relative to the prosperity of Agent Memory, LLM Memory still faces numerous challenges, such as the "Stability-Plasticity Dilemma." When attempting to inject new information into parameters through fine-tuning, models often lose old, equally important knowledge. [1-4]

**How is the Research Perspective on AI Memory Changing?**

1. The core value of AI Memory is not limited to mitigating technical bottlenecks such as the finite context window of large language models and interaction statelessness; it is increasingly viewed as a transformative empowering tool. It drives the upgrade of artificial intelligence systems from general-purpose tools to human-centric agents with adaptive and collaborative capabilities. [1-4]

2. With the continuous exploration of AI Memory, researchers have begun to examine this cornerstone of AI capability from diverse perspectives, profoundly exploring and iterating on its theoretical basis, operational mechanisms, and boundaries.
   ① In April 2025, "From Human Memory to AI Memory" by Huawei Noah's Ark Lab provided an analogical framework for understanding the memory mechanisms of LLM Agents, starting from memory theories in human cognitive science. [1-5]
   ② In December 2025, "AI Meets Brain" by institutions such as Harbin Institute of Technology, Peng Cheng Laboratory, and Fudan University uniformly examined human brain memory mechanisms alongside Agent Memory and conducted an analysis of its storage structures. [1-6]

3. In early 2026, the MemoryOS team from Beijing University of Posts and Telecommunications (BUPT) together with Huawei researchers published a new survey titled "Survey on AI Memory," integrating cognitive psychology and neuroscience models to clarify the conceptual boundaries of "Memory" in the field of AI.
   ① The survey divides the conceptual boundaries of "Memory" into three levels. LLM Memory primarily emphasizes the computational core and provides the prediction engine; Agent Memory focuses on functional processes and is responsible for managing task-oriented execution processes.
   ② Above LLMs and Agents, "AI Memory" is the most macroscopic cognitive concept. It encompasses the biological inspiration of artificial cognition and the ultimate goal of lifelong learning, focusing on lifelong evolution and experience accumulation, and governing the first two.

4. After clarifying the hierarchical boundaries of AI Memory, researchers further proposed the 4W memory classification system, categorizing AI memory systems along four orthogonal core dimensions: When (Lifecycle), What (Type), How (Storage), and Which (Modality). Each dimension corresponds to a fundamental characteristic of AI memory. Combining theories from fields like cognitive science and computer engineering, detailed definitions and explanations for sub-types under each dimension were provided.
   ① When (Lifecycle Dimension): Focuses on the existence time and survival duration of memory, from instantaneous to persistent storage across sessions, corresponding to the time-span characteristics of memory within AI agent systems.
   ② What (Type Dimension): Based on cognitive science theory, memory is classified by the type of information captured or the nature of the knowledge, reflecting the functional role of memory in agent behavior.
   ③ How (Storage Dimension): Explores the representation forms and technical storage implementations of memory, distinguishing between implicit storage within the model and explicit external storage.
   ④ Which (Modality Dimension): Categorizes by the information format or modality processed by the memory, divided into unimodal and multimodal, reflecting the AI memory's ability to process different types of information.

5. Furthermore, researchers from BUPT and Huawei sorted out single-agent and multi-agent memory architectures as well as memory evaluation methods. They decomposed three core bottlenecks currently existing in the development of AI memory: architectural conflicts, gaps in theoretical methodology, and complexity in security and operations.
   ① "Architectural Conflicts and System Limitations" covers the contradiction between the limited context window of LLMs and the massive accumulation of long-term experience; the high computational cost of parametric memory updates and the issue of catastrophic forgetting; and the challenges of heterogeneous information fusion and unified representation in multimodal memory.
   ② "Theoretical and Methodological Gaps" emphasizes that current memory research is biased toward the temporal dimension, neglecting the object and storage form dimensions, leading to conceptual fragmentation. The evaluation system lacks high-order capability indicators (e.g., generalization and robustness); multi-agent memory sharing lacks a mature theory for information partitioning, synchronization, and consistency.
   ③ "Security Risks and Operational Complexity" involves different scenarios. In single-agent scenarios, user data storage must balance personalization and privacy protection, with inherent risks of sensitive information inference. In multi-agent collaboration scenarios, static permission designs cannot adapt to complex environments, easily triggering efficiency bottlenecks and data inconsistency.

**Table: The 4W Classification and Technical System of AI Memory. [1-4]**

**How are Recent Works Exploring LLM Memory and Agent Memory?**

1. Accompanied by the industry's emphasis on AI Memory and the goal of driving LLM evolution toward continuous learning and autonomous intelligence, explorations of LLM Memory in early 2026 focused on model-native context and knowledge storage mechanisms. Related work on Agent Memory addressed multi-turn interaction, long-term personalization, and memory management in multi-agent collaboration.

2. Researchers from DeepSeek and Peking University released the "Engram" work at the beginning of the year, proposing a sparsity dimension of "conditional memory" to supplement the conditional computation paradigm of existing MoE models. This aims to solve the problem where the Transformer architecture lacks native knowledge lookup primitives and must simulate retrieval through inefficient computation. [1-7]
   ① This work designed the "Engram" scalable lookup module, borrowing embedding ideas from classic N-grams to achieve knowledge lookup with O(1) time complexity. This allows the model to quickly invoke static knowledge based on local input patterns, without the need for repeated deep computation to reconstruct high-frequency, templated information.
   ② Testing showed that under equivalent parameter and FLOPs conditions, a 27B-scale Engram model significantly outperformed MoE models in knowledge-based tasks (MMLU +3.4, CMMLU +4.0), general reasoning (BBH +5.0, ARC-Challenge +3.7), and code/math domains (HumanEval +3.0, MATH +2.4). In long-context tasks, Multi-Query NIAH accuracy improved from 84.2% to 97.0%.
   ③ Mechanism analysis indicated that Engram liberates shallow networks from static reconstruction tasks, allowing deep layers to focus on complex reasoning, equivalently increasing the model's effective depth. Meanwhile, its deterministic retrieval features support the decoupling of storage and computation; memory tables can be deployed on CPU/SSD, significantly reducing reliance on GPU VRAM.

3. Addressing the capability assessment of LLM Memory, Tianqiao Chen's team at Shanda Group recently proposed the "EverMemBench" benchmark. This is designed to evaluate the long-term interactive memory capabilities of LLMs, solving the problem where existing benchmarks mostly focus on binary, single-topic dialogues and struggle to capture real-world complexity. [1-8]
   ① EverMemBench decomposes memory capability into three core evaluation dimensions: fine-grained recall, memory awareness, and user persona understanding. Fine-grained recall emphasizes the precise extraction of specific facts; memory awareness tests whether the model can identify the relevance of historical information to new scenarios and apply it appropriately; user persona understanding focuses on the model's ability to mine implied user habits and traits from long-term dialogues.
   ② Researchers evaluated the performance of various long-context language models (including Gemini-3-Flash, GPT-4.1-mini, LLaMA-4-Scout, etc.) and memory-augmented systems (such as Zep, Mem0, EverMemOS, etc.) based on EverMemBench, pointing out current memory defects in LLMs.
   ③ Experimental results showed that multi-hop reasoning performance drops sharply in multi-party scenarios, with the best-performing Gemini-3-Flash achieving an accuracy of only 26.51%. The core reason is that relevant information in multi-party scenarios is scattered across different speakers, groups, and time points. Temporal reasoning remains an unsolved challenge; existing models struggle to handle version semantics and evolution logic of information, with the best model achieving less than 50% accuracy.
   ④ Furthermore, the study found that memory awareness is limited by retrieval quality. Existing similarity-based retrieval methods cannot bridge the semantic gap between queries and implicitly relevant memories, resulting in memory-augmented systems performing significantly worse than full-context models.

4. Regarding Agent Memory, researchers from the Guangdong Institute of Intelligence Science and Technology, Tokyo Institute of Technology, and Hong Kong Polytechnic University recently designed a multi-agent memory framework, "BMAM," by referencing brain cognitive mechanisms. By simulating the hippocampus-neocortex dual memory system and combining task coordination logic from the prefrontal cortex, it addresses memory management, temporal consistency, and long-range reasoning in multi-agent collaboration. [1-9]
   ① The BMAM framework adopts a modular design, including a hippocampus-inspired episodic memory module, a neocortex-inspired semantic memory module, and a coordination module responsible for memory integration and retrieval. This enables hierarchical management, parallel updating, and precise retrieval of working memory and long-term memory.
   ② This work proposed a diagnostic perspective of "soul erosion," defined as the comprehensive degradation of three dimensions: temporal coherence, semantic consistency, and identity preservation. It links Agent memory failure modes with architectural design.
   ③ BMAM designed dedicated solutions for each mode of "soul erosion," such as solving temporal erosion through StoryArc timeline indexing, stabilizing facts through the integration mechanism from the hippocampus to the temporal lobe to combat semantic erosion, and using amygdala-inspired saliency markers to protect identity-related information from being overwritten by temporary context.
   ④ Testing showed that BMAM achieved 78.45% accuracy on the LoCoMo benchmark and 52.6% accuracy in cross-session task integration, outperforming existing multi-agent memory systems. Ablation studies confirmed that hippocampal episodic memory is the core performance driver; removing it resulted in a 24.62% drop in accuracy, while other subsystems provided supplementary support for specific failure modes.

5. Researchers from the School of Information at Renmin University of China, MemTensor, and the Shanghai Institute for Advanced Algorithms, in a recent work, explored issues such as memory noise accumulation, personality inconsistency, and the conflict between infinite dialogue and finite context in long-term personalized dialogue systems. They proposed the "Inside Out" framework, which uses an explicitly structured PersonaTree as the core of long-term memory to maintain user personalization states under unbounded interaction. [1-10]
   ① The "Inside Out" framework borrows the functional division of memory from cognitive science, decomposing memory into four functional sub-systems: episodic memory, semantic memory, saliency perception, and control orientation, rather than a single unstructured storage. These sub-systems collaborate across different time scales.
   ② The work constructs a hierarchical memory schema based on the biopsychosocial model and designs an iterative tree update mechanism. Simultaneously, a lightweight MemListener model is trained using reinforcement learning with proximal rewards to transform unstructured dialogue streams into executable tree operations (ADD, UPDATE, DELETE), achieving dynamic evolution and precise maintenance of memory.
   ③ During the inference phase, an adaptive generation pipeline is employed. A "fast mode" directly uses the PersonaTree to ensure low-latency responses, while a "proxy mode" introduces details on demand under the constraints of the tree structure, balancing efficiency and personalization depth.
   ④ Experimental verification showed that PersonaTree comprehensively out-performed full-text connection and existing personalized memory systems in suppressing context noise and maintaining personality consistency. Moreover, the small MemListener model achieved memory operation performance comparable to large models, pioneering an efficient collaboration paradigm where "small models maintain memory, and large models handle generation," providing a structured and interpretable memory solution for long-term personalized dialogue Agents.

## Reference Links

[1-1] https://github.com/openclaw/openclaw

[1-2] https://www.usaii.org/ai-insights/vertical-ai-agents-explained-mechanisms-use-cases-and-adoption

[1-3] https://www.aalpha.net/blog/vertical-vs-horizontal-ai-agents/

[1-4] https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf

[1-5] https://arxiv.org/pdf/2504.15965

[1-6] https://arxiv.org/abs/2512.23343

[1-7] https://arxiv.org/pdf/2601.07372

[1-8] https://arxiv.org/pdf/2602.01313

[1-9] https://arxiv.org/pdf/2601.20465

[1-10] https://arxiv.org/pdf/2601.05171

[1-11] https://iclr.cc/virtual/2026/workshop/10000792
