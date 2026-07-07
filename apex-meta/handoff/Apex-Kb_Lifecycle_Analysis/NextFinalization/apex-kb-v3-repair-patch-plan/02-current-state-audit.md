# Current State Audit

## 1. Executive finding

```yaml
current_state_verdict: REPAIR
reason:
  - "0c747db4 is in main history and landed some useful surfaces."
  - "The original patch pack is invalid because git apply check failed."
  - "Manual equivalent edits were applied."
  - "Several advertised features are currently stub-class or partial."
  - "Targeted repair is safer than default full revert."
do_not_revert_by_default: true
````

## 2. What to preserve

```yaml
preserve:
  cli_output_json:
    status: KEEP_REAL
    reason: "Both lifecycle and retrieval scripts have --output-json machinery and path-constrained writes."
  cli_flag_placement:
    status: REPAIR_PARTIAL
    reason: "normalize_global_flag_placement exists and is useful, but docs/parser behavior still needs command-level validation."
  source_payload_manifest:
    status: KEEP_REAL
    reason: "Source-payload manifest generation is implemented and should be smoke-tested, not redesigned."
  status_freshness_split:
    status: REPAIR_PARTIAL
    reason: "wiki_index_status and retrieval_index_status exist, but retrieval_index_status is only present/missing."
```

## 3. What to repair

```yaml
repair:
  pointer_only_phase0:
    failure_class: REPLACE_STUB
    live_evidence:
      - "cmd_phase0 scans sources/raw files first."
      - "resolve_pointer_only_text_files is called after artifact structures are already built."
      - "pointer_only_warning_count is hardcoded to 0."
      - "pointer_only_unresolved is hardcoded to empty."
    required_repair:
      - "Resolve accessible local text pointers before Phase 0 parse."
      - "Include resolved pointer-only files in Phase 0 scanning."
      - "Report unresolved pointers truthfully."

  quality_coverage:
    failure_class: REPLACE_STUB
    live_evidence:
      - "quality_report creates source_to_page_map and page_to_source_map with empty lists."
      - "phase2_repair_candidates and shell_page_candidates are always empty."
    required_repair:
      - "Compute source/page maps from manifest and wiki frontmatter source_refs."
      - "Detect missing source_refs and missing Phase 2 value sections."
      - "Detect deterministic shell page candidates."

  query_eval:
    failure_class: REPLACE_STUB
    live_evidence:
      - "cmd_query_eval returns path plus empty expected_minimal_pages and raw_source_needed."
      - "It does not read, initialize, write, or validate a pack."
    required_repair:
      - "Read existing query-eval pack."
      - "Initialize minimal pack only with --init and --allow-write."
      - "Validate entries deterministically."

  graph_process_flow:
    failure_class: REPLACE_STUB
    live_evidence:
      - "process_graph_extract returns empty edge_type, yaml_path_reference, and process_sequence arrays."
      - "cmd_graph does not write manifests/phase0 artifacts."
    required_repair:
      - "Extract Markdown links, wikilinks, repo path references, YAML path references, and process sequence markers."
      - "Write deterministic artifacts under manifests/phase0 when --allow-write is used."

  script_command_contract_alignment:
    failure_class: DOCS_ONLY_REPAIR
    live_evidence:
      - "script-command-contract.md claims behavior not currently implemented."
    required_repair:
      - "After script repair, document only implemented behavior."
      - "Label partial or experimental behavior explicitly."
```

## 4. Later commits after 0c747db4

```yaml
later_commit_assessment:
  compare_base: 0c747db4
  compare_head: main
  ahead_by: 11
  target_file_repairs_detected_after_0c747db4: false
  observed_later_file_classes:
    - "handoff/prompt artifacts"
    - "Agent Mode process learning"
    - "post-codex audit JSON logs"
    - "pycache artifacts"
  consequence: "The suspect target-file implementation remains the baseline for repair."
```

## 5. Suspect patch artifacts

```yaml
invalid_patch_artifacts:
  path: "apex-meta/patches/apex-kb-v3-p0-p2-closure/"
  status: "historical_invalid"
  reason:
    - "git_apply_check failed."
    - "abbreviated hunk headers were used."
    - "manual equivalent edits replaced patch application."
  future_use:
    allowed:
      - "forensic evidence"
      - "anti-pattern reference"
    forbidden:
      - "implementation authority"
      - "baseline patch source"
      - "copy-forward into repair pack"
```

## 6. Audit conclusion

The repair pack must be built from live target files on main, not from the failed patch files. It must replace stub behavior with deterministic implementations or explicitly downgrade unsupported docs. It must preserve existing real functionality.
