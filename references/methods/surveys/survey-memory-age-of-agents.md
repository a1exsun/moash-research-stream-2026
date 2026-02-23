# Memory in the Age of AI Agents — Survey

**论文：** [arXiv 2512.13564v2](https://arxiv.org/abs/2512.13564)
**来源：** surveys/arXiv-2512.13564v2
**类别：** Survey — Agent Memory全景式分类框架

---

## 核心贡献

提出三维分类框架审视Agent Memory：Forms（存储形式）、Functions（功能目的）、Dynamics（运行机制），覆盖100+系统的系统性综述。

## 三维框架

### Forms — 记忆载体

1. **Token-level Memory** — 显式离散单元，可见可编辑
   - Flat (1D)：无拓扑的序列/集合（MemGPT, Mem0, Reflexion, Voyager等）
   - Planar (2D)：单层结构化组织，树/图（HAT, MemTree, A-MEM, D-SMART等）
   - Hierarchical (3D)：多层互联（GraphRAG, HippoRAG, Zep, AriGraph等）

2. **Parametric Memory** — 存储于模型参数中
   - Internal：直接修改基座模型（预训练/中训/后训阶段）
     - 知识编辑：MEND, ROME, MEMIT, AlphaEdit
     - 角色注入：Character-LM, CharacterGLM, SELF-PARAM
   - External：附加参数模块（不修改原始权重）
     - Adapter：K-Adapter, WISE, ELDER, T-Patcher, MemLoRA
     - 辅助LM：MAC, Retroformer

3. **Latent Memory** — 隐式内部表示（KV cache, 隐状态, 潜在嵌入）
   - Generate：辅助模型生成嵌入（Gist, AutoCompressor, MemoryLLM, M+, LM2, Titans, MemGen）
   - Reuse：直接复用计算状态（Memorizing Transformers, FOT, LONGMEM）
   - Transform：压缩/重组现有状态（Scissorhands, SnapKV, PyramidKV, H2O, RazorAttention, R³Mem）

### Functions — 功能目的

1. **Factual Memory** — 声明性知识库（一致性、连贯性、适应性）
   - User Factual：对话连贯性、目标一致性
   - Environment Factual：知识持久化、多智能体共享访问

2. **Experiential Memory** — 过程性/策略性知识（持续学习、自我进化）
   - Case-based：原始轨迹/解决方案存储
   - Strategy-based：洞见/工作流/模式提取
   - Skill-based：可执行代码/函数/API/MCP

3. **Working Memory** — 有限容量的活跃上下文管理
   - Single-turn：输入压缩与观察抽象
   - Multi-turn：状态整合、分层折叠、认知规划

### Dynamics — 运行机制

1. **Memory Formation** — 原始数据→知识
   - 语义摘要（增量/分区）
   - 知识蒸馏（事实/经验）
   - 结构化构建（实体级/块级）
   - 潜在表示（文本/多模态）
   - 参数内化（知识/能力）

2. **Memory Evolution** — 知识库动态演化
   - 整合（局部/聚类/全局）
   - 更新（外部存储更新/模型编辑）
   - 遗忘（时间/频率/重要性驱动）

3. **Memory Retrieval** — 上下文感知检索
   - 时机与意图自动化
   - 查询构建（分解/重写）
   - 检索策略（词法/语义/图/生成/混合）
   - 后处理（重排序过滤/聚合压缩）

## 前沿方向

1. **检索→生成**：从静态检索到主动生成记忆表示
2. **手工→自动**：从人工设计到自主管理的记忆系统
3. **RL驱动记忆**：从启发式到端到端RL优化的记忆控制
4. **多模态记忆**：跨模态统一存储与检索
5. **多智能体共享记忆**：从隔离到协作认知基底
6. **世界模型记忆**：从数据缓存到状态模拟
7. **可信记忆**：隐私、可解释性、幻觉鲁棒性

## 开源框架

MemGPT/Letta, Mem0, Memobase, MIRIX, MemoryOS, MemOS, Zep, LangMem, SuperMemory, Cognee, Memary等
