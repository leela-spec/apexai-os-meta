---
type: Reference
id: V2-STATUS-INDEX-v1.0
title: Status Index — Every Finding, Decision, Question and Defect
description: Single coverage view of every tracked item across both research folders, with its status and owning document, so nothing from the design conversation is left only in commit messages.
status: current
tags: [status, index, coverage, audit]
---

# Status Index

**Purpose: one place to verify nothing was lost.** Every finding, decision, open question and defect
raised across this project, with its current status and the document that owns it.

**Verified by ID sweep** across both research folders: defects `D1`–`D10`, decisions `DEC-01`–`DEC-21`
plus `DEC-M*`/`DEC-C*`/`DEC-W*`/`DEC-O*`, backlog `RBL-01`–`RBL-08`, research packets `RP-01`–`RP-10`.
No orphan IDs remain — the earlier `RQ-1`–`RQ-4` scheme was reconciled into `RP-04`–`RP-07`
(12 references updated), because two ID schemes for the same questions is the drift pattern this
project exists to prevent.

---

## 1. Needs operator action — nothing blocks these

| Item | What | Status |
|---|---|---|
| **`RBL-07`** | **Plaintext password and API token for OpenProject in a git-tracked file** — `apex-meta/AI-Snippets/Orga/2Dos Ai Instructions.md` lines 66-69. Outside this project's scope and never acted on. Requires **rotation**, not just deletion — git history retains it | 🔴 **Open, unaddressed** |
| **`D10`** | `GEMINI.md` is missing the entire `## Informatics & Knowledge Routing` section, so Gemini agents receive no informatics routing. Independent of the contract work | 🔴 **Open, fixable now** |

These two are the only items that need nothing from anyone else first.

---

## 2. Defects

| ID | Defect | Status | Owner document |
|---|---|---|---|
| `D1` | Duplicate durable ID `FA-04` | ✅ Fixed → `FA-13` | [DeepReasoning/M03](../DeepReasoning/modules/M03-file-architecture.md) |
| `D2` | Frontmatter contracts contradicted between `FA` and `GS` | ✅ Fixed | [DeepReasoning/M03](../DeepReasoning/modules/M03-file-architecture.md) |
| `D3` | Root `index.md` violated the `tags` contract it published | ✅ Fixed | [DeepReasoning/M01](../DeepReasoning/modules/M01-routers-and-index.md) |
| `D4` | Bundle topology tree stale — omitted 4 live files and `tests/` | ✅ Fixed | [DeepReasoning/M03](../DeepReasoning/modules/M03-file-architecture.md) |
| `D5` | Sentence-length target vs advisory gate unreconciled | ✅ Fixed; **register overstated the defect, corrected** | [DeepReasoning/M02](../DeepReasoning/modules/M02-writing-profile.md) §3 |
| `D6` | `GS-04` and `GS-18` stated the same rule in one file | ✅ Fixed | [DeepReasoning/M06](../DeepReasoning/modules/M06-governance-schemas.md) |
| `D7` | `standard.md` vs modular suite dual authority | ✅ Fixed via precedence ladder | [DeepReasoning/M01](../DeepReasoning/modules/M01-routers-and-index.md) |
| `D8` | `estimate_tokens` duplicated across two test files | ⚪ **Declined** — fixing it means adding a module to dedupe 4 lines; fails `AD-25` and `AD-13` | [DeepReasoning/M06](../DeepReasoning/modules/M06-governance-schemas.md) §7 |
| `D9` | Inline `patch_intent.v1` schema had drifted from the authoritative JSON, dropping every `maxLength` bound | ✅ Fixed — **the pass's highest-value item** | [DeepReasoning/01](../DeepReasoning/01-system-wide-overlap-and-token-audit.md) §4 |
| `D10` | `GEMINI.md` missing informatics routing | 🔴 **Open** | [11](11-instruction-surface-architecture.md) §1 |

---

## 3. Decisions

### Applied to the live suite

`DEC-01`…`DEC-09` — dedup granularity, frontmatter ownership, schema registry, `FA-04` renumbering,
precedence ladder, test-update policy, router untouched, `D8` declined, three new rules
(`WP-23`/`24`/`25`). All verified green: validator `0/0`, 196 tests.
→ [01-decision-register.md](01-decision-register.md) Part A

### Superseded, withdrawn, corrected — kept visible on purpose

| ID | Was | Now |
|---|---|---|
| `DEC-10` | "Modules must restate universal invariants to stay self-sufficient" | **Superseded.** Live artifact: 23 `Canonical:` markers in the five modules — accurate today, residue of old reasoning |
| `DEC-11` | One uniform `CROSS_LINK` policy for all duplicates | **Superseded** by the Rule of Three threshold; 8 of 13 concepts qualify for extraction |
| `DEC-W1` | "Audit the 3,031-token always-on tier" | **Withdrawn** — those files are placeholders this work feeds |
| `DEC-W2` | "Decide whether `index.md` is a guaranteed kernel" | **Withdrawn** — it is not the router |
| `DEC-C1` | "The named-tag design is the operator's own" | **Corrected** — unverified appeal to authority; it is a likely AI-drafted repo candidate |
| `DEC-C2` | "Named tags cost ~150 tokens" | **Corrected** — measured at 17 tokens; the growth was new content, not formatting |

→ [01-decision-register.md](01-decision-register.md) Part B

### Architecture — proposed, not applied

