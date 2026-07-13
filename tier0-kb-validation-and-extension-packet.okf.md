# Tier 0 KB Validation and Extension Packet

**Finding:** The Tier 0 direction is broadly sound: reduce always-loaded duplication, preserve one canonical owner per rule, route detailed instructions through activated skills and references, and add explicit recovery behavior for long orchestration runs.

**Decision:** The evidence is sufficient for a bounded implementation plan, but not for a patch or application. Exact targets must be revalidated against the then-current repository snapshot, and deterministic checks must run in a terminal-backed worktree.

**Required action:** Stop at Phase 1. No semantic wiki page, source manifest, generated index, or Tier 0 runtime file was modified in this run.

```okf
kb_validation_and_extension_packet:
  metadata:
    repository: "leela-spec/apexai-os-meta"
    repository_ref:
      observation_baseline: "f70fe668b74bcf67909d41602bb7719185120f85"
      phase1_write_head: "dc0cc1eddfda130df449f386ed8955d7c82e20d6"
    kb_roots:
      - "apex-meta/kb/old-apex-full-orchestration-agent-kb"
      - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    authoritative_task: "Validate Tier 0 orchestration improvements; Phase 1 only; no runtime implementation."
    phase_completed: "phase1_analysis_only"
    approval_status: "approve ingest not received"
    environment_capabilities:
      connected_repository_read: true
      connected_repository_whole_file_create: true
      local_worktree: false
      shell_execution: false
      python_execution: false
      deterministic_index_rebuild: false
      git_diff_execution: false
    execution_limitations:
      - "No repository Python commands could be executed."
      - "Source hashes, retrieval freshness, lint, audit, status, health, and quality could be inspected only through stored artifacts."
      - "Connector readback proves stored content, not deterministic validity."

  executive_assessment:
    overall_status: "supported_with_qualification"
    safe_to_plan: true
    safe_to_patch: false
    safe_to_apply: false
    highest_priority_findings:
      - "The live activation file duplicates the weekly loop contract already owned by the weekly-orchestrator skill."
      - "The live activation copy is stale: it still assigns G5 to APSU while the current weekly skill routes G5 through status_merge and apex-session."
      - "The proposed preload-name repair is already complete on main and must be removed from future patch scope."
      - "Blanket skill and agent description rewrites are not justified; use an inventory-driven offender list and preserve load-bearing trigger and invocation metadata."
      - "KB v1 has outdated source custody and duplicate connector-workaround pages."
      - "KB v2 has an index/topic-registry mismatch and incomplete compiled topic coverage."
    unresolved_blockers:
      - "No exhaustive current skill and agent inventory with measured description sizes."
      - "No deterministic preflight or retrieval-staleness execution."
      - "No trigger-regression test proving description reductions preserve skill routing."
      - "No current runtime test confirming the recognized activation-file path and case behavior in this repository environment."
```

## 1. Contract and Phase Boundary

**Conflict:** The current global Apex KB skill permits continuous Phase 1-to-Phase 2 compilation by default when wiki output is selected. The task handover and both KB-local schemas require an explicit stop before semantic wiki mutation and the exact phrase `approve ingest` for continuation.

**Decision:** This run used `analysis_only` / `phase1_only`. The explicit no-mutation instruction and KB-local review policies are narrower than the global default and therefore control this run.

```yaml
contract_conflict:
  finding_id: CONTRACT-001
  current_global_contract: "Phase 2 may follow Phase 1 by default for wiki output tiers."
  task_and_local_contract: "Stop after Phase 1 until exact phrase approve ingest."
  disposition: "follow_explicit_task_boundary"
  claim_status: "directly_observed"
  evidence: 100
  risk: 94
  impact: 92
  score_basis: "All controlling files were read directly; violating the narrower boundary would create unauthorized semantic mutations."
```

## 2. Deterministic Preflight

A passing stored report is historical evidence only. It is not a current execution result.

```yaml
deterministic_preflight:
  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    status: "requires_execution_validation"
    health: "requires_execution_validation"
    lint: "requires_execution_validation"
    audit: "stored audit items inspected; current audit command not run"
    retrieval_index: "stored SQLite FTS5 metadata exists for 17 pages; freshness not revalidated"
    source_custody_issues:
      - "source-manifest contains two pointer_only Windows absolute tree roots"
      - "no source-payload-manifest.json under the current contract"
      - "repository source copies exist, but per-file custody is not represented in the source manifest"
      - "wiki contains canonical and rerun-v2 duplicate pages created after connector overwrite blocks"
    requires_execution_validation: true

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    status: "requires_execution_validation"
    health: "requires_execution_validation"
    lint: "requires_execution_validation"
    audit: "stored high-impact conflict register inspected; current audit command not run"
    retrieval_index: "stored SQLite FTS5 metadata exists for 17 pages; index/topic mismatch indicates rebuild or generator review is required"
    source_custody_issues:
      - "source manifest and payload manifest exist for 418 copied files"
      - "payload hashes were not recomputed in this environment"
      - "wiki/index.md renders six topics as Untitled topic although topic-registry.json contains titles"
      - "repository system index reports 19 page files while generated wiki index enumerates 17"
    requires_execution_validation: true
```

