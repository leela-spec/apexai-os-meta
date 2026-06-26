---
analysis_id: claude-skill-design-official-guidance-analysis
kb_slug: claude-skill-design
source_slug: official-guidance
phase: ingest_phase_1
status: operator_review_needed
phase_2_allowed: false
required_confirmation_phrase: "approve ingest"
created_by: apex-kb
created_at: "2026-06-25T12:09:30Z"
---

# Phase 1 Ingest Analysis: Official Guidance

```yaml
source_ref:
  source_path:
    - "apex-meta/kb/claude-skill-design/sources/curated/official-docs/"
    - "apex-meta/kb/claude-skill-design/sources/curated/official-pdfs/"
  source_type: "article"
  source_storage_mode: "pointer_only"
  source_hashes:
    official_docs: "42db62082288683e9ef6037119853fed28f4b5f73f1eca868ddd6c7ff3de4efb"
    official_pdfs: "af2894549966d0ccba8e9e1571096274b083a2b012866126e83da6ae12cb3bca"
  hash_algorithm: "sha256"
  no_hash_reason: "NA"
operator_gate:
  phase_2_allowed: false
  required_confirmation_phrase: "approve ingest"
```

## 1. Source Identity

```yaml
source_identity:
  title: "Official Claude and Agent Skills guidance"
  author_or_origin: "Anthropic and Agent Skills specification sources"
  publication_or_creation_date: "mixed"
  source_authority_level: "primary"
  source_authority_rationale: "Official Anthropic docs and the Agent Skills specification are primary or high-authority sources for the package model."
  source_scope: "Skill anatomy, progressive disclosure, MCP plus skills, planning/design, testing, iteration, and distribution."
  source_limitations:
    - "HTML extraction may include navigation boilerplate."
    - "The long-form guide is converted Markdown from a PDF and may omit images."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: "Official guidance defines skills as portable, composable folders that encode repeatable workflows through SKILL.md and optional support resources."
  compact_summary: >
    The official guide frames skills as reusable task/workflow packages that reduce repeated prompting.
    It emphasizes SKILL.md as required, with scripts, references, and assets as optional support files.
    Progressive disclosure is central: frontmatter routes, SKILL.md instructs, and linked files supply
    deeper context only when needed. The guide also distinguishes MCP as connectivity from skills as
    workflow knowledge, making skills the recipe layer over tool access. Planning, testing, iteration,
    and distribution are treated as part of skill quality rather than afterthoughts.
  relevant_to_kb_because:
    - "Provides canonical source authority for skill structure."
    - "Defines core vocabulary for Phase 2 concept pages."
  likely_not_relevant_for:
    - "Apex-specific package policy unless corroborated by operator notes."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#fundamentals"
      reason: "Defines what a skill is and lists required/optional folder contents."
      extraction_priority: "high"
    - section_ref: "official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#progressive-disclosure"
      reason: "Explains the three-level loading model."
      extraction_priority: "high"
    - section_ref: "official-docs/agentskills-specification.html"
      reason: "Defines open specification expectations."
      extraction_priority: "high"
  reusable_definitions:
    - term: "SKILL.md"
      source_pointer: "official-pdfs complete guide, What is a skill?"
      definition_candidate: "The required Markdown instruction file in a skill package, with YAML frontmatter used for discovery/routing."
      confidence: "high"
  reusable_processes:
    - process_name: "skill planning and design"
      source_pointer: "official-pdfs complete guide, Planning and design"
      process_summary: "Select a repeatable workflow, define the package structure, write routing instructions, add support files only when needed, test, and iterate."
      possible_apex_use: "Use as a canonical flow for future skill-design concept and checklist pages."
      confidence: "medium"
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "skill-package-anatomy"
    concept_label: "Skill package anatomy"
    source_pointers:
      - "official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#what-is-a-skill"
    concept_summary: "A skill package consists of required SKILL.md plus optional scripts, references, and assets."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/skill-package-anatomy.md"
    related_existing_pages: ["none"]
    confidence: "high"
    review_flags: []
  - concept_slug: "mcp-plus-skills"
    concept_label: "MCP plus Skills"
    source_pointers:
      - "official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#for-mcp-builders-skills-connectors"
    concept_summary: "MCP provides tool/data access while skills encode how to use that access reliably."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/mcp-plus-skills.md"
    related_existing_pages: ["none"]
    confidence: "high"
    review_flags: []
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "claude"
    entity_label: "Claude"
    entity_type: "tool"
    source_pointers:
      - "official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md"
    entity_summary: "The target assistant/runtime for the skill guidance."
    proposed_page_action: "create"
    proposed_page_path: "wiki/entities/claude.md"
    related_existing_pages: ["none"]
    confidence: "high"
    review_flags: []
```

