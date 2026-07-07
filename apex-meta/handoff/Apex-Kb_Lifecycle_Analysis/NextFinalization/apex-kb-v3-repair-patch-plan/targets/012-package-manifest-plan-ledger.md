# Target Plan — 012 package-manifest-plan-ledger

## 1. Target file

```text
.claude/skills/apex-kb/package-manifest.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Patch Plan.txt"
    - "AgentModePatchGuide_v4.md"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/package-manifest.md"
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "Package manifest lists package path, script paths, runtime policy, inventory, canonical paths, derived paths, and scope exclusions."
    - "It does not need broad repair."
    - "It may need minor alignment if new or repaired docs are added."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "The manifest is mostly correct; update only if the repair pack changes package file inventory or adds new reference/example files."
  user_value_problem: "Package manifests are used for future navigation and should not go stale after repair."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve package_name apex-kb"
    - "preserve package_path .claude/skills/apex-kb/"
    - "preserve runtime script paths"
    - "ensure repaired reference files remain listed"
    - "ensure canonical/derived path lists remain accurate"
  must_not:
    - "rename package"
    - "touch apex-kb2"
    - "add patch-plan files as runtime package files"
    - "claim the skill folder is executable by itself"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Patch only if necessary.

Implementation intent:

- If target files remain the existing package files, leave package manifest unchanged.
    
- If builder adds any new package reference file, add it to Inventory.
    
- Do not list `apex-meta/handoff/.../apex-kb-v3-repair-patch-plan/` as a package runtime file.
    
- Do not list `apex-meta/patches/apex-kb-v3-repair/` as a package runtime file; it is patch artifact history.
    
- Keep executability note.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "package_name remains apex-kb."
    - "script paths remain apex-meta/scripts/apex_kb.py and apex-meta/scripts/apex_kb_retrieval.py."
    - "canonical and derived paths match SKILL.md and kb-contract.md."
  behavioral:
    - "N/A documentation alignment only."
  regression:
    - "No apex-kb2 references introduced."
    - "No patch-pack artifact path listed as runtime package file."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "012-package-manifest-plan-ledger.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/012-package-manifest-plan-ledger.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "package rename"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 12
  post_apply_checks:
    - "grep package_name"
    - "grep script_paths"
    - "grep canonical_paths"
```
