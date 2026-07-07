# Target Plan — 005 status-freshness

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
    - "Apex KB v3 Patch Plan.txt"
    - "codex-old-agent-kb-execution-process-audit.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - "apex-meta/scripts/apex_kb_retrieval.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "cmd_status returns wiki_index_status and retrieval_index_status."
    - "retrieval_index_status only returns present or missing based on derived/search/index-meta.json."
    - "It does not compare retrieval metadata to current wiki pages."
```

## 3. Failure class

```yaml
failure_class:
  status: REPAIR_PARTIAL
  reason: "The split exists and is useful, but retrieval freshness is only presence detection."
  user_value_problem: "Operators can mistake a present retrieval index for a fresh retrieval index."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve wiki_index_status"
    - "preserve retrieval_index_status"
    - "report retrieval index missing, fresh, stale, or unknown"
    - "avoid importing or shelling into retrieval script if a simple metadata check is sufficient"
    - "remain read-only"
  must_not:
    - "collapse wiki and retrieval freshness into one status field"
    - "claim fresh when only metadata is present"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `retrieval_index_status(kb_root)`.

Implementation intent:

- Keep `wiki_index_status` as `stale_index_status(kb_root)`.
    
- For retrieval:
    
    - If `derived/search/index-meta.json` is missing, return `missing`.
        
    - If metadata cannot be read, return `unknown` or `unreadable`.
        
    - If metadata includes indexed wiki file hashes, compare them to current wiki page hashes.
        
    - If any current page hash differs, any indexed page is missing, or any current wiki page is absent from metadata, return `stale`.
        
    - If metadata shape is older and cannot prove freshness, return `present_unknown_freshness` or `unknown` instead of `fresh`.
        
- Do not run `apex_kb_retrieval.py` from inside `apex_kb.py`.
    
- Do not write.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "retrieval_index_status must not return present merely because index-meta.json exists."
  behavioral:
    - "No index-meta.json -> retrieval_index_status: missing."
    - "Unreadable/legacy metadata -> unknown or present_unknown_freshness."
    - "Fresh metadata matching wiki hashes -> fresh."
    - "Modify a wiki page after metadata -> stale."
  regression:
    - "status command remains read-only."
    - "source_payload_manifest_status remains unchanged."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "005-apex-kb-py-status-freshness.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/005-apex-kb-py-status-freshness.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 5
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> status --json"
```
