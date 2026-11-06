---
type: handover
id: HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW-v1.0
title: Handover — Matrix 2 Real Calendar View (2h Sequences, 30m Sprints & 3-Item Slots)
description: Architectural specification and handover for Matrix 2, defining the true hourly calendar integration with 2-hour sequences, 30-minute sprints, 3 items per sprint, and external meeting coordination.
status: active
tags: [weekly-orchestration, precap-week, matrix-2, calendar-view, sequence-sprint, em-09]
---

# Handover — Matrix 2 Real Calendar View (2h Sequences, 30m Sprints & 3-Item Slots)

## 1. 4-Dimensional Handover Contract

### 1.1 Input & Priority Ledger
- **Authoritative Sources**:
  - `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`: Google Calendar placement algorithm, routine anchors, and meeting safety rules.
  - Operator Guidance:
    - Standard Sequence = **2 hours** (120 minutes).
    - Sprint = **30 minutes**.
    - Sprint Depth Requirement: **At least 3 distinct items per sprint**.
    - Day Coverage: **Monday through Saturday**.
  - Upstream Matrix 1: Supplies the decomposed 30-minute Sprint Units for each project.
- **Deliberately Excluded**: Untyped ad-hoc lists; generic non-hourly calendar tables.

### 1.2 Process & Placement Architecture
1. **Time Geometry**:
   - Operating Window: `08:00 – 18:30` (10.5 hours daily).
   - Protected Anchors:
     - Morning Routine / Daily Setup: `08:00 – 09:00` (60m).
     - Midday Reset / Lunch: `12:30 – 13:30` (60m).
     - Shutdown / Outro: `18:00 – 18:30` (30m).
   - Net Focus Available: Up to 8.0 hours (four 2-hour sequences on unconstrained days).
2. **Sequence Structure (2-Hour Focus Blocks)**:
   - Sequence 1: `09:00 – 11:00` (Morning Focus Sequence)
   - Sequence 2: `11:00 – 12:30` + Buffer / Overflow or `10:30 – 12:30`
   - Sequence 3: `13:30 – 15:30` (Afternoon Build Sequence)
   - Sequence 4: `15:45 – 17:45` (Late Afternoon System / Secondary Sequence)
3. **Sprint Granularity (30-Minute Execution Blocks)**:
   - Inside each 2-hour sequence, up to 3 to 4 sprints of 30 minutes are executed.
   - Standard 2h allocation: **Sprint 1 (30m)** + **Sprint 2 (30m)** + **Sprint 3 (30m)** + **Sprint 4 / Review Buffer (30m)**.
4. **3-Item Sprint Cell Standard**:
   - Every sprint slot must explicitly display up to 3 distinct actionable items / micro-deliverables derived from Matrix 1.

---

## 2. Specification for Calendar & Sequence Visualizations

### 2.1 Full-Width HTML Interactive Calendar Specification

