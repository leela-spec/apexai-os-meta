# Apex KB

Apex KB is a local, manifest-driven Python application that maps an entire configured corpus, delegates bounded meaning-based work to AI workers, independently evaluates compiled knowledge, builds a rebuildable SQLite FTS5 index, and performs selective incremental updates.

The CLI—not a Skill, chat, or database—owns configuration, paths, state, legal transitions, task construction, validation, recovery, and completion.

## Install

From this directory:

```bash
python -m pip install .
```

For development:

```bash
python -m pip install -e .
pytest
```

The stable console entry point is:

```text
apex-kb
```

## Normal operator flow

```bash
apex-kb start
apex-kb continue --run-root "/absolute/path/to/kb"
apex-kb status --run-root "/absolute/path/to/kb"
```

Additional read and maintenance surfaces:

```bash
apex-kb query --run-root "/absolute/path/to/kb" --query "What owns Skill Tree navigation?"
apex-kb update --run-root "/absolute/path/to/kb"
```

`start` always renders the canonical guided Start template first. It can load a draft configuration, prompt only for missing fields, validate independent source/destination roots, show a deterministic readback, and create the frozen run only after confirmation:

```bash
apex-kb start --config run-config.yaml
apex-kb start --config run-config.yaml --non-interactive --yes
```

A minimal draft may use the original PR #10 field names; it is normalized to the v2 contract:

```yaml
source:
  repository: leela-spec/leela
  root: C:/GitDev/leela
  folders:
    - LeelaAppDevelopment

destination:
  repository: leela-spec/apexai-os-meta
  root: C:/GitDev/apexai-os-meta
  folder: apex-meta/kb/leela-app

exclusions:
  - path: LeelaAppDevelopment/LeelaApp-Index-KB-Wiki
    reason: generated_kb_output

topics:
  - name: Skill Tree
    phrases: [skill tree, skilltree]
    ambiguous_or_negative_terms: [tree]
    questions:
      - What is the current Skill Tree and what does it own?

run_options:
  source_handling: pointer_only
  semantic_depth: standard
  output: query_ready
  non_text: inventory_and_report
  git_metadata: true
  graph_depth: links
  ai_help_after_preflight: false
  max_semantic_repairs: 2
```

The normalized v2 form separates primary phrases, aliases, supporting terms, ambiguous terms, negative terms, question priority, answer requirements, and expected dossier/atlas routes. Advanced runs may also declare `lifecycle_hint_rules` and scored `authority_hint_rules`; every matched rule is preserved as inspectable evidence, and no path name silently becomes semantic authority. The generated `run-config.yaml` is the human-readable input; `run-manifest.json` freezes its canonical SHA-256 hash and `corpus_scope`; `run-state.json` is the single atomic lifecycle state.

## What `continue` does

Each invocation performs exactly one legal action:

1. deterministic whole-corpus intelligence;
2. create one bounded Phase 1 source-review packet;
3. import and validate its result;
4. repeat for all affected topics;
5. create/import one Phase 2 dossier-and-atlas packet per topic;
6. create/import one independent acceptance packet per topic;
7. run deterministic postflight over source freshness, semantic completion, and acceptance;
8. build and validate retrieval for `query_ready` runs only after postflight passes;
9. write `completion.json` and derive the truthful terminal state.

When a semantic packet is active, `status` reports its exact packet directory and incoming result path. The worker reads `TASK.md`, `task.json`, `source-allowlist.json`, and `output.schema.json`, then writes only the declared JSON result. It never edits run state, manifests, stage results, wiki pages, retrieval files, or source files. The application validates identity, schema, candidate completeness, target-question completeness, page routes, source-atlas completeness, and fresh-context acceptance before advancing.

A semantically invalid result produces a bounded repair instruction next to the incoming result and leaves lifecycle state unchanged.

## Deterministic corpus intelligence

Every discovered file is inventoried or explicitly excluded. The current run publishes:

```text
manifests/source-inventory.ndjson
manifests/source-manifest.json
manifests/source-payload-manifest.json
manifests/phase0/corpus-profile.md
manifests/phase0/structure-map.ndjson
manifests/phase0/heading-map.json
manifests/phase0/frontmatter-map.json
manifests/phase0/markdown-link-map.json
manifests/phase0/link-graph.json
manifests/phase0/term-postings.ndjson
manifests/phase0/duplicate-map.json
manifests/phase0/topic-maps/<topic>.json
manifests/phase0/topic-maps/<topic>.md
manifests/phase0/phase0-navigation-report.md
manifests/phase0/phase0-stats.json
```

The JSON topic map is the exhaustive authoritative candidate set. It is never truncated to top N. Each candidate preserves field-separated reasons and exact pointers for path, filename, frontmatter title, generic title, H1, headings, body, links, repository references, and configured-identifier co-occurrence. It also records source format and size, Git/date/version facts, matched lifecycle/authority rules, an inspectable score vector, and deterministic duplicate representatives. Ambiguous-only matches remain visible in a suppressed ledger rather than becoming false semantic workload. The Markdown projection is intentionally bounded only as a navigation view.

