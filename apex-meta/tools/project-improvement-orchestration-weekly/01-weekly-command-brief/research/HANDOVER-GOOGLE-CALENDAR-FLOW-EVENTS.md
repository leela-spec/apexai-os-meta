# Handover: APEX Google Calendar Flow Event Creation

## 1. Objective
Implement automated creation of Google Calendar time-block events for planned APEX Flows (F1–F4) generated during weekly planning (`PrecapWeek`) and daily planning (`PrecapNextDay`).

---

## 2. Operating Boundary & Invariants
- **Role:** Non-destructive calendar writer.
- **Authority:** Only writes discretionary APEX Flow blocks into verified open time windows.
- **Safety Invariant:** NEVER overwrite, move, shorten, or delete existing external calendar events.
- **Anchor Invariant:** Respect standard routine anchors (Morning Routine 08:00–09:00, Midday Reset 12:30–13:30, Shutdown 18:00–18:30) as protected and unavailable for flow scheduling unless explicitly overridden by the operator.
- **Non-Execution Invariant:** Calendar events represent scheduled flow focus windows; they do not trigger autonomous code execution or background task workers without explicit operator confirmation.

---

## 3. Placement Algorithm & Rules
1. **Fetch Daily Calendar:** Query the operator's primary Google Calendar for the target date `[00:00 – 23:59]`.
2. **Calculate Free Blocks:**
   - Subtract all existing fixed meetings and protected anchors.
   - Identify contiguous free windows of $\ge 45$ minutes.
3. **Map Daily Flows into Time Windows:**
   - `F1 (Morning Deep Work):` Schedule in the first available morning window (ideally 09:00–10:30 or 09:30–11:00).
   - `F2 (Core Feature Build):` Schedule in the late morning or early afternoon window.
   - `F3 (System / Infrastructure):` Schedule in the mid-afternoon window.
   - `F4 (Secondary / Buffer):` Schedule in late afternoon before shutdown.
4. **Capacity & Compression Mapping:**
   - **Standard Flow:** 90-minute block (3 sprints $\times$ 25m + 15m transition/buffer).
   - **Compressed Flow:** 60-minute block (2 sprints $\times$ 25m + 10m buffer).
   - **Minimal Flow:** 30-minute block (1 sprint $\times$ 25m + 5m buffer).
   - **Deferred / Omitted Flow:** Do not create a calendar event.

---

## 4. Google Calendar Event Schema

For each active flow, emit a Google Calendar API `events.insert` payload conforming to this schema:

```json
{
  "summary": "[APEX F{flow_num}] {project_name}: {sub_target_name}",
  "description": "Project: {project_name} ({sub_target_tag})\nWeekly Target: {weekly_project_target}\n\n=== SPRINT TOPICS ===\n• S1: {s1_topic}\n• S2: {s2_topic}\n• S3: {s3_topic}\n\n=== DOWNSTREAM ARTIFACT ===\nFlow Card: file:///artifacts/flows/{date}/F{flow_num}-card.md",
  "start": {
    "dateTime": "YYYY-MM-DDTHH:MM:00+02:00",
    "timeZone": "Europe/Berlin"
  },
  "end": {
    "dateTime": "YYYY-MM-DDTHH:MM:00+02:00",
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

### Concrete Example
* **Event Title:** `[APEX F1] MasterOfArts: Lock Core IA & Hero Copy`
* **Start/End:** `2026-08-17T09:00:00+02:00` – `2026-08-17T10:30:00+02:00`
* **Description:**
  ```text
  Project: MasterOfArts ([MoA-T1])
  Weekly Target: Website Definition Baseline
  
  === SPRINT TOPICS ===
  • S1: Locate & audit current site source
  • S2: Reconcile audience & value proposition
  • S3: Synthesize baseline architecture brief
  
  === DOWNSTREAM ARTIFACT ===
  Flow Card: file:///artifacts/flows/2026-08-17/F1-card.md
  ```

---

## 5. Implementation Interfaces for Implementing AI
The implementing AI may realize this specification via any of the following supported mechanisms:

1. **Option A (MCP Calendar Server):** Use a Model Context Protocol (MCP) Google Calendar server (e.g. `google-calendar-mcp`) to invoke `create_event` with the schema above.
2. **Option B (Python / CLI Script):** Call a dedicated automation script (e.g. `scripts/calendar/sync_flow_events.py`) authenticated via local OAuth / service account.
3. **Option C (Deterministic ICS Export):** Generate a standard `.ics` calendar file (e.g. `artifacts/calendar/2026-W34-flows.ics`) that imports directly into Google Calendar / Apple Calendar with one click.
