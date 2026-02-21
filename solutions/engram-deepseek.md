# Engram — DeepSeek & 北大

**论文：** [arXiv 2601.07372](https://arxiv.org/pdf/2601.07372)
**来源：** 机器之心Pro Week 07
**类别：** LLM Memory — 架构扩展（可扩展查找模块）

---

## 问题

Transformer缺乏原生知识查找原语，需通过低效的深层计算模拟检索。

## 方法

提出"条件记忆"（conditional memory）的稀疏性维度，补充MoE的条件计算范式。设计Engram可扩展查找模块，借鉴经典N-gram嵌入思想，实现O(1)时间复杂度的知识查找，让模型基于输入局部模式快速调用静态知识。

## 机制分析

浅层网络从静态知识重建任务中解放，深层专注复杂推理，等效增加模型有效深度。确定性检索特性支持存算解耦，记忆表可部署于CPU/SSD，降低GPU显存依赖。

## 结果

27B规模，同等参数与FLOPs条件下：
- 知识类：MMLU +3.4, CMMLU +4.0（vs MoE baseline）
- 通用推理：BBH +5.0, ARC-Challenge +3.7
- 代码数学：HumanEval +3.0, MATH +2.4
- 长上下文：Multi-Query NIAH 84.2% → 97.0%
