![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-0-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-0-1.png)
## **Continual Learning of Large** **Language Model**

Tongtong Wu, Linhao Luo, Trang Vu, Reza Haffari



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-0-2.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-0-3.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-0-4.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-0-5.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-0-6.png)
## Schedule and Tutorial Scope

Part I  - Preliminary and Categorisation  (20 minutes) - Reza Haffari
Part II - Continual Pre-Training        (30 minutes) - Tongtong Wu
Part III - Continual Instruction Tuning    (30 minutes) - Linhao Luo


- Break —


Part IV - Continual Alignment          (30 minutes) - Trang Vu
Part V - Continual LLM-based Agents   (30 minutes) - Tongtong Wu
Part VI - Challenges and Future Directions (20 minutes) - Tongtong Wu



2



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-1-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-2-0.png)
## **PART** **I** **_Preliminary_**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-2-2.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-2-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-3-1.png)
## Continual Learning

##### What is Continual Learning

Continual (lifelong) learning is the constant development of increasingly complex
behaviours; the process of building more complicated skills on top of those already
developed.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-3-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-4-2.png)
## Motivating Applications

##### Where Do We Need Continual Learning?

We live in a dynamic and ever changing world:

 - Time Drift: facts change (news, science, policies).

 - Domain Drift: enterprise or specialised sectors evolve.

 - Language Drift: new slang and multilingual corpora appear.

 - etc



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-4-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-4-1.png)
## Motivating Applications

##### From Data Drift to Learning-Strategy Drift


- Data drift demands adaptive training strategies.

- Over-updating causes forgetting; under-updating causes staleness.

- Continual learning finds the balance between the two.



⚠️
Catastrophic

Forgetting



6



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-5-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-5-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-6-2.png)
## Formalisation and Evaluation

##### Problem Settings as Incremental Learning:

Task-IL, Domain-IL, and Class-IL


_arXiv:1909.08383_ 2.6 (2019): 2.



7



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-6-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-6-1.png)
## Formalisation and Evaluation

##### Basic Assumption of Continual Learning

Data Constraints:

- Limited or no access to previously seen data (e.g., due to privacy, storage, or
computational costs).


Optimisation Constraints:

- Training and inference should minimise computational overhead, such as time and
energy consumption.


Parameter Constraints:

- The model should function effectively with fixed or tightly constrained memory, and
parameters should grow sub-linearly (or remain constant) as tasks accumulate,
avoiding the need for exponential increases in model size.



8



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-7-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-8-4.png)
### Continual Learning (CL): Domain-IL

##### ● Domain incremental learning


  - All tasks in the task sequence differ in the input distribution but


share the same label set


  - Examples: a sequence of sentiment analysis tasks on product


review: book -> computer -> …


  - Shared label classes: {positive, negative}



9



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-8-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-8-1.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-8-2.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-8-3.png)
### Continual Learning (CL): Class-IL

##### ● Class incremental learning


  - New classes are added to the incoming task
##### ● Model suffers from catastrophic forgetting


  - A phenomenon of sudden performance drop in previously


learned tasks during learning the current task



10



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-9-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-9-1.png)
### Continual Learning (CL): Task-IL

##### ● Task incremental learning


  - A relaxation of class-incremental learning


  - Each task is assigned with a unique id which is then added to its


data samples so that the task-specific parameters can be


activated accordingly



11



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-10-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-10-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-11-3.png)
## Formalisation and Evaluation

##### Metrics for Continual Learning


- Classical: Average Accuracy, Forgetting, Forward Transfer, Backward Transfer.

- Generative: Exact Match / Rouge / Human Eval.


Average
Performance


Backward
Transfer


Forward Transfer



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-11-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-11-1.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-11-2.png)
## Foundational Methods

##### Buffer Memory-Based vs. Regularisation-Based Methods


- Replay reuses or generates past samples, robust but requires a buffer or generator.

- Regularisation constraints weights to retain old skills, lightweight but fragile under

large shifts.


Bohao, P. E. N. G., et al. "Scalable Language Model with Generalized Continual Learning." _The Twelfth International_
_Conference on Learning Representations_ . 2024.



13



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-12-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-12-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-13-2.png)
## Foundational Methods

##### Parameter-Efficient CL


- Adapters: small modules for each task, easy to roll back or combine.

- LoRA: trains low-rank updates while keeping the base model frozen.

- Enables efficient continual tuning across multiple domains.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-13-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-13-1.png)
## Foundational Methods

##### From Benchmarks to LLM-Scale Reality


- Early CL focused on MNIST/Split CIFAR; now it’s trillion-token corpora.

- New challenges: compute, contamination, governance.

- This motivates LLM-specific continual paradigms covered next.


De Lange, Matthias, et al. "Continual learning: A comparative study on how to defy forgetting in classification tasks." _arXiv_
_preprint arXiv:1909.08383_ 2.6 (2019): 2.



15



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-14-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-14-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-15-1.png)
## Continual Learning of LLM

##### From Static Models to the Three-Staged Paradigm

CPT: continual pretraining for new domains/languages/facts.
CIT: continual instruction/skill fine-tuning as tasks arrive sequentially.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-15-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-16-1.png)
## Continual Learning of LLM

##### From Static Models to the Three-Stage Paradigm

