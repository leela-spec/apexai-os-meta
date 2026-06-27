# Apex KB Project Resource Machine-Readable Knowledge Index

This document transforms `SourceIndex.md` into a deterministic, schema-driven knowledge index.

It does not re-analyze the Apex KB project, change recommendations, merge files, delete files, or invent new project facts. It preserves the original `Fxx` file identifiers, priorities, read guidance, cluster logic, supersession logic, contamination flags, and next-run instructions, while normalizing the representation into a single parseable YAML structure.

The canonical data lives in the YAML block below. The appendices define the schema, allowed enum values, and validation status so that LLM agents, Python scripts, YAML parsers, JSON conversion tools, and future Deep Research runs can consume the index as a knowledge database rather than as a prose report.


## Canonical YAML Knowledge Index

```yaml
metadata:
  id: IDX001
  version: 1.0.0
  project: Apex KB / Apex-KB_Development
  generated_from: SourceIndex.md
  source_index_title: Apex KB Project Resource Intelligence Index v0.2 — Deep Research Optimized
  purpose: Canonical deterministic machine-readable knowledge index transformed from the existing project resource intelligence index.
  schema_version: apex_resource_index_schema_v1
  created: '2026-06-26'
  updated: '2026-06-26'
  total_files: 38
  total_clusters: 8
  primary_decision_source: F01
  status: representation_transform_only_no_new_research
global_decisions:
  D_NEXT_RUN_MODE:
    id: D_NEXT_RUN_MODE
    status: locked
    authority: binding
    source: IDX001
    description: Use a decision-locked, source-routed Deep Research run, not a broad architecture rediscovery run.
  D_PRIMARY_DECISION_SOURCE:
    id: D_PRIMARY_DECISION_SOURCE
    status: locked
    authority: binding
    source: F01
    description: Apex Phase 0 Corpus Intelligence Implementation Decision.md is the primary binding source for Phase 0.
  D_PHASE0_SCOPE:
    id: D_PHASE0_SCOPE
    status: locked
    authority: binding
    source: F01
    description: Phase 0 is deterministic pre-LLM corpus intelligence that creates navigation artifacts before semantic ingest.
  D_PHASE0_NOT_SCOPE:
    id: D_PHASE0_NOT_SCOPE
    status: locked
    authority: binding
    source: IDX001
    description: Phase 0 does not create a final Apex KB skill, final Python script, repo patch, semantic ingest analysis, wiki page, vector store, or network/LLM call inside the Phase 0 script.
  D_LAYER_BOUNDARY:
    id: D_LAYER_BOUNDARY
    status: locked
    authority: binding
    source: IDX001
    description: 'Apex KB has two layers that must not be collapsed: Phase 0 corpus intelligence and later SQLite FTS5/BM25 retrieval/indexing.'
  D_GENERIC_KB_ROOT:
    id: D_GENERIC_KB_ROOT
    status: locked
    authority: binding
    source: F01
    description: Use a generic --kb-root. claude-skill-design is the first test KB, not a fixed script target.
  D_PARSER_STRATEGY:
    id: D_PARSER_STRATEGY
    status: locked_for_v1
    authority: verified
    source: F02
    description: V1 parser is a simple Python state-machine parser. markdown-it-py is optional for V1.5. Node/remark is deferred.
  D_GRAPH_STRATEGY:
    id: D_GRAPH_STRATEGY
    status: future_v1_5
    authority: verified
    source: F03
    description: Graph extraction is useful but belongs in V1.5 and must parse YAML, path, process, and contract edges rather than only Markdown links or wikilinks.
  D_RETRIEVAL_STRATEGY:
    id: D_RETRIEVAL_STRATEGY
    status: future_v1_5_or_later
    authority: verified
    source: F06
    description: SQLite FTS5/BM25 is valuable later but requires runtime FTS5 probing, BM25 fixtures, safe frontmatter parsing, and derived-artifact discipline.
  D_V1_ARTIFACT_CONTRACT:
    id: D_V1_ARTIFACT_CONTRACT
    status: locked
    authority: binding
    source: F01
    description: V1 artifacts are deterministic navigation aids, not semantic summaries.
  D_TOOL_STACK_STRATEGY:
    id: D_TOOL_STACK_STRATEGY
    status: locked_for_v1
    authority: verified
    source: F04
    description: V1 uses source inventory, rg/Python stdlib, parser maps, keyword hits, topic-file map, priority candidates, and navigation report.
  D_APEX_KB_SKILL_BOUNDARY:
    id: D_APEX_KB_SKILL_BOUNDARY
    status: supporting
    authority: supporting
    source: F05
    description: apex-kb is a source-preserving KB compiler with scaffold, two-phase ingest, query, lint, and audit modes; live repo contents must be reverified before patching.
  D_CLAUDE_NATIVE_PACKAGING_SCOPE:
    id: D_CLAUDE_NATIVE_PACKAGING_SCOPE
    status: later_context
    authority: supporting
    source: F32
    description: Claude-native packaging material is useful later but must not override the Phase 0 corpus-intelligence scope.
  D_PERSONAL_ORCHESTRATION_DOMAIN:
    id: D_PERSONAL_ORCHESTRATION_DOMAIN
    status: locked_boundary
    authority: supporting
    source: F37
    description: Personal orchestration memory is adjacent to project KB and must not be collapsed into project KB.
  D_OUTPUT_CONTRACT:
    id: D_OUTPUT_CONTRACT
    status: recommended_next_run_output
    authority: supporting
    source: IDX001
    description: The next Deep Research run should output validated Phase 0 truth, a populated integration map, a code-ready Phase 0 spec, and optionally a future V1.5 retrieval/graph plan.
  D_NO_ARCHITECTURE_REDISCOVERY:
    id: D_NO_ARCHITECTURE_REDISCOVERY
    status: locked
    authority: binding
    source: IDX001
    description: Do not restart architecture research. Validate and integrate from the existing source spine.
  D_VECTOR_NODE_STATIC_SITE_DEFERRAL:
    id: D_VECTOR_NODE_STATIC_SITE_DEFERRAL
    status: deferred
    authority: binding
    source: IDX001
    description: Vector search, MCP/cloud retrieval, Node/remark, and static-site generation are deferred unless separately authorized.
  RISK_C01_HARDCODED_KB_PATH:
    id: RISK_C01_HARDCODED_KB_PATH
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'claude-skill-design is the fixed script target. Correct rule: Use generic --kb-root; claude-skill-design is first test KB. Appears in: Phase 0 prompt/context. Severity: critical.'
  RISK_C02_WIKI_PAGE_SCOPE_DRIFT:
    id: RISK_C02_WIKI_PAGE_SCOPE_DRIFT
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Phase 0 should create wiki pages. Correct rule: Phase 0 creates navigation artifacts only. Appears in: Older ingest/retrieval framing. Severity: critical.'
  RISK_C03_SEMANTIC_INGEST_SCOPE_DRIFT:
    id: RISK_C03_SEMANTIC_INGEST_SCOPE_DRIFT
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Phase 0 should produce semantic ingest analyses. Correct rule: Semantic ingest belongs later. Appears in: Older apex-kb mode confusion. Severity: critical.'
  RISK_C04_IMMEDIATE_FTS5_SCOPE_DRIFT:
    id: RISK_C04_IMMEDIATE_FTS5_SCOPE_DRIFT
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'SQLite FTS5/BM25 is immediate V1. Correct rule: FTS5 is V1.5/later, with local runtime test. Appears in: Retrieval files. Severity: high.'
  RISK_C05_STDLIB_ONLY_INJECTION:
    id: RISK_C05_STDLIB_ONLY_INJECTION
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Python stdlib-only/no PyYAML was operator-decided. Correct rule: Treat as AI-injected unless operator explicitly decides. Appears in: SQLite/BM25 verifier chain. Severity: high.'
  RISK_C06_REGEX_YAML_OVERTRUST:
    id: RISK_C06_REGEX_YAML_OVERTRUST
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Regex-only YAML parsing is safe. Correct rule: Use strict subset or robust parser; detect malformed frontmatter. Appears in: Older parser/retrieval assumptions. Severity: high.'
  RISK_C07_MARKDOWN_LINK_GRAPH_UNDERCOUNT:
    id: RISK_C07_MARKDOWN_LINK_GRAPH_UNDERCOUNT
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Pure Markdown links are enough for graph. Correct rule: Parse YAML/path/process/contract edges. Appears in: Obsidian-style graph framing. Severity: high.'
  RISK_C08_RUNTIME_EQUALS_WINDOWS:
    id: RISK_C08_RUNTIME_EQUALS_WINDOWS
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Tool availability in runtime equals Windows machine. Correct rule: Verify on C:\GitDev\apexai-os-meta. Appears in: Tool audit. Severity: medium.'
  RISK_C09_PROVIDER_FEATURE_STABILITY:
    id: RISK_C09_PROVIDER_FEATURE_STABILITY
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Current Claude/provider feature scores are stable. Correct rule: Web-verify current provider claims if reused. Appears in: research2_gem.md and orchestration research. Severity: medium.'
  RISK_C10_PATCH_PACK_REPO_VERIFICATION:
    id: RISK_C10_PATCH_PACK_REPO_VERIFICATION
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Patch packs are repo-verified. Correct rule: Re-read live repo before applying. Appears in: Patch packs. Severity: high.'
  RISK_C11_SOUL_HERMES_COPY_DRIFT:
    id: RISK_C11_SOUL_HERMES_COPY_DRIFT
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Old SOUL/Hermes language should be copied. Correct rule: Translate to Claude-native paths only. Appears in: ClaudeSetupGeneral and ClaudePhase1FilePreparation. Severity: medium.'
  RISK_C12_READ_ALL_FILES_AGAIN:
    id: RISK_C12_READ_ALL_FILES_AGAIN
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Deep Research should read every file again. Correct rule: Read prioritized source spine, then topic-specific files. Appears in: Broad prompt variants. Severity: high.'
  RISK_C13_SKELETON_NAV_REPORT:
    id: RISK_C13_SKELETON_NAV_REPORT
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'phase0-navigation-report.md can be a skeleton. Correct rule: phase0-navigation-report.md must contain populated ranked file guidance. Appears in: Future output risk. Severity: critical.'
  RISK_C14_PERSONAL_MEMORY_MIXING:
    id: RISK_C14_PERSONAL_MEMORY_MIXING
    status: active_risk_rule
    authority: supporting
    source: IDX001
    description: 'Personal orchestration memory belongs inside project KB. Correct rule: Keep personal orchestration as adjacent domain, not mixed into project KB. Appears in: Broad memory docs. Severity: medium.'
clusters:
  C1:
    id: C1
    name: phase0_decision_and_contracts
    purpose: Binding Phase 0 scope and artifact contract.
    authority: binding
    priority: P0
    files:
    - F01
    recommended_use: Start here. Extract decisions. Do not reinterpret older research as equal authority.
  C2:
    id: C2
    name: parser_and_markdown_structure_extraction
    purpose: Parser strategy and Markdown structure extraction contract for Phase 0 navigation artifacts.
    authority: verified
    priority: P0
    files:
    - F02
    - F24
    - F07
    recommended_use: Use to write the code-ready parser spec. Do not classify semantic concepts in Phase 0.
  C3:
    id: C3
    name: tool_stack_and_deterministic_pre_llm_mechanisms
    purpose: Local deterministic tools, installability caveats, and pre-LLM corpus mechanism patterns.
    authority: supporting
    priority: P1
    files:
    - F04
    - F15
    - F16
    recommended_use: Use for local-check commands and tool ranking, not as definitive Windows proof.
  C4:
    id: C4
    name: graph_and_process_flow_extraction
    purpose: V1.5 graph extraction policy, schema, hubs, weak spots, and deterministic edge types.
    authority: verified
    priority: P1
    files:
    - F03
    - F12
    - F13
    - F14
    - F25
    recommended_use: Build deterministic graph artifacts later. Do not rely on Markdown links alone.
  C5:
    id: C5
    name: existing_apex_kb_skill_architecture
    purpose: Orientation to existing apex-kb skill modes, package shape, boundaries, and source-preserving KB compiler logic.
    authority: supporting
    priority: P1
    files:
    - F05
    recommended_use: Use as orientation, then verify live repo contents before patching or writing final files.
  C6:
    id: C6
    name: sqlite_fts5_bm25_retrieval_and_architecture_context
    purpose: Later retrieval layer, SQLite FTS5/BM25 risks, implementation sequencing, patch plans, and broad KB architecture background.
    authority: supporting
    priority: P1_P4
    files:
    - F06
    - F08
    - F09
    - F10
    - F11
    - F17
    - F18
    - F19
    - F20
    - F21
    - F22
    - F23
    recommended_use: Use for V1.5 search-index design and future apex-kb retrieval integration, not Phase 0 V1 implementation.
  C7:
    id: C7
    name: prompt_failures_and_anti_contamination
    purpose: Prompt-failure provenance and anti-contamination lessons.
    authority: failure_context
    priority: P4
    files:
    - F26
    - F27
    - F28
    - F29
    - F30
    recommended_use: Use anti-contamination rules; do not read all failed prompts unless debugging prompt design.
  C8:
    id: C8
    name: claude_native_packaging_and_orchestration_context
    purpose: Later Claude-native packaging, skill/orchestration context, personal orchestration domain, and weekly/daily process graph terms.
    authority: supporting
    priority: P2_P4
    files:
    - F31
    - F32
    - F33
    - F34
    - F35
    - F36
    - F37
    - F38
    recommended_use: Use only after Phase 0 output contract is settled, or for graph/process-loop terminology.
files:
- id: F01
  file_name: Apex Phase 0 Corpus Intelligence Implementation Decision.md
  cluster: C1
  priority: P0
  authority: binding
  freshness: current_binding
  value_score: null
  read_order: deep_read
  role: Binding Phase 0 source
  summary: V1/V1.5 artifact contract; no-LLM/no-network/no-wiki; generic script design
  strengths:
  - Binding Phase 0 source
  - V1/V1.5 artifact contract; no-LLM/no-network/no-wiki; generic script design
  weaknesses:
  - Mentions `claude-skill-design`; must remain test KB only
  risks:
  - Mentions `claude-skill-design`; must remain test KB only
  supersedes:
  - F22
  - F18
  - F17
  - F10
  superseded_by: []
  recommended_use: Read first
  implementation_phase: phase0_v1_v1_5_contract
  tags:
  - binding
  - contract
  - deterministic_navigation
  - phase0
  dependencies: []
  related_files: []
- id: F02
  file_name: markdown-parser-spike-report.md
  cluster: C2
  priority: P0
  authority: verified
  freshness: current
  value_score: null
  read_order: deep_read
  role: Parser contract
  summary: Python state-machine parser; fields; failure cases; V1/V1.5 split
  strengths:
  - Parser contract
  - Python state-machine parser; fields; failure cases; V1/V1.5 split
  weaknesses:
  - Sample-based, not full crawl
  risks:
  - Sample-based, not full crawl
  supersedes:
  - F24
  superseded_by: []
  recommended_use: Read first
  implementation_phase: phase0_v1_parser_contract
  tags:
  - frontmatter
  - links
  - markdown_structure
  - parser
  dependencies: []
  related_files:
  - F24
  - F07
- id: F03
  file_name: process-flow-graph-audit.md
  cluster: C4
  priority: P0/P1
  authority: verified
  freshness: current_with_caveat
  value_score: null
  read_order: deep_read
  role: Graph schema
  summary: deterministic edges, hub files, script/LLM boundary
  strengths:
  - Graph schema
  - deterministic edges, hub files, script/LLM boundary
  weaknesses:
  - Not exhaustive local crawl
  risks:
  - Not exhaustive local crawl
  supersedes:
  - F25
  superseded_by: []
  recommended_use: Read first
  implementation_phase: phase0_v1_5_graph_contract
  tags:
  - graph
  - process_flow
  - v1_5
  dependencies: []
  related_files:
  - F12
  - F13
  - F14
  - F25
- id: F04
  file_name: Pre-LLMToolStack.md
  cluster: C3
  priority: P1
  authority: verified
  freshness: current_with_caveat
  value_score: null
  read_order: deep_read
  role: Tool feasibility
  summary: runtime tool checks; V1 stack; installed/missing tools
  strengths:
  - Tool feasibility
  - runtime tool checks; V1 stack; installed/missing tools
  weaknesses:
  - Not operator Windows machine
  risks:
  - Not operator Windows machine
  supersedes: []
  superseded_by: []
  recommended_use: Read first
  implementation_phase: phase0_v1_tool_feasibility
  tags:
  - local_execution
  - pre_llm
  - tool_stack
  dependencies: []
  related_files:
  - F15
  - F16
- id: F05
  file_name: Updates_apex-kb.md
  cluster: C5
  priority: P1
  authority: supporting
  freshness: current_with_caveat
  value_score: null
  read_order: deep_read
  role: Existing apex-kb skill map
  summary: scaffold/ingest/query/lint/audit modes; package shape
  strengths:
  - Existing apex-kb skill map
  - scaffold/ingest/query/lint/audit modes; package shape
  weaknesses:
  - Repo state must be reverified
  risks:
  - Repo state must be reverified
  supersedes: []
  superseded_by: []
  recommended_use: Read first
  implementation_phase: apex_kb_skill_orientation
  tags:
  - apex_kb
  - skill_architecture
  - source_custody
  dependencies: []
  related_files: []
- id: F06
  file_name: Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
  cluster: C6
  priority: P1
  authority: verified
  freshness: current_for_future_retrieval
  value_score: null
  read_order: deep_read_for_retrieval
  role: Retrieval verifier
  summary: FTS5 probe, BM25 vector risks, derived index rule
  strengths:
  - Retrieval verifier
  - FTS5 probe, BM25 vector risks, derived index rule
  weaknesses:
  - Implementation-focused; not Phase 0 binding
  risks:
  - Implementation-focused; not Phase 0 binding
  supersedes:
  - F09
  - F19
  - F20
  - F21
  superseded_by: []
  recommended_use: Read first for retrieval
  implementation_phase: future_retrieval_v1_5_verifier
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies: []
  related_files:
  - F08
  - F09
  - F10
  - F11
  - F17
  - F18
  - F19
  - F20
  - F21
  - F22
  - F23
- id: F07
  file_name: Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
  cluster: C2
  priority: P1
  authority: verified
  freshness: current_with_caveat
  value_score: null
  read_order: targeted_read_parser_policy
  role: Contamination correction
  summary: stdlib-only/PyYAML AI-injection; parser dependency options
  strengths:
  - Contamination correction
  - stdlib-only/PyYAML AI-injection; parser dependency options
  weaknesses:
  - Narrow scope
  risks:
  - Narrow scope
  supersedes:
  - F09
  - F19
  - F20
  - F21
  superseded_by: []
  recommended_use: Read for parser policy
  implementation_phase: parser_dependency_policy_and_retrieval_correction
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies: []
  related_files:
  - F02
  - F24
- id: F08
  file_name: Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
  cluster: C6
  priority: P1
  authority: supporting
  freshness: current_with_caveat
  value_score: null
  read_order: targeted_read_after_F06
  role: Latest retrieval add-on
  summary: newest corrections around retrieval
  strengths:
  - Latest retrieval add-on
  - newest corrections around retrieval
  weaknesses:
  - Add-on, not full plan
  risks:
  - Add-on, not full plan
  supersedes:
  - F09
  - F19
  - F20
  - F21
  superseded_by: []
  recommended_use: Read after GPTv2
  implementation_phase: future_retrieval_v1_5_addon
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies:
  - F06
  related_files:
  - F06
  - F09
  - F10
  - F11
  - F17
  - F18
  - F19
  - F20
  - F21
  - F22
  - F23
- id: F09
  file_name: Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
  cluster: C6
  priority: P2
  authority: supporting
  freshness: superseded_context
  value_score: null
  read_order: targeted_read_later_coding_spec
  role: Retrieval implementation plan
  summary: sequencing, shared DB, preflight, tests
  strengths:
  - Retrieval implementation plan
  - sequencing, shared DB, preflight, tests
  weaknesses:
  - Can pull work into premature implementation
  risks:
  - Can pull work into premature implementation
  supersedes: []
  superseded_by:
  - F06
  - F07
  - F08
  recommended_use: Read if coding spec later
  implementation_phase: future_retrieval_later_implementation_plan
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies: []
  related_files:
  - F06
  - F08
  - F10
  - F11
  - F17
  - F18
  - F19
  - F20
  - F21
  - F22
  - F23
- id: F10
  file_name: DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md
  cluster: C6
  priority: P2
  authority: supporting
  freshness: superseded_context
  value_score: null
  read_order: future_patch_planning
  role: Patch-pack candidate
  summary: retrieval docs, patch surfaces, command contracts
  strengths:
  - Patch-pack candidate
  - retrieval docs, patch surfaces, command contracts
  weaknesses:
  - Repo access partly unverified
  risks:
  - Repo access partly unverified
  supersedes: []
  superseded_by:
  - F01
  recommended_use: Later patch planning only
  implementation_phase: future_patch_planning
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies: []
  related_files:
  - F06
  - F08
  - F09
  - F11
  - F17
  - F18
  - F19
  - F20
  - F21
  - F22
  - F23
- id: F11
  file_name: FB_DR_RetrievalINtegration_Claude.md
  cluster: C6
  priority: P2
  authority: supporting
  freshness: superseded_context
  value_score: null
  read_order: future_patch_planning_pair
  role: Patch critique
  summary: collision risks, feedback, integration corrections
  strengths:
  - Patch critique
  - collision risks, feedback, integration corrections
  weaknesses:
  - Assumption-heavy
  risks:
  - Assumption-heavy
  supersedes: []
  superseded_by: []
  recommended_use: Read with patch pack
  implementation_phase: future_patch_planning_feedback
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies:
  - F10
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F17
  - F18
  - F19
  - F20
  - F21
  - F22
  - F23
- id: F12
  file_name: Apex Link Graph and Process-Flow Representability Audit.md
  cluster: C4
  priority: P1
  authority: verified
  freshness: current_with_caveat
  value_score: null
  read_order: targeted_read_graph_design
  role: Full graph rationale
  summary: why graph is partial/useful; Apex-specific edge types
  strengths:
  - Full graph rationale
  - why graph is partial/useful; Apex-specific edge types
  weaknesses:
  - Sample-based
  risks:
  - Sample-based
  supersedes: []
  superseded_by: []
  recommended_use: Read if graph output design
  implementation_phase: phase0_v1_5_graph_rationale
  tags:
  - graph
  - process_flow
  - v1_5
  dependencies: []
  related_files:
  - F03
  - F13
  - F14
  - F25
- id: F13
  file_name: link-graph.sample.json
  cluster: C4
  priority: P2
  authority: supporting
  freshness: current_with_caveat
  value_score: null
  read_order: schema_reference
  role: Concrete schema
  summary: node/edge schema and graph metadata
  strengths:
  - Concrete schema
  - node/edge schema and graph metadata
  weaknesses:
  - Sample only
  risks:
  - Sample only
  supersedes: []
  superseded_by: []
  recommended_use: Schema reference
  implementation_phase: phase0_v1_5_graph_schema_sample
  tags:
  - graph
  - process_flow
  - v1_5
  dependencies: []
  related_files:
  - F03
  - F12
  - F14
  - F25
- id: F14
  file_name: graph-summary.md
  cluster: C4
  priority: P2
  authority: supporting
  freshness: current_with_caveat
  value_score: null
  read_order: quick_context
  role: Fast graph orientation
  summary: hubs, weak spots, V1.5 output set
  strengths:
  - Fast graph orientation
  - hubs, weak spots, V1.5 output set
  weaknesses:
  - Summary only
  risks:
  - Summary only
  supersedes: []
  superseded_by: []
  recommended_use: Use for quick context
  implementation_phase: phase0_v1_5_graph_summary
  tags:
  - graph
  - process_flow
  - v1_5
  dependencies: []
  related_files:
  - F03
  - F12
  - F13
  - F25
- id: F15
  file_name: Pre-LLM Tool Stack Installability and Value Audit.md
  cluster: C3
  priority: P2
  authority: supporting
  freshness: supporting_context
  value_score: null
  read_order: targeted_read_tool_checks
  role: Tool audit prompt + candidates
  summary: candidate list, Windows local checks, scoring dimensions
  strengths:
  - Tool audit prompt + candidates
  - candidate list, Windows local checks, scoring dimensions
  weaknesses:
  - Mixed prompt/report
  risks:
  - Mixed prompt/report
  supersedes: []
  superseded_by: []
  recommended_use: Use to formulate local checks
  implementation_phase: phase0_v1_tool_audit_prompt
  tags:
  - local_execution
  - pre_llm
  - tool_stack
  dependencies: []
  related_files:
  - F04
  - F16
- id: F16
  file_name: Pre-LLMCorbusMechanisms_GPT.md
  cluster: C3
  priority: P3
  authority: supporting
  freshness: supporting_context
  value_score: null
  read_order: context_only
  role: Pattern library
  summary: MkDocs/mdBook/remark/FTS5 patterns
  strengths:
  - Pattern library
  - MkDocs/mdBook/remark/FTS5 patterns
  weaknesses:
  - Tool patterns not equally applicable
  risks:
  - Tool patterns not equally applicable
  supersedes: []
  superseded_by: []
  recommended_use: Context only
  implementation_phase: phase0_tool_pattern_library
  tags:
  - local_execution
  - pre_llm
  - tool_stack
  dependencies: []
  related_files:
  - F04
  - F15
- id: F17
  file_name: KB-Researchv3_gpt_FB_claude.md
  cluster: C6
  priority: P2/P3
  authority: supporting
  freshness: supporting_context
  value_score: null
  read_order: context_if_scoring_needed
  role: Score correction
  summary: corrected rankings and vector-cost caveats
  strengths:
  - Score correction
  - corrected rankings and vector-cost caveats
  weaknesses:
  - Not binding
  risks:
  - Not binding
  supersedes: []
  superseded_by:
  - F01
  recommended_use: Context if scoring needed
  implementation_phase: architecture_scoring_context
  tags:
  - architecture_research
  - background
  dependencies: []
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F11
  - F18
  - F19
  - F20
  - F21
  - F22
  - F23
- id: F18
  file_name: KB-Researchv3_gpt.md
  cluster: C6
  priority: P3
  authority: historical
  freshness: historical_context
  value_score: null
  read_order: background_only
  role: Broad architecture background
  summary: layered KB/memory model
  strengths:
  - Broad architecture background
  - layered KB/memory model
  weaknesses:
  - May restart architecture debate
  risks:
  - May restart architecture debate
  supersedes: []
  superseded_by:
  - F01
  recommended_use: Background only
  implementation_phase: architecture_background_context
  tags:
  - architecture_research
  - background
  dependencies: []
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F11
  - F17
  - F19
  - F20
  - F21
  - F22
  - F23
- id: F19
  file_name: Apex KB+SQLite FTS5BM25 Implementation Plan.md
  cluster: C6
  priority: P3
  authority: historical
  freshness: superseded_context
  value_score: null
  read_order: contradiction_check_only
  role: Alternate implementation plan
  summary: consistency with CCv2
  strengths:
  - Alternate implementation plan
  - consistency with CCv2
  weaknesses:
  - Duplicate plan
  risks:
  - Duplicate plan
  supersedes: []
  superseded_by:
  - F06
  - F07
  - F08
  recommended_use: Only if contradictions
  implementation_phase: future_retrieval_later_alternate_plan
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies:
  - F09
  - F06
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F11
  - F17
  - F18
  - F20
  - F21
  - F22
  - F23
- id: F20
  file_name: Claude_Apex KB_SQLiteFTS5BM25_CCv3.md
  cluster: C6
  priority: P3
  authority: historical
  freshness: superseded_context
  value_score: null
  read_order: avoid_unless_auditing
  role: Old verifier variant
  summary: audit trail, risk lists
  strengths:
  - Old verifier variant
  - audit trail, risk lists
  weaknesses:
  - contaminated by stdlib-only framing
  risks:
  - contaminated by stdlib-only framing
  supersedes: []
  superseded_by:
  - F06
  - F07
  - F08
  recommended_use: Avoid unless auditing
  implementation_phase: retrieval_audit_trail
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies:
  - F06
  - F07
  - F08
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F11
  - F17
  - F18
  - F19
  - F21
  - F22
  - F23
- id: F21
  file_name: Claude_Apex KB_SQLiteFTS5BM25_CC.md
  cluster: C6
  priority: P4
  authority: obsolete
  freshness: stale
  value_score: null
  read_order: archive_context
  role: Original retrieval spec
  summary: original pipeline concepts
  strengths:
  - Original retrieval spec
  - original pipeline concepts
  weaknesses:
  - superseded; frontmatter/BM25 drift
  risks:
  - superseded; frontmatter/BM25 drift
  supersedes: []
  superseded_by:
  - F06
  - F07
  - F08
  recommended_use: Archive/context
  implementation_phase: historical_retrieval_context
  tags:
  - bm25
  - retrieval
  - sqlite_fts5
  dependencies:
  - F09
  - F06
  - F07
  - F08
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F11
  - F17
  - F18
  - F19
  - F20
  - F22
  - F23
- id: F22
  file_name: KB-Researchv2_gpt.md
  cluster: C6
  priority: P4
  authority: obsolete
  freshness: stale
  value_score: null
  read_order: archive
  role: Older research
  summary: provenance only
  strengths:
  - Older research
  - provenance only
  weaknesses:
  - superseded
  risks:
  - superseded
  supersedes: []
  superseded_by:
  - F01
  recommended_use: Archive
  implementation_phase: historical_kb_research
  tags:
  - architecture_research
  - background
  dependencies: []
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F11
  - F17
  - F18
  - F19
  - F20
  - F21
  - F23
- id: F23
  file_name: research2_gem.md
  cluster: C6
  priority: P4
  authority: obsolete
  freshness: time_sensitive_stale
  value_score: null
  read_order: avoid_unless_web_validating
  role: Provider options
  summary: native/cloud memory vocabulary
  strengths:
  - Provider options
  - native/cloud memory vocabulary
  weaknesses:
  - time-sensitive provider claims
  risks:
  - time-sensitive provider claims
  supersedes: []
  superseded_by: []
  recommended_use: Avoid unless web-validating
  implementation_phase: provider_context_requires_web_validation
  tags:
  - architecture_research
  - background
  dependencies: []
  related_files:
  - F06
  - F08
  - F09
  - F10
  - F11
  - F17
  - F18
  - F19
  - F20
  - F21
  - F22
- id: F24
  file_name: Markdown Structure Parser Spike for Apex KB Phase.md
  cluster: C2
  priority: P3
  authority: historical
  freshness: historical_context
  value_score: null
  read_order: prompt_lesson_only
  role: Parser prompt origin
  summary: sample rules, fake-simulation correction
  strengths:
  - Parser prompt origin
  - sample rules, fake-simulation correction
  weaknesses:
  - prompt wording allowed simulation
  risks:
  - prompt wording allowed simulation
  supersedes: []
  superseded_by:
  - F02
  recommended_use: Use for prompt lesson
  implementation_phase: parser_prompt_origin
  tags:
  - frontmatter
  - links
  - markdown_structure
  - parser
  dependencies: []
  related_files:
  - F02
  - F07
- id: F25
  file_name: CLI_Process_GPT.md
  cluster: C4
  priority: P4
  authority: obsolete
  freshness: superseded_context
  value_score: null
  read_order: avoid
  role: Graph prompt origin
  summary: relation types and task framing
  strengths:
  - Graph prompt origin
  - relation types and task framing
  weaknesses:
  - superseded by graph outputs
  risks:
  - superseded by graph outputs
  supersedes: []
  superseded_by:
  - F03
  recommended_use: Avoid
  implementation_phase: graph_prompt_origin
  tags:
  - graph
  - process_flow
  - v1_5
  dependencies: []
  related_files:
  - F03
  - F12
  - F13
  - F14
- id: F26
  file_name: DR_PromptFinalization2ndTry_v1.md
  cluster: C7
  priority: P4
  authority: obsolete
  freshness: failure_context
  value_score: null
  read_order: avoid
  role: Prompt-failure context
  summary: anti-contamination prompt attempts
  strengths:
  - Prompt-failure context
  - anti-contamination prompt attempts
  weaknesses:
  - superseded
  risks:
  - superseded
  supersedes: []
  superseded_by: []
  recommended_use: Avoid
  implementation_phase: prompt_failure_analysis
  tags:
  - anti_contamination
  - prompt_failure
  dependencies: []
  related_files:
  - F27
  - F28
  - F29
  - F30
- id: F27
  file_name: Anotehr failed DRPromptdesign.md
  cluster: C7
  priority: P4
  authority: failure_context
  freshness: failure_context
  value_score: null
  read_order: delete_or_archive
  role: Failure-only
  summary: none except anti-patterns
  strengths:
  - Failure-only
  - none except anti-patterns
  weaknesses:
  - failure artifact
  risks:
  - failure artifact
  supersedes: []
  superseded_by: []
  recommended_use: Delete/archive
  implementation_phase: prompt_failure_analysis
  tags:
  - anti_contamination
  - prompt_failure
  dependencies: []
  related_files:
  - F26
  - F28
  - F29
  - F30
- id: F28
  file_name: Anotehr failed DRPromptdesign2.md
  cluster: C7
  priority: P4
  authority: failure_context
  freshness: failure_context
  value_score: null
  read_order: delete_or_archive
  role: Failure-only
  summary: none except anti-patterns
  strengths:
  - Failure-only
  - none except anti-patterns
  weaknesses:
  - failure artifact
  risks:
  - failure artifact
  supersedes: []
  superseded_by: []
  recommended_use: Delete/archive
  implementation_phase: prompt_failure_analysis
  tags:
  - anti_contamination
  - prompt_failure
  dependencies: []
  related_files:
  - F26
  - F27
  - F29
  - F30
- id: F29
  file_name: Anotehr failed DRPromptdesign3.md
  cluster: C7
  priority: P4
  authority: failure_context
  freshness: failure_context
  value_score: null
  read_order: delete_or_archive
  role: Failure-only
  summary: none except anti-patterns
  strengths:
  - Failure-only
  - none except anti-patterns
  weaknesses:
  - failure artifact
  risks:
  - failure artifact
  supersedes: []
  superseded_by: []
  recommended_use: Delete/archive
  implementation_phase: prompt_failure_analysis
  tags:
  - anti_contamination
  - prompt_failure
  dependencies: []
  related_files:
  - F26
  - F27
  - F28
  - F30
- id: F30
  file_name: FBGPT_Claude1.md
  cluster: C7
  priority: P4
  authority: failure_context
  freshness: failure_context
  value_score: null
  read_order: archive
  role: Failure feedback
  summary: only if diagnosing prior failed run
  strengths:
  - Failure feedback
  - only if diagnosing prior failed run
  weaknesses:
  - not binding
  risks:
  - not binding
  supersedes: []
  superseded_by: []
  recommended_use: Archive
  implementation_phase: prompt_failure_analysis
  tags:
  - anti_contamination
  - prompt_failure
  dependencies: []
  related_files:
  - F26
  - F27
  - F28
  - F29
- id: F31
  file_name: Apex_Alfred_Skill_Definition_Guide.md
  cluster: C8
  priority: P2
  authority: supporting
  freshness: supporting_context
  value_score: null
  read_order: later_packaging
  role: Skill packaging rules
  summary: SKILL.md anatomy, frontmatter, gates
  strengths:
  - Skill packaging rules
  - SKILL.md anatomy, frontmatter, gates
  weaknesses:
  - not Phase 0-specific
  risks:
  - not Phase 0-specific
  supersedes:
  - F36
  superseded_by: []
  recommended_use: Later packaging
  implementation_phase: later_packaging_skill_rules
  tags:
  - claude_native_packaging
  - orchestration
  dependencies: []
  related_files:
  - F32
  - F33
  - F34
  - F35
  - F36
  - F37
  - F38
- id: F32
  file_name: Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
  cluster: C8
  priority: P2/P3
  authority: supporting
  freshness: supporting_context
  value_score: null
  read_order: packaging_only
  role: Claude-native file flow
  summary: approved paths, four roles, output contract
  strengths:
  - Claude-native file flow
  - approved paths, four roles, output contract
  weaknesses:
  - not KB Phase 0
  risks:
  - not KB Phase 0
  supersedes:
  - F35
  superseded_by: []
  recommended_use: Packaging only
  implementation_phase: later_packaging_claude_native_flow
  tags:
  - claude_native_packaging
  - orchestration
  dependencies: []
  related_files:
  - F31
  - F33
  - F34
  - F35
  - F36
  - F37
  - F38
- id: F33
  file_name: Apex Alfred Orchestration Realization in Claude.md
  cluster: C8
  priority: P3
  authority: historical
  freshness: time_sensitive_context
  value_score: null
  read_order: context_only
  role: Claude-native research
  summary: external Claude docs and orchestration choices
  strengths:
  - Claude-native research
  - external Claude docs and orchestration choices
  weaknesses:
  - needs web revalidation if reused
  risks:
  - needs web revalidation if reused
  supersedes: []
  superseded_by: []
  recommended_use: Context only
  implementation_phase: orchestration_context
  tags:
  - claude_native_packaging
  - orchestration
  dependencies: []
  related_files:
  - F31
  - F32
  - F34
  - F35
  - F36
  - F37
  - F38
- id: F34
  file_name: DR_ApexOrchestrationClaude.md
  cluster: C8
  priority: P3
  authority: historical
  freshness: duplicate_context
  value_score: null
  read_order: use_one_copy_only
  role: Duplicate orchestration research
  summary: same as F33
  strengths:
  - Duplicate orchestration research
  - same as F33
  weaknesses:
  - duplicate
  risks:
  - duplicate
  supersedes: []
  superseded_by: []
  recommended_use: Use one copy only
  implementation_phase: duplicate_orchestration_context
  tags:
  - claude_native_packaging
  - orchestration
  dependencies:
  - F33
  related_files:
  - F31
  - F32
  - F33
  - F35
  - F36
  - F37
  - F38
- id: F35
  file_name: ClaudePhase1FilePreparation.md
  cluster: C8
  priority: P4
  authority: obsolete
  freshness: stale
  value_score: null
  read_order: avoid
  role: Old conversion map
  summary: SOUL/SKILL mapping history
  strengths:
  - Old conversion map
  - SOUL/SKILL mapping history
  weaknesses:
  - stale SOUL framing
  risks:
  - stale SOUL framing
  supersedes: []
  superseded_by:
  - F32
  recommended_use: Avoid
  implementation_phase: historical_conversion_context
  tags:
  - claude_native_packaging
  - orchestration
  dependencies: []
  related_files:
  - F31
  - F32
  - F33
  - F34
  - F36
  - F37
  - F38
- id: F36
  file_name: ClaudeSetupGeneral.md
  cluster: C8
  priority: P4
  authority: obsolete
  freshness: stale
  value_score: null
  read_order: avoid
  role: Early setup context
  summary: old questions and assumptions
  strengths:
  - Early setup context
  - old questions and assumptions
  weaknesses:
  - stale
  risks:
  - stale
  supersedes: []
  superseded_by:
  - F31
  recommended_use: Avoid
  implementation_phase: historical_setup_context
  tags:
  - claude_native_packaging
  - orchestration
  dependencies: []
  related_files:
  - F31
  - F32
  - F33
  - F34
  - F35
  - F37
  - F38
- id: F37
  file_name: PersonalOrchestrationProcessFlow.md
  cluster: C8
  priority: P2/P3
  authority: supporting
  freshness: supporting_context
  value_score: null
  read_order: context_domain_separation
  role: Personal orchestration artifact system
  summary: separate personal memory domain; flow/prompt-pack/status loop
  strengths:
  - Personal orchestration artifact system
  - separate personal memory domain; flow/prompt-pack/status loop
  weaknesses:
  - can be confused with KB scope
  risks:
  - can be confused with KB scope
  supersedes: []
  superseded_by: []
  recommended_use: Context for domain separation
  implementation_phase: personal_orchestration_context
  tags:
  - personal_orchestration
  - routine_loop
  dependencies: []
  related_files:
  - F31
  - F32
  - F33
  - F34
  - F35
  - F36
  - F38
- id: F38
  file_name: WeeklyRoutine_Overview_Marco&Meso.md
  cluster: C8
  priority: P2/P3
  authority: supporting
  freshness: supporting_context
  value_score: null
  read_order: context_graph_process_terms
  role: Routine/process graph context
  summary: PreCapWeek → PreCapNextDay → FlowRecap → APSU chain
  strengths:
  - Routine/process graph context
  - PreCapWeek → PreCapNextDay → FlowRecap → APSU chain
  weaknesses:
  - not KB authority
  risks:
  - not KB authority
  supersedes: []
  superseded_by: []
  recommended_use: Context for graph/process terms
  implementation_phase: process_graph_context
  tags:
  - graph
  - personal_orchestration
  - process_flow
  - routine_loop
  - v1_5
  dependencies: []
  related_files:
  - F31
  - F32
  - F33
  - F34
  - F35
  - F36
  - F37
reading_strategies:
  deep_research_80_20:
    phase_a_deep_read_always:
      files:
      - F01
      - F02
      - F03
      - F04
      - F05
      - F06
      purpose: Read deeply, always.
    phase_b_selective:
      files:
      - F07
      - F08
      - F09
      - F10
      - F11
      - F12
      - F13
      - F14
      purpose: Read selectively when topic-relevant.
    phase_c_context_only:
      files:
      - F18
      - F17
      - F16
      - F32
      - F37
      - F38
      - F33
      - F34
      purpose: Use as context only.
    phase_d_avoid_unless_failure_analysis:
      files:
      - F27
      - F28
      - F29
      - F26
      - F30
      - F25
      - F36
      - F35
      - F23
      - F22
      - F21
      purpose: Avoid unless doing failure analysis, provenance checks, or explicit web validation.
  topic_to_file_routing:
    phase0_corpus_intelligence:
      read_first:
      - F01
      - F02
      - F04
      extract:
      - V1 artifacts and required schemas
      - V1.5 deferrals
      - no semantic ingest / no wiki / no vector boundaries
      - generic --kb-root script rule
      avoid:
      - SQLite implementation plans as scope authority
      - old architecture research as equal authority
    v1_artifact_contract:
      read_first:
      - F01
      output_artifacts:
      - corpus-profile.md
      - heading-map.json
      - markdown-link-map.json
      - frontmatter-map.json
      - keyword-hits.ndjson
      - topic-file-map.json
      - source-priority-candidates.md
      - phase0-navigation-report.md
      key_rule: Artifacts are deterministic navigation aids, not semantic summaries.
    markdown_parser:
      read_first:
      - F02
      read_second:
      - F24
      - F07
      extract:
      - Python state-machine parser as V1
      - fence tracking
      - frontmatter detection
      - markdown links
      - wikilinks
      - code block boundaries
      - parser warnings
      avoid:
      - simulated parser results
      - semantic concept classification
    pre_llm_tool_stack:
      read_first:
      - F04
      - F15
      read_second:
      - F16
      extract:
      - git/rg/Python stdlib as V1
      - markdown-it-py as V1.5
      - SQLite FTS5 test as V1.5
      - Node/static-site tooling deferred
      caution:
      - runtime was not operator Windows machine
    graph_extraction:
      read_first:
      - F03
      - F12
      - F13
      read_second:
      - F14
      - F38
      extract:
      - explicit_file_reference
      - yaml_path_reference
      - process_sequence
      - contract_dependency
      - owns / hands_off_to / does_not_own
      - hub files and missing nodes
      avoid:
      - pure Obsidian interpretation
      - semantic edges invented by the LLM
    apex_kb_existing_skill:
      read_first:
      - F05
      read_second:
      - F10
      - F11
      extract:
      - current apex-kb modes
      - source custody
      - two-phase ingest
      - query/lint/audit boundaries
      - existing package layout
      mandatory_followup:
      - verify against live repo before patching
    sqlite_fts5_bm25_retrieval:
      read_first:
      - F06
      - F07
      read_second:
      - F08
      - F09
      - F19
      extract:
      - runtime FTS5 probe
      - BM25 vector/schema fixtures
      - search.sqlite as derived
      - frontmatter parser correction
      - .gitignore before first DB build
      avoid:
      - treating retrieval as immediate Phase 0 V1 requirement
    claude_native_packaging:
      read_first:
      - F32
      - F31
      read_second:
      - F33
      - F34
      extract:
      - approved Claude-native paths
      - four permanent roles
      - skill/frontmatter style
      - no Hermes/SOUL drift
      avoid:
      - using these to override Phase 0 corpus-intelligence scope
    personal_orchestration_domain:
      read_first:
      - F37
      - F38
      extract:
      - personal orchestration as adjacent domain
      - PreCap/FlowRecap/status loop terms
      - artifact chain for graph context
      avoid:
      - collapsing personal orchestration into project KB
  later_deep_research_output_contract:
    output_A:
      name: validated_phase0_truth
      must_include:
      - binding decisions
      - superseded decisions
      - hardcoded path corrections
      - repo-truth checks still needed
      - no architecture rediscovery
    output_B:
      name: populated_integration_map
      must_include:
      - corpus-profile.md
      - heading-map.json
      - markdown-link-map.json
      - frontmatter-map.json
      - keyword-hits.ndjson
      - topic-file-map.json
      - source-priority-candidates.md
      - phase0-navigation-report.md
      - V1.5 search-index fallback
      - V1.5 graph files
      forbidden:
      - empty skeleton table
      - semantic claims without source
    output_C:
      name: code_ready_phase0_spec
      must_include:
      - CLI arguments
      - --kb-root generic behavior
      - input files
      - output schemas
      - parser state machine
      - keyword groups
      - source-priority candidate heuristics
      - error handling
      - Windows PowerShell examples
      - acceptance tests
    output_D_optional:
      name: future_v1_5_retrieval_and_graph_plan
      must_include:
      - FTS5 runtime probe
      - search-index.sqlite or JSON/NDJSON fallback
      - link graph schema
      - process graph schema
      - frontmatter parser upgrade option
      - explicit deferral of vector search
  final_next_prompt_strategy:
    mission: create validated, code-ready Phase 0 corpus intelligence specification
    do_not_create:
    - final Apex KB skill
    - final scripts
    - repo patches
    - wiki pages
    - semantic ingest analyses
    - vector stores
    binding_rules:
    - Newest explicit decision wins.
    - Operator instruction overrides AI output.
    - Apex Phase 0 decision file is primary authority.
    - Phase 0 is deterministic pre-LLM navigation.
    - Phase 0 creates artifacts, not wiki pages or semantic analyses.
    - Use generic --kb-root; do not hardcode claude-skill-design.
    - V1 uses source inventory, rg/Python stdlib, parser maps, keyword hits, topic file map, priority candidates, and navigation report.
    - V1.5 may add FTS5/search fallback and graph artifacts.
    - Vector search, MCP/cloud retrieval, Node/remark, and static-site generation are deferred unless separately authorized.
    v1_artifacts:
    - corpus-profile.md
    - heading-map.json
    - markdown-link-map.json
    - frontmatter-map.json
    - keyword-hits.ndjson
    - topic-file-map.json
    - source-priority-candidates.md
    - phase0-navigation-report.md
    v1_5_artifacts:
    - search-index.sqlite or JSON/NDJSON fallback
    - link-graph.json
    - graph-summary.md
    - process-flow-graph-audit.md
relationships:
- source: C1
  relation: contains_file
  target: F01
  evidence: source_cluster_map
  note: null
- source: C2
  relation: contains_file
  target: F02
  evidence: source_cluster_map
  note: null
- source: C2
  relation: contains_file
  target: F24
  evidence: source_cluster_map
  note: null
- source: C2
  relation: contains_file
  target: F07
  evidence: source_cluster_map
  note: null
- source: C3
  relation: contains_file
  target: F04
  evidence: source_cluster_map
  note: null
- source: C3
  relation: contains_file
  target: F15
  evidence: source_cluster_map
  note: null
- source: C3
  relation: contains_file
  target: F16
  evidence: source_cluster_map
  note: null
- source: C4
  relation: contains_file
  target: F03
  evidence: source_cluster_map
  note: null
- source: C4
  relation: contains_file
  target: F12
  evidence: source_cluster_map
  note: null
- source: C4
  relation: contains_file
  target: F13
  evidence: source_cluster_map
  note: null
- source: C4
  relation: contains_file
  target: F14
  evidence: source_cluster_map
  note: null
- source: C4
  relation: contains_file
  target: F25
  evidence: source_cluster_map
  note: null
- source: C5
  relation: contains_file
  target: F05
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F06
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F08
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F09
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F10
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F11
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F17
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F18
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F19
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F20
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F21
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F22
  evidence: source_cluster_map
  note: null
- source: C6
  relation: contains_file
  target: F23
  evidence: source_cluster_map
  note: null
- source: C7
  relation: contains_file
  target: F26
  evidence: source_cluster_map
  note: null
- source: C7
  relation: contains_file
  target: F27
  evidence: source_cluster_map
  note: null
- source: C7
  relation: contains_file
  target: F28
  evidence: source_cluster_map
  note: null
- source: C7
  relation: contains_file
  target: F29
  evidence: source_cluster_map
  note: null
- source: C7
  relation: contains_file
  target: F30
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F31
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F32
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F33
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F34
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F35
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F36
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F37
  evidence: source_cluster_map
  note: null
- source: C8
  relation: contains_file
  target: F38
  evidence: source_cluster_map
  note: null
- source: F01
  relation: supersedes
  target: F22
  evidence: supersession_map.phase0_scope
  note: Phase 0 scope supersedes KB-Researchv2_gpt.md.
- source: F01
  relation: supersedes_scope_where_broadened
  target: F18
  evidence: supersession_map.phase0_scope
  note: Supersedes KB-Researchv3_gpt.md where it broadens scope.
- source: F01
  relation: supersedes_scope_where_broadened
  target: F17
  evidence: supersession_map.phase0_scope
  note: Supersedes KB-Researchv3_gpt_FB_claude.md where it broadens scope.
- source: F01
  relation: supersedes_immediate_implementation_implication
  target: F10
  evidence: supersession_map.phase0_scope
  note: Supersedes retrieval patch packs where they imply immediate implementation.
- source: F02
  relation: supersedes_prompt_wording_when_simulated
  target: F24
  evidence: supersession_map.parser
  note: 'Current rule: attempt bounded execution; do not simulate parser results.'
- source: F03
  relation: supersedes
  target: F25
  evidence: supersession_map.graph
  note: Graph belongs in V1.5 and must parse Apex-specific path/YAML/process edges.
- source: F12
  relation: supports
  target: F03
  evidence: source_cluster_map.C4
  note: Full graph rationale supports focused graph artifact.
- source: F06
  relation: partly_supersedes
  target: F09
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F06
  relation: partly_supersedes
  target: F19
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F06
  relation: partly_supersedes
  target: F20
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F06
  relation: partly_supersedes
  target: F21
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F07
  relation: partly_supersedes
  target: F09
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F07
  relation: partly_supersedes
  target: F19
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F07
  relation: partly_supersedes
  target: F20
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F07
  relation: partly_supersedes
  target: F21
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F08
  relation: partly_supersedes
  target: F09
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F08
  relation: partly_supersedes
  target: F19
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F08
  relation: partly_supersedes
  target: F20
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F08
  relation: partly_supersedes
  target: F21
  evidence: supersession_map.retrieval
  note: Use current retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
- source: F32
  relation: supersedes
  target: F35
  evidence: supersession_map.claude_packaging
  note: Supersedes where SOUL/Hermes framing conflicts.
- source: F31
  relation: supersedes
  target: F36
  evidence: supersession_map.claude_packaging
  note: Current packaging guide supersedes early setup context for packaging.
- source: F33
  relation: duplicates_or_overlaps
  target: F34
  evidence: file_index.F34
  note: Use one copy only.
- source: F13
  relation: schema_for
  target: F03
  evidence: file_index.F13
  note: Concrete graph sample schema for graph/process artifact.
- source: F14
  relation: summarizes
  target: F12
  evidence: file_index.F14
  note: Fast graph orientation for full graph rationale.
- source: F37
  relation: context_for
  target: F38
  evidence: file_index.F37_F38
  note: Personal orchestration domain and routine loop process terms are related context files.
- source: F06
  relation: supports_future_retrieval_plan
  target: F01
  evidence: executive_verdict
  note: Retrieval is valuable later but not immediate Phase 0 V1.
- source: D_PRIMARY_DECISION_SOURCE
  relation: supported_by
  target: F01
  evidence: global_decisions.source
  note: null
- source: D_PHASE0_SCOPE
  relation: supported_by
  target: F01
  evidence: global_decisions.source
  note: null
- source: D_GENERIC_KB_ROOT
  relation: supported_by
  target: F01
  evidence: global_decisions.source
  note: null
- source: D_PARSER_STRATEGY
  relation: supported_by
  target: F02
  evidence: global_decisions.source
  note: null
- source: D_GRAPH_STRATEGY
  relation: supported_by
  target: F03
  evidence: global_decisions.source
  note: null
- source: D_RETRIEVAL_STRATEGY
  relation: supported_by
  target: F06
  evidence: global_decisions.source
  note: null
- source: D_V1_ARTIFACT_CONTRACT
  relation: supported_by
  target: F01
  evidence: global_decisions.source
  note: null
- source: D_TOOL_STACK_STRATEGY
  relation: supported_by
  target: F04
  evidence: global_decisions.source
  note: null
- source: D_APEX_KB_SKILL_BOUNDARY
  relation: supported_by
  target: F05
  evidence: global_decisions.source
  note: null
- source: D_CLAUDE_NATIVE_PACKAGING_SCOPE
  relation: supported_by
  target: F32
  evidence: global_decisions.source
  note: null
- source: D_PERSONAL_ORCHESTRATION_DOMAIN
  relation: supported_by
  target: F37
  evidence: global_decisions.source
  note: null
- source: D_PHASE0_SCOPE
  relation: constrains
  target: D_RETRIEVAL_STRATEGY
  evidence: global_decisions
  note: Retrieval must not become immediate Phase 0 V1.
- source: D_PHASE0_SCOPE
  relation: constrains
  target: D_CLAUDE_NATIVE_PACKAGING_SCOPE
  evidence: global_decisions
  note: Packaging context must not override Phase 0 corpus-intelligence scope.
- source: D_GENERIC_KB_ROOT
  relation: mitigates
  target: RISK_C01_HARDCODED_KB_PATH
  evidence: contamination_audit
  note: null
- source: D_GRAPH_STRATEGY
  relation: mitigates
  target: RISK_C07_MARKDOWN_LINK_GRAPH_UNDERCOUNT
  evidence: contamination_audit
  note: null
- source: D_RETRIEVAL_STRATEGY
  relation: mitigates
  target: RISK_C04_IMMEDIATE_FTS5_SCOPE_DRIFT
  evidence: contamination_audit
  note: null
- source: D_PERSONAL_ORCHESTRATION_DOMAIN
  relation: mitigates
  target: RISK_C14_PERSONAL_MEMORY_MIXING
  evidence: contamination_audit
  note: null
```

