# Proposal 05: 基于 Human Feedback 的长程持续学习 Arena 评测基准

## 核心主张与目标

**核心洞察**：大量的固定套路 Benchmark 极易被作弊或过拟合。在长程推理和记忆维持任务中，人类用户对“模型是否还记得过去的设定与互动”感知是极其敏锐且不可替代的。

**目标**：构建第一个面向持续学习领域的 **Continual Learning Arena**（持续学习竞技场）。依托于一个真实上线的、具有结构化叙事特征的 AI 陪伴/文字冒险类应用，通过搜集真实玩家的对话数据与偏好反馈，来量化评估不同 LLM 、记忆工程策略或微调架构在真正的长文本跨度、长周期情境下的持续学习表现。

---

## 竞技场沙盒：结构化叙事 AI 引擎

为了支撑这个评估基准，本研究计划利用一款已经搭建并准备发布的 **结构化叙事 AI 引擎 (Anify Engine)** 作为沙盒平台。

与市面上常规的基于无状态 Prompt 的闲聊类（Chit-chat）陪伴竞品不同，Anify 引擎在底层维护了一个严格的 **结构化剧情大纲与长程状态机 (TRPG 风格)**：

- 玩家与专属的 AI 伙伴 (Game Master 驱动) 一同进行无尽的 TRPG 冒险。
- 在引擎的 `NarrativeState` 中，实时且持久化地追踪极端复杂的长程状态：
  - **动态角色关系 (`characterRelations`)**：追踪每一位 NPC 的精确好感度 (`favorability`)、互动往事 (`summary`) 与重大事件 (`significantEvents`)。
  - **区域冒险进度 (`adventureProgress`)**：追踪地理维度的探索次数、被击败的特定敌人 (`defeatedEnemies`) 与区域叙事状态。
  - **动态战役与任务 (`CampaignMeta` & `DynamicQuest`)**：包含严格的前置条件 (`prerequisites`)、触发 Flag (`completionFlags`) 以及多路线分支。
  - **长文本记忆流 (`gmMemory`)**：按时间窗口压缩与滚动的剧情摘要。

**为什么这是完美的测试床？**
这种“非结构化自然语言交互 + 强结构化底层状态”的双轨长程用例，对 LLM 的持续学习能力提出了最极致且真实的考验。AI 必须在数十万 Token 的长周期里，维系对话文本与底层 `NarrativeState` 严丝合缝的一致性（绝不能复活已被标记在 `defeatedEnemies` 中的 Boss，也不能遗忘 `characterRelations` 中记录的深度羁绊）。用户对这种状态错乱的主观“痛感”和敏感度会被极大放大，从而提供极高质量的人类反馈（Human Feedback）。

---

## 评估协议与机制设计 (Evaluation Protocol)

基于 Anify 应用的运行链路，我们将隐式或显式地接入持续学习竞技（Arena）机制：

1. **盲测双盲评比 (Blind A/B Testing)**：
   在触发 `DynamicQuest` 结算、调用历史 `significantEvents` 等高度依赖长程记忆的对话轮次，后台平行调用两种不同的持续学习基座模型（或不同外挂 Memory 架构）。用户只看剧情连贯性和历史记忆的准确度进行盲选（Option A is better / Option B is better / Tie）。
2. **显式剧情连贯性评分 (Coherence Rating)**：
   引入用户反馈按钮（如踩/赞，或特定的话题报错机制：“AI忘了我的设定”）。通过统计每千轮对话的用户纠错率，形成定量的记忆遗忘惩罚率指标。

3. **动态状态机一致性探针 (Dynamic State Tracking Consistency)**：
   区别于由人类主观评价的内容，此项为客观探针。借助于明确的 `NarrativeState` （如好感度、击杀记录），我们在后台自动比对大模型生成的隐式状态参数与其自身刚刚更新到真实物理世界引擎里的状态集是否发生滑移与矛盾。

---

## 预期贡献

1. **破局现有基准**：提出并开源首个基于真实人类长程互动反馈的 Continual Learning Benchmark，终结纯静态数据集跑分的过度拟合问题。
2. **构建高价值数据集**：通过 Arena 收集的高质量 Human Feedback，可沉淀为包含真实长期意图演化和人类奖惩评价的 DPO（Direct Preference Optimization）多轮数据集，供未来的长程模型对齐研究使用。
3. **真实业务指引**：在最贴近商业化 AI 陪伴应用的场景中，直观揭示当前各家 LLM （及外挂架构）在长效记忆留存上的真实差距，具备极高的行业风向标价值。
