# CPPO

来源: Continual Learning of Large Language Model

核心机制:
Continual Proximal Policy Optimization。在 Continual Alignment 时为了克服在强化学习人类反馈 (RLHF) 中的对齐灾难遗忘问题。设计了根据奖励 (Reward) 及生成概率 (Probability) 的五个组合阈值更新策略，提供策略保留惩罚 (Retention penalty)，以此极大提高训练稳定性。
