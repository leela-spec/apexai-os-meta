# Phase 1 Batch 01 — Skill Package and Skill Contracts

```yaml
title: "Skill Package and Skill Contracts"
source_batch_id: "phase1-batch01-skill-package-contracts"
kb_slug: "claude-code-orchestration-design"
phase: "ingest_phase_1"
status: "operator_review_needed"
created_at: "2026-07-02T00:00:00Z"
claim_labels_allowed:
  - fact
  - interpretation
  - recommendation
  - open_question
  - contradiction
confidence_labels_allowed:
  - high
  - medium
  - low
operator_gate:
  phase_2_allowed: false
  required_confirmation_phrase: "approve ingest"
```

## 1. Source Scope

This batch analyzes skill package design, `SKILL.md` semantics, official Agent Skills guidance, client implementation requirements, the official `skill-creator` pattern, and Apex-specific skill-definition conventions.

This is Phase 1 semantic ingest only. Phase 2 wiki synthesis is blocked pending operator approval with the exact phrase `approve ingest`.

## 2. Source Files Read

```yaml
source_files_read:
  - source_id: "anthropic-complete-guide-to-building-skills-for-claude"
    path: "raw/source-groups/claude-skill-design/sources/curated/official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md"
    source_type: "official_pdf_markdown"
    authority: "primary"
    pointers:
      - "lines 23-28: skill purpose and repeatable workflows"
      - "lines 71-80: required and optional folder components"
      - "lines 93-103: progressive disclosure tiers"
      - "lines 174-248: use-case planning and workflow categories"
  - source_id: "agentskills-specification"
    path: "raw/source-groups/claude-skill-design/sources/curated/official-repos/agentskills-agentskills/docs/specification.mdx"
    source_type: "official_spec"
    authority: "primary"
    pointers:
      - "lines 8-19: directory structure"
      - "lines 21-34: SKILL.md frontmatter fields"
      - "lines 60-99: name and description constraints"
      - "lines 178-188: body content and splitting long instructions"
      - "lines 189-224: optional directories and progressive disclosure"
      - "lines 226-247: file references and validation"
  - source_id: "agentskills-client-implementation"
    path: "raw/source-groups/claude-skill-design/sources/curated/official-repos/agentskills-agentskills/docs/client-implementation/adding-skills-support.mdx"
    source_type: "official_docs"
    authority: "primary"
    pointers:
      - "lines 9-18: lifecycle and implementation variables"
      - "lines 20-33: three-tier loading strategy"
      - "lines 34-60: skill discovery scopes"
      - "lines 83-94: name collisions and trust checks"
      - "lines 105-160: frontmatter parsing, lenient validation, stored record shape"
      - "lines 161-220: catalog disclosure and behavioral instructions"
      - "activation continuation lines 3-23: model-driven activation and dedicated tool activation"
      - "activation continuation lines 31-79: activated content, structured wrapping, bundled resources, allowlisting"
      - "activation continuation lines 81-102: compaction protection and subagent delegation"
  - source_id: "anthropic-skill-creator-skill"
    path: "raw/source-groups/claude-skill-design/sources/curated/official-repos/anthropics-skills/skills/skill-creator/SKILL.md"
    source_type: "official_skill"
    authority: "primary"
    pointers:
      - "lines 3-6: skill frontmatter and trigger description"
      - "lines 12-24: creation/eval/iteration loop"
      - "lines 47-71: intent capture and SKILL.md components"
      - "lines 73-115: anatomy, progressive disclosure, lack-of-surprise principle"
      - "lines 143-164: test prompt and eval format"
      - "lines 165-242: benchmark workflow"
  - source_id: "apex-alfred-skill-definition-guide"
    path: "raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Apex_Alfred_Skill_Definition_Guide.md"
    source_type: "operator_supplied_note"
    authority: "primary"
    pointers:
      - "lines 5-18: Apex loop-to-skill mapping"
      - "lines 21-43: SKILL.md zones"
      - "lines 44-75: frontmatter and allowed-tools discipline"
      - "lines 76-93: objective and procedure block rules"
      - "lines 94-120: artifact contracts and operator gates"
```

## 3. Source-Grounded Claims

