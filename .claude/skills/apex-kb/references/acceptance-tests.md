# Apex KB Acceptance Tests

Run from repository root. Replace `<kb-slug>` with a test slug such as `apex-kb-smoke`.

## Precheck

Pass criteria:

- Required skill package files exist.
- `apex-meta/scripts/apex_kb.py` exists.
- `apex-meta/scripts/apex_kb_retrieval.py` exists.
- `python --version` is 3.10+.

## Command smoke tests

```powershell
$KB="apex-meta/kb/apex-kb-smoke"
python apex-meta/scripts/apex_kb.py --kb-root $KB --json scaffold
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json scaffold --title "Apex KB Smoke"
python apex-meta/scripts/apex_kb.py --kb-root $KB --json health
python apex-meta/scripts/apex_kb.py --kb-root $KB --json status
python apex-meta/scripts/apex_kb.py --kb-root $KB --json lint
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json health
```

Pass criteria:

- First scaffold previews writes and does not create files.
- Second scaffold creates required files/directories.
- Health reports Python and SQLite FTS5 probe.
- Status reports KB root exists.
- Lint does not report missing required scaffold paths.

## Source intake and Phase 0

```powershell
New-Item -ItemType Directory -Force -Path tmp | Out-Null
@"
# Smoke Source

This source mentions Apex KB, source manifest, Phase 1, approve ingest, SQLite FTS5, and BM25.
"@ | Set-Content -Encoding UTF8 tmp/smoke-source.md
python apex-meta/scripts/apex_kb.py --kb-root $KB --json hash --path tmp/smoke-source.md
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json source-intake --source-path tmp/smoke-source.md --source-type note --storage-mode copy_into_kb --source-id smoke-source
python apex-meta/scripts/apex_kb.py --kb-root $KB generate-source-payload-manifest --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root $KB phase0 --allow-write --json
```

Pass criteria:

- Hash returns SHA-256.
- Source file is copied to `raw/notes/smoke-source.md`.
- Source manifest includes `smoke-source`.
- `manifests/source-payload-manifest.json` exists, includes per-file SHA-256 records, includes group `notes`, and has a root aggregate SHA-256.
- `manifests/phase0/` contains eight deterministic artifacts.
- No `ingest-analysis/` or semantic wiki pages are created by Phase 0.

## Ingest gate

```powershell
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json ingest-phase1 --source-path tmp/smoke-source.md --source-slug smoke-source
python apex-meta/scripts/apex_kb.py --kb-root $KB --json ingest-phase2 --analysis smoke-source.analysis.md --approval-phrase "not approved"
python apex-meta/scripts/apex_kb.py --kb-root $KB --json ingest-phase2 --analysis smoke-source.analysis.md --approval-phrase "approve ingest"
```

Pass criteria:

- Phase 1 creates an analysis shell and halts.
- Incorrect approval phrase is blocked.
- Exact `approve ingest` plus existing analysis validates the gate.

## Wiki/index/retrieval

Create one compiled page:

```powershell
New-Item -ItemType Directory -Force -Path "$KB/wiki/concepts" | Out-Null
@"
---
title: "Retrieval"
page_type: concept
kb_slug: "apex-kb-smoke"
source_refs:
  - source_id: "smoke-source"
created_at: "2026-06-27T00:00:00Z"
updated_at: "2026-06-27T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---
# Retrieval

SQLite FTS5 and BM25 provide local lexical retrieval over compiled KB pages. Search indexes are derived artifacts.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "smoke-source"
    rationale: "only source in this smoke test"
    coverage: "describes retrieval features"
```

## Macro / Meso / Micro

### Macro

<High-level retrieval summary.>

### Meso

<Mid-level retrieval patterns.>

### Micro

<Specific details anchored to source lines.>

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "SQLite FTS5 and BM25 provide local lexical retrieval over compiled KB pages"
    source_pointer: "<pointer>"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "How does retrieval work?"
    leads_to: "apex-kb-smoke/wiki/concepts/retrieval.md"
    rationale: "describes retrieval"
