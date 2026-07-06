# Apex KB Lifecycle Runbook

## 1. Scaffold

Create one KB root under `apex-meta/kb/<kb-slug>/`. Verify there is no `CLAUDE.md` or `SKILL.md` inside the KB root.

## 2. Source intake

Add each source through `source-intake`, not by silently dropping files into wiki pages. Select storage mode, preserve original path, hash source, and update the source manifest.

## 3. Phase 0 corpus intelligence

Run `phase0` after source intake. Use the generated maps to choose high-signal files for LLM analysis. Phase 0 is not semantic ingest.

## 4. Phase 1 analysis

Create the analysis file under `ingest-analysis/`. Fill it from source evidence only. Stop with `operator_review_needed`.

## 5. Operator gate

Proceed only after the operator says exactly `approve ingest`. In normal operation, do not accept same-prompt approval before Phase 1 exists.

## 6. Phase 2 wiki compilation

Generate or update summary, concept, and entity pages. Include source pointers, confidence, claim labels, contradictions, open questions, and review flags. Do not over-resolve contradictions.

## 7. Index and validation

Run deterministic index rebuild, lint, and retrieval index build. Treat stale indexes as derived-state problems, not source truth problems.

Write-enabled deterministic commands must pass `--allow-write` as a global flag before the subcommand:

```bash
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ --allow-write index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/<kb-slug>/ --allow-write build-index
```

## 8. Query

Read `wiki/index.md` first, retrieve only the smallest sufficient evidence set, synthesize from compiled pages, and save query outputs when reusable.

## 9. Maintenance

Run `lint`, `audit`, `status`, and `health`. List repair actions, but do not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU, or personal orchestration artifacts from Apex KB.
