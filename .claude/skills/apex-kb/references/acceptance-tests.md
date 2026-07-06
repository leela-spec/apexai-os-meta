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
