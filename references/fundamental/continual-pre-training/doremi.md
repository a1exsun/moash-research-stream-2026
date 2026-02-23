# DoReMi

Source: Continual Learning of Large Language Model

Core Mechanism:
Automated Mixture Tuning. To balance the sampling proportions of different domain data during CPT transition, DoReMi uses a minimal parameter proxy model to estimate and optimize data mixture weights. These weights are then used to train the larger model, significantly improving convergence speed and efficiency.
