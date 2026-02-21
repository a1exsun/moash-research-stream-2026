# RLVF

来源: Continual Learning of Large Language Model

核心机制:
Control Overgeneralization。为了缓解基于 Prompt 调整带来的过度泛化问题(即在非相关任务上也错误地应用了偏好)。对 In-Scope 数据使用 DPO 进行微调，并在 Out-of-Scope 的数据对上进行监督上下文蒸馏 (Supervised Context Distillation, SCD)，来维持原始行为。