CPT: continual pre-training for new domains/languages/facts.
CIT: continual instruction/skill fine-tuning as tasks arrive sequentially.
CA: rolling updates to policy, preference, and safety.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-16-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-17-0.png)
## **PART** **II** **_Continual Pre-Training_**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-17-2.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-17-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-7.png)
## Why Continual Pretraining (CPT)

##### What is Continual Pretraining?

massive text corpora to understand language structure, patterns, and context.

- CPT refers to further pretraining of LLMs on new data distributions.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-6.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-1.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-2.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-3.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-4.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-18-5.png)









Gururangan, Suchin, et al. "Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks." _Proceedings of the_
_58th Annual Meeting of the Association for Computational Linguistics_ . 2020.



19


## Why Continual Pretraining (CPT)

##### What is Continual Pretraining?



Incremental Pre-training


Sequential Tasks / Domains



Adaptive Pre-training


Specific Domain



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-19-0.png)

Gururangan, Suchin, et al. "Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks." _Proceedings of the_
_58th Annual Meeting of the Association for Computational Linguistics_ . 2020.



20



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-19-1.png)
## Why Continual Pretraining (CPT)

##### When CPT vs. RAG vs. Editing

Retrieval-augmented Generation:

- Lightweight, instant updates via context windows, but lacks persistence.


Model Editing:

- Local, fast updates, useful for single facts.


Continual Pretraining:

- Best suited for systematic knowledge or style changes across distributions.


Wu, Tongtong, et al. "Continual learning for large language models: A survey." _arXiv preprint arXiv:2402.01364_ (2024).



21



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-20-0.png)
## Why Continual Pretraining (CPT)

##### Case Studies: FinPythia

FinPythia:
careful data selection and scheduling boost in-domain results while preserving
general skills.


Xie, Yong, Karan Aggarwal, and Aitzaz Ahmad. "Efficient continual pre-training for building domain specific large language
models." _Findings of the Association for Computational Linguistics ACL 2024_ . 2024.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-21-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-21-0.png)
## Why Continual Pretraining (CPT)

##### Case Studies: Swallow

Swallow:
extend vocabulary, feed high-quality native text, and gain steadily with more tokens.


Fujii, Kazuki, et al. "Continual Pre-Training for Cross-Lingual LLM Adaptation: Enhancing Japanese Language
Capabilities." _First Conference on Language Modeling_ .



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-22-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-22-0.png)
## Learning Dynamics & Re-Warmup

##### Re-Warmup is Optional


- Re-Warmup: increase a small learning

rate to keep training a pre-trained
language model on new data.


- Re-warmup is essential in CPT for training

stability in the early stage.


- Even if the checkpoint is trained well, rewarmup helps transition to new data
distributions.


Gupta, Kshitij, et al. "Continual Pre-Training of Large Language Models: How to re-warm your model?." _Workshop on_
_Efficient Systems for Foundation Models@ ICML2023_ .



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-23-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-23-0.png)
## Learning Dynamics & Re-Warmup

##### Model Size, Domain Similarity, and Order


- Small models learn and forget faster.

- The order of domain exposure and their similarity affect forgetting and transfer.


Yıldız, Çağatay, et al. "Investigating Continual Pretraining in Large Language Models: Insights and
Implications." _Transactions on Machine Learning Research_ .



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-24-2.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-24-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-24-1.png)
## Learning Dynamics & Re-Warmup

##### Chinchilla Scaling and Token Budgeting


- Optimal training involves proportional scaling of model size and training tokens.

- Empirically, feeding more data is often better than just scaling parameters.


Hoffmann, Jordan, et al. "Training compute-optimal large language models." Proceedings of the 36th International
Conference on Neural Information Processing Systems. 2022.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-25-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-25-0.png)
## Learning Dynamics & Re-Warmup

##### Automated Mixture Tuning: DoReMi and Mixing Laws


- The sampling ratio from different domains strongly affects performance.

- DoReMi uses a small proxy model to estimate weights, then trains the large one.


Xie, Sang Michael, et al. "Doremi: Optimizing data mixtures speeds up language model pretraining." _Advances in Neural_
_Information Processing Systems_ 36 (2023): 69798-69818.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-26-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-26-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-27-1.png)
## Learning Dynamics & Re-Warmup

##### Data Selection via Perplexity and Similarity


- Moore-Lewis filtering and perplexity-based pruning are simple and effective.

- Perplexity-to-benchmark correlation helps select samples without training.


Moore, Robert C., and William Lewis. "Intelligent selection of language model training data." _Proceedings of the ACL 2010_


_Thirteenth International Conference on Learning Representations_ .





![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-27-0.png)
## Forgetting, Retention, and Replay

##### True vs. Spurious Forgetting


- A drop in performance is not always due to lost knowledge; it may be caused by

formatting or alignment mismatches.

- Evaluation must separate: output format, factual correctness, and reliability.


Zheng, Junhao, et al. "Spurious Forgetting in Continual Learning of Language Models." _The Thirteenth International_
_Conference on Learning Representations_ .



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-28-2.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-28-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-28-1.png)
## Forgetting, Retention, and Replay

##### Replay: Explicit and Self-Synthesised


- Experience replay: mix a small

portion of “old distribution” data
during new training.


- Self-synthesised replay: the model

generates “knowledge cards” for
cheap rehearsal.


