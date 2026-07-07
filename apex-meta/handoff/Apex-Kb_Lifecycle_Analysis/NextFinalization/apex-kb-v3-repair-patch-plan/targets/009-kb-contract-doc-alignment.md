# Target Plan — 009 kb-contract-doc-alignment

## 1. Target file

```text
.claude/skills/apex-kb/references/kb-contract.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
    - "Apex-KB_UpdatePlan.md"
    - "Apex KB v3 Audit.txt"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/SKILL.md"
    - "apex-meta/scripts/apex_kb.py"
  evidence:
    - "kb-contract.md already defines canonical versus derived paths."
    - "source-payload-manifest is included as canonical."
    - "Phase 2 page value contract is included and mostly aligned."
    - "Source custody says pointer_only requires source_path/source_hash/source_storage_mode, but live pointer_only may have no hash with no_hash_reason."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "The contract is largely valid but may need minimal alignment with repaired pointer-only and payload-manifest behavior."
  user_value_problem: "Source custody rules must not force impossible hashes for pointer-only local paths when no_hash_reason is the correct durable record."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve canonical/derived split"
    - "preserve source-payload-manifest role"
    - "align pointer_only source fields with actual manifest behavior"
    - "state that pointer_only Phase 0 scans only safe local text pointers or reports unresolved"
    - "keep no external BagIt dependency rule"
  must_not:
    - "reopen source-payload manifest architecture"
    - "weaken source custody"
    - "turn source-payload-manifest into replacement for source-manifest.json"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Patch only the source custody section if needed.

Implementation intent:

- Keep existing data root, canonical/derived, root shape, page contract, and boundary contract.
    
- In `source_storage_modes.pointer_only`, allow:
    
    - `source_path`
        
    - `source_storage_mode`
        
    - `source_hash` when available
        
    - `no_hash_reason` when not hashable
        
- Add a concise line that Phase 0 may use safe resolved pointer-only local text files for deterministic navigation, and must report unresolved pointers.
    
- Do not add new schema bureaucracy.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "pointer_only contract mentions source_hash when available or no_hash_reason when unavailable."
    - "contract says source-payload-manifest does not replace source-manifest.json."
  behavioral:
    - "N/A documentation alignment only."
  regression:
    - "canonical/derived paths remain unchanged."
    - "boundary contract remains unchanged."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "009-kb-contract-doc-alignment.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/009-kb-contract-doc-alignment.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "broad lifecycle rewrite"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 9
  post_apply_checks:
    - "grep source-payload-manifest references"
    - "grep pointer_only source_storage_modes"
```