### Preflight findings

```yaml
preflight_findings:
  - finding_id: PF-001
    finding: "KB v1 lacks the source payload manifest required by the current contract."
    claim_status: "directly_observed"
    evidence: 98
    risk: 57
    impact: 72
    score_basis: "The current contract requires the artifact and a direct repository read returned no file; acting on old aggregate hashes risks incomplete custody assumptions."

  - finding_id: PF-002
    finding: "KB v1 contains duplicate canonical and rerun-v2 pages with identical indexed hashes."
    claim_status: "directly_observed"
    evidence: 97
    risk: 68
    impact: 70
    score_basis: "The stored retrieval metadata lists paired paths with identical hashes; duplicate retrieval can distort evidence ranking and page ownership."

  - finding_id: PF-003
    finding: "KB v2 wiki topic labels are stale or incorrectly generated."
    claim_status: "directly_observed"
    evidence: 99
    risk: 45
    impact: 66
    score_basis: "The generated index says Untitled topic while the canonical topic registry supplies explicit titles."

  - finding_id: PF-004
    finding: "Neither KB can be certified current from connector inspection alone."
    claim_status: "requires_execution_validation"
    evidence: 100
    risk: 88
    impact: 85
    score_basis: "The active KB contract explicitly states that connector readback does not prove lint, quality, health, index freshness, or query readiness."
```

## 3. Current Repository Position

```yaml
repository_findings:
  - finding_id: REPO-001
    path: ".claude/Claude.md"
    observation: "The recognized project activation candidate contains identity, the full core loop, skill table, agent table, project-engine boundary, artifact paths, startup procedure, exclusions, and constraints."
    proposed_issue: "Always-loaded scope is broad and duplicates activated contracts."
    claim_status: "directly_observed"
    recommended_action: "Retain only global identity, hard global constraints, and pointers after confirming this path is the runtime-recognized activation file."
    evidence: 98
    risk: 81
    impact: 96
    score_basis: "The complete file was read at the pinned baseline; changing activation scope affects every session and therefore has high impact and rollback sensitivity."

  - finding_id: REPO-002
    path: ".claude/Claude.md"
    observation: "The copied core loop assigns G5 to APSU and names updated_all_project_status_packet."
    proposed_issue: "This conflicts with the live weekly-orchestrator contract, which assigns G5 to status_merge and routes confirmed changes through apex-session."
    claim_status: "contradicted"
    recommended_action: "Do not repair the duplicated loop in place; remove it from the activation file and preserve one canonical loop owner."
    evidence: 99
    risk: 89
    impact: 94
    score_basis: "Both conflicting live files were read directly; leaving two owners permits stale routing at the highest orchestration layer."

  - finding_id: REPO-003
    path: ".claude/skills/weekly-orchestrator/SKILL.md"
    observation: "The skill already owns stage routing, G1-G5 handling, packet-envelope validation, review triggering, loop-position discovery, and apex-session mutation routing."
    proposed_issue: "The skill is the natural canonical owner for the weekly loop, but lacks an explicit resume/compaction reread rule."
    claim_status: "directly_observed"
    recommended_action: "Keep the loop here; add only a narrowly worded recovery instruction after runtime verification."
    evidence: 97
    risk: 48
    impact: 86
    score_basis: "Ownership is explicit in the skill; recovery behavior is an omission whose exact runtime wording still requires validation."

  - finding_id: REPO-004
    path: ".claude/agents/apex-precap-week.md; .claude/agents/apex-precap-next-day.md; .claude/agents/apex-project-status.md"
    observation: "Preloaded skill names now match precap-week, precap-next-day, and project-status-overview."
    proposed_issue: "The master plan's Tier 1 preload defect is superseded."
    claim_status: "contradicted"
    recommended_action: "Remove this repair from future implementation scope; retain only a regression check."
    evidence: 100
    risk: 25
    impact: 78
    score_basis: "All three current agent files and the dedicated fixing commit were inspected."

  - finding_id: REPO-005
    path: ".claude/skills/*/SKILL.md"
    observation: "Descriptions vary: several are already compact and trigger-focused, while deterministic-markdown-patcher and some control-plane skills remain materially longer."
    proposed_issue: "A blanket rewrite of every description would alter already-good trigger metadata and may remove boundaries or invocation requirements."
    claim_status: "supported_with_qualification"
    recommended_action: "Generate a current inventory; shorten only measured offenders; preserve literal triggers, inputs, outputs, does-not-do clauses, and invocation-mode constraints."
    evidence: 84
    risk: 76
    impact: 87
    score_basis: "Representative live files were inspected, but the connector did not provide a complete, authoritative directory inventory or routing regression test."

  - finding_id: REPO-006
    path: ".claude/agents/*.md"
    observation: "Some descriptions contain load-bearing invocation-mode constraints, including instructions that main-conversation roles must not be spawned."
    proposed_issue: "Reducing descriptions by word count alone can remove execution semantics."
    claim_status: "directly_supported"
    recommended_action: "Optimize selectively and preserve execution-surface constraints even when shortening prose."
    evidence: 94
    risk: 82
    impact: 85
    score_basis: "Current Alfred and Meta Ops definitions explicitly carry invocation-mode constraints in their descriptions."

  - finding_id: REPO-007
    path: "apex-meta/orchestration/00-START-HERE.md"
    observation: "This is the final orchestration system map and law, while runtime machinery remains in skills, agents, scripts, schemas, and workflows."
    proposed_issue: "Tier 0 must not make the weekly skill the owner of system-wide orchestration doctrine."
    claim_status: "directly_observed"
    recommended_action: "Activation should point separately to the final orchestration map and to the domain-specific weekly loop; do not merge their ownership."
    evidence: 98
    risk: 77
    impact: 91
    score_basis: "The current start page explicitly distinguishes the system package from runtime machinery."

  - finding_id: REPO-008
    path: "apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md"
    observation: "The repository already has a canonical cross-system map, including the distinct purposes and status of both historical KBs."
    proposed_issue: "A new agents/skills map would duplicate an existing map unless it owns a demonstrably different inventory."
    claim_status: "directly_observed"
    recommended_action: "Extend or reference the existing map; do not create a parallel general map for Tier 0."
    evidence: 96
    risk: 61
    impact: 74
    score_basis: "The file explicitly declares itself the single map and documents both old KBs and current orchestration surfaces."
```