Huang, Jianheng, et al. "Mitigating Catastrophic Forgetting in Large Language Models with Self-Synthesized
Rehearsal." _ACL (1)_ . 2024.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-29-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-29-0.png)
## Forgetting, Retention, and Replay

##### Regularisation and Parameter Anchoring


- EWC is prone to diminishing effects in large models unless combined with

scheduling or data replay.


Kruengkrai, Canasai, and Junichi Yamagishi. "Mitigating the diminishing effect of elastic weight consolidation." _Proceedings_
_of the 29th International Conference on Computational Linguistics_ . 2022.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-30-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-30-0.png)
## Evaluation and Monitoring

##### General Benchmarking and Contamination Control


- Common suites (MMLU, BBH) must be de-duplicated and checked for leakage.

- Long-term evaluation should emphasize A/B consistency and statistical power.


Soldaini, Luca, et al. "Dolma: An open corpus of three trillion tokens for language model pretraining research." _Proceedings_
_of the 62nd annual meeting of the association for computational linguistics (volume 1: long papers)_ . 2024.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-31-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-31-0.png)
## Evaluation and Monitoring

##### Freshness Evaluation: FreshQA and UnSeenTimeQA


- FreshQA: tests models’ ability to absorb recent facts via time-split QA.


Vu, Tu, et al. "Freshllms: Refreshing large language models with search engine augmentation." _Findings of the Association_
_for Computational Linguistics: ACL 2024_ . 2024.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-32-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-32-0.png)
## Evaluation and Monitoring

##### Freshness Evaluation: FreshQA and UnSeenTimeQA


- UnSeenTimeQA:

- broader time spans and

more diverse sources for
freshness benchmarking.


Uddin, Md Nayem, et al. "Unseentimeqa: Time-sensitive question-answering beyond llms’ memorization." Proceedings of
the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2025.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-33-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-33-0.png)
## Evaluation and Monitoring

##### Online Monitoring and Rollback


- During training: monitor with PPL curves and old-task probes.

- Post-deployment: set up drift alerts and rollback plans.


Liao, Chonghua, et al. "Exploring forgetting in large language model pre-training." Proceedings of the 63rd Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers). 2025.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-34-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-34-0.png)
## Engineering and Infrastructure

##### Attention and Parallelism: Save Time and Memory


- FlashAttention: boosts throughput and lowers memory usage.

- ZeRO or Offload is essential for large models on small clusters.


Dao, Tri, et al. "Flashattention: Fast and memory-efficient exact attention with io-awareness." _Advances in neural_
_information processing systems_ 35 (2022): 16344-16359.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-35-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-35-0.png)
## Engineering and Infrastructure

##### Data Pipelines and Reproducibility


- Ensure full pipeline traceability: mixture, version, filtering must be logged.

- Use small proxy runs before scaling to save compute.


Xie, Sang Michael, et al. "Doremi: Optimizing data mixtures speeds up language model pretraining." _Advances in Neural_
_Information Processing Systems_ 36 (2023): 69798-69818.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-36-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-36-0.png)
## Domain-Specific and Cross-Lingual CPT

##### Finance and Industry Domains: Small but High-Quality Wins


- Carefully selected domain corpora for

CPT can yield major gains on a small
budget.


- Watch for compliance, IP concerns, and

representativeness of the domain data.


Xie, Yong, Karan Aggarwal, and Aitzaz Ahmad. "Efficient continual pre-training for building domain specific large language
models." _Findings of the Association for Computational Linguistics ACL 2024_ . 2024.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-37-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-37-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-38-1.png)
## Domain-Specific and Cross-Lingual CPT

##### Cross-Lingual: Vocabulary Expansion and Parallel Data


- Expanding the vocabulary and scaling native-language data consistently improves

performance.

- Watch for compliance, IP concerns, and representativeness of the domain data.


Capabilities." _First Conference on Language Modeling_ .



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-38-0.png)
## Continual Pre-Training

##### Takeaways

###### - Refresh LLMs with new domains and facts without full retraining. - Training order, data mix, and re-warmup drive stability. - Prioritize efficiency, contamination control, and freshness evaluation.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-39-0.png)


![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-40-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-40-1.png)
## **PART III** **_Continual Instruction Tuning_**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-40-2.png)


## Recap: Multiple-stage Training of LLMs



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-41-0.png)





**1** Alignment **2** Finetune aligned model **3** Continual alignment





43



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-41-1.png)
## Introduction to Continual Instruction Tuning


 - **Definition**

    - Finetune the LLMs to learn how to follow instructions and transfer knowledge for
new tasks.




- **Goals**



Question
Translation
Answering



**Adapt to new tasks.**




- Adapt to new tasks and domains.

- Adapt to new skills and tools. Legal
Domain



Medical
Domain



Math
###### …
Solving


Financial
###### …

Domain


Tool Ver.
###### …

3.0



**Adapt to new domains.**



Tool Ver.

1.0



Tool Ver.

2.0



**Adapt to new skills and tools.**





44



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-42-0.png)
## Difference between CIT and CPT












|Difference|Continual Instruction Tuning (CIT)|Continual Pre-training (CPT)|
|---|---|---|
|Goals|How to utilize knowledge to solve<br>tasks|How to learn new knowledge|
|Training|Supervised training|Unsupervised training|
|Data|Instruction following dataset|Text corpus dataset|
|Challenges|1. How to adapt to new<br>tasks/domains?<br>2. How to prevent forgetting in old<br>tasks/domains?<br>3. How to learn new skills and<br>tools?|1. How to prevent knowledge forgetting?|



