---
type: Reference
id: V2-BLUEPRINT-AGENTS-v1.0
title: BLUEPRINT — AGENTS.md With The Finalized v1.0 Contract Block Integrated
description: Non-active blueprint of AGENTS.md showing the two-layer v1.0 integration (Layer 1 Portable Contract + Layer 2 Repo-Specific Operating Context), line-by-line merge map, and updated token budget.
status: candidate_not_active
tags: [blueprint, agents-md, merge-map, non-active, v1.0, two-layer]
---

# BLUEPRINT — `AGENTS.md` With The Finalized `v1.0` / `v1.0-ultra` Contract Block Integrated

> ## ⚠️ THIS IS A NON-ACTIVE BLUEPRINT FOR LATER SYSTEM INTEGRATION
>
> This is a **blueprint** showing how [`AGENTS.md`](../../../AGENTS.md) (and its byte-identical carrier sections in [`CLAUDE.md`](../../../CLAUDE.md) and [`GEMINI.md`](../../../GEMINI.md)) will look when the finalized `v1.0` / `v1.0-ultra` contract is introduced into the live system.
>
> - The **real** `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` remain untouched during this staging phase (enforced by `test_carrier_immutability`).
> - **Updated to `v1.0-ultra` ([16-candidate-3A-ultra.md](16-candidate-3A-ultra.md) / [13-candidate-3A-xml.md](13-candidate-3A-xml.md)):**
>   1. Incorporates the finalized 22-rule Option B compressed XML block (1,225 BPE / 1,479 repo tokens).
>   2. Applies the `Git Dispatch` deduplication decided in `09-contract-block-v0.5.md` §1 (`<sync>` owns general git behavior; Layer 2 keeps only the 45-token repo-specific WSL2 ext4 / `/mnt/c` constraint, saving 140 tokens).
>   3. Explicitly separates **Layer 1 (Portable Universal Contract)** from **Layer 2 (Repository-Specific Operating Context)** per `RP-10`.
>   4. Integrates the **QMD Knowledge Retrieval & Evidence Tooling lens** into Layer 2B (`DEC-QMD-01` two-tier speed protocol, `DEC-QMD-04` surgical slicing), grounding `<ground>` and `<context>` without inflating Layer 1.

---

## 1. Two-Layer Merge Map — What Happens to Each Existing Section of `AGENTS.md`

The real `AGENTS.md` is 50 lines / ~998 tokens across six sections. Measured `v1.0` disposition:

| Existing Section | ~Tokens | Overlaps Contract | `v1.0-ultra` Disposition |
|---|---:|---|---|
| **Infrastructure Banner** | 215 | none | **Eliminate from Workstation Carrier.** The ki-basis WSL2/Docker stack is an isolated background harness tracked under OpenProject WP #198 and governed by [07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md](../07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md) §6. Windows agents must not reintroduce this banner. |
| **Git Dispatch** (7 rules) | 185 | 6 of 7 rules covered by `<sync>` | **Deduplicate.** General git sequence, rebase, and file-preservation live once in `<sync>`. Retired WSL2 `/mnt/c` warning removed for Windows host. |
| **Directness** (5 rules) | 115 | `<scope>`, `<target>`, `<sync>` | **Replace** with Layer 1 contract. |
| **Core Intent Execution** (10 rules) | 240 | `<target>`, `<scope>`, `<current_truth>`, `<recovery>`, `<trade_off>` | **Replace** with Layer 1 contract. |
| **Informatics & Knowledge Routing** (2 rules) | 85 | `<authoring>`, `<schemas>`, `base_ref="apex-meta/informatics/"` | **Replace** with Layer 1 contract (and fixes `D10` in `GEMINI.md` upon installation). |
| **Scope** (3 rules) | 70 | `<scope>` | **Replace** with Layer 1 contract. |
| **Final Rule** ("never describe a proposed block as applied") | 35 | Sharpens `<ground>` / `<target>` | **Keep verbatim in Layer 2 (`## Completion Reporting`).** |

