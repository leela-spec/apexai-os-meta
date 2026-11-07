---
type: Runbook
id: RUNBOOK-HANDOVER-CODEX-DUAL-ACCOUNT-v1.0
title: Informatics Instruction Integration Handover — Codex / Cortex (2 Accounts)
description: Concrete integration handover and dual-account synchronization runbook for OpenAI Codex / Cortex CLI on Windows 11 using the v1.0-ultra two-layer carrier architecture.
status: current_truth
tags: [handover, runbook, codex, cortex, dual-account, multi-cli, agents-md, v1.0-ultra]
---

# Informatics Instruction Integration Handover: Codex / Cortex (2 Accounts)

> **Target Platform:** OpenAI Codex / Cortex CLI (`@codex`)  
> **Host OS:** Windows 11 (`C:\Users\gehma\.codex\`)  
> **Accounts:** 2 active developer accounts (e.g. Account 1: Personal/Admin, Account 2: Organization/Work)  
> **Carrier Files:** Global [`C:\Users\gehma\.codex\AGENTS.md`](file:///C:/Users/gehma/.codex/AGENTS.md) & Workspace [`AGENTS.md`](file:///c:/GitDev/apexai-os-meta/AGENTS.md)  
> **Target Version:** Apex AI OS Contract `v1.0-ultra` (Option B Pure XML, ~1,225 BPE tokens)

---

## 1. Architectural Discovery & Precedence

Cortex / Codex evaluates instructions at multiple hierarchical levels:

1. **Global Configuration Root (`C:\Users\gehma\.codex\`):**
   - Reads global `AGENTS.md` (or `instructions.md`) for machine-wide developer conventions.
   - Evaluates `config.toml` for model routing, context window thresholds, and reasoning effort.
2. **Repository Workspace Root (`<repo-root>\AGENTS.md`):**
   - Automatically injected as primary repository rules when running from any subdirectory of the workspace.
3. **Directory-Scoped Rules (`<subdir>\AGENTS.md`):**
   - Evaluated dynamically when Codex tools navigate into nested modules (e.g. `creator-onboarding-lab/AGENTS.md`).

---

## 2. Dual-Account Management Topology

Because the operator runs **2 active accounts**, choose between the two architectural isolation strategies below:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CODEX DUAL-ACCOUNT ARCHITECTURE                      │
│                                                                        │
│  STRATEGY A: SHARED WORKSTATION CARRIER (Recommended Default)          │
│  Both accounts run on the same Windows host and share:                 │
│    - Global:    C:\Users\gehma\.codex\AGENTS.md (Layer 1 + Devlore)    │
│    - Workspace: C:\GitDev\<repo>\AGENTS.md                             │
│  Accounts switch via auth profile / token in auth.json without drift.  │
│                                                                        │
│  STRATEGY B: ISOLATED HOME PROFILES (Environment Switching)            │
│  Account 1: CODEX_HOME=C:\Users\gehma\.codex-acc1                      │
│  Account 2: CODEX_HOME=C:\Users\gehma\.codex-acc2                      │
│  Used when accounts require disjoint API keys, telemetry, or proxies. │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Global Carrier Integration (`C:\Users\gehma\.codex\AGENTS.md`)

Deploy the Two-Layer carrier into the global Codex directory so that **both accounts** immediately inherit the universal contract without clobbering personal Windows defaults.

### 3.1 Concrete Global Configuration File

Write the following content to `C:\Users\gehma\.codex\AGENTS.md`:

```markdown
# Personal Windows development defaults

<!-- ===================================================================== -->
<!-- LAYER 1: PORTABLE UNIVERSAL AI OPERATING CONTRACT (v1.0-ultra)         -->
<!-- Canonical Owner: specs/apex_contract_v1.0_ultra.xml                     -->
<!-- ===================================================================== -->

<apex_contract v="1.0-ultra" base_ref="c:/GitDev/apexai-os-meta/apex-meta/informatics/final/">

<target>Verify the delivered result against each stated requirement before claiming completion. Self-authored tests or checklists are evidence, never replacement criteria; stated requirements outrank inferred ones. If evidence shows no change is needed, say so and stop.</target>

<product_first>Build the working product before surrounding machinery. Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss. A passing verification script never defines done.</product_first>

<scope>Do only authorized work and material enablers. Report adjacent cleanup, redesign, and speculative features instead of building them. Analyzing or planning never authorizes implementing.</scope>

<communication>Active voice, explicit actor, conclusion first. One imperative per sentence. Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report results and exact blockers; compress tool chatter.</communication>

<hold_position>Do not reverse on pushback without new evidence; restate evidence or clarify the flaw. Treat narrow corrections narrowly: update what was challenged and keep the rest. State disagreement plainly when evidence supports it.</hold_position>

<ground>Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries. State the command producing any absence, zero, or count claim. Check what is checkable now instead of deferring it. For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.</ground>

<reuse>Before building, inspect repository scripts, installed tools, libraries, and skills. Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.</reuse>

<context>Load context just-in-time; never bulk-read directories or references at start. Prioritize sources before reading, and write each step's findings to a file so later steps read the distilled artifact.</context>

<recovery>Work around incidental failures using the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>

<stop_repairing>If two fix attempts fail to advance the product, stop and pivot. Prior effort gives a failing approach zero claim on continuing.</stop_repairing>

<current_truth>State active truth only. Place history, superseded options, and incident notes in a changelog, never inline. Never name retired components in live rules.</current_truth>

<surgical>Never regenerate or overwrite an existing file in full.</surgical>

<editing when="changing, moving or deleting a file that already exists" ref="specs/execution-modes/patch-discipline.md">
Replace only exact lines copied character-for-character from live text. One change per edit. Move or copy via git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.
</editing>

<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">
Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies.
</new_machinery>

<detour when="about to propose a refactor, redesign, migration or infrastructure addition">
Must this be fixed before testing the product? If not, defer it in one line.
</detour>

<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md">
Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout.
</authoring>

<trade_off when="the operator must choose between material alternatives, or asks for options" ref="specs/execution-modes/bake-off.md">
Decide routine reversible choices yourself. For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.
</trade_off>

<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="specs/execution-modes/handover.md">
Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD).
</handover>

