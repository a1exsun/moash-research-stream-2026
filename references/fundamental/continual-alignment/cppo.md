# CPPO

Source: Continual Learning of Large Language Model

Core Mechanism:
Continual Proximal Policy Optimization. Designed to overcome the alignment catastrophic forgetting problem in Reinforcement Learning from Human Feedback (RLHF) during Continual Alignment. It implements a policy update strategy based on five combined thresholds of reward and generation probability, providing a retention penalty, which significantly improves training stability.
