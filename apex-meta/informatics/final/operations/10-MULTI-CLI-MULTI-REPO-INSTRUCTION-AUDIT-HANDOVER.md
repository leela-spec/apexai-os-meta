---
type: Runbook
id: RUNBOOK-MULTI-CLI-REPO-AUDIT-v1.0
title: Multi-CLI & Multi-Repo Instruction Audit & Alignment Handover
description: Master handover and architectural blueprint analyzing instruction discovery across 5 CLI agent accounts and 3 primary repositories (apexai-os-meta, MasterOfArts, Leela-Cloud-2026), mapping universal contracts to repo-specific lore.
status: current_truth
tags: [handover, runbook, multi-cli, multi-repo, instruction-audit, two-layer-architecture]
---

# Multi-CLI & Multi-Repo Instruction Audit & Alignment Handover

> **Purpose:** Handover document to onboard a new chat session to the Apex AI OS Instruction Architecture project. It defines the exact instruction discovery mechanisms for all 5 active CLI accounts and audits the instruction surfaces across our 3 primary GitDev repositories (`apexai-os-meta`, `MasterOfArts`, `Leela-Cloud-2026`) to cleanly separate **Layer 1 (Universal Portable Contract)** from **Layer 2 (Repo-Specific Lore that must be preserved)**.

---

## 1. Project Context & Current-Truth Baseline

