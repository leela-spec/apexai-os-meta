---
type: Reference
id: APEX-INFRA-OVERVIEW-20261112
title: Apex CLI-Agent Infrastructure Design Package
description: Operator review guide, proposed target, artifact relationships, evidence boundary and concrete adoption choices.
status: draft
adoption_status: proposed_for_operator_review
research_date: 2026-11-12
source_revision: 6c93ad31e42a72de74119218b9365bdd9d6ee386
tags: [apex, infrastructure, design-package, review]
---

# Apex CLI-Agent Infrastructure Design Package

**Proposed target:** preserve Apex’s current 23-rule contract and detailed owners, improve native routing and source delivery, and verify actual outcomes independently. Use a declarative activation registry, three coherent workflow candidates and only the native adapters justified by a demonstrated gap. Keep the improved-existing-system option available as both baseline and fallback.

**Intended reviewer:** the Apex operator deciding the next repository, local-agent, instruction, skill and hook architecture. This is a complete design package for that decision, not a new installation, accepted-state update or abstract research handover. It contains concrete target paths, exact unapplied pointer corrections, inert examples, evaluation cases and an implementation sequence.

## What is populated

| Artifact | Contents and role |
|---|---|
| [Findings](01-findings.md) | Reconciles current authority, accepted scoped choices, implementation evidence, historical failures, current platform facts and empirical counterevidence |
| [Decision matrix](02-decisions.md) and [canonical decision data](design/decisions.json) | 26 material choices, 82 options, reasons, trade-offs, sources, new raw estimates and explicit reconsideration conditions |
| [Rule registry](registry/rules.json), [schema](registry/rule-registry.schema.json), [coverage](registry/coverage.md), [history](registry/history.json) | 145 populated records: 23 current XML tags, 100 detailed rule IDs, 22 relevant scoped clauses; original raw tags and historical supersessions preserved |
| [Architecture](03-architecture.md) | Ownership, native adapters, source delivery, task context, recovery, role boundaries, maintenance and distribution |
| [Integration map](04-integration-map.md), [machine map](design/integration-map.json), [pointer proposals](design/pointer-patch-proposals.json) | Existing-file dispositions and proposed targets; six exact, unapplied corrections across three files; no whole-file rewrite |
| [Compatibility](compatibility/compatibility.md) | Codex, Claude Code, Antigravity and relevant Gemini history, separated by surface; 49 source-linked claims and 14 unexecuted native probes |
| [Examples](examples/end-to-end-flows.md) and [architecture comparison](examples/architecture-comparison.md) | Chat-only decisions, governed specifications, long research/recovery, engineering and negative cases; serious alternatives and complete inert native/workflow templates |
| [Evaluation/adoption plan](evaluation/evaluation-plan.md) and [cases](evaluation/cases.json) | 22 unexecuted cases with focused assertions across all 23 XML rules; independent packaging arms and a reminder × hook factorial; acceptance and rollout stages |
| [Source guide](evidence/source-guide.md) and [empirical appraisal](evidence/empirical-findings.md) | 83 exact repository snapshots, 62 current primary external sources, study methods/limits and evidence-class distinctions |
| [Validation report](07-validation-report.md) and [manifest](manifest.json) | Actual package checks, independent review corrections, remaining limits and complete artifact hashes |

The machine files own the structured registry, decision data, integration map and case records. Human documents are navigation and interpretation views. Frozen source excerpts and snapshots support inspection without becoming second normative owners. No model should load this whole package as an always-on instruction block.

## Review in this order

1. Read the findings’ conclusion and conflict table, then the architecture. Confirm that Weekly Orchestrator and Multi-Agent Orchestration remain separate and that Plan-Sync-Session remains their shared capability backbone.
2. Review D-01, D-04, D-07, D-08, D-13, D-15 and D-26 in the decision matrix, then any affected choice from the navigation table. The all-reference-skills alternative remains visible and testable.
3. Follow one rule end to end: for example `XML.trade_off` → the live bake-off reference and QA owner → the decision-support example → native or explicit delivery → independent answer check → a case in `evaluation/cases.json`. Repeat for `XML.authoring` and one negative case.
4. Inspect the integration map and exact pointer proposals. Confirm the destination and scope of any stage you later authorize. The correct governance patch-schema link is retained; the existing standalone Git adapter is reused.
5. Read compatibility limits, the evaluation/adoption stages and the validation report before deciding on a pilot. A passed schema or synthetic check is not a native trial or installation acceptance.

## Evidence and authority

Authenticated `main` resolved to **`6c93ad31e42a72de74119218b9365bdd9d6ee386`**. The read-only run retrieved and checked exact source bytes at that revision. Of the guide’s 50 prioritized entries, 49 were retrieved; all 49 match the guide’s file hashes despite the different repository revision. The unselected prompt-design standard is not needed to repeat the already explicit research assignment. This is targeted source expansion, not a claim of an indiscriminate repository audit.

Authority remains: current operator instructions and live owners; accepted decisions in their recorded scope; observed configurations/implementation/execution; retained research and proposals; then current primary external evidence about capabilities. New vendor evidence can revise a loading assumption but cannot change Apex domain meaning. Original priorities remain separate from new estimates, criterion scores, reading priority and experimental measurements.

The package distinguishes documented capability, repository-observed content, source-reported trials, executed synthetic checks, design inference and proposal. The research container reported `codex-cli 0.167.0-alpha.4`; that is not the operator’s installation. The operator’s native versions, effective permissions, trust, account roots, global files and actual event/tool coverage remain to be probed.

## Main conclusions that affect approval

The lifecycle gap is broader than “make the agent read a file.” A correct source must be applicable, discovered, selected, delivered, executed and independently checked against the requested outcome. File-write hooks alone cannot activate chat-only rankings. Read receipts cannot establish comprehension. Current hooks also differ by event and surface; there is no universal before-model injector or shared permission envelope.

The current evidence favors a bounded pilot, not a universal framework. Small existing routing improvements performed usefully in the retained Stage-1 study, while some judgment reads still failed. The later Antigravity improvement combined hooks and reminders, so its whole gain cannot be assigned to hooks. The package also demonstrates four synthetic counterexamples in a retained scorer, requiring grader repair before new adoption metrics.

The proposed registry does not replace XML or detailed owners. Existing Plan/Sync/Session/Weekly/AIRouting skills stay in place. New portable workflow locations are pilot candidates under Hermes D05. Native carrier simplification remains conditional on verified loader behavior. The schema-mismatched Claude permission setting, whose installed effect is unknown, receives a probe and review item, not a bypass-enabling patch.

## Concrete next approval choices

The [adoption decision sheet](evaluation/evaluation-plan.md) supports a later scoped choice: accept the package as a design basis, revise a material decision, authorize S1 source/evaluator repairs and a read-only host audit, or authorize a named isolated S2 pilot after its prerequisites. S3 guards/carrier changes and S4 expansion are separate decisions. No recommendation is accepted by silence.

There was no repository edit, branch, pull request, commit, installation, CI change or deployment in this run. All new work is inside this proposed package. The ZIP is the complete deliverable; its manifest excludes only the manifest’s own hash to avoid a self-reference loop.

**Failure guard:** review the actual artifacts and evidence, preserve accepted source meaning, and approve only a concrete bounded implementation stage. Unknown installed behavior stays unknown until observed.
