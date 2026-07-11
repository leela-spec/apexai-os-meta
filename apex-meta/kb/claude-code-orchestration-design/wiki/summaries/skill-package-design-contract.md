---
title: "Skill Package Design Contract"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "skill-package-design-contract"
source_refs:
  - source_id: "anthropic-complete-guide-to-building-skills"
    source_path: "raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23/raw/official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md"
    source_hash: "NA"
    source_pointer: "lines 65-101 (progressive disclosure), 318-397 (frontmatter field requirements), 1322-1339 (large-context solutions / size limits)"
    source_storage_mode: "pointer_only"
  - source_id: "anthropics-skill-creator-skill-md"
    source_path: "raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23/raw/repo-extracts/anthropics-skills__skills__skill-creator__SKILL.md"
    source_hash: "NA"
    source_pointer: "lines 1-40, official skill-creator SKILL.md frontmatter and body"
    source_storage_mode: "pointer_only"
created_at: "2026-07-11T00:00:00Z"
updated_at: "2026-07-11T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "compact-activation-file"
  - "compact-activation-seed"
  - "progressive-disclosure-for-agent-kbs"
  - "skill-boundary"
related_entities:
  - "agent-skills-standard"
review_flags: []
---

# Skill Package Design Contract

## Core Summary

A Claude Agent Skill is a folder, not a prompt snippet: `SKILL.md` (required) plus optional `scripts/`, `references/`, and `assets/` directories. The entire design contract exists to serve one mechanism — **progressive disclosure** — so that Claude only pays token cost for what a given task actually needs. This page covers the official (P0) structural and frontmatter rules, sourced directly from Anthropic's own "Complete Guide to Building Skills for Claude" and the official `skill-creator` skill, which is the reference implementation of everything the guide prescribes.

## What This Adds

```yaml
adds:
  - "The exact three-level progressive disclosure model (frontmatter / body / linked files) and what triggers each level to load."
  - "Hard frontmatter validation rules: naming, description content requirements, character limits, no XML tags."
  - "Concrete size thresholds for when a skill has grown too large (SKILL.md under 5,000 words; move detail to references/)."
clarifies:
  - "The description field is not documentation for a human reader -- it is the only thing Claude sees before deciding to load the skill, so it must encode both what the skill does and when to use it."
limits:
  - "Does not cover this KB's own apex-kb skill's specific SKILL.md (see wiki/summaries/informatics-design-formats-practice-guide.md for that layer); this page is the general official contract."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "anthropic-complete-guide-to-building-skills"
    rationale: "Official Anthropic first-party guide (P0 tier, skill-best-practices-official-2026-06-23 acquisition); the authoritative statement of the frontmatter and progressive-disclosure contract, not a third-party interpretation."
    coverage: "Full technical requirements chapter: file structure, YAML frontmatter field-by-field rules, progressive disclosure model, and troubleshooting/size-limit guidance."
  - rank: 2
    source_id: "anthropics-skill-creator-skill-md"
    rationale: "The official skill-creator skill is Anthropic's own reference implementation of the guide's rules -- a real, working SKILL.md that demonstrates the minimal frontmatter contract in practice rather than describing it abstractly."
    coverage: "A concrete, in-production example of a compliant name/description frontmatter pair and a body written for progressive disclosure (body content only loads once the skill is judged relevant)."
```

## Macro / Meso / Micro

### Macro

Everything about skill package design reduces to one constraint: minimize what Claude must read before it knows whether a skill is relevant, while keeping everything it might need once it decides to use it. The frontmatter is a decision gate, the body is the working instructions, and any linked files are an on-demand reference library. Violating this shape -- cramming detail into frontmatter, or inlining reference material into the body instead of a linked file -- doesn't break functionality, it just taxes every future conversation's context budget whether or not that skill's full depth was needed.

### Meso

The guide states the three-level system directly: "First level (YAML frontmatter): Always loaded in Claude's system prompt... Second level (SKILL.md body): Loaded when Claude thinks the skill is relevant... Third level (Linked files): Additional files... Claude can choose to navigate and discover only as needed. This progressive disclosure minimizes token usage while maintaining specialized expertise" (lines 91-101). The frontmatter is then subject to hard validation rules, not stylistic suggestions: `name` must exactly match `SKILL.md` casing conventions and be kebab-case matching the folder name; `description` is required, must state both *what the skill does* and *when to use it* (trigger conditions), must stay under 1024 characters, and must not contain XML tags (lines 345-381). The guide explicitly forbids a `README.md` inside the skill folder -- "All documentation goes in SKILL.md or references/" (lines 381-395) -- which is a progressive-disclosure consequence, not an arbitrary convention: a second undiscoverable doc file defeats the model that Claude only reads what's linked from SKILL.md.

