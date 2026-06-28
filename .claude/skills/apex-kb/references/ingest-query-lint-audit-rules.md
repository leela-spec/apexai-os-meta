# Apex KB Ingest, Query, Lint, and Audit Rules

## Shared rules

```yaml
source_grounding:
  raw_source_or_pointer_required: true
  generated_pages_require_source_pointers: true
  missing_source_rule: never infer source contents
  contradiction_rule: expose contradictions instead of silently resolving

phase_boundaries:
  phase0_must_not_create:
    - ingest-analysis files
    - wiki pages
    - semantic summaries
    - vector stores
  phase1_must_halt_before:
    - wiki page generation
    - manifest semantic updates
  phase2_requires:
    exact_phrase: approve ingest
```

## Ingest rules

### Source intake

1. Select storage mode: `pointer_only`, `copy_into_kb`, or `snapshot_copy`.
2. Hash source before ingest, or record `no_hash_reason`.
3. Update `manifests/source-manifest.json` with deterministic custody fields.
4. Stop if a duplicate source hash exists unless the operator explicitly requests a version or duplicate.

### Phase 0

Python may create only deterministic artifacts under `manifests/phase0/`:

- `corpus-profile.md`
- `heading-map.json`
- `markdown-link-map.json`
- `frontmatter-map.json`
- `keyword-hits.ndjson`
- `topic-file-map.json`
- `source-priority-candidates.md`
- `phase0-navigation-report.md`

### Phase 1

LLM writes one analysis under `ingest-analysis/<source-slug>.analysis.md`. It must include source identity, source summary, extraction candidates, concept/entity candidates, key claims, contradictions, proposed wiki changes, and open questions. It must halt with `operator_review_needed`.

### Phase 2

Requires exact phrase `approve ingest`. Allowed outputs are compiled wiki pages, manifest semantic updates, deterministic index updates, audit items, and logs. Contradictions and low-confidence claims must remain visible.

## Query rules

1. Read `wiki/index.md` first.
2. Check retrieval stale status when using `derived/search/`.
3. Retrieve the smallest sufficient evidence set.
4. Answer only from compiled wiki pages and their source pointers.
5. Cite page paths and source pointers.
6. Save a query packet under `outputs/queries/` when the answer is reusable or operator requests it.
7. Query mode is read-only with respect to Plan/Sync/Session/personal orchestration.

## Lint rules

Deterministic lint checks:

- required root paths
- forbidden KB root files
- source-manifest JSON shape
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
