---
analysis_id: claude-skill-design-corpus-analysis
kb_slug: claude-skill-design
source_slug: corpus
phase: ingest_phase_1
status: operator_review_needed
phase_2_allowed: false
required_confirmation_phrase: "approve ingest"
created_by: apex-kb
created_at: "2026-06-25T12:09:30Z"
---

# Phase 1 Ingest Analysis: Corpus

```yaml
source_ref:
  source_path: "apex-meta/kb/claude-skill-design/sources/"
  source_type: "other"
  source_storage_mode: "pointer_only"
  source_hash: "e25e529a523169c0a01ccff7942a8bcc642354143e6a27ccf7094eead6d45630"
  hash_algorithm: "sha256"
  no_hash_reason: "NA"
preflight:
  report_available: true
  status: "failed"
  existing_manifest_entry: false
  existing_phase_1_analysis: false
  index_status: "missing"
  preflight_review_flags:
    - "missing kb-schema.md"
    - "missing source-manifest.json"
    - "missing wiki/index.md"
    - "missing raw/articles, raw/papers, raw/notes, raw/refs"
    - "missing audit, outputs/queries, log before this run report"
operator_gate:
  phase_2_allowed: false
  required_confirmation_phrase: "approve ingest"
```

## 1. Source Identity

```yaml
source_identity:
  title: "Claude Skill Design source corpus"
  author_or_origin: "mixed: official Anthropic, Agent Skills specification, official repositories, academic papers, secondary navigation pages, and operator notes"
  publication_or_creation_date: "mixed"
  source_authority_level: "mixed"
  source_authority_rationale: >
    The corpus combines primary official guidance and repos with academic/security analysis,
    secondary navigation sources, and operator-supplied design notes. Claims must retain
    their source tier during Phase 2.
  source_scope: >
    Skill package anatomy, progressive disclosure, SKILL.md frontmatter, description
    routing, support-file boundaries, scripts/references/assets, testing/evaluation,
    MCP plus skills, distribution, and security/governance concerns.
  source_limitations:
    - "The installed Apex KB contract expects raw/ and kb-schema.md, but this KB currently uses sources/ as the working corpus."
    - "The existing source-inventory files are not a substitute for manifests/source-manifest.json under the installed script contract."
    - "No Phase 2 wiki pages exist yet, so contradictions against compiled KB pages could not be checked."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: >
    The corpus supports a source-grounded KB about designing reliable Claude and Agent Skills with progressive disclosure, precise routing, bounded support files, testable workflows, and explicit security review.
  compact_summary: >
    Official sources establish the baseline skill model: a SKILL.md entrypoint with YAML
    frontmatter, optional references/scripts/assets, and progressive disclosure to reduce
    context load while preserving task-specific expertise. Official examples and repositories
    show concrete patterns for routing descriptions, support-file organization, tool/script
    boundaries, and skill-specific workflows. Academic and security sources add ecosystem,
    validation, and semantic supply-chain concerns. Operator notes add Apex-specific quality
    criteria such as machine readability, token efficiency, resilient simplicity, and package
    boundaries. The corpus is ready for operator review, but Phase 2 should wait until the KB
    scaffold gap is resolved or explicitly accepted.
  relevant_to_kb_because:
    - "It contains primary and example evidence for Claude skill design."
    - "It separates official, academic, secondary, and operator-supplied source tiers."
    - "It includes both design guidance and risk/governance material."
  likely_not_relevant_for:
    - "General Apex task planning."
    - "Running production skill evals directly."
    - "Creating wiki pages before operator approval."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "sources/curated/official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#fundamentals"
      reason: "Defines skill anatomy, portability, composability, and progressive disclosure."
      extraction_priority: "high"
    - section_ref: "sources/curated/repo-extracts/*__SKILL.md"
      reason: "Shows real SKILL.md descriptions and support-file routing patterns."
      extraction_priority: "high"
    - section_ref: "sources/curated/academic/arxiv-skill-md-semantic-supply-chain.html.meta.md"
      reason: "Frames SKILL.md wording and discovery as a semantic supply-chain risk surface."
      extraction_priority: "medium"
  reusable_definitions:
    - term: "skill"
      source_pointer: "official-pdfs complete guide, Fundamentals"
      definition_candidate: "A folder containing SKILL.md plus optional scripts, references, and assets that teaches Claude a repeatable task or workflow."
      confidence: "high"
    - term: "progressive disclosure"
      source_pointer: "official-pdfs complete guide, Fundamentals"
      definition_candidate: "A three-level loading model: frontmatter always available, SKILL.md loaded when relevant, and linked files loaded only as needed."
      confidence: "high"
  reusable_processes:
    - process_name: "two-tier source promotion before KB ingest"
      source_pointer: "sources/curated/manifests and sources/operator-supplied/notes/ClaudePhase1FilePreparation.md"
      process_summary: "Keep immutable acquisition archives separate from KB-specific source corpora, then run Phase 1 only against the KB source folder."
      possible_apex_use: "Preserve traceability while keeping each KB's evidence corpus clear."
      confidence: "medium"
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "progressive-disclosure"
    concept_label: "Progressive disclosure"
    source_pointers:
      - "sources/curated/official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#fundamentals"
      - "sources/curated/official-docs/agentskills-specification.html"
    concept_summary: "Skills minimize always-loaded instructions by putting routing metadata in frontmatter, procedural guidance in SKILL.md, and large details in references/scripts/assets."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/progressive-disclosure.md"
    related_existing_pages:
      - "none"
    confidence: "high"
    review_flags: []
  - concept_slug: "skill-routing-description"
    concept_label: "Skill routing description"
    source_pointers:
      - "sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md#frontmatter-rules"
      - "sources/curated/repo-extracts/anthropics-skills__skills__skill-creator__SKILL.md"
    concept_summary: "The description is the primary trigger surface and should state when the skill applies, accepted inputs, output, and boundaries."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/skill-routing-description.md"
    related_existing_pages:
      - "none"
    confidence: "medium"
    review_flags:
      - "operator note may be more prescriptive than official examples; preserve source tier."
  - concept_slug: "semantic-supply-chain-risk"
    concept_label: "Semantic supply-chain risk"
    source_pointers:
      - "sources/curated/academic/arxiv-skill-md-semantic-supply-chain.html.meta.md"
    concept_summary: "Skill package text and descriptions can influence discovery, selection, and behavior, making source authority and review important."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/semantic-supply-chain-risk.md"
    related_existing_pages:
      - "none"
    confidence: "medium"
    review_flags:
      - "academic source needs deeper read before strong claims."
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "anthropic"
    entity_label: "Anthropic"
    entity_type: "organization"
    source_pointers:
      - "sources/curated/official-docs/*.meta.md"
      - "sources/curated/official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md"
    entity_summary: "Primary source origin for Claude skill guidance and official examples."
    proposed_page_action: "create"
    proposed_page_path: "wiki/entities/anthropic.md"
    related_existing_pages:
      - "none"
    confidence: "high"
    review_flags: []
  - entity_slug: "agent-skills-specification"
    entity_label: "Agent Skills Specification"
    entity_type: "framework"
    source_pointers:
      - "sources/curated/official-docs/agentskills-specification.html.meta.md"
    entity_summary: "Open specification source for SKILL.md package format and progressive disclosure."
    proposed_page_action: "create"
    proposed_page_path: "wiki/entities/agent-skills-specification.md"
    related_existing_pages:
      - "none"
    confidence: "high"
    review_flags: []
```

