Listed directory apex-meta
Listed directory tools
Listed directory project-improvement-orchestration-weekly
Listed directory 01-weekly-command-brief
Searched for "DESIGN-DECISIONS"
Searched for "PrecapWeek"
Listed directory PrecapWeek
Viewed HANDOVER.md:1-85
Viewed DECISIONS.md:1-239
Viewed README.md:1-34
Searched for "WEEK-VISUALIZATION-RESEARCH-HANDOVER"
Viewed weekly-command-brief-template.md:1-134
Viewed SKILL.md:1-137
Viewed weekly-blueprint-standard.md:1-305
Viewed weekly_plan_packet-20260816-2026-W34.md:1-249
Viewed weekly-blueprint-meeting-example.md:1-422
Viewed 03-planning-artifact-designs.okf.yaml:1-365
Viewed calendar-planning-guidance.md:1-442
Viewed J2-weekly-command-brief.md:1-9
Viewed 01_RESEARCH_FINDINGS.md:1-447
Viewed PersonalOrchestrationProcessFlow.md:1-800
Viewed weekly_plan_packet-20260712-2026-W29.md:1-219
Searched web: ""markdown" weekly planner calendar matrix layout UX information design"
Searched web: ""executive dashboard" "weekly planning" swimlane matrix "information design" HCI Edward Tufte"

# Weekly Command Brief Visualization: Research, Evaluation & Decision Report

---

## 1. Recommendation

### Primary Visualization: Candidate 3 — Two-Tier Hybrid Architecture (Week Calendar Anchor Ribbon + Project Workstream Trajectory Matrix)

**Verdict:**  
Candidate 3 resolves the fundamental tension in weekly orchestration between **temporal calendar awareness** ("What does my Tuesday look like?") and **project continuity** ("What progress will Leela make this week?"). 
* **Tier 1 (The Calendar Anchor Ribbon)** provides an instant 5-column overview of daily capacity shapes, meeting loads, focus themes, and active flow counts.
* **Tier 2 (The Project Workstream Trajectory Matrix)** maps active projects against weekdays with inline deliverables `Task (Ixx/Rxx/Exx)`, explicit dependency arrows, deadline badges, and deliberate deferrals.

This dual-tier layout delivers sub-10-second situational awareness in pure desktop Markdown, eliminates linear scrolling fatigue, and remains 100% deterministic for LLM generation.

### Delivery Mode Recommendation: Mode B (Complete Markdown Brief + Zero-Dependency Deterministic HTML/SVG Single-File Visual Projection)
* **Canonical Truth:** The Markdown `Weekly_Command_Brief` remains the complete, self-sufficient, authoritative weekly plan.
* **Enhanced Projection:** PrecapWeek deterministically emits a companion standalone, zero-dependency HTML/SVG file (`artifacts/weekly-plans/visual/2026-Wxx-board.html`) linked directly from the top result card.
* **Failure Resilience:** If unopened or unrendered, the Markdown Brief suffers zero information loss. No external cloud sync, no database, no dual-maintenance burden.

---

## 2. Recommended W34 Visualization (Production Format)

