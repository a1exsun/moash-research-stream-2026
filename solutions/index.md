# Solutions Index

按技术分类索引所有整理的技术方案。

---

## Surveys

| 文档                                                                  | 来源               | 关注点                                         |
| --------------------------------------------------------------------- | ------------------ | ---------------------------------------------- |
| [survey-memory-age-of-agents](surveys/survey-memory-age-of-agents.md) | arXiv 2512.13564v2 | Agent Memory三维框架：Forms/Functions/Dynamics |
| [survey-ai-memory-baijia](surveys/survey-ai-memory-baijia.md)         | 机器之心Pro W07    | 4W分类体系，三层AI Memory划分                  |
| [survey-human-to-ai-memory](surveys/survey-human-to-ai-memory.md)     | 机器之心Pro W07    | 认知科学视角的记忆类比框架                     |
| [survey-ai-meets-brain](surveys/survey-ai-meets-brain.md)             | 机器之心Pro W07    | 人脑与Agent Memory统一视角                     |

---

## Token-level Memory

### Flat (1D) — 无拓扑

| 文档                                                     | 核心机制                                             |
| -------------------------------------------------------- | ---------------------------------------------------- |
| [memgpt](token-level-memory/memgpt.md)                   | OS隐喻，Main/External Context虚拟内存层次            |
| [mem0](token-level-memory/mem0.md)                       | 标准化记忆CRUD操作，图+向量混合存储                  |
| [think-in-memory](token-level-memory/think-in-memory.md) | 归纳性thoughts的hash table存储，cluster-level fusion |
| [comedy](token-level-memory/comedy.md)                   | 单模型完成记忆生成、压缩和复用                       |
| [openclaw](token-level-memory/openclaw.md)               | 跨会话个性化记忆工程方案                             |

### Planar (2D) — 单层结构化

| 文档                                     | 核心机制                                 |
| ---------------------------------------- | ---------------------------------------- |
| [hat](token-level-memory/hat.md)         | 层次化聚合树，coarse-to-fine检索         |
| [memtree](token-level-memory/memtree.md) | 动态层次schema，自底向上摘要更新         |
| [a-mem](token-level-memory/a-mem.md)     | 卡片式记忆单元，语义链接构建记忆网络     |
| [d-smart](token-level-memory/d-smart.md) | KG + 推理树混合，neuro-symbolic pipeline |

### Hierarchical (3D) — 多层互联

| 文档                                                                   | 核心机制                                          |
| ---------------------------------------------------------------------- | ------------------------------------------------- |
| [graphrag](token-level-memory/graphrag.md)                             | 社区检测递归聚合，多层图索引                      |
| [hipporag](token-level-memory/hipporag.md)                             | 神经生物学启发，dual-layer graph + PageRank检索   |
| [arigraph](token-level-memory/arigraph.md)                             | 统一图中semantic KG + episodic component          |
| [zep](token-level-memory/zep.md)                                       | 三层时序KG（Episodic/Semantic/Community）         |
| [g-memory](token-level-memory/g-memory.md)                             | 三层图（interaction/query/insight），多智能体共享 |
| [lyfe-agents](token-level-memory/lyfe-agents.md)                       | Working/Short-term/Long-term三层社交模拟          |
| [inside-out-personatree](token-level-memory/inside-out-personatree.md) | PersonaTree分层记忆schema与操作更新               |

---

## Parametric Memory

### Internal — 直接修改模型权重

**Pre-Train / Mid-Train:**

| 文档                                              | 核心机制                                 |
| ------------------------------------------------- | ---------------------------------------- |
| [lmlm](parametric-memory/lmlm.md)                 | 将知识检索记忆存模型中，知识本身在外部库 |
| [streamingllm](parametric-memory/streamingllm.md) | Attention Sink机制优化长窗口记忆         |

**Post-Train — Knowledge Editing:**

| 文档                                                      | 核心机制                                 |
| --------------------------------------------------------- | ---------------------------------------- |
| [rome](parametric-memory/rome.md)                         | Causal tracing定位 + rank-one update注入 |
| [memit](parametric-memory/memit.md)                       | 多层残差分布批量编辑数千事实             |
| [mend](parametric-memory/mend.md)                         | 辅助网络分解梯度实现快速单步编辑         |
| [alphaedit](parametric-memory/alphaedit.md)               | 零空间约束的知识编辑                     |
| [knowledge-editor](parametric-memory/knowledge-editor.md) | 定向内部参数修改                         |

