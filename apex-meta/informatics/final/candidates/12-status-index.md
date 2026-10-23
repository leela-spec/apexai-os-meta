---
type: Reference
id: V2-STATUS-INDEX-v1.0
title: Status Index — Every Finding, Decision, Question and Defect (Updated Post-ResearchOfFile10)
description: Single coverage view of every tracked item across DeepReasoning, v2-always-on-architecture, ResearchOfFile10, and FinalizationDossier, with current status and owning document.
status: current
tags: [status, index, coverage, audit, v1.0]
---

# Status Index (`v1.0` — Post-`ResearchOfFile10`)

**Purpose: one place to verify nothing was lost.** Every finding, decision, research packet, open question, and defect raised across this project, with its current status and the document that owns it.

- **Start at [FinalizationDossier/index.md](FinalizationDossier/index.md)** to click through the step-by-step file-by-file verification and patch dossier (`Steps 0` through `6`).

---

## 1. Needs operator action at system-integration time

| Item | What | Status |
|---|---|---|
| **`RBL-07`** | **Plaintext password and API token for OpenProject in `apex-meta/AI-Snippets/Orga/2Dos.md` lines 109–111 (tracked) and `2Dos Ai Instructions.md` (untracked).** Redacted in working files; because the tracked file was previously pushed to `origin/main`, the credentials remain in remote git history until rotated in OpenProject. | 🟡 **Redacted in workspace — Rotate credential in OpenProject** |
| **`D10`** | `GEMINI.md` is missing the `## Informatics & Knowledge Routing` section in the live root. Resolved in the `v1.0` Blueprint ([03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md)) and Surface Architecture ([11-instruction-surface-architecture.md](11-instruction-surface-architecture.md)) for the upcoming system-integration step. | 🟢 **Blueprint & test ready for system integration** |

---

## 2. Defects (`D1`–`D10`)

| ID | Defect | Status | Owner document |
|---|---|---|---|
| `D1` | Duplicate durable ID `FA-04` | ✅ Fixed → `FA-13` | [DeepReasoning/M03](../DeepReasoning/modules/M03-file-architecture.md) |
| `D2` | Frontmatter contracts contradicted between `FA` and `GS` | ✅ Fixed | [DeepReasoning/M03](../DeepReasoning/modules/M03-file-architecture.md) |
| `D3` | Root `index.md` violated the `tags` contract it published | ✅ Fixed | [DeepReasoning/M01](../DeepReasoning/modules/M01-routers-and-index.md) |
| `D4` | Bundle topology tree stale — omitted 4 live files and `tests/` | ✅ Fixed | [DeepReasoning/M03](../DeepReasoning/modules/M03-file-architecture.md) |
| `D5` | Sentence-length target vs advisory gate unreconciled | ✅ Fixed | [DeepReasoning/M02](../DeepReasoning/modules/M02-writing-profile.md) §3 |
| `D6` | `GS-04` and `GS-18` stated the same rule in one file | ✅ Fixed | [DeepReasoning/M06](../DeepReasoning/modules/M06-governance-schemas.md) |
| `D7` | `standard.md` vs modular suite dual authority | ✅ Fixed via precedence ladder | [DeepReasoning/M01](../DeepReasoning/modules/M01-routers-and-index.md) |
| `D8` | `estimate_tokens` duplicated across two test files | ⚪ **Declined** (`AD-25` / `AD-13`) | [DeepReasoning/M06](../DeepReasoning/modules/M06-governance-schemas.md) §7 |
| `D9` | Inline `patch_intent.v1` schema had drifted from authoritative JSON | ✅ Fixed | [DeepReasoning/01](../DeepReasoning/01-system-wide-overlap-and-token-audit.md) §4 |
| `D10` | `GEMINI.md` missing informatics routing | 🟢 **Spec & Blueprint finalized** (applies at system integration) | [11-instruction-surface-architecture.md](11-instruction-surface-architecture.md) §1 |

---

## 3. Decisions (`DEC-01`–`DEC-24`)

### Applied to the live modular suite (`apex-meta/informatics/*.md`)
- `DEC-01`…`DEC-09` — Canonical ownership, frontmatter ownership, schema registry, `FA-13` renumbering, precedence ladder, `WP-23`/`24`/`25`.
- **`DEC-24` (Library Synchronization from `ResearchOfFile10`):**
  - `WP-04` updated with **Insights Discovery Cool Blue** analytical register and warranted-uncertainty distinction (`RP-04`).
  - `AD-01` & `AD-02` updated with positive requirement-by-requirement final validation and FixedBench no-op legitimacy (`RP-05`, `RP-07`).
  - `AD-10` & `AD-25` updated with pre-action blocker requirement (`RP-07`).
  - `AD-22` added to codify `<hold_position>` (anti-sycophancy and narrow-correction discipline) in the canonical library (`08-discussion-and-open-threads.md` §5).

### Finalized `v1.0` Architecture Decisions (Ready for System Integration)

