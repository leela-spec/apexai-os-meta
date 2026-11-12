---
okf_version: "0.2"
type: ExecutionPrompt
id: HANDOVER-15-PRO-THINKING-APEX-RULE-REGISTRY
title: Pro Thinking Research Prompt — Complete Apex Rule Registry and Unified Agent Instruction Architecture
description: High-autonomy, evidence-grounded research brief to extract and rank the complete accessible Apex rule corpus and deliver an integrated, testable, cross-CLI activation and compliance architecture.
status: proposed
tags: [informatics, pro-thinking, research-prompt, rule-registry, skills, hooks, agent-instructions, routing]
---

# Pro Thinking Prompt — Complete Apex Rule Registry and Unified Activation Architecture

## Use

Paste the text from **Start prompt** through **End prompt** into a Pro/extended-thinking research agent with access to `leela-spec/apexai-os-meta` and current public documentation. Attach **01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md** if the receiving environment cannot access the uploaded copy. The *preceding* Handover 14 provides extended rationale, exact coverage cases and research orientation; this prompt remains usable independently.

## Start prompt

<system_instruction>
You are the independent instruction-systems research and architecture lead. Research, reconcile, rank, and create a **complete, source-traceable, proposed Apex Rule Registry and cross-CLI activation architecture** in one continuous run. Your primary deliverable is the populated and validated research package, not a general discussion, proposal to do research later, unverified hook deployment, or rewritten live rules.

Use high-autonomy research judgment. Define the destination, source authority and acceptance criteria precisely; choose an efficient internal workflow yourself. Do not invent source evidence, operator decisions, implementation status, compatibility or benchmark results.
</system_instruction>

<context>
- Repository: `leela-spec/apexai-os-meta`; current branch: `main`.
- Owning area: `apex-meta/informatics/final/`.
- Immediate handover: `apex-meta/informatics/final/operations/handovers/HANDOVER-14-APEX-RULE-REGISTRY-AND-ACTIVATION-INTEGRATION.md`.
- Ratified always-on constitution: `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml` (23 rules; **read-only**).
- Current cross-CLI hooks design: `apex-meta/informatics/final/specs/cross-cli-hook-architecture.md` (proposed; **not deployed**).
- Operator problem: AI agents regularly fail to activate, read, understand or follow their instruction references. Problems affect **conversational outputs**, Q&A and rankings, governed file creation, multi-rule engineering, research, long iterations and handovers. File-write hooks alone cannot solve them.
- Intended operators: a non-programmer overseeing Codex, Claude Code, Antigravity and ChatGPT/browser workflows across multiple repositories.
- Critical desiderata: exhaustive accessible source coverage, transparent rule provenance and raw impact/evidence/risk dimensions, robust native discovery, conditional context injection, low token waste, independent outcome verification and no silent migration.
- Do not treat current contracts, historical analyses, accepted choices, proposed patches and experiments as equal authority.
</context>

<target>
Deliver a **populated, reproducible, research-backed Apex Registry and Activation System proposal** which explicitly answers, rule by rule:
1. What was originally intended and what is authoritative now?
2. Which prompts, intents, file operations, lifecycle events, paths or state transitions activate the rule?
3. Should it be always-on, path-scoped, a native Agent Skill, a skill-bundled reference, a standalone reference, a plugin, a hook-enforced invariant, a schema/validator, or a combination? Why?
4. How is it selected, loaded/injected, executed, verified and maintained?
5. What priority, impact, evidence, risk, frequency, false-positive cost and coverage confidence does it have? Preserve original P0–P3 and separate raw I/E/R where present. Provide a separate explicit comparative ranking without inventing quantitative source facts.
6. How do precedence, exclusions, dependencies, skill collisions, absent hooks, compaction, delegation, stale sources and version differences affect it?
7. What demonstrable mechanism prevents the same historical failure mode from recurring?

Make the research cover the **entire accessible Apex instruction program and materially relevant precursor research**, not only the XML contract, not just Handover 13, not only the informatics specs, and not only a few illustrative rules. Include proposed/retired/rejected instructions in a distinct historical lineage rather than treating them as active.
</target>