All current-truth assets of the Universal AI Instruction Architecture live inside:
`c:\GitDev\apexai-os-meta\apex-meta\informatics\final\`

### Verified State:
- **Consolidation Complete:** Specs, candidates, verification suites, research iterations, and operations live strictly under `final/`. Root pointer [`index.md`](../../index.md) is under 100 lines / 4,000 chars.
- **Verification Engine:** **338 local pytest tests pass in 0.67–0.79s** (`python -m pytest apex-meta/informatics/final/verification/suites`).
- **Validated Candidate:** [`16-candidate-3A-ultra.md`](../candidates/16-candidate-3A-ultra.md) (1,225 BPE tokens, 22 surgical Option B rules) and [`03-BLUEPRINT-agents.md`](../candidates/03-BLUEPRINT-agents.md) (Two-Layer Carrier Blueprint).
- **Live Empirical Trial Validated:** Native Antigravity subagent A/B trial executed (`09-TRIAL-RUN-EVALUATION-REPORT.md`) proving that XML `<when="..." ref="...">` gates bypass index bloat and enforce surgical 20–40 line reading windows in practice.

---

## 2. Multi-CLI Agent Instruction Discovery Map

The operator uses **5 active agent accounts across 3 CLI ecosystems**:

| Ecosystem | Accounts | Global Discovery Path | Repository Discovery Path | Precedence & Inheritance Behavior |
|---|:---:|---|---|---|
| **Cortex / Codex** | 2 accounts | `C:\Users\gehma\.codex\AGENTS.md` (or `instructions.md`) | `AGENTS.md` (at repo root) | Cortex reads the workspace root `AGENTS.md`. If nested subdirectories contain `AGENTS.md`, some runners evaluate directory-scoped rules. |
| **Claude Code** | 2 accounts | `C:\Users\gehma\.claude\CLAUDE.md` | `CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/*.md` | Claude Code loads `~/.claude/CLAUDE.md` globally, then overrides/augments with repo `./CLAUDE.md`. It auto-imports all modular rules in `.claude/rules/`. |
| **Antigravity** | 1 account | `C:\Users\gehma\.gemini\GEMINI.md`, `~/.gemini/antigravity/` | `GEMINI.md` (at repo root), `.gemini/` | Antigravity injects `GEMINI.md` as workspace system rules, plus global rules from `~/.gemini/antigravity/global_rules/` and registered skills. |

### The Carrier Synchronization Imperative:
Because Cortex, Claude Code, and Antigravity look for different filenames (`AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`), the architecture uses a **Synchronized Two-Layer Carrier Pattern**:
- **Layer 1 (The Kernel):** The byte-identical `<apex_contract v="1.0-ultra">` XML block across all carriers.
- **Layer 2 (The Shell):** The repository-specific environment context and tooling rules.

---

## 3. Three Target Repositories Audit (`C:\GitDev\`)

We have audited the 3 target repositories on disk. Each repository has distinct domain responsibilities and critical lore that **must never be wiped or overwritten**:

### Repo 1: `c:\GitDev\apexai-os-meta` (Architecture & Meta-Orchestration)
- **Active Carrier Files:** `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude/rules/informatics.md`
- **What Must Be Preserved (Layer 2 Repo Context):**
  1. **Windows Host Environment:** Windows 11 host (`c:\GitDev\apexai-os-meta`). Isolated from external server harnesses.
  2. **QMD Retrieval Tooling:** Canonical QMD speed protocol (`qmd search` BM25 first, `qmd query` hybrid escalation, surgical 20–40 line slicing).
  3. **Canonical OpenProject Skill Route:** `node C:\GitDev\agent-skills\skills\openproject\client\opCall.js` targeting Leela OpenProject on `http://127.0.0.1:8083`.
  4. **Strict Carrier Immutability Gate:** `test_carrier_immutability` pytest protection.

### Repo 2: `c:\GitDev\MasterOfArts` (Portfolio & Project Families)
- **Active Carrier Files:** Root [`AGENTS.md`](file:///c:/GitDev/MasterOfArts/AGENTS.md) (28 lines), historical blueprints in `AIHowTo/Codex/`
- **What Must Be Preserved (Layer 2 Repo Context):**
  1. **Hermes Operating Doctrine (ADR-002):** Target architecture is NousResearch Hermes Agent full-functional stack.
  2. **Project Family Isolation:** First-level directories (`Lika/`, `ACIM/`, `Business/`) are distinct project families; internal structure stays strictly within that family.
  3. **Docker Sandboxed Terminal:** All file mutations and command executions run sandboxed via Docker backend (`terminal.backend = docker`).
  4. **Untracked Source Materials Manifest:** [`UNTRACKED-SOURCE-MATERIALS.md`](file:///c:/GitDev/MasterOfArts/UNTRACKED-SOURCE-MATERIALS.md) governs ~454 heavy ignored binaries (~630 MB: PDFs, audio, scans) awaiting transcription/transformation. Never bulk-commit raw binaries.
  5. **QMD Scopes:** Multi-family hybrid indexes (`moa-<family>`).
  6. **OpenProject Route:** Canonical Node client at `C:\GitDev\agent-skills\skills\openproject`.

### Repo 3: `c:\GitDev\Leela-Cloud-2026` (Production Application Stack)
- **Active Carrier Files:** Root [`AGENTS.md`](file:///c:/GitDev/Leela-Cloud-2026/AGENTS.md) (238 lines / 16.9 KB), [`CLAUDE.md`](file:///c:/GitDev/Leela-Cloud-2026/CLAUDE.md) (64 lines), `creator-onboarding-lab/AGENTS.md`
- **What Must Be Preserved (Layer 2 Repo Context):**
  1. **Product Authority Hierarchy:** Accepted operator decisions + authored per-feature materialization ledgers (Tier 1) > current code (Tier 2) > SSOT narrative/spec/canon (Tier 3).
  2. **Materialization Contracts:** `docs/ssot/architecture/materialization.md` and validator `scripts/check_ssot_contracts.py`. The ledger in `materialization.csv` owns build state (`target_status`).
  3. **Database & Code Boundaries:** Supabase migrations (`lib/**`, `supabase/migrations/**`).
  4. **OpenProject Feature Hierarchy:** Project `leela-cloud-2026` with feature subprojects (`leela-path`, `leela-skill-tree`, `leela-sequencing`, `leela-rhythm`).
  5. **Blast Radius Guard:** Report blast radius before modifying > 10 tracked files.
  6. **Framework Trigger Restrictions:** BMAD and Superpowers are operator-selected only; agents must never auto-invoke them.
  7. **Decision Integration Batch Semantics:** Exact 5-step semantic transaction protocol.

---

## 4. The Two-Layer Architecture: How Universal & Repo-Specific Merge

When rolling out our unified instruction system across these repositories, **we do not overwrite existing repository lore**. Instead, we assemble each carrier using the Two-Layer formula:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TWO-LAYER CARRIER MODEL                         │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ LAYER 1: UNIVERSAL PORTABLE OPERATING CONTRACT (v1.0-ultra)      │  │
│  │ (Byte-identical across all repos & CLIs. ~1,225 BPE tokens)      │  │
│  │                                                                  │  │
│  │  <apex_contract v="1.0-ultra" base_ref="...">                   │  │
│  │    <target> ... </target>                                        │  │
│  │    <scope> ... </scope>                                          │  │
│  │    <surgical> ... </surgical>                                    │  │
│  │    <hold_position> ... </hold_position>                          │  │
│  │    <iterative when="..." ref="..."> ... </iterative>             │  │
│  │  </apex_contract>                                                │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                  │                                     │
│                                  ▼                                     │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ LAYER 2: REPOSITORY & CLI SPECIFIC OPERATING CONTEXT             │  │
│  │ (Custom tailored per repo; preserves 100% of local rules)        │  │
│  │                                                                  │  │
│  │  - apexai-os-meta: Windows host + QMD speed protocol             │  │
│  │  - MasterOfArts:   Hermes stack + Docker backend + Untracked bz  │  │
│  │  - Leela-Cloud:    Materialization SSOT + Supabase + OpenProject │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Dispatch Instructions for the Next Chat Session

When continuing this work in the next chat session, prompt the agent with:

```markdown
You are continuing the Apex AI OS Instruction System rollout.
Read the master handover: `apex-meta/informatics/final/operations/10-MULTI-CLI-MULTI-REPO-INSTRUCTION-AUDIT-HANDOVER.md`.

Your objective:
1. Review the audited Layer 2 requirements for `apexai-os-meta`, `MasterOfArts`, and `Leela-Cloud-2026`.
2. Formulate the concrete Two-Layer Carrier Draft for each repository:
   - Keep Layer 1 (<apex_contract v="1.0-ultra">) identical.
   - Assemble Layer 2 preserving the exact domain lore audited in Section 3.
3. Verify that zero local invariants (such as Leela's materialization rules or MasterOfArts' Docker sandboxing) are diluted or lost.
4. Run deterministic validation (`python -m pytest apex-meta/informatics/final/verification/suites`).
```