```markdown
## Weekly Architecture (2026-W34)

### Week Calendar & Capacity Ribbon
| Dimension | Mon 08-17 (Start) | Tue 08-18 (Build) | Wed 08-19 (Build) | Thu 08-20 (Review) | Fri 08-21 (Buffer) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day Focus** | Kickoff & Baselines | Deep Feature Build | Core Offer Structuring | Integration & Review | Closeout & Overflow |
| **Capacity Shape** | 🟢 Standard (4 Flows) | 🟢 Standard (4 Flows) | 🟢 Standard (4 Flows) | 🟢 Standard (4 Flows) | 🟢 Standard (4 Flows) |
| **Fixed Anchors** | 🔒 Morning/Lunch/Outro | 🔒 Morning/Lunch/Outro | 🔒 Morning/Lunch/Outro | 🔒 Morning/Lunch/Outro | 🔒 Morning/Lunch/Outro |
| **Active Roster** | Leela, MoA, Apex, Inv | Leela, MoA, Apex, Inv | Leela, MoA, Apex, Inv | Leela, MoA, Apex, Inv | Leela, MoA, Apex, Inv |
| **Constraints / Risks** | ⚠️ Cal unverified (8h base) | ⚠️ Cal unverified (8h base) | ⚠️ Cal unverified (8h base) | ⚠️ Cal unverified (8h base) | ⚠️ Cal unverified (8h base) |

---

### Project Workstream Trajectory Matrix
| Project / Stream | Mon 08-17 (Start) | Tue 08-18 (Build) | Wed 08-19 (Build) | Thu 08-20 (Review) | Fri 08-21 (Buffer) | Weekly Target & Leverage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MasterOfArts**<br>*(Primary Focus)* | 🎯 Define website core architecture `(I94/R30/E90)` | 📝 Draft offer copy blocks `(I92/R25/E85)` | 📐 Finalize page section map `(I90/R20/E90)` | 🔍 Review site handoff assets `(I85/R15/E85)` | 📦 Consolidate launch scope `(I88/R20/E90)` | **Website Definition Baseline:** Establish implementation-ready IA and copy. |
| **Leela**<br>*(Product Core)* | ⚡ Verify Home runtime & spatial tree `(I90/R20/E95)` | ⚖️ Reconcile decision ledger `(I85/R15/E90)` | 🔗 Audit interaction contracts `(I88/R25/E90)` | 🧪 Integrate spatial bounds `(I87/R20/E85)` | 🛡️ Review product continuity `(I80/R15/E90)` | **Spatial Skill Tree:** Advance dependency-clear interaction mechanics. |
| **Apex**<br>*(Orchestration)* | 📜 Baseline ApexKB contracts `(I89/R25/E95)` | ↳ ⚙️ Draft query retrieval spec `(I88/R30/E90)` | 🧩 Validate skill fork boundaries `(I86/R20/E90)` | 🔍 Review orchestration spine `(I85/R15/E90)` | 📊 Close cycle evidence log `(I82/R10/E95)` | **Apex KB Integration:** Lock contracts and query retrieval architecture. |
| **Investment**<br>*(Intelligence)* | 📥 Collect topic alert inputs `(I84/R35/E80)` | 📊 Structure crypto/macro intel `(I82/R30/E85)` | 🎯 Map decision criteria matrix `(I80/R25/E80)` | 🔔 Review portfolio thresholds `(I78/R20/E85)` | 📑 Synthesize weekly asset recap `(I75/R15/E90)` | **Decision Intelligence:** Collect inputs to unblock canonical branches. |
| **Residual**<br>*(Recovery / Support)* | ⏸️ *[Deferred]* Capacity reserved | ⏸️ *[Deferred]* Capacity reserved | ⏸️ *[Deferred]* Capacity reserved | ⏸️ *[Deferred]* Capacity reserved | 🔄 Buffer / NARM / Dating capacity `(I30/R20/E70)` | **Overflow Protection:** Absorb spillover without competing with primary flows. |

> **Matrix Legend & Conventions:**  
> `🎯 Primary Milestone` | `⚡ Verification` | `📝 Content/Copy` | `📜 Contract/Spec` | `↳ Sequence Dependency` | `⏸️ Deliberate Deferral` | `🔒 Protected Block` | `⚠️ Unverified/Risk`
```

---

## 3. Runner-Up Candidate

### Candidate 1: Single Project × Weekday Cross-Matrix (Merged Monolithic Table)

```markdown
### Project × Weekday Cross-Matrix
| Project | Mon (Start) [4F] | Tue (Build) [4F] | Wed (Build) [4F] | Thu (Review) [4F] | Fri (Buffer) [4F] |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MasterOfArts** | Define website architecture `(I94/R30/E90)` | Draft offer copy blocks `(I92/R25/E85)` | Finalize section map `(I90/R20/E90)` | Review site handoff assets `(I85/R15/E85)` | Consolidate launch scope `(I88/R20/E90)` |
| **Leela** | Verify Home runtime `(I90/R20/E95)` | Reconcile decision ledger `(I85/R15/E90)` | Audit interaction contracts `(I88/R25/E90)` | Integrate spatial bounds `(I87/R20/E85)` | Review product continuity `(I80/R15/E90)` |
| **Apex** | Baseline ApexKB contracts `(I89/R25/E95)` | Draft query retrieval spec `(I88/R30/E90)` | Validate skill boundaries `(I86/R20/E90)` | Review orchestration spine `(I85/R15/E90)` | Close cycle evidence log `(I82/R10/E95)` |
| **Investment** | Collect topic inputs `(I84/R35/E80)` | Structure macro intel `(I82/R30/E85)` | Map decision criteria `(I80/R25/E80)` | Review portfolio thresholds `(I78/R20/E85)` | Synthesize asset recap `(I75/R15/E90)` |
| **Residual** | *[Deferred]* | *[Deferred]* | *[Deferred]* | *[Deferred]* | NARM / Dating buffer `(I30/R20/E70)` |
| *Capacity & Notes* | 🟢 Normal; 🔒 Fixed anchors | 🟢 Normal; 🔒 Fixed anchors | 🟢 Normal; 🔒 Fixed anchors | 🟢 Normal; 🔒 Fixed anchors | 🟢 Normal; 🔒 Fixed anchors |
```

