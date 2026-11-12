## Purpose

Stage 1A Intake captures non-inferable weekly operator intent and outputs JSON conforming to [`operator-weekly-command-brief.schema.json`](../../../../apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/schemas/operator-weekly-command-brief.schema.json) (`OPERATOR-COMMAND-BRIEF-v1.0`).
6-Portfolio definitions and clock defaults are NOT duplicated here; see [`SPEC-PRECAP-WEEK-MASTER.okf.md`](../../../../apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md) and [`week-blueprint.json`](../../../../apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json).

## Adaptive-Hybrid Q&A & Notation Rules

```yaml
adaptive_hybrid_intake:
  schema_owner: apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/schemas/operator-weekly-command-brief.schema.json
  principle: >
    Accept free-form operator intent or JSON matching schemas/operator-weekly-command-brief.schema.json.
    Ask ONLY high-leverage, non-inferable questions; never ask the operator to
    re-enter OpenProject work packages or week-blueprint.json clock windows.
  shorthand_notation:
    I: input_or_issue
    R: risk
    E: evidence   # never "effort" or "estimate"
  routing_buckets:
    New:
      definition: "Week-specific intent, 6-Portfolio focus pauses/freezes, Mon-Wed evening themes, and G1 gates."
      gate_values: [PROPOSED_FOR_G1, APPROVED, CONFIRMED_INPUT]
    Standard:
      definition: "Baseline defaults hydrated automatically from 02-weekly-dispersal/week-blueprint.json."
      override_guard: "Tag OPERATOR OVERRIDE only when verified {sysDef, opChoice, srcRef} exists."
    Ongoing:
      definition: "Standing multi-week rules and ignored ambient calendar holds (e.g., WC Meister)."
```

## Canonical Stage 1A JSON Shape (`OPERATOR-COMMAND-BRIEF-v1.0`)

Reference executable fixture: [`w46-reference-intake.json`](../../../../apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/fixtures/w46-reference-intake.json).

```json
{
  "schema_version": "OPERATOR-COMMAND-BRIEF-v1.0",
  "week_id": "2026-W46",
  "weekly_intent": "Concise weekly portfolio direction",
  "project_focus_overrides": [
    { "portfolio_id": "leela", "directive": "Pause Path UI; ship Skill Tree freeze gate.", "gate_status": "PROPOSED_FOR_G1" }
  ],
  "calendar_ignores": [
    { "match": "WC Meister", "bucket": "Ongoing", "reason": "Standing ignored evening hold" }
  ],
  "special_evenings": {
    "mon_tue_wed_project_night_theme": "Optional theme split; omitted uses week-blueprint.json standard"
  },
  "personal_focus_priorities": {
    "mental": ["Daily morning intention coherence"],
    "physical": ["Protect right knee via *_*_I3_P"],
    "regeneration": ["Screen-off at 22:30 Day Outro"]
  }
}
```
