---
type: Reference
id: APEX-INFRA-ARCH-COMPARISON-20261112
title: Architecture Alternatives on Real Apex Task Families
description: Four-phase design bake-off with distinct estimated criteria, grounded paper walkthroughs and explicit limits.
status: draft
adoption_status: proposed_for_operator_review
tags: [alternatives, bake-off, estimates, evaluation]
---

# Architecture comparison

**The incremental native composition is the proposed pilot; the improved-existing-system alternative remains the mandatory baseline and a viable final outcome.** This document implements the four-phase EM-07/GS-13 rubric for the architecture question. It is a paper design comparison, not an executed agent experiment. The canonical numeric data is [architecture-bakeoff.json](../design/architecture-bakeoff.json). D-01 in [the decision matrix](../02-decisions.md) retains raw I/E/R separately.

## Phase 1 — Candidate discovery and hard gates

The seven serious options below cover the operator-owned all-references-as-skills proposal, retained small-routing improvements, native scoping, broader inlining, and a new router service. The historical evidence already discussed these patterns; no claim is made that this run invented them. Origins: `apex-meta/informatics/final/research/02-deep-reasoning/06-how-the-routing-actually-works.md`, §§4,7; `apex-meta/informatics/final/research/09-ultra-contract-and-layers-synthesis/index.md`, Topics 2–3; the retained activation brief §2. Original studies are appraised in [empirical findings](../evidence/empirical-findings.md).

Hard filters are source ownership, current operator permission, support for both conversational and governed-file outcomes, and a reversible isolated pilot. None may redefine the XML, delete a domain owner, infer acceptance, weaken native permissions or claim unsupported events. A full inline or monolithic candidate is considered only as a controlled projection of existing meanings, not a new source owner. A scoped-only candidate retains the core/direct-reference fallback for chat. A service candidate would require a separately approved service boundary; it cannot be deployed under this run.

All seven remain intelligible comparison options under those constraints. Native installation eligibility is conditional until the exact profile is probed. An unsupported arm is reported unsupported on that surface, never awarded a fictitious zero behavioral score. Deployment authorization is absent for every arm here.

## Phase 2 — Weighted criterion evaluation matrix

These are **new uncalibrated design estimates**, on the source-owned 1–100 criterion scale. They are not results of the case suite, empirical confidence or WP-07 I/E/R. The weights make the design preference reviewable: task coverage 30%, maintainability 25%, context selectivity 20%, portability 15%, inspectability/recovery 10%. Mechanism evidence is in D-01 through D-17 and the capability specification; the criterion scores themselves are explicitly judgment.

| Candidate | Coverage 30% | Maintenance 25% | Selectivity 20% | Portability 15% | Inspection 10% | Weighted criterion total | Primary Failure Mode |
|---|---:|---:|---:|---:|---:|---:|---|
| B — Incremental native composition | 95 | 80 | 85 | 80 | 90 | 86.50 | Wrong or skipped skill; missing hook coverage. |
| A — Improve existing native files only | 75 | 95 | 80 | 85 | 70 | 82.00 | Judgment reference omitted despite a correct pointer. |
| D — All references as independent skills | 85 | 60 | 70 | 80 | 85 | 75.00 | Conflicting descriptions or selection of a definition fragment. |
| G — Native scoped rules/direct refs | 65 | 85 | 85 | 60 | 75 | 74.25 | No path event for a chat-only decision; divergent descendant behavior. |
| E — One multi-task Apex skill | 75 | 65 | 55 | 85 | 65 | 69.00 | The monolith is chosen but a branch is skipped or irrelevant detail loaded. |
| C — Registry semantic router service | 90 | 35 | 90 | 35 | 90 | 68.00 | Router/service failure or another unverified policy authority. |
| F — All detailed rules always on | 90 | 40 | 15 | 70 | 55 | 56.00 | Context competition, irrelevant ceremony and duplicated projection drift. |

The totals do not validate the winner. They expose how the current judgments produce it. If maintainability receives 50% and coverage/selectivity 15% each, with portability/inspection 10% each, the improved-existing-only arm scores 86.25 and the proposed composition 84.00: the preference reverses. The empirical pilot must therefore test whether the proposed coverage benefit is real enough to justify its additional maintenance. Changes to those judgments are legitimate; changing I/E/R into this aggregate is not.

## Phase 3 — Ranked verdicts and two grounded walkthroughs

The ranking is conditional on the stated estimates and weights. It is not a measured reliability ordering.

**Common reversal boundary:** before installation, revise the proposal; after a bounded pilot, restore only captured pilot files/configuration. A service pilot additionally requires removal of its approved service dependency. Broad inlining requires removal of only the added projection, preserving all owner sources.

### 1. Incremental native composition — option B

**Placement verdict:** Select when P1 misses material cases and a bounded workflow improves outcomes. Avoid expanding if it adds no useful benefit.

**Apex operator deciding in chat, then authoring a governed specification:** Chat: native intent selects the decision workflow and its actual owners. Spec: authoring workflow plus tested path/operation constraints.

**Apex operator resuming long research with an unresolved source conflict:** Research: current state and source hashes recover through a supported boundary; receipt remains separate from correctness.

### 2. Improve existing native files only — option A

