---
type: Standard
id: HO-PW-RULE-00
title: "Canonical Decision-to-Owner Lock Rule — Root-Cause & Governance Fix"
description: "Explains why file sprawl and state drift happened during Precap Week design and defines the mandatory CDL-01..CDL-05 writeback and archive rule."
status: proposed
date: 2026-11-11
tags: [governance, anti-drift, single-owner, archive-policy, canonical-lock]
---

# 00 · Canonical Decision-to-Owner Lock Rule

## 1. Forensic Diagnosis — Why Sprawl & Drift Kept Happening

Five verified structural defects caused dozens of files to pile up while runtime skills drifted behind:

| Root Cause | Live Evidence (`path:line`) | Consequence |
|---|---|---|
| **1. "Or" writeback loophole** | `apex-meta/tools/project-improvement-orchestration-weekly/CONTEXT-RESILIENCE.md:11` (`"...reflected in CURRENT-STATE.md, DECISIONS.md, a module README/handover, or the actual production file it governs."`) | Agents treated logging a note inside a new `HANDOVER-*.md` or `DECISIONS.md` as done, skipping the dominating spec and production skill. |
| **2. Missing global Decision-Lock rule** | `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml:34` (`<current_truth>`) + `writing-profile.md` (`WP-23`) | Existing rules ban historical clutter inside active prose, yet never require patching the dominating file + retiring the old handover in the same turn. |
| **3. Runtime lag violating `D011`** | `.claude/skills/PrecapWeek/weekly-command-brief-template.md:57-205` + `validation-checklist.md:232-233` vs `01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md` | Nov 6–11 changes stayed inside `01-weekly-command-brief/` drafts (`21` root files + `14` `research/` folders). `.claude/skills/PrecapWeek/` still runs an Aug `Mon–Sat` `Seq 1–4` HTML table and rejects Saturday/Sunday planning. |
| **4. Six modules crammed into one directory** | `01-weekly-command-brief/` contains Stats (`HANDOVER-05`), Decisions (`HANDOVER-04`), Matrix 1 (`HANDOVER-01/03/06/MATRIX-1`), Matrix 2 (`HANDOVER-02/GCal`), Sequencing (`Q13/SEQ-SKILL`), OP intake (`00-*`), and 5 HTML/research trees. | A fresh chat reading `01-weekly-command-brief/` ingests conflicting Nov 6, Nov 8, Nov 9 (`v05`), and Nov 10 (`T1`) layers at once and loses what is live. |
| **5. Incomplete sweeps & prepend edits** | `CURRENT-STATE.md:1-18` vs `19-87`; `HANDOVER-03:87-89`; `HANDOVER-04:24`; `HANDOVER-05:77`; `ASSUMPTIONS-AND-DECISIONS-REGISTER.md:29-41` | Prepending new summaries above old text without sweeping callers left `21:00 Shutdown`, `Sun OFF`, `G-I-P-S-O drawer`, and `Dropdown` contradictions active inside "updated" files. |

---

## 2. The Canonical Decision-to-Owner Lock Rule (`CDL-01..CDL-05`)

Adopt these five non-negotiable rules for every architecture, spec, or skill change:

- **CDL-01 [P0 | I98/E95/R05] Single Canonical Owner Map:** Every concern has **one dominating file** registered in the bundle index (e.g., clock = `02-weekly-dispersal/week-blueprint.json`; cockpit layout = `SPEC-PRECAP-WEEK-MASTER.okf.md`; runtime execution = `.claude/skills/<Skill>/SKILL.md` + active templates). Never create a new `HANDOVER-*`, `DESIGN-*`, or `.patch` file to store a settled decision.
- **CDL-02 [P0 | I97/E92/R06] Mandatory Same-Turn Owner Writeback:** Before claiming completion on any accepted decision, apply an exact surgical patch (`AD-03`) to:
  1. the **canonical dominating specification**, AND
  2. the **active production runtime skill/template** (or emit an explicit `pending_runtime_sync` blocker in the final answer if mutation is gated by operator confirmation).
- **CDL-03 [P0 | I94/E95/R05] Thin Register Pointers Only:** Decision ledgers (`DECISIONS.md`, `log.md`, `ASSUMPTIONS-AND-DECISIONS-REGISTER.md`) store **only ID, date, status, 1–2 line ruling, and link to the canonical owner**. Never duplicate formulas, clock tables, or HTML specs inside ledgers.
- **CDL-04 [P0 | I95/E90/R08] Obligatory Caller Sweep (`AD-15`):** Whenever a constant, window, or rule changes (e.g., `Sun OFF -> Sat–Sun 12:00–16:00`, `21:00 -> Day Outro 22:00–22:30`), run `rg` across `.claude/skills/` and the active improvement module in the same turn and patch or flag every lingering hit.
- **CDL-05 [P1 | I90/E92/R05] Immediate Deterministic Archive (`ARCHIVE-POLICY.md`):** When a handover, `.patch`, or draft revision is superseded by landing into its canonical owner, move it immediately via `git mv` into `apex-meta/archive/weekly-orchestration/<batch>/` with `archive_metadata`. Zero competing drafts remain in active directories.

