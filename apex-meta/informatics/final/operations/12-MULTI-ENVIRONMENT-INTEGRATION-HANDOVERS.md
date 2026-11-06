---
type: Runbook
id: RUNBOOK-MULTI-ENV-INTEGRATION-v1.0
title: Multi-Environment Informatics Instruction Integration Master Handover
description: Master operations runbook and synchronization blueprint coordinating the integration of the Apex AI OS Informatics instruction architecture across 5 environments (Gemini Web, Antigravity CLI, Codex dual-account, ChatGPT Web dual-account, Claude Code dual-account).
status: current_truth
tags: [runbook, multi-environment, multi-cli, gemini, antigravity, codex, chatgpt, claude-code, dual-account, handovers]
---

# Multi-Environment Informatics Instruction Integration Master Handover

> **Document ID:** `RUNBOOK-MULTI-ENV-INTEGRATION-v1.0`  
> **Status:** Current Truth  
> **Target Version:** Apex AI OS Contract `v1.0-ultra` (Option B Pure XML, ~1,225 BPE tokens)  
> **Scope:** 5 Target Environments covering all active web, workstation CLI, and dual-account setups.

---

## 1. Executive Summary & Integration Topology

This master runbook orchestrates the rollout of the **Apex AI OS Informatics Instruction Architecture** across the operator's 5 operational AI environments. 

Per architectural decisions `DEC-21` and `DEC-22`, the system strictly decouples:
- **Layer 1 (The Kernel):** The byte-identical `<apex_contract v="1.0-ultra">` XML block (~1,225 BPE tokens) defining universal operating behavior (target dominance, product first, scope bounds, surgical edits, anti-sycophancy, Cool Blue register).
- **Layer 2 (The Shell):** Environment-specific tooling routes, account isolation profiles, and repository-specific safety lore.

### The 5 Target Environments Matrix

| # | Target Environment | Accounts | Primary Discovery Mechanism | Integration Format | Dedicated Handover File |
|---|---|:---:|---|---|---|
| **1** | **Gemini Online Web AI** | 1 account | Custom Gems & Google AI Studio System Instructions | XML Kernel with attached specification files | [`HANDOVER-01-GEMINI-WEB-AI.md`](handovers/HANDOVER-01-GEMINI-WEB-AI.md) |
| **2** | **Antigravity CLI** | 1 account | `C:\Users\gehma\.gemini\GEMINI.md` + repo `GEMINI.md` | Two-Layer Markdown Carrier + OpenProject skill route | [`HANDOVER-02-ANTIGRAVITY-CLI.md`](handovers/HANDOVER-02-ANTIGRAVITY-CLI.md) |
| **3** | **Codex / Cortex** | 2 accounts | `C:\Users\gehma\.codex\AGENTS.md` + repo `AGENTS.md` | Shared Carrier or `CODEX_HOME` dual profiles | [`HANDOVER-03-CODEX-DUAL-ACCOUNT.md`](handovers/HANDOVER-03-CODEX-DUAL-ACCOUNT.md) |
| **4** | **ChatGPT Online AI** | 2 accounts | Custom Instructions (chats) & Custom GPTs (architecture) | High-density 1,500-char profile & full 8k Custom GPT | [`HANDOVER-04-CHATGPT-WEB-DUAL-ACCOUNT.md`](handovers/HANDOVER-04-CHATGPT-WEB-DUAL-ACCOUNT.md) |
| **5** | **Claude Code Windows** | 2 accounts | `C:\Users\gehma\.claude\CLAUDE.md` + `.claude/rules/` | Two-Layer Carrier + `ANTHROPIC_CONFIG_DIR` profiles | [`HANDOVER-05-CLAUDE-CODE-DUAL-ACCOUNT.md`](handovers/HANDOVER-05-CLAUDE-CODE-DUAL-ACCOUNT.md) |

---

## 2. Environment Handover Directory

Each environment has a dedicated, self-contained runbook with exact copy-paste ready blocks, token counts, account switching procedures, and verification test probes:

1. [`HANDOVER-01-GEMINI-WEB-AI.md`](handovers/HANDOVER-01-GEMINI-WEB-AI.md)
   - Configuration for Google Gemini Advanced **Custom Gems** (`Apex Informatics Architect`).
   - Configuration for **Google AI Studio** System Instructions (low-temperature parameter tuning).
   - Knowledge attachment instructions for cloud environments without local disk mounts.

2. [`HANDOVER-02-ANTIGRAVITY-CLI.md`](handovers/HANDOVER-02-ANTIGRAVITY-CLI.md)
   - Deployment to global [`C:\Users\gehma\.gemini\GEMINI.md`](file:///C:/Users/gehma/.gemini/GEMINI.md).
   - Coupling with the canonical OpenProject Node client route (`C:\GitDev\agent-skills\skills\openproject`).
   - QMD speed protocol (`DEC-QMD-01`/`04`) and workspace injection rules.

3. [`HANDOVER-03-CODEX-DUAL-ACCOUNT.md`](handovers/HANDOVER-03-CODEX-DUAL-ACCOUNT.md)
   - Deployment to global [`C:\Users\gehma\.codex\AGENTS.md`](file:///C:/Users/gehma/.codex/AGENTS.md).
   - Dual-account strategies: Shared Workstation Carrier vs. Isolated `CODEX_HOME` profiles (`.codex-acc1` / `.codex-acc2`).
   - Preservation of personal Windows Developer Mode symlink conventions and Flutter doctor lore.

4. [`HANDOVER-04-CHATGPT-WEB-DUAL-ACCOUNT.md`](handovers/HANDOVER-04-CHATGPT-WEB-DUAL-ACCOUNT.md)
   - Dual-box Custom Instructions profile calibrated to stay strictly within 1,500 character UI limits.
   - Dedicated **Custom GPT** (`Apex OS Architect`) embedding the full 5,917-character `v1.0-ultra` XML block.
   - Cross-account sharing protocol between Account 1 (creator) and Account 2 (subscriber).

5. [`HANDOVER-05-CLAUDE-CODE-DUAL-ACCOUNT.md`](handovers/HANDOVER-05-CLAUDE-CODE-DUAL-ACCOUNT.md)
   - Deployment to global [`C:\Users\gehma\.claude\CLAUDE.md`](file:///C:/Users/gehma/.claude/CLAUDE.md).
   - Dual-account profile switching via `ANTHROPIC_CONFIG_DIR` and non-elevated Windows symbolic links.
   - Modular path-scoped rules integration via [`.claude/rules/informatics.md`](file:///c:/GitDev/apexai-os-meta/.claude/rules/informatics.md).

---

## 3. Maintenance & Change Synchronization Protocol

When the core operating contract or specification modules under `apex-meta/informatics/` are updated:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SINGLE-SOURCE SYNCHRONIZATION FLOW                   │
│                                                                        │
│               16-candidate-3A-ultra.md (Canonical Source)              │
│                                   │                                    │
│         ┌─────────────────────────┴─────────────────────────┐          │
│         ▼                                                   ▼          │
│  LOCAL WORKSTATION CARRIERS                         ONLINE WEB SURFACES│
│  - C:\Users\gehma\.gemini\GEMINI.md                 - Gemini Custom Gem│
│  - C:\Users\gehma\.codex\AGENTS.md                  - AI Studio Preset │
│  - C:\Users\gehma\.claude\CLAUDE.md                 - ChatGPT GPT (Acc1)│
│  - Repository Root Carriers (3 Repos)                  │               │
│                                                        ▼               │
│                                                     (Syncs to Acc 2)   │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Local CLI Verification:** Run deterministic tests before pushing changes:
   ```powershell
   python -m pytest apex-meta/informatics/final/verification/suites
   ```
2. **Web Carrier Propagation:** Update the Custom GPT in ChatGPT Account 1 and the Custom Gem in Gemini Web.
3. **No-Divergence Rule:** Never introduce local, ad-hoc edits into individual web boxes or CLI files that differ from the canonical `<apex_contract v="1.0-ultra">` text without logging an architectural decision in [`01-decision-register.md`](../candidates/01-decision-register.md).