## 4. Retrieved Wiki Claims

```yaml
retrieved_wiki_claims:
  - claim_id: V1-C001
    kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    wiki_path: "wiki/summaries/reusable-old-agent-kb-patterns.md"
    heading: "Macro Synthesis"
    line_range: "39-45"
    claim: "Reusable patterns include compact doctrine surfaces, candidate-only learning, owner-validator separation, route contracts, and evidence-based closure."
    claim_label: "source_backed_summary"
    confidence: "high"
    source_pointers: ["AGENT_KB_INDEX.md", "meta_detective/APPENDIX_INTERNAL_MODES.md", "special_ops__hygiene_clean/ESSENCE.md", "special_ops__ai_handling_routing/ESSENCE.md"]
    present_in: {v1: true, v2: "partially"}

  - claim_id: V1-C002
    kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    wiki_path: "wiki/summaries/migration-to-claude-native-orchestration.md"
    heading: "Macro Synthesis"
    line_range: "37-47"
    claim: "Preserve source-grounded patterns rather than copying old runtime assumptions; current implementation requires repo verification."
    claim_label: "source_backed_summary"
    confidence: "mixed"
    source_pointers: ["batch04-reusable-patterns-and-migration.analysis.md", "semantic continuation report"]
    present_in: {v1: true, v2: true}

  - claim_id: V1-C003
    kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    wiki_path: "wiki/concepts/validation-and-routing-guardrails.md"
    heading: "Macro Synthesis / Micro Synthesis"
    line_range: "37-63"
    claim: "Trustworthy routing requires explicit evidence, gaps, stop conditions, owners, validators, and evidence-backed closure."
    claim_label: "source_backed_summary"
    confidence: "high"
    source_pointers: ["meta_detective/APPENDIX_INTERNAL_MODES.md", "AI Handling Routing ESSENCE", "Hygiene Clean ESSENCE"]
    present_in: {v1: true, v2: true}

  - claim_id: V2-C001
    kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    wiki_path: "wiki/summaries/agent-architecture.md"
    heading: "Core Summary / Key Claims"
    line_range: "20-41"
    claim: "Isolation comes from explicit role/state boundaries and controlled validator overlap; operational state determines permission."
    claim_label: "source_backed_summary"
    confidence: "high"
    source_pointers: ["managed/agents/AGENT_INDEX.md", "managed/rules/AGENT_SWARM_INTERACTION_CANON.md"]
    present_in: {v1: "principle only", v2: true}

  - claim_id: V2-C002
    kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    wiki_path: "wiki/summaries/resilient-iterative-orchestration.md"
    heading: "Core Summary / Macro-Meso-Micro"
    line_range: "20-41"
    claim: "Bounded work advances through explicit handoffs and build/review loop-back; macro/meso/micro terminology is an inference."
    claim_label: "behavioral_inference"
    confidence: "mixed"
    source_pointers: ["HOLDING_ORCHESTRATION_FLOW.md", "AGENT_HANDOFF_CONTRACTS.md", "AGENT_SWARM_INTERACTION_CANON.md"]
    present_in: {v1: "partial", v2: true}

  - claim_id: V2-C003
    kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    wiki_path: "wiki/summaries/claude-orchestration-implementation-brief.md"
    heading: "Decision / Use Guidance"
    line_range: "23-42"
    claim: "Build Claude orchestration around a small coordinator, explicit task-state records, specialist routes, and independent validation."
    claim_label: "source_backed_summary"
    confidence: "mixed"
    source_pointers: ["managed AGENT_INDEX", "AGENT_SWARM_INTERACTION_CANON", "Hermes skills documentation"]
    present_in: {v1: false, v2: true}
```

