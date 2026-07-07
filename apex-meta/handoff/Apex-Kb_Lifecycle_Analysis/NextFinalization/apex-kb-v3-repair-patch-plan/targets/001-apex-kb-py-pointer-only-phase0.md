# Target Plan — 001 pointer-only-phase0

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
    - "Apex KB v3 Failure Audit.txt"
    - "Apex KB v3 Patch Plan.txt"
    - "Apex KB Lifecycle Execution Audit.md"
    - "codex-old-agent-kb-execution-process-audit.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "cmd_phase0 builds files = iter_source_files(kb_root) and structures before pointer_only resolution."
    - "resolve_pointer_only_text_files returns string paths but those files are not added to the structures parsed for Phase 0 artifacts."
    - "pointer_only_warning_count is hardcoded to 0."
    - "pointer_only_unresolved is hardcoded to []."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The surface reports pointer_only fields but does not include resolved pointer-only files in Phase 0 artifact generation and does not report unresolved pointers truthfully."
  user_value_problem: "Pointer-only repo/local sources can be recorded in custody but then disappear from deterministic navigation, causing later LLM ingest to miss source material."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "detect pointer_only sources from source-manifest.json"
    - "support repo-local and kb-root-relative local text pointers"
    - "include accessible pointer-only text files in Phase 0 scanning or emit explicit unresolved status"
    - "avoid network fetches"
    - "report pointer_only_source_status with resolved/unresolved entries"
    - "report pointer_only_scanned_count accurately"
    - "report pointer_only_warning_count accurately"
    - "report pointer_only_unresolved accurately"
  must_not:
    - "hardcode warning_count: 0"
    - "hardcode unresolved: []"
    - "count resolved pointer files without scanning them"
    - "fetch network URLs"
    - "scan binary files"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair the `pointer_only_manifest_sources`, `resolve_pointer_only_text_files`, and `cmd_phase0` flow.

Implementation intent:

- Normalize manifest source storage mode lookup to support both `source_storage_mode` and legacy `storage_mode`.
    
- Read pointer path from `source_path`, `pointer`, or equivalent existing manifest field.
    
- Reject URLs and unsupported schemes as unresolved with a reason.
    
- Resolve relative pointers first against `kb_root`, then against repository root if the script can infer it safely from the current working tree or parent directories.
    
- Only allow files with text extensions already accepted by Phase 0.
    
- Produce structured status entries with `source_id`, `pointer`, `status`, `resolved_path`, and `reason`.
    
- Add resolved pointer files to the Phase 0 file list before `parse_markdown_structure`.
    
- Deduplicate files by resolved path so copied and pointer sources do not double-count.
    
- Count `pointer_only_scanned_count` from pointer files actually included in structures.
    
- Count `pointer_only_warning_count` from unresolved or unsupported pointer entries.
    
- Populate `pointer_only_unresolved` with unresolved status entries.
    

Do not change semantic ingest behavior. Do not create wiki pages. Do not perform network access.

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "grep for pointer_only_warning_count and verify it is not hardcoded to 0."
    - "grep for pointer_only_unresolved and verify it is derived from status entries."
  behavioral:
    - "Create KB-local file raw/pointer-source.md and a source-manifest pointer_only entry pointing to it."
    - "Run phase0 --allow-write --json."
    - "Verify heading-map.json contains raw/pointer-source.md."
    - "Verify pointer_only_scanned_count is 1."
    - "Create one missing pointer_only entry and verify pointer_only_unresolved contains it."
  regression:
    - "Existing copied raw/ sources still scan normally."
    - "Phase 0 still writes only manifests/phase0 artifacts."
    - "No network URL is fetched."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "001-apex-kb-py-pointer-only-phase0.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/001-apex-kb-py-pointer-only-phase0.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 1
  post_apply_checks:
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
    - "run pointer_only Phase 0 fixture"
```