**Post-Train — Other:**

| 文档                                              | 核心机制                              |
| ------------------------------------------------- | ------------------------------------- |
| [self-param](parametric-memory/self-param.md)     | KL divergence蒸馏注入知识，无额外参数 |
| [character-lm](parametric-memory/character-lm.md) | SFT微调注入角色特征/人格              |

### External — 附加参数模块

**Adapter-based:**

| 文档                                                    | 核心机制                                    |
| ------------------------------------------------------- | ------------------------------------------- |
| [k-adapter](parametric-memory/k-adapter.md)             | 任务特定adapter，backbone冻结               |
| [wise](parametric-memory/wise.md)                       | 双参数记忆 + 动态路由选择                   |
| [elder](parametric-memory/elder.md)                     | 多LoRA模块 + 语义路由函数                   |
| [t-patcher](parametric-memory/t-patcher.md)             | 识别并修补"值得修补的神经元"                |
| [memory-decoder](parametric-memory/memory-decoder.md)   | 即插即用，兼具外部RAG灵活性和参数化推理速度 |
| [memlora](parametric-memory/memlora.md)                 | 蒸馏专家adapter实现记忆增强                 |
| [meta-smf](parametric-memory/meta-smf.md)               | 稀疏记忆池，1.3B+1B params，89%→11%遗忘     |
| [engram-deepseek](parametric-memory/engram-deepseek.md) | 条件记忆O(1)查找模块                        |

**Auxiliary LM-based:**

| 文档                                            | 核心机制                                         |
| ----------------------------------------------- | ------------------------------------------------ |
| [mac](parametric-memory/mac.md)                 | Amortization network压缩文档为compact modulation |
| [retroformer](parametric-memory/retroformer.md) | 学习过去任务执行的成败经验                       |

---

## Latent Memory

### Generate — 辅助模型生成嵌入

**Single Modal:**

| 文档                                                                        | 核心机制                                              |
| --------------------------------------------------------------------------- | ----------------------------------------------------- |
| [gist-tokens](latent-memory/gist-tokens.md)                                 | 长prompt压缩为gist tokens                             |
| [autocompressor](latent-memory/autocompressor.md)                           | 长文档编码为summary vectors作soft prompts             |
| [memorag](latent-memory/memorag.md)                                         | LLM生成全局语义隐状态 + hypothetical document查询重写 |
| [memoryllm](latent-memory/memoryllm.md)                                     | 潜在空间内嵌入自更新memory tokens                     |
| [m-plus](latent-memory/m-plus.md)                                           | 跨层长期记忆token池                                   |
| [lm2](latent-memory/lm2.md)                                                 | 每层矩阵形状潜在记忆slot                              |
| [titans](latent-memory/titans.md)                                           | 长程信息压缩为在线更新MLP权重                         |
| [memgen](latent-memory/memgen.md)                                           | 解码时动态生成潜在记忆（Memory Trigger + Weaver）     |
| [emu](latent-memory/emu.md)                                                 | 带return标注的state encoder嵌入                       |
| [memoria-park](latent-memory/memoria-park.md)                               | 三层记忆with engrams（生物学启发）                    |
| [google-nested-learning-hope](latent-memory/google-nested-learning-hope.md) | Nested Optimization                                   |

**Multimodal:**

| 文档                            | 核心机制                                   |
| ------------------------------- | ------------------------------------------ |
| [comem](latent-memory/comem.md) | Q-Former压缩vision-language为固定长度token |
| [xmem](latent-memory/xmem.md)   | 视频对象分割的多阶段KV嵌入记忆             |

### Reuse — 直接复用计算状态

| 文档                                                                | 核心机制                                |
| ------------------------------------------------------------------- | --------------------------------------- |
| [memorizing-transformers](latent-memory/memorizing-transformers.md) | 存储过去KV对，KNN搜索检索               |
| [fot](latent-memory/fot.md)                                         | Memory-attention layers + KNN检索额外KV |
| [longmem](latent-memory/longmem.md)                                 | Residual SideNet持久化历史KV嵌入        |

### Transform — 压缩/重组现有状态

