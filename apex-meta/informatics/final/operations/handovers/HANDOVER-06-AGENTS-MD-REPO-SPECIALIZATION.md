---
type: Runbook
id: RUNBOOK-HANDOVER-AGENTS-MD-SPECIALIZATION-v1.0
title: AGENTS.md Repository Specialization & De-Genericization Handover
description: Concrete handover and ready-to-deploy specification for refactoring AGENTS.md from generic agent behavioral prose into a sharp, high-signal repository operating map and architectural boundary guide.
status: current_truth
tags: [handover, runbook, agents-md, de-genericization, repo-specific, codex, cursor, copilot]
---

# Handover: `AGENTS.md` Repository Specialization & De-Genericization

> **Target Surface:** [`c:\GitDev\apexai-os-meta\AGENTS.md`](file:///c:/GitDev/apexai-os-meta/AGENTS.md)  
> **Target Audience:** Cross-tool coding agents (Codex CLI, Cursor, GitHub Copilot, Antigravity)  
> **Objective:** Strip generic agent truisms already enforced by the global Gemini carrier (`v1.0-ultra`) and replace them with high-signal, repo-specific architectural navigation, authority ladders, and tooling boundaries.

---

## 1. Audit: Why Current `AGENTS.md` Needs Specialization

The existing [`AGENTS.md`](file:///c:/GitDev/apexai-os-meta/AGENTS.md) (50 lines / ~998 tokens) is over **70% generic agent behavioral philosophy**:

| Section in Current `AGENTS.md` | Content Summary | Classification | Disposition |
|---|---|---|---|
| **Header Banner (lines 1–11)** | WSL2 Docker engine & single PostgreSQL topology redirect | Repo-Specific (but partly stale) | **Condense & Ground**: State current live stack concisely without outdated migration history. |
| **`## Git Dispatch` (lines 13–20)** | "Push known files starts with Git commands, sequence, rebase retry, ignore dirty files" | **100% Generic** | **Eliminate**: Fully covered by `<sync>` in the universal contract. (Linux `/mnt/c` warning is also obsolete on Windows 11 host). |
| **`## Directness` (lines 22–28)** | "Take shortest correct path, do not invent workflow, ignore dirty files" | **100% Generic** | **Eliminate**: Fully covered by `<iterative>` and `<scope>`. |
| **`## Core Intent Execution` (lines 29–40)** | "Target, ignore, preserve, classify, workaround, decide, report, current-truth, no-changelog" | **100% Generic** | **Eliminate**: This is literally the prose source of `<product_first>`, `<target>`, `<recovery>`, `<trade_off>`, and `<current_truth>`. |
| **`## Informatics & Knowledge Routing` (lines 41–44)** | Route doc changes to `apex-meta/informatics/index.md` | **Repo-Specific** | **Keep & Elevate**: High-value repo authority pointer. |
| **`## Scope` (lines 45–48)** | "Keep actions tied to target, no adjacent cleanup" | **100% Generic** | **Eliminate**: Fully covered by `<scope>`. |
| **Line 50** | "Never describe a proposed block as applied..." | **Execution Guard** | **Keep Verbatim**: Essential anti-hallucination verification gate. |

---

## 2. What High-Value Information SHOULD Be in `AGENTS.md`?

When an agent lands in `apexai-os-meta`, it doesn't need generic reminders to "be direct" or "not hedge." It needs to know:

1. **Repository Mission & Architectural Map:** What is this repo, and what lives in each top-level directory (`apex-meta/`, `ki-basis/`, `.agents/skills/`)?
2. **Frozen & Forbidden Zones:** Which legacy directories are historic archives that must **never** be touched or refactored (`ApexDefinition&OldVersions/`, `working_deleting/`, `_recovery_backup...`)?
3. **Authority & Precedence Hierarchy:** When documentation contradicts itself, what is the single source of truth? (`apex-meta/informatics/final/specs/` overrides general prose; `GLOSSARY.md` governs terminology).
4. **Local Tooling & Commands:** How does an agent actually test or validate changes in this repository? (`okf_validator.py`, pytest test suites, QMD retrieval speed protocol).
5. **Host Environment & Subsystem Boundaries:** Confirm that host execution is Windows 11 (`c:\GitDev\`), while the `ki-basis` Docker stack runs in a separate VM tracked under OpenProject WP #198.

---

## 3. Concrete Proposed `AGENTS.md` (Drop-In Replacement)

The following block is ready to replace [`c:\GitDev\apexai-os-meta\AGENTS.md`](file:///c:/GitDev/apexai-os-meta/AGENTS.md):

```markdown
# Apex AI OS Meta — Repository Operating Guide

> **📍 Core Infrastructure:** Windows 11 host (`c:\GitDev\apexai-os-meta`). The `ki-basis` Linux Docker/WSL2 engine runs in an isolated VM tracked under OpenProject WP #198. Do not run WSL/Linux daemon commands on host paths.

---

## 1. Repository Topology & Subsystem Map

- **`apex-meta/` (Core OS & Governance):**
  - `informatics/final/`: Canonical informatics standards, writing profiles (`WP`), file architectures (`FA`), and schemas (`GS`). Router: `final/index.md`.
  - `orchestration/`: Multi-agent orchestration runbooks, role definitions, and candidate architecture. Terminology authority: `GLOSSARY.md`.
  - `operations/`: Handover runbooks, integration logs, and system deployment specs.
- **`ki-basis/` (AI Engine Subsystem):** Isolated Docker/WSL2 service stack, OpenMouseBot, fixtures, and database scripts.
- **`.agents/skills/` (Local Agent Skills):** Custom tools including QMD fast retrieval (`qmd/SKILL.md`) and session ingests.
- **⚠️ Frozen Legacy Archives (READ-ONLY):**
  - `ApexDefinition&OldVersions/`, `working_deleting/`, `_recovery_backup_*`, `_restore_staging_*`.
  - **Invariant:** NEVER refactor, clean up, rename, or delete files in these directories.

---

## 2. Authority & Governance Precedence

1. **Specification Precedence:** When guidance conflicts, specifications under `apex-meta/informatics/final/specs/` (`standard.md`, `writing-profile.md`, `file-architecture.md`, `governance-schemas.md`) override informal notes or superseded blueprints.
2. **Terminology Authority:** `apex-meta/orchestration/GLOSSARY.md` governs multi-agent naming. Propose new terms as candidates; never invent parallel terminology.
3. **Current-Truth Doctrine:** Ground all claims in live originating artifacts (`path:line`), not historical changelogs or superseded summaries (`AGENT-OPERATING-CONTEXT.md` and `CURRENT-STATE.md` in `ki-basis` are superseded).

---

## 3. Evidence, Tooling & Verification Protocols

- **Knowledge Retrieval (QMD Speed Protocol):**
  - Run fast FTS5 BM25 search first: `qmd search <term>` (0.3s).
  - Escalate to hybrid AI search (`qmd query`) only when keyword search yields zero results (`DEC-QMD-01`).
  - Fetch surgical 20–40 line windows (`qmd get <path:line:count>`). Never bulk-read entire documents (`DEC-QMD-04`).
- **OpenProject Management:**
  - Route all OpenProject operations through the canonical Node client:
    `node C:\GitDev\agent-skills\skills\openproject\client\opCall.js <operation> ...`
  - Instance: Leela v17.x on `http://127.0.0.1:8083`. Mutating operations require `--confirmed`. Never write directly to PostgreSQL.
- **Deterministic Validation Gates:**
  - Governed Knowledge: Validate bundles before completing edits:
    `python apex-meta/informatics/final/tools/okf_validator.py --target <bundle_path>`
  - Informatics Test Suite: Ensure all tests pass:
    `python -m pytest apex-meta/informatics/final/verification/suites/`

---

## 4. Completion & Patch Gate

- **Completion Reporting Rule:** Never describe a proposed block as applied. Completion requires the executor's exact-match result plus the required test evidence.
- **Surgical Edits:** Modify existing files via exact-match character-for-character replacements. Never rewrite full files.
```

---

## 4. Verification & Health Check

After applying the updated `AGENTS.md`:
1. **Line Count & Token Reduction:**
   - Previous: 50 lines of generic philosophy (~998 tokens).
   - Specialized: ~55 lines of dense, actionable repository navigation, authority maps, and exact commands (~750 tokens).
2. **Run Pytest Gate:**
   ```powershell
   python -m pytest apex-meta/informatics/final/verification/suites/test_canonical_ownership.py
   ```
3. **Agent Active Probe:**
   Ask any agent landing in the repo:
   *"Where are canonical informatics specifications located, and what is our policy on the `ApexDefinition&OldVersions` directory?"*
   - Expected: Cites `apex-meta/informatics/final/specs/` and identifies `ApexDefinition&OldVersions/` as a frozen, read-only archive.