```html
<!-- Real Hourly Calendar Table with 2h Sequence Blocks & 30m Sprints -->
<div class="calendar-viewport" style="width:100%; overflow-x:auto;">
  <table style="width:100%; min-width:1150px; border-collapse:collapse; font-size:0.84em; border:1px solid #30363d;">
    <thead>
      <tr style="background:#161b22; color:#f0f6fc;">
        <th style="width:8%; padding:6px; border:1px solid #30363d;">Time Window</th>
        <th style="width:15%; padding:6px; border:1px solid #30363d;">Monday</th>
        <th style="width:15%; padding:6px; border:1px solid #30363d;">Tuesday</th>
        <th style="width:15%; padding:6px; border:1px solid #30363d;">Wednesday</th>
        <th style="width:15%; padding:6px; border:1px solid #30363d;">Thursday</th>
        <th style="width:15%; padding:6px; border:1px solid #30363d;">Friday</th>
        <th style="width:17%; padding:6px; border:1px solid #30363d;">Saturday</th>
      </tr>
    </thead>
    <tbody>
      <!-- Routine Anchor -->
      <tr style="background:rgba(110,118,129,0.1); color:#8b949e;">
        <td style="padding:4px; text-align:center; font-family:monospace;">08:00 - 09:00</td>
        <td colspan="6" style="padding:4px; text-align:center;">🔒 Protected Anchor: Morning Routine & Daily Orchestrator Prep</td>
      </tr>

      <!-- Sequence Block 1: 09:00 - 11:00 (2 Hours) -->
      <tr style="border-top:2px solid #58a6ff;">
        <td style="padding:6px; text-align:center; font-weight:600; background:rgba(88,166,255,0.08);">
          09:00 - 11:00<br><span style="font-size:0.8em; color:#58a6ff;">Sequence 1 (2h)</span>
        </td>
        <td style="padding:6px; vertical-align:top;">
          <strong>Apex OS: Driver Hook</strong>
          <!-- Sprint 1 (30m) with 3 Items -->
          <div style="margin:4px 0; padding:4px; background:#161b22; border-left:2px solid #3fb950; border-radius:3px;">
            <span style="font-size:0.8em; color:#3fb950; font-weight:600;">Sp 1 (09:00-09:30)</span>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:0.88em;">
              <li>1. Parse HID tables</li>
              <li>2. Bitmask map register</li>
              <li>3. Kernel hook stub</li>
            </ul>
          </div>
          <!-- Sprint 2 (30m) with 3 Items -->
          <div style="margin:4px 0; padding:4px; background:#161b22; border-left:2px solid #3fb950; border-radius:3px;">
            <span style="font-size:0.8em; color:#3fb950; font-weight:600;">Sp 2 (09:30-10:00)</span>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:0.88em;">
              <li>1. Interrupt service routine</li>
              <li>2. Ring buffer allocate</li>
              <li>3. Zero packet drop test</li>
            </ul>
          </div>
          <!-- Sprint 3 (30m) with 3 Items -->
          <div style="margin:4px 0; padding:4px; background:#161b22; border-left:2px solid #3fb950; border-radius:3px;">
            <span style="font-size:0.8em; color:#3fb950; font-weight:600;">Sp 3 (10:00-10:30)</span>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:0.88em;">
              <li>1. Latency bench pass</li>
              <li>2. Log timestamp deltas</li>
              <li>3. Kernel trace verify</li>
            </ul>
          </div>
        </td>
        <!-- Repeat across Tue-Sat -->
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top;">...</td>
        <td style="padding:6px; vertical-align:top; background:rgba(110,118,129,0.05);">Saturday Buffer</td>
      </tr>

      <!-- External Meeting / Break Interruption Example -->
      <tr style="background:rgba(210,153,34,0.1); border-left:4px solid #d29922;">
        <td style="padding:4px; text-align:center; font-family:monospace;">11:00 - 11:30</td>
        <td style="padding:4px;">☕ Transition Buffer</td>
        <td style="padding:4px; background:rgba(210,153,34,0.2); color:#f0f6fc;">📅 <strong>Stakeholder Sync</strong> (11:00-11:30)</td>
        <td style="padding:4px;">☕ Transition Buffer</td>
        <td style="padding:4px;">☕ Transition Buffer</td>
        <td style="padding:4px;">☕ Transition Buffer</td>
        <td style="padding:4px;">Review Gate</td>
      </tr>

      <!-- Midday Reset Anchor -->
      <tr style="background:rgba(110,118,129,0.1); color:#8b949e;">
        <td style="padding:4px; text-align:center; font-family:monospace;">12:30 - 13:30</td>
        <td colspan="6" style="padding:4px; text-align:center;">🔒 Protected Anchor: Midday Reset & Lunch</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 3. 5-Component Forensic Report

1. **Observation**: Previous drafts represented Matrix 2 as an abstract matrix of arbitrary project names with a single task per cell, disconnected from actual daily clock hours (08:00–18:30), external calendar meetings, and fixed routine anchors.
2. **Logic Chain**: The operator requires an actionable, visually realistic calendar schedule where standard 2-hour sequences are positioned in real open time windows around external meetings, and subdivided into 30-minute sprints accommodating at least 3 distinct checklist items.
3. **Caveats**: Actual external meetings must be queried via Google Calendar API or provided in the planning feed; where unavailable, standard default 2h windows (09:00–11:00, 11:30–12:30/13:30, 13:30–15:30, 15:45–17:45) apply.
4. **Conclusion**: Matrix 2 is now formally specified as the **True Hourly Calendar & Sequence/Sprint Grid**.
5. **Verification Method**: Inspect `WEEKLY_PRECAP_DRAFT_W45.html` and `WEEKLY_PRECAP_DRAFT_W45.md` to confirm the presence of hourly time blocks, 2h sequence containers, 30m sprint subdivisions, and 3 items per sprint.
