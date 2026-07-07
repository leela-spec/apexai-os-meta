# Apex KB Script Command Contract

## Shared policy

```yaml
script_policy:
  invocation_pattern: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand> [flags] or [global flags] <subcommand>
  retrieval_invocation_pattern: python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand> [flags] or [global flags] <subcommand>
  kb_root_required: true
  no_silent_default_kb: true
  network_access: forbidden
  shell_out: forbidden
  required_dependency: Python standard library
  default_mode: dry_run
  writes_require: --allow-write
  outside_kb_root_writes: forbidden
  destructive_canonical_writes: forbidden
  optional_runtime_detection: [git, rg, sqlite3_fts5, markdown-it-py, python-frontmatter, PyYAML]
```

`--allow-write`, `--json`, `--dry-run`, and `--strict` may be placed before or after the subcommand. Prefer before-subcommand placement in scripts, but the lifecycle helper accepts either order for operator resilience:

```bash
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ --allow-write index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/<kb-slug>/ --allow-write build-index
```

Post-subcommand placement is accepted for these boolean global flags. Options with values, such as `--kb-root`, still keep their value next to the option.

## `apex_kb.py` commands

| Command | Writes possible | Owner | Role |
|---|---:|---|---|
| `scaffold` | yes | Python | create required KB skeleton and starter deterministic files |
| `source-intake` | yes | Python | copy/pointer source custody and source manifest entry |
| `hash` | no | Python | SHA-256 file or deterministic directory hash |
| `generate-source-payload-manifest` | yes | Python | write `manifests/source-payload-manifest.json` with per-file, group, and root SHA-256 payload custody |
| `preflight` | no | Python | validate source, manifest, duplicate hash, existing analysis, index freshness |
| `phase0` | yes | Python | deterministic corpus navigation artifacts under `manifests/phase0/` |
| `ingest-phase1` | optional shell only | Python+LLM | create deterministic Phase 1 shell; LLM fills semantics and halts |
| `ingest-phase2` | no in script | LLM | validate `approve ingest` gate; LLM drafts pages |
| `index` | yes | Python | rebuild auto-generated section of `wiki/index.md` |
| `query` | optional query packet | Python+LLM | retrieve/read evidence; LLM synthesizes answer |
| `lint` | no | Python | deterministic health checks |
| `audit` | no | Python | list/group audit items |
| `status` | no | Python | lifecycle status summary |
| `health` | no | Python | runtime/tool/FTS5 probe |

## Source payload manifest command

```text
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ generate-source-payload-manifest --allow-write --json
```

Options:

- `--raw-root <path>` defaults to `<kb-root>/raw`.
- `--output <path>` defaults to `<kb-root>/manifests/source-payload-manifest.json`.
- `--group-map <json>` optionally maps explicit raw-relative or KB-relative paths to group names.
- `--include-generated-at` adds a volatile timestamp and is off by default for deterministic diffs.

Grouping defaults to first-level folders under `raw/`; files directly under `raw/` use group `root`. The command uses Python standard library hashing only and must not add an external BagIt package.

Global flags:

```text
--kb-root <path>     required
--json              machine-readable output
--allow-write       permit deterministic writes inside kb_root
--dry-run           force preview mode even with --allow-write
--strict            lint warnings become failure
```

## `apex_kb_retrieval.py` commands

| Command | Writes possible | Role |
|---|---:|---|
| `health` | no | probe Python sqlite3, SQLite FTS5, optional modules |
| `build-index` | yes | build `derived/search/search-index.json`, `.ndjson`, metadata, and FTS5 DB when available |
| `stale` | no | compare wiki file hashes to `derived/search/index-meta.json` |
| `query` | optional | query FTS5/BM25 or JSON fallback; optionally save query packet |
| `export` | yes | export deterministic chunk index |
| `clear-index` | yes, derived only | remove derived search index files after exact confirmation |

Retrieval writes are restricted to `derived/search/` and `outputs/queries/`. `clear-index` may remove only derived index files and requires:

```text
--confirm-clear-index "clear derived search index"
```

## Exit policy

```yaml
exit_codes:
  0: success_or_nonblocking_warnings
  1: script_error
  2: blocked_or_strict_failure
```

### v3 closure additions

The v3 P0-P2 closure introduces new deterministic commands and fields:

- **quality / coverage**: deterministic quality/coverage report with `source_to_page_map`, `page_to_source_map`, `phase2_repair_candidates`, `shell_page_candidates`, and optional `--strict` enforcement. Accepts `--json` and may be invoked as `coverage` alias. (quality / coverage)
- **query-eval**: validate or initialize a query evaluation pack in `outputs/queries/evals/query-eval-pack.json`. Each eval entry defines `expected_routes`, `expected_minimal_pages`, and `raw_source_needed` instead of performing LLM grading. (query-eval)
- **graph**: generate deterministic process-flow graph artifacts under `manifests/phase0/`. Edges include markdown links, wikilinks, repository path references, and YAML/path/process edges. (graph, process-flow)
- **--output-json <path>**: global flag to write JSON output to a file instead of stdout. Useful for PowerShell-safe redirection. (--output-json)
- **pointer_only Phase 0**: when the manifest has sources marked as `pointer_only`, Phase 0 resolves repo-local pointers and reports `pointer_only_source_status`, `pointer_only_scanned_count`, `pointer_only_warning_count`, and `pointer_only_unresolved` in its result. (pointer_only)
- **Freshness split**: `status` now distinguishes `wiki_index_status` and `retrieval_index_status` separately from `source_payload_manifest_status`. (wiki_index_status, retrieval_index_status)

These additions are deterministic and do not introduce external dependencies or LLM calls.
