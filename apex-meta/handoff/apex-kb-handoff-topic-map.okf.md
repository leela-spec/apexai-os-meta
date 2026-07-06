```okf
okf_document:
  id: apex_kb_handoff_topic_map
  artifact_type: machine_readable_topic_map
  source_folder: apex-meta/handoff/
  generated_for: future_apex_kb_planning_and_patch_runs
  source_access:
    status: pass
    method: github_connector_search_and_fetch_file
    files_read:
      - apex-meta/handoff/task_plan.md
      - apex-meta/handoff/findings.md
      - apex-meta/handoff/progress.md
      - apex-meta/handoff/next-session.md
      - apex-meta/handoff/narm-index-prep-handover.md
      - apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
      - apex-meta/handoff/apex-kb-v2-planning-handover.md

files:
  - path: apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
    authority: P0_binding
    read_priority: 1
    currentness: current_process_memory
    topics:
      - process_drift
      - lifecycle_phase_preservation
      - codex_prompt_standard
      - executor_routing
      - no_option_sprawl
  - path: apex-meta/handoff/apex-kb-v2-planning-handover.md
    authority: P0_binding
    read_priority: 2
    currentness: current_planning_handover_live_verification_required
    topics:
      - apex_kb_v2
      - value_to_overhead
      - quality_command
      - output_tier_policy
      - source_set_plan
      - skill_compaction
  - path: apex-meta/handoff/narm-index-prep-handover.md
    authority: P1_operational
    read_priority: 3
    currentness: current_for_narm_pre_indexing
    topics:
      - narm_support_kb
      - definitions_of_done
      - index_artifact_plan
      - source_file_map
      - workflow_prompts
  - path: apex-meta/handoff/next-session.md
    authority: P1_operational
    read_priority: 4
    currentness: partly_superseded_by_narm_index_prep
    topics:
      - narm_next_actions
      - open_items
      - process_drift_risk
  - path: apex-meta/handoff/task_plan.md
    authority: P1_operational
    read_priority: 5
    currentness: current_h6_plan
    topics:
      - narm_project_phases
      - therapy_support_scope
      - privacy_redaction
  - path: apex-meta/handoff/findings.md
    authority: P1_operational
    read_priority: 6
    currentness: current_narm_source_notes
    topics:
      - durable_findings
      - source_notes
      - operator_validation
  - path: apex-meta/handoff/progress.md
    authority: P1_operational
    read_priority: 7
    currentness: historical_session_log
    topics:
      - h6_creation_log
      - state_deltas
      - apex_sync_route

topics:
  - id: current_state_locks
    summary: >
      The handoff folder locks process behavior more strongly than implementation details.
      Future Apex KB runs must preserve lifecycle phase, executor class, deterministic/semantic
      ownership, and main-only Codex behavior unless explicitly overridden.
    files:
      - path: apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
        authority: P0_binding
        relevance: highest
        key_findings:
          - Apex KB lifecycle order is explicit and must not be rewound without proof.
          - Deterministic validation is a gate, not the product.
          - Codex handoffs must be complete one-artifact execution packets.
      - path: apex-meta/handoff/apex-kb-v2-planning-handover.md
        authority: P0_binding
        relevance: high
        key_findings:
          - V1 executed and V2 should optimize value-to-overhead.
          - Python owns deterministic structure; LLM owns semantic synthesis.
          - Repaired package files and execution-test artifacts must be loaded before planning.
    future_use: Read before any Apex KB planning, prompt-flow repair, or Codex handoff.

  - id: deterministic_script_inefficiencies
    summary: >
      The handoff folder identifies script-improvement directions but is not enough by itself
      to patch scripts. It proposes quality/eval, source-set planning support, coverage,
      query evals, and structural checks.
    files:
      - path: apex-meta/handoff/apex-kb-v2-planning-handover.md
        authority: P0_binding
        relevance: highest
        key_findings:
          - Add deterministic quality/eval command as a high-impact V2 change.
          - Add source-set planning before ingestion.
          - Add claim-density, redundancy, query-performance, and coverage checks.
    future_use: Live-verify `apex-meta/scripts/apex_kb.py` and command contracts before patching.

  - id: lifecycle_prompt_flow_inefficiencies
    summary: >
      Prior failures came from phase rewinds, option sprawl, partial Codex prompts,
      deterministic loop overextension, wrong executor routing, and poor state compression.
    files:
      - path: apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
        authority: P0_binding
        relevance: highest
        key_findings:
          - Do not offer options when the process has a defined next step.
          - Do not create another deterministic task after a PASS unless a hard failure remains.
          - Chunk by execution boundary, not reasoning boundary.
    future_use: Use as the process standard for all future handoffs and Codex prompts.

  - id: missing_or_wrongly_excluded_high_impact_tools
    summary: >
      Many high-impact tools are absent or only indirectly evidenced in the live handoff folder.
      Absence here does not prove absence from the repo; it means future runs must route to
      broader project resources or live repo files before implementation.
    files:
      - path: apex-meta/handoff/apex-kb-v2-planning-handover.md
        authority: P0_binding
        relevance: medium
        key_findings:
          - Retrieval/query eval and coverage are high-impact V2 extensions.
          - Command contracts and repaired package files should be reloaded before planning.
      - path: apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
        authority: P0_binding
        relevance: medium
        key_findings:
          - Phase 1/Phase 2 semantic synthesis and deterministic ownership split are explicit.
          - Main-only Codex execution standard is explicit.
    future_use: Build a tool-specific audit from live repo/project resources, not from this folder alone.

  - id: source_custody_and_manifest_integrity
    summary: >
      For NARM, the folder preserves source names and the source folder. For generic Apex KB,
      it preserves ownership rules for hashing/source manifests but not a complete payload-manifest contract.
    files:
      - path: apex-meta/handoff/findings.md
        authority: P1_operational
        relevance: high_for_narm
        key_findings:
          - Exact source folder and named source files are recorded.
          - Operator validation is confirmed.
      - path: apex-meta/handoff/narm-index-prep-handover.md
        authority: P1_operational
        relevance: high_for_narm
        key_findings:
          - Source-file-map artifact is required before final index building.
      - path: apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
        authority: P0_binding
        relevance: medium_for_generic_apex_kb
        key_findings:
          - File hashing and source manifest shape are deterministic ownership.
    future_use: For source-payload-manifest work, find the specific source-payload handover or live script contract.

  - id: retrieval_and_query_layer
    summary: >
      The handoff folder treats retrieval as a lifecycle/evaluation topic, not as a technical contract.
    files:
      - path: apex-meta/handoff/apex-kb-v2-planning-handover.md
        authority: P0_binding
        relevance: medium
        key_findings:
          - Query-performance smoke tests are a ranked V2 priority.
          - `wiki/index.md` is a stable query entry point.
    future_use: Verify `apex_kb_retrieval.py`, retrieval contracts, and derived-artifact policy outside this folder.

  - id: graph_and_phase0_navigation
    summary: >
      The folder preserves Phase 0 as deterministic navigation ownership but does not contain
      graph/process-flow extraction details.
    files:
      - path: apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
        authority: P0_binding
        relevance: medium
        key_findings:
          - Corpus profile, heading/link/frontmatter maps, keyword maps, and deterministic index sections are deterministic ownership.
    future_use: Treat graph/process-flow extraction as V1.5 unless a live spec says otherwise.

  - id: codex_and_github_execution_process
    summary: >
      Future Codex prompts must be main-only by default, complete, target-scoped,
      and must avoid optional branches or broad validation loops.
    files:
      - path: apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
        authority: P0_binding
        relevance: highest
        key_findings:
          - Work directly on main and complete with commit/push when requested.
          - Do not split Codex work into partial packets.
          - Do not stop on unrelated dirty files unless they conflict with target paths.
    future_use: Include these rules in every Apex KB Codex handoff.

  - id: narm_support_kb_continuation
    summary: >
      NARM files define a separate domain-specific continuation: prepare artifacts under
      `apex-meta/artifacts/narm-support-knowledgebase/` before any final index build.
    files:
      - path: apex-meta/handoff/narm-index-prep-handover.md
        authority: P1_operational
        relevance: highest_for_narm
        key_findings:
          - Create definitions-of-done, index-artifact-plan, validation questions, source-file-map, and workflow-prompts.
          - Do not write final indexes yet.
      - path: apex-meta/handoff/task_plan.md
        authority: P1_operational
        relevance: high_for_narm
        key_findings:
          - The system is therapy-support infrastructure, not therapist replacement.
    future_use: Route NARM tasks here; do not confuse with generic Apex KB process patches.

tool_inclusion_audit:
  - tool_or_pattern: source-payload-manifest / BagIt-style hashing
    desired_layer: source_custody
    current_status: not_evidenced_in_live_handoff_folder
    wanted_by_operator: unknown_from_this_folder
    evidence_files: []
    recommendation: Find dedicated source-payload-manifest handover or live script contract before patching.
  - tool_or_pattern: SQLite FTS5/BM25
    desired_layer: retrieval
    current_status: indirectly_evidenced_as_query_eval_need
    wanted_by_operator: unknown_from_this_folder
    evidence_files:
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    recommendation: Verify retrieval contract and `apex_kb_retrieval.py` outside this folder.
  - tool_or_pattern: JSON retrieval fallback
    desired_layer: retrieval
    current_status: not_evidenced_in_live_handoff_folder
    wanted_by_operator: unknown_from_this_folder
    evidence_files: []
    recommendation: Do not infer status; live-verify retrieval script.
  - tool_or_pattern: apex_kb_retrieval.py
    desired_layer: retrieval_script
    current_status: not_evidenced_in_live_handoff_folder
    wanted_by_operator: unknown_from_this_folder
    evidence_files: []
    recommendation: Fetch live script before retrieval tasks.
  - tool_or_pattern: markdown-it-py
    desired_layer: phase0_parser_v1_5
    current_status: not_evidenced_in_live_handoff_folder
    wanted_by_operator: unknown_from_this_folder
    evidence_files: []
    recommendation: Keep out of handoff-driven patches unless parser warnings are active.
  - tool_or_pattern: PyYAML / python-frontmatter
    desired_layer: frontmatter_parsing
    current_status: not_evidenced_in_live_handoff_folder
    wanted_by_operator: unknown_from_this_folder
    evidence_files: []
    recommendation: Treat as dependency decision, not a default handoff-folder action.
  - tool_or_pattern: graph/process-flow extraction
    desired_layer: phase0_v1_5_navigation
    current_status: indirectly_relevant_only
    wanted_by_operator: unknown_from_this_folder
    evidence_files:
      - apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
    recommendation: Route to graph/process audit resources before implementation.
  - tool_or_pattern: GitHub connector
    desired_layer: repo_access_and_publish
    current_status: not_explicitly_documented
    wanted_by_operator: unknown_from_this_folder
    evidence_files: []
    recommendation: Future handoffs should state local Codex vs connector execution surface.
  - tool_or_pattern: LLM Phase 1/Phase 2 semantic synthesis
    desired_layer: semantic_lifecycle
    current_status: explicitly_evidenced
    wanted_by_operator: true
    evidence_files:
      - apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    recommendation: Preserve LLM ownership and gate rules.
  - tool_or_pattern: lint/audit/status/health
    desired_layer: deterministic_validation
    current_status: evidenced_as_existing_or_needed
    wanted_by_operator: true
    evidence_files:
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    recommendation: Extend with quality/coverage only after live command-surface check.
  - tool_or_pattern: command-contract docs
    desired_layer: package_contract
    current_status: evidenced_as_files_to_reload
    wanted_by_operator: true
    evidence_files:
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    recommendation: Always compare docs with live script before patching.
  - tool_or_pattern: Codex main-only execution standard
    desired_layer: execution_process
    current_status: explicitly_evidenced
    wanted_by_operator: true
    evidence_files:
      - apex-meta/handoff/apex-kb-chat-drift-learning.okf.md
    recommendation: Use by default unless operator explicitly asks for branch/PR.

ranked_backlog:
  - rank: 1
    idea: Add or verify output tier policy
    layer: lifecycle_user_experience
    impact: 94
    evidence: 85
    risk: 25
    cost: 35
    source_files:
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    next_action: Live-verify package contracts and add compact tier rules.
  - rank: 2
    idea: Add deterministic quality/eval command
    layer: validation
    impact: 92
    evidence: 82
    risk: 40
    cost: 55
    source_files:
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    next_action: Implement only countable structure checks first.
  - rank: 3
    idea: Compact SKILL.md into routing kernel
    layer: skill_package
    impact: 88
    evidence: 75
    risk: 45
    cost: 45
    source_files:
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    next_action: Do after current live package is stable.
  - rank: 4
    idea: Add source-set planning before ingestion
    layer: ingest_planning
    impact: 87
    evidence: 78
    risk: 35
    cost: 40
    source_files:
      - apex-meta/handoff/apex-kb-v2-planning-handover.md
    next_action: Add LLM-owned plan artifact with deterministic placement.
  - rank: 5
    idea: Create NARM preparation artifacts
    layer: narm_project
    impact: 80
    evidence: 95
    risk: 30
    cost: 45
    source_files:
      - apex-meta/handoff/narm-index-prep-handover.md
    next_action: Create definitions-of-done, artifact plan, validation questions, source map, and workflow prompts.
```
