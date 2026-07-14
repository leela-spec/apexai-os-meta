# Apex KB Current Research Index — Machine Readable

The YAML block is the routing authority for the final-design Deep Research run. Paths are repository-relative and contain no local-drive dependency.

```yaml
schema: apex.kb.final-design-research-index.v1
snapshot:
  date: "2026-07-14"
  implementation_commit: "d72f07f7b598"
  implementation_branch: "main"
  research_root: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase"
  blueprint_root: "source-knowledge/ProjectRepos"
mission: >-
  Define the smallest resilient Apex KB lifecycle that deterministically maps the
  complete scoped corpus and lets an LLM compile a Macro/Meso/Micro concept dossier
  plus a complete per-source atlas that materially reduces future AI reading.
authority_order:
  - operator_target_in_00_start_here
  - current_main_implementation
  - explicit_phase0_and_integration_decisions
  - executed_research_reports
  - local_blueprint_implementations
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
priority_definitions:
  P0: "complete read; binding decision or current implementation truth"
  P1: "complete read; executed research or direct implementation blueprint"
  P2: "targeted read for a named decision"
  P3: "provenance/reference only"
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
    use_for: [minimal_tool_stack, setup_cost, token_savings, deferrals]
    caveat: "Runtime checks were not the operator Windows environment."
  - id: R006
    path: "FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Apex Link Graph and Process-Flow Representability Audit.md"
    priority: P1
    read_mode: complete
    role: graph_and_process_edge_audit
    use_for: [path_edges, yaml_edges, process_edges, graph_optionality]
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
    use_for: [tree_creation, minimal_bootstrap]
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
decision_routes:
  deterministic_phase0:
    start: [R001, R002, I002]
    expand: [R004, R005, R006, R007, R008]
  semantic_compilation:
    start: [I001, I003, I004, I005, B001, B003, B005, B006]
    validate_against: [R003]
  retrieval:
    start: [I006, I007]
    expand: [R012, R013, R014, R015]
  token_and_instruction_efficiency:
    start: [R002, B002, B004, B005]
    inspect_current: [I001, I004, I005]
required_reconciliation:
  - "intended_phase0_artifacts_vs_current_runtime_outputs"
  - "complete_candidate_map_vs_top30_ranking"
  - "current_semantic_v2_vs_required_whole_corpus_source_atlas"
  - "blueprint_compounding_value_vs_current_one_summary_per_topic_behavior"
  - "mandatory_instruction_context_vs_tokens_left_for_source_reading_and_writing"
  - "semantic_acceptance_vs_discovery_and_atlas_acceptance"
```