## Schema Appendix

```yaml
schema_appendix:
  root:
    type: object
    required_sections:
    - metadata
    - global_decisions
    - clusters
    - files
    - reading_strategies
    - relationships
    section_count: 6
  metadata:
    type: object
    purpose: Describes the index itself, not the project content.
    required_fields:
    - id
    - version
    - project
    - generated_from
    - source_index_title
    - purpose
    - schema_version
    - created
    - updated
    - total_files
    - total_clusters
    - primary_decision_source
    - status
  global_decision:
    type: object_map
    key: decision_id
    required_fields:
    - id
    - status
    - authority
    - source
    - description
  cluster:
    type: object_map
    key: cluster_id
    required_fields:
    - id
    - name
    - purpose
    - authority
    - priority
    - files
    - recommended_use
  file:
    type: array_item
    key: id
    required_fields:
    - id
    - file_name
    - cluster
    - priority
    - authority
    - freshness
    - value_score
    - read_order
    - role
    - summary
    - strengths
    - weaknesses
    - risks
    - supersedes
    - superseded_by
    - recommended_use
    - implementation_phase
    - tags
    - dependencies
    - related_files
    field_definitions:
      id: Stable file identifier from the original index.
      file_name: Exact file name as represented in the original index.
      cluster: Cluster ID from the canonical cluster map.
      priority: Original priority value from the index.
      authority: Normalized authority enum.
      freshness: Normalized freshness enum.
      value_score: Numeric value score when present in the original source; null when no numeric value score exists in v0.2.
      read_order: Normalized machine-readable read-order enum.
      role: Primary purpose/main value from the original table.
      summary: What Deep Research should find there, preserved from the original table.
      strengths: Structured representation of main value and extractable value.
      weaknesses: Structured risk/contamination caveat, null when unknown.
      risks: Structured risk list, null when unknown.
      supersedes: List of file IDs this file supersedes, derived only from supersession statements.
      superseded_by: List of file IDs that supersede this file, derived only from supersession statements.
      recommended_use: Original use verdict string.
      implementation_phase: Normalized phase/use bucket.
      tags: Search tags derived from original cluster/topic labels.
      dependencies: File IDs that should be read first when explicitly implied by read guidance.
      related_files: Other file IDs in the same canonical cluster.
  reading_strategies:
    type: object
    purpose: Structured read-order and topic-routing guidance converted from prose/tables/YAML-like blocks.
  relationship:
    type: array_item
    required_fields:
    - source
    - relation
    - target
    - evidence
    - note
    id_reference_rule: source and target must reference a valid metadata id, decision id, cluster id, or file id.
```

