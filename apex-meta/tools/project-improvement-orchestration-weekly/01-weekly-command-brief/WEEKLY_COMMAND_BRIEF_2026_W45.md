---
type: command_brief
id: WEEKLY-COMMAND-BRIEF-2026-W45-NORTHSTAR
title: Weekly Command Brief — 2026-W45 (Northstar Live Architecture)
description: Canonical production Weekly Command Brief for 2026-W45 in the Northstar design, integrating live OpenProject work packages, live Google Calendar events (gehm77@gmail.com), 4-flow daily 3x3 repetition, and reconciled calendar schedule.
status: approved
tags: [weekly-orchestration, precap-week, command-brief, w45-2026, northstar-design, calendar-view, critical-path, openproject-intake, google-calendar-live]
---

# Weekly Command Brief — 2026-W45

> **Weekly State:** `APPROVED_FOR_EXECUTION`  
> **Cadence:** Monday Nov 9 – Saturday Nov 14, 2026 (Sunday Nov 15 OFF per Decision D017).  
> **Design Pattern:** Design 01 — *Northstar* (Portfolio Strategy Canvas & Progressive Drilldown Cards).  
> **Domain Distribution:** 2 Flows Master of Arts (Website, Content Production, Invoicing), 1 Flow Investment / IPOS, 1 Residual Flow (Apartment & Art, Sexy Content, Community & Traveling).  
> **Integration Engine:** Sequencing system (holistic life/work, habits, daily cadence, flow cards).  
> **Google Calendar Status:** Live connection verified (`gehm77@gmail.com`); real events reconciled into timeline.  
> **OpenProject Connectivity:** Live instance `http://127.0.0.1:8083` reconciled.

---

## 1. Portfolio Compass & Live Calendar Verification

```
╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║                                     PORTFOLIO COMPASS                                     ║
╠══════════════════════════════╦══════════════════════════════╦═════════════════════════════╣
║ 04 Active Fronts             ║ 04 Flows / Day (3x3 Standard)║ Verified Google Calendar    ║
║ • Master of Arts (Web/Biz)   ║ • F1: MoA Content Production ║ • Thu 10:00 Alex & Chris    ║
║ • Investment / IPOS          ║ • F2: MoA Website & Invoicing║ • Thu 18:45 München Tanz   ║
║ • Sequencing Meta-System     ║ • F3: Investment / IPOS      ║ • Wed 18:00 WC Meister      ║
║ • Residual Life & Art Flow   ║ • F4: Residual (Art/Sex/Com) ║ • Fri 18:00 WC Meister      ║
╚══════════════════════════════╩══════════════════════════════╩═════════════════════════════╝
```

### Live Calendar Verification Receipt:
- **Authenticated Account:** `gehm77@gmail.com` via `gcalendar` CLI.
- **Fixed External Commitments Reconciled (Non-Destructive Invariant):**
  - • **Thursday Nov 12, 10:00–11:00:** `Alex & Chris` (Meeting with Christian Sgarz). Protected; F1 compressed to 09:00–10:00.
  - • **Thursday Nov 12, 18:45–21:00:** `München Tanz`. Protected; shutdown completes at 18:15.
  - • **Wednesday Nov 11, 18:00–20:00:** `WC Meister`. Protected; shutdown completes at 17:45.
  - • **Friday Nov 13, 18:00–20:00:** `WC Meister`. Protected; weekly wrap completes at 17:45.
  - • **All-Day Markers:** Nov 9 Christoph Wallraff Geburtstag; Nov 12 Serena Geb.

---

## 2. 01 · Proposed Attention Order (Northstar Priority Candidates)