**Placement verdict:** Select when existing mechanisms meet the same cases. Keep as fallback. Avoid claiming it mechanically enforces missed semantic routes.

**Apex operator deciding in chat, then authoring a governed specification:** Chat: current XML prompts the model to open the owner directly. Spec: repaired routing/pointers guide the same direct read.

**Apex operator resuming long research with an unresolved source conflict:** Research: existing iterative/handover files preserve state; no new receipts or runtime layer.

### 3. All references as independent skills — option D

**Placement verdict:** Select if same-content tests show improved routing with tolerable metadata cost. Avoid when irrelevant selection or source drift increases.

**Apex operator deciding in chat, then authoring a governed specification:** Chat: the model chooses QA and bake-off skills separately. Spec: it must choose authoring, task fields and schemas without double-loading.

**Apex operator resuming long research with an unresolved source conflict:** Research: many metadata entries compete; source bodies remain authoritative references.

### 4. Native scoped rules/direct refs — option G

**Placement verdict:** Select for stable file families with proven loaders. Avoid as the sole mechanism for conversational activation.

**Apex operator deciding in chat, then authoring a governed specification:** Chat: depends on core/direct-reference recognition. Spec: verified native path scope supplies the appropriate rule.

**Apex operator resuming long research with an unresolved source conflict:** Research: recovery relies on existing current-state files; scope does not choose evidence by task meaning.

### 5. One multi-task Apex skill — option E

**Placement verdict:** Select only as a thin orientation entrypoint if useful. Avoid making it the normative owner of every workflow.

**Apex operator deciding in chat, then authoring a governed specification:** Chat and spec both invoke the same entrypoint, which branches into existing owner references.

**Apex operator resuming long research with an unresolved source conflict:** Research: the entrypoint can restore state, but broad scope makes selection and retention harder to diagnose.

### 6. Registry semantic router service — option C

**Placement verdict:** Select only after measured scale/selection failures defeat simpler repairs. Avoid without an approved service boundary and maintenance owner.

**Apex operator deciding in chat, then authoring a governed specification:** Chat: an external classifier selects EM-06. Spec: it selects file/authoring constraints before native execution.

**Apex operator resuming long research with an unresolved source conflict:** Research: the service must preserve task/epoch identity and handle outage/recovery; new operational dependencies appear.

### 7. All detailed rules always on — option F

**Placement verdict:** Select only a bounded critical slice supported by evidence. Avoid universal owner-corpus inlining.

**Apex operator deciding in chat, then authoring a governed specification:** Chat and spec both receive the whole detailed corpus before either needs it.

**Apex operator resuming long research with an unresolved source conflict:** Research: early details can still be lost or compete after long context; full loading does not prove adherence.

These walkthroughs use the actual conversational-ranking, test-specification and long-research tasks from the retained brief and new case suite. They predict mechanisms qualitatively; no simulated success rate or invented runtime measurement is assigned. The file-backed paper scenarios are distinct from the source-reported 72-cell Stage-1 experiment and Round-2 Antigravity runs.

## Phase 4 — Concrete prototypes and decision boundaries

For the leading incremental candidate, the complete inert [decision-support](workflows/apex-decision-support/SKILL.md.example), [governed-authoring](workflows/apex-governed-authoring/SKILL.md.example) and [research-cycle](workflows/apex-research-cycle/SKILL.md.example) procedures are reviewable. They open the existing owners and preserve exclusions. [Native adapter canaries](native/README.md) provide syntactically complete event/configuration examples and deterministic checks; they are not production enforcement code. Production guard construction is conditional on a demonstrated missing precondition.

For the improved-existing-only baseline, [exact pointer patches](../design/pointer-patch-proposals.json) and the existing native/direct-reference route are the complete proposed intervention: no new runtime, registry injection, skill or hook. Its future trial reads the same current XML and downstream owner content. The below model-facing action is an illustrative task procedure, not an installable core replacement:

```text
Use the current task and current operator authorization to determine applicability.
When the current XML condition matches, open its referenced owner before the dependent action.
Read any additional owner section needed to execute correctly.
Create the requested result within scope.
Verify the actual result against the original target and applicable owners.
For a long task, preserve the existing current-state/handoff fields before interruption.
```

**Select the incremental candidate if** the supported-profile comparison improves useful outcomes or required-source delivery on the relevant cases without material false triggers, scope breaches or unearned infrastructure burden. **Avoid further adapters if** P1 already satisfies the same cases or the adapter cannot observe the relevant event.

**Select all-reference skills if** the same-content P2 comparison improves discovery and final outcomes at acceptable metadata and maintenance cost. **Avoid it if** definition fragments are selected as tasks, overlapping packages compete, or source ownership is duplicated. This operator-owned alternative remains a live contender.

The [evaluation plan](../evaluation/evaluation-plan.md) supplies the independent architecture arms and the separate reminder × hook factorial. The [end-to-end flows](end-to-end-flows.md) show selected-path behavior and faults. Later operator review can select a different candidate without reconstructing the evidence.

**Failure guard:** preserve the distinction between a criterion estimate, a paper walkthrough, a synthetic software test and an executed agent trial. Let a supported smaller solution win if the actual outcomes justify it.
