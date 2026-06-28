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
  manifests/source-manifest.json: source custody manifest
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
    required_fields: [source_path, source_hash, source_storage_mode]
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

## Boundary contract

Apex KB may expose read-only evidence packets to Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU/status-merge, and personal orchestration. It must not mutate their files or redefine their ownership. Knowledge gaps may be offered as planning candidates, but task creation and status mutation belong outside Apex KB.
