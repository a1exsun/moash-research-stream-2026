# RazorAttention — Tang et al. 2025

- **Paper**: Tang et al. (2025), ICLR
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Transform — Compensated Window
- **Task**: Language Modeling

## Core Mechanism

RazorAttention calculates the effective attention span for each head, retaining only a finite local window while using compensation tokens to preserve information from discarded entries.

- Calculates the effective attention span for each attention head, quantifying the actual context range required by each head.
- Retains only a finite local window for each head, discarding remote KV pairs that fall outside this range.
- Introduces compensation tokens: key information from discarded remote KV entries is compressed into these compensation tokens.
- Compensation tokens are injected into the attention calculation to compensate for information loss caused by window truncation.
- Implements per-head adaptive KV cache management, where different heads receive different cache strategies based on their attention spans.
