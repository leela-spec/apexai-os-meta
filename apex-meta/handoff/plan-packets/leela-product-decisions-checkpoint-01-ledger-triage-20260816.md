---
title: "Leela Product Decisions Checkpoint 01 — Decision Ledger Triage"
document_role: iterative_planning_checkpoint
created: 2026-08-16
status: completed_initial_triage
project: leela-product-decisions
source_of_truth_rule: reread_this_checkpoint_and_current_leela_decision_registry_before_next_decision_workstep
canonical_mutation_performed: false
---

# Leela Product Decisions — Decision Ledger Triage

## Operating rule

This checkpoint is durable planning context for the broad operator goal "close decisions and questions across all of the app and project".

Before each subsequent decision workstep:

1. read this checkpoint;
2. read current `docs/ssot/decisions/OPEN_QUESTIONS.md`;
3. read current `docs/ssot/decisions/registry.csv` and `index.md`;
4. inspect the specific decision records/code/specs relevant to the next QA cluster;
5. save a new checkpoint before moving to the next cluster.

Do not reconstruct the decision queue from chat memory.

## Authority and process truth

Current Leela decision ledger rules are explicit:

- an agent may not resolve an open `QA-*` row by inference;
- genuine conflicts must be added rather than silently defaulted;
- a QA row closes only with a pointer to the artifact carrying the answer.

Therefore this project has two distinct types of work:

1. **reconciliation work** — prove that a row is already answered by an existing authoritative artifact and repair stale ledger state; this does not require a new operator choice;
2. **operator-choice work** — present only genuinely unresolved choices, with evidence, consequences and bounded options, then record the operator answer in a decision artifact.

## Initial repository findings

### The decision ledger is not internally synchronized

Confirmed example:

- `SSOT-D-027` in `docs/ssot/decisions/index.md` explicitly says it resolves `QA-130`.
- `docs/ssot/decisions/registry.csv` still marks `QA-130` as `open` with no answer pointer.
- the current Skill Tree feature spec also cites `SSOT-D-027` as closing the parent-summary question represented by QA-130.

Disposition: **ledger reconciliation defect**, not a new operator question.

This establishes that the global closure project must not bulk-present every row currently labelled `open`.

## Triage classes

### A. Immediate blockers to the current Leela Core Interaction milestone

These need verification and, if still genuinely open, small operator decision packets before the current Home -> Skill Tree -> frozen-resolution-context work can be fully settled.

#### QA-02 — Which entry flows are `ad_hoc` versus `path_bound`?

Why it matters now:

- current Algorithm SSOT permits current-window resolution with optional Path demand;
- current Packet-09 `ResolutionRequest` implementation requires a `PathDemandSnapshot` ID/revision;
- the current core-interaction v2 plan already flags this as `path_optionality_mismatch`.

Status after initial triage: **genuinely open candidate; evidence sweep required before operator packet**.

Related rows/contracts:

- QA-11 profile split / ad-hoc factor
- `SEQ-RES-001`
- current `ResolutionRequest`/`ResolutionContext`

#### QA-100 — Home scope/duration override persistence

Question: reset after each request, survive current Home visit, or persist until explicitly cleared?

Why it matters now:

- first Home -> Skill Tree slice introduces a real confirmed scope into Home request state;
- persistence changes only interaction state, not Algorithm ranking semantics;
- the current core milestone can technically use a bounded default, but choosing one silently would violate the ledger rule.

Status: **genuinely open candidate; direct operator-choice packet likely needed**.

#### QA-138 — Accessible non-spatial fallback for spatial Skill Tree

Why it matters now:

- current SSOT/materialization says bounded cluster is canonical and legacy list should be accessibility/debug fallback;
- the current Leela Core v2 plan must decide whether `/skill-tree` is retained as a supported accessible fallback or retired;
- current design sources disagree on mandatory versus optional fallback status.

Status: **genuinely open candidate; blocks final legacy-surface disposition, but does not block runtime verification of bounded cluster**.

#### QA-73 — What is `harmonization/` architecturally?

Why it matters now:

- current bounded Skill Tree confirmation pushes `HarmonizedPathScreen`;
- `SpatialRepository` reads through `LeelaReadRepository` from the harmonization package;
- many current runtime seams depend on `features/harmonization/`, but it is not one of the named 11 feature owners.

Status: **genuinely open ownership question; evidence sweep needed before deciding whether it blocks only naming/ownership or actual current integration**.

### B. Related but not required for the first Home -> Skill Tree milestone

These should remain visible but not enlarge the first development slice.

