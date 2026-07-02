# Phase 1 Batch 03 — External Orchestration Repo Patterns

```yaml
title: "External Orchestration Repo Patterns"
source_batch_id: "phase1-batch03-external-orchestration-patterns"
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

This batch analyzes reusable patterns from external orchestration repositories only where they clarify repo-map design, workflow structure, commands/agents/skills layout, validation practices, migration discipline, and agent-computer-interface design.

The sources are not treated as authoritative over official Claude Code/Agent Skills documentation. They are comparative implementation-pattern material.

This is Phase 1 semantic ingest only. Phase 2 wiki synthesis is blocked pending operator approval with the exact phrase `approve ingest`.

## 2. Source Files Read

```yaml
source_files_read:
  - source_id: "shanraisshan-claude-code-best-practice-readme"
    path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-clone/shanraisshan__claude-code-best-practice/README.md"
    source_type: "external_repo_readme"
    authority: "secondary"
    pointers:
      - "lines 28-45: concept table mapping subagents, commands, skills, workflows, hooks, MCP, plugins, settings, memory"
      - "lines 47-76: hot feature table including dynamic workflows, agent teams, scheduled tasks, routines"
  - source_id: "shanraisshan-workflow-claude-skills"
    path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-clone/shanraisshan__claude-code-best-practice/.claude/commands/workflows/best-practice/workflow-claude-skills.md"
    source_type: "external_repo_workflow"
    authority: "secondary"
    pointers:
      - "lines 3-18: command frontmatter and read-then-report workflow scope"
      - "lines 22-37: research agent prompt and exact drift dimensions"
      - "lines 40-67: previous changelog comparison and report generation"
      - "lines 71-110: mandatory changelog append and badge update"
      - "lines 114-139: action offering and critical rules"
  - source_id: "bmad-native-skills-migration-checklist"
    path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-clone/bmad-code-org__BMAD-METHOD/tools/docs/native-skills-migration-checklist.md"
    source_type: "external_repo_migration_doc"
    authority: "secondary"
    pointers:
      - "lines 3-14: migration scope and status"
      - "lines 16-28: Claude Code migration from commands to skills plus ancestor conflict protection"
      - "lines 29-40: Codex CLI migration to `.agents/skills` and conflict protection"
      - "lines 42-80: platform-by-platform migration, testing, and legacy cleanup pattern"
      - "lines 194-208: GitHub Copilot migration and marker cleanup"
  - source_id: "bmad-skill-validator"
    path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-clone/bmad-code-org__BMAD-METHOD/tools/skill-validator.md"
    source_type: "external_repo_validator"
    authority: "secondary"
    pointers:
      - "lines 3-18: deterministic first pass before inference validation"
      - "lines 19-28: validation workflow"
      - "lines 31-40: definitions"
      - "lines 43-100: critical SKILL.md checks"
      - "lines 119-177: path-reference rules and encapsulation"
      - "lines 181-204: step-file rules"
  - source_id: "aider-repo-map-ctags"
    path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-read-only/Aider-AI__aider/aider/website/docs/ctags.md"
    source_type: "external_repo_docs"
    authority: "secondary"
    pointers:
      - "lines 18-23: note that ctags was superseded by tree-sitter repo map"
      - "lines 26-52: codebase-context problem"
      - "lines 86-107: whole-codebase context and hand-picked-file limitations"
      - "lines 108-162: repo map mechanism and benefits"
      - "lines 164-205: ctags-derived map output and compact hierarchical format"
      - "lines 221-245: future work on map subsets/search/LSP"
  - source_id: "swe-agent-aci"
    path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-read-only/princeton-nlp__SWE-agent/docs/background/aci.md"
    source_type: "external_repo_docs"
    authority: "secondary"
    pointers:
      - "lines 3-10: ACI definition and importance"
      - "lines 11-17: linter, file viewer, search command, empty output handling"
  - source_id: "source-priority-candidates"
    path: "manifests/phase0/source-priority-candidates.md"
    source_type: "phase0_navigation"
    authority: "primary_navigation"
    pointers:
      - "lines 9-58: external repos and docs selected as high-priority candidates"
  - source_id: "source-root-map"
    path: "manifests/migration/source-root-map.json"
    source_type: "migration_manifest"
    authority: "primary_navigation"
    pointers:
      - "lines 42-54 and 119-135: Claude orchestration agents copied as external repo pattern source group"