| ID | Decision | Status | Owner |
|---|---|---|---|
| `DEC-12` | Universal invariants move into an always-on contract in two steps (Step 1 install first; Step 2 dedup after burn-in) | ✅ **Finalized for Step 1** | [01-decision-register.md](01-decision-register.md) Part C |
| `DEC-13` | Reduced-form rules in the contract, not bare pointers | ✅ **Finalized** | [13-candidate-3A-xml.md](13-candidate-3A-xml.md) & [14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md) |
| `DEC-14` | `index.md` becomes a bundle index upon Step 1 installation | ✅ **Finalized** | [01-decision-register.md](01-decision-register.md) Part C |
| `DEC-15` | `general-informatics-router.md` remains the ultra-lean portable router (`<500` tokens), while `13`/`14` own the full portable contract | ✅ **Finalized** | [FinalizationDossier/03-root-index-and-router-audit.md](FinalizationDossier/03-root-index-and-router-audit.md) |
| `DEC-16` | Conditional branches cross a file boundary (`execution-modes.md` per-adapter split) | 🟡 **Gated on Read-Trace Protocol ([04](04-empirical-test-protocol.md))** | [01-decision-register.md](01-decision-register.md) Part C |
| `DEC-17` | Named XML tags per rule (`3A`) vs. Hybrid XML + Conditional Table (`3B`) | ✅ **Both finalized (`13` & `14`) for head-to-head read-trace test (`Option 6C`)** | [13-candidate-3A-xml.md](13-candidate-3A-xml.md), [14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md) |
| `DEC-21` | Canonical owner `AGENTS.md` + byte-identical `<apex_contract>` blocks in `CLAUDE.md` & `GEMINI.md` enforced by `pytest` | ✅ **Verified & Finalized (`RP-10`)** | [11-instruction-surface-architecture.md](11-instruction-surface-architecture.md) |
| `DEC-22` | Two-Layer Separation: Layer 1 (`<apex_contract v="1.0" base_ref="apex-meta/informatics/">`) + Layer 2 (Repo-Specific sections outside XML) | ✅ **Finalized (`Option 2A` + `5A`)** | [03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md), [11-instruction-surface-architecture.md](11-instruction-surface-architecture.md) |
| `DEC-23` | Drop `deepen_when=` (-99 tokens across 5 tags, `RP-08`) and reject arbitrary 1,000-token wall under prompt caching (`RP-09`) | ✅ **Finalized** | [01-decision-register.md](01-decision-register.md) Part H |
| `DEC-24` | Empirical wording upgrades integrated into `<target>` (`RP-05`/`07`), `<communication>` (`RP-04`), and `<new_machinery>` (`RP-07`) | ✅ **Finalized & Applied** | [13-candidate-3A-xml.md](13-candidate-3A-xml.md), [14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md) |

---

## 4. Research Packets (`RP-01`–`RP-10`) — **10/10 COMPLETE**

Executed in [ResearchOfFile10/](ResearchOfFile10/RESULTS-11-synthesis.md) and critically audited in [FinalizationDossier/00-research-critique-and-architecture-design.md](FinalizationDossier/00-research-critique-and-architecture-design.md).

| ID | Question | Result File | Verdict & Integration Status |
|---|---|---|---|
| `RP-01` | Does conditional gating actually work? | [RESULTS-01](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md) | ✅ **Complete** — Model-interpreted text, not parser-enforced; test via [04-empirical-test-protocol.md](04-empirical-test-protocol.md). |
| `RP-02` | Could vector retrieval replace static dispatch? | [RESULTS-02](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-02-vector-retrieval.md) | ✅ **Complete** — Rejected for mandatory invariants; always-on core + progressive disclosure wins. |
| `RP-03` | What is this reasoning missing or stale about? | [RESULTS-03](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-03-currency-check.md) | ✅ **Complete** — 1,000-token wall unsupported; 3-tier architecture sound. |
| `RP-04` | The communication register term | [RESULTS-04](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md) | ✅ **Complete & Integrated** — **Insights Discovery Cool Blue** + warranted uncertainty vs. empty hedges. |
| `RP-05` | Stopping self-authored acceptance criteria | [RESULTS-05](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md) | ✅ **Complete & Integrated** — Positive requirement-by-requirement final validation check (*SpecBench*). |
| `RP-06` | Full serialization comparison (XML vs. bullets vs. table) | [RESULTS-06](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-06-condition-syntax.md) | ✅ **Complete & Integrated** — Rendered both `3A` ([13](13-candidate-3A-xml.md)) and `3B` ([14](14-candidate-3B-hybrid.md)). |
| `RP-07` | What reduces over-building | [RESULTS-07](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md) | ✅ **Complete & Integrated** — *FixedBench* no-op legitimacy + pre-action blocker requirement. |
| `RP-08` | How `deepen_when` actually works | [RESULTS-08](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md) | ✅ **Complete & Integrated** — Dropped all 5 `deepen_when=` attributes (-99 tokens). |
| `RP-09` | Every remaining efficiency lever & caching | [RESULTS-09](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md) | ✅ **Complete & Integrated** — Prompt caching reframes cost; `base_ref` factoring applied. |
| `RP-10` | Tool loader matrix & Universal vs. Repo layering | [RESULTS-10](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md) | ✅ **Complete & Integrated** — 2-Layer Blueprint ([03](03-BLUEPRINT-agents.md)) & Surface Architecture ([11](11-instruction-surface-architecture.md)) finalized. |
| **Synth** | Cross-packet synthesis | [RESULTS-11](ResearchOfFile10/RESULTS-11-synthesis.md) | ✅ **Complete & Audited** in [FinalizationDossier/00](FinalizationDossier/00-research-critique-and-architecture-design.md). |