- `QA-131` — manual resolution-override persistence. Current `ResolvedScope` is transitional debt and the first milestone deliberately does not require manual override persistence; likely coordinate later with QA-100, but do not silently merge the questions.
- `QA-134` — Life-level selection. Current canonical `ScopeSelection.scopeType` is Epic/Block/Chunk; first milestone stays inside that enum.
- `QA-137` — Journey ownership. Important architectural ownership question, but the first milestone uses bounded Skill Tree structural discovery and does not need Journey ownership resolved.
- `QA-136` — unbuilt spatial alternatives disposition. Design-history cleanup, not a first-slice blocker.
- `QA-139` / `QA-140` — decision-ID namespace collisions. Important anti-drift cleanup, but independent of first interaction functionality.

### C. High-leverage broader product/architecture decisions

These should form later decision batches after the current milestone blockers are clarified:

- QA-07 — Sequencing Builder owner/concept and reconciliation of existing builder surfaces.
- QA-08 — creator-seeded priority and TP semantics.
- QA-10 / QA-11 — Sequencing identity/profile details.
- QA-13 — remaining acceptance-vs-placement atomicity question.
- QA-14 / QA-42 — high-risk cross-feature schemas and Precap/Recap policy.
- QA-16 — user-facing planned-vs-actual review lens.
- QA-17 — Variant ownership/identity cleanup.
- QA-20a — user-visible term collision around "Mode".
- QA-21a — universal Chunk cuttability versus TimingPolicy semantics.
- QA-76 — `primaryChunkIds` execution-authority defect/authorization.
- QA-101 / QA-102 — Stats expected-volume and best-practice-policy ownership.

### D. Evidence/source-integrity and SSOT-maintenance work

These may not need product choices, but they materially affect whether future agents can trust the repository:

- QA-30 — mandatory scientific research intake never consumed.
- QA-40 — 44 StatusQuo net-new candidates need disposition.
- QA-85 / QA-86 — semantic-patch provenance and unused Apex KB Phase-0 index.
- QA-141 / QA-142 — source-worklist hash/denominator defects.
- QA-143 / QA-160 — branch/current-trunk evidence mismatches, partly narrowed by Packet 09.
- QA-151 — largely executed Design/UX masterplan not retired, creating stale actionable instructions.

These should be handled as an evidence-reconciliation stream rather than dumped into an operator-choice queue.

### E. Future/deferred scope confirmation

Examples:

- QA-05 — confirm future boundary for streaks/badges/quests/etc.
- QA-103 / QA-104 — future feedback mode / point-cap provenance.

These should be batched only after current product blockers, unless they become execution blockers for another epic.

## Decision-processing workflow

For each cluster:

```yaml
workflow:
  1: select one coherent QA cluster
  2: reread current ledger + registry + relevant decision sheet
  3: inspect current code/spec/materialization and any newer decision records
  4: classify each QA as:
       - already_answered_ledger_stale
       - evidence_can_narrow_but_operator_choice_remains
       - genuinely_operator_only
       - obsolete_due_to_supersession
       - deferred_not_current
  5: persist evidence checkpoint to Apex Git
  6: for genuinely open choices, prepare a compact decision packet:
       - user-facing question
       - why it matters
       - 2-4 concrete versions
       - worked consequence/example
       - recommendation if evidence supports one
       - exact downstream artifacts affected
  7: obtain operator answer only when the project actually reaches that decision batch
  8: Leela decision record/ledger update is performed in the Leela repo under its decision authority
  9: re-read resulting artifact and verify downstream materialization/status
```

## Recommended processing order

1. **Core interaction blocker cluster:** QA-02/QA-11, QA-100, QA-138, QA-73.
2. **Reconcile stale already-answered rows:** start QA-130 and expand by registry/index comparison.
3. **Sequencing/Builder cluster:** QA-07, QA-10, QA-13, QA-16, QA-17, QA-20a, QA-21a, QA-76.
4. **Path/Stats/Policy cluster:** QA-08, QA-14, QA-42, QA-101, QA-102, QA-132/143 where still open.
5. **Source-integrity/SSOT maintenance:** QA-30, QA-40, QA-85/86, QA-141/142/151/160.
6. **Deferred/future confirmation batch.**

## Next workstep

Evidence-sweep the immediate Core Interaction blocker cluster, beginning with QA-02/QA-11 because it directly overlaps the already-confirmed ResolutionContext contract mismatch. Save a dedicated checkpoint before proceeding to QA-100/QA-138/QA-73.