```

## 3. Source-Grounded Claims

```yaml
claims:
  - id: "B03-C001"
    label: fact
    confidence: medium
    claim: >
      The `claude-code-best-practice` repository organizes Claude Code concepts as a mapped surface: subagents, commands, skills, workflows, hooks, MCP, plugins, settings, memory, dynamic workflows, agent teams, scheduled tasks, and routines.
    source_pointers:
      - "shanraisshan__claude-code-best-practice/README.md lines 28-76"

  - id: "B03-C002"
    label: interpretation
    confidence: medium
    claim: >
      The `claude-code-best-practice` README is useful as an external repo-map pattern: it turns a large feature surface into a quick navigational table with feature, path/location, and implementation/reference links.
    source_pointers:
      - "shanraisshan__claude-code-best-practice/README.md lines 28-45"

  - id: "B03-C003"
    label: fact
    confidence: medium
    claim: >
      The `workflow-claude-skills` command demonstrates a read-then-report drift workflow: launch a research agent, compare official docs and changelog against a local report, read previous changelog entries, append a new changelog entry, update a badge, and only take action after user approval.
    source_pointers:
      - "workflow-claude-skills.md lines 8-18"
      - "workflow-claude-skills.md lines 22-37"
      - "workflow-claude-skills.md lines 40-67"
      - "workflow-claude-skills.md lines 71-139"

  - id: "B03-C004"
    label: interpretation
    confidence: medium
    claim: >
      The drift workflow is a useful Apex pattern for maintaining volatile Claude Code documentation: separate drift detection, changelog update, badge/status update, and execution approval rather than silently patching all findings.
    source_pointers:
      - "workflow-claude-skills.md lines 12-18"
      - "workflow-claude-skills.md lines 71-110"
      - "workflow-claude-skills.md lines 114-139"

  - id: "B03-C005"
    label: fact
    confidence: medium
    claim: >
      BMAD's migration checklist treats native skill adoption as a platform-by-platform migration problem with tests for fresh install, reinstall/upgrade, legacy cleanup, path compatibility, and ancestor conflict behavior.
    source_pointers:
      - "native-skills-migration-checklist.md lines 3-28"
      - "native-skills-migration-checklist.md lines 42-80"
      - "native-skills-migration-checklist.md lines 194-208"

  - id: "B03-C006"
    label: fact
    confidence: medium
    claim: >
      BMAD's validation pattern uses deterministic checks first and inference validation second, skipping rules that passed deterministically and reserving LLM judgment for semantic or ambiguous rules.
    source_pointers:
      - "skill-validator.md lines 3-18"
      - "skill-validator.md lines 19-28"

  - id: "B03-C007"
    label: fact
    confidence: medium
    claim: >
      BMAD's validator emphasizes package encapsulation: internal references should be relative from the originating file, `installed_path` is an anti-pattern, external references should use project-root/config variables, and skills should not reach into other skill directories by file path.
    source_pointers:
      - "skill-validator.md lines 119-177"

  - id: "B03-C008"
    label: fact
    confidence: medium
    claim: >
      Aider's repo-map documentation frames the core large-codebase problem as context compression: whole-codebase inclusion does not fit the context window, and hand-picked files waste context and require manual selection.
    source_pointers:
      - "Aider-AI__aider/aider/website/docs/ctags.md lines 26-52"
      - "Aider-AI__aider/aider/website/docs/ctags.md lines 86-107"

  - id: "B03-C009"
    label: fact
    confidence: medium
    claim: >
      Aider's repo-map pattern sends a concise map of repository files, symbols, and call signatures so the model can infer APIs and ask for specific files when needed.
    source_pointers:
      - "Aider-AI__aider/aider/website/docs/ctags.md lines 108-162"
      - "Aider-AI__aider/aider/website/docs/ctags.md lines 164-205"

  - id: "B03-C010"
    label: fact
    confidence: medium
    claim: >
      Aider itself notes that the older ctags-based map was superseded by a tree-sitter repo map, making ctags a historical pattern rather than the current implementation target.
    source_pointers:
      - "Aider-AI__aider/aider/website/docs/ctags.md lines 18-23"

  - id: "B03-C011"
    label: fact
    confidence: medium
    claim: >
      SWE-agent defines an Agent-Computer Interface as the tools and interaction format that allow an agent to operate in a computer environment, and states that good ACI design materially improves agent results.
    source_pointers:
      - "princeton-nlp__SWE-agent/docs/background/aci.md lines 3-10"

  - id: "B03-C012"
    label: fact
    confidence: medium
    claim: >
      SWE-agent's ACI includes design details that resemble deterministic guardrails: linting before edits are accepted, a bounded file viewer, succinct full-directory search results, and explicit success text for empty command output.
    source_pointers:
      - "princeton-nlp__SWE-agent/docs/background/aci.md lines 11-17"

  - id: "B03-C013"
    label: recommendation
    confidence: medium
    claim: >
      Apex should copy the patterns, not the full external repo architectures: repo-map/context compression from Aider, deterministic-then-inference validation from BMAD, drift workflows from shanraisshan, and ACI/tool-output discipline from SWE-agent.
    source_pointers:
      - "Aider ctags.md lines 108-162"
      - "BMAD skill-validator.md lines 3-28"
      - "workflow-claude-skills.md lines 8-18 and 71-139"
      - "SWE-agent aci.md lines 11-17"

  - id: "B03-C014"
    label: contradiction
    confidence: medium
    claim: >
      External repos optimize for their own runtime assumptions and may conflict with Apex's source-preserving KB lifecycle; BMAD's platform migration and shanraisshan's command workflows are useful patterns but should not override Apex's operator gate, source custody, or Phase 1/Phase 2 separation.
    source_pointers:
      - "native-skills-migration-checklist.md lines 3-28"
      - "workflow-claude-skills.md lines 114-139"
      - "manifests/phase0/phase0-navigation-report.md lines 20-24"

  - id: "B03-C015"
    label: open_question
    confidence: medium
    claim: >
      It remains unresolved whether Apex should invest in a tree-sitter/LSP style repo-map layer for code-heavy orchestration repos, or keep V1 Phase 0 maps to Markdown headings, links, frontmatter, and keywords.
    source_pointers:
      - "Aider ctags.md lines 18-23 and 221-245"
      - "manifests/phase0/phase0-navigation-report.md lines 9-18"
