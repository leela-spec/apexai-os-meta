# Target Plan — 011 phase2-value-contract-alignment

## 1. Target file

```text
.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
    - "Apex KB Phase 2 Repair.txt"
    - "Apex KB v3 Pre-Analysis.txt"
    - "Apex KB v3 Audit.txt"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
  evidence:
    - "Rules already define Phase 2 page value sections."
    - "Lint rules mention stale retrieval index, but current status/quality behavior needs clearer alignment."
    - "Query rules mention index-first retrieval, but query-eval pack behavior is not described."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "Rules are mostly valid but should align with repaired quality/coverage and query-eval behavior."
  user_value_problem: "Future agents need one operational rule page that explains how quality, query-eval, and lint/reporting interact without turning them into semantic grading."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve Phase 2 value contract"
    - "define quality/coverage as deterministic structural reporting"
    - "define query-eval as deterministic route/schema pack validation, not LLM grading"
    - "define graph/process-flow as deterministic Phase 0 navigation artifact"
    - "distinguish report-only findings from blocking lint failures"
  must_not:
    - "weaken source grounding"
    - "add page_value_score"
    - "require fixed source count"
    - "make graph extraction a semantic inference task"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Add a concise v3 repair subsection.

Implementation intent:

- Under Query rules, add query-eval pack rule:
    
    - queries define expected routes/pages/raw-source-needed
        
    - script validates schema only
        
    - no answer grading
        
- Under Lint rules or new Quality rules, describe:
    
    - `quality` and `coverage` report source/page maps
        
    - pages missing source refs
        
    - pages missing Phase 2 value sections
        
    - repair candidates
        
    - shell candidates
        
    - report-only by default
        
- Under Phase 0, mention graph/process-flow artifacts if implemented:
    
    - extracted deterministically
        
    - written under `manifests/phase0`
        
    - no Obsidian/Node dependency
        
- Keep current Phase 1/Phase 2 boundaries.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "Rules explicitly say quality/coverage is deterministic and non-semantic."
    - "Rules explicitly say query-eval is not LLM grading."
    - "Rules explicitly say graph/process-flow is deterministic."
  behavioral:
    - "N/A documentation alignment only."
  regression:
    - "Phase 0 must_not_create list remains."
    - "Query remains read-only for Plan/Sync/Session."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "011-phase2-value-contract-alignment.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/011-phase2-value-contract-alignment.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "new semantic grading system"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 11
  post_apply_checks:
    - "grep for query-eval non-grading rule"
    - "grep for quality/coverage deterministic reporting rule"
```