---

## 3. Input & Priority Ledger (Where This Rule Can Be Installed)

- **Weekly Orchestration governance (`local`, zero multi-repo blast radius):**
  - `apex-meta/tools/project-improvement-orchestration-weekly/CONTEXT-RESILIENCE.md:11` (close the `"or"` loophole).
  - `apex-meta/tools/project-improvement-orchestration-weekly/ORCHESTRATOR-DEFINITION.md:89-97` (`Completion behavior`).
  - `.claude/skills/weekly-orchestrator/SKILL.md` + `.claude/CLAUDE.md:43-53` (`Global boundaries`).
- **Global Apex Informatics contract (`multi-repo`, propagated by `apex_carrier_sync.py`):**
  - `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml:34` (`<current_truth>`) or `specs/carrier-layer2-shared.md`.
  - Sync script: `python apex-meta/informatics/final/tools/apex_carrier_sync.py --source worktree --sync` (touches `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`, plus `Leela-Cloud-2026` & `mindful-bar` vendoring checks).

---

## 4. Open Implementation Choice (Operator Approval Required)

| Option | Surface Patched | `I` (Impact) | `E` (Effort) | `R` (Risk) | Recommendation & Rejections |
|---|---|---:|---:|---:|---|
| **A (Recommended Scope-First)** | Patch `CONTEXT-RESILIENCE.md`, `ORCHESTRATOR-DEFINITION.md`, `.claude/CLAUDE.md`, and add scoped `.claude/rules/canonical-decision-lock.md` first | 90 | 20 | 10 | **Recommend:** Solves weekly sprawl immediately across Claude/Codex/AGY inside `apexai-os-meta` without triggering cross-repo vendor drift in `Leela` / `Mindful Bar`. |
| **B (Global Carrier Sync)** | Extend `<current_truth>` in `apex_contract_v1.0_ultra.xml` (or `carrier-layer2-shared.md`) and run `apex_carrier_sync.py --sync` | 96 | 45 | 35 | Reject for immediate blind run: touches global home-dir carriers and external repos; apply after Option A passes one module cycle cleanly. |
| **C (Hook / Script Gate)** | Pre-commit git hook rejecting multi-handover files | 60 | 70 | 45 | Reject: heavy verification machinery (`<new_machinery>`); clear carrier/local rules + `git mv` hygiene fix the cause directly. |

---

## 5. Exact Patch Ready to Apply Upon Confirmation (`Option A`)

Target 1 — `apex-meta/tools/project-improvement-orchestration-weekly/CONTEXT-RESILIENCE.md:11`:
- **Replace:** `until it is reflected in CURRENT-STATE.md, DECISIONS.md, a module README/handover, or the actual production file it governs.`
- **With:** `until it is patched into its single canonical dominating file (AND active .claude/skills/ runtime if behavior changes), linked as a thin pointer in DECISIONS.md, swept via rg for stale siblings, and all superseded handovers moved via git mv per ARCHIVE-POLICY.md.`

Target 2 — `apex-meta/tools/project-improvement-orchestration-weekly/ORCHESTRATOR-DEFINITION.md:89-97`:
- Add step under `Completion behavior`: `Execute CDL-01..CDL-05 (single-owner writeback, caller rg sweep, git mv archival of replaced handovers) before reporting a module decision closed.`

---

## 6. Definition of Done (DoD)

1. `CONTEXT-RESILIENCE.md:11` no longer permits leaving locked decisions only inside handovers or chat.
2. `.claude/CLAUDE.md` (or `.claude/rules/canonical-decision-lock.md`) explicitly routes settled decisions to their single canonical owner and forbids parallel competing handovers.
3. `CURRENT-STATE.md` top block (`lines 1-18`) is cleaned to match `FA-01` current-truth rules without contradictory `D017 Sunday off` residue.
4. `python apex-meta/informatics/final/tools/apex_carrier_sync.py` (if Option B chosen) exits `0`.

## 7. Fresh-Chat Starter Prompt

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/00-RULE-CANONICAL-DECISION-LOCK.md.
Apply Option A (or Option B if confirmed) surgically to close the decision-writeback loophole in CONTEXT-RESILIENCE.md, ORCHESTRATOR-DEFINITION.md, and .claude/CLAUDE.md / .claude/rules/, clean the stale D017 top banner in CURRENT-STATE.md, and verify zero broken references before closing.
```
