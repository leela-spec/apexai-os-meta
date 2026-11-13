# Operator Phase 1 Review Decisions — Claude Code Orchestration Design

```yaml
kb_slug: claude-code-orchestration-design
phase: operator_review_after_ingest_phase_1
status: reviewed_policy_direction_recorded
created_at: 2026-07-02
phase_2_allowed: false
required_phase_2_phrase: approve ingest
report_type: operator_decision_log
```

## 1. Scope clarification

These decisions do not mean Apex is building the final orchestration system now.

They are Phase 2 compile-policy decisions for the Claude Code Orchestration Design KB. Their purpose is to tell the next Phase 2 wiki compiler how to represent the ingested knowledge, which claims can become doctrine, and which items remain future implementation work.

Current lifecycle position:

```yaml
current_position:
  deterministic_phase0: complete
  phase1_semantic_ingest: complete
  operator_review: in_progress
  phase2_wiki_compile: blocked_until_approval
  retrieval_indexing_after_phase2: not_yet
```

Important distinction:

```yaml
kb_indexing_and_compilation:
  purpose: create reusable summaries, concept pages, entity pages, contradiction pages, and later retrieval indexes over the compiled KB
  not_the_same_as: building the operational Apex orchestration system

orchestration_system_build:
  purpose: use the compiled KB later as source-grounded design input for actual skills, hooks, workflows, agents, plugins, prompt packs, MCP policies, or runtime files
  timing: after the KB has compiled and indexed the best-practice knowledge
```

## 2. Operator decisions

```yaml
operator_decisions:
  Q001_skill_validation_policy:
    answer: A
    interpretation: target_one_simple_policy_now
    decision: strict_agent_skills_policy_for_canonical_apex_skill_packages
    note: Keep one target for now rather than a two-tier model.

  Q002_hook_or_script_enforcement:
    answer: follow_recommendation
    decision: hard_enforce_high_risk_gates_only
    hard_enforce:
      - phase2_without_approve_ingest
      - write_outside_kb_root
      - raw_source_delete_or_mutation
      - kb_schema_overwrite_without_explicit_flag
      - destructive_archive_delete
    soft_enforce:
      - style
      - terminology
      - preferred source ordering
      - low-risk documentation conventions

  Q003_packaging_surface:
    answer: project_skills_now_plugins_later
    decision: use_project_skills_as_current_reusable_orchestration_surface
    defer:
      - plugins
    note: Plugins remain later packaging work after the project-skill layer stabilizes.

  Q004_subagent_persistence:
    answer: validated
    decision: keep_persistent_subagents_small_and_validated
    persistent_when:
      - repeated domain role
      - stable validation or audit role
      - security-sensitive repo executor with explicit constraints
    ephemeral_when:
      - one-off source scouting
      - temporary comparison reading
      - broad exploration

  Q005_mcp_policy:
    answer: mcp_later
    decision: defer_mcp_policy_and_committed_mcp_json_rules
    current_phase2_treatment: preserve_as_open_question_or_later_policy_page

  Q006_tree_sitter_lsp_repo_maps:
    answer: later
    decision: defer_phase0_v1_5_code_repo_map_extension
    trigger_later_if:
      - code-heavy external repo questions cannot be resolved from Markdown/docs
      - repeated implementation questions require symbol-level repo maps

  Q007_prompt_pack_filesystem:
    answer: validated
    decision: one_prompt_pack_file_per_flow
    convention:
      flow_packet: planning artifact
      prompt_pack: execution prompt artifact
      relationship: flow_packet_points_to_prompt_pack
    note: Do not place execution prompt packs inside Apex KB wiki pages.

  Q008_halt_clarify_file_output_task_closure:
    answer: validated
    decision: apex_wide_minimal_core_with_local_extensions
    globalize:
      - HALT
      - CLARIFY
      - file_output_proof
      - task_closure_proof
      - fetch_back_validation
    local_extensions:
      - promptflow examples
      - flow-pack conventions
      - model-routing details
```

## 3. Phase 2 implications

```yaml
phase2_implications:
  write_as_doctrine:
    - strict_agent_skills_policy_for_canonical_apex_skill_packages
    - project_skills_now_plugins_later
    - one_prompt_pack_file_per_flow
    - apex_wide_minimal_core_for_halt_clarify_and_file_output_proof

  write_as_boundary_or_open_question:
    - exact_hook_enforcement_scope_beyond_high_risk_gates
    - plugin_packaging_timing
    - full_subagent_roster
    - MCP server allowlist and committed .mcp.json policy
    - tree_sitter_lsp_repo_map_extension

  avoid_in_phase2:
    - pretending the operational orchestration system has been built
    - writing runtime hooks/workflows/plugins from this KB compile step
    - turning deferred implementation work into current doctrine
```

## 4. Current gate

Phase 2 remains blocked until the operator says exactly:

```text
approve ingest
```
