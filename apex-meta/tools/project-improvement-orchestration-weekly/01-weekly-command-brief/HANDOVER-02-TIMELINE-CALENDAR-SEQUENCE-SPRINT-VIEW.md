---
type: handover
id: HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW-v1.0
title: Handover — Matrix 2 Real Calendar View (2h Sequences, 30m Sprints & 3-Item Slots)
description: Architectural specification and handover for Matrix 2, defining the true hourly calendar integration with 2-hour sequences, 30-minute sprints, 3 items per sprint, and external meeting coordination.
status: active
tags: [weekly-orchestration, precap-week, matrix-2, calendar-view, sequence-sprint, em-09]
---

# Handover — Matrix 2 Real Calendar View (2h Sequences, 30m Sprints & 3-Item Slots)

### Operator-Corrected Display Contract (`v05` 2026-11-09, Clock Reconciled 2026-11-10)

- Keep **one** fit-to-width **Monday–Sunday** hourly timetable covering [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) (`08:00–24:00` weekday regime with `F1–F4`, protected anchors, `18:30–19:30` Evening Physical Course, `20:30–22:00` `Project Night`/`Freizeit`, `22:00–22:30` `Day Outro`, `23:30–24:00` `Sleep Routine`; plus `12:00–16:00` Saturday–Sunday 2-Flow weekend regime). Never substitute an abstract Flow-only strip.
- **No horizontal scrollbar**: remove fixed minimum table widths (`min-width:1150px` / `overflow-x:auto`); use `table-layout:fixed; overflow-wrap:anywhere;`, wrap cell text cleanly, and reflow into stacked day columns if viewport width cannot hold seven readable day columns.
- Remove unrequested secondary controls: no secondary Monday expanded detail panel (`#flowdetail`), no separate day-role card strip (`#daystrip`), no second `Full saved sprint-by-day table`, and no extra meeting/summary button or pill bars (`.displayrow`). The hourly timetable is the single visible calendar interface.
- Immediately below the final `23:30–24:00` timetable row, show one full-width 3-column personal-focus strip: **Mental**, **Physical**, and **Regeneration**, each holding a `1–3` item bullet list supplied by the operator (`not yet specified` when empty). These are personal priorities, not projects, work packages, or Flow assignments.
- Keep detailed sprint data in canonical records; removing duplicate UI panels is not authorization to discard underlying planning data.

## 1. 4-Dimensional Handover Contract

### 1.1 Input & Priority Ledger
- **Authoritative Sources**:
  - `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`: Google Calendar placement algorithm, routine anchors, and meeting safety rules.
  - Operator Guidance:
    - Standard Sequence = **2 hours** (120 minutes).
    - Sprint = **30 minutes**.
    - Sprint Depth Requirement: **At least 3 distinct items per sprint**.
    - Day Coverage: **Monday through Sunday** (Mon–Fri weekday regime `08:00–24:00`; Sat–Sun weekend regime `12:00–16:00`).
  - Upstream Matrix 1: Supplies Priority Goal contexts; [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) owns all clock windows.
- **Deliberately Excluded**: Untyped ad-hoc lists; generic non-hourly calendar tables; hardcoded clock tables overriding `week-blueprint.json`.

### 1.2 Process & Placement Architecture
1. **Single Clock Owner**: Exact daily block start/end timestamps (`08:00–24:00` Mon–Fri = `960m`, `Day Outro 22:00–22:30`, `Sat/Sun 12:00–16:00` = `240m`) read dynamically from [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json).
2. **Sequence / Flow Structure (`120m` Focus Blocks)**:
   - Every `120m` Flow follows `3 × (P 2m + M 3m + C 30m + recap 1m) + R 12m` across `24` weekly Flows (`F1–F4` Mon–Fri, `F1–F2` Sat–Sun).
3. **3-Item Craft Sprint Standard**:
   - Inside each `30m C` Craft block, display up to `3` distinct actionable items / micro-deliverables (while in-Flow `P/M/R` carry read-only practice Chunks).

---

## 2. Specification for Calendar & Sequence Visualizations

### 2.1 Full-Width HTML Interactive Calendar Specification

