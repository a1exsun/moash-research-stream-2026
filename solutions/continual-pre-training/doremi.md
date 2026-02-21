# DoReMi

来源: Continual Learning of Large Language Model

核心机制:
Automated Mixture Tuning。为了在 CPT 过渡中平衡不同领域数据的采样比例，DoReMi 使用一个极小参数量(Proxy)的模型来估算和优化数据混合权重，随后再用该权重组合训练大模型，大幅提升收敛速度和效率。
