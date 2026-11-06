---
type: specification
id: SPEC-WEEKLY-COMMAND-BRIEF-DUAL-MATRIX-v1.0
title: Weekly Command Brief Specification — Dual-Matrix Architecture & OpenProject Engine
description: Canonical layout specification for the Weekly Command Brief combining non-temporal project process flows, full-width HTML calendar sequences, and OpenProject grounding.
status: approved_specification
tags: [weekly-orchestration, precap-week, openproject, dual-matrix, command-brief]
---

# Weekly Command Brief Specification — Dual-Matrix Architecture & OpenProject Engine

## 1. Core Architectural Invariants

- [P0 | I98/E95/R05] Dual-View Separation: Every Weekly Command Brief must cleanly separate non-temporal project development (Matrix 1) from calendar sequence allocation (Matrix 2).
- [P0 | I96/E94/R08] OpenProject Identity Authority: All project tasks, work packages, and subtasks must reference canonical OpenProject identifiers (`[OP-WP#<id>]`). When OpenProject is offline or unreachable, mark state as `[OP-UNRESOLVED]` with fallback markers; never invent synthetic identifiers.
- [P0 | I95/E95/R05] Informatics Decision Governance: Operator decisions must adhere to QMD informatics tagging `[P0–P3 | I/E/R]` with structured bullet nesting, status, impact, and actionable resolutions.
- [P0 | I94/E92/R10] Four-Sequence Calendar Floor: Matrix 2 must assign daily sprints across the four active weekly sequences:
  1. Sequence 1: Priority Master of Arts website (including invoices).
  2. Sequence 2: Investment (pipeline recheck, ingestion, data dashboard).
  3. Sequence 3: Apex OS (OpenMouse button integration, driver bindings).
  4. Sequence 4: Leela (skill tree completion).
- [P0 | I92/E90/R08] Downstream Contract Preservation: The Weekly Command Brief must retain the embedded YAML `presentation_handoff` block for seamless, 0-token consumption by `PrecapNextDay`.

---

## 2. Section Specifications

### 2.1 Operator Decision Block (`## Operator Decisions`)
The operator decision block enforces human sovereignty over weekly scope, trade-offs, and critical path locks.
- **Rule Syntax**: Each decision must be tagged with `[P0-P3 | I<impact>/E<effort>/R<risk>]`.
- **Nesting Structure**:
  - `Decision ID & Title [P# | I#/E#/R#]`: The high-level decision or governance action.
    - `• Context`: The underlying constraint, blocker, or tradeoff surfaced by synthesis.
    - `• OpenProject Anchor`: Associated work package (`[OP-WP#<id>]`) or project ID.
    - `• Action Required`: Explicit instruction for the operator or planning engine.
    - `• Status`: `[PROPOSED | APPROVED | REJECTED | DEFERRED]`.

### 2.2 Weekly Direction Block (`## Weekly Direction`)
Defines the portfolio-level North Star across all active project sequences.
- **Header**: High-level portfolio outcome summary.
- **Highlight Goals Ledger**:
  - `• Project Name`: Primary measurable deliverable due by Saturday close.
  - `• Strategic Leverage`: Why this work must happen during this specific weekly iteration.
  - `• Capacity Floor`: Total allocated focus hours across the 4 sequences.

---

## 3. Matrix 1: Project Architecture & Process Flow (Non-Temporal)

Matrix 1 visualizes *how* each project evolves mechanically from current baseline to target completion, without being constrained by calendar dates or day allocations.

### 3.1 Structure per Active Project
Each active project entry must follow this exact nested hierarchy:

