# Apex KB Contract

## Data root

```yaml
data_root_contract:
  root_template: apex-meta/kb/<kb-slug>/
  one_kb_slug_per_invocation: true
  forbidden_root_files:
    CLAUDE.md: KB-local schema must be kb-schema.md
    SKILL.md: skill entrypoint belongs in .claude/skills/apex-kb/
```

## Canonical versus derived

```yaml
canonical:
  - raw/
  - kb-schema.md
  - manifests/source-manifest.json
  - manifests/source-payload-manifest.json
  - manifests/topic-registry.json
  - ingest-analysis/
  - wiki/
  - audit/
  - log/

derived_rebuildable:
  - manifests/phase0/
  - derived/search/
  - outputs/queries/
```

Canonical artifacts are durable source/custody/semantic records. Derived artifacts must be rebuildable from canonical artifacts and may never become the sole source of truth.

## Required KB root shape

```yaml
required_files:
  README.md: human orientation
  kb-schema.md: KB-local schema, authority, taxonomy, language, operator-review policy

required_directories:
  raw/articles/: source custody
  raw/papers/: source custody
  raw/notes/: source custody
  raw/refs/: source custody
  raw/other/: source custody
  ingest-analysis/: Phase 1 analysis before wiki generation
  wiki/index.md: query entrypoint and machine index
  wiki/concepts/: compiled concept pages
  wiki/entities/: compiled entity pages
  wiki/summaries/: compiled source/topic summaries
  manifests/source-manifest.json: source-reference custody manifest
  manifests/source-payload-manifest.json: deterministic raw-payload custody ledger
  manifests/phase0/: deterministic corpus intelligence
  derived/search/: local search indexes
  audit/resolved/: resolved review items
  outputs/queries/: saved query packets
  log/: operation notes
```

## Source custody

```yaml
source_storage_modes:
  pointer_only:
    use_when: source already exists durably in repository or stable local path
    required_fields: [source_path, source_storage_mode]
    optional_fields: [source_hash]
    when_unhashable: record no_hash_reason instead of source_hash
  copy_into_kb:
    use_when: source is uploaded, external, temporary, or not otherwise durable
    required_fields: [source_path, copied_to, source_hash, source_storage_mode]
  snapshot_copy:
    use_when: source may change and a frozen evidence copy is required
    required_fields: [source_path, snapshot_path, source_hash, source_storage_mode]

defaults:
  repo_internal_sources: pointer_only
  external_or_uploaded_sources: copy_into_kb
```

Rules:

- Preserve exact source filename and original path where possible.
- Hash sources before ingest, or record `no_hash_reason`.
- Never infer source contents from filename, title, memory, or prior summaries.
- Generated pages must record source pointers.
- `source-manifest.json` remains the source-reference ledger; do not replace it with the payload manifest.
- `source-payload-manifest.json` records per-file path, byte size, SHA-256, group, group aggregate SHA-256, root aggregate SHA-256, total file count, and total byte count.
- Payload groups are folder-derived by default: first-level folders under `raw/`; files directly under `raw/` use group `root`.
- Optional group maps must be explicit JSON. Do not infer deterministic groups from filenames or LLM semantic decisions.
- Do not add an external BagIt dependency; the Apex-native ledger uses Python stdlib hashing.
- Phase 0 resolves `pointer_only` sources that are safe local text files (kb-root-relative or repo-local, never a network URL) and includes them in corpus-navigation scanning; pointers that cannot be safely resolved are reported as unresolved rather than silently dropped.

## Page contract

Every generated wiki/query/audit page requires YAML frontmatter:

```yaml
required_frontmatter:
  - title
  - page_type
  - kb_slug
  - source_refs
  - created_at
  - updated_at
  - confidence
  - claim_label
  - status
page_type_allowed: [summary, concept, entity, index, query_output, audit_item]
confidence_allowed: [high, medium, low, mixed, unknown]
claim_label_allowed:
  - raw_source
  - source_backed_summary
  - behavioral_inference
  - working_hypothesis
  - operator_question
  - practitioner_question
status_allowed: [draft, active, needs_review, deprecated, superseded]
```

Do not place claim-label values in the confidence field.

## Page type definitions

These three page types are not interchangeable labels on the same generic template -- each answers a different kind of question, and the difference determines how much synthesis a page needs.

