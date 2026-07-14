# Apex KB Current Research Index — Machine Readable

The YAML block is the machine-readable routing authority for the final-design Deep Research run. It must express the same identity, evidence modes, module routing, and exclusions as file `04`. All repository paths are relative to the declared repository identity.

```yaml
schema: apex.kb.final-design-research-index
repository_identity:
  owner: leela-spec
  name: apexai-os-meta
  full_name: leela-spec/apexai-os-meta
  branch: main
  package_root: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch"
  path_style: repository_relative
current_main_resolution:
  resolve_at_run_start: true
  record_commit: true
  fixed_commit_is_current_authority: false
research_roots:
  package: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch"
  knowledge_base: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase"
  blueprints: "source-knowledge/ProjectRepos"
source_access_contract:
  path_semantics: logical_repository_identity
  physical_wrapper_directories_required: false
  preferred_routes:
    - uploaded_project_sources
    - designated_google_drive_source_roots
    - official_primary_web_documentation
    - explicitly_authorized_github_read_for_specific_gap
  google_drive_source_roots:
    research_and_indexes:
      displayed_root: "KnowledgeBase"
      important_child: "ApexKBFinalDesignDeepResearch"
      logical_prefix: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase"
    apex_kb_skill:
      displayed_root: "apex-kb"
      logical_prefix: ".claude/skills/apex-kb"
    orchestration_design:
      displayed_root: "claude-code-orchestration-design"
      logical_prefix: null
      identity: standalone_source_corpus
    llm_wiki_original:
      displayed_root: "llm-wiki"
      logical_prefix: "source-knowledge/ProjectRepos/llm-wiki"
    llm_wiki_operational:
      displayed_root: "llm-wiki-main"
      logical_prefix: "source-knowledge/ProjectRepos/llm-wiki-main"
    llm_wiki_skill:
      displayed_root: "llm-wiki-skill-main"
      logical_prefix: "source-knowledge/ProjectRepos/llm-wiki-skill-main"
  project_sources_role:
    - git_snapshot_files
    - implementation_files_missing_from_drive
    - repository_level_configuration
  rules:
    - "Do not require a physical apexai-os-meta source root."
    - "Do not require a physical source-knowledge source root."
    - "Record displayed source route and logical identity separately."
    - "Treat Drive and Project Source copies as snapshots unless freshness is established."
    - "Do not count duplicate representations as independent evidence."
mission: >-
  Define one final multifunctional Apex KB architecture that deterministically maps
  the configured corpus, preserves durable concept-to-source intelligence, compiles
  Macro/Meso/Micro knowledge and source atlases, supports configurable execution
  profiles, and materially reduces future AI reading and repeated semantic work.
source_access_routes:
  - github_app_or_connector
  - public_github_main
  - raw_github_main
  - uploaded_project_sources
  - architecture_research_without_apex_implementation
evidence_modes:
  full_repository_evidence:
    implementation_mismatch_allowed: true
  project_source_repository_snapshot:
    record_snapshot_limitations: true
  architecture_research_without_apex_implementation:
    current_mismatch_value: unverified
    continue_research: true
project_source_fallback:
  preserve_repository_relative_identity: true
  never_infer_current_main_from_snapshot: true
authority_order:
  - operator_target_in_00_start_here_and_07_prompt
  - verified_current_main_implementation
  - explicitly_labeled_project_source_snapshot
  - explicit_phase0_and_integration_decisions
  - executed_research_reports
  - llm_wiki_blueprint_implementations
  - claude_skill_and_orchestration_design_evidence
  - external_primary_sources
  - older_research_and_feedback
excluded_roots:
  - path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Failed_Prompts"
    reason: "failed_prompt_outputs_not_design_authority"
  - path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/FailedKBCreation"
    reason: "failed_creation_transcripts_not_design_authority"
excluded_source_classes:
  - standalone_prompt_draft
  - chat_history
  - superseded_draft_plan
  - failed_generation_output
routing_classes:
  shared_authority: "complete at run start when available"
  module_bundle: "complete or targeted inside the active module"
  provenance: "targeted only for disagreement or omitted design recovery"
  excluded: "do not read"
sources:
  - id: R001
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex Phase 0 Corpus Intelligence Implementation Decision.md"
    priority: P0
    read_mode: complete
    role: phase0_product_and_artifact_contract
    use_for: [deterministic_scope, artifact_interfaces, parser_boundary, navigation_report, acceptance]
    caveat: "Reconcile older artifact names and paths with current runtime."
  - id: R002
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex KB × Apex Orchestration Integration Map.md"
    priority: P0
    read_mode: complete
    role: lifecycle_integration_and_ownership_map
    use_for: [macro_architecture, meso_handoffs, micro_interfaces, token_layering, optionality]
    caveat: "The report lacked live repository access; verify implementation claims."
  - id: I001
    path: ".claude/skills/apex-kb/SKILL.md"
    priority: P0
    read_mode: complete
    role: current_operational_authority
    use_for: [routes, lifecycle_states, semantic_rules, completion, instruction_load]
    caveat: "Read current main."
  - id: I002
    path: "apex-meta/scripts/apex_kb.py"
    priority: P0
    read_mode: targeted_complete_functions
    role: current_deterministic_runtime
    use_for: [phase0, ranking, quality, lint, status, postflight, scaffold]
    must_inspect_functions: [cmd_phase0, generic_term_frequency, rank_topic_sources, priority_candidates, phase0_report]
  - id: I003
    path: ".claude/skills/apex-kb/references/semantic-value-contract.md"
    priority: P0
    read_mode: complete
    role: current_semantic_completion_contract
    use_for: [target_queries, source_use, candidate_disposition, independent_acceptance]
    caveat: "Does not independently establish exhaustive corpus discovery."
  - id: I004
    path: ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
    priority: P0
    read_mode: complete
    role: current_phase1_authored_interface
    use_for: [source_analysis, target_query_coverage, dispositions, instruction_cost]
  - id: I005
    path: ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    priority: P0
    read_mode: complete
    role: current_phase2_authored_interface
    use_for: [page_shape, macro_meso_micro, source_use, instruction_cost]
  - id: R003
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/APEX KB — LLM-Wiki Blueprint Capability Map.md"
    priority: P1
    read_mode: complete
    role: blueprint_capability_audit
    use_for: [operations, scripts, data_layout, copy_adapt_omit, missing_capabilities]
  - id: R004
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/markdown-parser-spike-report.md"
    priority: P1
    read_mode: complete
    role: executed_markdown_parser_research
    use_for: [state_machine_parser, output_fields, line_spans, warnings, dependency_choice]
  - id: R005
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Pre-LLMToolStack.md"
    priority: P1
    read_mode: complete
    role: deterministic_tool_value_audit
    use_for: [deterministic_tool_options, setup_cost, token_savings, configurable_reject_or_probe_decisions]
    caveat: "Runtime checks were not the operator Windows environment."
  - id: R006
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Apex Link Graph and Process-Flow Representability Audit.md"
    priority: P1
    read_mode: complete
    role: graph_and_process_edge_audit
    use_for: [path_edges, yaml_edges, process_edges, graph_value_configuration_and_probe_criteria]
  - id: B001
    path: "source-knowledge/ProjectRepos/llm-wiki/llm-wiki.md"
    priority: P1
    read_mode: complete
    role: original_compounding_wiki_vision
    use_for: [product_value, multi_page_ingest, index_first_query, lint, saved_synthesis]
  - id: B002
    path: "source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/SKILL.md"
    priority: P1
    read_mode: complete
    role: operational_llm_wiki_entrypoint
    use_for: [progressive_disclosure, proactive_query, command_routing, hash_idempotency]
  - id: B003
    path: "source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/workflows/ingest.md"
    priority: P1
    read_mode: complete
    role: two_phase_ingest_workflow
    use_for: [source_read, phase1, phase2, contradictions, crosslinks, index_manifest_sentinel]
  - id: B004
    path: "source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/workflows/query.md"
    priority: P1
    read_mode: complete
    role: index_first_query_workflow
    use_for: [page_selection, evidence, gaps, contradictions, save_loop]
  - id: B005
    path: "source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md"
    priority: P1
    read_mode: complete
    role: hierarchical_wiki_skill
    use_for: [typed_tree, compile, ingest, query, lint, audit, source_summaries]
  - id: B006
    path: "source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/references/article-guide.md"
    priority: P1
    read_mode: complete
    role: wiki_page_writing_guide
    use_for: [concept_entity_summary_shapes, splitting, links, contradictions]
    caveat: "Treat word counts as heuristics, never semantic completion gates."
  - id: I006
    path: "apex-meta/scripts/apex_kb_retrieval.py"
    priority: P1
    read_mode: targeted_complete_functions
    role: current_retrieval_runtime
    use_for: [chunking, fts5_probe, lexical_fallback, staleness, query_packets]
  - id: I007
    path: ".claude/skills/apex-kb/references/retrieval-contract.md"
    priority: P1
    read_mode: complete
    role: current_retrieval_contract
    use_for: [canonical_derived_boundary, chunk_fields, stale_policy]
  - id: R007
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Pre-LLM Tool Stack Installability and Value Audit.md"
    priority: P2
    read_mode: targeted
    role: expanded_tool_comparison
    use_for: [dependency_options, install_cost, keep_test_reject]
    caveat: "Contains generating-prompt content; use executed findings only."
  - id: R008
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Pre-LLMCorbusMechanisms_GPT.md"
    priority: P2
    read_mode: targeted
    role: broad_pre_llm_pattern_catalog
    use_for: [ast, static_search, graph, link_validation, external_patterns]
    caveat: "Later Phase 0 decisions supersede tool defaults."
  - id: R009
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/process-flow-graph-audit.md"
    priority: P2
    read_mode: targeted
    role: compact_graph_contract
    use_for: [edge_schema, process_examples]
  - id: R010
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/link-graph.sample.json"
    priority: P2
    read_mode: targeted
    role: graph_fixture
    use_for: [node_schema, edge_schema, fixture_design]
  - id: R011
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/graph-summary.md"
    priority: P2
    read_mode: brief
    role: graph_orientation
    use_for: [hubs, weak_spots]
  - id: R012
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md"
    priority: P2
    read_mode: targeted
    role: retrieval_technical_verifier
    use_for: [token_layers, fts5, bm25, snippets, yaml, staleness, fixtures]
  - id: R013
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md"
    priority: P2
    read_mode: targeted
    role: frontmatter_constraint_correction
    use_for: [parser_options, contamination_prevention]
  - id: R014
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/DR_Apex KB  QueryRetrieval Integration_Final Patch Pack.md"
    priority: P2
    read_mode: targeted
    role: prior_retrieval_patch_design
    use_for: [schema, commands, validation, risk_history]
    caveat: "Predates current code; never apply directly."
  - id: R015
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/FB_DR_RetrievalINtegration_Claude.md"
    priority: P2
    read_mode: targeted
    role: retrieval_patch_critique
    use_for: [collision_risks, assumption_checks]
  - id: R016
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Updates_apex-kb.md"
    priority: P2
    read_mode: targeted
    role: earlier_apex_kb_snapshot
    use_for: [baseline_modes, drift_history, deterministic_semantic_split]
    caveat: "Not current implementation authority."
  - id: B007
    path: "source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/workflows/lint.md"
    priority: P2
    read_mode: targeted
    role: quick_and_semantic_lint_workflow
    use_for: [structural_checks, contradiction_sweep, gap_analysis]
  - id: B008
    path: "source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/WIKI_SCHEMA.md"
    priority: P2
    read_mode: targeted
    role: page_and_index_schema
    use_for: [page_types, index_format, contradiction_format, health_categories]
  - id: B009
    path: "source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/references/schema-guide.md"
    priority: P2
    read_mode: targeted
    role: startup_schema_guidance
    use_for: [scope, naming, current_articles, questions, gaps]
  - id: B010
    path: "source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/scripts/lint_wiki.py"
    priority: P2
    read_mode: targeted
    role: deterministic_lint_blueprint
    use_for: [dead_links, orphans, index_coverage, audit_shape]
  - id: B011
    path: "source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/scripts/scaffold.py"
    priority: P2
    read_mode: targeted
    role: simple_scaffold_blueprint
    use_for: [tree_creation, deterministic_bootstrap_simplification]
  - id: H001
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex_KB_Project_Resource_Index.machine-readable.yaml.md"
    priority: P3
    read_mode: reference
    role: old_research_routing_index
    use_for: [risk_history, supersession_model, per_file_metadata_ideas]
    caveat: "Old paths and priorities are not current."
  - id: H002
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex_KB_Project_Resource_Machine_Readable_Knowledge_Index.md"
    priority: P3
    read_mode: reference
    role: old_machine_index_schema
    use_for: [authority, freshness, relationships, risks, read_order_schema]
    caveat: "Use schema ideas only."
  - id: H003
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/FBClaude4GPT_KBSkillthroughLLMWIKI.md"
    priority: P3
    read_mode: reference
    role: early_skill_packaging_feedback
    use_for: [skill_executability, always_loaded_boundary]
  - id: H004
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM-Wiki_Details&projects.md"
    priority: P3
    read_mode: reference
    role: broader_llm_wiki_repo_survey
    use_for: [alternative_repositories]
    caveat: "External repository claims require revalidation."
  - id: H005
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Apex KB+SQLite FTS5BM25  Implementation Plan.md"
    priority: P3
    read_mode: reference
    role: older_retrieval_implementation_plan
    use_for: [sequencing_history, validation_ideas]
  - id: H006
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CC.md"
    priority: P3
    read_mode: reference
    role: original_retrieval_specification
    use_for: [macro_meso_micro_history]
  - id: H007
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CCv2.md"
    priority: P3
    read_mode: reference
    role: older_retrieval_sequence
    use_for: [implementation_order_history]
  - id: H008
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CCv3.md"
    priority: P3
    read_mode: reference
    role: older_technical_verifier
    use_for: [gap_history, option_matrix]
  - id: H009
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md"
    priority: P3
    read_mode: reference
    role: feasibility_correction
    use_for: [blueprint_gap_history]
    caveat: "Time-sensitive external claims."
  - id: H010
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/KB-Researchv2_gpt.md"
    priority: P3
    read_mode: reference
    role: early_architecture_research
    use_for: [memory_retrieval_history]
  - id: H011
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/KB-Researchv3_gpt.md"
    priority: P3
    read_mode: reference
    role: broader_personal_orchestration_research
    use_for: [domain_boundary_vocabulary]
  - id: H012
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/KB-Researchv3_gpt_FB_claude.md"
    priority: P3
    read_mode: reference
    role: architecture_score_feedback
    use_for: [option_score_corrections]
  - id: H013
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/research2_gem.md"
    priority: P3
    read_mode: reference
    role: provider_option_snapshot
    use_for: [provider_vocabulary_only]
    caveat: "Provider scores are unstable."
shared_authority_sources:
  package: [00, 01, 02, 03, 04, 05, 06, 07]
  current_apex_when_available: [I001, I002, I003, I004, I005, I006, I007]
module_source_bundles:
  deterministic_corpus_intelligence:
    apex: [R001, R002, I002]
    research: [R004, R005, R006, R007, R008, R009, R010, R011]
    llm_wiki: [B001, B002, B003, B005]
    micro_design: [CD001, CD002, CD003]
  semantic_compilation_and_source_atlas:
    apex: [I001, I003, I004, I005]
    research: [R002, R003]
    llm_wiki: [B001, B003, B005, B006, B008, B009]
    micro_design: [CD001, CD002, CD004, CD005]
  retrieval_query_and_maintenance:
    apex: [I006, I007]
    research: [R012, R013, R014, R015, R016]
    llm_wiki: [B004, B007, B008, B010]
    micro_design: [CD001, CD002, CD005]
  configurable_profiles_and_orchestration:
    apex: [I001, I002, I003]
    research: [R002, R003, R005, R006]
    llm_wiki: [B002, B003, B004, B005]
    micro_design: [CD001, CD002, CD003, CD004, CD005, CD006]
micro_design_sources:
  - id: CD001
    path: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md"
    use_for: [file_structure, field_design, micro_creation_patterns]
  - id: CD002
    path: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/agent-skill-orchestration-resilient-workflows.md"
    use_for: [workflow_ownership, resilience, recovery]
  - id: CD003
    path: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/agent-subagent-design-patterns.md"
    use_for: [agent_subagent_boundaries]
  - id: CD004
    path: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/agent-vs-subagent-vs-skill.md"
    use_for: [mechanism_choice]
  - id: CD005
    path: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/commands-hooks-rules-memory-model.md"
    use_for: [commands_hooks_rules_memory]
  - id: CD006
    path: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/apex-application-orchestration-patterns.md"
    use_for: [apex_orchestration_integration]
external_primary_source_rules:
  use_when: "an unstable external fact materially affects a decision"
  prefer: [official_documentation, official_specification, primary_repository]
  separate_fact_inference_recommendation: true
required_reconciliation:
  - "intended_phase0_artifacts_vs_current_runtime_outputs"
  - "complete_candidate_map_vs_top30_ranking"
  - "current_semantic_v2_vs_required_whole_corpus_source_atlas"
  - "blueprint_compounding_value_vs_current_one_summary_per_topic_behavior"
  - "mandatory_instruction_context_vs_tokens_left_for_source_reading_and_writing"
  - "semantic_acceptance_vs_discovery_and_atlas_acceptance"
  - "one_final_architecture_vs_v1_v1_5_deferred_drift"
  - "configuration_axes_vs_separate_product_versions"
  - "github_route_failure_vs_project_source_and_architecture_only_modes"
  - "codex_browser_runtime_ownership_and_save_batches"
  - "micro_file_design_vs_claude_skill_orchestration_evidence"
```