**Supervised CIT**


Domains, Tasks,
Tools…



**Instruction:** Please **Unsupervised CPT**
answer the following
question.
**Q** : Who won the 60th A fox jumps over
U.S. president the lazy _
election?
**Answer** : _



45



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-43-1.png)
## Roadmap of Methods


 - **Adapt to new tasks and domains.**

     - Fine-tuning on series of tasks/domains.

     - Parmeter-efficient tuning.

     - In-context learning.

     - Multi-experts.


 - **Adapt to new skills and tools.**

     - New tools modelling.

     - Tool instruction tuning.



46



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-44-0.png)
## Task and Domains-incremental CIT


 - **Definitions:**

   - Task/Domains-incremental Continual Instruction Tuning aims to continuously
finetune LLMs on a sequence of task/domain-specific instructions and acquire
the ability to solve novel tasks.




- **Methods:**

   - Finetuning on series of tasks/domains.

   - Parmeter-efficient tuning.

   - In-context learning.

   - Multi-experts.

   - Plug-in-memory.



Question
Translation
Answering


**Adapt to new tasks.**



Legal
Domain



Medical
Domain



Math
Solving


Financial
###### …

Domain



**Adapt to new domains.**



47



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-45-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-46-1.png)
## Finetuning on Series of Tasks and Domain

**Issues:** catastrophic forgetting of the learned knowledge and problem

solving skills in previous tasks.


Wang, X., et al. (2023). TRACE: A Comprehensive Benchmark for Continual Learning in Large Language Models. arXiv preprint
48
arXiv:2310.06762.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-46-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-47-2.png)
## Finetuning on Series of Tasks and Domains

**Data distributions under different domains and tasks are different.**


 - Simple data selection strategy that retrieves unlabelled text from the in-domain
corpus, aligning it with the task distribution ( **Reply** ).


**Vocabulary overlap (%) between domains.**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-47-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-47-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-48-2.png)
## Finetuning on Series of Tasks and Domains

**Separate training and model merging.**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-48-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-48-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-49-1.png)
## Finetuning on Series of Tasks and Domains

**Adaptive merging weights from different domains**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-49-0.png)
## Parmeter-efficient Tuning

**LoRA fine-tuning only finetunes a small, low-rank portion of the model's**
**parameters.**



5
2



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-50-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-50-1.png)
## Parmeter-efficient CIT

**LoRA fine-tuning in continual instruction tuning.**


 - Learn LoRA parameters for each task in orthogonal space.


Wang, X., Chen et al. (2023, December). Orthogonal Subspace Learning for Language Model Continual Learning. EMNLP 2023
Findings



5
3



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-51-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-51-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-52-2.png)
## In-context Learning

**In-context learning (ICL) allows LLMs to learn from examples without changing**
**their weight.**


5
https://ludwig.ai/latest/user_guide/llms/in_context_learning/
4



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-52-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-52-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-53-1.png)
## Parmeter-free CIT

**Retrieval-based continual instruction tuning.**


Wan, Z., et al. (2024, August). Reformulating Domain Adaptation of Large Language Models as Adapt-Retrieve-Revise: A Case Study
55
on Chinese Legal Domain. ACL 2024 Findings.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-53-0.png)
## Multi-experts

**Exploring the benefits of training expert language models over instruction tuning**

- Train small expert adapter on top LLM for each task



56



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-54-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-54-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-55-1.png)
#### Multi-experts CIT

**Select different expert LLMs for each tasks.**


Zhao, W., et al. (2024, August). Sapt: A shared attention framework for parameter-efficient continual learning of



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-55-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-56-1.png)
#### Plug-in-memory Domain-incremental CIT

**Train a memory module for each domain.**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-56-0.png)
## Tool-incremental CIT


 - **Definitions:**

   - Tool-incremental Continual Instruction Tuning (Tool-incremental CIT) aims to
fine-tune LLMs continuously, enabling them to interact with the real world and
enhance their abilities by integrating with tools, such as calculators, search
engines, and new code libraries.


 - **Methods:**

   - Learn to understand new tools.

   - Learn to use new tools.



59



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-57-0.png)
## Learn to Use New Tools

**Continual teach LLMs to learn how to use new tools.**


Qin, Y., et al. ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. ICLR 2024.



60



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-58-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-58-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-59-1.png)
#### Learn to Use New Tools

**How to represent tools and how to select tools for CIT?**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-59-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-60-1.png)
## Learn to use new external tools

**Reinforcement Learning enables better tools usage.**


Computing 3 (2024): 0063.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-60-0.png)
## Summary of CIT


 - **Goal:**

    - CIT finetune the LLMs to learn how to follow instructions and transfer knowledge
for new tasks.

 - **Pros and Cons**








- **Limitations:**

|Methods|Pros.|Cons.|
|---|---|---|
|Finetuning on series<br>of tasks/domains|Easy to use|Training efficiency<br>issues|
|Parmeter-efficient<br>CIT|Increase efficiency|Less effective|
|In-context CIT|Training free|Limited performance|
|Multi-experts|Generability|Model size|



   - Forget of knowledge learned during CPT.

   - Response of instructions is not aligned with human => **Continual Alignment.**



