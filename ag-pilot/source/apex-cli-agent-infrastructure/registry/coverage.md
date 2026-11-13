---
type: Reference
id: APEX-INFRA-REGISTRY-COVERAGE
title: Current rule coverage and activation design
description: Coverage boundary, source fidelity, conflicts and registry interpretation.
status: draft
tags: [apex, registry, proposal, validation]
---

# Current rule coverage

The registry contains **23 current XML tags**, **100 source-owned downstream rules**, and **22 scoped authority/host clauses**. All activation architecture is **proposed and uninstalled**. The current source revision is `6c93ad31e42a72de74119218b9365bdd9d6ee386`.

| Source family | Rules |
|---|---:|
| AD | 28 |
| EM | 15 |
| FA | 13 |
| GS | 19 |
| WP | 25 |


## Current XML review map

This is navigation into [rules.json](rules.json), not a second rule definition. The XML text remains the source owner.

| Current tag | Activation profile | Detailed rule references | Trigger boundary |
|---|---|---|---|
| `align` | alignment | `EM-13` | Nontrivial new unapproved task |
| `authoring` | authoring | `WP-09`, `FA-05`, `FA-06`, `FA-13`, `WP-07` | Governed knowledge/spec file create/edit/validate |
| `communication` | invariant | `WP-02`, `WP-03`, `WP-05`, `WP-12` | Communicating result, blocker or decision |
| `context` | context | `EM-03`, `EM-10` | Research or multi-stage work |
| `current_truth` | authoring | `FA-01`, `AD-15` | Changing current operating meaning |
| `detour` | invariant | `AD-05`, `AD-10` | Before refactor/redesign/migration/infrastructure expansion |
| `editing` | patch | `EM-08`, `AD-23` | Existing-file change, move or deletion |
| `ground` | grounding | `AD-19`, `AD-20`, `EM-02` | Factual/design/version/count claim |
| `handover` | handoff | `EM-09`, `EM-14` | Major step/session closure or delegation |
| `hold_position` | invariant | `AD-22` | Receiving pushback or narrow correction |
| `iterative` | context | `EM-10`, `EM-11`, `EM-13` | Multi-module/research/multi-pass task |
| `new_machinery` | invariant | `AD-13`, `AD-25` | Before adding script/test/gate/schema/wrapper |
| `pointers` | invariant | `EM-13`, `WP-18` | Any matched conditional ref before action/final output |
| `product_first` | invariant | `AD-09`, `AD-10`, `AD-12` | Choosing work before usable product exists |
| `recovery` | invariant | `AD-16`, `AD-21` | Incidental failure |
| `reuse` | invariant | `AD-11`, `AD-14`, `WP-23` | Before building |
| `schemas` | schema | `GS-01`, `GS-09`, `GS-10`, `GS-11` | Patch intent or bundle/schema validation |
| `scope` | invariant | `AD-18` | Selecting or expanding an action |
| `stop_repairing` | invariant | `AD-02`, `AD-07`, `AD-24` | Two non-advancing repairs in same subsystem |
| `surgical` | patch | `EM-01`, `EM-08` | Existing-file mutation |
| `sync` | sync | `EM-12` | Explicit operator sync/commit/push request |
| `target` | invariant | `AD-01`, `AD-09`, `AD-12` | Each action and completion claim |
| `trade_off` | comparison | `EM-06`, `EM-06a`, `EM-07` | Material choice or requested options/ranking |

## Meaning and ownership

- [rules.json](rules.json) indexes the existing semantic owners. It does not replace the XML, modular specifications, or native permissions.
- `source.quote` preserves inspected source text and refreshed inclusive 1-based lines. Source hashes identify inspected bytes.
- `source_priority` preserves authored P0–P3 and raw I/E/R. Missing XML/scoped-clause ratings stay null. Historical reading order is not reliability.
- `canonical_owner` follows explicit source delegation markers; `definition_role` distinguishes reduced-contract, canonical and delegated views.
- Each rule binds a lifecycle profile plus its own trigger, exclusions, dependencies and observable check. `activation.delivery_plan` separates mandatory matched XML refs from conditional detail reads; a list of available references is not a bulk-read instruction. Shared profiles avoid copying the same mechanism prose into independent definitions.
- Formal writing profile applies to governed artifacts; chat-only recommendation content uses Q&A rules without forcing frontmatter or STE on ordinary answers.