```

## 4. Concepts Extracted

```yaml
concepts_extracted:
  - concept_slug: external-feature-surface-map
    label: "External feature-surface map"
    definition: "A README/table pattern that maps orchestration features to implementation locations, docs, and status links."
    confidence: medium
    source_pointers:
      - "shanraisshan__claude-code-best-practice/README.md lines 28-45"

  - concept_slug: drift-detection-workflow
    label: "Drift detection workflow"
    definition: "A read-then-report workflow that compares live external docs against a local report, reads prior changelog entries, records a new entry, and asks before acting."
    confidence: medium
    source_pointers:
      - "workflow-claude-skills.md lines 8-18 and 40-139"

  - concept_slug: deterministic-then-inference-validation
    label: "Deterministic-then-inference validation"
    definition: "A two-pass validation model where mechanical shape checks happen first and LLM review focuses only on remaining judgment-heavy rules."
    confidence: medium
    source_pointers:
      - "skill-validator.md lines 3-28"

  - concept_slug: skill-package-encapsulation
    label: "Skill package encapsulation"
    definition: "A rule set preventing skills from relying on absolute/internal cross-skill paths and requiring relative internal references."
    confidence: medium
    source_pointers:
      - "skill-validator.md lines 119-177"

  - concept_slug: repo-map-context-compression
    label: "Repo-map context compression"
    definition: "A compact representation of repository files, symbols, and signatures that helps an agent choose relevant files without loading the whole repo."
    confidence: medium
    source_pointers:
      - "Aider ctags.md lines 108-162"

  - concept_slug: agent-computer-interface
    label: "Agent Computer Interface"
    definition: "A deliberate tool and interaction format design that shapes how an agent acts in a computer environment."
    confidence: medium
    source_pointers:
      - "SWE-agent aci.md lines 3-10"
