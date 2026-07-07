# Validation Contract

## 1. Patch validity

```yaml
patch_validity:
  must:
    - "every .patch has normal diff --git headers"
    - "every hunk has line-range headers"
    - "git apply --check passes individually"
    - "git apply --check passes cumulatively"
    - "no abbreviated hunk headers"
    - "no manual equivalent edits"
````

## 2. Static validation

```yaml
static_validation:
  commands:
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
    - "python -m py_compile apex-meta/scripts/apex_kb_retrieval.py"
    - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design --help"
    - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/claude-skill-design --help"
  required:
    - "help output includes phase0"
    - "help output includes quality"
    - "help output includes coverage"
    - "help output includes query-eval"
    - "help output includes graph or process-graph"
    - "docs mention only implemented behavior"
```

## 3. Behavioral validation

```yaml
behavioral_validation:
  pointer_only_phase0:
    - "create a test KB with source-manifest.json containing pointer_only source_path to a KB-local text file"
    - "run phase0 --allow-write --json"
    - "assert resolved pointer file contributes to heading/link/frontmatter artifacts"
    - "assert pointer_only_scanned_count equals resolved scanned files"
    - "assert unresolved pointer reports in pointer_only_unresolved"

  quality_coverage:
    - "create wiki pages with and without source_refs"
    - "assert source_to_page_map and page_to_source_map are non-empty when source_refs exist"
    - "assert pages_without_source_refs reports missing refs"
    - "assert pages_missing_phase2_value_sections reports missing required sections"
    - "assert phase2_repair_candidates and shell_page_candidates are deterministically populated"

  query_eval:
    - "run query-eval --init without --allow-write and assert planned write only"
    - "run query-eval --init --allow-write and assert outputs/queries/evals/query-eval-pack.json is created"
    - "run query-eval on existing pack and assert status, issue_count, expected_routes, expected_minimal_pages, raw_source_needed"

  graph_process_flow:
    - "create fixture Markdown with markdown links, wikilinks, repo path references, YAML path references, and sequence arrows"
    - "run graph --allow-write --json"
    - "assert deterministic JSON output contains edge categories"
    - "assert artifacts are written under manifests/phase0/"

  output_json:
    - "--output-json writes valid UTF-8 JSON inside kb_root"
    - "outside-kb-root output path is rejected"

  cli_flag_placement:
    - "global flags work before subcommand"
    - "supported global flags work after subcommand"
```

## 4. Final validation

```yaml
final_validation:
  - "git status limited to expected files"
  - "no target files modified in Agent Mode builder final state"
  - "no patch workaround report in new repair patch pack"
  - "no manual equivalent edits"
  - "final report classifies each feature"
  - "invalid old p0-p2 closure patch files remain historical only"
```
