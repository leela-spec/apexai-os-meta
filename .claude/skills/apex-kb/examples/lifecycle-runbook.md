# Apex KB Lifecycle Runbook

## A. Prepare

Create or validate one KB root under `apex-meta/kb/<kb-slug>/`. Verify there is no `CLAUDE.md` or `SKILL.md` inside the KB root. Select the run profile and output tier before intake.

```yaml
output_tiers:
  source_only: custody and manifests only
  analysis_only: semantic analysis, no wiki pages
  compiled_minimal: small high-value wiki with index and patch backlog
  compiled_full: full summaries/concepts/entities
  query_ready: compiled wiki plus postflight, retrieval, quality/query checks
```

## B. Ingest and compile

Add each source through `source-intake`, not by silently dropping files into wiki pages. Select storage mode, preserve original path, hash source, and update `manifests/source-manifest.json`.

Run `generate-source-payload-manifest` after source intake and before Phase 0. It writes `manifests/source-payload-manifest.json`, grouped by first-level `raw/` folder with direct `raw/` files in group `root`.

Run `phase0` after the payload manifest. Use the generated maps to choose high-signal files for LLM analysis. Phase 0 is not semantic ingest.

When the output tier includes wiki pages, Phase 1 analysis and Phase 2 wiki compile are one continuous semantic compile by default. Stop before wiki only for `analysis_only`, `phase1_only`, or `operator_explicit_stop_before_wiki`.

## C. Postflight

Use `postflight` as the preferred bounded completion interface:

```powershell
python apex-meta/scripts/apex_kb.py --kb-root $KB --json postflight
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json postflight
```

## D. Query or maintain

Read `wiki/index.md` first, retrieve only the smallest sufficient evidence set, synthesize from compiled pages, and save query outputs when reusable. Run `lint`, `audit`, `status`, and `health` for maintenance. List repair actions, but do not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU, or personal orchestration artifacts from Apex KB.
> EXAMPLE ONLY — This runbook illustrates a terminal-backed execution sequence. Follow the execution-surface router in `SKILL.md` first.