## 5. Raw Source Verification

```yaml
raw_source_verification:
  - claim_id: V1-C001
    source_id: "old-apex-agent-kb-primary"
    raw_path_or_pointer: "sources/primary/managed-agent-kb/AGENT_KB_INDEX.md"
    source_location: "Scaffold convention; Agent KB root map; Boundary note"
    verification_status: "directly_supported"
    qualifications: "Supports compact seeds and owned doctrine, not Claude-specific token limits."
    contradiction: null
    corrected_interpretation: "Use the layered ownership pattern; derive current paths and budgets from the live repository and runtime evidence."
    evidence: 97
    risk: 54
    impact: 89
    score_basis: "The raw file directly states compact seeds, rich doctrine roots, validators, and candidate-only learning."

  - claim_id: V1-C001
    source_id: "old-apex-agent-kb-primary"
    raw_path_or_pointer: "sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md"
    source_location: "Purpose; Operating doctrine; Read-budget profiles"
    verification_status: "directly_supported"
    qualifications: "Read-budget profiles are task classes, not numerical token budgets."
    contradiction: null
    corrected_interpretation: "Progressive disclosure is supported; a universal 400-500 token target is not established by this source."
    evidence: 98
    risk: 49
    impact: 90
    score_basis: "The raw source explicitly defines compression-only activation and targeted read modes."

  - claim_id: V1-C003
    source_id: "old-apex-agent-kb-primary"
    raw_path_or_pointer: "sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md"
    source_location: "Doctrine statement; Non-drift rules; Standard validation flow"
    verification_status: "directly_supported"
    qualifications: "Internal modes are historical role doctrine and do not require separate Claude agents."
    contradiction: null
    corrected_interpretation: "Preserve independent validation lenses without multiplying permanent agents or granting reviewers execution authority."
    evidence: 98
    risk: 72
    impact: 84
    score_basis: "The source repeatedly prohibits new-agent sprawl, self-approval, patching, and truth mutation."

  - claim_id: V2-C001
    source_id: "source-05bc8d6b022c9444"
    raw_path_or_pointer: "raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md"
    source_location: "Default operating stance; Operational state model; Delegation rules; Role-switching and separation rules"
    verification_status: "directly_supported"
    qualifications: "The source defines the historical system's BUILD/VERIFY/LOCK model; it does not prove current Apex must import that state machine."
    contradiction: "A mandatory current-runtime state-machine interpretation would exceed the source's authority."
    corrected_interpretation: "Preserve explicit permission, ownership, handoff, and independent-review properties using the least sufficient current mechanism."
    evidence: 99
    risk: 86
    impact: 93
    score_basis: "The raw canon is explicit, but historical-to-current promotion without need would create architecture inflation."

  - claim_id: V2-C002
    source_id: "source-401eeb0e75bfbd22"
    raw_path_or_pointer: "raw/other/managed/processes/HOLDING_ORCHESTRATION_FLOW.md"
    source_location: "Entry rule; Activation; Validation; Handoff expectation"
    verification_status: "directly_supported"
    qualifications: "It prefers the smallest activation set and one bounded flow; it does not endorse broad parallel swarm execution."
    contradiction: null
    corrected_interpretation: "Current orchestration should activate only the necessary roles and parallelize only demonstrably independent work."
    evidence: 96
    risk: 65
    impact: 86
    score_basis: "The source directly states smallest bounded activation and risk-proportional validation."

  - claim_id: V2-C003
    source_id: "source-8c534a90902556f2; source-05bc8d6b022c9444"
    raw_path_or_pointer: "raw/other/managed/agents/AGENT_INDEX.md; raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md"
    source_location: "Default routing; State and delegation rules"
    verification_status: "supported_with_qualification"
    qualifications: "The sources support coordinator, specialist, handoff, and validator principles. Claude-specific implementation wording is an operator/current-repo synthesis."
    contradiction: "The page's imperative Build Claude wording can be mistaken for a raw-source mandate."
    corrected_interpretation: "Use the historical sources as design evidence, then validate every current mechanism against current Apex files."
    evidence: 89
    risk: 79
    impact: 88
    score_basis: "The architecture principles are strongly supported, but the target-runtime prescription is not itself a historical source claim."
```

