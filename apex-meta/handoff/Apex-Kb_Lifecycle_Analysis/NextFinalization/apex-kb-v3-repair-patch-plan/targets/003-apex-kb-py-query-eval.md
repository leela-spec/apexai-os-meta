# Target Plan — 003 query-eval

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
    - "DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "query_eval_pack_path returns outputs/queries/evals/query-eval-pack.json."
    - "cmd_query_eval returns a path plus expected_minimal_pages: [] and raw_source_needed: []."
    - "It does not read an existing pack."
    - "It does not initialize a pack."
    - "It does not validate pack schema."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The command only returns a path and empty arrays while docs claim read/init/validate behavior."
  user_value_problem: "Apex KB cannot evaluate query-routing coverage deterministically, so retrieval usefulness remains untested."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "read existing outputs/queries/evals/query-eval-pack.json if present"
    - "initialize a minimal valid pack when --init and --allow-write are provided"
    - "validate schema deterministically"
    - "report expected_routes, expected_minimal_pages, raw_source_needed"
    - "avoid semantic LLM grading"
  must_not:
    - "only return a path"
    - "hardcode empty arrays without reading the pack"
    - "judge answer quality semantically"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `cmd_query_eval` and related parser flags.

Implementation intent:

- Keep pack path at `outputs/queries/evals/query-eval-pack.json`.
    
- Add parser support for:
    
    - `--init`
        
    - `--json`
        
    - `--allow-write` via normalized global flag
        
- Define minimal pack schema:
    
    - `schema: apex.query_eval_pack.v1`
        
    - `kb_slug`
        
    - `queries`
        
    - each query has `query`, `expected_routes`, `expected_minimal_pages`, `raw_source_needed`
        
- If pack exists:
    
    - read JSON
        
    - validate object structure
        
    - validate every query entry
        
    - return `status`, `issue_count`, `issues`, `query_count`, `expected_routes`, `expected_minimal_pages`, `raw_source_needed`
        
- If pack missing and `--init` without effective write:
    
    - return `status: planned`
        
    - include planned write path
        
    - do not write
        
- If pack missing and `--init --allow-write`:
    
    - create parent directory
        
    - write minimal valid pack
        
    - return `status: initialized`
        
- If pack missing and no `--init`:
    
    - return `status: missing`
        
    - do not fail unless strict is later added.
        
- No LLM grading, no query execution, no web/network access.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "cmd_query_eval must read or initialize query-eval-pack.json."
    - "result must include status and issue_count."
  behavioral:
    - "Run query-eval --init without --allow-write; verify no file created and planned status returned."
    - "Run query-eval --init --allow-write; verify valid JSON file created."
    - "Run query-eval on valid pack; verify issue_count 0."
    - "Run query-eval on invalid pack; verify deterministic issues."
  regression:
    - "No LLM grading occurs."
    - "outputs are valid JSON with --output-json."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "003-apex-kb-py-query-eval.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/003-apex-kb-py-query-eval.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 3
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> query-eval --init --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> --allow-write query-eval --init --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> query-eval --json"
```
