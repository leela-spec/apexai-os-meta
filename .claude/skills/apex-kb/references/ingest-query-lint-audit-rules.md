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

1. Select storage mode: `pointer_only`, `copy_into_kb`, or `snapshot_copy`, or use the control plane's exact `--source-root` command for a confirmed bounded root.
2. Hash source before ingest, or record `no_hash_reason`. A recursive source root inventories every file, including unsupported/non-text files; later extraction status may be blocked but custody may not silently omit it.
3. Update `manifests/source-manifest.json` with deterministic source-reference custody fields. Re-running one source-root intake replaces the entries owned by that root so deleted files do not survive as stale custody records.
4. Run `generate-source-payload-manifest` after source intake to write `manifests/source-payload-manifest.json`.
5. Stop with a reason code if a source ID or duplicate source hash already exists unless the operator explicitly requests a version or duplicate. Never return `ok` without recording the source.

### Phase 0

Python may create only deterministic artifacts under `manifests/phase0/`. Phase 0 should run after the source payload manifest exists, or report that it is missing/stale:

- `corpus-profile.md`
- `heading-map.json`
- `markdown-link-map.json`
- `frontmatter-map.json`
- `source-facts.json`
- `term-frequency.json`
- `topic-source-rankings.json`
- `work-packs/<topic-slug>.json`
- `work-packs/<topic-slug>.md`
- `source-priority-candidates.md`
- `phase0-navigation-report.md`

`topic-source-rankings.json` is the exhaustive machine candidate/custody set. A topic work pack is the bounded semantic projection. Neither is a second registry, an authority decision, or semantic acceptance. The control plane validates these exact paths and fingerprints them before rendering semantic packets.

`graph` extracts deterministic process-flow/navigation edges (markdown links, wikilinks, repository path references, YAML path references, process-sequence markers) and, with `--allow-write`, writes `manifests/phase0/process-flow-graph.json`. It is a Phase 0 navigation artifact, not a semantic inference step — it must never fail on an empty KB, and must report zero edges truthfully rather than guessing.

### Phase 1


LLM writes one topic-scoped analysis under `ingest-analysis/<topic-slug>.analysis.md`, containing every accepted source record for that topic. The exact input set, ledger path, output path, write allowlist, readback, and completion response come from the run-specific Phase 1 packet. In addition to source identity, summary, extraction candidates, concepts/entities, claims, uncertainty, and proposed changes, the analysis records source read status/passages, authority, target-query outcomes, additional evidence required, and topic completion effect.

Every concept/entity candidate receives exactly one disposition: `promote`, `embed_in_summary`, `defer_blocked`, or `reject_no_independent_value`, with rationale, affected query IDs, and destination when applicable. Phase 1 alone is `analysis_complete_unvalidated`. For a compiled tier, successful deterministic reconciliation advances directly to the Phase 2 packet; there is no second free-form command decision and no mandatory legacy approval phrase.
### Phase 2


When the selected output tier includes wiki output, Phase 2 follows Phase 1 unless a safe stop mode applies. The Phase 2 packet derives the exact expected page paths from the topic registry and validated Phase 1 page decisions; pages outside its allowlist are wrong-path output. Source selection continues until locked critical/routine questions are covered or evidence is genuinely unavailable. Rankings nominate candidates only. A readable known source that can answer an unresolved priority query blocks completion.

Pages implement semantic contract v2, answer declared target queries directly, use only reviewed/materially-used evidence, preserve contradictions, and expose classified reopen triggers. Structural/schema/path reconciliation proves only declared interface correctness. A separate clean-context page-only and claim-entailment packet must produce a valid `semantic-acceptance.schema.json` artifact before `compiled_unvalidated`. Connector constraints may produce `partial`; they never reduce semantic requirements.
## Query rules

1. Read `wiki/index.md` first.
2. Check retrieval stale status when using `derived/search/`.
3. Retrieve the smallest sufficient evidence set.
4. Answer only from compiled wiki pages and their source pointers.
5. Cite page paths and source pointers.
6. Save a query packet under `outputs/queries/` when the answer is reusable or operator requests it.
7. Query mode is read-only with respect to Plan/Sync/Session/personal orchestration.

### Query-eval pack


`query-eval` reads v1 packs for compatibility and initializes `apex.query_eval_pack.v2` from registry target queries when present. Each v2 entry records query ID, priority, answer requirements, expected routes, and expected raw-source requirement. The command validates structure and route references only; it never runs an LLM or grades answer meaning. Legacy v1 packs receive a migration report.
## Quality / coverage rules


`quality` (alias `coverage`) reports structural page metrics and v2 contract wiring. Strict v2 findings include missing/unknown target-query IDs, absent routes, ranked/reference/analysis/use inconsistencies, missing candidate dispositions, readable unopened blockers, missing/incomplete semantic acceptance, inconsistent topic status, and legacy semantic contracts.

These checks are deterministic and reason-coded. They validate declared interfaces and evidence wiring; they never infer semantic meaning. A structural pass cannot create `semantic_pass`.
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


After deterministic wiring checks, a clean-context evaluator answers every target query using compiled pages first and independently checks material claims against resolved source passages. Store one artifact per topic under `audit/semantic-acceptance/<run-id>/<topic-slug>.json`.

Query results are `answerable`, `partial`, `not_answerable`, or `blocked`. Claim results are `supported`, `partially_supported`, `contradicted`, or `unresolvable`. Final verdicts are `semantic_pass`, `semantic_partial`, `semantic_fail`, or `insufficient_evidence`.

Every critical/routine query must be answerable and every sampled material claim supported for `semantic_pass`. No numeric average, headings, counts, length, rankings, or drafter self-report can establish acceptance. Repair only reason-coded failures and reevaluate in a fresh context.