<authority_and_starting_sources>
Use authority in this order:
1. Ratified live contract, active operational specifications, current carrier ownership and explicitly accepted operator decisions.
2. Authoritative owner files and current repository state for each domain or module.
3. Empirical execution traces, benchmarks, reproducible tests and current installed behavior when accessible.
4. Prior research syntheses, module studies, archives, candidates and handovers as historical evidence and design hypotheses.
5. Current official vendor documentation, official Agent Skills specification, relevant engineering literature and external research for capability and best-practice claims; do not allow external generalities to silently replace accepted Apex semantics.

Named repository entry points (expand by source links, inventory and targeted search):
- `apex-meta/informatics/final/index.md` — live corpus map, rule-to-research matrix.
- `apex-meta/informatics/final/specs/` — XML, writing profile, file architecture, execution modes + adapters, anti-drift, governance schemas, general informatics router, standard, carrier layer.
- `apex-meta/informatics/final/research/01-universal-instruction-research/` — module map, instruction access/serialization research, module deepening, past corrections and handovers.
- `apex-meta/informatics/final/research/02-deep-reasoning/` — router reality, context/token and overlap/owner audits.
- `apex-meta/informatics/final/research/03-research-of-file-10/` through `10-ultra-upgrade-validation/` — complete relevant research lineage, prioritization research, vendor and hook experiments, 22-rule historical KB, read-trace experiments, integrated seven-topic synthesis and latest benchmark.
- In particular, `research/01-universal-instruction-research/05-INSTRUCTION-ACCESS-AND-SERIALIZATION-MATRIX.md`, `research/02-deep-reasoning/06-how-the-routing-actually-works.md`, `research/09-ultra-contract-and-layers-synthesis/index.md` (Topics 2 and 3), `research/10-ultra-upgrade-validation/01-results-and-verdict.md`.
- `apex-meta/informatics/final/operations/handovers/HANDOVER-08-DETERMINISTIC-ENFORCEMENT-FOR-JIT-GATES.md`, `HANDOVER-12-TEST-UPGRADED-CONTRACT-AND-ALIGNMENT-ARMS.md`, `HANDOVER-13-CROSS-CLI-HOOK-ARCHITECTURE-AND-REPOSITORY-ORGANIZATION.md`, and the preceding HANDOVER-14.
- `apex-meta/handoff/universal-ai-instruction-system/`, original module evidence, prior accepted recommendations, superseded proposals and change records.
- Current root and scoped `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.agents/`, `.claude/`, other vendor-rule directories, existing skills, configs, validators, carrier sync and drift tools.
- For cross-repository deployment verification, inspect only relevant live carrier/skill/hook surfaces in `leela-spec/mindful-bar` and `leela-spec/Leela-Cloud-2026`. Do not edit those repositories.

Inventory the full live Git tree to establish coverage; **do not bulk-inject its contents into model context**. Use deterministic indexing, path inventories and selective retrieval. Record excluded materials and source-access gaps. An absent historical conversation, workstation file or external app record must remain an evidence gap, not be reconstructed from speculation.
</authority_and_starting_sources>

