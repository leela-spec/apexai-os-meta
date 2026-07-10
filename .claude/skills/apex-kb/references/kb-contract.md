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

An entity or concept page's Adaptive Ranked Source Set (below) should be populated primarily from `manifests/phase0/topic-source-rankings.json` when that topic has a registry entry -- a deterministic, hit-count-ranked list of raw files, computed by script, never invented by the LLM. The LLM's own prose contribution should be a short delta only: what does *this project specifically* decide, constrain, or use differently from generic public knowledge of the term. If there is no real project-specific delta, the page is honestly just the ranked pointer list with a one-line note that no project-specific constraint was found -- that is a valid, complete page, not a failure. A page that restates generic public knowledge of the term instead of this delta is exactly the failure mode this contract exists to prevent.

## Topic registry

`manifests/topic-registry.json` holds one entry per topic the KB should have a summary page for: `name`, `slug`, `page_type` (almost always `summary`), `keywords` (the input to `rank_topic_sources()` -- never a ranking result itself), `source` (`operator` from the Step 0 interview, or `llm_proposed` from the post-Phase-0 review of `term-frequency.json`), `status` (`not_started`/`draft`/`complete`), and `target_page`. It is operator/LLM-authored input, not a deterministic output -- never write ranking results into it, and never compute its `keywords` field from anything other than the interview or the LLM's own topic proposal. Registry completeness is reported by `status`/`quality` but is not currently a `quality --strict` gate.

## Page value contract for Phase 2 compiled pages

Phase 2 wiki compile introduces an adaptive page‑level value contract for summary, concept, and entity pages. In addition to the required frontmatter above, compiled pages **must** include the following narrative sections using the exact headings listed:

- **Adaptive Ranked Source Set** – a list of sources ranked by relevance and diversity to the page's scope. The number of sources should scale with KB size, topic breadth, and source diversity. Each entry must include a rationale for its rank and a brief description of coverage. Do **not** impose a fixed 2–5 source cap. For a page tied to a topic registry entry, populate this from `topic-source-rankings.json`'s ranked list rather than from LLM judgment (see Page type definitions above). A source cluster map may optionally be provided in future iterations but is not required.
- **Macro / Meso / Micro** – a three‑layer synthesis. Macro describes high‑level themes across all sources; Meso captures mid‑level patterns; Micro provides specific details anchored by source pointers.
- **Key Claims** – specific claims supported by source pointers. Each claim must include an id, description, pointer, confidence, and claim label. This section remains required.
- **Routes Here** – navigational cues that help users and LLMs route queries to this page. Include route‑by‑question examples and cross‑links to related pages. This integrated routing list replaces prior “Relationships” or “Known Relationships” sections.
- **Uncertainty / Raw Source Reopen Triggers** – consolidate contradictions, open questions, and any situation that requires revisiting raw sources. Each item must describe the uncertainty, provide a source pointer, and suggest how it should be handled (e.g., audit item, planning task candidate, revisit source, leave as gap, ask operator).

Compiled pages may include additional sections if useful, but must not include any page‑level score metric or impose a rigid 20‑field schema. The goal is to adapt the depth and breadth of each section to the KB context while preserving source grounding and operator oversight.

## Boundary contract

Apex KB may expose read-only evidence packets to Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU/status-merge, and personal orchestration. It must not mutate their files or redefine their ownership. Knowledge gaps may be offered as planning candidates, but task creation and status mutation belong outside Apex KB.
