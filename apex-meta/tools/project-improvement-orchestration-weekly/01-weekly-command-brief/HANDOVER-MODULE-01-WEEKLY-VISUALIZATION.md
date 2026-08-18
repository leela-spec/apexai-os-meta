# Module 01 Handover — Weekly Command Brief Visualization Architecture

## 1. Executive Summary
This document provides complete architectural orientation for any AI agent or operator working on Module 01 (`Weekly_Command_Brief`). The week visualization problem is resolved, validated against operator requirements, and integrated into the canonical production template `.claude/skills/PrecapWeek/weekly-command-brief-template.md`.

---

## 2. Core Architecture: The Two-Matrix System

Weekly planning is divided into two sequential visual matrices placed immediately under `## Weekly architecture` in the Brief:

### Matrix 1: Project Strategy, Sub-Targets & Leverage Ledger
- **Purpose:** Answers "What strategic progress are our active projects achieving this week, and why does it matter now?"
- **Structure:**
  - **Project / Stream:** Active project name (with `★` focus marker if named priority).
  - **Weekly Strategic Target:** Single macro objective for the week.
  - **Granular Sub-Targets:** 2–4 discrete, numbered sub-targets (`[Proj-T1]`, `[Proj-T2]`, etc.) with concise definitions. These tags provide 1-to-1 traceability into Matrix 2.
  - **Strategic Leverage & Deliverables:** Explains strategic unlock and expected output artifact.

### Matrix 2: Flow-by-Day Calendar & Execution Grid
- **Purpose:** Answers "How are the 4 daily flows (F1–F4) allocated across Monday–Friday, around real meeting commitments, and what is the concrete goal of each sprint?"
- **Structure:**
  - **Columns:** Weekdays (Monday through Friday).
  - **Column Headers:** Real external calendar meetings and focus hours formatted as stats: `FreeT: Xh | Meets: X (Yh)` + meeting titles/times. Internal routine anchors (morning/lunch/outro) are excluded from the visual headers.
  - **Rows:** Four planned daily flows (`F1` Focus, `F2` Build, `F3` System, `F4` Ops/Secondary).
  - **Cell Syntax:**
    ```text
    **[{Project Name} ★] · `[{Proj-Tx}]`**
    • S1: {Concrete S1 Outcome Goal}
    • S2: {Concrete S2 Outcome Goal}
    • S3: {Concrete S3 Outcome Goal}
    ```
  - **Deferral Syntax:**
    ```text
    *[{Project Name}] · `[{Proj-Tx}]` Deferred*
    *({Concise Reason, e.g. Shifted to Thu due to 6h meeting load})*
    ```
  - **Visual Calm Rule:** Composite scores and raw metrics are omitted from Matrix 2 table cells to avoid visual clutter.

---

## 3. Decision Metrics & Scoring Specification
Where scoring calculations are required (e.g. downstream prioritization or machine handoff), the scratchpad syntax is used:
- **Syntax:** `(I{Impact}/E{Evidence}/R{Risk}: {CompositeScore})` (e.g. `(I94/E90/R20: 80)`).
- **Scale:** Normalized integer index from `1` to `100`.
- **Formula:**
  $$\text{Score} = \text{round}\left( \frac{\text{Impact} \times \text{Evidence}}{100} \times \left(1 - \frac{\text{Risk}}{200}\right) \right)$$
- **Autoregressive Scratchpad Property:** Writing `(I90/E95/R20)` before emitting the final score forces the LLM attention heads to attend to the input parameters, ensuring deterministic arithmetic.

---

## 4. Google Calendar Integration Handover
Automated time-blocking of planned flows (`F1`–`F4`) in Google Calendar around real meeting constraints is specified in:
[`research/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`](./research/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md)

Key rules for calendar writers:
1. **Safety:** Never modify or delete existing external meetings.
2. **Anchors:** Protect standard routines (08:00–09:00, 12:30–13:30, 18:00–18:30).
3. **Placement:** Fit standard (90m), compressed (60m), or minimal (30m) flow blocks into available focus windows.
4. **Description:** Populate event body with project name, sub-target tag, weekly target, and S1/S2/S3 sprint goals.

---

## 5. File Inventory & Status
- **Canonical Production Template:** `.claude/skills/PrecapWeek/weekly-command-brief-template.md` (Updated with Dual-Matrix architecture; legacy Daily Seed Map removed).
- **Design Authority:** `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md` (Updated & locked).
- **Interactive Prototypes:** `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/prototypes/` (All 5 standalone visual candidates preserved for reference).
- **Calendar Handover:** `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md` (Active reference for calendar integrations).
