# Week 3 — Financial Infrastructure, Invoicing & Bookkeeping SOPs

```
week_theme: financial_infrastructure_invoicing_bookkeeping_sops
primary_projects: [Investment, Business]
secondary_projects: [MasterOfArts_meta]
entry_input: Week-02 handoff seed (offers ready for pricing, cost drivers, validation questions)
exit_gate: G3_Financial_Spine_Live
blueprint_basis: weekly-blueprint-standard.md
project_flow_priority_applied: operator-priority override recorded D-031 — Investment & Business elevated; reason: gate dependency
constraint: NO real transactions executed during simulation — SOPs, templates, and dry-run data only. Confidential/financial handling per privacy policy.
time_precision: 15-minute internal precision, block-level human output
```

## Week Outcome Statement

By Friday, the Business family has an operational invoice template with a
numbering scheme under `Business/Invoices`, a monthly-close bookkeeping SOP
with category taxonomy and receipt workflow, pricing sheets for the W2
curricula reconciled against `Business/Offers`, and a 13-week rolling cash-flow
projection v1 that passes arithmetic verification.

## Daily Block Breakdown

### Monday — Ledger Foundations

- **Morning routine** (fixed): standard + review W2 handoff seed.
- **work_flow_1 (Investment)**: Audit current financial surface: inventory
  `Business/Invoices/`, `Business/Offers/`, `Business/Legal/`,
  `Business/Registration/`. Output: `Business/financial-inventory.md`.
- **work_flow_2 (Investment)**: Define chart-of-accounts-lite: revenue
  categories (workshops, therapy-adjacent offerings, content, other) and expense
  categories mapped to real cost drivers from W2 seed.
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: Decision log D-031 (priority override), D-032 (category taxonomy v1); Kanban G3 tasks seeded.
- **work_flow_3 (Business)**: Invoice template design: mandatory fields,
  VAT/tax placeholders, payment terms, numbering scheme
  (`YYYY-FAMILY-SEQ`), credit-note variant. Save as `Business/Invoices/templates/invoice-template-v1.md`.
- **work_flow_4 (MasterOfArts meta)**: Check Orchestration governance docs need no finance-side amendments; note findings.
- **Evening**: physical block preserved.
- **day_outro / sleep_routine** (fixed).

### Tuesday — Invoicing SOP

- **Morning routine** (fixed): standard.
- **work_flow_1 (Business)**: Write invoicing SOP: trigger events (booking,
  milestone, delivery), issuance steps, dunning ladder (day 0/7/14/30),
  reconciliation into ledger, archiving rule pointing at SSoT index pattern from W1.
- **work_flow_2 (Business)**: Dry-run: generate 3 fictional invoices through the
  full SOP path (marked SIMULATION-DATA, never sent). Verify numbering, template fill, archive placement.
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: One-block sweep; finance questions routed to tasks not done inline.
- **work_flow_3 (Investment)**: Bookkeeping SOP part 1 — receipt capture
  workflow (where receipts land, naming convention, weekly triage slot in admin blocks).
- **work_flow_4 (Business/Legal)**: Cross-check invoice terms against
  `Business/Legal/` and registration constraints; flag gaps for operator review (do NOT self-authorize legal changes).
- **Evening**: social/evening preserved.
- **day_outro / sleep_routine** (fixed).

### Wednesday — Pricing Reconciliation

- **Morning routine** (fixed): standard + energy check (judgment-heavy day).
- **work_flow_1**: Answer W2 validation questions that bear on pricing;
  unresolved ones become explicit assumptions recorded in the pricing sheet header.
- **work_flow_2 (Business/Offers)**: Build pricing sheets for Dance Fusion and
  Awakening curricula: tier options (drop-in / series / early-bird), cost-floor
  calculation from W2 cost drivers, margin targets. Save to `Business/Offers/pricing-W2-curricula.md`.
- **lunch_prep / lunch_break** (fixed): protected.
- **work_flow_3 (Business/Offers)**: Reconcile existing offers in
  `Business/Offers/` with new pricing logic; mark conflicts; log decisions D-033…D-038.
- **admin_or_2Do**: Decision log updates; stale Kanban prune.
- **work_flow_4 (Investment)**: Bookkeeping SOP part 2 — monthly close
  checklist: cut-off date, categorization sweep, reconciliation steps, report outputs, sign-off line.
- **Evening**: recovery-weighted evening after judgment-heavy day.
- **day_outro / sleep_routine** (fixed).

### Thursday — Cash-Flow Projection v1

- **Morning routine** (fixed): standard.
- **work_flow_1 (Investment)**: Build 13-week rolling cash-flow projection v1:
  known fixed costs, scenario-based revenue lines (conservative/base/optimistic)
  derived from Wednesday's pricing sheets. Save to `Business/cashflow-projection-v1.md`.
- **work_flow_2**: Arithmetic verification pass — recompute totals independently
  (script or by-hand second pass); every figure must reconcile to a source cell.
  Auditor persona demands this evidence.
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: QMD refresh for Business index; decision log updates.
- **work_flow_3**: Persona stress-test round 3 — The Auditor traces every
  number to source; The Skeptic challenges optimistic scenarios (see persona section).
- **work_flow_4 (Residual)**: Overflow capture if stress-test remediation is light.
- **Evening**: physical/social preserved.
- **day_outro / sleep_routine** (fixed).

### Friday — Gate Review & Handoff Seed

- **Morning routine** (fixed): standard + gate G3 checklist review.
- **work_flow_1**: Gate G3 execution — walk all four checklist items with evidence paths.
- **work_flow_2 (Business)**: Final consistency pass: invoice template ↔ SOP ↔
  taxonomy ↔ projection all reference the same categories and terms.
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: Decision log finalize (target ≥45 cumulative); Kanban sweep.
- **work_flow_3**: Handoff seed for Week 4: approved price points usable in
  decks/calendars, brand claims cleared vs marketing overclaim rules, asset
  list available for content repurposing. Save to `Week-03/handoff-to-week-04.md`.
- **work_flow_4 (MasterOfArts meta)**: Confirm W4 calendar plan can cite prices
  without violating the "no unsupported numbers" rule.
- **Evening**: light social/evening; week-close reflection ≤10 min.
- **day_outro / sleep_routine** (fixed). Sunday precap prepares Week 4.

## Conflict Handling Applied This Week

| Situation | Response per blueprint |
|---|---|
| Legal gap found beyond agent authority | Flagged for operator review; no self-directed legal edits |
| Projection work threatened evening block | Deferred overflow to Thursday work_flow_4, evening preserved |
| Residual items competing with fixed project work | Kept lowest; single residual block granted |

## Persona Stress Tests (W3)

- **The Auditor**: every projection figure traced to a source cell; dry-run invoices marked SIMULATION-DATA; satisfied.
- **The Operator**: flagged that pricing decisions consume more emotional energy than expected → mitigation: decision caps (max 5 pricing decisions/day) and pre-committed default tiers.
- **The Skeptic**: optimistic revenue scenario assumed full cohorts → added third assumption line requiring named demand evidence before upgrade.
- **The Integrator**: taxonomy risked diverging from future web-store categories → taxonomy v1 written with forward-compatible slugs for W5 integration.

## Exit Criteria (Gate G3)

All four G3 checkboxes evidenced; projection arithmetically verified; dry-run
invoices archived correctly; handoff seed written; no real transactions executed.