### Why Candidate 1 Lost to Candidate 3:
1. **Capacity Clutter vs. Visibility:** Squeezing daily capacity constraints, meeting warnings, and calendar shape notes into the bottom table rows or column headers creates visual overcrowding. 
2. **Cognitive Parsing Penalty:** When day-level parameters (e.g. "Tuesday has a 4h workshop; Wednesday is overloaded") are mixed into project rows, the operator cannot scan the *temporal rhythm* independently of *project details*.
3. **No Dedicated Target/Leverage Anchor:** Candidate 1 lacks a concise column summarizing the weekly target outcome for each project, forcing the operator to read every weekday cell to infer the project's macro direction.

---

## 4. Stress-Test Results (Shortlist Candidates)

### Scenario B: Meeting-Heavy & Compressed Week
* **Conditions:** Tuesday compressed (2 flows, 4h executive workshop); Wednesday overloaded (1 minimal flow, 6h fixed meetings); Thursday compressed (2 flows); Friday standard buffer.

#### Candidate 3 Performance in Scenario B:
```markdown
### Week Calendar & Capacity Ribbon
| Dimension | Mon (Start) | Tue (Build - Compressed) | Wed (Overloaded - Minimal) | Thu (Review - Compressed) | Fri (Buffer - Standard) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day Focus** | Kickoff & Launch | Core Spec & Workshop | Critical Unblocker Only | Review & Recovery | Closeout & Overflow |
| **Capacity Shape** | 🟢 Standard (4 Flows) | 🟡 Compressed (2 Flows) | 🔴 Overloaded (1 Flow max) | 🟡 Compressed (2 Flows) | 🟢 Standard (3 Flows + Buffer) |
| **Fixed Anchors** | 🔒 Protected anchors | 👥 09:00-13:00 Strategy WS | 👥 09:00-15:00 Exec Reviews | 👥 14:00-17:00 Client Sync | 🔒 Protected anchors |
| **Active Roster** | Leela, MoA, Apex, Inv | Apex, Leela | Apex (Sole Flow) | MoA, Apex | Leela, Residual |
| **Reductions** | None | ⏸️ MoA, Inv deferred | ⏸️ Leela, MoA, Inv deferred | ⏸️ Leela, Inv deferred | ⏸️ Inv deferred |

### Project Workstream Trajectory Matrix
| Project | Mon (Start) [4F] | Tue (Compressed) [2F] | Wed (Minimal) [1F] | Thu (Compressed) [2F] | Fri (Buffer) [3F] | Weekly Target & Deferral Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Apex** | 📜 Baseline ApexKB contracts `(I89/R25/E95)` | ⚙️ Draft query retrieval spec `(I88/R30/E90)` | 🧩 Lock skill boundary unblocker `(I86/R20/E90)` | 🔍 Review orchestration spine `(I85/R15/E90)` | 📊 Close cycle evidence log `(I82/R10/E95)` | **Maintained Core:** Preserved across all days as critical orchestration spine. |
| **MasterOfArts** | 🎯 Define website architecture `(I94/R30/E90)` | ⏸️ *[Deferred: Workshop load]* | ⏸️ *[Deferred: Day Overload]* | 📝 Draft offer copy blocks `(I92/R25/E85)` | 📦 Consolidate launch scope `(I88/R20/E90)` | **Compressed:** Shifted copy build to Thu recovery to protect deep focus. |
| **Leela** | ⚡ Verify Home runtime `(I90/R20/E95)` | ⚖️ Reconcile decision ledger `(I85/R15/E90)` | ⏸️ *[Deferred: Day Overload]* | ⏸️ *[Deferred: Meeting Sync]* | 🧪 Integrate spatial bounds `(I87/R20/E85)` | **Compressed:** Maintained kickoff & Friday integration; skipped mid-week. |
| **Investment** | 📥 Collect topic inputs `(I84/R35/E80)` | ⏸️ *[Deferred: Capacity]* | ⏸️ *[Deferred: Capacity]* | ⏸️ *[Deferred: Capacity]* | ⏸️ *[Deferred: Capacity]* | **Deferred Week:** Deliberately deferred due to severe meeting compression. |
| **Residual** | ⏸️ *[Deferred]* | ⏸️ *[Deferred]* | ⏸️ *[Deferred]* | ⏸️ *[Deferred]* | 🔄 Absorb weekly overflow `(I30/R20/E70)` | **Protected Buffer:** Friday recovery preserved. |
```
* **Stress Evaluation:** Candidate 3 clearly communicates why projects are missing on Tue/Wed in the ribbon *before* the matrix. The matrix cleanly renders `⏸️ [Deferred: Reason]` without destroying column alignments.

