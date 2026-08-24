# Standardized Weekly Multi-Domain Orchestration Blueprint

## 1. Operating Model Overview
The Apex AIOS weekly orchestration workflow operates across a recurring Monday-to-Friday execution cycle governed by the 5-week progressive simulation trajectory and daily morning flow recaps.

### Cadence Matrix
- **Sunday Evening (Pre-Cap):** Review prior week milestone gates, lock incoming sprint themes, seed task backlogs.
- **Monday – Thursday (Daily Execution):**
  - `08:00 – 08:30`: Morning Flow Recap & Task Lock (`monday_flow_recap.md`, etc.).
  - `08:30 – 17:00`: Core Production Blocks (Deep Work, Execution, Verification).
  - `17:00 – 17:30`: Next-Day Plan & Milestone Buffer (`monday_next_day_plan.md`, etc.).
- **Friday (Milestone Sign-Off):** Milestone gate verification (`G1`–`G5`), git freeze, automated systemd portfolio rollup verification.

## 2. Milestone Gates Reference
- **Gate G1 (SSoT Lock):** Single source of truth frozen; zero duplicate or orphan documents.
- **Gate G2 (Curriculum & Product Lock):** Learning outcomes, course arcs, and deliverables locked to G1 sources.
- **Gate G3 (Financial Infrastructure Lock):** Invoicing, bookkeeping SOPs, and cashflow monitors active.
- **Gate G4 (Content & Distribution Lock):** Content calendars, campaign assets, and pitch decks aligned with verified offers.
- **Gate G5 (Web Integration & Compounding Learnings):** System integration, cross-portfolio retrospectives, and learned skill promotions.

## 3. Related Systems & Artifacts
- **Simulation Suite:** `apex-meta/orchestration/simulations/5-week-progressive-simulation/`
- **Selection & MCDA:** `apex-meta/orchestration/mcda-evaluation/`
- **Daily Systemd Rollup:** `apex-portfolio-rollup.timer` / `scripts/hermes/apex_portfolio_rollup.py`
