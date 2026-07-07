# Target Plan — 002 quality-coverage

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Pre-Analysis.txt"
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
  evidence:
    - "quality_report returns source_to_page_map and page_to_source_map, but every list is empty."
    - "phase2_repair_candidates is always empty."
    - "shell_page_candidates is always empty."
    - "Current lint checks missing Phase 2 value headings, but quality command does not expose coverage meaningfully."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The quality command exposes expected keys but performs no real source/page coverage or shell-page analysis."
  user_value_problem: "Apex KB can pass structural checks while still producing low-value pages with weak source routing."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "compute source_to_page_map from wiki page frontmatter source_refs and/or structured source pointers"
    - "compute page_to_source_map"
    - "report pages_without_source_refs"
    - "report pages_missing_phase2_value_sections"
    - "report phase2_repair_candidates"
    - "detect shell/low-value pages using minimal structural heuristics"
    - "remain deterministic and non-semantic"
  must_not:
    - "return only empty maps"
    - "perform LLM grading"
    - "create a subjective page_value_score"
    - "hard fail by default"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `quality_report(kb_root)` and `cmd_quality`.

Implementation intent:

- Load `source-manifest.json`.
    
- Build canonical source identifiers from `source_id`, `id`, `source_path`, and pointer fields.
    
- Iterate `wiki_pages(kb_root)`.
    
- Parse frontmatter and body.
    
- Extract `source_refs` from frontmatter:
    
    - list of strings
        
    - list of objects with `source_id`, `source_path`, `source_pointer`
        
    - scalar fallback
        
- Build `page_to_source_map` as page path -> list of source identifiers/pointers.
    
- Build `source_to_page_map` as manifest source -> pages that reference it.
    
- Add source IDs found in pages but not manifest under `unmanifested_source_refs`.
    
- Add manifest sources not used by any page under `manifest_sources_without_pages`.
    
- Add pages with no usable source refs under `pages_without_source_refs`.
    
- Detect missing Phase 2 value sections using `PHASE2_VALUE_HEADINGS`.
    
- Detect shell page candidates with structural heuristics:
    
    - missing source refs
        
    - low body density after frontmatter
        
    - no Key Claims section
        
    - no Macro/Meso/Micro section
        
    - only YAML blocks and minimal narrative
        
- Populate `phase2_repair_candidates` when summary/concept/entity pages miss required value headings or source routing.
    
- Keep `--strict` behavior optional and deterministic; strict can return fail status if candidates exist, but default should report only.
    

Do not score semantic quality. Do not rewrite pages.

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "quality_report must populate maps from parsed wiki page source_refs."
    - "phase2_repair_candidates must be derived from actual page checks."
  behavioral:
    - "Create one page with source_refs and one page without source_refs."
    - "Run quality --json."
    - "Verify page_to_source_map includes the referenced source."
    - "Verify source_to_page_map maps the source to the page."
    - "Verify pages_without_source_refs includes the unreferenced page."
    - "Verify pages_missing_phase2_value_sections reports missing headings."
  regression:
    - "quality command remains read-only."
    - "coverage alias returns the same structure."
    - "No LLM calls, network calls, or outside-kb writes occur."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "002-apex-kb-py-quality-coverage.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/002-apex-kb-py-quality-coverage.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 2
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> quality --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> coverage --json"
```