| 文档                                              | 核心机制                                       |
| ------------------------------------------------- | ---------------------------------------------- |
| [scissorhands](latent-memory/scissorhands.md)     | 基于attention scores修剪KV cache               |
| [snapkv](latent-memory/snapkv.md)                 | Head-wise voting聚合高重要性前缀KV             |
| [pyramidkv](latent-memory/pyramidkv.md)           | 跨层重新分配KV预算                             |
| [h2o](latent-memory/h2o.md)                       | Heavy-Hitter Oracle淘汰策略                    |
| [razorattention](latent-memory/razorattention.md) | Effective attention span + compensation tokens |
| [r3mem](latent-memory/r3mem.md)                   | 虚拟记忆tokens + 可逆压缩                      |

---

## Experiential Memory

### Case-based — 原始轨迹/解决方案

| 文档                                      | 核心机制                              |
| ----------------------------------------- | ------------------------------------- |
| [expel](experiential-memory/expel.md)     | Trial-and-error积累，轨迹+洞见混合    |
| [synapse](experiential-memory/synapse.md) | 抽象state-action episodes作上下文示例 |

### Strategy-based — 洞见/工作流/模式

| 文档                                                            | 核心机制                                      |
| --------------------------------------------------------------- | --------------------------------------------- |
| [reflexion](experiential-memory/reflexion.md)                   | 短期trajectory + 长期self-reflection feedback |
| [buffer-of-thoughts](experiential-memory/buffer-of-thoughts.md) | Meta-buffer思维模板检索与实例化               |
| [awm](experiential-memory/awm.md)                               | 从成功轨迹提取可复用工作流                    |

### Skill-based — 可执行代码/函数/API

| 文档                                                                | 核心机制                              |
| ------------------------------------------------------------------- | ------------------------------------- |
| [voyager](experiential-memory/voyager.md)                           | Minecraft中不断增长的可执行技能代码库 |
| [darwin-godel-machine](experiential-memory/darwin-godel-machine.md) | 安全自重写代码，递归自修改            |

### Meta-evolution

| 文档                                          | 核心机制                       |
| --------------------------------------------- | ------------------------------ |
| [memevolve](experiential-memory/memevolve.md) | 联合进化经验知识和底层记忆架构 |

---

## Working Memory

### Single-turn — 输入压缩

| 文档                                     | 核心机制                           |
| ---------------------------------------- | ---------------------------------- |
| [llmlingua](working-memory/llmlingua.md) | Token perplexity估计丢弃可预测内容 |

### Multi-turn — 状态维护

| 文档                                                 | 核心机制                           |
| ---------------------------------------------------- | ---------------------------------- |
| [mem1](working-memory/mem1.md)                       | 共享内部状态 + PPO优化摘要         |
| [memagent](working-memory/memagent.md)               | 固定预算循环记忆 + GRPO优化        |
| [resum](working-memory/resum.md)                     | 周期性历史蒸馏为推理状态           |
| [hiagent](working-memory/hiagent.md)                 | 子目标中心层次化工作记忆           |
| [context-folding](working-memory/context-folding.md) | 可学习折叠策略，自主决定分支与抽象 |

---

## Multi-Agent Memory

| 文档                                                         | 核心机制                                         |
| ------------------------------------------------------------ | ------------------------------------------------ |
| [generative-agents](multi-agent-memory/generative-agents.md) | 社交模拟，recency/importance/relevance三因素检索 |
| [bmam](multi-agent-memory/bmam.md)                           | 海马-新皮层双系统多智能体记忆框架                |

---

## Frameworks — 开源记忆框架

| 文档                                                   | 核心抽象                             |
| ------------------------------------------------------ | ------------------------------------ |
| [memos-framework](frameworks/memos-framework.md)       | MemOS — MemScheduler动态选择记忆类型 |
| [memoryos-framework](frameworks/memoryos-framework.md) | MemoryOS — 层次化S/M/LTM架构         |
| [memobase-framework](frameworks/memobase-framework.md) | Memobase — 结构化profiles            |
| [langmem-framework](frameworks/langmem-framework.md)   | LangMem — Core API + manager         |
| [cognee-framework](frameworks/cognee-framework.md)     | Cognee — Knowledge graph-based       |

---

## Eval — 评估基准

| 文档                                 | 核心机制                             |
| ------------------------------------ | ------------------------------------ |
| [evermembench](eval/evermembench.md) | 细粒度回忆/记忆意识/用户画像三维评估 |

---

## 待展开

| 文档                                                              | 状态               |
| ----------------------------------------------------------------- | ------------------ |
| [mit-beyond-context-limits](pending/mit-beyond-context-limits.md) | 仅提及，待阅读原文 |
