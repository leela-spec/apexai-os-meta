# Apex KB Script Command Contract

## Shared policy

```yaml
script_policy:
  invocation_pattern: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand> [flags] or [global flags] <subcommand>
  retrieval_invocation_pattern: python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand> [flags] or [global flags] <subcommand>
  kb_root_required: true
  no_silent_default_kb: true
  network_access: forbidden
  shell_out:
    default: forbidden
    read_only_exceptions:
      phase0_freshness: "git -C <repo> log --format=COMMIT\t%cI --name-only -- <kb-path>"
      control_classification: "git --no-optional-locks -C <repo> status --porcelain=v2 --branch --untracked-files=all"
    prohibited_git_actions: [fetch, pull, reset, stash, merge, rebase, cherry-pick, revert, commit, push]
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
| `control` | yes | Python | canonical run intent/state, legal transitions, exact next command, semantic packets, recovery, input invalidation, and read-only Git classification; delegates existing domain commands |
| `scaffold` | yes | Python | create required KB skeleton and starter deterministic files |
| `source-intake` | yes | Python | copy/pointer source custody and source manifest entry |
| `hash` | no | Python | SHA-256 file or deterministic directory hash |
| `generate-source-payload-manifest` | yes | Python | write `manifests/source-payload-manifest.json` with per-file, group, and root SHA-256 payload custody |
| `preflight` | no | Python | validate source, manifest, duplicate hash, existing analysis, index freshness |
| `topic-sanity-check` | no | Python | Step 0c validation input: check a newly locked topic's phrases/aliases against KB-scope evidence (path, sibling topics, a filename sample); its verdict feeds the Step 0d operator read-back and is not a standalone stop; never writes |
| `phase0` | yes | Python | deterministic corpus navigation artifacts under `manifests/phase0/` |
| `ingest-phase1` | optional shell only | Python+LLM | create/append the topic-scoped Phase 1 shell at `ingest-analysis/<topic-slug>.analysis.md` (one file per topic, never per source); LLM fills semantics and halts |
| `ingest-phase2` | no in script | LLM | validate `approve ingest` gate; LLM drafts pages |
| `index` | yes | Python | rebuild auto-generated section of `wiki/index.md` |
| `query` | optional query packet | Python+LLM | retrieve/read evidence; LLM synthesizes answer |
| `lint` | no | Python | deterministic health checks |
| `audit` | no | Python | list/group audit items |
| `status` | no | Python | lifecycle status summary |
| `health` | no | Python | runtime/tool/FTS5 probe |
| `postflight` | yes, derived only | Python | bounded seven-stage deterministic completion aggregate |

## `control` command

`control` is a nested subcommand of the existing lifecycle CLI; it is not a second operator CLI and does not copy domain logic.

```text
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ control <action> [flags]
```

| Action | Writes | Role |
|---|---:|---|
| `init` | yes with `--allow-write` | validate compact run configuration; create `manifests/run-intent.md` and `manifests/run-state.json`; render the first exact stage result |
| `confirm` | yes with `--allow-write` | record the operator's verbatim Step 0 confirmation |
| `status` | no | validate canonical intent/state, fingerprints, and next legal stage |
| `next` | no | return the exact next PowerShell-safe command or one-line semantic packet trigger |
| `run` | yes with `--allow-write` | execute exactly one legal deterministic stage in-process or render exactly one semantic packet |
| `reconcile` | yes only when accepting a detected input change | resume from repository files, validate packet output, classify drift, and invalidate only affected downstream stages |
| `git-state` | no | classify branch, HEAD, upstream, ahead/behind, dirty/untracked/conflicted counts, and in-progress operations without mutation |
| `doctor` | no | validate the apex-kb skill package's own internal consistency (schemas parse, template schema references exist, `SKILL.md`/`kb-contract.md` canonical paths agree, control test files are discoverable, `apex_kb_control.py` compiles, every parser action has a dispatch branch) - independent of any specific KB |

The compact result for every action conforms to `apex.kb.stage-result.v1`. A controlled KB has `manifests/run-state.json`; direct low-level mutation commands are blocked for that KB so state cannot drift. Legacy KBs without run state keep their existing low-level command behavior.

Git policy is read-only classification. Dirty or untracked files remain visible and may be safe for bounded KB writes; unmerged paths, an in-progress merge/rebase/cherry-pick/revert/bisect, Git status failure, or a configured target-commit mismatch blocks the controlled stage. Apex KB never resolves, stashes, resets, or synchronizes operator work.

Recovery policy is file-based. `control reconcile` checks canonical input fingerprints and run-specific packet fingerprints. A changed source, registry, work pack, analysis, page, schema, or template invalidates the earliest affected stage and its downstream completion records. The operator must explicitly pass `--accept-input-change` before new fingerprints replace recorded ones.

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

## Postflight evidence contract

`quality --strict --json` must emit page-level measurements and reason-coded repair candidates. A successful postflight records exact commands, command status, output paths, retrieval freshness, and remaining candidates. File read-back or required-heading presence is not execution proof. Connector-only runs may report `compiled_unvalidated`; they may not report `query_ready`.

## `postflight` command

`postflight` is the preferred bounded terminal completion interface. It delegates existing implementations in this fixed order:

1. wiki index
2. retrieval build
3. lint strict
4. quality strict
5. audit
6. status
7. retrieval stale

The command resolves one KB root and propagates it to every delegate. Every delegate result is preserved under `steps[].result`.

```yaml
postflight_contract:
  schema: apex.kb.postflight.v1
  default_mode:
    status: planned
    evidence_complete: false
    writes: none
  allow_write_mode:
    pass_requires:
      - every blocking stage passes
      - retrieval stale result proves fresh
  blocking_stages: [wiki_index, retrieval_build, lint_strict, quality_strict, status, retrieval_stale]
  nonblocking_stages: [audit]
  dependency_rule: skip retrieval stale after wiki-index or retrieval-build failure
  exit_codes:
    planned_or_pass: 0
    internal_error: 1
    fail: 2
```

`--allow-write --dry-run` remains planned and performs no writes. Lint and quality failures do not prevent safe diagnostics such as audit and status from running. Internal delegate exceptions are captured as `status: internal_error`, preserved in the relevant step result, and cause exit code `1`.

The command does not add retries, scheduling, persisted orchestration state, dynamic graphs, rollback, semantic review, query evaluation, ranking changes, commit, or push.

The connector checklist is preventive authoring guidance only. Terminal `quality --strict` remains the authoritative deterministic quality gate.