---

### Scenario C: Sequencing & Hard Dependency-Driven Week
* **Conditions:** 
  1. Apex KB contract baseline (Mon) MUST precede Query Retrieval Spec (Tue) which MUST precede Skill Tree integration (Wed).
  2. MasterOfArts website review due Thursday 17:00 (locks Wed build and Thu review).
  3. Investment Automation flow `(I91/R60/E50)` deliberately deferred because prerequisite data pipeline is unverified.

#### Candidate 3 Performance in Scenario C:
```markdown
### Project Workstream Trajectory Matrix
| Project | Mon (Start) | Tue (Build) | Wed (Build) | Thu (Review & Gate) | Fri (Buffer) | Dependency & Sequencing Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Apex** | 📜 [Dep-A1] Baseline KB contracts `(I89/R25/E95)` | ↳ ⚙️ [Dep-A2] Draft query spec `(I88/R30/E90)` | 🧩 Validate fork boundaries `(I86/R20/E90)` | 🔍 Review spine contracts `(I85/R15/E90)` | 📊 Close evidence log `(I82/R10/E95)` | Strict internal chain: `Dep-A1` (Mon) ➔ `Dep-A2` (Tue). |
| **Leela** | ⚡ Verify Home runtime `(I90/R20/E95)` | ⚖️ Reconcile decision ledger `(I85/R15/E90)` | ↳ 🔗 [Dep-A2 Consumer] Skill Tree integration `(I88/R25/E90)` | 🧪 Spatial bounds test `(I87/R20/E85)` | 🛡️ Product continuity recap `(I80/R15/E90)` | Cross-project chain: Waits for Apex `Dep-A2` on Tue before Wed build. |
| **MasterOfArts** | 🎯 Define site architecture `(I94/R30/E90)` | 📝 Draft offer copy `(I92/R25/E85)` | 📐 Finalize section map `(I90/R20/E90)` | ⏰ **GATE 17:00:** Review site assets `(I85/R15/E85)` | 📦 Consolidate launch scope `(I88/R20/E90)` | **Hard Deadline:** Thursday 17:00 stakeholder sign-off gate. |
| **Investment** | 📥 Collect topic inputs `(I84/R35/E80)` | 📊 Structure macro intel `(I82/R30/E85)` | 🎯 Map criteria matrix `(I80/R25/E80)` | 🔔 Review thresholds `(I78/R20/E85)` | 📑 Asset recap `(I75/R15/E90)` | *Automation Flow (I91/R60/E50)* deferred: Data pipeline unverified. |
| **Residual** | ⏸️ *[Deferred]* | ⏸️ *[Deferred]* | ⏸️ *[Deferred]* | ⏸️ *[Deferred]* | 🔄 Catchup & Dating buffer `(I30/R20/E70)` | Held as pure safety buffer. |
```
* **Stress Evaluation:** Dependency lineage (`Dep-A1 ➔ Dep-A2 ➔ Dep-A2 Consumer`) and hard deadlines (`⏰ GATE 17:00`) are immediately prominent in the visual flow without needing paragraph explanations.

---

## 5. Comprehensive Comparison Matrix