## Coverage boundary

The 100 downstream IDs include all 25 WP, 13 FA, 28 AD, 19 active GS, and 15 EM (EM-01–14 plus EM-06a) declarations in the inspected owners. Detailed adapter source spans retain their meaningful subrequirements: six task fields, approved-step criteria, Q&A components and L0–L3 scaling, unique exact-match safety, four-dimensional delegation, step close-out, Route0/1/2 and recovery. Retired GS-16/18/19 remain only in history.

Additional rules inside unrelated subsystem/domain skills are not claimed as a universal complete corpus. This registry covers the current XML and its relevant modular detail owners, plus authority/host clauses that materially constrain delivery. The scoped rows additionally capture the project router, orchestration roles and gates, Weekly isolation/mutation, backbone separation, AIRouting boundary and current QMD policy. The architecture package expands their integration implications.

## Source and runtime conflicts

The machine-readable `conflicts` table records eleven consequential reconciliations: authorization/confirmation, close-out pushes, silence-as-acceptance, weighted comparisons versus raw I/E/R, named-file push versus full sync, stale links, approximate directive ceilings, historical index role, QMD owner/projection drift, and intent-driven procedure selection versus unsolicited activation, and the duplicate current EM-12 owner occurrence. These are not silently installed amendments. EM-12 currently appears in both the general execution-modes file and standalone `execution-modes/git-sync.md`; selecting the existing standalone adapter as the delivery owner is a disclosed proposal, not proof of applied deduplication.

Authenticated reads returned 404 for `apex-meta/informatics/standard.md`, `apex-meta/informatics/final/specs/index.md` and `apex-meta/informatics/final/specs/migration.md`. Accessible resolved owners are `apex-meta/informatics/final/specs/standard.md`, `apex-meta/informatics/final/index.md` and `apex-meta/informatics/final/operations/migration.md`. The patch-intent schema was opened at `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json`; the links in `execution-modes/patch-discipline.md` resolve to the wrong locations. The corresponding `governance-schemas.md` link resolves correctly and is retained. These source defects do not authorize live fixes in this run.

## Historical traceability

[history.json](history.json) preserves the 22-rule historical roster and the later 23rd align row. The current tag roster is extracted from XML, never inferred from the old count. Recorded candidate statuses, withdrawals, corrections, falsification conditions and operator-named-tag decision remain evidence. The history also preserves the C01–C12 ledger, all its authored option priorities/raw I/E/R, and the finalization decision/backlog dispositions. C12 has an original P1-versus-P0 discrepancy; both source values are retained. The older C03 task-field proposal is explicitly distinguished from current EM-13. Candidate token counts are not current runtime measurements. Carrier decisions must be reconciled with later carrier-map evidence and versioned loader behavior before adoption.

## Executed validation

[validation.json](validation.json) reports the local JSON Schema check, duplicate-ID check, dependency/owner existence, exact source-quote recheck and XML identity coverage. Dependencies express co-applicable rule references, not a hard execution-order DAG. `source.quote` is frozen evidence for review, never a second normative owner. Reproduce from the package's validation tooling against the bundled registry; the construction script is scratch working material and is not required for runtime adoption. These structural checks do not prove skill selection, hook execution, source comprehension or useful outcomes. All such runtime evaluation remains explicitly unexecuted unless separately evidenced.

## Failure guard

Never treat a proposed activation row, a read receipt, a historical score, a source status label, or a schema pass as proof that the installed agent obeyed the rule. Verify applicability, reading, adherence and outcome separately.