6
3



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-61-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-62-0.png)
## **PART** **IV** **_Continual Alignment_**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-62-2.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-62-1.png)
## Recap: Multiple-stage Training of LLMs



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-63-0.png)





![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-63-1.png)

**1** Alignment **2** Finetune aligned model **3** Continual alignment


6
Cite
5


## Alignments of Large Language Models

Alignment is the method of steering the generative process to satisfy a
specified property, reward or affinity metric.


Askell et al. 2021. A General Language Assistant as a Laboratory for Alignment. Arxiv 2112.00861



6
6



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-64-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-64-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-65-1.png)
## Reinforcement Learning with Human Feedback

6
[Lambert & Ustalov. Reinforcement Learning with Human Feedback Tutorial. ICML 2023.](https://icml.cc/media/icml-2023/Slides/21554.pdf)
7



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-65-0.png)
## Alignment Tax


- _Alignment-forgetting trade-off_ : aligning LLMs with RLHF can lead to
forgetting pretrained abilities


[Noukhovitch et al. 2023. Language Model Alignment with Elastic Reset. In NeurIPS 2023.](https://openreview.net/forum?id=6lgugutkin)
Lin et al. 2024 Mitigating the Alignment Tax of RLHF. In EMNLP 2024



6
8



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-66-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-66-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-67-2.png)
## RLHF is a trade-off

6
[Noukhovitch et al. 2023. Language Model Alignment with Elastic Reset. In NeurIPS 2023.](https://openreview.net/forum?id=6lgugutkin)
9



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-67-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-67-1.png)
## Elastic Research

Periodically reset the online model to an exponentially moving average
(EMA) of itself


[Noukhovitch et al. 2023. Language Model Alignment with Elastic Reset. In NeurIPS 2023.](https://openreview.net/forum?id=6lgugutkin)



7
0



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-68-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-68-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-69-2.png)
## Elastic Research

7
[Noukhovitch et al. 2023. Language Model Alignment with Elastic Reset. In NeurIPS 2023.](https://openreview.net/forum?id=6lgugutkin)
1



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-69-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-69-1.png)
## Heterogeneous Model Averaging (HMA)

Interpolating between pre and post RLHF model weights


[Lin et al. 2024 Mitigating the Alignment Tax of RLHF. In EMNLP 2024](https://arxiv.org/abs/2309.06256v4)



7
2



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-70-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-70-1.png)
## Heterogeneous Model Averaging (HMA)

Interpolating between pre and post RLHF model weights archives the
most strongest alignment-forgetting Pareto front


[Lin et al. 2024 Mitigating the Alignment Tax of RLHF. In EMNLP 2024](https://arxiv.org/abs/2309.06256v4)



7
4



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-71-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-71-1.png)
## Model Averaging vs Experience Replay

Model averaging outperform Experience Replay on 2 out of 3 datasets


[Lin et al. 2024 Mitigating the Alignment Tax of RLHF. In EMNLP 2024](https://arxiv.org/abs/2309.06256v4)



7
5



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-72-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-72-1.png)
## Recap: Multiple-stage Training of LLMs



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-73-0.png)





**1** Alignment **2** Finetune aligned model **3** Continual alignment



7
6



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-73-1.png)
## Fine-tuning Aligned LLMs Compromises Safety

Fine-tuning GPT-3.5 Turbo leads to safety degradation with
harmfulness scores increase across 11 categories after fine-tuning


Qi, Xiangyu, et al. "Fine-tuning aligned language models compromises safety, even when users do not intend to!." ICLR 2024



7
7



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-74-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-74-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-75-1.png)
## Mitigating Alignment Tax

Experience replay: mixing safety samples to fine-tuning data


Ouyang, Long, et al. "Training language models to follow instructions with human feedback." NeurIPS 2022



7
8



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-75-0.png)
## Safety Re-alignment

Interpolation between the domain and alignment delta parameters


Thakka et al. 2025. Combining Domain and Alignment Vectors Provides Better Knowledge-Safety Trade-offs in LLMs. ACL
2025



79



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-76-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-76-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-77-2.png)
## Safety Re-alignment

Thakka et al. 2025. Combining Domain and Alignment Vectors Provides Better Knowledge-Safety Trade-offs in LLMs. ACL
80
2025



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-77-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-77-1.png)
## Recap: Multiple-stage Training of LLMs



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-78-0.png)





![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-78-1.png)

**1** Alignment **2** Finetune aligned model **3** Continual alignment


8
Cite
1


## Diverse Nature of Human Preference


- High level ethical principles


- Culturally specific values


- Laws and regulations


- Social etiquette and best practices in
various human societies and
professional settings


- Domain-specific human preferences


Sorensen et al. 2024 A Roadmap to Pluralistic Alignment. ICML 2024



8
2



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-79-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-79-1.png)
## Human Values and Preferences Evolves


- Societal values, social norms and ethical guidelines evolves over
times

- Preference diversity across different demographic groups

- Individual’s preference changing overtime


Qiu et al. “ProgressGym: Alignment with a Millennium of Moral Progress”. NeurIPS 2024



8
3



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-80-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-80-1.png)
## Two Scenarios of Continual Alignment


 - Updating value or preference

  - Update LLMs to reflect shifts in societal values

  - Unlearn outdated custom

  - Incorporating new values

  - Similar to model editing and machine unlearning


 - Integrate new value

  - Adding new demographic groups or value type

  - Preserve the previous learned values

  - Similar to standard continual learning problem



