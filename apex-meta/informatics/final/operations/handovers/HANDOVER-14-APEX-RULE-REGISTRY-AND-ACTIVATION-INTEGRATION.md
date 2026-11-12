---
okf_version: "0.2"
type: Handover
id: HANDOVER-14-APEX-RULE-REGISTRY
title: Apex Rule Registry and Unified Activation Architecture Handover
description: Reconstruct the complete instruction and research lineage, then design evidence-based rule ownership, routing, skills, hooks, injection, state recovery, and verification as one coherent Apex system.
status: proposed
tags: [informatics, handover, rule-registry, instructions, skills, hooks, routing, context-engineering, research]
---

# Handover 14 — Apex Rule Registry and Unified Activation Architecture

## 1. Target and current state

**Objective:** Establish a source-traceable, ranked and testable Apex Rule Registry covering the entire applicable instruction ecosystem. Determine how each rule is best represented, activated, delivered, enforced, evaluated and maintained across Codex, Claude Code, Antigravity, and relevant repositories. The final research must produce a *populated proposed registry and a defensible target architecture*, not merely another abstract proposal.

**Repository:** leela-spec/apexai-os-meta, branch main. Research owner: apex-meta/informatics/final/. This handover and its linked Pro prompt are research authorizations only, not permission to install hooks, convert skills, change the live XML, or edit other operating files.

**Current truth:** apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml is the ratified 23-rule always-on contract. Retain it unchanged while evaluating improvements. Apex already maintains a research corpus, modules, conditional refs, carrier sync, rule-to-research mapping, and an experimental hook specification.

**Pro research launcher:** HANDOVER-15-PRO-THINKING-APEX-RULE-REGISTRY-RESEARCH-PROMPT.md in this same directory.

## 2. Diagnosis — evidence, not a new invented architecture

1. The existing research **already studied** semantic routing, keyword routing, scoped rules, Agent Skills and progressive disclosure. See research/01-universal-instruction-research/05-INSTRUCTION-ACCESS-AND-SERIALIZATION-MATRIX.md; research/02-deep-reasoning/06-how-the-routing-actually-works.md; research/09-ultra-contract-and-layers-synthesis/index.md (especially Topic 2 ref/when gating and Topic 3 skill invocation triggers).
2. Prior work divided universal instructions, deep specifications, vendor carriers, runtime hooks and operational evaluations into separate work packages. No confirmed unified, per-rule activation-to-compliance registry currently binds all of them.
3. Handover 13 was explicitly scoped to CLI hook compatibility, shared Python organization and limited operational guardrails. Its completed design is specs/cross-cli-hook-architecture.md, status proposed; no shared runtime installation was verified. Do not mistake this narrow scope for a comprehensive review of skill routing or conversational-answer compliance.
4. Empirical Round 2 Antigravity evidence: XML/footer baseline 18/33 versus XML + hooks + workspace reminders 31/33. The intervention was combined. Pre-tool denials drove required handover-spec pre-reads; closeout reminders drove separate gains. T3 showed possible over-application. This is **not** proof that hooks alone solve every rule.
5. Earlier research made specific selections, including selective high-leverage skill gates. Preserve those decisions as provenance; re-evaluate rather than assume they were never considered.
6. Current CLI documentation supports additional lifecycle integration, but vendor support varies by event, installed version, trust, CLI surface and execution path. Cross-CLI equivalence must be demonstrated, not inferred.

## 3. Operator requirements to preserve

- **Complete decision surface:** Material operator-owned alternatives must remain visible with grounded mechanisms, rankings, recommendations, rejections and uncertainty. Do not narrow the substantive choice set to a "smallest needed choice." Routine reversible implementation decisions may remain autonomous.
- **Rules apply to answers as well as files:** Q&A matrices, rankings, communication format, evidence standards and research methods must activate for a purely conversational request; file-write gates alone are insufficient.
- **Reliable discovery:** Prefer established platform routing (native skill metadata, file/path-scoped rules, lifecycle hooks and supported plugins) over speculative keyword-only behavior. Evaluate a shared rule registry as an additional coordination layer.
- **Dynamic context:** Inject task-relevant instructions just in time. Do not load entire rule libraries at startup; retain persistent task state and restore critical constraints across resumption, compaction, delegation and iteration when supported.
- **Independent verification:** Reading a spec is not proof of compliance. Separate instruction activation, tool enforcement, schema validation, output quality evaluation and outcome verification.
- **Full source traceability:** Every extracted rule, origin, historical decision, supersession, conflict, routing trigger, and evaluation finding must have reproducible provenance and confidence. Preserve source intent; no fabricated ratings or findings.
- **Proportionality:** Trivial tasks must not trigger heavyweight preflights, irrelevant reads or repetitive remediation. Explicit exceptions and negative cases matter.
- **One canonical owner:** Avoid copied contracts across XML, skill bodies, hook scripts and vendor carriers. References and adapters should depend on authoritative definitions, with drift checks.
- **No unauthorized mutation:** An architectural recommendation is not approval to install it. Work on main only; no branches or PRs unless newly requested.