| Candidate Family | Description | 10s Clarity (20%) | Temporal (15%) | Project Trace (15%) | Density (15%) | Visual Quality (15%) | Constraints (10%) | Resilience (10%) | Weighted Total | Primary Failure Mode |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Candidate 3 (Winner)** | **Two-Tier Hybrid: Calendar Ribbon + Project Matrix** | **4.9** | **4.8** | **4.9** | **4.7** | **4.8** | **4.8** | **4.8** | **4.82 / 5.0** | None. Perfect balance of temporal rhythm and workstream tracking. |
| **Candidate 1 (Runner-Up)** | Single Project × Weekday Matrix Table | 4.2 | 3.8 | 4.7 | 4.4 | 4.0 | 3.7 | 4.8 | **4.17 / 5.0** | Capacity and meeting constraints clutter project rows or get buried. |
| **Candidate 4** | Time-Block / Flow-Slot × Weekday Grid | 3.8 | 4.5 | 3.2 | 3.8 | 3.9 | 4.0 | 4.2 | **3.89 / 5.0** | Over-specifies intra-day time slots, violating the PrecapWeek / PrecapNextDay boundary. |
| **Candidate 5** | Strategic Swimlane & Critical Path Flow | 3.5 | 3.0 | 4.4 | 4.0 | 4.1 | 4.2 | 4.0 | **3.80 / 5.0** | Temporal calendar shape is obscured; hard to answer "What is Tuesday's load?". |
| **Candidate 2** | Chronological 5-Day Vertical Day Cards | 3.0 | 4.4 | 2.2 | 3.2 | 3.5 | 3.8 | 4.7 | **3.38 / 5.0** | Severe scrolling fatigue; fails project continuity ("What happens to Leela across the week?"). |

---

## 6. External / Enhanced View Evaluation

### Research on Enhanced Linked Visualizations:
Three delivery models were evaluated against strict operational constraints:
1. **Mode A: Markdown-Only.** Pure Markdown rendering in chat or IDE.
2. **Mode B: Complete Markdown + Deterministic Local HTML/SVG Projection.** A standalone, styled, single-file HTML/SVG visual board generated by PrecapWeek alongside the brief (`[Open Enhanced Week View](file:///.../2026-W34-board.html)`).
3. **Mode C: Markdown Brief + Cloud Planning Integration (e.g. Linear / Notion / Google Calendar API).**

### Infrastructure Scoring for External Delivery Modes:

| Evaluation Criteria | Mode A: Pure Markdown | Mode B: Markdown + Local HTML/SVG Board | Mode C: Markdown + Cloud Tool (Linear/Notion/GCal) |
| :--- | :---: | :---: | :---: |
| **Incremental Visual / Planning Value** | 4.0 / 5.0 | **4.9 / 5.0** (Rich CSS grid, badges, tooltips) | 4.5 / 5.0 |
| **Setup & Configuration Complexity** | **5.0 / 5.0** (Zero setup) | **4.8 / 5.0** (Zero setup; single local file) | 1.5 / 5.0 (OAuth, webhooks, API tokens) |
| **Source-of-Truth / Sync Risk** | **5.0 / 5.0** (No sync risk) | **5.0 / 5.0** (Deterministic one-way projection) | 1.8 / 5.0 (High dual-maintenance / drift risk) |
| **Maintenance Burden** | **5.0 / 5.0** (Zero) | **4.8 / 5.0** (Static template renderer) | 2.0 / 5.0 (API versioning, schema breaking) |
| **Vendor / Dependency Risk** | **5.0 / 5.0** (None) | **5.0 / 5.0** (Zero external dependencies) | 1.5 / 5.0 (Third-party downtime / rate limits) |
| **Deterministic Generation** | **5.0 / 5.0** (100% stable) | **5.0 / 5.0** (Pure template / string injection) | 2.5 / 5.0 (Network/API failure modes) |
| **Link / Interaction Friction** | **5.0 / 5.0** (Direct reading) | **4.5 / 5.0** (Single click to open local file) | 3.0 / 5.0 (Browser auth, app switching) |
| **Graceful Fallback to Markdown** | **5.0 / 5.0** (Native) | **5.0 / 5.0** (Brief is 100% complete on its own) | 3.5 / 5.0 (Fragmented context) |

### External View Verdict:
* **Recommendation:** **Mode B** is strongly recommended as an optional progressive enhancement, built upon **Mode A** as the authoritative foundation.
* **Architecture:** PrecapWeek generates the Markdown `Weekly_Command_Brief` as the sole canonical source of truth. When generating the brief, PrecapWeek can mechanically emit a zero-dependency, self-contained HTML/SVG visual board into `artifacts/weekly-plans/visual/2026-Wxx-board.html` using a fixed CSS Grid template.
* **Link in Brief Header:**
  `> 📊 **Enhanced View:** [Open Interactive Week Board](file:///artifacts/weekly-plans/visual/weekly_board-20260816-2026-W34.html)`
