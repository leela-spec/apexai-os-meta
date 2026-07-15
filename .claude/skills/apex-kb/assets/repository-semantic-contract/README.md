# Repository-Local Apex KB Semantic Contract

These files define the LLM-owned Phase 1 and Phase 2 lifecycle. They are intentionally repository-local; account-level Skills are optional and never required. Phase 0 and deterministic artifacts are prepared separately.

Semantic executors may create or replace complete owned files only under `ingest-analysis/`, `wiki/summaries/`, `wiki/concepts/`, `wiki/entities/`, `audit/semantic-acceptance/`, `log/semantic-runs/`, and `manifests/run-intent.md` (the operator-confirmed intake record). Deterministic validation happens later. Semantic completion is capped at `compiled_unvalidated`.

Before selecting any source, complete the intake and intent lock in `semantic-execution-contract.md`: capture and read back the operator's intent, KB identity, source locus, and success definition, and record the operator's explicit confirmation in `manifests/run-intent.md`. No source selection or Phase 1/Phase 2 writing proceeds until that confirmation exists.

Read `semantic-execution-contract.md`, both templates, `source-authority-and-contradictions.md`, and `browser-chat-git-connector-instructions.md` before Phase 1.
