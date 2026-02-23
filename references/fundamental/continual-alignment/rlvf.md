# RLVF

Source: Continual Learning of Large Language Model

Core Mechanism:
Control Overgeneralization. To alleviate the overgeneralization issue caused by prompt-based tuning (i.e., incorrectly applying preferences to unrelated tasks), it uses DPO for fine-tuning on in-scope data and employs Supervised Context Distillation (SCD) on out-of-scope data pairs to maintain the original behavior.