### Micro

Concrete size guidance for when a skill needs splitting: under "Large context issues" the guide lists the symptom ("Skill seems slow or responses degraded"), causes ("Skill content too large," "Too many skills enabled simultaneously," "All content loaded instead of progressive disclosure"), and the fix -- "Optimize SKILL.md size: Move detailed docs to references/, Link to references instead of inline, Keep SKILL.md under 5,000 words" (lines 1322-1339). Separately, it recommends evaluating "if you have more than 20-50 skills enabled simultaneously" and considering "skill 'packs' for related capabilities" (lines 1339-1343) -- i.e., granularity has an upper bound on both axes: an individual skill's body should stay small, and the total enabled-skill count should stay bounded, with packaging (not padding one skill) as the release valve for growth. The official `skill-creator` SKILL.md itself demonstrates the minimal compliant form: a two-field frontmatter (`name: skill-creator`, `description:` naming both the action and explicit trigger phrases -- "create a skill from scratch, edit, or optimize an existing skill, run evals...") followed by a body written as a numbered process outline rather than an exhaustive reference (skill-creator SKILL.md lines 1-20).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Skills use a three-level progressive disclosure system: frontmatter is always loaded into the system prompt, the SKILL.md body loads only when Claude judges the skill relevant, and linked files load only as Claude chooses to navigate them."
    source_pointer: "anthropic-complete-guide-to-building-skills-for-claude.md lines 91-101"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C002
    claim: "The description frontmatter field is required, must state both what the skill does and when to use it, must stay under 1024 characters, and must not contain XML tags."
    source_pointer: "anthropic-complete-guide-to-building-skills-for-claude.md lines 369-380"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "A skill folder must not contain a README.md; all documentation belongs in SKILL.md or references/, since an undiscoverable second doc file defeats progressive disclosure."
    source_pointer: "anthropic-complete-guide-to-building-skills-for-claude.md lines 381-395"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C004
    claim: "When a skill causes large-context slowdowns, the prescribed fix is to keep SKILL.md under 5,000 words and move detailed docs into references/ rather than inlining them, and to keep the total number of simultaneously enabled skills under roughly 20-50, packaging related capabilities together rather than growing one skill indefinitely."
    source_pointer: "anthropic-complete-guide-to-building-skills-for-claude.md lines 1322-1343"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "What must a SKILL.md frontmatter contain, and what will fail validation?"
    leads_to: "wiki/summaries/skill-package-design-contract.md"
    rationale: "Direct official field-requirement rules for name and description."
  - question: "My skill feels slow / bloats context -- how big should a SKILL.md be, and when do I split it?"
    leads_to: "wiki/summaries/skill-package-design-contract.md"
    rationale: "Covers the official size thresholds and the references/ vs inline-content split."
  - related_page: "wiki/concepts/progressive-disclosure-for-agent-kbs.md"
    relation: "Companion concept applying the same progressive-disclosure principle to this KB's own retrieval/wiki design, not to a Claude Agent Skill package."
  - related_page: "wiki/entities/agent-skills-standard.md"
    relation: "Narrow entity page for the Agent Skills standard itself."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The guide's 5,000-word SKILL.md ceiling and 20-50 simultaneously-enabled-skill range are stated as troubleshooting guidance for a symptom ('seems slow'), not as hard platform-enforced limits; treat them as strong practitioner guidance rather than an enforced technical maximum unless corroborated elsewhere in the corpus."
    source_pointer: "anthropic-complete-guide-to-building-skills-for-claude.md lines 1322-1343"
    proposed_handling: "revisit_source"
  - id: U002
    description: "This page did not cross-check the guide's granularity guidance against this KB's own apex-kb SKILL.md or the other project skills in .claude/skills/ for compliance; that comparison belongs to the apex-application-orchestration-patterns page or a dedicated audit pass."
    proposed_handling: "planning_task_candidate"
```