```

## 5. Entities Extracted

```yaml
entities_extracted:
  - entity_slug: shanraisshan-claude-code-best-practice
    entity_label: "shanraisshan/claude-code-best-practice"
    entity_type: "external_repo"
    role: "Comparative map of Claude Code feature surfaces and drift-maintenance workflows."
    confidence: medium

  - entity_slug: bmad-method
    entity_label: "bmad-code-org/BMAD-METHOD"
    entity_type: "external_repo"
    role: "Comparative source for native skill migration, validation, and package encapsulation patterns."
    confidence: medium

  - entity_slug: aider
    entity_label: "Aider"
    entity_type: "external_repo"
    role: "Comparative source for repo-map and context-compression patterns."
    confidence: medium

  - entity_slug: swe-agent
    entity_label: "SWE-agent"
    entity_type: "external_repo"
    role: "Comparative source for agent-computer-interface and tool-output discipline."
    confidence: medium
```

## 6. Contradictions or Tensions

```yaml
contradictions_or_tensions:
  - id: "B03-T001"
    label: contradiction
    confidence: medium
    summary: >
      Aider's ctags repo-map source is explicitly superseded by a newer tree-sitter approach, so its value is as a conceptual pattern for context compression, not as a direct implementation recommendation.
    source_pointers:
      - "Aider ctags.md lines 18-23"
      - "Aider ctags.md lines 221-245"

  - id: "B03-T002"
    label: contradiction
    confidence: medium
    summary: >
      BMAD's skill validator has BMAD-specific naming rules such as `bmad-` prefix, which should not be imported into Apex unless Apex explicitly chooses a project-specific prefix policy.
    source_pointers:
      - "skill-validator.md lines 69-83"

  - id: "B03-T003"
    label: contradiction
    confidence: medium
    summary: >
      shanraisshan workflows include mandatory local changelog and badge writes before presenting a report; Apex Phase 1 must avoid analogous semantic wiki writes before the `approve ingest` gate.
    source_pointers:
      - "workflow-claude-skills.md lines 71-110"
      - "manifests/phase0/phase0-navigation-report.md lines 20-24"
```

## 7. Open Questions

```yaml
open_questions:
  - id: "B03-Q001"
    label: open_question
    confidence: medium
    question: "Should Apex Phase 0 V1.5 add tree-sitter/LSP-style code symbol maps for raw external repos, or keep that layer deferred until code-heavy query failures appear?"
    source_pointers:
      - "Aider ctags.md lines 18-23 and 221-245"

  - id: "B03-Q002"
    label: open_question
    confidence: medium
    question: "Which BMAD validator rules generalize to Apex skill packages without importing BMAD-specific naming/prefix assumptions?"
    source_pointers:
      - "skill-validator.md lines 43-100 and 119-177"

  - id: "B03-Q003"
    label: open_question
    confidence: medium
    question: "Should Apex preserve a drift changelog per volatile source group, or rely on Phase 0 reruns plus Phase 1 re-ingest reports?"
    source_pointers:
      - "workflow-claude-skills.md lines 40-110"

  - id: "B03-Q004"
    label: open_question
    confidence: medium
    question: "What is the minimum ACI/tool-output contract Apex should require for local agents or Codex-style repo executors?"
    source_pointers:
      - "SWE-agent aci.md lines 11-17"
```

## 8. Proposed Phase 2 Wiki Targets

```yaml
proposed_phase_2_wiki_targets:
  summaries:
    - "wiki/summaries/external-orchestration-repo-patterns.md"
  concepts:
    - "wiki/concepts/external-feature-surface-map.md"
    - "wiki/concepts/drift-detection-workflow.md"
    - "wiki/concepts/deterministic-then-inference-validation.md"
    - "wiki/concepts/skill-package-encapsulation.md"
    - "wiki/concepts/repo-map-context-compression.md"
    - "wiki/concepts/agent-computer-interface.md"
  entities:
    - "wiki/entities/shanraisshan-claude-code-best-practice.md"
    - "wiki/entities/bmad-method.md"
    - "wiki/entities/aider.md"
    - "wiki/entities/swe-agent.md"
  contradiction_pages:
    - "wiki/concepts/external-repo-patterns-vs-apex-kb-lifecycle-boundary.md"
```

## 9. Phase 2 Gate Statement

Phase 2 is blocked. Do not write `wiki/concepts/`, `wiki/entities/`, `wiki/summaries/`, semantic index sections, or final compiled KB pages until the operator gives the exact approval phrase in a later turn:

```text
approve ingest
```
