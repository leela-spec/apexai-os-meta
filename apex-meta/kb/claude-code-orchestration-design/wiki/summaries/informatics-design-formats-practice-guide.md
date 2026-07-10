---
title: "Informatics Design, Formats, and Practice Guide"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "informatics-design-formats-practice-guide"
source_refs:
  - source_id: "claude-skill-promptflow-design-guidance"
    source_path: "raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md"
    source_hash: "a168e103d089b17e"
    source_pointer: "lines 305-393, Part 2 Mandatory Rules for Every Future Claude Skill Prompt Flow"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "1b61082b311fd82d"
    source_pointer: "claims B01-C002, B01-C010"
    source_storage_mode: "pointer_only"
created_at: "2026-07-10T21:00:00Z"
updated_at: "2026-07-10T21:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Informatics Design, Formats, and Practice Guide

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "claude-skill-promptflow-design-guidance"
    rationale: "This is the one source in the corpus that states formatting/structure rules as explicit, checkable instructions rather than general best-practice prose -- directly on-topic for a 'formats and practice guide' page rather than a restatement of what a skill is."
    coverage: "Ten mandatory structural rules for authoring Claude skill packages, each with an instruction and an enforcement check."
  - rank: 2
    source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Independently-extracted Phase 1 claims corroborate the same progressive-disclosure and single-source-of-truth principles from a different primary source (the Agent Skills specification), rather than from this operator's own notes alone."
    coverage: "Progressive disclosure structure; the reusable design rule to keep SKILL.md as routing logic and move heavy contracts elsewhere."
```

## Macro / Meso / Micro

### Macro

Good informatics design for an LLM-consumed package is not a style preference -- it is what makes a document *checkable* rather than merely readable. The source guidance frames every rule around one property: can a rule violation be caught by a deterministic check before the document is used, or does it require someone to notice by reading? Two rules make this concrete and matter beyond skill authoring specifically: **rule_08** requires every schema or contract structure to be defined exactly once, with other sections referencing it rather than copying it -- the same duplication problem this KB's own architecture review found repeatedly across `SKILL.md`, `kb-contract.md`, and the lifecycle-state-machine reference. **rule_09** requires identical key names for the same concept across every file in a package, so a downstream reader or script never has to guess whether `source_id` and `source_pointer` in one file mean the same thing as `source` and `pointer` in another.

### Meso

The rules cluster into three enforceable categories rather than a flat checklist. Structural rules govern shape: YAML blocks must use consistent 2-space indentation and be self-checked against a standard parser before output (rule_01); numeric and enum constraints must be typed (`type: integer / min: 1 / max: 100`) rather than written as prose strings like "integer 1-100" (rule_07), because a typed constraint is machine-validatable and a prose one is not. Content-density rules govern grain: a procedure step is one complete action plus one observable outcome, targeting 5-8 steps for a single-responsibility skill, and a procedure exceeding 10 steps is a scope violation rather than something to document more thoroughly (rule_03) -- this is the same principle behind this KB's own per-page compile density checks, just applied to procedure design instead of wiki pages. Consistency rules govern the whole package: canonical key names (rule_09) and single schema definitions (rule_08) exist specifically so that adding a new file to a package can't silently introduce a second, drifting definition of something already defined.

### Micro

Each rule pairs an instruction with a named enforcement mechanism, which is itself the practice worth generalizing: rule_02 requires every `SKILL.md` frontmatter description to begin with the literal string "Use this skill when," name what input is accepted, what output is produced, and what the skill explicitly does not do, capped at 75 words, checked by exact string match before the file is accepted (lines 320-329). Rule_05 requires a Failure Modes section as a YAML block, each entry exactly a `trigger` and a `correction` sentence, capped at 8 modes -- if a skill needs more failure modes than that, the rule's position is that the skill's scope is too broad, not that the section needs to grow (lines 350-357). The pattern across all ten rules is the same: state the rule, state the exact enforcement check, and treat a rule with no enforcement check as incomplete.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Every schema or contract structure in a package must be defined exactly once; other sections reference it by key rather than copying it, and a prompt that creates a duplicate definition must merge it into one canonical block before output."
    source_pointer: "Claude_Skill_PromptFlow_Design_Guidance_v1.md lines 376-383 (rule_08)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "All files in one package must use identical key names for the same concept, checked against a canonical key-names dictionary before generating each file; synonyms or alternative names for an established key are not permitted."
    source_pointer: "Claude_Skill_PromptFlow_Design_Guidance_v1.md lines 385-392 (rule_09)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Numeric range and enum constraints must be written as typed fields (type/min/max, or type/allowed-list), never as prose strings like 'integer 1-100', so a constraint can be validated by a schema check rather than read and interpreted."
    source_pointer: "Claude_Skill_PromptFlow_Design_Guidance_v1.md lines 367-374 (rule_07)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "A procedure step is defined as one complete action plus one observable outcome; a procedure exceeding roughly 10 steps is treated as a scope violation in the skill's design, not a case for a longer procedure."
    source_pointer: "Claude_Skill_PromptFlow_Design_Guidance_v1.md lines 331-339 (rule_03)"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What makes a skill package or KB document well-formatted for an LLM to actually parse and follow, not just readable?"
    leads_to: "wiki/summaries/informatics-design-formats-practice-guide.md"
    rationale: "Gives the specific, checkable rules rather than general advice about clarity."
  - question: "Why does this KB keep finding the same information duplicated across multiple files?"
    leads_to: "wiki/summaries/informatics-design-formats-practice-guide.md"
    rationale: "rule_08's single-schema-definition requirement names exactly this failure mode and its fix."
  - related_page: "wiki/concepts/yaml-first-artifact-design.md"
    relation: "Narrower concept page on YAML-first structure; this summary covers the fuller rule set it draws from."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The source guidance is written for GPT agents generating Claude skill packages specifically -- it is not independently verified whether all ten rules apply equally to KB wiki-page authoring (a different artifact type) rather than SKILL.md packages."
    source_pointer: "Claude_Skill_PromptFlow_Design_Guidance_v1.md lines 2-6"
    proposed_handling: "revisit_source"
  - id: U002
    description: "This page cites only rules 1-3, 7, 8, 9 as Key Claims; rules 4, 5, 6, 10 (supporting-files format, failure-modes format, completion-gate format, prompt-0 rule) exist in the same source but are not yet independently verified against this KB's own SKILL.md for compliance."
    proposed_handling: "audit_item"
