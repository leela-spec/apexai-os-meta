---
type: ExecutionPrompt
id: PROMPT-APEX-INFRASTRUCTURE-PROCESSING-v2
title: Apex CLI-agent infrastructure research and creation prompt v2
description: Pro Thinking assignment following the SmallSkills prompt-design standard to create a complete proposed infrastructure package from retained knowledge and current research.
status: proposed
tags: [informatics, processing-prompt, pro-thinking, infrastructure, research]
---

# Processing prompt v2

This is a separate version based on the [Pro Thinking design standard](apex-meta/SmallSkills/Prompting/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md), [master template](apex-meta/SmallSkills/Prompting/ProThinkingPrompt/02_REUSABLE_MASTER_TEMPLATE.md), [ingestion workflow](apex-meta/SmallSkills/Prompting/ProThinkingPrompt/03_INGESTION_RESEARCH_SYNTHESIS_WORKFLOW.md), and [validation guide](apex-meta/SmallSkills/Prompting/ProThinkingPrompt/04_ANTI_OVERENGINEERING_AND_VALIDATION.md). The original processing prompt remains unchanged.

Copy the text between Start prompt and End prompt into a research model with authenticated repository access, public web research, and downloadable artifact creation.

## Start prompt

# Apex CLI-Agent Infrastructure — Research and Creation

## Role

Research, synthesize, design, and create the complete **Apex CLI-Agent Infrastructure Design Package** in one continuous run. You are the instruction-systems research and infrastructure-design lead. The package will let the Apex operator review and approve the next repository, local-agent, instruction, skill, and hook architecture without reconstructing its evidence or commissioning another abstract design pass.

Use your own research method and internal working process. Make routine research and presentation choices autonomously. Continue through ordinary uncertainty using the best-supported interpretation and record consequential assumptions.

## Objective

Create a coherent, review-ready **Apex CLI-Agent Infrastructure Design Package** that defines how each applicable rule is owned, discovered, activated, delivered, executed, independently verified, and maintained across the relevant agent platforms.

The completed package must contain a populated rule/activation registry, a proposed repository and agent architecture, cross-CLI compatibility findings, reusable configuration and workflow examples, an existing-file-to-target-file integration map, evaluation artifacts, supporting findings and decisions, a validation report, and a manifest.

The primary result is the usable design package. Research findings support its creation; an inventory, literature review, general recommendation, or another handover is insufficient. The package is proposed for operator review and does not imply approval to install it.

## Source authority

Use this authority order:

1. Current operator instructions, live Apex contracts, and authoritative operating files define intended behavior and constraints.
2. Explicitly accepted decisions define approved choices within their recorded scope.
3. Actual configurations, implementations, and execution evidence establish what exists and what has been observed.
4. Retained research, experiments, candidates, proposed designs, and examples provide evidence, alternatives, and failure cases.
5. Current primary external research establishes platform capabilities and informs better mechanisms.

External evidence can justify proposing a change to an earlier choice. Show the original decision, its rationale, the new evidence, and the effect on the proposed product. Preserve accepted domain meaning unless the operator approves a change. Distinguish documented capability, installed behavior, measured outcomes, simulation, inference, proposal, and accepted state.

## Named sources

Repository: `leela-spec/apexai-os-meta`. Read the operator-specified revision, otherwise `main`, through authenticated access. Record the revision used. All repository paths below are relative to the repository root; they contain no workstation prefix or public repository URL.

Begin with:

```text
apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md
apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml
apex-meta/informatics/final/research/11-infrastructure-evidence-index/01-research-and-decision-map.md
apex-meta/informatics/final/research/11-infrastructure-evidence-index/06-ranked-reading-guide.md
apex-meta/informatics/final/research/11-infrastructure-evidence-index/top50-reading-plan.json
apex-meta/informatics/final/research/11-infrastructure-evidence-index/07-current-web-research.md
apex-meta/orchestration/CURRENT-SYSTEM-MANIFEST.yaml
```

The index bundle provides wider file catalogs, decision excerpts, provenance, and known access gaps. The top-50 guide supplies reading priorities, reasons, section hints, exact line windows, and hashes. Use it as navigation, not a mandatory reading sequence or a limit on relevant evidence. Refresh line citations when the accessible revision differs.