8
4



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-81-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-82-1.png)
## Persona Prompting

8
Hu and Collier. "Quantifying the Persona Effect in LLM Simulations." ACL 2024
5



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-82-0.png)
## Overgeneralization

Prompting-based approach is efficient, but tends overgeneralize, i.e.
forgetting the preferences on unrelated targets


Stephan et al.. "RLVF: Learning from Verbal Feedback without Overgeneralization." ICML 2024



8
6



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-83-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-83-1.png)
## Control Overgeneralization


- Fine-tuning with DPO on the in-scope data

- Supervised context distillation (SCD) on the out-of-scope and nearscope dataprompts


Stephan et al.. "RLVF: Learning from Verbal Feedback without Overgeneralization." ICML 2024



8
7



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-84-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-84-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-85-1.png)
## Control Overgeneralization

8
Stephan et al.. "RLVF: Learning from Verbal Feedback without Overgeneralization." ICML 2024
8



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-85-0.png)
## Continual RLHF Training


- A desired policy should always generate high-reward results with
high probabilities

- Categorize the rollout samples into five types according to their
rewards and generation probabilities


Zhang et al. ”CPPO: Continual Learning for Reinforcement Learning with Human Feedback” ICLR 2024



8
9



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-86-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-86-1.png)
## Continual Proximal Policy Optimization (CPPO)

- Each rollout type has a weighting strategy for policy learning (α(x))
and knowledge retention (β(x))



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-87-0.png)

clipped policy
learning



knowledge
retention
penalty term



Zhang et al. ”CPPO: Continual Learning for Reinforcement Learning with Human Feedback” ICLR 2024



9
0



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-87-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-88-1.png)
## Continual Proximal Policy Optimization (CPPO)

- CPPO exhibits better training stability


unable to continuously increase the reward score


Zhang et al. ”CPPO: Continual Learning for Reinforcement Learning with Human Feedback” ICLR 2024



9
1



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-88-0.png)
## Continual Proximal Policy Optimization (CPPO)

- CPPO exhibits better training stability


Training process of Task-2. The PPO algorithm is unstable at 7k steps
and is unable to continuously increase the reward score


Toy settings with 2 summarization tasks
How does it perform in the Helpful, Honest, Harmless framework in alignments?


Zhang et al. ”CPPO: Continual Learning for Reinforcement Learning with Human Feedback” ICLR 2024



9
2



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-89-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-89-1.png)
## Summary



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-90-0.png)






- Overgeneralization to the new preferences


- Continual alignment is still under explored due to lack of data



9
3



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-90-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-91-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-91-1.png)
## **PART** **V** **_“Non-Parametric” Continual Learning_** **_& Lifelong Agents_**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-91-2.png)


## Why Now?

##### Four Pain Points of Parametric Continual Learning

Freshness, Forgetting, Domain transfer,
and Tool (or interface) explosion



95



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-92-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-92-1.png)
## Non-Parametric Continual Learning

##### Definition and Contrast

Parametric:

- pretraining, fine-tuning; update model weights (Δθ)


Non-Parametric:

- external memory / communication graph / prompt; update structure (ΔS)


Move less in weights, more in memory and structure


Gutiérrez, Bernal Jiménez, et al. "From rag to memory: Non-parametric continual learning for large language models." _arXiv_
_preprint arXiv:2502.14802_ (2025).



96



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-93-0.png)
## Non-Parametric Continual Learning

##### Evolving Path: From Naive Retrieval to Graph-RAG


 - Evolves from vector retrieval to
graph-based routing and
summarisation


 - Enables multi-hop reasoning and
scalable knowledge organisation


Edge, Darren, et al. "From local to global: A graph rag approach to query-focused summarization." _arXiv preprint_
_arXiv:2404.16130_ (2024).



97



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-94-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-94-1.png)
## Non-Parametric Continual Learning

##### Evolving Path: From Naive Retrieval to Graph-RAG

“Structured Association”
outperforms stacking pure
similarity


Edge, Darren, et al. "From local to global: A graph rag approach to query-focused summarization." _arXiv preprint_
_arXiv:2404.16130_ (2024).



98



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-95-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-95-1.png)
## Non-Parametric Continual Learning

##### HippoRAG

Hippocampus-like Index
with Personalised
PageRank (PPR)


- Knowledge Graph

- Multi-hop QA


Jimenez Gutierrez, Bernal, et al. "Hipporag: Neurobiologically inspired long-term memory for large language
models." _Advances in Neural Information Processing Systems_ 37 (2024): 59532-59569.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-96-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-96-0.png)
## Non-Parametric Continual Learning

##### HippoRAG 2: From RAG to Long-term Memory Systems

The persistent, evolvable memory layer serves as the operating system of continual
learning.


Gutiérrez, Bernal Jiménez, et al. "From rag to memory: Non-parametric continual learning for large language models." _ICML_
_2025_



10
0



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-97-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-97-1.png)
## Non-Parametric Continual Learning

##### HippoRAG 2: From RAG to Long-term Memory Systems

Improvements on associative memory tasks and online updates


Gutiérrez, Bernal Jiménez, et al. "From rag to memory: Non-parametric continual learning for large language models." _ICML_
_2025_



10
1



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-98-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-98-1.png)
## Non-Parametric Continual Learning

