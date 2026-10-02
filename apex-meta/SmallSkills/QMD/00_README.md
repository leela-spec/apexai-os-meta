# QMD (Query Markdown) SmallSkill

Practical operational guide and retrieval doctrine for **QMD** (@tobilu/qmd) — local on-device hybrid search engine combining BM25 keyword search, vector embeddings (`embeddinggemma-300M`), Reciprocal Rank Fusion (RRF), and LLM cross-encoder reranking (`qwen2.5`).

## Contents

| File | What it is |
|---|---|
| `QMD-Knowledge-Base-And-Failure-Modes.md` | Complete operational guide: CLI commands, context trees, hybrid retrieval pipeline, and the RAG Metadata Over-Engineering failure mode. |

## Core Operating Rule

> **Never impose relational database schemas onto hybrid semantic search.**
> QMD thrives on natural language prose, clear Markdown heading hierarchies (`#`, `##`, `###`), and atomic notes. Keep YAML frontmatter minimal (3–4 fields max: `title`, `summary`, `tags`, `source`). Let BM25 and vector embeddings do the retrieval work rather than rigid categorical variables.

## Cross-References
- AI Failure Case Study: `apex-meta/AI-Snippets/AIFailure/AI-Failure-RAG-Metadata-Overengineering.md`
- Anti-Drift Doctrine: `apex-meta/AI-Snippets/Snippets.md` (Product before infrastructure, minimalism rule)