<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="specs/execution-modes/iterative-execution.md">
Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition.
</iterative>

<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="specs/governance-schemas.md">
Conform to declared schemas exactly; never invent fields. Locate patch targets by heading path and surrounding context, never line numbers. Open ref for exact JSON or YAML schemas.
</schemas>

<sync when="the operator asks to sync, commit or push">
Execute git commands immediately, not repo analysis. Preserve all files: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.
</sync>

<pointers>
Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.
</pointers>

</apex_contract>

<!-- ===================================================================== -->
<!-- LAYER 2: WORKSTATION OPERATING CONTEXT                                -->
<!-- ===================================================================== -->

- On Windows, Developer Mode permits non-elevated symbolic-link creation. When a new project, package manager, or build tool reports missing symlink support, check Developer Mode before requiring an elevated terminal.
- For Flutter projects, run `flutter doctor` before diagnosing a target-toolchain issue. Android, web, and Windows desktop have independent prerequisites.
```

---

## 4. Multi-Account Switching Workflow

### Workflow A: Shared Carrier (Single Home)
When both accounts share `C:\Users\gehma\.codex\`, switch logins cleanly without touching instruction files:
```powershell
# Check current account
codex auth whoami

# Switch to Account 2 (interactive or token)
codex auth login
```

### Workflow B: Isolated Environments (Dual Homes)
If you configure independent homes for complete sandboxing:
```powershell
# Launch under Account 1
$env:CODEX_HOME = "C:\Users\gehma\.codex-acc1"
codex

# Launch under Account 2
$env:CODEX_HOME = "C:\Users\gehma\.codex-acc2"
codex
```
*Note: If using Strategy B, ensure both `C:\Users\gehma\.codex-acc1\AGENTS.md` and `C:\Users\gehma\.codex-acc2\AGENTS.md` are symlinked to `C:\Users\gehma\.codex\AGENTS.md` or deployed identically.*

---

## 5. Verification & Health Check

Execute inside any target workspace (e.g., `c:\GitDev\MasterOfArts`):

1. **Verify Rule Ingestion:**
   ```powershell
   codex exec "State our two-strike repair rule and our file edit constraint."
   ```
   **Pass Criteria:**
   - Cites `<stop_repairing>`: two attempts without product advance triggers stop & pivot.
   - Cites `<editing>`: surgical line replacements copied character-for-character from live text.