## 6. Omission Discovery

```yaml
omission_discovery:
  - finding_id: OM-001
    source_id: "old-apex-agent-kb-primary"
    source_location: "special_ops__hygiene_clean/ESSENCE.md#Read-budget-profiles"
    finding: "The raw source defines explicit targeted read modes, a stronger Tier 0 mechanism than the wiki's generic compact-doctrine summary."
    tier0_relevance: "Direct support for progressive disclosure and reduced always-loaded context."
    current_wiki_coverage: "partial"
    proposed_destination: "wiki/summaries/reusable-old-agent-kb-patterns.md"
    confidence: "high"
    claim_label: "source_backed_summary"
    dependencies: ["operator approval", "Phase 2 semantic edit"]
    contradictions: []
    evidence: 98
    risk: 35
    impact: 88
    score_basis: "The source contains a concrete loading mechanism omitted from the current synthesis."

  - finding_id: OM-002
    source_id: "old-apex-agent-kb-primary"
    source_location: "AGENT_KB_INDEX.md#Agent-KB-root-map; #Boundary-note"
    finding: "Activation seed, owned detailed doctrine, and shared governance are separate canonical layers."
    tier0_relevance: "Prevents moving every removed activation detail into one oversized skill or creating another duplicate map."
    current_wiki_coverage: "implicit_only"
    proposed_destination: "wiki/summaries/reusable-old-agent-kb-patterns.md"
    confidence: "high"
    claim_label: "source_backed_summary"
    dependencies: ["operator approval"]
    contradictions: []
    evidence: 97
    risk: 52
    impact: 92
    score_basis: "The raw index explicitly distinguishes these surfaces, but the compiled wiki compresses them into compact doctrine surfaces."

  - finding_id: OM-003
    source_id: "source-05bc8d6b022c9444"
    source_location: "AGENT_SWARM_INTERACTION_CANON.md#Default-operating-stance; #Delegation-rules"
    finding: "The default posture is one main active flow with bounded delegation, not broad swarm concurrency."
    tier0_relevance: "Guards against over-expanding the weekly orchestrator while optimizing activation and routing."
    current_wiki_coverage: "partial"
    proposed_destination: "wiki/summaries/resilient-iterative-orchestration.md"
    confidence: "high"
    claim_label: "source_backed_summary"
    dependencies: ["operator approval"]
    contradictions: ["Historical experiments may show broader swarm behavior."]
    evidence: 99
    risk: 63
    impact: 83
    score_basis: "The governing raw canon states the conservative default explicitly."

  - finding_id: OM-004
    source_id: "current_repository"
    source_location: ".claude/skills/weekly-orchestrator/SKILL.md"
    finding: "The live weekly skill already contains the corrected G5, project-mutation, review, and artifact-discovery responsibilities missing or stale in the activation copy."
    tier0_relevance: "Relocation should converge on the current skill rather than reconstructing the historical loop."
    current_wiki_coverage: "not_current_repo_specific"
    proposed_destination: "No historical KB page unless framed as a dated current-repo observation."
    confidence: "high"
    claim_label: "raw_source"
    dependencies: ["current repository ref"]
    contradictions: [".claude/Claude.md contains stale duplicate routing."]
    evidence: 99
    risk: 81
    impact: 96
    score_basis: "The current skill and activation file were compared directly."

  - finding_id: OM-005
    source_id: "current_repository_and_runtime_docs"
    source_location: "Claude activation, skill listing, preload, and compaction behavior"
    finding: "Both historical KBs lack current Claude-specific evidence for exact activation recognition, idle description cost, preload semantics, and compaction recovery."
    tier0_relevance: "These facts determine whether the proposed token reductions and recovery line actually work."
    current_wiki_coverage: "missing"
    proposed_destination: "Current Claude orchestration design KB, not either historical KB, after source intake and verification."
    confidence: "high"
    claim_label: "operator_question"
    dependencies: ["current official source verification", "runtime execution test"]
    contradictions: []
    evidence: 92
    risk: 84
    impact: 95
    score_basis: "The historical sources are product-specific to old Apex/OpenClaw/Hermes and cannot establish current Claude behavior."
```

## 7. Wiki Page Audit