## 4. Repository evidence map — prioritized entry points

**Live authority**
- apex-meta/informatics/final/index.md — corpus navigation and rule-to-research matrix.
- apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml — current 23-rule constitution.
- apex-meta/informatics/final/specs/ — writing profile, file architecture, execution modes and adapters, anti-drift, governance schemas, informatics router, standard, shared carrier layer.
- apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md and tools/apex_carrier_sync.py, tools/check_vendor_drift.py — current distribution ownership.

**Design lineage, disagreements, research and findings**
- apex-meta/informatics/final/research/01-universal-instruction-research/ — module map, semantic trigger research, instruction-access matrix, module-deepening records and corrections.
- apex-meta/informatics/final/research/02-deep-reasoning/ — routing reality, overlap ownership, module analysis and prior architecture options.
- apex-meta/informatics/final/research/03-research-of-file-10/ through research/09-ultra-contract-and-layers-synthesis/ — underlying experiments, rule research, options and settled/provisional interpretations.
- apex-meta/informatics/final/research/06-layered-rule-kb/ — historical 22-rule atomic decomposition and audits; reconcile to 23-rule current contract, do not silently substitute it.
- apex-meta/informatics/final/research/08-read-trace-routing-experiments/ and research/10-ultra-upgrade-validation/ — measured activation/compliance, benchmark fixtures, outcomes and known confounds.
- apex-meta/informatics/final/operations/handovers/HANDOVER-08-DETERMINISTIC-ENFORCEMENT-FOR-JIT-GATES.md, HANDOVER-12-TEST-UPGRADED-CONTRACT-AND-ALIGNMENT-ARMS.md and HANDOVER-13-CROSS-CLI-HOOK-ARCHITECTURE-AND-REPOSITORY-ORGANIZATION.md.
- apex-meta/informatics/final/specs/cross-cli-hook-architecture.md — proposed shared hook implementation, **not** proof of deployment.
- Historical program root apex-meta/handoff/universal-ai-instruction-system/ and earlier corrections, where still present; historical proposals are evidence, not current authority.

**Integration and deployment surfaces**
- Repository-root AGENTS.md, CLAUDE.md, GEMINI.md and local scoped variants; .agents/, .claude/, .cursor/, .kiro/, .windsurf/, .pi/, skills-lock.json, skill-package-template/, relevant scripts and skill directories.
- leela-spec/mindful-bar and leela-spec/Leela-Cloud-2026 only for actual carrier and hook/skill compatibility evidence; they are not substitute governing authorities for Apex. Leela's default branch has historically been master; verify any future integration plan instead of assuming main exists.
- Official CLI, skill, plugin, hook, model-context and trust documentation as of execution, alongside installed-version probes if the environment provides them.

## 5. Complete coverage without uncontrolled bulk reading

Begin from a complete Git tree and the final master index. Record an inventory of potentially governed rules, metadata, templates, references, skills, vendor carriers, hooks, validators, experiments and archived versions. Classify every candidate as current, historical, duplicate, proposed, unrelated or inaccessible. Make an explicit in-scope/excluded ledger so "all" is auditable.

Use deterministic indexing/search where supported and read the authoritative owner plus only the research needed to resolve each rule's origin, intended behavior, conflicts and evidence. Research-derived candidates that were never adopted must remain separately marked. Do not read tens of thousands of unrelated blobs into the model context.

"Everything ever wanted" means the full **accessible evidence record**. Repository files, retained decisions and provided handovers are discoverable; conversations or local files not present in the accessible corpus must be listed as evidence gaps, never silently invented.

## 6. Per-rule registry contract to design and populate

Every rule or conditional subrule should be traceable to at least these conceptual fields; the research may refine the schema:

- stable_rule_id; canonical_owner; exact source path and section or line; source version/status; operator intent; original rule text pointer; duplicates/supersessions/conflicts.
- applicability_scope (global, repo, path, task, operation, response, lifecycle); explicit trigger examples; semantic-intent examples; negative triggers/exclusions; dependencies; precedence; collision resolution.
- normative priority tier (retain native P0–P3 as-is); original raw I/E/R when present; independent re-evaluated importance, risk, evidence, frequency and impact; confidence, scoring rationale and comparative rank. **Never conflate I/E/R or manufacture scores.**
- preferred representation (constitution, scoped instruction, standalone skill, skill-bundled reference, direct reference, validator/schema, hook, plugin-distributed unit, or combination) with alternatives/rejection rationale.
- activation mechanism (native routing, explicit invocation, path match, intent classifier, hook event); delivery mechanism (pointer/read, skill activation, injection); enforceability (hard, soft, output-checkable, judgment-only); independent verification and failure handling.
- source-of-truth update path; vendor support/version conditions; context/token and latency budget where measured; false-positive risk; adversarial/negative test identifiers; adoption status.

