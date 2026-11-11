## Purpose

```yaml
purpose:
  file_role: operator_weekly_command_brief_intake_contract
  stage: Stage_1A_Pre_Run_Operator_Intake
  downstream_compiler: PrecapWeek
  owns:
    - operator_weekly_command_brief_schema
    - adaptive_hybrid_qa_rules
    - six_portfolio_focus_override_rules
    - new_vs_standard_vs_ongoing_routing
  goal: >
    Define the lightweight Stage 1A Operator Weekly Command Brief input contract
    that precedes PrecapWeek compilation. Captures weekly operator intent,
    portfolio focus overrides across the 6 canonical portfolio areas (Leela,
    IPOS, Master of Arts, Apex AI, Mindful Bar, Residual), ignored calendar
    holds, special evening themes, personal Mental/Physical/Regeneration focus
    priorities, and week-demand.json dispersal dials without forcing the
    operator to author raw JSON or re-state standard blueprint defaults.
```

## Canonical 6-Portfolio Roster

```yaml
canonical_portfolio_areas:
  count: 6
  areas:
    - id: leela
      label: "Leela"
      owner_system: "OpenProject + leela-game-flutter + leela-website + leela-spec"
    - id: ipos
      label: "IPOS"
      owner_system: "OpenProject + IPOS"
    - id: master_of_arts
      label: "Master of Arts"
      owner_system: "OpenProject + MasterOfArts"
    - id: apex_ai
      label: "Apex AI"
      owner_system: "Apex Session / Sync + apexai-os-meta"
    - id: mindful_bar
      label: "Mindful Bar"
      owner_system: "OpenProject / leela-spec/mindful-bar + mindful-bar"
    - id: residual
      label: "Residual"
      owner_system: "Overflow / Recovery / Admin / Unassigned"
```

## Adaptive-Hybrid Intake Rules

```yaml
adaptive_hybrid_intake:
  principle: >
    Ask only high-leverage, non-inferable weekly questions. Never ask the
    operator to repeat standard blueprint clock times, OpenProject state, or
    unchanged ongoing policies.
  routing_buckets:
    New:
      definition: "Week-specific operator intent, scope pauses, or evening theme overrides."
      gate_status: "PROPOSED_FOR_G1 | APPROVED | CONFIRMED_INPUT"
    Standard:
      definition: "Canonical defaults from 02-weekly-dispersal/week-blueprint.json (e.g., Mon-Wed Project Night 20:30-22:00, Thu-Fri Freizeit 20:30-22:00, 18:30-19:30 Evening Physical)."
      override_guard: "Only tag as OPERATOR OVERRIDE when a verified {system_default, operator_choice, source_ref} delta exists."
    Ongoing:
      definition: "Standing multi-week operator rules and ignored ambient calendar holds (e.g., WC Meister)."
```

## Operator Weekly Command Brief Schema

```yaml
operator_weekly_command_brief:
  week_id: "YYYY-Www"
  weekly_intent: "Concise portfolio North Star for the week."
  project_focus_overrides:
    - portfolio_area: "Leela | IPOS | Master of Arts | Apex AI | Mindful Bar | Residual"
      directive: "Week-specific focus, scope freeze, or pause instruction."
      gate_status: "CONFIRMED_INPUT | PROPOSED_FOR_G1"
  calendar_ignores:
    - match: "Calendar event title substring (untrusted data)"
      bucket: "Ongoing | New"
      reason: "Why this calendar hold is ignored for capacity calculation."
  special_evenings:
    mon_tue_wed_project_night_theme: "Optional weekly theme override for the standard Mon-Wed 20:30-22:00 Project Night block."
  personal_focus_priorities:
    mental:
      - "Mental focus bullet for the week"
    physical:
      - "Physical / injury-protection focus bullet (e.g., right knee I3_P pin)"
    regeneration:
      - "Regeneration / boundary focus bullet"
  dispersal_dials_override:
    source_ref: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-demand.json"
    notes: "Optional adjustments to Mental/Physical/Craft epic shares or focus_days."
```