```html
<!-- Real Hourly Calendar Table with 2h Sequence Blocks & 30m Sprints (fit-to-width; timestamps from week-blueprint.json) -->
<div class="calendar-viewport" style="width:100%; overflow-x:visible;">
  <table style="width:100%; table-layout:fixed; overflow-wrap:anywhere; border-collapse:collapse; font-size:0.84em; border:1px solid #30363d;">
    <thead>
      <tr style="background:#161b22; color:#f0f6fc;">
        <th style="width:10%; padding:6px; border:1px solid #30363d;">Time Window</th>
        <th style="width:12.8%; padding:6px; border:1px solid #30363d;">Monday</th>
        <th style="width:12.8%; padding:6px; border:1px solid #30363d;">Tuesday</th>
        <th style="width:12.8%; padding:6px; border:1px solid #30363d;">Wednesday</th>
        <th style="width:12.8%; padding:6px; border:1px solid #30363d;">Thursday</th>
        <th style="width:12.8%; padding:6px; border:1px solid #30363d;">Friday</th>
        <th style="width:13%; padding:6px; border:1px solid #30363d;">Saturday</th>
        <th style="width:13%; padding:6px; border:1px solid #30363d;">Sunday</th>
      </tr>
    </thead>
    <tbody>
      <!-- Routine Anchor (08:00-08:30 per week-blueprint.json) -->
      <tr style="background:rgba(110,118,129,0.1); color:#8b949e;">
        <td style="padding:4px; text-align:center; font-family:monospace;">08:00 - 08:30</td>
        <td colspan="5" style="padding:4px; text-align:center;">🔒 Protected Anchor: Morning Routine</td>
        <td colspan="2" style="padding:4px; text-align:center;">Weekend regime starts 12:00</td>
      </tr>

      <!-- Flow Block 1: 08:30 - 10:30 (120m Weekday) -->
      <tr style="border-top:2px solid #58a6ff;">
        <td style="padding:6px; text-align:center; font-weight:600; background:rgba(88,166,255,0.08);">
          08:30 - 10:30<br><span style="font-size:0.8em; color:#58a6ff;">Flow 1 (120m)</span>
        </td>
        <td style="padding:6px; vertical-align:top;">
          <strong>Apex OS: Driver Hook (C Craft · 3×3 Interleaved with P/M + 12m R)</strong>
          <!-- Iteration 1 Craft Sprint (30m) with 3 Items -->
          <div style="margin:4px 0; padding:4px; background:#161b22; border-left:2px solid #3fb950; border-radius:3px;">
            <span style="font-size:0.8em; color:#3fb950; font-weight:600;">C1 (30m · after P 2m + M 3m)</span>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:0.88em;">
              <li>1. Parse HID tables</li>
              <li>2. Bitmask map register</li>
              <li>3. Kernel hook stub</li>
            </ul>
          </div>
          <!-- Iteration 2 Craft Sprint (30m) with 3 Items -->
          <div style="margin:4px 0; padding:4px; background:#161b22; border-left:2px solid #3fb950; border-radius:3px;">
            <span style="font-size:0.8em; color:#3fb950; font-weight:600;">C2 (30m · after P 2m + M 3m)</span>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:0.88em;">
              <li>1. Interrupt service routine</li>
              <li>2. Ring buffer allocate</li>
              <li>3. Zero packet drop test</li>
            </ul>
          </div>
          <!-- Iteration 3 Craft Sprint (30m) with 3 Items -->
          <div style="margin:4px 0; padding:4px; background:#161b22; border-left:2px solid #3fb950; border-radius:3px;">
            <span style="font-size:0.8em; color:#3fb950; font-weight:600;">C3 (30m · +1m recap, 12m R)</span>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:0.88em;">
              <li>1. Latency bench pass</li>
              <li>2. Log timestamp deltas</li>
              <li>3. Kernel trace verify</li>
            </ul>
          </div>
        </td>
        <!-- Repeat across Tue-Sun (7 day columns; colspan sums match 8 total cols) -->
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top; background:rgba(110,118,129,0.05);">Weekend starts 12:00</td>
        <td style="padding:6px; vertical-align:top; background:rgba(110,118,129,0.05);">Weekend starts 12:00</td>
      </tr>

      <!-- Flow 2 (10:30 - 12:30) and Midday Reset Anchor (12:30 - 13:30) -->
      <tr style="background:rgba(110,118,129,0.1); color:#8b949e;">
        <td style="padding:4px; text-align:center; font-family:monospace;">12:30 - 13:30</td>
        <td colspan="5" style="padding:4px; text-align:center;">🔒 Protected Anchor: Lunch + AfterLunch</td>
        <td colspan="2" style="padding:4px; text-align:center;">Sat/Sun Flow 1 (`12:00–14:00`)</td>
      </tr>

      <!-- Remaining week-blueprint.json rows (F3 13:30-15:30, Break 15:30-16:00, Finanzen 16:00-16:30, F4 16:30-18:30, Evening Physical 18:30-19:30, Abend 19:30-20:30, Project Night/Freizeit 20:30-22:00, Day Outro 22:00-22:30, Freizeit 22:30-23:30, Sleep Routine 23:30-24:00) -->
    </tbody>
  </table>
  <!-- Immediately below the final 23:30-24:00 Sleep Routine row: -->
  <div style="display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; margin-top:12px;">
    <div><strong>Mental</strong><ul><li>not yet specified</li></ul></div>
    <div><strong>Physical</strong><ul><li>not yet specified</li></ul></div>
    <div><strong>Regeneration</strong><ul><li>not yet specified</li></ul></div>
  </div>
</div>
```

---

## 3. 5-Component Forensic Report

1. **Observation**: Previous drafts either decoupled Matrix 2 from daily clock timestamps or introduced `min-width:1150px` horizontal scrolling and duplicate secondary Monday/sprint panels.
2. **Logic Chain**: Rendering **one** fit-to-width `Mon–Sun` hourly timetable driven solely by [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) (`08:00–24:00` weekday + `12:00–16:00` weekend `F1–F4`, anchors, and `Day Outro`), followed directly by the 3-column personal-focus strip, preserves scannability without duplicate controls or overflow.
3. **Caveats**: Actual external calendar meetings must be read via Google Calendar integration where available; `v05` presentation overrides prohibit extra secondary panels without deleting source data.
4. **Conclusion**: Matrix 2 is formally aligned to the `v05` operator display contract and `T1` single blueprint owner (`week-blueprint.json`).
5. **Verification Method**: Inspect rendered cockpit HTML at both desktop (`1280px`) and narrow mobile (`390px`) viewports confirming `scrollWidth <= clientWidth`, `08:00–24:00` `Mon–Sun` rows, zero secondary Monday/sprint panels, and the `Mental | Physical | Regeneration` strip directly below `23:30–24:00`.
