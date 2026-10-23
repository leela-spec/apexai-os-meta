---
okf_version: "0.2"
type: Plan
id: V2-FINAL-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS
title: QMD & Informatics Integration Plan and Operational Decision Ledger (Windows Native Workstation)
description: Authoritative implementation plan and operational decision record governing the integration of 16-candidate-3A-ultra, 06-layered-rule-kb, and QMD execution on the Windows native workstation.
status: current
tags: [integration-plan, operational-decisions, qmd, 16-ultra, layered-kb, windows-native]
---

# QMD & Informatics Integration Plan & Operational Decision Ledger

> **Location:** `apex-meta/informatics/final/07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md`  
> **Complements:** [index.md](index.md), [06-EXECUTION-PLAN-AND-THINKING-PROCESS.md](06-EXECUTION-PLAN-AND-THINKING-PROCESS.md), [candidates/16-candidate-3A-ultra.md](candidates/16-candidate-3A-ultra.md), and [research/06-layered-rule-kb/index.md](research/06-layered-rule-kb/index.md).

---

## 1. Context & Windows Native Workstation Environment

This plan governs operations strictly on this **Windows Native Workstation**:

- **Host Filesystem:** Windows 11 host (`c:\GitDev\apexai-os-meta`).
- **Indexing Scope:** Scoped exclusively to [`apex-meta/informatics/final/`](index.md) under the collection `apex-informatics-final` (152 markdown files, 961 vector chunks).
- **Execution Model:** Direct CLI tool invocation (`qmd search`, `qmd get`, `qmd query`).
- **Daemon Prohibition:** Background daemons (`--daemon`) are strictly prohibited due to Windows process tracking constraints in the upstream runtime.
- **Hardware Acceleration:** Local GGUFs cached at `C:\Users\gehma\.cache\qmd\models\` running via Intel Arc 140V Vulkan / CPU.

---

## 2. Canonical Operational Decisions (The Decision Register)

| Decision ID | Operational Domain | Formal Decision | Empirical Grounding & Source |
|---|---|---|---|
| **DEC-QMD-01** | **Search Speed Policy** | **Two-Tier Escalation:** Agents MUST run `qmd search` (FTS5 BM25) first. Escalation to `qmd query` (hybrid AI reranking) is authorized ONLY when keyword search yields zero results. | Measured latency: `qmd search` executes in **0.32 seconds**; `qmd query` takes **19 to 44 seconds** (130x latency differential). `RESULTS-09`. |
| **DEC-QMD-02** | **Windows Daemon Policy** | **Direct CLI Execution Only:** On Windows, all agents MUST invoke `qmd` via direct terminal commands. Running `qmd mcp --daemon` or `--http --daemon` is banned. | Audit of `@tobilu/qmd/dist/cli/mcp-pid.js`: relies on Unix process inspection, causing orphaned zombie processes on Windows. |
| **DEC-QMD-03** | **Index Scope Bounding** | **Final-Only Workstation Bounding:** The local QMD collection (`apex-informatics-final`) indexes only `apex-meta/informatics/final/**.md`. | `FA-03` [Five-Plane Separation], `AD-04` [Context Hygiene]. Keeps the index tightly focused on active specs and research. |
| **DEC-QMD-04** | **Surgical Slicing Discipline** | **Mandatory Slice Fetching:** Agents MUST use `qmd get "#docid:from:count"` or `qmd get path:line:count` to pull 20–40 line windows. Bulk whole-file reads are forbidden. | `AD-04`, `AD-19`. Consumes <10% of full-file token budgets; prevents LLM cognitive overload and attention drift. |
| **DEC-QMD-05** | **Structured Query Document Authoring** | **Negative Space Intent Formulation:** When `qmd query` is required, agents MUST supply typed query documents (`intent:` + `lex:` + `vec:`) to bypass the 11.8s expansion phase. | Prevents Tobias Lütke 1.7B expansion model from drifting on specialized research terms. Cuts query latency by 57%. |
| **DEC-QMD-06** | **Index Refresh Cadence** | **On-Demand & Git Hook Sync:** Re-indexing is triggered on-demand via `qmd update` when documentation changes. Unchanged files are skipped via SHA-256 content hashing. | Incremental hashing takes <2 seconds when no files have changed. |

---

## 3. The 3-Layer Integration Architecture

The integration of candidate specifications into live agent operating surfaces is structured across three distinct layers:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ LAYER 0: ALWAYS-ON CORE CONTRACT (Carried in Memory)                        │
│ • Source: candidates/16-candidate-3A-ultra.md (1,225 BPE / 1,479 repo tkns)│
│ • Carried by: AGENTS.md, CLAUDE.md, GEMINI.md (Byte-Identical Layer 1)     │
│ • Contents: 22 XML semantic tags (<target> through <pointers>)              │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼ ref pointers
┌─────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: RULE-BY-RULE RATIONALE LEDGER (Searchable via QMD)                 │
│ • Source: research/06-layered-rule-kb/ (index.md + rule-01 to rule-22)      │
│ • Contents: Atomic blocks (SB-XX.k), Option A/B/C, default RLHF audits,     │
│   and empirical benchmark citations (SpecBench, FixedBench, Cool Blue)      │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼ ref pointers
┌─────────────────────────────────────────────────────────────────────────────┐
│ LAYER 2: CANONICAL PLANE 4 DEEP SPECS (Loaded Just-In-Time)                 │
│ • writing-profile.md (WP-01..25)         • anti-drift-rules.md (AD-01..28)  │
│ • execution-modes.md (EM-01..12)         • governance-schemas.md (GS-01..22)│
│ • file-architecture.md (FA-01..13)       • general-informatics-router.md    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. QMD Agent Skill Structure (`.agents/skills/qmd/`)

In conformance with the **Apex Informatics Standard (`STD-APEX-INFORMATICS-v0.2`)**, the QMD agent skill directory is organized into a primary entrypoint and dedicated reference modules:

```text
.agents/skills/qmd/
├── SKILL.md                          <- Primary Task-Triggered Entrypoint (RFC 2119 / STE)
└── references/
    ├── search-speed-protocol.md      <- Two-tier speed escalation rules (0.32s vs 44s)
    ├── runtime-topology-windows.md   <- Windows CLI constraints & daemon prohibition
    ├── structured-query-craft.md     <- Intent, lex, vec, hyde authoring grammar
    └── benchmarks-and-fixtures.md    <- Quality assurance fixtures and qmd bench specs
```

---

## 5. Execution Roadmap & Verification Gates

1. **Gate 1: Skill Structure (`.agents/skills/qmd/`)**
   - Author `SKILL.md` mandating `DEC-QMD-01` through `DEC-QMD-06`.
   - Maintain supporting reference modules under `.agents/skills/qmd/references/`.
2. **Gate 2: Carrier File Blueprint Rollout**
   - Integrate `16-candidate-3A-ultra.md` into `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` following [03-BLUEPRINT-agents.md](candidates/03-BLUEPRINT-agents.md).
   - Update `test_m5_challenger_verification.py` from `test_carrier_immutability` to `test_carrier_byte_identity`.
   - Verify all 338+ pytest checks pass.

---

## 6. Cross-Environment Boundary & External Harness Flag (OpenProject WP #198)

> **⚠️ ARCHITECTURAL BOUNDARY FLAG (DO NOT TOUCH UNLESS OPERATING IN LINUX HARNESS):**  
> This repository (`apexai-os-meta`) is accessed by two distinct operating environments:
> 1. **This Environment (Windows Native Workstation):** Runs directly on the Windows 11 host (`c:\GitDev\apexai-os-meta`). Uses native Windows Node/Python and local QMD (`apex-informatics-final`). **Windows workstation agents MUST NOT touch, invoke, or re-introduce the `ki-basis` WSL2/Docker infrastructure.**
> 2. **The External Server Harness (`ki-basis` / CORTEX_PB Linux Stack):** Runs inside WSL2 Linux Docker with shared PostgreSQL. Tracked exclusively in **OpenProject Work Package #198** (`http://127.0.0.1:8083/work_packages/198`).
>
> **Deletion Record & Cross-Environment Invariant:**
> - The legacy `ki-basis/docs/INFRASTRUCTURE.md` banner and the Linux `/mnt/c` 9p bridge rule were permanently deleted from the Windows workstation carrier blueprint ([candidates/03-BLUEPRINT-agents.md](candidates/03-BLUEPRINT-agents.md)) to prevent cross-environment drift.
> - **Warning for Linux Agents:** When implementing OpenProject WP #198 in the Linux harness, agents must ensure they do not run in `/mnt/c` (which causes unkillable D-state locks) and maintain their local stack pointers inside Linux-specific configurations—**without re-contaminating the Windows workstation carrier files**.

---

## 7. Operational 2DO: Test Suite Audit & Anti-Fake-Verification Review

- [ ] **Action Item:** Audit the 338 tests currently in `apex-meta/informatics/tests/` during the relocation to `final/verification/`.
- [ ] **Pruning Target:** Identify and prune over-engineered mechanical checks (arbitrary sentence word length limits, hyper-tight character ceilings) that cause unnecessary prose shaving.
- [ ] **Truth Verification:** Ensure all retained tests verify genuine, durable system invariants (broken relative links, duplicate rule IDs, carrier immutability, context isolation) rather than self-verifying AI tautologies or fake green lights.
- [ ] **Knowledge Base Governance:** Build the Test Knowledge Base (`final/verification/test-kb/`), requiring explicit justification documents for tests, strictly enforcing `<target>` and `<new_machinery>`.
