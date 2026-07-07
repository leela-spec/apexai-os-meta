# Target Plan — 010 acceptance-tests

## 1. Target file

```text
.claude/skills/apex-kb/references/acceptance-tests.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "AgentModePatchGuide_v4.md"
    - "Apex KB Lifecycle Execution Audit.md"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/acceptance-tests.md"
    - "apex-meta/scripts/apex_kb.py"
    - "apex-meta/scripts/apex_kb_retrieval.py"
  evidence:
    - "Acceptance tests cover scaffold, source intake, source-payload manifest, Phase 0, gate, wiki/index/retrieval, lint/audit."
    - "Acceptance tests do not yet explicitly validate repaired pointer-only Phase 0."
    - "Acceptance tests do not yet explicitly validate quality maps/candidates."
    - "Acceptance tests do not yet explicitly validate query-eval init/read/schema."
    - "Acceptance tests do not yet explicitly validate graph/process-flow extraction."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "Acceptance tests do not yet prevent stub-class surfaces from passing."
  user_value_problem: "Marker-only or empty-output implementations can pass unless behavior fixtures are required."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "add deterministic acceptance checks for pointer_only Phase 0"
    - "add deterministic acceptance checks for quality/coverage maps"
    - "add deterministic acceptance checks for shell page candidates"
    - "add deterministic acceptance checks for query-eval --init"
    - "add deterministic acceptance checks for graph/process-flow extraction"
    - "add --output-json checks"
  must_not:
    - "replace compile and behavior checks with grep-only checks"
    - "require external dependencies"
    - "require network access"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Append a v3 repair acceptance section.

Implementation intent:

- Add fixture setup commands that create a small KB with:
    
    - one copied raw note
        
    - one pointer-only local text source
        
    - one missing pointer-only source
        
    - one good wiki concept page with source_refs and Phase 2 value headings
        
    - one shell page missing source_refs/value headings
        
    - one file with link/wikilink/path/YAML/sequence graph cues
        
- Add commands:
    
    - `phase0 --allow-write --json`
        
    - `quality --json`
        
    - `coverage --json`
        
    - `query-eval --init` dry-run
        
    - `query-eval --init --allow-write`
        
    - `graph --allow-write --json`
        
    - `status --output-json log/status.json`
        
    - retrieval `health --output-json log/retrieval-health.json`
        
- Add pass criteria checking behavior, not only markers.
    
- Keep examples shell-neutral where possible; include PowerShell-safe and Git Bash variants only if concise.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "File includes pointer_only Phase 0 repair fixture."
    - "File includes quality/coverage repair fixture."
    - "File includes query-eval repair fixture."
    - "File includes graph/process-flow repair fixture."
  behavioral:
    - "Commands are runnable from repo root."
    - "Pass criteria assert non-empty or accurately unresolved outputs where expected."
  regression:
    - "Existing scaffold/source-intake/retrieval tests remain."
    - "No dependency beyond Python stdlib."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "010-acceptance-tests.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/010-acceptance-tests.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "grep-only acceptance criteria"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 10
  post_apply_checks:
    - "read acceptance tests and run the new v3 repair fixture subset"
```