```yaml
claims:
  - id: "B01-C001"
    label: fact
    confidence: high
    claim: >
      A skill is defined as a folder-based instruction package whose required entrypoint is `SKILL.md`; optional resources include scripts, references, and assets.
    source_pointers:
      - "anthropic-complete-guide-to-building-skills-for-claude.md lines 71-80"
      - "agentskills-specification.mdx lines 8-19"

  - id: "B01-C002"
    label: fact
    confidence: high
    claim: >
      Agent Skills rely on progressive disclosure: startup metadata/catalog, activated `SKILL.md` instructions, and on-demand bundled resources.
    source_pointers:
      - "anthropic-complete-guide-to-building-skills-for-claude.md lines 93-103"
      - "agentskills-specification.mdx lines 216-224"
      - "adding-skills-support.mdx lines 20-33"

  - id: "B01-C003"
    label: fact
    confidence: high
    claim: >
      The Agent Skills specification requires YAML frontmatter with `name` and `description`; `name` has strict lowercase/hyphen constraints and must match the parent directory, while `description` should include what the skill does and when to use it.
    source_pointers:
      - "agentskills-specification.mdx lines 21-34"
      - "agentskills-specification.mdx lines 60-99"

  - id: "B01-C004"
    label: fact
    confidence: high
    claim: >
      Agent clients should discover skill directories, parse frontmatter, disclose a compact catalog, and activate full instructions only when selected by the model or user.
    source_pointers:
      - "adding-skills-support.mdx lines 34-60"
      - "adding-skills-support.mdx lines 105-160"
      - "adding-skills-support.mdx lines 161-220"
      - "adding-skills-support.mdx activation continuation lines 3-23"

  - id: "B01-C005"
    label: fact
    confidence: high
    claim: >
      Client implementations should handle collisions deterministically and treat project-level skills as potentially untrusted until a trust check or equivalent approval occurs.
    source_pointers:
      - "adding-skills-support.mdx lines 83-94"

  - id: "B01-C006"
    label: fact
    confidence: high
    claim: >
      Activated skills can be delivered either as full `SKILL.md` files or body-only instructions; a dedicated activation tool can wrap content, enumerate resources without eagerly reading them, and enforce permissions.
    source_pointers:
      - "adding-skills-support.mdx activation continuation lines 31-79"

  - id: "B01-C007"
    label: fact
    confidence: high
    claim: >
      Skill content needs lifecycle handling after activation: context compaction can silently degrade behavior unless skill content is protected or deduplicated.
    source_pointers:
      - "adding-skills-support.mdx activation continuation lines 81-102"

  - id: "B01-C008"
    label: fact
    confidence: high
    claim: >
      The official `skill-creator` uses an iterative loop: capture intent, write a draft, create test prompts, compare with-skill and baseline runs, grade/aggregate benchmarks, and rewrite based on qualitative and quantitative evidence.
    source_pointers:
      - "anthropics-skills/skills/skill-creator/SKILL.md lines 12-24"
      - "anthropics-skills/skills/skill-creator/SKILL.md lines 143-164"
      - "anthropics-skills/skills/skill-creator/SKILL.md lines 165-242"

  - id: "B01-C009"
    label: fact
    confidence: medium
    claim: >
      Apex's operator-supplied skill guide maps the orchestration loop into discrete skills connected by artifact contracts, not direct calls.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 5-18"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 94-107"

  - id: "B01-C010"
    label: interpretation
    confidence: high
    claim: >
      The strongest reusable design rule for Apex skill packages is: keep `SKILL.md` as triggerable, concise routing and procedure logic; move heavy contracts, schemas, examples, and templates into referenced files.
    source_pointers:
      - "agentskills-specification.mdx lines 178-224"
      - "skill-creator/SKILL.md lines 88-111"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 85-93"

  - id: "B01-C011"
    label: recommendation
    confidence: high
    claim: >
      Apex should validate critical skills with both deterministic checks and inference-based review: deterministic checks for file shape/name/frontmatter/path sanity, and LLM review for workflow clarity, scope boundaries, trigger quality, and contradiction exposure.
    source_pointers:
      - "skill-creator/SKILL.md lines 143-164"
      - "skill-creator/SKILL.md lines 223-242"
      - "agentskills-specification.mdx lines 239-247"

  - id: "B01-C012"
    label: contradiction
    confidence: medium
    claim: >
      There is a specification tension between strict Agent Skills `name` requirements and Claude Code's documented behavior where the command name is derived from location and only `description` is recommended in some Claude Code skill frontmatter.
    source_pointers:
      - "agentskills-specification.mdx lines 27-34 and 60-68"
      - "primary-code-claude-com-docs-en-skills.md.md lines 212-220 and command-name continuation, read in Batch 2 source set"

  - id: "B01-C013"
    label: open_question
    confidence: medium
    claim: >
      The KB should decide whether Apex canonical skills target strict cross-client Agent Skills validation, Claude Code-native permissive frontmatter, or a two-tier policy that separates portable package rules from Claude Code runtime compatibility.
    source_pointers:
      - "agentskills-specification.mdx lines 21-34"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 44-75"
```

## 4. Concepts Extracted

