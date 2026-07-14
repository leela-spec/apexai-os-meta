# Deep Research Prompt Packet

## Packet metadata

```yaml
packet_id: apex-kb-final-architecture-deep-research
primary_task_type: research
secondary_task_types:
  - repository_and_snapshot_evidence_analysis
  - long_context_digestion
  - workflow_and_micro_design_extraction
  - architecture_synthesis
  - implementation_planning
expected_output_type: decision_complete_final_architecture_and_detailed_implementation_guidance
provider_target: ChatGPT Deep Research
run_model: one_prompt_one_coherent_run
operator_pauses_during_run: false
code_or_repository_mutation: false
source_access_fallbacks:
  - github_app_or_connector
  - public_github_main
  - raw_github_main
  - uploaded_project_sources
  - architecture_research_without_apex_implementation
```

## Clean copy-paste prompt

```text
You are a senior knowledge-system architect conducting one coherent Deep Research run to define the final Apex KB architecture and detailed implementation guidance.

Do not write repository patches, finished scripts, complete replacement files, or falsely finalized contracts. Produce enough module-level and file/script-level detail that implementation agents can execute the design without rediscovering the architecture.

NON-NEGOTIABLE PRODUCT TARGET

Design one final multifunctional Apex KB architecture that:

1. deterministically inventories every configured source or explicitly excludes it with a reason;
2. creates durable concept-to-source intelligence showing where each concept is discussed and why each file was surfaced;
3. preserves current, historical, prototype, implementation, contextual, duplicate, superseded, incidental, blocked, and irrelevant-after-review source relationships;
4. uses scripts for observable repeatable work and LLM judgment only for meaning, authority, contradiction, synthesis, and other semantic decisions;
5. compiles durable Macro, Meso, and Micro knowledge that creates more value than rereading raw sources;
6. creates a durable concept dossier and durable source atlas or equivalent lossless source-map surface for every configured concept;
7. makes future AI queries faster, cheaper, more complete, and easier to verify;
8. supports incremental maintenance without rereading unchanged evidence unnecessarily;
9. supports configurable execution profiles inside the same architecture;
10. supports a future low-token Codex orchestration loop that delegates semantic work to ChatGPT web in the strongest suitable available reasoning mode;
11. removes redundant instructions, duplicate metadata, and guardrails that neither prevent a demonstrated failure nor eliminate repeat work;
12. remains honest when evidence or tooling is unavailable.

The source map and source atlas are durable product outputs, not disposable preprocessing.

KNOWN FAILURE MODE — INCOMPLETE VERSION DRIFT

Do not reinterpret `efficient`, `bounded`, `prioritized`, `iterative`, `configurable`, or `token-saving` as permission to design a lightweight, minimal, preliminary, V1, V1.5, later-completed, deferred, or partially functional product.

- Prioritization controls research order.
- Configuration controls execution scope.
- Neither reduces, postpones, or fragments the final architecture.

Allowed dispositions are `keep`, `change`, `add`, `merge`, `remove`, `configurable`, `reject`, and `requires_evidence_probe`.

Reject a capability only when it creates insufficient target value relative to its cost and complexity. Difficulty alone is not sufficient. Technical schema versions may exist only as compatibility identifiers and may not imply product maturity.

REPOSITORY IDENTITY

```yaml
repository_owner: leela-spec
repository_name: apexai-os-meta
repository_full_name: leela-spec/apexai-os-meta
branch: main
research_package_root: FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch
path_style: repository_relative
```

Use repository-relative paths after this block. They are logical provenance identities, not requirements for the physical layout of Google Drive or Project Sources: do not require a physical `apexai-os-meta` wrapper folder or a physical `source-knowledge` wrapper folder. Accepted representations include the `KnowledgeBase`, `apex-kb`, and `claude-code-orchestration-design` Drive roots, the three standalone `llm-wiki`, `llm-wiki-main`, and `llm-wiki-skill-main` Drive roots, and uploaded Project Sources containing Git snapshots or missing implementation files. Do not use local-checkout assumptions. Resolve and record the current `main` commit when repository access works; a commit named in an older file is only a snapshot. For every source read, record the displayed source route actually opened alongside the inferred repository-relative identity, and do not count two representations of the same file as independent evidence.

SOURCE-ACCESS PROBE AND EVIDENCE MODES

Before substantive research, attempt to open completely:

1. `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/00-START-HERE.md`
2. `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/02-LIFECYCLE-COMPONENT-VALUE-MAP.md`
3. `.claude/skills/apex-kb/SKILL.md`

Try routes in this order:

1. enabled GitHub app or connector;
2. public GitHub pages for `leela-spec/apexai-os-meta` on `main`;
3. raw GitHub files for the same repository and branch;
4. uploaded Project Sources containing the package and selected repository files.

Do not attempt local paths. Select one evidence mode:

- `full_repository_evidence` — current package and implementation are reliably accessible;
- `project_source_repository_snapshot` — GitHub routes fail but uploaded files provide a bounded repository snapshot;
- `architecture_research_without_apex_implementation` — no reliable current Apex implementation evidence is available.

Do not abort in the third mode. Continue with the available package, self-created research, LLM-Wiki sources, Claude skill/orchestration sources, official primary web documentation, and primary tool/library repositories. Mark current implementation facts and current-mismatch scores as `unverified`, list what must later be checked, and do not lower the target.

EVIDENCE CLASSES

Separate operator target, verified current implementation facts, Project Source snapshot facts, existing Apex research intent, LLM-Wiki blueprint evidence, Claude skill/orchestration evidence, external primary evidence, inference, and recommendation.

MANDATORY SOURCE FAMILIES

1. Read package files `00`–`06` in numeric order. Treat file `02` as a seed hypothesis that this run must update.
2. When available, inspect the current Apex skill, references, templates, runtime scripts, tests, fixtures, manifests, and runbooks. Inspect code behavior, not only prose.
3. For every lifecycle module, consult relevant LLM-Wiki mechanisms and concrete files/scripts/workflows. State what Apex should copy, adapt, combine, configure, reject, or probe.
4. For every micro recommendation about a skill file, reference, template, workflow, script, hook, agent, browser handoff, loading, or recovery, consult relevant Claude skill/orchestration design evidence from the indexes, including compiled informatics, resilient-workflow, agent/subagent, mechanism-choice, commands/hooks/rules/memory, and Apex orchestration pages.
5. Use current official primary web documentation when unstable external facts materially affect a decision.

Do not use `Failed_Prompts/`, `FailedKBCreation/`, standalone prompt drafts, chat histories, or superseded draft plans as design authority.

ONE COHERENT PRIORITY-DRIVEN RESEARCH SEQUENCE

Do not use one flat global question checklist and do not pause for operator approval.

Step 1 — Target Lock

Make the first substantive output the complete target: future-AI jobs, durable dossier, durable source map/atlas, deterministic versus semantic ownership, token/value requirements, configurable-mode principles, measurable success, non-success proxies, and known failure modes.

Step 2 — Verify and update the Lifecycle Component and Value Map

Use file `02` only as a seed. Verify every component; correct definitions; add missing components; merge duplicates; identify ownership, dependencies, producers, consumers, and interconnections; compare with current Apex when evidence permits; score on 1–100 dimensions; assign a justified disposition; and place each component in a research group. Do not inherit current scores, groupings, or recommendations.

Step 3 — Group the lifecycle

Create coherent groups based on dependencies, source overlap, and decision boundaries. Include target/scope/custody, deterministic corpus intelligence, durable source maps and atlases, semantic compilation, acceptance, retrieval, maintenance, configurable profiles, Codex/browser/runtime orchestration, and skill/package micro design where supported by evidence.

Step 4 — Rank groups

Research highest-value mismatches first using:

```text
current Apex mismatch × achievable product-value gain × downstream lifecycle leverage
```

When implementation evidence is unavailable, use target contribution, failure severity, and downstream leverage and mark mismatch `unverified`.

Step 5 — Research each group iteratively inside this same run

For each group: state target contribution; identify current mismatch or unverified facts; derive only the questions needed for that group; select a focused source bundle; compare Apex, LLM-Wiki, Claude skill/orchestration design, and current primary evidence; design modules and submodules; specify implementation guidance and interconnections; create file/script design records; update remaining priorities; then continue to the next group.

Grouping prevents context mixing. It does not create separate Deep Research runs or operator checkpoints.

DESIGN DISCIPLINE

- Scripts report observable facts; LLMs judge meaning, authority, contradiction, and synthesis; the orchestrator coordinates without duplicating semantic work.
- Keep exhaustive machine candidate sets separate from compact navigation projections; no top-N view may replace the authoritative set.
- Preserve durable per-concept source maps and atlases with every candidate reconciled, exact pointers, blocked visibility, individual value, and relationships.
- Do not use counts, headings, fields, pages, or self-reported reads as semantic proof.
- Do not add an artifact, field, gate, evaluator, tool, or instruction without naming its consumer, demonstrated failure prevented or repeat work removed, and recurring cost.
- Prefer derived fields and progressive disclosure over LLM-authored duplicate metadata and always-loaded contracts.
- Assess graph, extraction, parser, UI, vector, and publishing capabilities by target value. Use `configurable`, `reject`, or `requires_evidence_probe`; complexity alone does not justify omission.
- Do not expose hidden chain-of-thought. Provide cited evidence, decision rationales, alternatives, uncertainty, and tradeoffs.
- Leela is a negative acceptance case, not the design subject.

SCORING — 1 TO 100

Score each material component, module, tool, script, artifact, and LLM instruction separately on:

- target contribution;
- current mismatch;
- achievable knowledge-value gain;
- token-saving potential;
- deterministic leverage;
- downstream leverage;
- failure severity if absent or wrong;
- resilience contribution;
- implementation cost;
- recurring token/compute/maintenance cost;
- evidence confidence.

Use `unverified` instead of inventing a current-mismatch score. A transparent sequencing score is allowed only if the formula and dimensional tradeoffs remain visible.

CONFIGURABLE EXECUTION-PROFILE STRATEGY

Design independent axes for source formats, corpus-priority coverage, topic coverage, semantic depth, full versus targeted reading, atlas depth, duplicate/version handling, graph extraction, external verification, acceptance depth, build/rebuild/update/repair mode, and terminal/connector/browser execution surface. Propose named profiles and defaults for operator consultation after the run. Do not create maturity-version tracks.

FUTURE CODEX / CHATGPT WEB / RUNTIME ORCHESTRATION

Design this as part of the final architecture, not as the method of this research run:

- Codex/orchestrator: necessary scope/profile Q&A, deterministic commands, bounded task packets, changed-path verification, Git operations, coordination; no deep corpus synthesis.
- ChatGPT web in the strongest suitable available reasoning mode: whole-file reading, semantic judgment, Phase 1/2 knowledge writing, semantic evaluation; no local lifecycle commands or Git pushes.
- Deterministic runtime: inventory, hashes, extraction status, Phase 0 maps, structural validation, retrieval rebuild, observable postflight; no semantic truth judgments.

Do not hard-code a model marketing label. Record the actual model/mode used at execution. Define a save batch as one coherent context-aware completed KB unit, such as one concept plus its source atlas or one tightly related source group. Add only validation or recovery mechanisms whose value is demonstrated.

MODULE OUTPUT CONTRACT

For every group provide purpose/value, current mismatch, focused questions and sources, final strategy, module/submodule boundaries, owners, inputs, operations, outputs, consumers, failure behavior, implementation order, migration, interfaces, tests, creation guidance, interconnections, configuration effects, and all affected file/script records.

For every file, script, template, workflow, reference, hook, manifest, or generated artifact provide repository-relative path, purpose, owner/status, current mismatch, final responsibilities/non-responsibilities, inputs/outputs/consumers, required sections or interfaces, control flow, deterministic/semantic boundary, relationships, progressive-disclosure behavior, Claude micro-design evidence, migration, tests, failure behavior, token/maintenance cost, risks, disposition, and rationale. Do not write the complete file or code.

REQUIRED FINAL REPORT — FIRST HALF

Return the report in this order.

# 1. Target Lock

Define the complete measurable product target, future-AI jobs, durable concept dossier, durable source map/atlas, ownership boundaries, configurable-mode principles, value/token requirements, success conditions, non-success proxies, and failure-mode prohibitions.

# 2. Evidence Mode and Source Truth

Record route attempts, selected evidence mode, current `main` commit when available, available/unavailable sources, snapshot limitations, evidence classes, unverified implementation facts, and substitutions. For every source used, record the displayed source route actually opened, the inferred repository-relative identity when reliable, and its completeness/duplicate status; do not count duplicate representations of the same file as independent corroboration.

# 3. Verified and Updated Lifecycle Component and Value Map

Return the corrected complete map immediately after the Target Lock and evidence truth: added/merged/removed/configurable/rejected/probe-required components, 1–100 scores, ownership, dependencies, research groups, and current mismatch or `unverified` status.

# 4. Research Grouping and Priority Order

Show groups, why each is coherent, its focused source bundle, priority dimensions/formula, and sequence.

# 5 onward. Priority-Ordered Module Research

Provide one complete module report per group using the Module Output Contract. Include deterministic corpus intelligence, durable source maps/atlases, semantic compilation, acceptance, retrieval/query, maintenance, configurable profiles, Codex/browser/runtime orchestration, and package/file/script micro design where supported by evidence.

Do not demand falsely finalized field-level contracts. Specify required behavior, interfaces, consumers, validation, migration, and creation guidance at implementation-ready design depth.

REQUIRED FINAL REPORT — SECOND HALF

# Configurable Apex KB Execution Profiles

Define independent configuration axes, named profiles, defaults, activation criteria, dependencies, consequences, costs, and genuine decisions for later operator consultation. Distinguish `rejected`, `configurable`, and `requires_evidence_probe`.

# Codex / ChatGPT Web / Deterministic Runtime Orchestration

Define responsibilities, task-packet structure, save batches, whole-file read/write expectations, allowed write scope, handoffs, Git ownership, failure behavior, demonstrated validation needs, token implications, and the actual-model/mode record.

# Durable Source-Map and Index Design

Specify exhaustive machine candidate maps, compact navigation projections, durable source atlases, individual file snapshots/value, freshness/authority/lifecycle/contradiction/duplicate/supersession relationships, exact pointers, blocked visibility, audit/failure-diagnosis use, retrieval behavior, invalidation, and future-AI navigation.

# Final File and Script Implementation Plan

Provide the proposed final tree and a File and Script Design Record for every affected existing or proposed artifact. Include dependency order, migration, compatibility, tests, fixtures, and micro-design evidence. Do not include code or complete replacement files.

# Cost, Token, and Complexity Audit

Show one-time and recurring costs, token drivers, deterministic savings, fields/files/gates to remove or merge, and the value required to justify high-cost capabilities.

# Implementation Acceptance Model

Define measurable product acceptance, deterministic checks, semantic checks whose value is demonstrated, durable source-map completeness, fixtures, real-corpus canaries, and truthful partial/blocked states.

# Research Confidence and Future Investigation

This is the last report section only. Include trusted findings, verified current implementation facts, limited-evidence findings, unvalidated hypotheses, remaining gaps, possible future research, named technical probes, what worked well, weak sources or approaches, and what implementation agents must verify. Do not interrupt the run with these questions earlier.

VALIDATION BEFORE RETURNING

Verify that:

- the first substantive section is the Target Lock;
- file `02` was verified, corrected, expanded, rescored, and regrouped by this run;
- every material component has a justified disposition;
- no valuable capability was omitted merely because it was difficult or expensive;
- no V1/V1.5/minimal/deferred product architecture remains;
- configuration is not confused with product incompleteness;
- every module used focused sources inside the same run;
- LLM-Wiki evidence was consulted for every module;
- Claude skill/orchestration evidence supports every micro file/workflow recommendation;
- current code is distinguished from research intent when accessible;
- fallback modes remain honest and useful;
- durable source maps and atlases are core outputs;
- all repository paths are relative after the identity block;
- the report contains no patches, finished scripts, complete replacement files, or unsupported claims;
- the design is detailed enough for implementation without architecture rediscovery;
- the final section records confidence, gaps, probes, and future research.

If repository evidence is inaccessible, continue in the selected fallback mode. Do not fabricate implementation facts, do not lower the target, and do not stop merely because optional historical material is unavailable. Do not patch, commit, push, or execute Apex KB.
```