## 6. Claim Candidates

```yaml
claim_candidates:
  - claim_id: "C001"
    claim_text: "Skills are useful for repeatable workflows and for standardizing how Claude performs recurring tasks."
    source_pointer: "official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#introduction"
    claim_label: "source_backed_summary"
    applies_to: ["skill-use-cases"]
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/skill-use-cases.md"
    review_flags: []
  - claim_id: "C002"
    claim_text: "Skills should be portable across Claude.ai, Claude Code, and API when their dependencies are supported."
    source_pointer: "official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md#portability"
    claim_label: "raw_source"
    applies_to: ["skill-portability"]
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/skill-portability.md"
    review_flags: []
```

## 7. Contradiction Candidates

```yaml
contradiction_candidates:
  status: "none_detected"
  items: []
```

## 8. Proposed Wiki Page Changes

```yaml
proposed_wiki_page_changes:
  summaries:
    - action: "create"
      path: "wiki/summaries/official-guidance.md"
      reason: "Official guidance should anchor the KB's primary claims."
      source_pointers_required: true
  concepts:
    - action: "create"
      path: "wiki/concepts/skill-package-anatomy.md"
      reason: "Foundational official concept."
      source_pointers_required: true
    - action: "create"
      path: "wiki/concepts/progressive-disclosure.md"
      reason: "Core design mechanism."
      source_pointers_required: true
  entities:
    - action: "create"
      path: "wiki/entities/claude.md"
      reason: "Runtime/product entity."
      source_pointers_required: true
  index:
    semantic_summary_update_needed: true
    proposed_index_notes:
      - "Official guidance is the primary authority tier for core definitions."
```

## 9. Proposed Manifest Updates

```yaml
proposed_manifest_updates:
  source_entry:
    source_id: "official-guidance"
    source_path: "apex-meta/kb/claude-skill-design/sources/curated/official-docs/"
    source_hash: "42db62082288683e9ef6037119853fed28f4b5f73f1eca868ddd6c7ff3de4efb"
    hash_algorithm: "sha256"
    ingest_status: "phase_1_complete_operator_review_needed"
    ingest_analysis_path: "ingest-analysis/official-guidance.analysis.md"
    generated_pages: []
    semantic_tags: ["official", "skill-anatomy", "progressive-disclosure"]
    concept_candidates: ["skill-package-anatomy", "progressive-disclosure", "mcp-plus-skills"]
    entity_candidates: ["claude", "anthropic", "agent-skills-specification"]
    review_flags: []
```

## 10. Open Questions

```yaml
open_questions:
  operator_questions:
    - question_id: "Q001"
      question: "Should the PDF guide and web docs be merged into one official-guidance summary or kept as separate source summaries?"
      blocks_phase_2: false
      related_source_pointer: "official-docs and official-pdfs"
  kb_questions: []
```

## 11. Review Flags

```yaml
review_flags: []
```

## 12. Operator Review Gate

```yaml
operator_review_gate:
  phase_1_result: "ready_for_operator_review"
  phase_2_recommendation: "approve_with_changes"
  phase_2_allowed_now: false
  required_operator_phrase: "approve ingest"
  recommended_operator_decision:
    decision: "approve_with_changes"
    rationale: "Official guidance is high-value and low-conflict, but KB scaffold gaps should be resolved before generation."
```