| ID | Decision | Status |
|---|---|---|
| `DEC-12` | Universal invariants move into an always-on contract, in two steps | Proposed |
| `DEC-13` | Reduced-form rules in the contract, not bare pointers | Proposed |
| `DEC-14` | `index.md` becomes a bundle index only | Proposed |
| `DEC-15` | Router becomes a labelled portable artifact | Proposed |
| `DEC-16` | **Conditional branches must cross a file boundary** — splitting `execution-modes.md` cuts a patch task 4,208 → 713 | Proposed, operator-endorsed, pending test |
| `DEC-17` | **Named tags per rule** | ✅ **Decided** (operator, clarity; 17-token cost). Confirmation test queued |
| `DEC-21` | **Contract goes to all shared-rule surfaces**; owner `AGENTS.md`, byte-identical carriers, enforced by test | ✅ **Resolved** — but turns on unverified facts, see `RP-10` |

### Mechanical facts — not opinions

`DEC-M1` an IF-clause inside a loaded file saves zero tokens · `DEC-M2` gates buy precision and
prevent downstream reads · `DEC-M3` a branch saves tokens only across a file boundary ·
`DEC-M4` a functional reduced form fits in ~721 tokens · `DEC-M5` a worked example is not duplication ·
`DEC-M6` the validator is blind to in-body rule IDs
→ [01-decision-register.md](01-decision-register.md) Part D

---

## 4. Open operator decisions

| ID | Question | Status |
|---|---|---|
| `DEC-O1` | Install the contract into the surfaces (Step 1)? | 🟡 Open — after the research |
| `DEC-O2` | Step 2 — delete the 8 restatements from modules? | 🟡 Open — after Step 1 runs |
| `DEC-O3` | Split `execution-modes.md` per adapter? | 🟡 Open — gated on `RP-01`/`DEC-20` |
| `DEC-O4` | Research before or after the empirical test? | ✅ Resolved — research first, handover dispatched |
| `DEC-O5` | Is the reduced-form wording acceptable? | 🟡 Open on v0.5 — v0.4 feedback incorporated |
| `DEC-O6` | Does existing `AGENTS.md` content merge or stay? | ✅ Resolved — per-section merge map in [03](03-BLUEPRINT-agents.md) §1 |
| **New** | **Keep `deepen_when`?** 99 tokens across six rules | 🟡 Open — gated on `RP-08` |
| **New** | **Build the byte-identity test before creating copies** | 🟡 Open — sequencing requirement, not a preference |

---

## 5. Research — dispatched

Ten packets, handover ready at [10-RESEARCH-EXECUTION-HANDOVER.md](10-RESEARCH-EXECUTION-HANDOVER.md).

| ID | Question | Decides |
|---|---|---|
| `RP-01` | Does conditional gating actually work? | Every `when=` in the design |
| `RP-02` | Could vector retrieval replace static dispatch? | The architecture itself |
| `RP-03` | What is this reasoning missing or stale about? | Seven stated claims |
| `RP-04` | The communication register term | `<communication>` wording |
| `RP-05` | Stopping self-authored acceptance criteria | `<target>` wording |
| `RP-06` | Full serialization comparison — XML / bullets / table / other | `DEC-17` final form, ~190 tokens |
| `RP-07` | What reduces over-building | `<new_machinery>`, `DEC-20` |
| `RP-08` | How `deepen_when` actually works | 99 tokens |
| `RP-09` | Every remaining efficiency lever; is ~1,000 reachable? | The floor claim |
| `RP-10` | Which agent reads which file; universal vs repo-specific layering | `DEC-21`, portability |

## 6. Research — backlog, not dispatched

| ID | Question | Status |
|---|---|---|
| `RBL-01` | Does single-gate JIT isolation hold in production routing? | Open — underpins the whole dedup policy |
| `RBL-02` | Are the plane token orientations calibrated to current practice? | Open |
| `RBL-03` | Root-surface consolidation of `WP-02`/`03`/`05` | Open — relocated from a live spec |
| `RBL-04` | Empirical directive ceiling per file | Open |
| `RBL-05` | Absolute `file:///` URLs | ✅ Fixed in the four governed files; validator enforcement still open |
| `RBL-06` | Promote rule-ID uniqueness into `okf_validator.py` | Partially closed by a pytest guard; repo-wide promotion open |
| `RBL-07` | **Plaintext credentials in a tracked file** | 🔴 **Open — see §1** |
| `RBL-08` | A spec-vs-upstream-artifact consistency gate | Deferred under `AD-25` until a second instance appears |

→ [DeepReasoning/03-research-backlog-and-open-questions.md](../DeepReasoning/03-research-backlog-and-open-questions.md)

---

## 7. Test queue

| ID | Item | Vehicle |
|---|---|---|
| `DEC-17` | Named tags — confirmation only | Arm E |
| `DEC-18` | The 18-token `<surgical>` stub | Arm F |
| `DEC-19` | `<stop_repairing>` placement | Arm G |
| `DEC-20` | `<new_machinery>` + `<detour>` as the drift replacement | Arm H |

→ [04-empirical-test-protocol.md](04-empirical-test-protocol.md), arms A–H, fixtures T1–T14.
**Designed, not run.**

---

## 8. Known gaps in this index

Stated so the index does not itself become a false completeness claim:

- **Nothing here is applied** except the `DeepReasoning` pass (commit `f925be40`). Every `v2` item
  is a candidate, a proposal, or a question.
- **The empirical test has not run.** Four decisions depend on it.
- **No research has been executed.** Ten packets are written and dispatched, zero returned.
- **`DEC-21` rests on unverified facts** about which tool reads which file. `RP-10` Part 1 settles it
  and could cancel the byte-identity test entirely.
- **The contract wording is still mine**, not the operator's, in every version.