## Failure and learning hints

| Likely failure | Correction built into the prompt |
|---|---|
| Reintroduces incomplete maturity versions | Binding incomplete-version-drift prohibition; configuration controls run scope. |
| Wastes the run when GitHub access fails | Project Source and architecture-only evidence modes continue useful research. |
| Loads every source into every decision | Priority-ordered modules use focused source bundles in one coherent run. |
| Returns another high-level outline | Module and file/script records require implementation-ready creation guidance. |
| Adds process theater | Every artifact, field, gate, or evaluator must prevent a demonstrated failure or remove repeat work. |
| Treats target queries as the whole product | Durable exhaustive source maps and source atlases are locked core outputs. |
| Uses deterministic scores as authority | Scores guide research and routing only; semantic authority remains LLM-owned and evidence-based. |
| Copies LLM-Wiki indiscriminately | Every module compares copy, adapt, combine, configurable, reject, and probe-required options. |
| Produces weak micro file designs | Claude skill/orchestration evidence is mandatory for every micro recommendation. |
| Confuses current code with research intent | Evidence modes and classes separate current facts, snapshots, research intent, inference, and recommendation. |
| Produces code instead of design | The prompt prohibits patches, complete files, finished scripts, and falsely finalized contracts. |

## Prompt quality review

```yaml
validation_status: ready_after_package_patch
run_integrity:
  one_prompt_one_run: true
  operator_pauses: false
  target_lock_first: true
  component_map_updated_by_research: true
source_integrity:
  canonical_repository_identity: true
  local_paths_prohibited: true
  fallback_modes_defined: true
  architecture_only_mode_continues: true
research_integrity:
  priority_driven_module_loop: true
  scores_1_to_100: true
  llm_wiki_per_module: true
  claude_micro_design_evidence: true
output_integrity:
  durable_source_map_core: true
  configurable_profiles_required: true
  codex_browser_runtime_design_required: true
  implementation_guidance_without_code: true
  confidence_and_future_research_last: true
```