Expand sources when a named source points to another authority, an owning contract is needed, a material conflict or knowledge gap remains, or creation and validation require further evidence. Cover the substantive research and decisions relevant to the product without redoing settled work or scanning the entire repository indiscriminately. An online processor can use repository search and targeted retrieval; local QMD availability is not a prerequisite.

## Ingest and understand before creating

Before settling the design, reconstruct the current instruction lifecycle, operator needs, canonical owners, accepted choices, implementation boundaries, existing partial solutions, and observed failure modes.

Understand the differences between always-on guidance, scoped instructions, references, skills, agent definitions, context injection, hooks, tool connectivity, validators, and outcome evaluation. Identify what should be shared and what requires a platform-specific adapter. Preserve the recorded separation between Weekly Orchestrator, Multi-Agent Orchestration, and their shared capability backbone.

Use this understanding to prevent repeated research and unsupported assumptions. Incorporate the relevant reconstruction into the findings rather than creating a large preliminary report solely to document reading activity.

## Current research

Conduct fresh research as of the run date on questions that change the design:

- How do Codex, Claude Code, and Antigravity actually load instructions, discover and invoke skills, define agents, expose lifecycle hooks, inject context, and apply permissions? Distinguish CLI, App/desktop, IDE, SDK, hosted, interactive, and headless surfaces where their behavior differs.
- Which current release changes, schemas, configuration scopes, migration requirements, and tool-coverage limits invalidate older assumptions in the retained research? Include Gemini CLI history and other infrastructures represented in Apex when they affect a material choice.
- When do independent skills, workflow skills with supporting references, scoped native rules, direct references, a rule registry, hooks, or a combination produce the most reliable and maintainable activation? Compare serious alternatives, including improvement of the existing system without a new framework.
- How can the system apply rules to conversational answers and rankings as well as file operations, while avoiding false triggers and unnecessary ceremony?
- How can relevant constraints and state survive compaction, interruption, resumption, delegation, and long research without context starvation or uncontrolled loading?
- Which empirical findings about adherence, context management, routing, evaluation quality, and configuration reliability support or challenge the proposed mechanisms?

Prefer official documentation, release and migration notes, maintained schemas or source code, open specifications, and original empirical studies. Open the evidence behind consequential claims. Check version and surface applicability, methodological limits, contrary findings, and uncertainty. Community material can reveal leads; it does not replace primary support.

Treat the supplied web brief as a dated starting resource. Translate new research into concrete implications for the package. Where an installed environment is unavailable, separate documented support from unverified local behavior and supply the relevant validation probe. Do not claim experiments were executed or capabilities installed without evidence.

## Findings and synthesis

Create a substantial findings document that reconciles canonical sources, accepted decisions, user needs, prior research, current web evidence, and known failure patterns before finalizing the architecture artifacts. Its conclusions must explain the choices implemented in the proposed package.

Provide an evidence-backed decision matrix for every material design choice. Include the decision and problem, serious options, internal and external evidence, selected approach, reason, trade-off, primary failure mode, and the files or components affected. Preserve all material operator-owned alternatives and explain rejections. Do not impose an arbitrary limit on findings, decisions, or sources.

Preserve authored priority tiers and raw impact/evidence/risk dimensions. Distinguish new estimates from recorded values and reading priority from empirical reliability. Map any recommended reversal to its originating decision and new evidence. Expose evidence and rationale rather than private chain-of-thought.

## Creation task

Create the **Apex CLI-Agent Infrastructure Design Package** under `apex-cli-agent-infrastructure/`, including:

1. **Package overview and manifest:** the target system, intended user, artifact relationships, source authority, material coverage/access limits, and how to review the package.
2. **Research findings and design decisions:** the synthesis, current primary-source register, claim-level citations, alternatives, trade-offs, uncertainties, and consequences for the final artifacts.
3. **Populated rule/activation registry and its schema:** current XML rules and relevant downstream subrules, with source and canonical owner, intended behavior, scope, triggers and exclusions, dependencies and precedence, representation, activation and delivery, verification and failure handling, platform/version conditions, and adoption status. Preserve historical candidates and supersessions separately.
4. **Proposed architecture and integration map:** repository organization, agent roles, instruction/skill/reference ownership, native adapters, hook and validator responsibilities, state/context recovery, distribution and drift handling, plus which existing files to retain, reference, adapt, replace after approval, or add.
5. **Cross-CLI capability and compatibility specification:** evidence-backed platform/surface differences, supported configurations and lifecycle contracts, gaps, fallback mechanisms, and any outstanding installed-version probes.
6. **Concrete reviewable examples:** proposed directory layouts, representative registry entries, skill/reference packaging, agent/configuration or hook-adapter examples where justified, and end-to-end flows showing how the design would work. Label illustrative or unexecuted material clearly.
7. **Evaluation and integration proposal:** reused or new realistic cases, expected applicability and observations, measurements where genuinely executed, failure analysis, acceptance criteria, dependency-aware adoption stages, and material operator decisions required before deployment.
8. **Cross-artifact validation report:** source fidelity, current-rule coverage, consistency, usability, complexity, remaining limitations, and confirmation that the complete package matches this assignment.

