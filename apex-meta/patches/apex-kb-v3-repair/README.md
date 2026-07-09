# apex-kb-v3-repair patch pack

Built from live `main` (`7318ca7a`) in an isolated `git worktree` (never touched the primary
checkout). Each patch is a `git diff` of a real edit — none were hand-authored — and every
patch was validated with `git apply --check` on a clean tree before and after being combined.

## Contents

| Patch | Target file | What it fixes |
|---|---|---|
| `001-apex-kb-py-v3-repair.patch` | `apex-meta/scripts/apex_kb.py` | Replaces 4 stub functions and repairs 1 partial one (see below). Cumulative single patch — the file's `pointer_only`, `quality`, `query-eval`, `graph`, and `status` regions all live in one diff rather than 5 separately-generated ones, avoiding fragile cross-patch context-line collisions. |
| `002-acceptance-tests.patch` | `.claude/skills/apex-kb/references/acceptance-tests.md` | Adds a real fixture-based acceptance section covering pointer_only/quality/query-eval/graph/retrieval-freshness — none of these had test coverage before. |
| `003-kb-contract-doc-alignment.patch` | `.claude/skills/apex-kb/references/kb-contract.md` | Fixes a real inaccuracy: `pointer_only` sources were documented as requiring `source_hash`, but they structurally can't have one (they record `no_hash_reason` instead). Adds a line on how Phase 0 handles pointer resolution. |
| `004-phase2-value-contract-alignment.patch` | `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md` | Adds the query-eval and quality/coverage operational rules the file was missing entirely, and documents `graph` as a deterministic Phase 0 navigation artifact. |

`script-command-contract.md` and `package-manifest.md` were diffed against the repaired
behavior and needed **no changes** — the former already described the intended v3 behavior
(it was aspirational, not overclaiming, once the stub was actually implemented); the latter's
inventory/paths were already correct. No patch was generated for either, and no patch was
generated for `apex_kb_retrieval.py` — its CLI surfaces (`health`, `stale`, `build-index`,
`--output-json`, flag placement) were regression-tested against a fixture KB and no defect
was found.

## What `001` actually repairs

- **`pointer_only_phase0`**: was checking the wrong manifest field name (`storage_mode`
  instead of the `source_storage_mode` field actually written by `source-intake`), never fed
  resolved pointer files into Phase 0 scanning, and hardcoded `pointer_only_warning_count: 0`
  / `pointer_only_unresolved: []`. Now resolves both field-name conventions, merges resolved
  pointer files into scanning before `parse_markdown_structure` runs, and reports real
  resolved/unresolved status per source (with a closed, testable reason vocabulary:
  `missing_pointer`, `unsupported_scheme`, `out_of_bounds`, `not_found`, `not_a_file`,
  `unsupported_extension`, `internal_error`). Path resolution is bounded to `kb_root` and an
  ancestor-inferred repo root (`.git`/`apex-meta` marker, never shells to `git`); URLs and
  out-of-bounds paths are rejected as `unresolved`, never fetched or followed, and a single
  bad manifest entry can never crash the command.
- **`quality_report`**: was returning every map/candidate list empty. Now parses real
  `source_refs` from wiki frontmatter (list-of-string, list-of-object, or scalar shapes),
  builds real `source_to_page_map`/`page_to_source_map`, and adds two fields the stub never
  had (`unmanifested_source_refs`, `manifest_sources_without_pages`). `shell_page_candidates`
  uses a disclosed fixed threshold (40 words / 200 chars after stripping fenced code, plus a
  missing structural anchor) — deterministic, not scored.
- **`cmd_query_eval`**: was returning only a path and two hardcoded empty arrays. Now reads
  and schema-validates an existing pack, supports `--init` (plan-only without
  `--allow-write`, real write with it, starting from an empty `queries: []`), and aggregates
  `expected_routes`/`expected_minimal_pages`/`raw_source_needed` as a sorted union for the
  top-level report.