- **entity** -- one specific named thing: a tool, a standard, a runtime mechanism. Narrow, single identity. Its job is to say what this specific thing is *in this project's usage* and point precisely to where it is discussed, not to restate what the thing generically is (any LLM already knows what a subagent is; it does not already know how this repo constrains or uses one).
- **concept** -- one specific rule, pattern, or distinction. Narrow-to-medium scope, defines a single idea clearly, may be source-backed or a documented behavioral inference.
- **summary** -- a topic-level synthesis answering a specific important question, drawing on multiple concepts, entities, and sources. This is the page type for cross-cutting topics identified in the Step 0 / post-Phase-0 topic interview (see `SKILL.md`), and it carries a stronger bar than entity/concept: more ranked sources, more key claims, and explicit coverage of the topic's real sub-questions, not a single generic paragraph.

### Entity and concept content shape


Create an entity or concept page only when it has independent project-specific retrieval value: stable fields, rules, lifecycle, relationships, repeated direct queries, or a definition reused across pages. Populate its Adaptive Ranked Source Set only with sources actually reviewed and materially used. Phase 0 rank may be recorded, but rank never substitutes for reading or evidence use.

If no independent value exists, do not create a pointer-only page. Record `embed_in_summary` or `reject_no_independent_value` in the Phase 1 candidate disposition and topic ledger. Generic public knowledge and ranked pointer lists are never complete project knowledge.
## Topic registry


`manifests/topic-registry.json` is operator/LLM-authored input. Each topic retains `name`, `slug`, `page_type`, `keywords`, `source`, `status`, and `target_page`, and v2 compiled topics add:

```yaml
target_queries:
  - query_id: "<stable-topic-query-id>"
    question: "<future-AI question>"
    priority: "critical | routine | supporting"
    answer_requirements: []
    expected_page: "wiki/<type>/<slug>.md"
```

Keep ranking results out of the registry. Empty queries are valid for `source_only` and early `analysis_only`. Every compiled topic requires target queries. `status: complete` is valid only when all critical/routine queries have existing accepted routes and the topic semantic-acceptance artifact is `semantic_pass`.

Maintain the machine-readable topic ledger at `log/semantic-runs/<run-id>/topics/<topic-slug>.json`. It records query status, candidate/read/use distinctions, exact reviewed passages, authority and availability, analyses, pages/claims using each source, unanswered questions, next actions, page decisions, candidate dispositions, and blockers. See `references/semantic-value-contract.md` and `references/semantic-run-ledger.schema.json`.
## Page value contract for Phase 2 compiled pages


Phase 2 pages implement semantic contract v2. In addition to required frontmatter, summary, concept, and entity pages declare `semantic_contract_version: "2"`, `semantic_run_id`, and `target_query_ids`, and use these exact sections:

- **Target Questions Answered** — map each declared query ID to a direct answer and page section/route. A declared query cannot be satisfied only by an uncertainty notice.
- **Adaptive Ranked Source Set** — include only sources actually reviewed and materially used. Each entry records source ID/path, original Phase 0 rank when available, Phase 1 analysis reference, reviewed status, supported query IDs, claim IDs, rationale, and coverage. Unreviewed candidates remain only in the topic ledger.
- **Macro / Meso / Micro** — Macro supplies cross-source framing, Meso supplies rules/workflows/relationships, and Micro supplies exact fields, formulas, examples, edge cases, and source pointers needed by target queries.
- **Key Claims** — record specific claims with IDs, exact source pointers, confidence, and claim labels. Do not duplicate the same list in frontmatter and prose.
- **Routes Here** — route target and related questions to answer-bearing sections/pages.
- **Uncertainty / Raw Source Reopen Triggers** — preserve conflicts and gaps. Classify each trigger as `evidence_unavailable`, `evidence_conflict`, `future_change`, or `readable_unopened`, and record completion effect. `readable_unopened` blocks critical/routine completion.

Depth and source count are adaptive to answer requirements. Boundary-only orientation cannot satisfy a broad domain topic. `compiled_minimal` minimizes page topology, not content or evidence coverage. Pages may add useful sections but never use a numeric page-value score as semantic authority.
## Boundary contract

Apex KB may expose read-only evidence packets to Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU/status-merge, and personal orchestration. It must not mutate their files or redefine their ownership. Knowledge gaps may be offered as planning candidates, but task creation and status mutation belong outside Apex KB.