## Enum Appendix

```yaml
enum_appendix:
  priority:
  - P0
  - P0/P1
  - P1
  - P2
  - P2/P3
  - P3
  - P4
  authority:
  - binding
  - failure_context
  - historical
  - obsolete
  - supporting
  - verified
  freshness:
  - current
  - current_binding
  - current_for_future_retrieval
  - current_with_caveat
  - duplicate_context
  - failure_context
  - historical_context
  - stale
  - superseded_context
  - supporting_context
  - time_sensitive_context
  - time_sensitive_stale
  read_order:
  - archive
  - archive_context
  - avoid
  - avoid_unless_auditing
  - avoid_unless_web_validating
  - background_only
  - context_domain_separation
  - context_graph_process_terms
  - context_if_scoring_needed
  - context_only
  - contradiction_check_only
  - deep_read
  - deep_read_for_retrieval
  - delete_or_archive
  - future_patch_planning
  - future_patch_planning_pair
  - later_packaging
  - packaging_only
  - prompt_lesson_only
  - quick_context
  - schema_reference
  - targeted_read_after_F06
  - targeted_read_graph_design
  - targeted_read_later_coding_spec
  - targeted_read_parser_policy
  - targeted_read_tool_checks
  - use_one_copy_only
  implementation_phase:
  - apex_kb_skill_orientation
  - architecture_background_context
  - architecture_scoring_context
  - duplicate_orchestration_context
  - future_patch_planning
  - future_patch_planning_feedback
  - future_retrieval_later_alternate_plan
  - future_retrieval_later_implementation_plan
  - future_retrieval_v1_5_addon
  - future_retrieval_v1_5_verifier
  - graph_prompt_origin
  - historical_conversion_context
  - historical_kb_research
  - historical_retrieval_context
  - historical_setup_context
  - later_packaging_claude_native_flow
  - later_packaging_skill_rules
  - orchestration_context
  - parser_dependency_policy_and_retrieval_correction
  - parser_prompt_origin
  - personal_orchestration_context
  - phase0_tool_pattern_library
  - phase0_v1_5_graph_contract
  - phase0_v1_5_graph_rationale
  - phase0_v1_5_graph_schema_sample
  - phase0_v1_5_graph_summary
  - phase0_v1_parser_contract
  - phase0_v1_tool_audit_prompt
  - phase0_v1_tool_feasibility
  - phase0_v1_v1_5_contract
  - process_graph_context
  - prompt_failure_analysis
  - provider_context_requires_web_validation
  - retrieval_audit_trail
  decision_status:
  - active_risk_rule
  - deferred
  - future_v1_5
  - future_v1_5_or_later
  - later_context
  - locked
  - locked_boundary
  - locked_for_v1
  - recommended_next_run_output
  - supporting
  relationship:
  - constrains
  - contains_file
  - context_for
  - duplicates_or_overlaps
  - mitigates
  - partly_supersedes
  - schema_for
  - summarizes
  - supersedes
  - supersedes_immediate_implementation_implication
  - supersedes_prompt_wording_when_simulated
  - supersedes_scope_where_broadened
  - supported_by
  - supports
  - supports_future_retrieval_plan
  contamination_severity:
  - critical
  - high
  - medium
  null_policy: Use null only when the source index does not contain a value and adding one would invent metadata.
```

## Validation Checklist

```yaml
validation_checklist:
  every_file_has_unique_id: pass
  every_cluster_has_unique_id: pass
  every_relationship_references_valid_ids: pass
  every_cluster_file_reference_is_valid: pass
  every_file_is_assigned_to_exactly_one_cluster: pass
  every_file_object_uses_canonical_schema: pass
  total_files_preserved: 38
  total_clusters_preserved: 8
  no_markdown_tables_in_output: pass
  no_new_research_performed: pass
  scores_changed: 'no'
  numeric_value_scores_in_source_v0_2: not_present
  value_score_policy: set_to_null_for_all_files_because_v0_2_contains priorities but no numeric value_score field
  information_loss_assessment: pass_best_effort_representation_transform
  notes:
  - All 38 Fxx records from the SourceIndex.md file-by-file operational index are represented.
  - Original priority and use-verdict strings are preserved as priority and recommended_use.
  - Normalized fields add parser-friendly enums without changing the preserved source values.
  - Relationships are derived from explicit cluster, read-spine, and supersession statements in the source index.
```
