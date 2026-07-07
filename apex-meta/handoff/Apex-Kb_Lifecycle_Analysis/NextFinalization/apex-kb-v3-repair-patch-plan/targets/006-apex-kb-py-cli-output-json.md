# Target Plan — 006 cli-output-json

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "codex-old-agent-kb-execution-process-audit.md"
    - "AgentModePatchGuide_v4.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "normalize_global_flag_placement exists and moves selected post-subcommand global flags before the subcommand."
    - "maybe_write_output_json exists and writes under kb_root."
    - "Parser has --output-json as global flag."
```

## 3. Failure class

```yaml
failure_class:
  status: KEEP_REAL
  reason: "The feature is real enough to preserve, but it needs regression tests because it came from the suspect workaround commit."
  user_value_problem: "PowerShell-safe JSON output and flexible flag placement prevent repeat execution friction."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve --output-json support"
    - "preserve path safety under kb_root"
    - "preserve global flag normalization where functional"
    - "ensure post-subcommand placement works for documented global flags"
    - "produce valid UTF-8 JSON"
  must_not:
    - "weaken path safety"
    - "allow output-json outside kb_root"
    - "rewrite the entire parser"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Do not redesign the parser. Validate and minimally harden the existing shim.

Implementation intent:

- Keep `normalize_global_flag_placement`.
    
- Confirm command set includes every lifecycle helper subcommand.
    
- Confirm global bool flags include `--json`, `--dry-run`, `--allow-write`, `--strict`.
    
- Confirm value flags include `--output-json`.
    
- Confirm parser-level `--output-json` remains a global option.
    
- Confirm `maybe_write_output_json` handles relative paths under KB root and rejects outside paths through `ensure_inside`.
    
- If any repaired commands add subcommand-specific flags, ensure normalization does not steal legitimate command-local flags.
    
- Add or update acceptance tests in target 010 rather than adding marker-only logic.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "normalize_global_flag_placement includes all current commands."
    - "maybe_write_output_json calls ensure_inside."
  behavioral:
    - "status --json works with --json before subcommand."
    - "status --json works with --json after subcommand."
    - "status --output-json log/status.json writes valid JSON."
    - "outside-kb-root --output-json path is rejected."
  regression:
    - "source-payload-manifest still supports --allow-write before and after subcommand."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "006-apex-kb-py-cli-output-json.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/006-apex-kb-py-cli-output-json.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 6
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> status --output-json log/status.json"
    - "python - <<'PY' parse the JSON file and assert command == status PY"
```