```markdown
### Project: {{PROJECT_NAME}} (OP ID: {{PROJECT_SLUG_OR_ID}})

- **Strategic Outcome**: {{MEASURABLE_WEEKLY_TARGET}}
- **Baseline State**: {{WHERE_THE_PROJECT_STANDS_NOW}}

- **Process Flow & Iterations**:
  - `Step 1: [OP-WP#<id>] {{NAME}}` ➔ `Step 2: [OP-WP#<id>] {{NAME}}` ↻ `Iteration [OP-WP#<id>] {{NAME}}` ➔ `Step 3: [OP-WP#<id>] {{NAME}}`
  - *Evolution Commentary*:
    - "This is there now": {{CURRENT_STATE_OR_EXISTING_ASSET}}
    - "This goes where": {{DESTINATION_FILE_OR_PIPELINE_HANDOFF}}

- **Shortlist (Weekly Commitments)**:
  - [ ] **[OP-WP#<id>] {{TASK_NAME}}** ({{I/R/E_SCORE}})
    - • Subtask 1: {{SUBTASK_NAME}} — Expected output: `{{ARTIFACT_PATH}}`
    - • Subtask 2: {{SUBTASK_NAME}} — Dependency: `[OP-WP#<parent_id>]`
    - • *Handshake*: {{HANDOFF_NOTES}}

- **Longlist (Backlog / Staged / Next in Queue)**:
  - [ ] **[OP-WP#<id>] {{STAGED_TASK_NAME}}**: Deferred reason or trigger condition.
  - [ ] **[OP-WP#<id>] {{FUTURE_PHASE_NAME}}**: Dependent on shortlist completion.
```

---

## 4. Matrix 2: Timeline & Calendar View (Temporal / Sequences & Flows)

Matrix 2 maps the four core sequences to Monday through Saturday sprint slots using a full-width, responsive HTML table. This circumvents standard Markdown width constraints while remaining fully renderable in Obsidian and GitHub.

### 4.1 Sequence Definitions & Roles
1. **Sequence 1 — Priority Master of Arts**: Website modernization, content staging, and invoice workflows.
2. **Sequence 2 — Investment**: Pipeline recheck, ingestion harness, and data dashboard verification.
3. **Sequence 3 — Apex OS**: OpenMouse button integration, driver bindings, and hardware loop verification.
4. **Sequence 4 — Leela**: Skill tree architecture, progression rules, and node validation.

### 4.2 HTML Responsive Matrix Standard (Sequence-by-Sprint Architecture)
The table must span 100% width with horizontal overflow scrolling, structured column headers for Mon–Sat, and explicit rows for Sprint 1, Sprint 2, and Sprint 3 under each Sequence.

```html
<div class="weekly-calendar-matrix" style="width: 100%; overflow-x: auto; margin: 16px 0;">
  <table style="width: 100%; min-width: 1050px; border-collapse: collapse; font-family: system-ui, sans-serif; font-size: 0.85em; border: 1px solid rgba(128,128,128,0.3);">
    <thead>
      <tr style="background: rgba(128,128,128,0.15); border-bottom: 2px solid #555;">
        <th style="width: 16%; padding: 8px; text-align: left;">Sequence / Project</th>
        <th style="width: 8%; padding: 8px; text-align: center;">Sprint</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Mon</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Tue</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Wed</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Thu</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Fri</th>
        <th style="width: 11%; padding: 8px; text-align: left;">Sat</th>
      </tr>
    </thead>
    <tbody>
      <!-- Repeat for each of the 4 Sequences with 3 Sprint rows -->
      <tr>
        <td rowspan="3" style="padding: 8px; vertical-align: top; background: rgba(128,128,128,0.05); border-bottom: 2px solid #555;">
          <strong>Seq 1: Master of Arts</strong><br>
          <span style="font-size: 0.85em; color: #888;">Website & Invoices</span>
        </td>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 1</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#110] Nav Header</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#110] Breakpoints</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#112] Asset Minify</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#112] Copy Sync</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#112] Quality Check</td>
        <td style="padding: 6px; vertical-align: top; color: #888;">Buffer</td>
      </tr>
      <tr>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 2</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#115] Data Schema</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#115] Line Math</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#120] Tax Formula</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#120] PDF Engine</td>
        <td style="padding: 6px; vertical-align: top;">[OP-WP#120] Template Bind</td>
        <td style="padding: 6px; vertical-align: top; color: #888;">Review Gate</td>
      </tr>
      <tr style="border-bottom: 2px solid #555;">
        <td style="padding: 6px; text-align: center; font-weight: 600;">Sprint 3</td>
        <td style="padding: 6px; vertical-align: top;">Baseline Review</td>
        <td style="padding: 6px; vertical-align: top;">Currency Formatter</td>
        <td style="padding: 6px; vertical-align: top;">Zero Discount Edge</td>
        <td style="padding: 6px; vertical-align: top;">Billing Export CLI</td>
        <td style="padding: 6px; vertical-align: top;">End-to-End Run</td>
        <td style="padding: 6px; vertical-align: top; color: #888;">Archival</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 5. OpenProject Skill Integration Protocol

### 5.1 Canonical Tool Routing
Whenever `PrecapWeek` prepares the weekly plan:
1. **Runner Path**: `node C:\GitDev\agent-skills\skills\openproject\client\opCall.js <command> ...`
2. **Read-Only Ingestion Sequence**:
   - `opCall.js doctor`: Check connection to `http://127.0.0.1:8083`.
   - `opCall.js project.list`: Fetch active project IDs and slugs.
   - `opCall.js wp.list --project <id>`: Fetch open work packages for Apex, Priority, Leela, Master of Arts, and Investment.
3. **Safety Gate**: Never perform mutating writes during precap planning unless explicitly authorized with `--confirmed`.

### 5.2 Degraded / Offline Protocol
If OpenProject returns `ECONNREFUSED` or authentication fails:
- Do not stall or abort the planning session.
- Tag work items with local fallback markers: `[OP-OFFLINE: WP-<project>-<index>]`.
- Log an Operator Decision with `[P1 | I85/E20/R15]` flagging that OpenProject synchronization is pending reconnection.

---

## 6. Failure Guards

- **FG-01 (No Synthetic IDs)**: AI agents must never create hallucinated numeric OpenProject IDs. Use `[OP-UNRESOLVED]` if an ID cannot be retrieved.
- **FG-02 (Scope Containment)**: `PrecapWeek` produces directional daily sprints; detailed intra-day task cards and prompt packets remain strictly with `PrecapNextDay`.
- **FG-03 (Format Integrity)**: Matrix 2 HTML must maintain valid tag closures to prevent corruption of Obsidian preview modes.
