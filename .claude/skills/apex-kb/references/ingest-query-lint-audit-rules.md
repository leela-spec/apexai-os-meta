# Apex KB Ingest, Query, Lint, and Audit Rules

## Shared rules

```yaml
source_grounding:
  raw_source_or_pointer_required: true
  generated_pages_require_source_pointers: true
  missing_source_rule: never infer source contents
  contradiction_rule: expose contradictions and uncertainties instead of silently resolving

phase_boundaries:
  phase0_must_not_create:
    - ingest-analysis files
    - wiki pages
    - semantic summaries
    - vector stores
  phase1_to_phase2_default:
    continuous_when_selected_output_tier_includes_wiki: true
  safe_modes_that_stop_before_wiki:
    - analysis_only
    - phase1_only
    - operator_explicit_stop_before_wiki
  legacy_explicit_gate_phrase: approve ingest
```

## Ingest rules

### Source intake

1. Select storage mode: `pointer_only`, `copy_into_kb`, or `snapshot_copy`.
2. Hash source before ingest, or record `no_hash_reason`.
3. Update `manifests/source-manifest.json` with deterministic source-reference custody fields.
4. Run `generate-source-payload-manifest` after source intake to write `manifests/source-payload-manifest.json`.
5. Stop if a duplicate source hash exists unless the operator explicitly requests a version or duplicate.

### Phase 0

Python may create only deterministic artifacts under `manifests/phase0/`. Phase 0 should run after the source payload manifest exists, or report that it is missing/stale:

- `corpus-profile.md`
- `heading-map.json`
- `markdown-link-map.json`
- `frontmatter-map.json`
- `keyword-hits.ndjson`
- `topic-file-map.json`
- `source-priority-candidates.md`
- `phase0-navigation-report.md`

`graph` extracts deterministic process-flow/navigation edges (markdown links, wikilinks, repository path references, YAML path references, process-sequence markers) and, with `--allow-write`, writes `manifests/phase0/process-flow-graph.json`. It is a Phase 0 navigation artifact, not a semantic inference step — it must never fail on an empty KB, and must report zero edges truthfully rather than guessing.

### Phase 1

LLM writes one analysis under `ingest-analysis/<source-slug>.analysis.md`. It must include source identity, source summary, extraction candidates, concept/entity candidates, key claims, uncertainty/raw source triggers, and proposed wiki changes. It must halt with `operator_review_needed`.

### Phase 2

When the selected output tier includes wiki output, Phase 2 follows Phase 1 in the same semantic compile by default. It halts only for `analysis_only`, `phase1_only`, or `operator_explicit_stop_before_wiki`. Compiled wiki pages must implement the Phase 2 page value contract, including the sections Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, and Uncertainty / Raw Source Reopen Triggers. Uncertainties and low-confidence claims must remain visible.

## Query rules

1. Read `wiki/index.md` first.
2. Check retrieval stale status when using `derived/search/`.
3. Retrieve the smallest sufficient evidence set.
4. Answer only from compiled wiki pages and their source pointers.
5. Cite page paths and source pointers.
6. Save a query packet under `outputs/queries/` when the answer is reusable or operator requests it.
7. Query mode is read-only with respect to Plan/Sync/Session/personal orchestration.

### Query-eval pack

`query-eval` validates or initializes `outputs/queries/evals/query-eval-pack.json`. Each entry defines `expected_routes`, `expected_minimal_pages`, and `raw_source_needed` for a query. The script validates pack schema only — it never grades answer quality and never runs an LLM eval.

## Quality / coverage rules

`quality` (alias `coverage`) reports `source_to_page_map`, `page_to_source_map`, pages missing `source_refs`, pages missing Phase 2 value sections, and structural repair/shell-page candidates. All checks are deterministic and structural — no LLM grading, no `page_value_score`. Findings are report-only by default; `--strict` turns repair candidates into a blocking failure.

## Lint rules

Deterministic lint checks:

- required root paths
- forbidden KB root files
- source-manifest JSON shape
- source payload manifest exists / stale status
- report-only Phase 2 value contract coverage: adaptive ranked source set, macro/meso/micro, key claims, routes, and raw-source reopen triggers
- required frontmatter fields
- confidence and claim_label enums
- dead wikilinks
- orphan pages
- stale `wiki/index.md`
- stale retrieval index

Semantic review flags:

- uncertain authority
- unresolved contradiction
- unsupported claim
- missing source pointer
- conflated confidence/claim label
- source conflict

## Audit rules

Audit items live under `audit/`; resolved items move to `audit/resolved/`. Audit mode lists and groups items, but does not silently accept, reject, or resolve them. Valid actions are `accept`, `partial`, `reject`, `defer`, and `needs_operator_review`.

## Phase 2 acceptance and repair loop

After wiki drafting, deterministic quality/lint runs first. Then a bounded independent semantic review checks target-query usefulness, claim specificity, source support, distinct Macro/Meso/Micro value, uncertainty preservation, routes, and raw-source reopen triggers. Verdicts are `semantic_pass`, `semantic_partial`, `semantic_fail`, or `insufficient_evidence`. Only reason-coded failed candidates are repaired; the failed gates are then rerun. Headings, source counts, length, or the drafting model's self-report cannot independently produce a pass.