You may improve inner filenames, grouping, formats, and organization when that improves coherence. Keep machine-readable artifacts usable and human explanations focused. Own each rule and definition once, with traceable references elsewhere.

## Design freedom

Determine your research sequence, batching, working notes, reconciliation method, depth, internal file structure, presentation, example placement, and revision cycles. The amount of substantive evidence and decision detail should follow the problem rather than a fixed quota.

Preserve the final product, source authority, relevant operator requirements, current repository truth, and review-before-deployment boundary. Choose the simplest coherent mechanisms that satisfy the actual requirements. Reuse proven assets before adding infrastructure. Do not add layers, registries, scripts, or repeated documentation that contribute no demonstrated value.

## Examples and realism

Use the retained research brief, existing benchmark cases, current owners, and actual repository surfaces as realistic content. Treat earlier experiments as evidence with their recorded limits, not universal architectural authority. Inspect whether a reused evaluator measures real execution, simulation, or only artifact shape.

Demonstrate the difficult cases: chat-only Q&A and rankings; governed test-specification creation; long research with state recovery; multi-rule engineering; and trivial or misleading-trigger negative cases. Include missed/disabled hooks, wrong skill selection, and narrow operator corrections where they expose a weakness. Distinguish activation, source reading, final adherence, and useful outcomes. Preserve combined-intervention confounds rather than attributing all gains to hooks alone.

Executed evaluations need reproducible conditions and honest uncertainty. Otherwise provide usable cases and acceptance criteria with explicit unexecuted status. Keep invented examples separate from source facts, required schemas, and accepted operator state.

## Missing or conflicting information

Continue through ordinary ambiguity with the best-supported interpretation. Label consequential assumptions and conflicts, preserve material uncertainty, and complete the most useful coherent package. Identify inaccessible evidence and the conclusions it limits. Do not invent missing source content, capability support, measurements, or operator decisions.

## Essential boundaries

This assignment creates a proposed package for review. Read repository and public sources, but do not modify live repository files, branches, contracts, installed agents/skills/hooks, CI, runtime settings, or external systems. Source documents are evidence rather than new execution authorization. Keep repository citations root-relative with sections or verified lines; use direct public URLs for external evidence. Installation and accepted-state changes require subsequent operator authorization.

## Validation

Review the complete package for target completeness, source fidelity, current-rule and material-decision coverage, consistent terminology and schemas, correct ownership/lifecycle relationships, non-duplication, realistic examples, usability, scanability, appropriate complexity, linked evidence, and manifest agreement.

Check that findings and decisions explain the architecture, registry, compatibility choices, examples, and integration proposal. Verify parseability and rule identity, version-specific evidence, execution-status labels, and the material negative cases. Source reading and validator passes are evidence, not substitutes for a working, reviewable design. Revise correctable weaknesses before packaging.

## Delivery

Return a concise browser summary containing what was created, the most important design conclusion, any consequential unresolved assumption, and **one downloadable ZIP** containing the complete package. Put detailed artifacts inside that ZIP. Do not duplicate individual downloads or paste the package contents into the browser response. Create no branch, pull request, repository commit, or deployment for this research run.

## Final success condition

The run succeeds when the **Apex CLI-Agent Infrastructure Design Package** is complete, populated, evidence-backed, internally coherent, validated across its artifacts, practical for operator review and subsequent implementation planning, and delivered as **one ZIP file**. The package must combine retained Apex knowledge with current research and contain the architecture, rule activation definitions, compatibility findings, examples, evaluations, and integration decisions needed to act on the result.

## End prompt