### Net Token & Caching Economics (`RP-09` Verified)

| Component | `v0.5` Legacy Blueprint | `v1.0-ultra` (Windows Native Workstation) |
|---|---:|---:|
| **Layer 2 Windows Context** (Host Env `20` + QMD Retrieval `38` + Completion Rule `35`) | 295 *(had WSL2 banner & ext4)* | **~93 BPE (~115 repo tkns)** |
| **Layer 1 Contract Block** (`<apex_contract ... base_ref="apex-meta/informatics/">`) | 1,632 (1,350 BPE) | **1,225 BPE (1,479 repo tkns)** |
| **Total Always-On Surface** | ~1,600 BPE (~1,927 repo tkns) | **~1,318 BPE (~1,594 repo tkns)** |

> **Why ~1,318 BPE tokens (~1,594 repo tokens) is the optimal operational size (`RP-03` & `RP-09`):**
> Purging the legacy WSL2 infrastructure banner saves 215 tokens immediately. Combined with prefix caching and QMD surgical slicing, downstream multi-turn context overhead is reduced by over 80%.

---

## 2. The Complete Two-Layer Blueprint (`AGENTS.md` / `CLAUDE.md` / `GEMINI.md`)

Everything inside the block below is the exact structure prepared for future installation into `AGENTS.md` (with single-source owner [16-candidate-3A-ultra.md](16-candidate-3A-ultra.md) or [13-candidate-3A-xml.md](13-candidate-3A-xml.md) pasted at the marker):

```markdown
# Codex Operating Note

<!-- ===================================================================== -->
<!-- LAYER 1: PORTABLE UNIVERSAL AI OPERATING CONTRACT (v1.0-ultra)         -->
<!-- Canonical Owner: 16-candidate-3A-ultra.md                              -->
<!-- To port to another repository: copy <apex_contract>...</apex_contract>-->
<!-- verbatim and adjust only base_ref if the informatics path differs.    -->
<!-- ===================================================================== -->

<!-- PASTE <apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/"> ... </apex_contract> HERE VERBATIM -->

<!-- ===================================================================== -->
<!-- LAYER 2: WINDOWS NATIVE WORKSTATION OPERATING CONTEXT                  -->
<!-- ===================================================================== -->
## Workspace & Host Environment
- Workstation: Windows 11 host (`c:\GitDev\apexai-os-meta`). Isolated from external server harnesses.

## Knowledge Retrieval & Evidence Tooling
- Tool: Use QMD (`.agents/skills/qmd/SKILL.md`) for indexed search and surgical file slicing.
- Speed Escalation: Run `qmd search` (FTS5 BM25, 0.3s) first. Escalate to `qmd query` (hybrid AI, 20s+) only when keyword search returns zero results (`DEC-QMD-01`).
- Surgical Slicing: Fetch 20–40 line windows via `qmd get <path:line:count>` or `#docid:from:count`. Never bulk-read entire files (`DEC-QMD-04`).

## Completion Reporting
- Rule: Never describe a proposed block as applied. Completion requires the executor's exact-match result plus the required test evidence.
```

---

## 3. Multi-Surface Carrier Specification (`DEC-21` + `RP-10` Resolved)

When this blueprint is introduced into the live repository in the future installation phase:
1. **Primary Carriers (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`):** Carry the exact `<apex_contract v="1.0" base_ref="apex-meta/informatics/">...</apex_contract>` block and Layer 2 sections, verified by a deterministic `pytest` byte-identity gate (`test_carrier_byte_identity`). This immediately resolves `D10` (`GEMINI.md` missing informatics routing) and works across 100% of CLIs and IDE rule injectors without `@import` preprocessor fragility.
2. **Secondary Task-Scoped Surfaces (`.claude/CLAUDE.md` and `.github/copilot-instructions.md`):** Retain their specialized orchestration/navigation content and update their informatics pointer to reference `AGENTS.md` and `apex-meta/informatics/index.md`.