## 6. Claim Candidates

```yaml
claim_candidates:
  - claim_id: "C001"
    claim_text: "A Claude skill is packaged as a folder with required SKILL.md and optional scripts, references, and assets."
    source_pointer: "sources/curated/official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#what-is-a-skill"
    claim_label: "raw_source"
    applies_to:
      - "skill-package-anatomy"
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/skill-package-anatomy.md"
    review_flags: []
  - claim_id: "C002"
    claim_text: "Progressive disclosure is a central mechanism for balancing specialized behavior with context efficiency."
    source_pointer: "sources/curated/official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#progressive-disclosure"
    claim_label: "source_backed_summary"
    applies_to:
      - "progressive-disclosure"
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/progressive-disclosure.md"
    review_flags: []
  - claim_id: "C003"
    claim_text: "Skill descriptions and package contents should be treated as a governance and security review surface."
    source_pointer: "sources/curated/academic/arxiv-skill-md-semantic-supply-chain.html.meta.md"
    claim_label: "behavioral_inference"
    applies_to:
      - "semantic-supply-chain-risk"
    confidence: "medium"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/semantic-supply-chain-risk.md"
    review_flags:
      - "needs deeper paper extraction before Phase 2."
```

## 7. Contradiction Candidates

```yaml
contradiction_candidates:
  status: "possible"
  items:
    - contradiction_id: "X001"
      severity: "medium"
      source_claim: "Operator note says every SKILL.md description must begin with exact string 'Use this skill when'."
      conflicting_existing_claim: "Official examples in the corpus may use more varied description wording."
      current_source_pointer: "sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md#frontmatter-rules"
      existing_source_pointer: "sources/curated/repo-extracts/*__SKILL.md"
      interpretation: "This may be an Apex house rule rather than an official Claude requirement."
      proposed_handling: "ask_operator"
      review_required: true
```

