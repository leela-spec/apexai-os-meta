# Apex KB Acceptance Tests

Run from repository root. Replace `<kb-slug>` with a test slug such as `apex-kb-smoke`.

## Precheck

Pass criteria:

- Required skill package files exist.
- `apex-meta/scripts/apex_kb.py` exists.
- `apex-meta/scripts/apex_kb_retrieval.py` exists.
- `python --version` is 3.10+.

## Automated control-plane tests

Run the existing and new tests from repository root after applying the patch pack:

```powershell
python -m unittest discover -s apex-meta/scripts/tests -p "test_apex_kb_control*.py" -v
```

Pass criteria:

- canonical run intent/state schemas validate;
- legal and illegal transitions are reason-coded;
- exact next commands and semantic packet paths are stable on Windows paths;
- interrupted deterministic stages rerun idempotently;
- wrong-path output, unauthorized writes, schema failure, missing readback, missing acceptance, and input fingerprint drift block progression;
- a new executor resumes from files only;
- Git classification never mutates the repository;
- direct low-level mutation remains compatible for legacy KBs and is blocked for a controlled KB;
- the synthetic end-to-end fixture reaches `query_ready` only after independent acceptance and postflight.

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

Compiled wiki pages are the primary retrieval layer; local indexes remain derived and rebuildable from those pages.

### Meso

The retrieval flow indexes compiled Markdown, applies local lexical ranking, and returns cited page routes before raw-source reopening.

### Micro

The smoke source names SQLite FTS5 and BM25 in its only paragraph, which supports the local lexical retrieval claim.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "SQLite FTS5 and BM25 provide local lexical retrieval over compiled KB pages"
    source_pointer: "raw/notes/smoke-source.md#Smoke Source paragraph 1"
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


Create fixtures that separate structural validity from semantic value:

1. Valid v2 summary with locked queries, reviewed/materially-used sources, linked claims, accepted routes, and semantic pass.
2. Every heading/multiple claims/routes/ranked sources but no target queries.
3. Unopened source represented as evidence.
4. Readable canonical source deferred through a reopen trigger.
5. Missing concept/entity disposition.
6. Source reference without Phase 1 evidence/use.
7. Missing or incomplete semantic acceptance.
8. Topic complete despite failed acceptance.
9. Legacy v1 compatibility without query-ready promotion.
10. Query-eval v2 initialization from registry.
11. Deterministic structural pass that still refuses semantic/query-ready promotion.

Pass only when reason-coded wiring checks behave as specified. Placeholder-positive examples are forbidden; length, headings, and counts are never semantic authority.
# Apex KB Acceptance Tests

## Connector checklist and postflight regression fixtures


Verify the browser/Git-connector package and deterministic boundary:

- New scaffold writes all repository-local `semantic-contract/` assets.
- Existing KB without those assets reports `legacy_semantic_contract` or a migration warning rather than crashing.
- Connector prompts lock target questions, distinguish candidate/reviewed/used sources, require whole-file read/write/readback, persist ledgers, prohibit artifact-count completion and self-certification, and stop at `compiled_unvalidated`.
- `semantic-acceptance-status` validates artifacts and returns only `missing`, `partial`, `pass`, or `fail`; it never runs an LLM.
- Postflight includes semantic acceptance as a blocking stage, preserves delegate results, and uses exit codes 0/1/2 for success/planned, internal error, and blocking failure.

The runtime and fixture expectations must recognize these reason codes: `missing_target_queries`, `unknown_target_query_id`, `target_query_route_missing`, `ranked_source_not_in_source_refs`, `ranked_source_not_analyzed`, `ranked_source_without_claim_use`, `source_ref_without_phase1_evidence`, `candidate_promotion_disposition_missing`, `readable_unopened_source_blocks_completion`, `semantic_acceptance_missing`, `semantic_acceptance_incomplete`, `topic_status_inconsistent`, and `legacy_semantic_contract`.
## Generic term-frequency domain-agnosticism fixture

Build a small synthetic raw corpus with vocabulary from an unrelated domain (e.g. cooking: "sourdough", "starter", "fermentation", "pasta", "dough") -- no Apex/skill/Claude-orchestration terms anywhere in it. Run `phase0 --allow-write`.

Pass criteria:
- `manifests/phase0/term-frequency.json` is produced and its top-ranked terms are exclusively domain terms from the synthetic corpus;
- no term from any prior hardcoded keyword bucket (`apex kb`, `flowrecap`, `skill.md`, `orchestration_boundary`, etc.) appears anywhere in the output;
- this proves the mechanism carries no hardcoded domain knowledge and produces the same kind of result regardless of what the KB is actually about.

## Registry-driven topic ranking fixture

Add `manifests/topic-registry.json` to the same synthetic corpus with two topics, each with a distinct `keywords` (or `phrases`/`supporting_terms`) list drawn from the corpus vocabulary. Run `phase0 --allow-write` again.

Pass criteria:
- `topic_registry_entries` in the `phase0` result equals the number of registry entries;
- `manifests/phase0/topic-source-rankings.json` contains one entry per topic slug (`schema: apex.kb.topic-source-rankings.v2`), each with an exhaustive `candidates` list -- no top-N truncation, so a corpus with more than 30 signal-bearing files retains all of them;
- every candidate has a `tier` (`filename | h1 | heading | body_strong | body_weak`) and a `why` object naming the exact field(s)/line(s) that matched, plus a `pointers` array with at least one field/line/section-span entry;
- a filename/H1/heading match always outranks a body-only match, regardless of body hit count;
- a topic's `negative_terms` never suppress a filename, H1, heading, or phrase/alias match -- only a body-only/supporting-term match with no other qualifying signal;
- `held_in_custody` and `zero_signal_custody` together account for every scanned source not selected by `gap_cut` -- nothing is silently dropped;
- `manifests/phase0/work-packs/<topic-slug>.md` (+ `.json`) is produced for each registry topic and discloses `candidate_count`, `held_in_custody` count, and `zero_signal_custody` count in its footer;
- regenerating `wiki/index.md` produces a "Topic Guides" section listing both topics by name, status, and source, ahead of the alphabetical Concept/Entity/Summary buckets;
- a KB with no registry file produces neither a `topic-source-rankings.json` ranking entry, nor a work pack, nor a Topic Guides section -- absence is a valid, non-blocking state.

## Per-page compile-check-retry loop fixture

Draft one summary page known to be thin (e.g. a single generic claim, file-level-only pointer) against a real or synthetic KB. Run `quality --strict --json` immediately per the Procedure's per-page loop in `SKILL.md`.

Pass criteria:
- the thin page is named in `phase2_repair_candidates` with its actual reason codes on the first check;
- redrafting using those exact reason codes and rechecking clears the page within the 2-retry bound described in `SKILL.md`;
- a page deliberately left thin through both retries is not silently accepted -- it must be flagged as an audit item with residual reason codes and the batch capped at `partial`, never promoted to a passing state;
- `phase2_repair_candidates`/`shell_page_candidates` empty for a page is required for that page to count as done; heading presence alone (`missing_phase2_value_sections` empty) is confirmed insufficient by re-running this fixture with a page that has every heading but fails on `thin_macro_meso_micro` or `single_claim_summary` instead.