```

## Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers: []
```
"@ | Set-Content -Encoding UTF8 "$KB/wiki/concepts/retrieval.md"
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json stale
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json query --query "sqlite bm25" --limit 3 --save
```

Pass criteria:

- `wiki/index.md` auto-generated section lists the compiled page.
- `derived/search/index-meta.json` exists.
- SQLite index exists if FTS5 probe passes; JSON fallback exists regardless.
- Query returns the retrieval page.
- Saved query packet appears under `outputs/queries/`.

## v3 repair fixtures (pointer_only, quality/coverage, query-eval, graph, retrieval freshness)

```powershell
$KB2="apex-meta/kb/apex-kb-v3-repair-smoke"
New-Item -ItemType Directory -Force -Path "$KB2/manifests","$KB2/external-pointers","$KB2/wiki" | Out-Null
@"
{
  "schema_version": "1.0",
  "kb_slug": "apex-kb-v3-repair-smoke",
  "sources": [
    {"source_id": "ptr-good", "source_storage_mode": "pointer_only", "source_path": "external-pointers/pointer-source.md"},
    {"source_id": "ptr-missing", "source_storage_mode": "pointer_only", "source_path": "external-pointers/does-not-exist.md"}
  ]
}
"@ | Set-Content -Encoding UTF8 "$KB2/manifests/source-manifest.json"
"# Pointer Source`n`nResolved only through pointer_only Phase 0 scanning." | Set-Content -Encoding UTF8 "$KB2/external-pointers/pointer-source.md"
@"
---
title: "Shell Page"
page_type: concept
kb_slug: "apex-kb-v3-repair-smoke"
source_refs: []
created_at: "2026-07-09T00:00:00Z"
updated_at: "2026-07-09T00:00:00Z"
confidence: "unknown"
claim_label: "working_hypothesis"
status: "draft"
---
# Shell Page

Nothing much here.
"@ | Set-Content -Encoding UTF8 "$KB2/wiki/shell-page.md"
python apex-meta/scripts/apex_kb.py --kb-root $KB2 --allow-write --json phase0
python apex-meta/scripts/apex_kb.py --kb-root $KB2 --json quality
python apex-meta/scripts/apex_kb.py --kb-root $KB2 query-eval --init --json
python apex-meta/scripts/apex_kb.py --kb-root $KB2 --allow-write query-eval --init --json
python apex-meta/scripts/apex_kb.py --kb-root $KB2 --allow-write --json graph
python apex-meta/scripts/apex_kb.py --kb-root $KB2 --json status
```

Pass criteria:

- `phase0` reports `pointer_only_scanned_count: 1` and `manifests/phase0/heading-map.json` includes `external-pointers/pointer-source.md`.
- `phase0` reports `ptr-missing` inside `pointer_only_unresolved` with a non-empty `reason`, and `pointer_only_warning_count` is not `0`.
- `quality` reports `wiki/shell-page.md` under both `pages_without_source_refs` and `shell_page_candidates`, derived from structural checks only (no LLM grading, no `page_value_score`).
- `query-eval --init` without `--allow-write` returns `status: "planned"` and creates no file; with `--allow-write` it creates a valid `outputs/queries/evals/query-eval-pack.json`, and immediately re-running `query-eval` reports `issue_count: 0`.
- `graph` reports `edge_count` greater than 0 whenever an edge-bearing file exists in the KB, and truthfully reports `edge_count: 0` (never fails) for an empty KB; `--allow-write` writes `manifests/phase0/process-flow-graph.json`.
- `status` reports `retrieval_index_status` as one of `missing`/`unknown`/`stale`/`fresh` based on an actual hash comparison against `derived/search/index-meta.json`, never merely on file presence.

## Maintenance

```powershell
python apex-meta/scripts/apex_kb.py --kb-root $KB --json lint --strict
python apex-meta/scripts/apex_kb.py --kb-root $KB --json audit
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json stale
```

## Source payload manifest deterministic fixture

```bash
KB="apex-meta/kb/apex-kb-payload-smoke"
mkdir -p "$KB/raw/group-a"
printf 'root
' > "$KB/raw/root-file.md"
printf 'group
' > "$KB/raw/group-a/file-a.md"
python apex-meta/scripts/apex_kb.py --kb-root "$KB" generate-source-payload-manifest --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" status --json
```

Pass criteria:

- Manifest exists at `manifests/source-payload-manifest.json`.
- `files` includes `raw/root-file.md` and `raw/group-a/file-a.md`.
- Groups include `root` and `group-a`.
- Re-running the command without `--include-generated-at` produces deterministic aggregate hashes.
- `status` reports source payload manifest status as `fresh`.

Pass criteria:

- Lint passes or reports only intentional test issues.
- Audit lists open audit items without mutating them.
- Stale status is `fresh` after rebuild.

## Phase 2 thin-but-structurally-complete regression fixtures

Create four pages: (1) all headings with one generic claim and one file-level pointer, (2) placeholder text under every heading, (3) a valid narrow entity with claim-specific pointers, and (4) a strong multi-source concept. Run `quality --strict --json`.

Pass criteria:
- fixtures 1 and 2 appear in `phase2_repair_candidates` with reason codes;
- fixture 3 (narrow named entity, one claim, one source, section-level pointer) does not fail solely for being concise;
- fixture 4 (multi-source concept, two claims each with a section-level pointer) passes with no repair reasons;
- a claim with no pointer at all produces `claim_pointer_coverage_below_100_percent`; a claim with only a file-level pointer is reported via `pointer_specificity` but does not block on its own;
- `--strict` exits nonzero when repair candidates remain;
- after repairing candidates, rerun quality, lint, retrieval stale, and the bounded semantic acceptance check.