Built-in extraction covers text/code/Markdown, JSON, CSV/TSV, HTML/XML, DOCX, PPTX, XLSX, and PDF. The three non-text policies are distinct: `inventory_and_report` inventories Office/PDF/image/unknown files without content extraction; `extract_when_supported` extracts installed deterministic formats; `block_on_unsupported` performs supported extraction and then fails closed if any included file remains unreadable, metadata-only, or unsupported. Images remain visible as metadata-only candidates requiring a visual semantic route. Unsupported or unreadable formats are never silently omitted.

Source custody modes are:

- `pointer_only`: preserve absolute path, repository path, hash, and repository snapshot without duplication;
- `copy_into_kb`: copy every included payload under `raw/sources/<repository-relative-path>`;
- `snapshot_copy`: create a run-bound snapshot under `raw/snapshots/<run-id>/<repository-relative-path>`.

Both copy modes verify content hashes, reuse byte-identical existing payloads, and fail with `custody_collision` rather than overwriting a different file.

The source repository is read-only in all modes.

## Durable semantic outputs

Phase 1 writes reusable, content-hash-addressed source capsules and one complete topic analysis:

```text
ingest-analysis/sources/<content-hash>.analysis.json
ingest-analysis/sources/<content-hash>.analysis.md
ingest-analysis/topics/<topic>.analysis.json
ingest-analysis/topics/<topic>.analysis.md
```

Every candidate receives one disposition and read status. The current contract distinguishes `core_current`, `supporting_current`, `implementation`, `prototype`, `historical`, `contextual`, `incidental`, `duplicate`, `superseded`, `irrelevant_after_review`, and `blocked_unreadable` (with legacy aliases accepted only for migration). Unchanged capsules are reused across topics and update runs.

Phase 2 is structured JSON rendered deterministically into:

```text
wiki/concepts/<topic>.md
wiki/summaries/<topic>-source-atlas.md
```

The dossier must answer all locked target questions and create distinct Macro, Meso, and Micro value. The source atlas preserves every Phase 0 candidate exactly once with its snapshot, value, authority/freshness judgment, duplicate/supersession relationship, disposition, read status, and pointers.

A fresh evaluator writes:

```text
audit/semantic-acceptance/<run-id>/<topic>.json
```

`semantic_pass` is accepted only when every critical/routine question is answerable from compiled pages without raw-source reopening and all sampled material claims are supported. The evaluator context ID must differ from the Phase 2 drafting context ID. Accepted page frontmatter is then promoted from `accepted_pending_evaluation` to `accepted` by the application.

## Retrieval and query

For `query_ready`, accepted pages are chunked by heading and indexed into a derived SQLite FTS5 database:

```text
derived/search/search.sqlite
derived/search/index-manifest.json
wiki/index.md
```

The index stores page hashes, source IDs, exact heading/line spans, run/config identity, and database hash. It is never canonical knowledge and can be deleted/rebuilt byte-identically from accepted Markdown. Query checks freshness and integrity before use, ranks with FTS5 BM25, and writes both JSON and Markdown evidence packets under `outputs/queries/`, including the index identity, page hash, source-atlas route, and raw-source reopen guidance.

## Incremental update

`apex-kb update`:

1. requires a stable completed or explicitly blocked run;
2. archives prior control files, manifests, and wiki under `log/control-archive/<prior-run-id>/`;
3. creates a new controlled update run;
4. rebuilds deterministic corpus intelligence;
5. writes `maintenance/impact-report.json` with added, changed, deleted, moved-identical, newly unreadable, and unchanged paths;
6. invalidates only topics whose candidate source bytes, candidate set, topic contract, or semantic-depth contract changed;
7. reuses unchanged content-hash capsules and accepted topic outputs where safe;
8. runs postflight before rebuilding retrieval and restoring `query_ready`;
9. writes a durable completion certificate only after every configured gate passes.

Changing from `analysis_only` to a compiled output reuses valid Phase 1 work but correctly schedules Phase 2 and acceptance. Changing topic questions/vocabulary or semantic depth invalidates the relevant semantic work even when source bytes are unchanged.

## Completion evidence

A successful run writes `completion.json`, an archived copy under `audit/completion/<run-id>.json`, and a validated completion stage result. The certificate records run/config identity, output tier, accepted topics, postflight and retrieval artifacts, canonical paths, blockers, and the source-mutation assertion. `query_ready` is never inferred merely from page counts or index existence.

## Migration and recovery

`status` is read-only. It reports legacy runs as `migration_required`. The next `continue` or `update` creates a backup under `log/migrations/<timestamp>/`, normalizes the legacy configuration into v2, writes a migration result, and begins a safe v2 run rather than guessing completion from weak legacy artifacts.

State writes use atomic replacement. The application reconstructs every next action from `run-config.yaml`, `run-manifest.json`, `run-state.json`, and referenced artifacts. Chat memory is never lifecycle authority.

## Runtime probe

```bash
apex-kb doctor
apex-kb doctor --run-root "/absolute/path/to/kb"
```

This reports Python, SQLite/FTS5, PDF extraction, template packaging, run status, and retrieval health without mutating the run.