### Candidate 01: [OP #16: WP #224] ADR-003: Formalize Karakeep Retirement & Code Deprecation
- **Native State:** `In progress` `(P0 | I95/E40/R10: 85)` **[CRITICAL PATH]**
- **Project:** Investment / IPOS (#16)
- **Why Now:** Deprecated Karakeep import mocks block clean integration of IBM Docling and Trafilatura adapters.
- **Proposed Slice:** Audit `ipos/ingest/`, purge legacy references, and lock ADR-003 architectural decision record.
- **Acceptance & Proof:** Zero Karakeep imports remaining; clean pytest execution on ingest stubs.
- **Unblocks:** WP #226 (Docling & Trafilatura Ingestion Adapter).

### Candidate 02: [OP #16: WP #226] RI-11: Implement IBM Docling & Trafilatura Ingestion Adapter
- **Native State:** `New` `(P0 | I94/E85/R20: 76)` **[CRITICAL PATH]**
- **Project:** Investment / IPOS (#16)
- **Why Now:** Financial research memo ingestion currently lacks structured multi-page PDF extraction and web article cleansing.
- **Proposed Slice:** Build Docling PDF extraction adapter and wire Trafilatura text parser to emit sovereign research JSON.
- **Acceptance & Proof:** Sample PDF extracted into clean structured JSON; Trafilatura cleans article boilerplate.
- **Unblocks:** WP #233 (End-to-End Pipeline Test Harness).

### Candidate 03: [OP #14: WP #163] Content Transformation & Website Flexbox Navigation
- **Native State:** `New` `(P1 | I90/E80/R15: 75)`
- **Project:** Master of Arts Website (#14)
- **Why Now:** Outdated navigation bar blocks clean public presentation of creative essays and media assets.
- **Proposed Slice:** Refactor CSS header with modern flexbox, build responsive mobile drawer, and wire dynamic markdown router.
- **Acceptance & Proof:** Mobile slide-out drawer renders smoothly across tablet and phone breakpoints; Lighthouse audit passes.

### Candidate 04: [OP #7: WP-BIZ-01] Business Invoicing Schema & Automated PDF Generator
- **Native State:** `Proposed` `(P1 | I94/E85/R15: 80)` **[CRITICAL PATH]**
- **Project:** Master of Arts Business (#7)
- **Why Now:** Billing calculations and client invoices are currently handled manually without unit tests or schema validation.
- **Proposed Slice:** Define line-item JSON schema, write tax formula recalculation tests, and build HTML-to-PDF template generator.
- **Acceptance & Proof:** Unit tests pass across zero-discount and tax edge cases; sample PDF invoice generated.

---

## 3. 02 · Layered Project Landscape (Progressive Drilldown Cards)

### 📁 Project: Master of Arts (Website, Content & Invoicing)
*OpenProject: Projects #14 (Website), #6 (Content), #7 (Business)*

- **Strategic Outcome:** Deploy responsive navigation flexbox; launch weekly creative essay and narration publishing pipeline; implement automated invoice billing engine.
- **Baseline State:** Website layout is outdated; content drafting lacks systematic audio/reel slicing; billing is calculated manually.
- **Process Flow:** `Flexbox Navigation` ➔ `Content Production Pipeline` ➔ `Invoice Schema & Tax Tests` ➔ `PDF Billing Release`
- **Evolution Commentary:**
  - *"This is there now":* Fragmented draft notes and manual billing calculations.
  - *"This goes where":* Production website build, published audio/written media, and compliant PDF billing records.

#### Epics & Work Packages:
1. **Epic: Website Modernization (Project #14)**
   - `WP #163 Content Transformation & Flexbox Nav` `[In progress]`: CSS flexbox header, responsive drawer, mobile layout.
2. **Epic: Content Production Pipeline (Project #6)**
   - `Creative Essays & Spoken Narration` `[Active]`: Thesis outlines, audio voiceover mastering, short reel media.
3. **Epic: Business & Invoicing Engine (Project #7)**
   - `Automated PDF Invoicing` `[Active]`: Line-item schema, tax unit tests, print stylesheet, batch generator.
4. **Project Backlog / Longlist:**
   - `[WP #204] ACIM Secular Credits Page`: Preserved in project record; unlinked from this week's active focus per operator priority.
   - `Stripe Webhook Integration`: Staged for future billing wave.

---

### 📁 Project: Investment / IPOS (Research Intake & Evidence Pipeline)
*OpenProject: Project #16*

- **Strategic Outcome:** Formalize Karakeep retirement (ADR-003); deploy Docling PDF and Trafilatura web intake adapters; verify reliability via reality validation test harness.
- **Baseline State:** Legacy Karakeep mocks remain in repository; upstream ingestion suffers timeouts; research intake lacks unified JSON evidence receipts.
- **Process Flow:** `[WP#224] Karakeep Deprecation` ➔ `[WP#226] Docling Ingestion` ➔ `[WP#233] Intake Harness` ➔ `[WP#232] Cockpit Dashboard`

#### Epics & Work Packages:
1. **Epic: Intake Debt Elimination & Adapters**
   - `[WP #224] ADR-003: Karakeep Retirement` `[In progress]`: Purge legacy mocks, lock decision record.
   - `[WP #226] RI-11: Docling & Trafilatura Ingestion Adapter` `[New]`: PDF and web extraction pipeline.
2. **Epic: Reality Validation & Operator Interface**
   - `[WP #233] RI-15: Ingestion Pipeline Test Harness` `[New]`: Backoff retry, timeout recovery, evidence receipt.
   - `[WP #232] RI-14: Cockpit UX Multi-Tier Dashboard` `[In specification]`: Live query views for research intake.
   - `[WP #227] Mission 2: Telegram Digest Dispatch` `[New]`: Weekly research summary payload verification.

---

### 📁 Project: Sequencing (Integration Meta-System)
*OpenProject: Project #11*

- **Strategic Outcome:** Organize holistic life/work balance, habits, meditation anchors, and daily flow cards (3x3 standard).
- **Epics:**
  - `[WP #215 / #216] Wave A Domain & Daily Flow Cards`: Govern the 4 daily flows and protect routine anchors.

---

### 📁 Project: Residual Integration Flow (Life, Art & Community)

- **Strategic Outcome:** Maintain life-art equilibrium across living space, creative aesthetics, and peer/travel networks.
- **Daily 3x3 Sprints:**
  - `Sprint 1: Apartment & Art`: Workspace acoustic tuning, physical studio organization, canvas prep.
  - `Sprint 2: Sexy Content`: Aesthetic lighting setup, photoshoot execution, high-tier photo color grading.
  - `Sprint 3: Community & Traveling`: Peer connection outreach, travel logistics, route and itinerary planning.

---

## 4. Matrix 2: Reconciled Timeline & Real Calendar Schedule

This schedule reconciles the 4 daily flows (3x3 standard) with verified live Google Calendar commitments:

| Time Window | Block Type | Monday (Nov 9) | Tuesday (Nov 10) | Wednesday (Nov 11) | Thursday (Nov 12) | Friday (Nov 13) | Saturday (Nov 14) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **08:00 – 09:00** | 🔒 **Protected Anchor** | **Morning Setup**<br>• Meditation & breathwork<br>• Calendar verify<br>• Day kickoff | **Morning Setup**<br>• Meditation & breathwork<br>• Calendar verify<br>• Day kickoff | **Morning Setup**<br>• Meditation & breathwork<br>• Calendar verify<br>• Day kickoff | **Morning Setup**<br>• Meditation & breathwork<br>• Calendar verify<br>• Day kickoff | **Morning Setup**<br>• Meditation & breathwork<br>• Calendar verify<br>• Day kickoff | **Morning Setup**<br>• Reflection<br>• Week review prep |
| **09:00 – 10:45** | ⚡ **Flow 1**<br>*MoA Content* | **MoA: Essay Pipeline**<br>1. Outline thesis essay<br>2. Reconcile key concepts<br>3. Record spoken audio<br>• Buffer (10:30–10:45) | **MoA: Reel Slicing**<br>1. Cut short reel clips<br>2. Sync audio waveforms<br>3. Format captions<br>• Buffer (10:30–10:45) | **MoA: Longform Writing**<br>1. Deep dive essay draft<br>2. Structure sections<br>3. Editorial polish<br>• Buffer (10:30–10:45) | **MoA: Audio Narration**<br>*(09:00–10:00 Compressed)*<br>1. Narrative voiceover<br>2. Balance audio mix<br>3. Master export | **MoA: Newsletter**<br>1. Synthesis newsletter<br>2. Email draft build<br>3. Broadcast release<br>• Buffer (10:30–10:45) | **Weekly Precap (D017)**<br>*(09:00–11:00)*<br>1. Audit week evidence<br>2. Scan OpenProject WPs<br>3. Draft W46 brief |
| **10:00 – 11:00** | 📅 **Fixed Calendar Event** | — | — | — | 🔒 **Alex & Chris**<br>*(Google Calendar Meeting)* | — | *(Precap continues)* |
| **10:45 – 11:15** | ☕ **Buffer / Transition** | ☕ Break & walk | ☕ Break & walk | ☕ Break & walk | ☕ Break & walk | ☕ Break & walk | ☕ Transition break |
| **11:15 – 12:30** | ⚡ **Flow 2**<br>*MoA Website & Biz* | **MoA: Nav Bar Flexbox**<br>1. CSS flexbox header<br>2. Mobile drawer layout<br>3. Staging deploy pass | **MoA: Content Engine**<br>1. Dynamic markdown feed<br>2. Responsive article view<br>3. Internal link validation | **MoA: Invoicing Schema**<br>1. Invoice JSON schema<br>2. Tax unit tests<br>3. Accounting path wire | **MoA: PDF Billing Engine**<br>1. HTML invoice template<br>2. Print stylesheet<br>3. PDF rendering engine | **MoA: Release Smoke**<br>1. Batch invoice run<br>2. Production build pass<br>3. Live release signoff | **Clean Room & Buffer**<br>• Workspace reset<br>• Documentation sync<br>*(11:30–13:00)* |
| **12:30 – 13:30** | 🔒 **Protected Anchor** | **Midday Reset & Lunch** | **Midday Reset & Lunch** | **Midday Reset & Lunch** | **Midday Reset & Lunch** | **Midday Reset & Lunch** | Lunch break |
| **13:30 – 15:30** | ⚡ **Flow 3**<br>*Investment / IPOS* | **IPOS: Karakeep & Docling**<br>1. Audit Karakeep refs<br>2. Lock ADR-003 record<br>3. Build Docling adapter | **IPOS: Ingest Pipeline**<br>1. Trafilatura text clean<br>2. FRED schema mapping<br>3. Batch runner script | **IPOS: Reality Validation**<br>1. Sample memo ingest<br>2. Backoff retry check<br>3. Write WP #233 proof | **IPOS: Cockpit Dashboard**<br>1. Cockpit UX wireframe<br>2. Live query view wire<br>3. Dashboard test pass | **IPOS: Telegram Digest**<br>1. Telegram export script<br>2. Dry-run test payload<br>3. Mission 2 signoff | **Afternoon OFF**<br>• Personal restoration |
| **15:30 – 16:00** | ☕ **Buffer / Transition** | ☕ Break & fresh air | ☕ Break & fresh air | ☕ Break & fresh air | ☕ Break & fresh air | ☕ Break & fresh air | Rest |
| **16:00 – 17:30 / 45**| ⚡ **Flow 4**<br>*Residual Flow (3x3)* | **Residual Flow**<br>• S1: Workspace tune<br>• S2: Aesthetic photoshoot<br>• S3: Peer network sync | **Residual Flow**<br>• S1: Studio refinement<br>• S2: Visual narrative edit<br>• S3: Travel itinerary sync | **Residual Flow (16:00–17:30)**<br>• S1: Physical art session<br>• S2: Brand visual draft<br>• S3: Shared project sync | **Residual Flow (16:00–17:30)**<br>• S1: Artwork varnish/finish<br>• S2: Portfolio export<br>• S3: Travel schedule lock | **Residual Flow (16:00–17:30)**<br>• S1: Studio clean reset<br>• S2: Weekly brand archive<br>• S3: Weekend plan confirm | **OFF** |
| **17:30 – 18:00** | 🔒 **Shutdown / Transition**| Daily recap notes | Daily recap notes | 🔒 **Shutdown before event** | 🔒 **Shutdown & dance prep** | 🔒 **Weekly Wrap Shutdown** | Rest |
| **18:00 – 21:00** | 📅 **Fixed Calendar Events** | — | — | 🔒 **18:00–20:00 WC Meister**<br>*(Google Calendar Event)* | 🔒 **18:45–21:00 München Tanz**<br>*(Google Calendar Event)* | 🔒 **18:00–20:00 WC Meister**<br>*(Google Calendar Event)* | **OFF** |
| **Night** | 🔒 **Protected Rest** | Evening rest | Evening rest | Evening rest | Evening rest | Evening rest | **OFF** |

---

## 5. Downstream Execution Handoff (PrecapNextDay Intake)

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_COMMAND_BRIEF_2026_W45.md"
  google_calendar_account: "gehm77@gmail.com"
  calendar_export_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/calendar-export/2026-W45-flows.ics"
  week: "2026-W45"
  result_state: "APPROVED_FOR_EXECUTION"
  weekly_intent: "Execute MoA website flexbox and invoice generation engine, retire Karakeep in IPOS and build Docling/Trafilatura intake pipeline, and maintain daily 3x3 residual life/art flows around verified Google Calendar events."
  integration_system: "Sequencing"
  daily_flow_budget: 4
  flow_repetition_standard: "3x3"
  reconciled_calendar_constraints:
    wednesday_evening: "18:00-20:00 WC Meister"
    thursday_morning: "10:00-11:00 Alex & Chris"
    thursday_evening: "18:45-21:00 München Tanz"
    friday_evening: "18:00-20:00 WC Meister"
  next_consumer: "PrecapNextDay"
  next_target_day: "Monday"
```
