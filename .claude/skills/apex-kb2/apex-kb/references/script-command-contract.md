# Apex KB Script Command Contract

## Shared policy

```yaml
script_policy:
  invocation_pattern: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand>
  retrieval_invocation_pattern: python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand>
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

## `apex_kb.py` commands

| Command | Writes possible | Owner | Role |
|---|---:|---|---|
| `scaffold` | yes | Python | create required KB skeleton and starter deterministic files |
| `source-intake` | yes | Python | copy/pointer source custody and source manifest entry |
| `hash` | no | Python | SHA-256 file or deterministic directory hash |
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