- **`process_graph_extract`/`cmd_graph`**: was returning three hardcoded empty arrays and
  writing nothing. Now extracts 5 deterministic edge families (`markdown_link`, `wikilink`,
  `repo_path_reference`, `yaml_path_reference`, `process_sequence`) from KB-local text files
  only, skips fenced code blocks when scanning for arrows (otherwise Python `-> ReturnType`
  annotations would flood the graph with false edges), and writes
  `manifests/phase0/process-flow-graph.json` (+ summary) under `--allow-write`.
- **`retrieval_index_status`**: was a binary `present`/`missing` check that reported a stale
  index as if it were fresh. Now reimplements the same hash-comparison `apex_kb_retrieval.py`
  uses (without importing it) against `derived/search/index-meta.json`, returning
  `missing`/`unknown`/`stale`/`fresh`.

## Validation performed

- `git apply --check` — each patch individually, on a clean checkout: **pass** (all 4).
- `git apply --check` — all 4 patches stacked, on a clean checkout: **pass**.
- `python -m py_compile apex-meta/scripts/apex_kb.py` after applying: **pass** (both from the
  live edit and from a checkout-then-apply-from-patch cycle).
- Fixture-KB behavioral tests, actually executed (not just asserted) against the patched
  script:
  - `phase0 --allow-write --json` on a KB with one resolvable pointer-only source (living
    outside the normally-scanned `raw/`/`sources/` roots) and one deliberately unresolvable
    one → `pointer_only_scanned_count: 1`, pointer file present in `heading-map.json`,
    unresolved entry reported with `reason: "not_found"`, `pointer_only_warning_count: 1`.
  - Edge cases: `https://...` pointer → `unsupported_scheme`; `../../../etc/hosts`-style
    escape attempt → `out_of_bounds`; legacy `storage_mode`/`pointer` field names → still
    resolved. No network access attempted in any case.
  - `quality --json` on a KB with one well-formed concept page and one shell page → correct
    `source_to_page_map`/`page_to_source_map`, shell page correctly flagged in both
    `pages_without_source_refs` and `shell_page_candidates`; `--strict` → exit code `2`;
    default mode → exit code `0` (never hard-fails by default).
  - `query-eval --init` without `--allow-write` → `status: "planned"`, no file written;
    with `--allow-write` → valid pack written; re-running on the valid pack →
    `issue_count: 0`; running on a deliberately invalid pack → 3 correct schema issues.
  - `graph --json` on a fixture with a markdown link, wikilink, repo-path reference,
    YAML-path reference, and `A -> B`/`Stage N` sequence → `edge_count: 9` across all 5
    edge types; `--allow-write` → `process-flow-graph.json` written; on an empty KB →
    `edge_count: 0` truthfully, no crash.
  - `status --json` → `retrieval_index_status` correctly reports `missing` (no index),
    `unknown` (unrecognized/legacy metadata shape), `fresh` (hash-matching metadata), and
    `stale` (after modifying a wiki page post-index).
  - `apex_kb_retrieval.py` regression: `health`/`stale` with flags before and after the
    subcommand, `--output-json` writes, `build-index` scoped to `derived/search/` only —
    all as expected, no defects found.
- Final `git status --porcelain` on the scratch worktree after reverting all 4 patches:
  clean except for this untracked `apex-meta/patches/apex-kb-v3-repair/` directory.

## Applying this pack

This pack is **not applied to `main`**. Applying it is a separate, explicit step:

```bash
git checkout main
git pull --ff-only origin main
git apply --check apex-meta/patches/apex-kb-v3-repair/*.patch
git apply apex-meta/patches/apex-kb-v3-repair/*.patch
python -m py_compile apex-meta/scripts/apex_kb.py
python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> --help
```

Then re-run the behavioral checks above (or the new fixture section in
`acceptance-tests.md`) against the applied tree before committing.