<research_questions>
Perform fresh, source-grounded research, including:
- Current official capabilities, actual installation/version caveats, trust and output schemas for **Codex, Claude Code and Antigravity**: prompt-submit, session-start, per-model/invocation, pre-/post-tool, Stop, compaction, subagents, skill metadata and invocation, CLI plugins, configuration inheritance and repo scope.
- The official **Agent Skills** open specification and platform-native skill routing behavior. Distinguish a registered skill from a mere file reference and from a rule embedded in agent instructions.
- Whether **every deep reference should become its own Skill**, and how skill discovery precision, competing descriptions, packaging overhead, and context costs compare with fewer coherent skills that own smaller reference files. Compare at least: all-as-skills, selected-workflow-skills-plus-references, registry-driven references without new skills, native-scoped rules, and a hybrid.
- Hooks as **event triggers**, registry routing as **selection logic**, injection as **context delivery**, skills as **execution procedures**, and validators as **independent artifact/outcome checks**. Test whether these boundaries can be combined without redundant independent owners.
- Deterministic keyword/tag signals versus semantic intent classification, native skill metadata, file/path triggers, explicit invocations and combinations; include German and English requests, synonyms, negative matches and misleading quoted signal words.
- Conversational-answer adherence and output-level verification (not merely file tools). Describe exactly what each platform permits, what requires a host orchestrator or evaluator, and what cannot be enforced by native hooks.
- Task-state persistence, iterative research, context compaction/recovery and resumed/delegated work without unbounded context injection.
- Industry best practices for policy-as-code, separation of authority/routing/execution/verification, source ownership, human-in-the-loop decisions, progressive disclosure, measurable compliance and non-overbearing tooling. Prefer official docs and primary research; differentiate established practices from design proposals.
- Why prior Apex work already studied these issues but did not deliver an end-to-end runtime architecture. Reassess prior accepted routing choices using **new evidence**, not hindsight alone.
</research_questions>

<comparative_evaluation>
Treat the approaches as genuine alternatives. Create a scored decision matrix with explicit criteria and weights justified by Apex operator priorities: correct activation and output adherence; false-positive obstruction; context/token and latency costs; task-surface coverage; portability; ease of maintenance; single-source-of-truth integrity; independent verification; and implementation complexity. Preserve Apex's native uncombined impact/evidence/risk estimators for operator-facing material decisions; do not silently replace them with weighted scores. Present both the multi-criteria architecture comparison and original rule-level priority dimensions.

For every substantive claim specify source, date/version where relevant, confidence and applicability. For benchmarked mechanisms separate what was measured from estimates and conjecture. Reuse prior traces and validators instead of creating a new framework merely to validate another framework.
</comparative_evaluation>

<mandatory_scenarios>
Require real examples and negative controls. At minimum:
A. Chat-only Q&A, options and recommendation with source grounding, uncombined I/E/R and a *full material operator choice surface*. No file write is required.
B. Chat-only ranking and standard response organization, including ambiguous intent, synonym triggers and keyword collision cases.
C. Create a test specification file with correct destination/format, prerequisite readings, safe changes, post-write schema and quality checks.
D. Iterative multi-source research surviving compaction, cross-session continuation, subagent handoff and task-state restoration without full re-reading.
E. Multi-rule software implementation involving scope authority, architecture, reuse, editing, tests, Git staging, commit/push and continuation.
F. Trivial typo or lookup must remain frictionless; no unnecessary broad skill, forced preflight or huge injection.
G. Hook missing/disabled/untrusted, skill missed, specification read but misunderstood, user manually invokes wrong skill, conflicting active rules and a prohibited action that requires a real hard stop.
H. A user correction that changes only a narrow target while other approved requirements remain intact.

Create a prompt bank and ground-truth rule applicability labels. Compare each architectural contender on the **same** cases, recording correct activation, misses, false positives, observed final adherence, hallucinated context, token cost, latency and intrusive behavior. Execute available tests when technically possible; otherwise create reproducible harness definitions with clearly unexecuted status and avoid fabricated metrics.
</mandatory_scenarios>

<required_outputs>
Create a coherent proposed research package organized under `apex-rule-registry-research/` with a concise README and manifest. The exact inner layout may be improved for coherence, but the following artifacts must exist:

1. **Complete source and coverage inventory** with provenance, explicit inclusion/exclusion and missing-access ledger, active-vs-historical reconciliation and current authority map.
2. **Populated machine-readable rule registry** (YAML or JSON; OKF 0.2-compatible metadata where meaningful), schema and rule-to-source crosswalk; cover all 23 XML tags and their meaningful conditional subrules plus relevant active downstream rules. Preserve atomic rule identity; enumerate inactive historical candidates separately.
3. **Trigger/routing catalog** specifying semantic intents, keywords as optional evidence, scopes/paths/events, positive and negative examples, dependencies, conflict precedence and invocation/delivery choices.
4. **Priority and traceability matrix** with raw existing P0–P3 / I/E/R where authored, re-evaluated comparative rankings with rationale/confidence, source lineage, duplicates, supersessions and unresolved contradictions. No synthetic certainty or unlabeled invented source ratings.
5. **Full option analysis and decision record** comparing skill packaging, reference-only, registry, hooks, native scoped rules, plugins, injection, validators and hybrids, with evidence-based recommendation and explicit rejection reasons.
6. **Cross-CLI compatibility and integration architecture** including version caveats, lifecycle event-to-rule mapping, recommended adapter points, trust/safety, fallbacks and distribution ownership.
7. **Context-injection and iteration specification** with bounded payload design, state schema, session/compaction/resume behavior and negative-context tests.
8. **Executable examples or unambiguous illustrative traces** for Q&A without files, rankings, test-spec creation, long research and complex development. Clearly label simulated versus observed behavior.
9. **Reproducible evaluation plan and fixtures** plus any honestly executed results and failure analysis. Include existing Round 2 data as distinct from new findings; do not attribute the combined improvement to hooks alone.
10. **Migration/integration proposal** that maps present files to retain-as-reference, convert-to-skill, retain-always-on, configure-as-hook, or validate-as-schema, including maintainer effort and backwards-compatible rollout.
11. **Operator decision surface**: ranked architecture alternatives, material unresolved trade-offs, grounded user stories, recommendation, remaining risks and explicit approval points.
12. **Validation/quality report** checking complete accessible-source inventory, current rule coverage, no contradictory authority, traceability, correct native capability claims and any unexecuted evaluations.

Package machine-readable registers and concise human-readable summaries together. Preserve source excerpts by link/path + section (or exact lines if reliably available), not verbatim bulk copies. Avoid two independently editable canonical versions of any rule.
</required_outputs>

<essential_boundaries>
- This is **research and proposed design only**. No changes to live XML, AGENTS/CLAUDE/GEMINI carriers, accepted specs, hook config, installed skills, CI or other repositories. Do not make current-system behavior claims based on merely proposed designs.
- Work against `main` if accessing Git; create no branches or PRs. **No repository writes are authorized for this research run**. Return artifacts as one ZIP; propose later repository integration for operator review.
- Keep historical outcomes, hypotheses, vendor docs and current runtime facts distinct. Validate official features against dated sources and installed versions when possible.
- The operator's substantive choice set must not be artificially narrowed under the language of minimality or context economy.
- Context minimization must not truncate research coverage: comprehensive inventory and indexed processing are required; selective *reading* should eliminate irrelevant token overhead without excluding relevant sources.
- No generic blocking checkpoints for ordinary ambiguity. Honor autonomy and direct execution where appropriate.
- Do not interpret this prompt's output instructions as approval to enact any recommended architecture.
</essential_boundaries>

<validation_and_delivery>
Before finalizing, verify manifest-to-file agreement; machine-readable parsing; rule ID uniqueness; every current XML tag mapped; provenance links; representation and activation completeness; historical/current separation; uncombined I/E/R; source-backed rankings; cross-CLI claims and version bounds; fixture coverage; negative cases; option analysis; non-duplication; and obvious operator usability.

Deliver **one downloadable ZIP** containing the full package `apex-rule-registry-research/`. The browser response should be concise: artifact link, the selected recommended architecture, major uncertainty and genuinely consequential operator decisions. Do not paste the whole research package into chat.

The run is successful when the complete **populated and traceable Apex Rule Registry and integrated cross-CLI activation architecture proposal** passes the listed coverage, evidence, consistency and validation checks, includes all required comparative analysis and scenarios, and is delivered as a single downloadable ZIP for operator review.
</validation_and_delivery>

## End prompt

## Launcher guidance

This prompt follows the uploaded *Pro Thinking Prompt Design Standard*: target-first, explicit authority, high-autonomy research, evidence-based synthesis, complete product delivery, material boundaries, and outcome-based validation. The named source set is a navigational starting point, **not** an exclusion of older applicable evidence. If browsing or GitHub file access fails, report exactly what could not be verified and still produce the strongest supported, clearly incomplete package possible.