## 8. Proposed Wiki Page Changes

```yaml
proposed_wiki_page_changes:
  summaries:
    - action: "create"
      path: "wiki/summaries/claude-skill-design-corpus.md"
      reason: "A corpus-level summary would orient later users after Phase 2 approval."
      source_pointers_required: true
  concepts:
    - action: "create"
      path: "wiki/concepts/progressive-disclosure.md"
      reason: "Core cross-cutting mechanism."
      source_pointers_required: true
    - action: "create"
      path: "wiki/concepts/skill-package-anatomy.md"
      reason: "Foundational package structure concept."
      source_pointers_required: true
    - action: "create"
      path: "wiki/concepts/semantic-supply-chain-risk.md"
      reason: "Security and governance theme."
      source_pointers_required: true
  entities:
    - action: "create"
      path: "wiki/entities/anthropic.md"
      reason: "Primary source authority entity."
      source_pointers_required: true
  index:
    semantic_summary_update_needed: true
    proposed_index_notes:
      - "Add source-tier navigation: official guidance, official examples, academic/security, secondary navigation, operator notes."
```

## 9. Proposed Manifest Updates

```yaml
proposed_manifest_updates:
  source_entry:
    source_id: "claude-skill-design-corpus"
    source_path: "apex-meta/kb/claude-skill-design/sources/"
    source_hash: "e25e529a523169c0a01ccff7942a8bcc642354143e6a27ccf7094eead6d45630"
    hash_algorithm: "sha256"
    ingest_status: "phase_1_complete_operator_review_needed"
    ingest_analysis_path: "ingest-analysis/corpus.analysis.md"
    generated_pages: []
    semantic_tags:
      - "skill-design"
      - "progressive-disclosure"
      - "skill-security"
    concept_candidates:
      - "progressive-disclosure"
      - "skill-package-anatomy"
      - "semantic-supply-chain-risk"
    entity_candidates:
      - "anthropic"
      - "agent-skills-specification"
    review_flags:
      - "kb_scaffold_incomplete"
      - "possible_house_rule_vs_official_guidance"
```

## 10. Open Questions

```yaml
open_questions:
  operator_questions:
    - question_id: "Q001"
      question: "Should Phase 2 proceed before creating kb-schema.md and source-manifest.json, or should the KB scaffold be repaired first?"
      blocks_phase_2: true
      related_source_pointer: "preflight report"
    - question_id: "Q002"
      question: "Should Apex-specific operator notes be treated as normative house rules or secondary design opinions when they exceed official guidance?"
      blocks_phase_2: true
      related_source_pointer: "sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md"
  kb_questions:
    - question_id: "KQ001"
      question: "Which concept taxonomy should be canonical for the KB: anatomy, routing, progressive disclosure, validation, security, examples, and distribution?"
      proposed_handling: "ask_operator"
      related_pages:
        - "none"
```

## 11. Review Flags

```yaml
review_flags:
  - flag_id: "RF001"
    type: "missing_context"
    severity: "high"
    summary: "Installed Apex KB contract required paths are missing."
    required_before_phase_2: true
    proposed_resolution: "Create or approve a KB-local schema and source manifest before wiki generation."
  - flag_id: "RF002"
    type: "source_authority"
    severity: "medium"
    summary: "Corpus mixes official, academic, secondary, and operator notes."
    required_before_phase_2: true
    proposed_resolution: "Approve a source authority ordering in kb-schema.md."
```

## 12. Operator Review Gate

```yaml
operator_review_gate:
  phase_1_result: "blocked"
  phase_2_recommendation: "defer"
  phase_2_allowed_now: false
  required_operator_phrase: "approve ingest"
  recommended_operator_decision:
    decision: "defer"
    rationale: "The corpus is semantically useful, but deterministic preflight failed because the KB scaffold is incomplete."
  if_approved_next_actions:
    - "Repair or approve the KB schema and manifest gap."
    - "Generate approved summary, concept, and entity pages with source pointers."
    - "Run deterministic postflight lint."
  if_rejected_next_actions:
    - "Do not generate wiki pages."
    - "Keep this analysis as Phase 1 evidence."
```