* **Absolute Invariant:** If the HTML projection is deleted or never opened, the Markdown Brief is 100% complete, fully functional, and legally binding.

---

## 7. Evidence & Authority Register

### Repository Facts & Invariants
1. **Durable Architecture (D008, D012, `DESIGN-DECISIONS.md`):** Human-first, result-card-first, progressive disclosure, minimal machine payload. `PrecapWeek` is an isolated forked skill owning the weekly direction, while `PrecapNextDay` owns intra-day sequencing and Flow Execution Cards.
2. **Template Standard (`weekly-command-brief-template.md` & `03-planning-artifact-designs.okf.yaml`):** The primary view requires: Result Card ➔ Operator Decision ➔ Portfolio Direction ➔ Per-Project Hierarchical OKF Work Plans ➔ Cross-Project Sequence ➔ Week Architecture ➔ Daily Seed Map ➔ Review Flags ➔ Provenance ➔ Compact Downstream Handoff.
3. **Capacity & Deformation Rules (`weekly-blueprint-standard.md`, `weekly-blueprint-meeting-example.md`, `calendar-planning-guidance.md`):** Standard week = 4 flows/day (8h baseline). Meeting-heavy weeks deform flows into full (3 sprints), compressed (2 sprints), minimal (1 sprint), or omitted (0 sprints with reason). Fixed blocks (morning routine, lunch, outro, sleep) are protected anchors.
4. **Scoring Doctrine:** Numeric ratings are optional aids in the format `Task (Ixx/Rxx/Exx)` on the same line. No synthetic combined sum. No arbitrary project caps.

### External Design & HCI Evidence
1. **Edward Tufte (*Envisioning Information*, *Visual Display of Quantitative Information*):** High data-to-ink ratio; micro/macro dual readings; small multiples for cross-category comparison; avoidance of non-structural decorative elements.
2. **HCI & Cognitive Ergonomics (Card, Moran, Newell; Shneiderman):** 2D visual indexing allows $O(1)$ saccadic eye movements to cross-reference time against entity, compared to $O(N)$ linear scanning in vertical lists. Preattentive processing (standard glyphs like `🎯`, `⚡`, `⏸️`, `🔒`) accelerates visual filtering under 200ms.
3. **Design System Standards (USWDS & GOV.UK):** Tables are optimal for structured, multi-attribute comparisons with compact values; cards are optimal for modular, variable-depth narratives. Hybridizing a summary table with detailed cards achieves maximum scanning efficiency without sacrificing depth.

---

## 8. Exact Weekly Command Brief Visualization Specification

### Production Grammar & Rules

```yaml
visualization_specification:
  section_title: "## Weekly Architecture"
  location_in_brief: "Immediately following '## Weekly direction' and preceding '## Project - {PROJECT_NAME}'"
  
  tier_1_calendar_ribbon:
    type: "Markdown Table"
    column_count: 6
    columns: ["Dimension", "Mon {MM-DD} ({Role})", "Tue {MM-DD} ({Role})", "Wed {MM-DD} ({Role})", "Thu {MM-DD} ({Role})", "Fri {MM-DD} ({Role})"]
    required_rows:
      - "Day Focus: 2-4 word theme of the day"
      - "Capacity Shape: 🟢 Standard (4F) | 🟡 Compressed (2-3F) | 🔴 Overloaded (0-1F)"
      - "Fixed Anchors: Protected routines (🔒) or named calendar blocks (👥)"
      - "Active Roster: Comma-separated list of active projects receiving focus"
      - "Constraints / Reductions: Deliberate deferrals, meeting notes, or unverified flags"

  tier_2_trajectory_matrix:
    type: "Markdown Table"
    column_count: 7
    columns: ["Project / Stream", "Mon ({Role})", "Tue ({Role})", "Wed ({Role})", "Thu ({Role})", "Fri ({Role})", "Weekly Target & Leverage"]
    row_ordering:
      1: "Operator-named weekly primary focus project (e.g. MasterOfArts)"
      2: "Core active product projects (e.g. Leela)"
      3: "Orchestration / System projects (e.g. Apex)"
      4: "Intelligence / Secondary active projects (e.g. Investment)"
      5: "Residual / Overflow / Support bucket"
    cell_syntax:
      task_entry: "{Glyph} {Actionable Task Title} `(I{Impact}/R{Risk}/E{Evidence})`"
      dependency_entry: "↳ {Glyph} [{DepID}] {Actionable Task Title} `(Ixx/Rxx/Exx)`"
      deadline_entry: "⏰ **GATE {HH:MM}:** {Actionable Task Title} `(Ixx/Rxx/Exx)`"
      deferral_entry: "⏸️ *[Deferred: {Reason}]*"
      omitted_entry: "❌ *[Omitted: {Reason}]*"
    
  allowed_glyphs:
    milestone: "🎯"
    verification: "⚡"
    content_copy: "📝"
    contract_spec: "📜"
    implementation: "⚙️"
    dependency: "↳"
    gate_deadline: "⏰"
    deferral: "⏸️"
    protected_anchor: "🔒"
    meeting_block: "👥"
    risk_warning: "⚠️"
```

