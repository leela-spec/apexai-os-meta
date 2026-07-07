# Target Plan — 007 retrieval-cli-output-json

## 1. Target file

```text
apex-meta/scripts/apex_kb_retrieval.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md"
    - "codex-old-agent-kb-execution-process-audit.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb_retrieval.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "normalize_global_flag_placement exists in retrieval script."
    - "maybe_write_output_json exists and writes JSON under kb_root."
    - "Script policy restricts writes to derived/search and outputs/queries."
```

## 3. Failure class

```yaml
failure_class:
  status: KEEP_REAL
  reason: "Retrieval CLI output-json and flag normalization are real enough to preserve and regression-test."
  user_value_problem: "Retrieval postflight should produce parseable UTF-8 JSON without PowerShell redirection problems."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve --output-json support"
    - "preserve path safety under kb_root"
    - "preserve retrieval command flag normalization"
    - "write valid JSON for health, stale, query, export, build-index, and clear-index where applicable"
  must_not:
    - "patch retrieval ranking semantics in this repair wave"
    - "weaken derived-path restrictions"
    - "allow output outside kb_root"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

This target is primarily regression validation. Patch only if live validation shows defects.

Implementation intent:

- Keep `normalize_global_flag_placement` in retrieval script.
    
- Confirm command set includes `health`, `build-index`, `stale`, `query`, `export`, `clear-index`.
    
- Confirm value flag normalization handles `--output-json <path>`.
    
- Confirm `maybe_write_output_json` resolves relative paths under KB root and enforces `ensure_inside`.
    
- Do not change ranking, indexing, chunking, FTS5, query-packet semantics, or clear-index confirmation behavior unless needed to keep output-json safe.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "normalize_global_flag_placement includes all retrieval commands."
    - "maybe_write_output_json calls ensure_inside."
  behavioral:
    - "health --output-json log/retrieval-health.json writes valid JSON."
    - "stale --output-json log/retrieval-stale.json writes valid JSON."
    - "post-subcommand --json works for health and stale."
  regression:
    - "build-index still writes only under derived/search."
    - "query --save still writes only under outputs/queries."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "007-apex-kb-retrieval-cli-output-json.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/007-apex-kb-retrieval-cli-output-json.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb_retrieval.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 7
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root <fixture-kb> health --output-json log/retrieval-health.json"
    - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root <fixture-kb> stale --json"
```
