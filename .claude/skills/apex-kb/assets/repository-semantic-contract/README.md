# Repository-Local Apex KB Semantic Contract

These files define the LLM-owned Phase 1 and Phase 2 lifecycle. They are intentionally repository-local; account-level Skills are optional and never required. Phase 0 and deterministic artifacts are prepared separately.

Semantic executors may create or replace complete owned files only under `ingest-analysis/`, `wiki/summaries/`, `wiki/concepts/`, `wiki/entities/`, `audit/semantic-acceptance/`, and `log/semantic-runs/`. Deterministic validation happens later. Semantic completion is capped at `compiled_unvalidated`.

Read `semantic-execution-contract.md`, both templates, `source-authority-and-contradictions.md`, and `browser-chat-git-connector-instructions.md` before Phase 1.