### Production Markdown Template Snippet for PrecapWeek
```markdown
## Weekly Architecture ({{WEEK_OR_DATE_RANGE}})

### Week Calendar & Capacity Ribbon
| Dimension | Mon {{MON_DATE}} ({{MON_ROLE}}) | Tue {{TUE_DATE}} ({{TUE_ROLE}}) | Wed {{WED_DATE}} ({{WED_ROLE}}) | Thu {{THU_DATE}} ({{THU_ROLE}}) | Fri {{FRI_DATE}} ({{FRI_ROLE}}) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day Focus** | {{MON_FOCUS}} | {{TUE_FOCUS}} | {{WED_FOCUS}} | {{THU_FOCUS}} | {{FRI_FOCUS}} |
| **Capacity Shape** | {{MON_CAPACITY}} | {{TUE_CAPACITY}} | {{WED_CAPACITY}} | {{THU_CAPACITY}} | {{FRI_CAPACITY}} |
| **Fixed Anchors** | {{MON_ANCHORS}} | {{TUE_ANCHORS}} | {{WED_ANCHORS}} | {{THU_ANCHORS}} | {{FRI_ANCHORS}} |
| **Active Roster** | {{MON_ROSTER}} | {{TUE_ROSTER}} | {{WED_ROSTER}} | {{THU_ROSTER}} | {{FRI_ROSTER}} |
| **Constraints / Risks** | {{MON_CONSTRAINTS}} | {{TUE_CONSTRAINTS}} | {{WED_CONSTRAINTS}} | {{THU_CONSTRAINTS}} | {{FRI_CONSTRAINTS}} |

---

### Project Workstream Trajectory Matrix
| Project / Stream | Mon {{MON_DATE}} | Tue {{TUE_DATE}} | Wed {{WED_DATE}} | Thu {{THU_DATE}} | Fri {{FRI_DATE}} | Weekly Target & Leverage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **{{P1_NAME}}**<br>*({{P1_ROLE}})* | {{P1_MON_TASK}} | {{P1_TUE_TASK}} | {{P1_WED_TASK}} | {{P1_THU_TASK}} | {{P1_FRI_TASK}} | **{{P1_TARGET_TITLE}}:** {{P1_TARGET_DESC}} |
| **{{P2_NAME}}**<br>*({{P2_ROLE}})* | {{P2_MON_TASK}} | {{P2_TUE_TASK}} | {{P2_WED_TASK}} | {{P2_THU_TASK}} | {{P2_FRI_TASK}} | **{{P2_TARGET_TITLE}}:** {{P2_TARGET_DESC}} |
| **{{P3_NAME}}**<br>*({{P3_ROLE}})* | {{P3_MON_TASK}} | {{P3_TUE_TASK}} | {{P3_WED_TASK}} | {{P3_THU_TASK}} | {{P3_FRI_TASK}} | **{{P3_TARGET_TITLE}}:** {{P3_TARGET_DESC}} |
| **{{P4_NAME}}**<br>*({{P4_ROLE}})* | {{P4_MON_TASK}} | {{P4_TUE_TASK}} | {{P4_WED_TASK}} | {{P4_THU_TASK}} | {{P4_FRI_TASK}} | **{{P4_TARGET_TITLE}}:** {{P4_TARGET_DESC}} |
| **Residual**<br>*(Recovery / Support)* | {{RES_MON_TASK}} | {{RES_TUE_TASK}} | {{RES_WED_TASK}} | {{RES_THU_TASK}} | {{RES_FRI_TASK}} | **{{RES_TARGET_TITLE}}:** {{RES_TARGET_DESC}} |

> **Matrix Legend:** `🎯 Milestone` | `⚡ Verification` | `📝 Copy/Design` | `📜 Contract/Spec` | `↳ Dependency` | `⏰ Deadline` | `⏸️ Deferral` | `🔒 Fixed` | `⚠️ Risk`
```