```yaml
concepts_extracted:
  - concept_slug: skill-package-contract
    label: "Skill package contract"
    definition: "A folder-level contract with `SKILL.md` entrypoint plus optional scripts, references, and assets."
    confidence: high
    source_pointers:
      - "anthropic-complete-guide-to-building-skills-for-claude.md lines 71-80"
      - "agentskills-specification.mdx lines 8-19"

  - concept_slug: progressive-disclosure
    label: "Progressive disclosure"
    definition: "The three-tier loading model: catalog metadata, activated instructions, then on-demand resources."
    confidence: high
    source_pointers:
      - "adding-skills-support.mdx lines 20-33"
      - "agentskills-specification.mdx lines 216-224"

  - concept_slug: skill-trigger-description
    label: "Skill trigger description"
    definition: "The description field as the primary model-facing activation cue, requiring what/when wording and concrete triggers."
    confidence: high
    source_pointers:
      - "agentskills-specification.mdx lines 93-110"
      - "skill-creator/SKILL.md lines 64-71"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 59-67"

  - concept_slug: artifact-contract-handoff
    label: "Artifact-contract handoff"
    definition: "A workflow connection pattern where one skill writes an artifact and the next skill reads it, avoiding direct skill-to-skill coupling."
    confidence: medium
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 94-107"

  - concept_slug: skill-validation-loop
    label: "Skill validation loop"
    definition: "Iterative skill improvement using test prompts, with-skill/baseline comparison, grading, benchmark aggregation, and rewrite."
    confidence: high
    source_pointers:
      - "skill-creator/SKILL.md lines 12-24"
      - "skill-creator/SKILL.md lines 165-242"

  - concept_slug: skill-trust-boundary
    label: "Skill trust boundary"
    definition: "The need to gate project-level or repo-provided skills before loading instructions, resources, or allowlisted tools."
    confidence: high
    source_pointers:
      - "adding-skills-support.mdx lines 91-100"
```

## 5. Entities Extracted

```yaml
entities_extracted:
  - entity_slug: agent-skills-specification
    entity_label: "Agent Skills specification"
    entity_type: "standard"
    role: "Defines portable skill directory, `SKILL.md`, frontmatter, and resource conventions."
    confidence: high

  - entity_slug: anthropic-skill-creator
    entity_label: "Anthropic skill-creator skill"
    entity_type: "official_skill"
    role: "Reference implementation pattern for creating, testing, and improving skills."
    confidence: high

  - entity_slug: claude-code
    entity_label: "Claude Code"
    entity_type: "runtime_surface"
    role: "Runtime that discovers and invokes skills, commands, agents, hooks, and MCP integrations."
    confidence: high

  - entity_slug: apex-alfred-skill-definition-guide
    entity_label: "Apex Alfred Skill Definition Guide"
    entity_type: "operator_supplied_contract"
    role: "Apex-specific skill style and orchestration-loop mapping source."
    confidence: medium
```

## 6. Contradictions or Tensions

```yaml
contradictions_or_tensions:
  - id: "B01-T001"
    label: contradiction
    confidence: medium
    summary: >
      Strict Agent Skills spec says `name` is required and must match the parent directory, while Claude Code's skill docs treat `description` as the key recommended field and derive invocation from path. This affects whether Apex enforces strict portable validation or Claude Code-native permissiveness.
    source_pointers:
      - "agentskills-specification.mdx lines 27-34 and 60-68"
      - "primary-code-claude-com-docs-en-skills.md.md lines 212-220 and command-name continuation"

  - id: "B01-T002"
    label: contradiction
    confidence: medium
    summary: >
      The Apex guide recommends concise, artifact-specific frontmatter plus `allowed-tools`, while Agent Skills treats `allowed-tools` as optional/experimental and Claude Code makes it a runtime permission affordance. Apex should avoid treating `allowed-tools` as a universal cross-client contract.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 44-75"
      - "agentskills-specification.mdx lines 165-176"
```

## 7. Open Questions

```yaml
open_questions:
  - id: "B01-Q001"
    label: open_question
    confidence: high
    question: "Should Apex canonical skill packages enforce the Agent Skills spec strictly, or allow Claude Code-specific optional frontmatter and path-derived command names?"
    source_pointers:
      - "agentskills-specification.mdx lines 21-34"
      - "primary-code-claude-com-docs-en-skills.md.md lines 212-220"

  - id: "B01-Q002"
    label: open_question
    confidence: medium
    question: "Which Apex skill types require deterministic test harnesses versus qualitative operator review only?"
    source_pointers:
      - "skill-creator/SKILL.md lines 143-164"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 108-120"

  - id: "B01-Q003"
    label: open_question
    confidence: medium
    question: "Should Apex treat artifact-contract handoffs as mandatory for all orchestration skills, including lightweight prompt/reference skills?"
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 94-107"
```

## 8. Proposed Phase 2 Wiki Targets

```yaml
proposed_phase_2_wiki_targets:
  summaries:
    - "wiki/summaries/skill-package-contracts.md"
  concepts:
    - "wiki/concepts/progressive-disclosure.md"
    - "wiki/concepts/skill-trigger-description.md"
    - "wiki/concepts/artifact-contract-handoff.md"
    - "wiki/concepts/skill-validation-loop.md"
    - "wiki/concepts/skill-trust-boundary.md"
  entities:
    - "wiki/entities/agent-skills-specification.md"
    - "wiki/entities/anthropic-skill-creator.md"
    - "wiki/entities/claude-code.md"
    - "wiki/entities/apex-alfred-skill-definition-guide.md"
  contradiction_pages:
    - "wiki/concepts/strict-agent-skills-vs-claude-code-runtime-skill-contract.md"
```

## 9. Phase 2 Gate Statement

Phase 2 is blocked. Do not write `wiki/concepts/`, `wiki/entities/`, `wiki/summaries/`, semantic index sections, or final compiled KB pages until the operator gives the exact approval phrase in a later turn:

```text
approve ingest
```
