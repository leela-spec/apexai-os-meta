---
type: PendingPatchPacket
title: Pending Architecture Patches — Authority and Mutation Boundary
description: Aider-style patch instructions for integrating the remaining cross-cutting controls without using whole-file GitHub connector rewrites.
status: pending_executor_application
created: 2026-09-07
patch_format: Aider editor-diff / SEARCH-REPLACE blocks
---

# Pending Architecture Patches — Authority and Mutation Boundary

Do not apply these changes through a whole-file connector rewrite. Apply with an authorized patch-capable editor/executor, inspect the resulting diff, and then update this packet's status separately.

## README — add active planning references

`apex-meta/handoff/universal-ai-instruction-system/README.md`

```text
<<<<<<< SEARCH
1. `README.md` — current truth, module status, locked decisions.
2. `09-MODULE-DEEPENING-HANDOVER.md` — reusable execution contract for a fresh chat, including the authoritative AI-native-first evidence order.
3. `10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md` — retroactive audit of completed A01-A05 plus pending semantic patch proposals. Its proposed wording is not live until explicitly applied.
4. `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` — current non-active XML pilot whose individual module wording is refined by this program.
5. `07-TIER-A-COVERAGE-AND-LIVE-AGENT-AUDIT.md` — supporting audit/evidence when a module needs prior repo findings.
6. `apex-meta/AI-Snippets/Snippets.md` — operator-originated source ideas when provenance is needed.
=======
1. `README.md` — current truth, module status, locked decisions.
2. `09-MODULE-DEEPENING-HANDOVER.md` — reusable execution contract for a fresh chat, including the authoritative AI-native-first evidence order.
3. `10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md` — retroactive audit of completed A01-A05 plus pending semantic patch proposals. Its proposed wording is not live until explicitly applied.
4. `10-UNIVERSAL-SHORT-RULE-COVERAGE-TODO.md` — final-synthesis TODO ensuring every high-value short-rule control is covered, merged, or rejected with evidence before live propagation.
5. `11-ONLINE-MODEL-PATCH-HANDOFF-DECISION.md` — candidate repository mutation boundary for online/browser subscription models.
6. `12-PENDING-ARCHITECTURE-PATCHES-AUTHORITY-MUTATION.md` — pending patch packet for integrating authority and mutation controls without whole-file connector rewrites.
7. `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` — current non-active XML pilot whose individual module wording is refined by this program.
8. `07-TIER-A-COVERAGE-AND-LIVE-AGENT-AUDIT.md` — supporting audit/evidence when a module needs prior repo findings.
9. `apex-meta/AI-Snippets/Snippets.md` — operator-originated source ideas when provenance is needed.
>>>>>>> REPLACE
```

## README — add locked authority and mutation decisions

`apex-meta/handoff/universal-ai-instruction-system/README.md`

```text
<<<<<<< SEARCH
- A13 `<grounding>` owns **external grounding and real-world verification**. When a material decision depends on real-world facts, capabilities, methods, integrations, standards, maturity, or reliability, model reasoning alone is insufficient: verify against sufficiently current authoritative external evidence and, where feasible, direct observed behavior or tests. A08 governs the quality of evidence; C02 governs deeper research methodology.
- Proven elsewhere does not automatically mean fit here. Reused systems and components must still be validated against the actual target, constraints, and operating environment.
- Do not install or propagate candidate Skills or rewrite live root agent instructions during this module-deepening program.
=======
- A13 `<grounding>` owns **external grounding and real-world verification**. When a material decision depends on real-world facts, capabilities, methods, integrations, standards, maturity, or reliability, model reasoning alone is insufficient: verify against sufficiently current authoritative external evidence and, where feasible, direct observed behavior or tests. A08 governs the quality of evidence; C02 governs deeper research methodology.
- A14 `<authority>` owns **action authorization and side-effect boundaries**. Task scope does not by itself authorize durable, external, destructive, privileged, or consequential actions; those actions require authority appropriate to the action at execution time.
- C04 `<mutation>` owns **online/browser repository patch handoff**. For existing-file changes through browser/subscription-model repository workflows, use Aider `editor-diff` / SEARCH-REPLACE patch handoff rather than whole-file connector rewrites; a separate authorized editor/executor applies and verifies the resulting change.
- Proven elsewhere does not automatically mean fit here. Reused systems and components must still be validated against the actual target, constraints, and operating environment.
- Do not install or propagate candidate Skills or rewrite live root agent instructions during this module-deepening program.
>>>>>>> REPLACE
```