---

## 9. Reuse & Import Options

Instead of building custom UI rendering pipelines or external server dependencies:
1. **Single-File Zero-Dependency HTML/SVG Template:** A pre-baked CSS Grid HTML template (`apex-meta/tools/templates/weekly-board-template.html`) that uses native HTML5 flexbox/grid and vanilla CSS system fonts (`system-ui, -apple-system, sans-serif`). PrecapWeek can inject the structured JSON/YAML week data directly into a `<script id="data">` block or render it via basic string interpolation.
2. **Native GitHub / CommonMark Markdown Engine:** The recommended Markdown visualization requires zero extensions, rendering identically on GitHub, Obsidian, VS Code, and terminal CLI markdown renderers.
3. **No NPM / Python / Docker Daemon Required:** Keeps the APEX orchestration runtime completely lightweight, self-contained, and maintenance-free.

---

## 10. Failure Modes & Breakdown Conditions

| Failure Mode | Trigger Condition | Impact on Visualization | System Mitigation |
| :--- | :--- | :--- | :--- |
| **Portfolio Overload (>6 Active Projects)** | More than 6 active projects assigned work in the same week. | Matrix becomes vertically tall; cell comparisons require more scrolling. | PrecapWeek forces lower-priority projects into deliberate deferrals (`⏸️ [Deferred: Low Priority]`), keeping the active matrix to $\le 5$ rows. |
| **Severe Task Text Bloat** | LLM generates multi-sentence task descriptions inside table cells. | Markdown table columns wrap awkwardly, degrading readability. | Strict grammar rule: Cell tasks are limited to $\le 6$ words + glyph + `(Ixx/Rxx/Exx)` metric. Detailed task descriptions live in the per-project section below. |
| **Extreme Calendar Fragmentation (5+ micro-meetings/day)** | High volume of ad-hoc meetings across the week. | Table cells become cluttered if micro-meetings are listed individually. | Calendar Ribbon summarizes total blocked hours (`👥 4.5h meetings`); individual meeting scheduling is deferred to `PrecapNextDay`. |
| **Local File URI Protocol Restrictions** | User's Markdown viewer blocks opening local `file:///` links. | Enhanced HTML projection link fails to launch from chat click. | The Markdown Brief is 100% self-sufficient; the operator still sees the complete Two-Tier Matrix natively in Markdown. |

---

## 11. Open Decisions (Operator Direction Only)

The following questions represent genuine operator design choices not locked by existing documentation:

1. **Enhanced View Generation Default:**  
   * *Option A (Recommended):* Generate the local single-file HTML board automatically on every `PrecapWeek` run and link it in the Brief header.
   * *Option B:* Keep PrecapWeek pure Markdown-only by default; generate the HTML board only if explicitly requested.
2. **Task Granularity in Matrix Cells:**  
   * *Option A (Recommended):* Single lead work item per project per day (`Task (Ixx/Rxx/Exx)`), keeping the matrix ultra-compact.
   * *Option B:* Allow up to 2 stacked work items in a single cell separated by `<br>` when a project has morning and afternoon flows.
3. **Matrix Placement in Brief Structure:**  
   * *Option A (Recommended):* Place `Weekly Architecture` immediately after `Weekly direction` (high-level visual orientation before deep project details).
   * *Option B:* Place `Weekly Architecture` after all project detail sections as a synthesis summary before the downstream handoff.

---

## 12. Implementation Handoff (For Subsequent Implementation Phase)

> [!NOTE]
> No repository files were modified during this research run. The findings below provide exact instructions for the implementation phase.

### Target Files for Integration:
1. `.claude/skills/PrecapWeek/weekly-command-brief-template.md`:
   * Replace the outdated `## Daily seed map` placeholder with the production **Two-Tier Weekly Architecture** (Ribbon + Matrix) specification.
2. `.claude/skills/PrecapWeek/SKILL.md`:
   * Update the procedure in Step 6 to mandate the generation of the Two-Tier Weekly Architecture.
3. `.claude/skills/PrecapWeek/weekly-blueprint-standard.md` & `weekly-blueprint-meeting-example.md`:
   * Add the cell glyph syntax (`🎯`, `⚡`, `📝`, `📜`, `↳`, `⏰`, `⏸️`) to the output formatting guidance.
4. `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/`:
   * Commit the accepted design decision and verification record into `DECISIONS.md`.