Do not preselect a single technical representation for all rules.

## 7. Decision studies required

Compare, with primary documentation and empirical tests where possible:

1. **All references as skills** vs **selected workflow skills + supporting references** vs **registry-directed references with minimal skills** vs **hybrid native skills + scoped rules + hooks + independent validators**. Evaluate retrieval recall, correct activation, context footprint, drift, false positives, maintenance and portability.
2. **Prompt recognition:** keywords/tags, semantic-intent classification, native skill descriptions, native path scope, explicit operator invocation, and hybrid selection. Test synonyms, multilingual prompts, omissions and misleading keyword matches.
3. **Context injection:** SessionStart, prompt-submission, Antigravity invocation, skill dynamic content, tool events, compaction and subagents. Respect documented event payloads, trust, ordering and lack of equivalent events.
4. **Execution confidence:** contract-only vs skill-only vs registry+injection vs lifecycle-gated and validated hybrids. A pre-read event is not a semantic correctness oracle.
5. **Distribution:** canonical registry in meta repository, plugin/skill packaging, repo-specific adapters and vendor carrier sync without editing identical policy in several locations.
6. **Prior accepted choices:** identify where improved vendor capabilities justify revisiting older selections, and where they do not. Expose all material alternatives to the operator.

## 8. Mandatory realistic evaluations

At least these user stories and counterexamples:

- **Q&A without file creation:** The operator asks which architecture to choose, with alternatives, raw I/E/R, evidence, full material choice surface and final recommendation. The relevant format must activate despite no tool write.
- **Test-specification file creation:** Grounded ownership, destination, spec pre-read, schema requirements, scoped file mutation and independent resulting-artifact validation.
- **Ranking and communication:** A conversational ranking request with misleading/missing keywords, explicit exclusions and a simple explanation that should not invoke a full Q&A skill.
- **Long research:** Iterations with many source files, context compaction, re-entry, delegation, task-state persistence, no bulk context, no stale decisions.
- **Complex engineering:** Multi-rule software task involving architecture, scope, file changes, tests, Git hygiene and completion verification.
- **Negative controls:** Typo fix, one-line lookup, user requests no file write, quoted keywords only, superseded refs, disabled/untrusted hooks and failed or skipped skill activation.

Compare all contenders using the **same tasks** and report activation precision/recall, missed mandatory gates, incorrect gates, final compliance, output quality, token/context cost, latency, false positives and infrastructure footprint. Distinguish measured from estimated results.

## 9. Expected Pro research product

Produce a cohesive proposed package under the conceptual root apex-rule-registry-research/ containing:

1. README and source authority / coverage manifest.
2. Populated machine-readable rule registry, schema, trigger catalog and source/owner crosswalk covering all current rules and relevant conditional detail.
3. Canonical owner, duplication, supersession, conflict and historically rejected-options ledger.
4. Comparative architecture and cross-CLI lifecycle/skill/plugin capability matrix with authoritative citations and version caveats.
5. Rule-by-rule priority/risk/evidence ranking, representation recommendation, enforcement/verification matrix and alternatives.
6. Concrete routing/injection examples, reference-vs-skill packaging decisions and compaction/task-state protocol.
7. Reproducible test cases, baselines, acceptance criteria, results where actually executed, and a validation/coverage report.
8. Proposed integration/migration plan and operator decision Q&A; **no implicit acceptance or implementation**.

Prefer OKF 0.2-compatible metadata and machine-readable YAML/JSON for persistent registries, with concise human-readable explanations. Keep the detailed deliverables out of the chat body.

## 10. Execution and authority boundaries

- **Research only:** No change to XML, existing AGENTS/CLAUDE/GEMINI carriers, reference files, hooks, skills, CI, vendor copies or branch settings in this phase.
- **Output:** Pro run returns one downloadable ZIP with the complete research package; repository writes are not authorized by this handover. Installing the resulting system requires a subsequent explicit operator decision.
- **Research quality:** Use primary vendor documentation and direct executable probes if available. Label unsupported/inaccessible local capabilities. Do not imply current functionality merely because a future design describes it.
- **Validation:** Source coverage, taxonomy coherence, known-rule reconciliation, cross-CLI facts, negative test cases, non-duplication and output completeness. Report deviations rather than claiming completion without proof.

## 11. Next continuation

Execute the separate Pro Thinking prompt in HANDOVER-15-PRO-THINKING-APEX-RULE-REGISTRY-RESEARCH-PROMPT.md with the live repository accessible. Evaluate the full architecture and produce the populated registry before proposing any implementation changes.

**Completion of this handover's next research step means a verifiable, exhaustive-in-scope, evidence-ranked proposed Apex registry and activation system delivered for operator review, not just another untested architectural opinion.**