```yaml
wiki_page_audit:
  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    wiki_path: "wiki/index-rerun-v2.md and canonical/rerun page pairs"
    status: "duplicate_or_misplaced"
    supported_claims: ["semantic rerun exists", "postflight remains required"]
    unsupported_claims: []
    missing_qualifications: ["which path is query-canonical before deterministic cleanup"]
    omitted_sources: []
    proposed_action: "After approval and terminal access, deterministically resolve duplicate ownership and rebuild index/retrieval artifacts."

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    wiki_path: "wiki/summaries/reusable-old-agent-kb-patterns.md"
    status: "verified_but_incomplete"
    supported_claims: ["compact doctrine", "internal-mode containment", "route contracts", "exact-span repair", "closure evidence"]
    unsupported_claims: []
    missing_qualifications: ["activation seed versus doctrine owner versus governance owner", "targeted read-budget profiles"]
    omitted_sources: ["Hygiene Clean read-budget profiles"]
    proposed_action: "Extend existing page after approve ingest."

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    wiki_path: "wiki/summaries/migration-to-claude-native-orchestration.md"
    status: "verified_complete"
    supported_claims: ["historical paths are evidence-only", "current repo verification required", "reuse patterns rather than runtime assumptions"]
    unsupported_claims: []
    missing_qualifications: []
    omitted_sources: []
    proposed_action: "No Tier 0 semantic change required beyond optional cross-link to layered activation ownership."

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
    wiki_path: "wiki/concepts/validation-and-routing-guardrails.md"
    status: "verified_but_incomplete"
    supported_claims: ["evidence-bound verdicts", "owner/validator routing", "closure by evidence"]
    unsupported_claims: []
    missing_qualifications: ["broad rewrite is not the default structural correction"]
    omitted_sources: ["one-file-before-many operating rule"]
    proposed_action: "Add narrow qualification after approve ingest."

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    wiki_path: "wiki/index.md"
    status: "outdated"
    supported_claims: ["17 pages are indexed in stored retrieval metadata"]
    unsupported_claims: ["Untitled topic labels as faithful registry representation"]
    missing_qualifications: ["two page files may be unenumerated", "three topics remain not_started"]
    omitted_sources: ["canonical topic-registry titles"]
    proposed_action: "Rebuild deterministic index and inspect generator behavior; do not hand-edit machine section."

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    wiki_path: "wiki/summaries/agent-architecture.md"
    status: "verified_but_incomplete"
    supported_claims: ["role/state distinction", "bounded validator overlap", "explicit handoffs"]
    unsupported_claims: []
    missing_qualifications: ["one-main-flow conservative default", "historical state machine is not automatically current runtime law"]
    omitted_sources: ["default operating stance qualification"]
    proposed_action: "Add qualification only if the page is used for current implementation decisions."

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    wiki_path: "wiki/summaries/resilient-iterative-orchestration.md"
    status: "verified_but_incomplete"
    supported_claims: ["bounded iterative loop", "explicit handoff minimums", "macro/meso/micro is inference"]
    unsupported_claims: []
    missing_qualifications: ["parallelism is bounded by independent work and conservative default"]
    omitted_sources: ["AGENT_SWARM_INTERACTION_CANON default posture"]
    proposed_action: "Extend after approve ingest."

  - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
    wiki_path: "wiki/summaries/claude-orchestration-implementation-brief.md"
    status: "partially_supported"
    supported_claims: ["small coordinator", "specialist routing", "explicit handoffs", "independent validation"]
    unsupported_claims: ["Any reading that treats BUILD/VERIFY/LOCK adoption as mandatory current Claude runtime law"]
    missing_qualifications: ["use the least sufficient current mechanism", "current repo verification decides implementation"]
    omitted_sources: ["current Apex authority-state and weekly orchestration implementation"]
    proposed_action: "Qualify historical-to-current translation after approve ingest."
```

## 8. Cross-KB Comparison

```yaml
cross_kb_comparison:
  shared_claims:
    - "Keep activation surfaces compact and route to richer owned doctrine."
    - "Candidate material does not become accepted truth by placement."
    - "Delegation and handoffs must be bounded and explicit."
    - "Important work requires an independent validator."
    - "Closure and advancement require evidence, not fluent prose or silence."
  v1_only:
    - "Five-file role-doctrine scaffold as a reusable pattern."
    - "Internal validation modes instead of multiplying permanent agents."
    - "Explicit read-budget profiles."
    - "Exact-span repair, one-file-before-many, and closure-by-evidence maintenance controls."
    - "Repo-execution routing card and historical-path authority discipline."
  v2_only:
    - "Formal BUILD/VERIFY/LOCK operational state model."
    - "Nine-agent first-wave activation and validator map."
    - "Conservative one-main-active-flow doctrine."
    - "EVD/IMP/RSK scoring bands and formal handoff packet fields."
    - "Explicit holding orchestration flow and current/finality state vocabulary."
  conflicts:
    - "V1 emphasizes selective doctrine reuse; V2's implementation brief can be read as more prescriptive about task-state records."
    - "V2 supports a historical state machine, while current Apex already implements candidate/verified/confirmed authority and review wiring without exposing the full state machine."
    - "V1 has weaker current-contract source custody; V2 has stronger copied-source custody but incomplete/stale index presentation."
  superseded_claims:
    - "The Tier 0 master plan's three preload-name mismatches are already repaired on current main."
    - "The activation file's APSU/G5 loop copy is superseded by the weekly-orchestrator skill contract."
  gaps_in_both:
    - "Current Claude activation filename recognition and case behavior."
    - "Measured current skill/agent inventory and always-loaded description footprint."
    - "Trigger-quality regression tests after description shortening."
    - "Current compaction/recovery behavior and exact reread requirements."
    - "Current artifact-path discovery behavior under missing, duplicate, or partially confirmed packets."
    - "Empirical token savings; no historical source supports the exact 400-500 token or 1.5-2.5K savings targets."
```