##### Memory Write Policies

Treat “writing” as a policy discipline, not a naive “dump everything”


- minimal successful evidence chains

- failure counterexamples

- Rules and constraints

- Reusable templates


Zhang, Zeyu, et al. "A survey on the memory mechanism of large language model-based agents." _ACM Transactions on_
_Information Systems_ 43.6 (2025): 1-47.



10
2



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-99-0.png)
## Non-Parametric Continual Learning

##### Example

ChatGPT’s Memory


- You can tell ChatGPT what to

remember, or let it learn over time


- Memory improves with continued

use, enabling personalised
assistance


- Supports recall of preferences,

context, and tasks across chats


https://openai.com/index/memory-and-new-controls-for-chatgpt/



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-100-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-100-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-101-1.png)
## Memory of LLM-based Agents

##### AI Model v.s. AI Agent



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-101-0.png)
## Memory of LLM-based Agents

##### Memory-as-a-System

Treat memory as a “Bus and Policy Layer” Not just storage, but governed interaction


Zhang, Zeyu, et al. "A survey on the memory mechanism of large language model-based agents." _ACM Transactions on_
_Information Systems_ 43.6 (2025): 1-47.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-102-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-102-0.png)
## Memory of LLM-based Agents

##### Memory Spectrum

Short-term:

- Context window / KV cache


Mid-term:

- Conversational episodic traces


Long-term:

- Semantic, programmatic, and
graph memory


Yang, Hongkang, et al. "Memory3: Language modeling with explicit memory." _arXiv preprint_
_arXiv:2407 01178_ (2024)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-103-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-103-0.png)
## Self-Evolving LLM-based Agents

##### Position: Why Episodic Memory Matters

Five properties:

- single-binding (one-shot capture),

- context-sensitive retrieval,

- fast adaptation,

- temporal sequencing,

- explicit provenance and attribution


Complementarity: Episodic Memory + Semantic / Programmatic Memory

- episodes supply fresh cues; semantics or programs generalise, compose, and reuse


Pink, Mathis, et al. "Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents." _arXiv preprint_
_arXiv:2502.06975_ (2025).



10
7



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-104-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-104-1.png)
## Self-Evolving LLM-based Agents

##### Experience-centred Self-Evolution

Definition


Self-evolving AI agents are autonomous systems that continuously and systematically
optimise their internal components through interaction with environments, with the goal
of adapting to changing tasks, contexts and resources while preserving safety and
enhancing performance.


Fang, Jinyuan, et al. "A comprehensive survey of self-evolving ai agents: A new paradigm bridging foundation models and
continual agentic systems." _arXiv preprint arXiv:2508.07407_ (2025).



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-105-0.png)


## Self-Evolving LLM-based Agents

##### Experience-centred Self-Evolution

Strategy Tuning ≠ Weight
Tuning


- Evolving Targets:

  - Tools

  - Workflows

  - Prompts

  - Sub-programs


Fang, Jinyuan, et al. "A comprehensive survey of self-evolving ai agents: A new paradigm bridging foundation models and
continual agentic systems." _arXiv preprint arXiv:2508.07407_ (2025).



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-106-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-106-0.png)
## Self-Evolving LLM-based Agents

##### Evaluation: Learning Curves and Stability



Key Metrics:
✓ Task success rate
✓ Reflection gains
✓ Memory reuse rate
✓ Cost and latency



Benchmark Types:
✓ Task-specific setups
✓ Interactive agent environments
✓ Tool-chain workflows



Zheng, Junhao, et al. "Continual learning of large language model based agents: A roadmap." _arXiv preprint_
_arXiv:2501.07278_ (2025).



11
0



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-107-0.png)
## Memory of LLM-based Agents

##### LightMem: Long-Short Term Agentic Memory


- STM ≠ Context
STM ≈ Context + Attention


- LTM ≠ Σ Trajectory_raw
LTM = Abstract Knowledge +
Evolving Skills


- Ideal Agentic Memory:

- Low cost, high accuracy,
strong retention.


Fang, Jizhan, et al. "LightMem: Lightweight and Efficient Memory-Augmented Generation." _arXiv preprint_
_arXiv:2510.18866_ (2025).



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-108-1.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-108-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-109-2.png)
## Topological and Prompt Optimisation

##### Prompt Optimisation: From APE to Planner-Aware APO

APE: black-box search for human-level instruction generation
RePrompt: planning-aware automated prompt engineering


11
Cite
2



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-109-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-109-1.png)
## Topological and Prompt Optimisation

##### Why Learn “Agentic Topology”?


 - Fixed triangle (Planner-Worker-Critic) destabilises across domains

 - Goal: task-adaptive balance between sparsity and density


Zhang, Guibin, et al. "G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks." _Forty-_
_second International Conference on Machine Learning_ .



11
3



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-110-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-110-1.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-110-2.png)
## Topological and Prompt Optimisation

##### Adaptive Topology: Designers and Routers

Key Concepts:

 - Conditional graph generation and search

 - Constraints:

   - cost (tokens, time, etc),

   - computation resources (size of base model),

   - Availability of tools


Trade-offs:

 - Lightweight adaptation (e.g. heuristic routing) vs. High-cost global search (e.g. full
topology optimisation)


Yue, Yanwei, et al. "Masrouter: Learning to route llms for multi-agent systems." _arXiv preprint arXiv:2502.11133_ (2025).



