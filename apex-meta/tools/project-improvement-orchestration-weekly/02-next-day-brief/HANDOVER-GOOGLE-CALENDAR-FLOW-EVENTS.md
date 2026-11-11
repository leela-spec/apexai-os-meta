# Handover: APEX Google Calendar Flow Event Creation (`PrecapNextDay` Gated Writer)

## 1. Objective
Implement gated, non-destructive creation of Google Calendar time-block events for approved daily APEX Flows (`F1–F4` weekday, `F1–F2` weekend) exclusively during daily planning (**`PrecapNextDay`**) after explicit operator approval (`Q10`). **`PrecapWeek` is strictly read-only (`create_calendar_events: false`) and emits `calendar_block_proposals` only.**

---

## 2. Operating Boundary & Invariants
- **Role:** Non-destructive calendar writer owned strictly by `PrecapNextDay` (`02-next-day-brief/`).
- **Clock Authority (`T1` / `D018`):** All nominal Flow windows and protected routine anchors are read directly from [`02-weekly-dispersal/week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json) (`Mon–Fri 08:00–24:00` with `F1 08:30–10:30`, `F2 10:36–12:36`, `Lunch + AfterLunch 13:04–14:20`, `F3 14:20–16:20`, `Break + Finanzen 16:20–16:30`, `F4 16:30–18:30`, `Evening Physical 18:30–19:30`, `Abend 19:30–20:30`, `Project Night / Freizeit 20:30–22:00`, `Day Outro 22:00–22:30`, `Sleep Routine 23:30–24:00`; `Sat–Sun 12:00–16:00` with `F1 12:00–14:00`, `F2 14:00–16:00`).
- **Safety Invariant:** NEVER overwrite, move, shorten, or delete existing external calendar events. Respect commute/prep buffers (e.g., `30m` buffer prior to offsite events like `München Tanz`).
- **Mixed-Project Sprint Support (`Q06` / `SEQ-Q2`):** A `120m` Flow may carry a single portfolio area or mixed-project `C1/C2/C3` Craft sprints across the **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`).
- **Non-Execution Invariant:** Calendar events represent scheduled flow focus windows; they do not trigger autonomous code execution without explicit operator confirmation.

---

## 3. Placement Algorithm & Rules
1. **Fetch Daily Calendar:** Query the operator's primary Google Calendar for the target date `[00:00 – 23:59]` in `Europe/Berlin` (automatic CET `+01:00` / CEST `+02:00` offset resolution).
2. **Calculate Free Blocks & Overlay Deformation:**
   - Subtract all existing fixed meetings, commute/prep buffers, and protected anchors from `week-blueprint.json`.
   - Preserve `slot_id` stability (`24` nominal `120m` Flows in `slot-inventory.json`) while applying the capacity overlay:
3. **Capacity & Compression Mapping (`T1` `120m` Nominal Flow):**
   - **Full Flow (`full_flow_3_sprints`):** `120-minute` nominal block (`3 × 30m C` Craft sprints + `24m` in-Flow `P/M/R` + `6m` flow recap).
   - **Compressed Flow (`compressed_flow_2_sprints`):** `2 × 30m C` Craft sprints + proportional `P/M/R` inside the remaining collision-free window.
   - **Minimal Flow (`minimal_flow_1_sprint`):** `1 × 30m C` Craft sprint inside a heavily constrained window.
   - **Deferred / Omitted Flow (`omitted_flow`):** Do not create a calendar event; record mandatory omission reason.

---

## 4. Google Calendar Event Schema

For each operator-approved daily flow in `PrecapNextDay`, emit a Google Calendar API `events.insert` payload using `Europe/Berlin` IANA timezone (resolving `+01:00` CET / `+02:00` CEST dynamically):

```json
{
  "summary": "[APEX F{flow_num}] {portfolio_area}: {flow_outcome}",
  "description": "Portfolio Area: {portfolio_area}\nWeekly Outcome: {weekly_project_target}\nCapacity Shape: {capacity_shape}\n\n=== 3x3 CRAFT SPRINTS (30m each) ===\n• C1: {c1_topic}\n• C2: {c2_topic}\n• C3: {c3_topic}\n\n=== IN-FLOW P/M/R CHUNKS (DD-22A) ===\n• P (3x2m): {p_chunks}\n• M (1x5m): {m_chunk}\n• R (3x5m): {r_chunks}\n\n=== DOWNSTREAM ARTIFACT ===\nFlow Card: file:///artifacts/flows/{date}/F{flow_num}-card.md",
  "start": {
    "dateTime": "YYYY-MM-DDTHH:MM:00",
    "timeZone": "Europe/Berlin"
  },
  "end": {
    "dateTime": "YYYY-MM-DDTHH:MM:00",
    "timeZone": "Europe/Berlin"
  },
  "colorId": "9",
  "transparency": "opaque",
  "reminders": {
    "useDefault": false,
    "overrides": [
      { "method": "popup", "minutes": 10 }
    ]
  }
}
```

### Concrete Example (`T1` `120m` Flow, CET)
* **Event Title:** `[APEX F1] Master of Arts: Website Content & Flexbox Navigation`
* **Start/End:** `2026-11-09T08:30:00+01:00` – `2026-11-09T10:30:00+01:00` (`Europe/Berlin`)
* **Description:**
  ```text
  Portfolio Area: Master of Arts ([OP-WP#163])
  Weekly Outcome: Website content draft & responsive layout
  Capacity Shape: full_flow_3_sprints (120m)
  
  === 3x3 CRAFT SPRINTS (30m each) ===
  • C1: Stage draft essay files & reading metadata
  • C2: Wire flexbox navigation & mobile reading drawer
  • C3: Desktop/mobile Chrome & Safari verification
  
  === IN-FLOW P/M/R CHUNKS (DD-22A) ===
  • P (3x2m): Martial Arts / General / Knee (I3_P pinned)
  • M (1x5m): Intention
  • R (3x5m): Yoga Nidra / Audiobooks / Socializing
  
  === DOWNSTREAM ARTIFACT ===
  Flow Card: file:///artifacts/flows/2026-11-09/F1-card.md
  ```

---

## 5. Implementation Interfaces for Implementing AI
The implementing AI may realize this specification via any of the following supported mechanisms:

1. **Option A (MCP Calendar Server):** Use a Model Context Protocol (MCP) Google Calendar server (e.g. `google-calendar-mcp`) to invoke `create_event` with the schema above.
2. **Option B (Python / CLI Script):** Call a dedicated automation script (e.g. `scripts/calendar/sync_flow_events.py`) authenticated via local OAuth / service account.
3. **Option C (Deterministic ICS Export):** Generate a standard `.ics` calendar file (e.g. `artifacts/calendar/2026-W34-flows.ics`) that imports directly into Google Calendar / Apple Calendar with one click.