## 9. Phase 1 Extension Ledger

```yaml
phase1_extension_ledger:
  - source_analysis_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/agent-kb-index-tier0.analysis.md"
    proposed_wiki_change: "Add activation-seed, doctrine-owner, and governance-owner distinction."
    target_page: "wiki/summaries/reusable-old-agent-kb-patterns.md"
    change_type: "extend_existing_page"
    source_basis: "AGENT_KB_INDEX.md"
    operator_review_needed: true

  - source_analysis_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/hygiene-clean-tier0.analysis.md"
    proposed_wiki_change: "Add targeted read-budget profiles and narrow-repair qualification."
    target_page: "wiki/summaries/reusable-old-agent-kb-patterns.md; wiki/concepts/validation-and-routing-guardrails.md"
    change_type: "extend_and_qualify"
    source_basis: "special_ops__hygiene_clean/ESSENCE.md"
    operator_review_needed: true

  - source_analysis_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/ingest-analysis/managed-agent-index-tier0.analysis.md"
    proposed_wiki_change: "Preserve compact-seed and conservative activation guidance; distinguish it from current Claude implementation authority."
    target_page: "wiki/summaries/agent-architecture.md"
    change_type: "add_qualification"
    source_basis: "managed/agents/AGENT_INDEX.md"
    operator_review_needed: true

  - source_analysis_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/ingest-analysis/agent-swarm-interaction-canon-tier0.analysis.md"
    proposed_wiki_change: "Qualify state-machine translation and add one-main-flow controlled-delegation rule."
    target_page: "wiki/summaries/claude-orchestration-implementation-brief.md; wiki/summaries/resilient-iterative-orchestration.md"
    change_type: "qualify_and_extend"
    source_basis: "managed/rules/AGENT_SWARM_INTERACTION_CANON.md"
    operator_review_needed: true
```

## 10. Phase 2 Change Ledger

```yaml
phase2_change_ledger:
  approval_received: false
  pages_created: []
  pages_updated: []
  claims_corrected: []
  contradictions_added: []
  indexes_rebuilt: []
  validation_results:
    status: "not_run"
    reason: "Exact approval phrase not received and terminal execution unavailable."
```

## 11. Tier 0 Evidence Handoff