11
4



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-111-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-112-1.png)
## Topological and Prompt Optimisation

##### CARD

(Conditioned Agent
Graph Designer)


- Featured by
runtime resourceaware adaptation


Wu, Tongtong, et al. Conditioned Agent Graph Designer.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-112-0.png)
## Topological and Prompt Optimisation

##### Joint Optimisation: Topology & Prompt

Two-stage: topology-thenprompt alternating; or unified
joint objective


Metrics: success rate, comms


Example:
GPT-Swarm


Zhuge, Mingchen, et al. "Gptswarm: Language agents as optimizable graphs." _Forty-first International Conference on_
_Machine Learning_ . 2024.



11
6



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-113-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-113-1.png)
## Topological and Prompt Optimisation

##### Joint Optimisation: Topology & Prompt

AFLOW


Automated framework using
MCTS to refine workflows via

and tree-structured memory.


Zhang, Jiayi, et al. "AFlow: Automating Agentic Workflow Generation." _The Thirteenth International Conference on Learning_
_Representations_ .



11
7



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-114-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-114-1.png)
## Lifelong LLM-based Agents

##### Takeaways

###### - Shift from weight updates to memory- and structure-based learning. - Treat memory as a governed system, not passive storage. - Optimize agent topology and prompts for adaptive coordination.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-115-0.png)


![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-116-0.png)
## **PART** **VI** **_Insights, Challenges_** **_and Open Problems_**



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-116-2.png)



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-116-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-117-0.png)
## Insights, Challenges and Open Problems

##### Reinterpreting the CL Paradigm for LLMs

Early paradigms like task-, domain-, or class-incremental learning, and core strategies
such as regularisation, replay, and parameter isolation, were built for small static models.


For LLMs, these are forms, not goals.


The true constraints lie in model scale, compliance, auditability, and real-world data flow.
Continual learning must be redefined for deployment settings rather than controlled lab
conditions.


12
Verwimp, Eli, et al. "Continual learning: Applications and the road forward." _arXiv preprint arXiv:2311.11908_ (2023).
0


## Insights, Challenges and Open Problems

##### Forgetting Across Stages Remains Fundamental

Modern LLM training proceeds through stages `：` pretraining, continual pretraining,
instruction tuning, alignment, and downstream adaptation.


Forgetting now happens across stages, not just between tasks.


As objectives shift from language modelling to preference and tool-use success,
maintaining stability becomes harder.


Future continual learning must explicitly address cross-stage stability.


Wu, Tongtong, et al. "Continual learning for large language models: A survey." _arXiv preprint arXiv:2402.01364_ (2024).



121



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-118-0.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-119-2.png)
## Insights, Challenges and Open Problems

##### From Snapshot Learning to Trajectory Learning


- Current LLMs learn from static, time-agnostic data snapshots.

- Mixed datasets blur version and temporal boundaries, obscuring when facts were valid.

- However, time and version awareness are essential for trustworthy AI.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-119-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-119-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-120-1.png)
## Insights, Challenges and Open Problems

##### From Massive Learning to Decomposed Adaptation


- Traditional fine-tuning entangles all knowledge in a shared parameter space

We propose disentangling into modular subspaces:

  - Language vs. Semantics

  - Facts vs. Skills

- Enables targeted adaptation, faster updates, and lower continual learning cost



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-120-0.png)
## Insights, Challenges and Open Problems

##### From Massive Learning to Decomposed Adaptation


- Traditional fine-tuning entangles all knowledge in a shared parameter space

We propose disentangling into modular subspaces:

  - Language vs. Semantics

  - Facts vs. Skills

- Enables targeted adaptation, faster updates, and lower continual learning cost


Chen, Yongrui, et al. "K-DeCore: Facilitating Knowledge Transfer in Continual Structured Knowledge Reasoning via
Knowledge Decoupling." _arXiv preprint arXiv:2509.16929_ (2025).



124



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-121-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-121-1.png)
![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-122-0.png)
## Insights, Challenges and Open Problems

##### From Learning from Data to Learning from Experience

After ChatGPT’s rise, community knowledge sources like StackOverflow declined.


**The web is no longer a steady source of new human data.**


Continual learning must shift from passive data intake to active experience learning.
Logs, tool traces, and feedback loops become key training signals.


Zhang, Zeyu, et al. "A survey on the memory mechanism of large language model-based agents." _ACM Transactions on Information_
_Systems_ 43.6 (2025): 1-47.


## Insights, Challenges and Open Problems

##### The Epistemic Boundaries of LLMs


- LLMs operate across four knowledge zones:


**1. Known; 2. Knowable but unseen; 3. Knowable but hard; 4. Unknowable**


- Continual learning should recognise and respect these epistemic limits, enabling
epistemic-aware scheduling and active learning strategies.


Steyvers, Mark, et al. "What large language models know and what people think they know." _Nature Machine Intelligence_ 7.2 (2025):
221-231.



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-123-0.png)


![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-124-0.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-124-1.png)
# **Q & A**

Tongtong Wu, Linhao Luo, Trang Vu, Reza Haffari



![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-124-2.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-124-3.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-124-4.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-124-5.png)

![](/Users/alex/Alex/monash/continual-learning/refs/monash/images/Continual-Learning-of-Large-Language-Model.pdf-124-6.png)
