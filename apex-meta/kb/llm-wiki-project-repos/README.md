# LLM-Wiki Project Repositories

This Apex KB root is a source-preserving knowledge base for `llm-wiki-project-repos`.

Canonical paths:

- `raw/` preserves source files or durable pointers.
- `ingest-analysis/` stores Phase 1 LLM analysis before operator approval.
- `wiki/` stores approved compiled KB pages.
- `manifests/source-manifest.json` records source custody and hashes.
- `manifests/phase0/` stores deterministic navigation artifacts.
- `derived/search/` stores rebuildable retrieval indexes.
- `audit/` stores open and resolved review items.
- `outputs/queries/` stores reusable cited query packets.

Apex KB must not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap,
APSU, or personal orchestration state. Other systems may consume KB outputs as
read-only evidence packets.