```yaml
tier0_evidence_handoff:
  validated_best_practices:
    - practice: "Reduce duplicated always-loaded orchestration content and retain pointers to canonical owners."
      status: "directly_supported"
      evidence: 96
      risk: 42
      impact: 97
      basis: "Both historical systems use compact activation anchors; the current activation file duplicates the weekly skill and contains stale routing."
    - practice: "Keep weekly stage routing, gates, packet validation, and loop-position logic in weekly-orchestrator."
      status: "directly_observed"
      evidence: 99
      risk: 39
      impact: 95
      basis: "The current skill already declares and implements this ownership."
    - practice: "Use one canonical owner per table, schema, path map, and routing rule."
      status: "directly_supported"
      evidence: 94
      risk: 44
      impact: 92
      basis: "Historical source layers and current stale duplication demonstrate both the intended pattern and failure mode."
    - practice: "Load detailed references only when the active task requires them."
      status: "directly_supported"
      evidence: 95
      risk: 31
      impact: 90
      basis: "V1 raw doctrine defines compression-only activation and explicit read-budget profiles."
    - practice: "Preserve independent review and executor/validator separation while simplifying activation."
      status: "directly_supported"
      evidence: 99
      risk: 87
      impact: 96
      basis: "Both KBs and the current final orchestration invariants make independent review load-bearing."
    - practice: "Use a narrow recovery instruction that rereads the active contract before gate decisions after context loss."
      status: "supported_with_qualification"
      evidence: 78
      risk: 35
      impact: 82
      basis: "File-backed resumability and targeted rereads are supported; exact compaction semantics require current runtime validation."

  rejected_best_practices:
    - proposal: "Rewrite every skill description to an arbitrary word cap in one pass."
      status: "unsupported"
      reason: "Many current descriptions are already compact; trigger quality and execution-surface constraints may be damaged."
      evidence: 86
      risk: 79
      impact: 85
    - proposal: "Rewrite every agent description and add a system marker regardless of current content."
      status: "unsupported"
      reason: "Several descriptions already carry system context and load-bearing invocation-mode constraints."
      evidence: 90
      risk: 82
      impact: 80
    - proposal: "Implement the three preload-name repairs from the plan."
      status: "contradicted"
      reason: "The names already match on current main."
      evidence: 100
      risk: 24
      impact: 77
    - proposal: "Import BUILD/VERIFY/LOCK as a new current runtime state machine during Tier 0."
      status: "unsupported"
      reason: "The historical principles are useful, but no demonstrated Tier 0 gap requires a new state machine."
      evidence: 92
      risk: 91
      impact: 89
    - proposal: "Create a new general agents/skills map."
      status: "unsupported"
      reason: "The repository already has an orchestration systems index and system start map; another general map would duplicate ownership."
      evidence: 95
      risk: 58
      impact: 66

  newly_discovered_mechanisms:
    - "Targeted read-budget profiles as a concrete progressive-disclosure mechanism."
    - "Three-layer canonical ownership: activation seed, detailed doctrine owner, shared governance owner."
    - "Use relocation to eliminate stale duplicates instead of repairing every copy."
    - "Preserve main-conversation versus spawned-agent invocation constraints during description optimization."
    - "Treat trigger regression as a required acceptance check for description changes."

  unresolved_conflicts:
    - "Global Apex KB default compile policy versus these KB-local exact approval gates."
    - "Historical BUILD/VERIFY/LOCK model versus the simpler current authority-state and operator-validation mechanism."
    - "KB v2 generated index labels versus canonical topic registry."
    - "The exact runtime-recognized activation filename/case has not been execution-tested."
    - "The claimed numeric token targets and savings remain unverified."

  micro_implementation_guidance:
    - "Re-read current targets at the implementation commit; do not patch from this packet's historical line numbers."
    - "Compact .claude/Claude.md by subtraction and pointers, not by moving every table wholesale into another always-read file."
    - "Keep global constraints global; keep weekly loop mechanics in weekly-orchestrator; keep system-wide law in apex-meta/orchestration/."
    - "Remove stale duplicate loop text rather than normalizing two canonical copies."
    - "Inventory all active SKILL.md and agent descriptions before selecting offenders."
    - "Preserve literal trigger phrases, inputs, outputs, does-not-do boundaries, and invocation-mode semantics."
    - "Add a compact recovery rule only after validating current compaction behavior."
    - "Do not alter semantic KB pages as part of the runtime Tier 0 patch."

  exact_candidate_paths:
    - ".claude/Claude.md"
    - ".claude/skills/weekly-orchestrator/SKILL.md"
    - "apex-meta/orchestration/00-START-HERE.md"
    - "apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md"
    - ".claude/skills/*/SKILL.md (measured offenders only)"
    - ".claude/agents/*.md (measured offenders only)"

  required_preimplementation_checks:
    - "Pin the current main commit and read every candidate target completely."
    - "Confirm the runtime-recognized activation file path and filename case."
    - "Generate an exact active skill and agent inventory excluding backups, staging, source-knowledge, and historical variants."
    - "Measure description bytes, words, and estimated tokens before selecting targets."
    - "Map every removed activation rule to exactly one current canonical destination."
    - "Verify all stage-agent skills values equal target skill names."
    - "Run trigger-routing regression checks before and after description changes."
    - "Run no-loss grep or structured checks for global constraints and loop responsibilities."
    - "Run current repository lint/tests plus Apex orchestration regression fixtures."
    - "Run KB status, health, lint, audit, quality, and retrieval stale checks separately for each KB if Phase 2 is later approved."
```

## 12. Operator Decision

**Established:** The core Tier 0 architecture should be relocation and deduplication, not redesign. The weekly skill is already the canonical operational owner of the weekly loop, while the final orchestration package owns system-wide law.

**Changed in the KB:** Four Phase 1 analysis files were added. No wiki page, manifest, index, audit resolution, or raw source was changed.

**Unresolved:** Exact runtime activation recognition, measured token savings, complete description inventory, routing regression, and deterministic KB health remain execution-dependent.

**Later implementation worker:** May safely prepare a bounded plan to compact the activation file, preserve canonical pointers, add a qualified recovery instruction, and optimize only measured description offenders. The worker may not treat this packet as a ready patch or proof of successful application.

**Approval gate:** To authorize semantic KB Phase 2, the operator must provide exactly:

`approve ingest`
