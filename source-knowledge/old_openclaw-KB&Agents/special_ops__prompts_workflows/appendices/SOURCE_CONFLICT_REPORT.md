# SOURCE_CONFLICT_REPORT

## Purpose

Bounded conflict report for the `special_ops__prompts_workflows` KB-base build.

## Conflict summary

|conflict_id|topic|sources|conflict|resolution|status|
|---|---|---|---|---|---|
|PW-CONFLICT-001|Patch-before-rewrite vs full-final-body/live-edit|`PROMPT_DESIGN_80_20_BEST_PRACTICE.md`; existing scaffold entries; Codex execution sources|General workflow doctrine says patch before rewrite; existing accepted Prompts Workflows entries say full final bodies or live-edit instructions can be safer for Markdown rewrites when unified diffs are fragile.|Resolve by context: patch-before-rewrite remains the default for bounded local defects; full final body or live-edit instruction is allowed when exact byte anchors, CRLF, connector output, or long Markdown diff transport make unified diffs riskier.|resolved|
|PW-CONFLICT-002|Stop-after-step vs practical promptflow execution|`WORKFLOW_80_20_ESSENCE.md`; `PROMPTFLOW_KB_BASE_BUILD.md`|General workflow doctrine says one deliverable then stop; this promptflow requires a bounded multi-file KB base build.|Resolve by treating the whole promptflow as the bounded execution unit, while preserving ordered gates: appendices before scaffolds, `ESSENCE.md` last, fetch-back verification after writes.|resolved|
|PW-CONFLICT-003|Template usefulness vs governance authority|Failure ledger; prompt/workflow template sources|Templates can become hidden runtime law if treated as authority rather than reusable pattern.|Resolve by explicit boundary: templates are reusable construction aids; governance/config/QA/promotion authority remains outside this KB lane.|resolved|

## Applied resolution rules

- **Rule:** Default to patch-first for small bounded defects.
- **Rule:** Use full final body or live-edit instruction when patch transport is less reliable than controlled replacement.
- **Rule:** Treat promptflow multi-file execution as bounded only when file set, order, and verification gates are closed.
- **Rule:** Keep templates as patterns, not authority surfaces.

## Impact on scaffold files

- `BEST_PRACTICES.md` should include the contextual patch-vs-rewrite resolution.
- `MISTAKES.md` should flag both destructive rewrite and fragile diff transport as distinct failure modes.
- `TEMPLATES.md` should include both patch-mode and live-edit/full-body-safe templates.
- `ESSENCE.md` should keep the higher-level boundary: reusable prompt/workflow construction, not governance ownership.
