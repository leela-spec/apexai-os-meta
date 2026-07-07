# Target Plan — 004 graph-process-flow

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
    - "process-flow-graph-audit.md"
    - "graph-summary.md"
    - "link-graph.sample.json"
    - "Apex Phase 0 Corpus Intelligence Implementation Decision.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "process_graph_extract returns edge_type: [], yaml_path_reference: [], process_sequence: []."
    - "cmd_graph wraps the empty result."
    - "No artifacts are written under manifests/phase0."
    - "Docs claim graph artifacts and multiple edge types."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The command exists but extracts no graph/process-flow information and writes no artifacts."
  user_value_problem: "Apex KB loses deterministic navigation value for process and file-reference relationships."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "extract deterministic graph/process-flow edges from markdown links, wikilinks, explicit repo path references, YAML path references, and process sequence markers"
    - "write or plan artifacts under manifests/phase0/ if --allow-write is used"
    - "produce deterministic JSON output"
    - "avoid Obsidian dependency"
    - "avoid Node/remark dependency for V1"
  must_not:
    - "return empty arrays only"
    - "pretend a pure Markdown-link graph is sufficient"
    - "crawl the entire repo outside the KB root"
    - "perform semantic graph inference"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `process_graph_extract` and `cmd_graph`.

Implementation intent:

- Iterate KB-local text files only:
    
    - `raw/`
        
    - `sources/` if present
        
    - `ingest-analysis/`
        
    - `wiki/`
        
    - `kb-schema.md`
        
    - `README.md`
        
    - exclude `derived/`, `outputs/`, binary files, and large generated logs unless explicitly safe.
        
- Extract edge records with stable fields:
    
    - `source_path`
        
    - `target`
        
    - `edge_type`
        
    - `line`
        
    - `raw`
        
    - `confidence: deterministic`
        
- Edge families:
    
    - `markdown_link`
        
    - `wikilink`
        
    - `repo_path_reference`
        
    - `yaml_path_reference`
        
    - `process_sequence`
        
- Markdown links and wikilinks may reuse existing regex logic.
    
- Repo path references should detect Apex repo path-like strings such as `.claude/...`, `apex-meta/...`, `wiki/...`, `raw/...`, `manifests/...`.
    
- YAML path references should detect lines where key names contain `path`, `file`, `root`, `source`, `target`, or `output`, and values look path-like.
    
- Process sequence markers should detect arrows like `A -> B`, `A → B`, ordered stage labels, and explicit `hands_off_to`/`depends_on`-style fields where deterministic.
    
- Deduplicate edges deterministically.
    
- Return:
    
    - `edge_count`
        
    - `edges_by_type`
        
    - `artifacts`
        
    - `deterministic_only`
        
- With `--allow-write`, write:
    
    - `manifests/phase0/process-flow-graph.json`
        
    - optionally `manifests/phase0/process-flow-graph-summary.md`
        
- Without write, report planned artifacts only.
    

Do not require Obsidian, Node, remark, network, or LLM calls.

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "process_graph_extract must not return only hardcoded empty arrays."
    - "cmd_graph must plan or write manifests/phase0 artifacts."
  behavioral:
    - "Create fixture file containing a Markdown link, wikilink, repo path reference, YAML path reference, and A -> B sequence."
    - "Run graph --json."
    - "Verify edge_count > 0."
    - "Verify edges_by_type includes markdown_link, wikilink, repo_path_reference, yaml_path_reference, and process_sequence."
    - "Run graph --allow-write --json and verify process-flow-graph.json exists under manifests/phase0."
  regression:
    - "No network fetch."
    - "No outside-kb crawl."
    - "No graph command hard failure for empty KB; it should return zero edges truthfully."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "004-apex-kb-py-graph-process-flow.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/004-apex-kb-py-graph-process-flow.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 4
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> graph --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> graph --allow-write --json"
```
