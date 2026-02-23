# MemoRAG — Qian et al. 2025

- **Paper**: Qian et al. (2025), WWW
- **Source**: arXiv 2512.13564v2 (Memory in the Age of AI Agents)
- **Category**: Latent Memory — Generate + Query Rewriting
- **Task**: QA, Summary

## Core Mechanism

MemoRAG uses an LLM to generate compact latent state memory to capture the global semantic structure and achieves query rewriting by generating hypothetical documents.

- Leverages an LLM to generate compact latent state memory, capturing the global semantic structure of input documents.
- Generates hypothetical documents for query rewriting, transforming ambiguous queries into more precise retrieval requests.
- Integrates global memory into the hypothetical document generation process, allowing retrieval to better match the global context.
- Combines the compression capabilities of latent memory with retrieval enhancement strategies of query rewriting.
