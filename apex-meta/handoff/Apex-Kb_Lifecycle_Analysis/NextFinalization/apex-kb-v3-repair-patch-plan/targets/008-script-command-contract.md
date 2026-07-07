# Target Plan — 008 script-command-contract

## 1. Target file

```text
.claude/skills/apex-kb/references/script-command-contract.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "AgentModePatchGuide_v4.md"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/script-command-contract.md"
    - "apex-meta/scripts/apex_kb.py"
    - "apex-meta/scripts/apex_kb_retrieval.py"
  evidence:
    - "Contract claims quality/coverage computes maps and candidates."
    - "Contract claims query-eval validates or initializes a pack."
    - "Contract claims graph generates deterministic artifacts under manifests/phase0."
    - "Contract claims pointer_only Phase 0 resolves repo-local pointers and reports unresolved/warnings."
    - "Live code does not yet implement those claims fully."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "The contract overclaims behavior that is currently partial or stub-class."
  user_value_problem: "Future agents and Codex prompts trust docs that do not match implementation, recreating PASS_WITH_WORKAROUNDS risk."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "script-command-contract.md must describe only implemented behavior"
    - "any experimental or partial command must be labeled partial or planned"
    - "PowerShell-safe --output-json examples must match parser behavior"
    - "global flag placement docs must match actual parser behavior"
  must_not:
    - "claim graph artifacts are generated if graph command only returns data"
    - "claim query-eval initializes packs if it does not"
    - "claim quality computes maps if maps remain empty"
    - "claim pointer-only scanned files if they are only counted"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Patch the contract after script behavior is repaired.

Implementation intent:

- Keep the shared policy and command tables.
    
- Update `v3 closure additions` so each command reflects implemented behavior after targets 001–007.
    
- If the builder fails to implement any script behavior, label that behavior `partial` or `planned`, not complete.
    
- Add exact examples:
    
    - before-subcommand global flags
        
    - after-subcommand global flags only where supported
        
    - `--output-json` writing inside KB root
        
- State that old p0-p2 closure patches are historical invalid artifacts and not command authority only if this belongs in contract; otherwise keep that in patch-pack manifest.
    
- Do not introduce a new lifecycle model.
    
- Do not claim behavior proven only by marker grep.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "No unsupported claim remains for quality/coverage."
    - "No unsupported claim remains for query-eval init/validate."
    - "No unsupported claim remains for graph artifact writing."
    - "No unsupported claim remains for pointer-only scanning."
  behavioral:
    - "Each documented command has a matching parser command."
    - "Each documented --output-json example executes in smoke tests."
  regression:
    - "Docs keep Python standard-library/no-network/no-shell-out policy."
    - "Docs keep writes-inside-kb-root policy."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "008-script-command-contract.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/008-script-command-contract.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only documentation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 8
  post_apply_checks:
    - "grep documented command names and verify parser has matching subcommands"
    - "grep for unsupported overclaim phrases"
```
