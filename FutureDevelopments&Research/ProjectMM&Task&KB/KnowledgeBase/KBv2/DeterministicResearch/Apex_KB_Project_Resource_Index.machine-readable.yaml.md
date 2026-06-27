project_index:
  id: apex_kb_project_resource_intelligence_index_v0_2_machine_readable
  title: Apex KB Project Resource Intelligence Index v0.2 — Deep Research Optimized
  source_document: SourceIndex.md
  executive_verdict:
    best_next_run_strategy: Use a decision-locked, source-routed Deep Research run, not a broad architecture rediscovery run.
    primary_source:
      file: Apex Phase 0 Corpus Intelligence Implementation Decision.md
      role: binding source for Phase 0
      reason: Locks the task as deterministic pre-LLM corpus intelligence, with navigation artifacts before semantic ingest.
    main_system_spine: Phase 0 decision → parser spike → tool audit → graph audit → apex-kb detective analysis → retrieval
      verifier
    most_important_distinction:
      apex_kb_layers_must_not_be_collapsed:
      - layer: Phase 0 corpus intelligence
        meaning: deterministic maps and navigation artifacts
      - layer: Later retrieval/indexing
        meaning: SQLite FTS5/BM25 and query surfaces
    biggest_confusion_risk: Older retrieval implementation files can pull the next run into premature patching before the
      Phase 0 artifact contract is validated.
    biggest_contamination_risk: Treating claude-skill-design as a hardcoded script target instead of the first test KB behind
      a generic --kb-root.
    parser_decision: V1 should use a simple Python state-machine parser; markdown-it-py is V1.5 optional; Node/remark is deferred.
    graph_decision: Graph extraction is useful but belongs in V1.5 and must parse YAML/path/process edges, not just Markdown
      links or wikilinks.
    retrieval_decision: SQLite FTS5/BM25 is valuable later, but needs runtime FTS5 probing, BM25 fixtures, safe frontmatter
      parsing, and “derived artifact, not source of truth” discipline.
    read_order_optimization: The next Deep Research should read roughly 8–12 files deeply, not all 38 equally. The old index
      already marked read-first and stale files; this v0.2 converts that into a stronger routing map.
  corpus_overview:
    total_files_indexed: 38
    index_goal: Make the next Deep Research run source-efficient by telling it exactly which files to read for each decision,
      what each file contributes, and which files are stale, duplicate, or contamination-prone.
    canonical_current_scope:
      phase: Phase 0 deterministic corpus intelligence
      not_scope:
      - final Apex KB skill generation
      - final Python script creation
      - repo patching
      - semantic ingest analysis
      - wiki page generation
      - vector store creation
      - network/LLM calls inside Phase 0 script
    primary_source:
      file: Apex Phase 0 Corpus Intelligence Implementation Decision.md
      priority: P0
      authority: binding
      reason: Locks Phase 0 as deterministic pre-LLM corpus intelligence and defines V1/V1.5 artifacts, script boundaries,
        parser choices, and deferrals.
    best_read_spine:
      phase0_contract:
      - Apex Phase 0 Corpus Intelligence Implementation Decision.md
      parser_contract:
      - markdown-parser-spike-report.md
      - Markdown Structure Parser Spike for Apex KB Phase.md
      tool_feasibility:
      - Pre-LLMToolStack.md
      - Pre-LLM Tool Stack Installability and Value Audit.md
      graph_contract:
      - Apex Link Graph and Process-Flow Representability Audit.md
      - process-flow-graph-audit.md
      - link-graph.sample.json
      - graph-summary.md
      apex_kb_existing_skill:
      - Updates_apex-kb.md
      retrieval_later:
      - Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
      - Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
      - Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
      - Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
      packaging_context_only:
      - Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
      - PersonalOrchestrationProcessFlow.md
      - WeeklyRoutine_Overview_Marco&Meso.md
    next_run_mode:
      recommended: decision_locked_code_ready_spec
      forbidden: architecture_rediscovery
  reading_plan:
    phase_A_read_deeply_always:
      files:
      - order: 1
        file: Apex Phase 0 Corpus Intelligence Implementation Decision.md
        why_it_matters: Binding Phase 0 contract
        extract_exactly: V1/V1.5 artifacts, script boundary, deferrals, acceptance criteria
        do_not_use_it_for: Broad retrieval implementation
      - order: 2
        file: markdown-parser-spike-report.md
        why_it_matters: Parser execution result
        extract_exactly: parser strategy, fields, warnings, Python state-machine logic
        do_not_use_it_for: Semantic interpretation
      - order: 3
        file: process-flow-graph-audit.md
        why_it_matters: Graph/process schema
        extract_exactly: edge types, hub files, script-vs-LLM boundary
        do_not_use_it_for: Obsidian workflow
      - order: 4
        file: Pre-LLMToolStack.md
        why_it_matters: Practical tool check
        extract_exactly: installed/missing tools, runtime caveats, V1/V1.5 stack
        do_not_use_it_for: Operator Windows proof
      - order: 5
        file: Updates_apex-kb.md
        why_it_matters: Existing apex-kb skill understanding
        extract_exactly: modes, boundaries, current skill architecture
        do_not_use_it_for: Live repo truth without re-check
      - order: 6
        file: Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
        why_it_matters: Best retrieval verifier
        extract_exactly: FTS5 risks, BM25 fixtures, .gitignore, derived DB rule
        do_not_use_it_for: Immediate Phase 0 scope
    phase_B_read_selectively:
      files:
      - file: Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
        read_when: Parser/frontmatter dependency decisions
        extract_exactly: stdlib-only contamination trace; python-frontmatter/PyYAML correction
      - file: Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
        read_when: Retrieval design needs latest correction
        extract_exactly: Add-on corrections only
      - file: Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
        read_when: Need implementation sequencing
        extract_exactly: preflight order, shared DB vs per-KB logic
      - file: DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md
        read_when: Later patch planning
        extract_exactly: patch anchors, retrieval command contract, repo-unverified parts
      - file: FB_DR_RetrievalINtegration_Claude.md
        read_when: Need critique of patch pack
        extract_exactly: collision risks and assumptions
      - file: Apex Link Graph and Process-Flow Representability Audit.md
        read_when: Need richer graph evidence
        extract_exactly: graph hub evidence, relationship types
      - file: link-graph.sample.json
        read_when: Need output schema
        extract_exactly: node/edge schema examples
      - file: graph-summary.md
        read_when: Need quick graph orientation
        extract_exactly: strong hubs, weak spots
    phase_C_context_only:
      files:
      - files:
        - KB-Researchv3_gpt.md
        why_context_only: Good architecture background, but broad enough to restart settled debates
      - files:
        - KB-Researchv3_gpt_FB_claude.md
        why_context_only: Useful score corrections, not binding
      - files:
        - Pre-LLMCorbusMechanisms_GPT.md
        why_context_only: Good pattern library; Phase 0 decision supersedes final tool choices
      - files:
        - Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
        why_context_only: Useful for later packaging, not Phase 0 corpus intelligence
      - files:
        - PersonalOrchestrationProcessFlow.md
        why_context_only: Useful for personal-orchestration domain separation
      - files:
        - WeeklyRoutine_Overview_Marco&Meso.md
        why_context_only: Useful for process graph context only
      - files:
        - Apex Alfred Orchestration Realization in Claude.md
        - DR_ApexOrchestrationClaude.md
        why_context_only: Use only one if Claude-native orchestration packaging is in scope
    phase_D_avoid_unless_doing_failure_analysis:
      files:
      - file: Anotehr failed DRPromptdesign*.md
        reason: Failure-only
      - file: DR_PromptFinalization2ndTry_v1.md
        reason: Prompt-finalization attempt, superseded
      - file: FBGPT_Claude1.md
        reason: Failure feedback, not current source authority
      - file: CLI_Process_GPT.md
        reason: Prompt/task predecessor, superseded by graph audit outputs
      - file: ClaudeSetupGeneral.md
        reason: Early setup, stale and question-heavy
      - file: ClaudePhase1FilePreparation.md
        reason: Older SOUL-era mapping, superseded by Claude-native file flow
      - file: research2_gem.md
        reason: Provider/current-feature scoring needs web validation
      - file: KB-Researchv2_gpt.md
        reason: Superseded by v3 + feedback + Phase 0 decision
      - file: Claude_Apex KB_SQLiteFTS5BM25_CC.md
        reason: Original spec; superseded by CCv2/GPTv2/Special/AddOn
  files:
  - id: F01
    file_name: Apex Phase 0 Corpus Intelligence Implementation Decision.md
    cluster: null
    priority: P0
    value_score: null
    freshness_score: null
    read_status: null
    role: Binding Phase 0 source
    summary: V1/V1.5 artifact contract; no-LLM/no-network/no-wiki; generic script design
    strengths: null
    weaknesses: null
    risks: Mentions claude-skill-design; must remain test KB only
    useful_for: Read first
    supersedes: null
    superseded_by: null
    read_next_run: Read first
    what_deep_research_should_find: V1/V1.5 artifact contract; no-LLM/no-network/no-wiki; generic script design
    risk_contamination: Mentions claude-skill-design; must remain test KB only
    use_verdict: Read first
  - id: F02
    file_name: markdown-parser-spike-report.md
    cluster: null
    priority: P0
    value_score: null
    freshness_score: null
    read_status: null
    role: Parser contract
    summary: Python state-machine parser; fields; failure cases; V1/V1.5 split
    strengths: null
    weaknesses: null
    risks: Sample-based, not full crawl
    useful_for: Read first
    supersedes: null
    superseded_by: null
    read_next_run: Read first
    what_deep_research_should_find: Python state-machine parser; fields; failure cases; V1/V1.5 split
    risk_contamination: Sample-based, not full crawl
    use_verdict: Read first
  - id: F03
    file_name: process-flow-graph-audit.md
    cluster: null
    priority: P0/P1
    value_score: null
    freshness_score: null
    read_status: null
    role: Graph schema
    summary: deterministic edges, hub files, script/LLM boundary
    strengths: null
    weaknesses: null
    risks: Not exhaustive local crawl
    useful_for: Read first
    supersedes: null
    superseded_by: null
    read_next_run: Read first
    what_deep_research_should_find: deterministic edges, hub files, script/LLM boundary
    risk_contamination: Not exhaustive local crawl
    use_verdict: Read first
  - id: F04
    file_name: Pre-LLMToolStack.md
    cluster: null
    priority: P1
    value_score: null
    freshness_score: null
    read_status: null
    role: Tool feasibility
    summary: runtime tool checks; V1 stack; installed/missing tools
    strengths: null
    weaknesses: null
    risks: Not operator Windows machine
    useful_for: Read first
    supersedes: null
    superseded_by: null
    read_next_run: Read first
    what_deep_research_should_find: runtime tool checks; V1 stack; installed/missing tools
    risk_contamination: Not operator Windows machine
    use_verdict: Read first
  - id: F05
    file_name: Updates_apex-kb.md
    cluster: null
    priority: P1
    value_score: null
    freshness_score: null
    read_status: null
    role: Existing apex-kb skill map
    summary: scaffold/ingest/query/lint/audit modes; package shape
    strengths: null
    weaknesses: null
    risks: Repo state must be reverified
    useful_for: Read first
    supersedes: null
    superseded_by: null
    read_next_run: Read first
    what_deep_research_should_find: scaffold/ingest/query/lint/audit modes; package shape
    risk_contamination: Repo state must be reverified
    use_verdict: Read first
  - id: F06
    file_name: Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
    cluster: null
    priority: P1
    value_score: null
    freshness_score: null
    read_status: null
    role: Retrieval verifier
    summary: FTS5 probe, BM25 vector risks, derived index rule
    strengths: null
    weaknesses: null
    risks: Implementation-focused; not Phase 0 binding
    useful_for: Read first for retrieval
    supersedes: null
    superseded_by: null
    read_next_run: Read first for retrieval
    what_deep_research_should_find: FTS5 probe, BM25 vector risks, derived index rule
    risk_contamination: Implementation-focused; not Phase 0 binding
    use_verdict: Read first for retrieval
  - id: F07
    file_name: Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
    cluster: null
    priority: P1
    value_score: null
    freshness_score: null
    read_status: null
    role: Contamination correction
    summary: stdlib-only/PyYAML AI-injection; parser dependency options
    strengths: null
    weaknesses: null
    risks: Narrow scope
    useful_for: Read for parser policy
    supersedes: null
    superseded_by: null
    read_next_run: Read for parser policy
    what_deep_research_should_find: stdlib-only/PyYAML AI-injection; parser dependency options
    risk_contamination: Narrow scope
    use_verdict: Read for parser policy
  - id: F08
    file_name: Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
    cluster: null
    priority: P1
    value_score: null
    freshness_score: null
    read_status: null
    role: Latest retrieval add-on
    summary: newest corrections around retrieval
    strengths: null
    weaknesses: null
    risks: Add-on, not full plan
    useful_for: Read after GPTv2
    supersedes: null
    superseded_by: null
    read_next_run: Read after GPTv2
    what_deep_research_should_find: newest corrections around retrieval
    risk_contamination: Add-on, not full plan
    use_verdict: Read after GPTv2
  - id: F09
    file_name: Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
    cluster: null
    priority: P2
    value_score: null
    freshness_score: null
    read_status: null
    role: Retrieval implementation plan
    summary: sequencing, shared DB, preflight, tests
    strengths: null
    weaknesses: null
    risks: Can pull work into premature implementation
    useful_for: Read if coding spec later
    supersedes: null
    superseded_by: null
    read_next_run: Read if coding spec later
    what_deep_research_should_find: sequencing, shared DB, preflight, tests
    risk_contamination: Can pull work into premature implementation
    use_verdict: Read if coding spec later
  - id: F10
    file_name: DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md
    cluster: null
    priority: P2
    value_score: null
    freshness_score: null
    read_status: null
    role: Patch-pack candidate
    summary: retrieval docs, patch surfaces, command contracts
    strengths: null
    weaknesses: null
    risks: Repo access partly unverified
    useful_for: Later patch planning only
    supersedes: null
    superseded_by: null
    read_next_run: Later patch planning only
    what_deep_research_should_find: retrieval docs, patch surfaces, command contracts
    risk_contamination: Repo access partly unverified
    use_verdict: Later patch planning only
  - id: F11
    file_name: FB_DR_RetrievalINtegration_Claude.md
    cluster: null
    priority: P2
    value_score: null
    freshness_score: null
    read_status: null
    role: Patch critique
    summary: collision risks, feedback, integration corrections
    strengths: null
    weaknesses: null
    risks: Assumption-heavy
    useful_for: Read with patch pack
    supersedes: null
    superseded_by: null
    read_next_run: Read with patch pack
    what_deep_research_should_find: collision risks, feedback, integration corrections
    risk_contamination: Assumption-heavy
    use_verdict: Read with patch pack
  - id: F12
    file_name: Apex Link Graph and Process-Flow Representability Audit.md
    cluster: null
    priority: P1
    value_score: null
    freshness_score: null
    read_status: null
    role: Full graph rationale
    summary: why graph is partial/useful; Apex-specific edge types
    strengths: null
    weaknesses: null
    risks: Sample-based
    useful_for: Read if graph output design
    supersedes: null
    superseded_by: null
    read_next_run: Read if graph output design
    what_deep_research_should_find: why graph is partial/useful; Apex-specific edge types
    risk_contamination: Sample-based
    use_verdict: Read if graph output design
  - id: F13
    file_name: link-graph.sample.json
    cluster: null
    priority: P2
    value_score: null
    freshness_score: null
    read_status: null
    role: Concrete schema
    summary: node/edge schema and graph metadata
    strengths: null
    weaknesses: null
    risks: Sample only
    useful_for: Schema reference
    supersedes: null
    superseded_by: null
    read_next_run: Schema reference
    what_deep_research_should_find: node/edge schema and graph metadata
    risk_contamination: Sample only
    use_verdict: Schema reference
  - id: F14
    file_name: graph-summary.md
    cluster: null
    priority: P2
    value_score: null
    freshness_score: null
    read_status: null
    role: Fast graph orientation
    summary: hubs, weak spots, V1.5 output set
    strengths: null
    weaknesses: null
    risks: Summary only
    useful_for: Use for quick context
    supersedes: null
    superseded_by: null
    read_next_run: Use for quick context
    what_deep_research_should_find: hubs, weak spots, V1.5 output set
    risk_contamination: Summary only
    use_verdict: Use for quick context
  - id: F15
    file_name: Pre-LLM Tool Stack Installability and Value Audit.md
    cluster: null
    priority: P2
    value_score: null
    freshness_score: null
    read_status: null
    role: Tool audit prompt + candidates
    summary: candidate list, Windows local checks, scoring dimensions
    strengths: null
    weaknesses: null
    risks: Mixed prompt/report
    useful_for: Use to formulate local checks
    supersedes: null
    superseded_by: null
    read_next_run: Use to formulate local checks
    what_deep_research_should_find: candidate list, Windows local checks, scoring dimensions
    risk_contamination: Mixed prompt/report
    use_verdict: Use to formulate local checks
  - id: F16
    file_name: Pre-LLMCorbusMechanisms_GPT.md
    cluster: null
    priority: P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Pattern library
    summary: MkDocs/mdBook/remark/FTS5 patterns
    strengths: null
    weaknesses: null
    risks: Tool patterns not equally applicable
    useful_for: Context only
    supersedes: null
    superseded_by: null
    read_next_run: Context only
    what_deep_research_should_find: MkDocs/mdBook/remark/FTS5 patterns
    risk_contamination: Tool patterns not equally applicable
    use_verdict: Context only
  - id: F17
    file_name: KB-Researchv3_gpt_FB_claude.md
    cluster: null
    priority: P2/P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Score correction
    summary: corrected rankings and vector-cost caveats
    strengths: null
    weaknesses: null
    risks: Not binding
    useful_for: Context if scoring needed
    supersedes: null
    superseded_by: null
    read_next_run: Context if scoring needed
    what_deep_research_should_find: corrected rankings and vector-cost caveats
    risk_contamination: Not binding
    use_verdict: Context if scoring needed
  - id: F18
    file_name: KB-Researchv3_gpt.md
    cluster: null
    priority: P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Broad architecture background
    summary: layered KB/memory model
    strengths: null
    weaknesses: null
    risks: May restart architecture debate
    useful_for: Background only
    supersedes: null
    superseded_by: null
    read_next_run: Background only
    what_deep_research_should_find: layered KB/memory model
    risk_contamination: May restart architecture debate
    use_verdict: Background only
  - id: F19
    file_name: Apex KB+SQLite FTS5BM25 Implementation Plan.md
    cluster: null
    priority: P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Alternate implementation plan
    summary: consistency with CCv2
    strengths: null
    weaknesses: null
    risks: Duplicate plan
    useful_for: Only if contradictions
    supersedes: null
    superseded_by: null
    read_next_run: Only if contradictions
    what_deep_research_should_find: consistency with CCv2
    risk_contamination: Duplicate plan
    use_verdict: Only if contradictions
  - id: F20
    file_name: Claude_Apex KB_SQLiteFTS5BM25_CCv3.md
    cluster: null
    priority: P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Old verifier variant
    summary: audit trail, risk lists
    strengths: null
    weaknesses: null
    risks: contaminated by stdlib-only framing
    useful_for: Avoid unless auditing
    supersedes: null
    superseded_by: null
    read_next_run: Avoid unless auditing
    what_deep_research_should_find: audit trail, risk lists
    risk_contamination: contaminated by stdlib-only framing
    use_verdict: Avoid unless auditing
  - id: F21
    file_name: Claude_Apex KB_SQLiteFTS5BM25_CC.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Original retrieval spec
    summary: original pipeline concepts
    strengths: null
    weaknesses: null
    risks: superseded; frontmatter/BM25 drift
    useful_for: Archive/context
    supersedes: null
    superseded_by: null
    read_next_run: Archive/context
    what_deep_research_should_find: original pipeline concepts
    risk_contamination: superseded; frontmatter/BM25 drift
    use_verdict: Archive/context
  - id: F22
    file_name: KB-Researchv2_gpt.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Older research
    summary: provenance only
    strengths: null
    weaknesses: null
    risks: superseded
    useful_for: Archive
    supersedes: null
    superseded_by: null
    read_next_run: Archive
    what_deep_research_should_find: provenance only
    risk_contamination: superseded
    use_verdict: Archive
  - id: F23
    file_name: research2_gem.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Provider options
    summary: native/cloud memory vocabulary
    strengths: null
    weaknesses: null
    risks: time-sensitive provider claims
    useful_for: Avoid unless web-validating
    supersedes: null
    superseded_by: null
    read_next_run: Avoid unless web-validating
    what_deep_research_should_find: native/cloud memory vocabulary
    risk_contamination: time-sensitive provider claims
    use_verdict: Avoid unless web-validating
  - id: F24
    file_name: Markdown Structure Parser Spike for Apex KB Phase.md
    cluster: null
    priority: P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Parser prompt origin
    summary: sample rules, fake-simulation correction
    strengths: null
    weaknesses: null
    risks: prompt wording allowed simulation
    useful_for: Use for prompt lesson
    supersedes: null
    superseded_by: null
    read_next_run: Use for prompt lesson
    what_deep_research_should_find: sample rules, fake-simulation correction
    risk_contamination: prompt wording allowed simulation
    use_verdict: Use for prompt lesson
  - id: F25
    file_name: CLI_Process_GPT.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Graph prompt origin
    summary: relation types and task framing
    strengths: null
    weaknesses: null
    risks: superseded by graph outputs
    useful_for: Avoid
    supersedes: null
    superseded_by: null
    read_next_run: Avoid
    what_deep_research_should_find: relation types and task framing
    risk_contamination: superseded by graph outputs
    use_verdict: Avoid
  - id: F26
    file_name: DR_PromptFinalization2ndTry_v1.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Prompt-failure context
    summary: anti-contamination prompt attempts
    strengths: null
    weaknesses: null
    risks: superseded
    useful_for: Avoid
    supersedes: null
    superseded_by: null
    read_next_run: Avoid
    what_deep_research_should_find: anti-contamination prompt attempts
    risk_contamination: superseded
    use_verdict: Avoid
  - id: F27
    file_name: Anotehr failed DRPromptdesign.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Failure-only
    summary: none except anti-patterns
    strengths: null
    weaknesses: null
    risks: failure artifact
    useful_for: Delete/archive
    supersedes: null
    superseded_by: null
    read_next_run: Delete/archive
    what_deep_research_should_find: none except anti-patterns
    risk_contamination: failure artifact
    use_verdict: Delete/archive
  - id: F28
    file_name: Anotehr failed DRPromptdesign2.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Failure-only
    summary: none except anti-patterns
    strengths: null
    weaknesses: null
    risks: failure artifact
    useful_for: Delete/archive
    supersedes: null
    superseded_by: null
    read_next_run: Delete/archive
    what_deep_research_should_find: none except anti-patterns
    risk_contamination: failure artifact
    use_verdict: Delete/archive
  - id: F29
    file_name: Anotehr failed DRPromptdesign3.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Failure-only
    summary: none except anti-patterns
    strengths: null
    weaknesses: null
    risks: failure artifact
    useful_for: Delete/archive
    supersedes: null
    superseded_by: null
    read_next_run: Delete/archive
    what_deep_research_should_find: none except anti-patterns
    risk_contamination: failure artifact
    use_verdict: Delete/archive
  - id: F30
    file_name: FBGPT_Claude1.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Failure feedback
    summary: only if diagnosing prior failed run
    strengths: null
    weaknesses: null
    risks: not binding
    useful_for: Archive
    supersedes: null
    superseded_by: null
    read_next_run: Archive
    what_deep_research_should_find: only if diagnosing prior failed run
    risk_contamination: not binding
    use_verdict: Archive
  - id: F31
    file_name: Apex_Alfred_Skill_Definition_Guide.md
    cluster: null
    priority: P2
    value_score: null
    freshness_score: null
    read_status: null
    role: Skill packaging rules
    summary: SKILL.md anatomy, frontmatter, gates
    strengths: null
    weaknesses: null
    risks: not Phase 0-specific
    useful_for: Later packaging
    supersedes: null
    superseded_by: null
    read_next_run: Later packaging
    what_deep_research_should_find: SKILL.md anatomy, frontmatter, gates
    risk_contamination: not Phase 0-specific
    use_verdict: Later packaging
  - id: F32
    file_name: Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
    cluster: null
    priority: P2/P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Claude-native file flow
    summary: approved paths, four roles, output contract
    strengths: null
    weaknesses: null
    risks: not KB Phase 0
    useful_for: Packaging only
    supersedes: null
    superseded_by: null
    read_next_run: Packaging only
    what_deep_research_should_find: approved paths, four roles, output contract
    risk_contamination: not KB Phase 0
    use_verdict: Packaging only
  - id: F33
    file_name: Apex Alfred Orchestration Realization in Claude.md
    cluster: null
    priority: P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Claude-native research
    summary: external Claude docs and orchestration choices
    strengths: null
    weaknesses: null
    risks: needs web revalidation if reused
    useful_for: Context only
    supersedes: null
    superseded_by: null
    read_next_run: Context only
    what_deep_research_should_find: external Claude docs and orchestration choices
    risk_contamination: needs web revalidation if reused
    use_verdict: Context only
  - id: F34
    file_name: DR_ApexOrchestrationClaude.md
    cluster: null
    priority: P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Duplicate orchestration research
    summary: same as F33
    strengths: null
    weaknesses: null
    risks: duplicate
    useful_for: Use one copy only
    supersedes: null
    superseded_by: null
    read_next_run: Use one copy only
    what_deep_research_should_find: same as F33
    risk_contamination: duplicate
    use_verdict: Use one copy only
  - id: F35
    file_name: ClaudePhase1FilePreparation.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Old conversion map
    summary: SOUL/SKILL mapping history
    strengths: null
    weaknesses: null
    risks: stale SOUL framing
    useful_for: Avoid
    supersedes: null
    superseded_by: null
    read_next_run: Avoid
    what_deep_research_should_find: SOUL/SKILL mapping history
    risk_contamination: stale SOUL framing
    use_verdict: Avoid
  - id: F36
    file_name: ClaudeSetupGeneral.md
    cluster: null
    priority: P4
    value_score: null
    freshness_score: null
    read_status: null
    role: Early setup context
    summary: old questions and assumptions
    strengths: null
    weaknesses: null
    risks: stale
    useful_for: Avoid
    supersedes: null
    superseded_by: null
    read_next_run: Avoid
    what_deep_research_should_find: old questions and assumptions
    risk_contamination: stale
    use_verdict: Avoid
  - id: F37
    file_name: PersonalOrchestrationProcessFlow.md
    cluster: null
    priority: P2/P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Personal orchestration artifact system
    summary: separate personal memory domain; flow/prompt-pack/status loop
    strengths: null
    weaknesses: null
    risks: can be confused with KB scope
    useful_for: Context for domain separation
    supersedes: null
    superseded_by: null
    read_next_run: Context for domain separation
    what_deep_research_should_find: separate personal memory domain; flow/prompt-pack/status loop
    risk_contamination: can be confused with KB scope
    use_verdict: Context for domain separation
  - id: F38
    file_name: WeeklyRoutine_Overview_Marco&Meso.md
    cluster: null
    priority: P2/P3
    value_score: null
    freshness_score: null
    read_status: null
    role: Routine/process graph context
    summary: PreCapWeek → PreCapNextDay → FlowRecap → APSU chain
    strengths: null
    weaknesses: null
    risks: not KB authority
    useful_for: Context for graph/process terms
    supersedes: null
    superseded_by: null
    read_next_run: Context for graph/process terms
    what_deep_research_should_find: PreCapWeek → PreCapNextDay → FlowRecap → APSU chain
    risk_contamination: not KB authority
    use_verdict: Context for graph/process terms
  topic_to_file_routing:
    phase0_corpus_intelligence:
      read_first:
      - Apex Phase 0 Corpus Intelligence Implementation Decision.md
      - markdown-parser-spike-report.md
      - Pre-LLMToolStack.md
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
      - Apex Phase 0 Corpus Intelligence Implementation Decision.md
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
      - markdown-parser-spike-report.md
      read_second:
      - Markdown Structure Parser Spike for Apex KB Phase.md
      - Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
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
      - Pre-LLMToolStack.md
      - Pre-LLM Tool Stack Installability and Value Audit.md
      read_second:
      - Pre-LLMCorbusMechanisms_GPT.md
      extract:
      - git/rg/Python stdlib as V1
      - markdown-it-py as V1.5
      - SQLite FTS5 test as V1.5
      - Node/static-site tooling deferred
      caution:
      - runtime was not operator Windows machine
    graph_extraction:
      read_first:
      - process-flow-graph-audit.md
      - Apex Link Graph and Process-Flow Representability Audit.md
      - link-graph.sample.json
      read_second:
      - graph-summary.md
      - WeeklyRoutine_Overview_Marco&Meso.md
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
      - Updates_apex-kb.md
      read_second:
      - DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md
      - FB_DR_RetrievalINtegration_Claude.md
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
      - Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
      - Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
      read_second:
      - Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
      - Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
      - Apex KB+SQLite FTS5BM25 Implementation Plan.md
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
      - Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
      - Apex_Alfred_Skill_Definition_Guide.md
      read_second:
      - Apex Alfred Orchestration Realization in Claude.md
      - DR_ApexOrchestrationClaude.md
      extract:
      - approved Claude-native paths
      - four permanent roles
      - skill/frontmatter style
      - no Hermes/SOUL drift
      avoid:
      - using these to override Phase 0 corpus-intelligence scope
    personal_orchestration_domain:
      read_first:
      - PersonalOrchestrationProcessFlow.md
      - WeeklyRoutine_Overview_Marco&Meso.md
      extract:
      - personal orchestration as adjacent domain
      - PreCap/FlowRecap/status loop terms
      - artifact chain for graph context
      avoid:
      - collapsing personal orchestration into project KB
  clusters:
  - id: C1
    name: Phase 0 decision and contracts
    best_files:
    - Apex Phase 0 Corpus Intelligence Implementation Decision.md
    role: Binding scope. It says the next work is a deterministic corpus-intelligence layer before LLM semantic ingest. It
      also names the V1 artifacts and defers graph/FTS5 to V1.5.
    important_correction: null
    deep_research_instruction: Start here. Extract decisions. Do not reinterpret older research as equal authority.
  - id: C2
    name: Parser and Markdown structure extraction
    best_files:
    - markdown-parser-spike-report.md
    - Markdown Structure Parser Spike for Apex KB Phase.md
    role: Defines how to produce heading-map.json, markdown-link-map.json, frontmatter-map.json, parser warnings, and sample
      structural extraction.
    important_correction: The parser does not decide meaning; it only records structure.
    deep_research_instruction: Use this to write the code-ready parser spec. Do not ask the LLM to classify concepts in Phase
      0.
  - id: C3
    name: Tool stack / deterministic pre-LLM mechanisms
    best_files:
    - Pre-LLMToolStack.md
    - Pre-LLM Tool Stack Installability and Value Audit.md
    - Pre-LLMCorbusMechanisms_GPT.md
    role: Shows which tools are plausible and which are overkill. The tool audit confirms a small deterministic stack and
      warns that runtime checks were not on the operator’s Windows machine.
    important_correction: null
    deep_research_instruction: Use for local-check commands and tool ranking, not as definitive Windows proof.
  - id: C4
    name: Graph and process-flow extraction
    best_files:
    - process-flow-graph-audit.md
    - Apex Link Graph and Process-Flow Representability Audit.md
    - link-graph.sample.json
    - graph-summary.md
    role: Defines graph extraction as V1.5 and explains that Apex graph edges mostly live in explicit paths, YAML fields,
      package manifests, owns, does_not_own, hands_off_to, and arrow sequences.
    important_correction: null
    deep_research_instruction: Build deterministic graph artifacts later. Do not rely on Markdown links alone.
  - id: C5
    name: Existing apex-kb skill architecture
    best_files:
    - Updates_apex-kb.md
    role: Explains apex-kb as a durable source-preserving knowledge-base compiler, with scaffold, ingest phase 1, ingest phase
      2, query, lint, and audit modes.
    important_correction: null
    deep_research_instruction: Use as an orientation map, then verify live repo contents before patching or writing final
      files.
  - id: C6
    name: SQLite FTS5/BM25 retrieval
    best_files:
    - Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
    - Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
    - Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
    - Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
    role: Later retrieval layer. It clarifies source custody vs retrieval, local lexical search, BM25 ranking, snippets, staleness,
      and pitfalls. The verifier stresses that the plan is directionally correct but unsafe without FTS5 availability checks,
      BM25 vector alignment, YAML parsing limits, .gitignore order, and skill/package gates.
    important_correction: null
    deep_research_instruction: Do not implement this as Phase 0 V1. Use it for V1.5 search-index design and future apex-kb
      retrieval integration.
  - id: C7
    name: Prompt failures and anti-contamination
    best_files:
    - mostly previous index + failed prompt files
    role: Diagnose how the research loop drifted into too much breadth, fake authority, simulation, and hardcoded paths.
    important_correction: null
    deep_research_instruction: Use the anti-contamination rules, but do not read all failed prompts unless debugging prompt
      design.
  - id: C8
    name: Claude-native packaging / orchestration context
    best_files:
    - Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
    - Apex_Alfred_Skill_Definition_Guide.md
    - PersonalOrchestrationProcessFlow.md
    - WeeklyRoutine_Overview_Marco&Meso.md
    role: Later packaging and process context. Useful to understand the broader Apex Alfred system, but not authoritative
      for Phase 0 KB corpus intelligence.
    important_correction: null
    deep_research_instruction: Use only after Phase 0 output contract is settled.
  supersession_map:
    phase0_scope:
      binding: Apex Phase 0 Corpus Intelligence Implementation Decision.md
      supersedes:
      - KB-Researchv2_gpt.md
      - KB-Researchv3_gpt.md where it broadens scope
      - KB-Researchv3_gpt_FB_claude.md where it broadens scope
      - retrieval patch packs where they imply immediate implementation
    parser:
      binding:
      - Apex Phase 0 Corpus Intelligence Implementation Decision.md
      - markdown-parser-spike-report.md
      supersedes:
      - Markdown Structure Parser Spike for Apex KB Phase.md when it says implement/simulate
      current_rule: Attempt bounded execution; do not simulate parser results.
    graph:
      binding:
      - Apex Phase 0 Corpus Intelligence Implementation Decision.md
      - process-flow-graph-audit.md
      - Apex Link Graph and Process-Flow Representability Audit.md
      supersedes:
      - CLI_Process_GPT.md
      current_rule: Graph belongs in V1.5 and must parse Apex-specific path/YAML/process edges.
    retrieval:
      current_best:
      - Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
      - Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
      - Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
      partly_supersedes:
      - Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
      - Apex KB+SQLite FTS5BM25 Implementation Plan.md
      - Claude_Apex KB_SQLiteFTS5BM25_CCv3.md
      - Claude_Apex KB_SQLiteFTS5BM25_CC.md
      current_rule: Use retrieval files for V1.5/later; Phase 0 V1 remains deterministic navigation.
    claude_packaging:
      current_best:
      - Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
      - Apex_Alfred_Skill_Definition_Guide.md
      supersedes:
      - ClaudeSetupGeneral.md
      - ClaudePhase1FilePreparation.md where SOUL/Hermes framing conflicts
  contamination_and_stale_claim_audit:
  - id: C01
    bad_claim_or_risk: claude-skill-design is the fixed script target
    where_it_appears: Phase 0 prompt/context
    correct_rule: Use generic --kb-root; claude-skill-design is first test KB
    severity: Critical
  - id: C02
    bad_claim_or_risk: Phase 0 should create wiki pages
    where_it_appears: Older ingest/retrieval framing
    correct_rule: Phase 0 creates navigation artifacts only
    severity: Critical
  - id: C03
    bad_claim_or_risk: Phase 0 should produce semantic ingest analyses
    where_it_appears: Older apex-kb mode confusion
    correct_rule: Semantic ingest belongs later
    severity: Critical
  - id: C04
    bad_claim_or_risk: SQLite FTS5/BM25 is immediate V1
    where_it_appears: Retrieval files
    correct_rule: FTS5 is V1.5/later, with local runtime test
    severity: High
  - id: C05
    bad_claim_or_risk: Python stdlib-only/no PyYAML was operator-decided
    where_it_appears: SQLite/BM25 verifier chain
    correct_rule: Treat as AI-injected unless operator explicitly decides
    severity: High
  - id: C06
    bad_claim_or_risk: Regex-only YAML parsing is safe
    where_it_appears: Older parser/retrieval assumptions
    correct_rule: Use strict subset or robust parser; detect malformed frontmatter
    severity: High
  - id: C07
    bad_claim_or_risk: Pure Markdown links are enough for graph
    where_it_appears: Obsidian-style graph framing
    correct_rule: Parse YAML/path/process/contract edges
    severity: High
  - id: C08
    bad_claim_or_risk: Tool availability in runtime equals Windows machine
    where_it_appears: Tool audit
    correct_rule: Verify on C:\GitDev\apexai-os-meta
    severity: Medium
  - id: C09
    bad_claim_or_risk: Current Claude/provider feature scores are stable
    where_it_appears: research2_gem.md, orchestration research
    correct_rule: Web-verify current provider claims if reused
    severity: Medium
  - id: C10
    bad_claim_or_risk: Patch packs are repo-verified
    where_it_appears: Patch packs
    correct_rule: Re-read live repo before applying
    severity: High
  - id: C11
    bad_claim_or_risk: Old SOUL/Hermes language should be copied
    where_it_appears: ClaudeSetupGeneral, ClaudePhase1FilePreparation
    correct_rule: Translate to Claude-native paths only
    severity: Medium
  - id: C12
    bad_claim_or_risk: Deep Research should read every file again
    where_it_appears: Broad prompt variants
    correct_rule: Read prioritized source spine, then topic-specific files
    severity: High
  - id: C13
    bad_claim_or_risk: phase0-navigation-report.md can be a skeleton
    where_it_appears: Future output risk
    correct_rule: Must contain populated ranked file guidance
    severity: Critical
  - id: C14
    bad_claim_or_risk: Personal orchestration memory belongs inside project KB
    where_it_appears: Broad memory docs
    correct_rule: Keep as adjacent domain, not mixed into project KB
    severity: Medium
  later_deep_research_output_contract_v0_2:
    output_A:
      name: validated_phase0_truth
      purpose: 'Convert the source index into a final, source-grounded truth table: what Phase 0 is, what it is not, and which
        files support each claim.'
      must_include:
      - binding decisions
      - superseded decisions
      - hardcoded path corrections
      - repo-truth checks still needed
      - no architecture rediscovery
    output_B:
      name: populated_integration_map
      purpose: Map every V1 and V1.5 artifact to producer, consumer, source inputs, output path, validation rule, and failure
        mode.
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
      purpose: Give Claude/Codex a code-ready but not-yet-code spec for phase0_corpus_intelligence.py.
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
      purpose: Isolate retrieval/graph future work so it does not pollute V1.
      must_include:
      - FTS5 runtime probe
      - search-index.sqlite or JSON/NDJSON fallback
      - link graph schema
      - process graph schema
      - frontmatter parser upgrade option
      - explicit deferral of vector search
  final_compact_block_for_next_prompt:
    mission:
      create: validated, code-ready Phase 0 corpus intelligence specification
      do_not_create:
      - final Apex KB skill
      - final scripts
      - repo patches
      - wiki pages
      - semantic ingest analyses
      - vector stores
    read_order:
      deep_read:
      - Apex Phase 0 Corpus Intelligence Implementation Decision.md
      - markdown-parser-spike-report.md
      - process-flow-graph-audit.md
      - Pre-LLMToolStack.md
      - Updates_apex-kb.md
      - Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
      targeted_read:
      - Apex Link Graph and Process-Flow Representability Audit.md
      - link-graph.sample.json
      - graph-summary.md
      - Pre-LLM Tool Stack Installability and Value Audit.md
      - Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
      - Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
      - Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
      - DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md
      - FB_DR_RetrievalINtegration_Claude.md
      context_only:
      - KB-Researchv3_gpt.md
      - KB-Researchv3_gpt_FB_claude.md
      - Pre-LLMCorbusMechanisms_GPT.md
      - Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
      - PersonalOrchestrationProcessFlow.md
      - WeeklyRoutine_Overview_Marco&Meso.md
      avoid_unless_failure_analysis:
      - Anotehr failed DRPromptdesign.md
      - Anotehr failed DRPromptdesign2.md
      - Anotehr failed DRPromptdesign3.md
      - DR_PromptFinalization2ndTry_v1.md
      - FBGPT_Claude1.md
      - CLI_Process_GPT.md
      - ClaudeSetupGeneral.md
      - ClaudePhase1FilePreparation.md
      - research2_gem.md
      - KB-Researchv2_gpt.md
      - Claude_Apex KB_SQLiteFTS5BM25_CC.md
    binding_rules:
    - Newest explicit decision wins.
    - Operator instruction overrides AI output.
    - Apex Phase 0 decision file is primary authority.
    - Phase 0 is deterministic pre-LLM navigation.
    - Phase 0 creates artifacts, not wiki pages or semantic analyses.
    - Use generic --kb-root; do not hardcode claude-skill-design.
    - V1 uses source inventory, rg/Python stdlib, parser maps, keyword hits, topic file map, priority candidates, and navigation
      report.
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
    key_contamination_flags:
      HARDCODED_KB_PATH:
        rule: claude-skill-design is first test KB, not fixed target.
      SEMANTIC_INGEST_CONFUSION:
        rule: No ingest-analysis/wiki generation in Phase 0.
      FTS5_ASSUMPTION:
        rule: Test FTS5 locally before relying on SQLite FTS5.
      YAML_STDLIB_ONLY_INJECTION:
        rule: Do not treat no-PyYAML/no-frontmatter as operator decision.
      GRAPH_UNDERCOUNT:
        rule: Parse YAML/path/process edges, not only Markdown links.
      REPO_PATCH_RISK:
        rule: Patch only after live repo truth check.
    recommended_next_prompt_strategy:
      name: decision_locked_phase0_spec_run
      instruction: Start from the Phase 0 decision file. Validate parser/tool/graph/retrieval implications from the read-first
        spine. Produce validated truth, populated integration map, and code-ready spec. Do not restart architecture research.
