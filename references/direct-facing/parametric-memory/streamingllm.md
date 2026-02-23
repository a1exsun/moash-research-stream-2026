# StreamingLLM (2023)

**论文：** (2023)
**来源：** arXiv 2512.13564v2 (Memory in the Age of AI Agents)
**类别：** Parametric Memory — Internal — Pre-Train

---

## 问题

标准Transformer在处理超长序列时，attention计算的内存和时间开销随序列长度增长，且模型在超出训练长度后性能急剧下降，无法支持流式（streaming）场景。

## 方法

发现并利用Attention Sink机制，优化attention的计算效率以增强长窗口记忆能力。核心设计：
- **Attention Sink发现** — 发现模型倾向于将大量attention权重分配给序列最开始的几个token（即attention sink），即使这些token本身语义并不重要
- **Sink Token保留** — 在滑动窗口attention中始终保留最初的几个sink token，确保attention分布的稳定性
- **滑动窗口 + Sink** — 结合固定大小的滑动窗口和sink token，实现在有限内存下对无限长序列的高效处理
- **无需微调** — 该方法可以直接应用于预训练模型，无需额外训练

## 影响

StreamingLLM揭示了Transformer中attention sink的重要现象，为长序列处理提供了简单有效的工程方案。该发现对理解Transformer的attention行为和设计更高效的长序列处理方法具有启发意义。

## 任务

- QA
- Reasoning