## README — queue A14 and C04 without changing the current NEXT module

`apex-meta/handoff/universal-ai-instruction-system/README.md`

```text
<<<<<<< SEARCH
| A12 | `<communication>` | Communication Economy | QUEUED |
| A13 | `<grounding>` | External Grounding & Real-World Verification | QUEUED |
| C01 | `<decision>` | Conditional Decision / Trade-off Discipline | QUEUED |
| C02 | `<research>` | Conditional Research Discipline | QUEUED |
| C03 | `<informatics>` | Conditional Informatics / Formal Authoring | QUEUED |
=======
| A12 | `<communication>` | Communication Economy | QUEUED |
| A13 | `<grounding>` | External Grounding & Real-World Verification | QUEUED |
| A14 | `<authority>` | Action Authorization & Side-Effect Boundary | QUEUED |
| C01 | `<decision>` | Conditional Decision / Trade-off Discipline | QUEUED |
| C02 | `<research>` | Conditional Research Discipline | QUEUED |
| C03 | `<informatics>` | Conditional Informatics / Formal Authoring | QUEUED |
| C04 | `<mutation>` | Online Repository Patch Handoff | QUEUED |
>>>>>>> REPLACE
```

## Pilot — add A14 authority candidate

`apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`

```text
<<<<<<< SEARCH
  <scope principles="scope-control,non-goals,change-control">
    Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
  </scope>

  <reuse principles="reuse-before-build,battle-tested-practice,adaptation-before-invention,fitness-for-use">
=======
  <scope principles="scope-control,non-goals,change-control">
    Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
  </scope>

  <authority principles="least-privilege,action-authorization,side-effect-boundary">
    Scope does not imply permission to act. Perform durable, external, destructive, privileged, costly, or consequential actions only when the action is authorized at execution time.
  </authority>

  <reuse principles="reuse-before-build,battle-tested-practice,adaptation-before-invention,fitness-for-use">
>>>>>>> REPLACE
```

## Pilot — add C04 patch-handoff candidate

`apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`

```text
<<<<<<< SEARCH
  <grounding principles="external-grounding,source-authority,real-world-verification">
    When a material decision depends on real-world facts, capabilities, methods, integrations, standards, maturity, or reliability, do not rely on model reasoning alone. Verify against current authoritative external evidence and, when feasible, direct observed behavior or tests; expose unresolved uncertainty.
  </grounding>

  <decision when="the operator must choose among material alternatives or explicitly asks for options"
=======
  <grounding principles="external-grounding,source-authority,real-world-verification">
    When a material decision depends on real-world facts, capabilities, methods, integrations, standards, maturity, or reliability, do not rely on model reasoning alone. Verify against current authoritative external evidence and, when feasible, direct observed behavior or tests; expose unresolved uncertainty.
  </grounding>

  <mutation when="an online or browser subscription model proposes changes to existing repository files"
            principles="patch-handoff,read-before-change,fail-closed"
            ref="apex-meta/handoff/universal-ai-instruction-system/11-ONLINE-MODEL-PATCH-HANDOFF-DECISION.md">
    Use Aider `editor-diff` / SEARCH-REPLACE patch handoff; do not rewrite existing repository files through whole-file connector updates. A separate authorized editor/executor applies and verifies the resulting change.
  </mutation>

  <decision when="the operator must choose among material alternatives or explicitly asks for options"
>>>>>>> REPLACE
```

## Handover — preserve actual-tool capability discipline

`apex-meta/handoff/universal-ai-instruction-system/09-MODULE-DEEPENING-HANDOVER.md`

```text
<<<<<<< SEARCH
Do not invent a local term when an established one already covers the behavior.

### B. Find existing proven agent implementations
=======
Do not invent a local term when an established one already covers the behavior.

Do not infer that a capability documented for a local coding agent, CLI, SDK, API, or shell-enabled runtime is available through an online/browser subscription model's connected repository tool. Verify the actual execution surface before designing a workflow around file-edit, patch, shell, Git, or other mutation capabilities.

### B. Find existing proven agent implementations
>>>>>>> REPLACE
```

## After application

- Re-read live `README.md` and verify the current `NEXT` module did not change.
- Inspect `git diff` / equivalent executor diff.
- Keep A14 and C04 `QUEUED`; do not mark them researched or DONE.
- Do not create module-deepening result folders for A14 or C04 until their dedicated runs.
- Do not apply further opportunistic cleanup.
