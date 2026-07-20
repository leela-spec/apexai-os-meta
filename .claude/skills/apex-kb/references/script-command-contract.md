# Apex KB Script Command Contract

## Shared policy

```yaml
script_policy:
  invocation_pattern: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand> [flags] or [global flags] <subcommand>
  start_invocation_pattern: python apex-meta/scripts/apex_kb.py start --config <start-config.yaml> --repo-root <repository-root> [--allow-write] [--dry-run] [--strict] [--json]
  retrieval_invocation_pattern: python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/<kb-slug>/ <subcommand> [flags] or [global flags] <subcommand>
  kb_root_required_except_start: true
  no_silent_default_kb: true
  network_access: forbidden
  shell_out:
    default: forbidden
    read_only_exceptions:
      phase0_freshness: "git -C <repo> log --format=COMMIT\t%cI --name-only -- <kb-path>"
      start_topology: "git rev-parse; git worktree list --porcelain; git remote get-url origin; git status; git rev-parse HEAD"
      control_classification: "git --no-optional-locks -C <repo> status --porcelain=v2 --branch --untracked-files=all"
    prohibited_git_actions: [fetch, pull, reset, stash, merge, rebase, cherry-pick, revert, commit, push]
  required_dependency: Python standard library
  default_mode: dry_run
  writes_require: --allow-write
  outside_kb_root_writes: forbidden
  destructive_canonical_writes: forbidden
  optional_runtime_detection: [git, rg, sqlite3_fts5, markdown-it-py, python-frontmatter, PyYAML]
```

`--allow-write`, `--json`, `--dry-run`, and `--strict` may be placed before or after the subcommand. Prefer before-subcommand placement in scripts, but the lifecycle helper accepts either order for operator resilience.

## `apex_kb.py` commands

| Command | Writes possible | Owner | Role |
|---|---:|---|---|
| `start` | preview no; confirmed Setup yes | Python | canonical new-KB Setup frontend; validates one operator configuration, resolves repository/source/destination truth read-only, previews derived values, and delegates initialization to control |
| `control` | yes | Python | canonical run intent/state, legal transitions, exact next command, semantic packets, recovery, input invalidation, and read-only Git classification; delegates existing domain commands |
| `scaffold` | yes | Python | create required KB skeleton and starter deterministic files |
| `source-intake` | yes | Python | copy/pointer source custody and source manifest entry |
| `hash` | no | Python | SHA-256 file or deterministic directory hash |
| `generate-source-payload-manifest` | yes | Python | write `manifests/source-payload-manifest.json` with per-file, group, and root SHA-256 payload custody |
| `preflight` | no | Python | validate source, manifest, duplicate hash, existing analysis, index freshness |
| `topic-sanity-check` | no | Python | validation input for operator readback; checks topic phrases/aliases against KB-scope evidence and never writes |
| `phase0` | yes | Python | deterministic corpus navigation artifacts under `manifests/phase0/` |
| `ingest-phase1` | optional shell only | Python+LLM | create/append one topic-scoped Phase 1 shell; LLM fills semantics and halts |
| `ingest-phase2` | no in script | LLM | validate legacy gate; LLM drafts pages |
| `index` | yes | Python | rebuild auto-generated section of `wiki/index.md` |
| `query` | optional query packet | Python+LLM | retrieve/read evidence; LLM synthesizes answer |
| `lint` | no | Python | deterministic health checks |
| `audit` | no | Python | list/group audit items |
| `status` | no | Python | lifecycle status summary |
| `health` | no | Python | runtime/tool/FTS5 probe |
| `postflight` | yes, derived only | Python | bounded deterministic completion aggregate |

## `start` command

```text
python apex-meta/scripts/apex_kb.py start --config <start-config.yaml> --repo-root <repository-root> --json --dry-run
```

`start --help` must expose `--config`, `--repo-root`, `--allow-write`, `--dry-run`, `--strict`, and `--json`. Preview is mandatory and creates no KB destination or KB artifact. Start inspects the current primary `main` worktree and HEAD without fetching, pulling, merging, switching branches, creating worktrees, or otherwise moving repository state. After the operator accepts the submitted and derived readback, rerun the same configuration with explicit `--allow-write` and without `--dry-run`.

Confirmed Start may write only Setup artifacts and initialize canonical control state. A Setup-only request stops there, before scaffold, source intake, deterministic corpus intelligence, semantic work, acceptance, retrieval, or postflight. Existing controlled KBs do not rerun Start.

## `control` command

`control` is a nested subcommand of the existing lifecycle CLI; it is not a second operator CLI and does not copy domain logic.

```text
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<kb-slug>/ control <action> [flags]
```

| Action | Writes | Role |
|---|---:|---|
| `init` | yes with `--allow-write` | validate compact run configuration; create `manifests/run-intent.md` and `manifests/run-state.json`; render the first exact stage result |
| `confirm` | yes with `--allow-write` | record the operator's verbatim Setup confirmation |
| `status` | no | validate canonical intent/state, fingerprints, and next legal stage |
| `next` | no | return the exact next PowerShell-safe command or one-line semantic packet trigger |
| `run` | yes with `--allow-write` | execute exactly one legal deterministic stage in-process or render exactly one semantic packet |
| `reconcile` | yes only when accepting a detected input change | resume from repository files, validate packet output, classify drift, and invalidate only affected downstream stages |
| `git-state` | no | classify branch, HEAD, upstream, ahead/behind, dirty/untracked/conflicted counts, and in-progress operations without mutation |
| `doctor` | no | validate the skill package's own internal consistency |

The compact result for every action conforms to `apex.kb.stage-result.v1`. A controlled KB has `manifests/run-state.json`; direct low-level mutation commands are blocked for that KB so state cannot drift. Legacy KBs without run state keep their existing low-level command behavior.

Git policy is read-only classification. Dirty or untracked files remain visible and may be safe for bounded KB writes; unmerged paths, an in-progress operation, Git status failure, or a configured target-commit mismatch blocks the controlled stage. Apex KB never resolves, stashes, resets, synchronizes, or moves operator work.

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
--kb-root <path>     required except for start
--json               machine-readable output
--allow-write        permit deterministic writes inside kb_root
--dry-run            force preview mode even with --allow-write
--strict             strict validation
```

## `apex_kb_retrieval.py` commands

| Command | Writes possible | Role |
|---|---:|---|
| `health` | no | probe Python sqlite3, SQLite FTS5, optional modules |
| `build-index` | yes | build derived search artifacts and FTS5 DB when available |
| `stale` | no | compare wiki file hashes to index metadata |
| `query` | optional | query FTS5/BM25 or JSON fallback; optionally save query packet |
| `export` | yes | export deterministic chunk index |
| `clear-index` | yes, derived only | remove derived search index files after exact confirmation |

Retrieval writes are restricted to `derived/search/` and `outputs/queries/`.

## Exit policy

```yaml
exit_codes:
  0: success_or_nonblocking_warnings
  1: script_error
  2: blocked_or_strict_failure
```

## Postflight evidence contract

`quality --strict --json` must emit page-level measurements and reason-coded repair candidates. A successful postflight records exact commands, command status, output paths, retrieval freshness, and remaining candidates. File read-back or required-heading presence is not execution proof. Connector-only runs may report `compiled_unvalidated`; they may not report `query_ready`.

## `postflight` command

`postflight` is the preferred bounded terminal completion interface. It delegates existing implementations in fixed order and preserves every delegate result. `--allow-write --dry-run` remains planned and performs no writes. The command does not add retries, scheduling, persisted orchestration state, dynamic graphs, rollback, semantic review, query evaluation, ranking changes, commit, or push.
