# PreCap Week Validation Gates & Operator Review Flags

Single owner for pre-`G1` executable validation and operator review-flag policies. Clock, schema, and UX definitions remain solely in `02-weekly-dispersal/week-blueprint.json`, `01-weekly-command-brief/schemas/`, and `SPEC-PRECAP-WEEK-ITERATIONS.okf.md`.

## 1. Automated Executable Gates (Run Before Presenting)

```powershell
python apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/render_precap_cockpit.py `
  --data <cockpit.json> --intake <intake.json> --validate-only

python apex-meta/scripts/okf_validator.py --target <okf-brief-folder>
```

Verify deterministically:
1. Schema conformance for `OPERATOR-COMMAND-BRIEF-v1.0`, `PRECAP-WEEK-DATA-v2.1`, and `PRECAP-WEEK-HANDOFF-v2.1` (`render_precap_cockpit.py` exits `0`).
2. `Mon–Sun` coverage (`7` days), all **6 canonical Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`), `zero` phantom WP tokens, `zero` unverified `OPERATOR OVERRIDE` badges, and `create_calendar_events: false`.
3. Every `00..05` section rendered without daily `S1–S3` sprint checklists, prompt packets, or status-merge mutations (`PrecapNextDay` boundary preserved).

## 2. Missing Input Behavior (Never Invent)

| Missing Input | Impact | Required Recovery |
|---|---|---|
| `weekly_intent` | Weak focus | Surface `missing_inputs` review flag; request intent before `G1` approval. |
| Live OP (`:8083`) | Unverified WP delta | Fallback automatically to `apex-meta/tools/project-improvement-orchestration-weekly/00-openproject-dependency-intake/EVIDENCE-20261106.okf.md` + `planning_feed`, tag `[OP-OFFLINE]`, keep unmapped items `[OP-UNRESOLVED]`. |
| Google Calendar | Conflict risk | Use `calendar_unavailable` fallback (`calendar-planning-guidance.md`), mark proposals `tentative`, flag `calendar_uncertainty`. |
| `week-blueprint.json` | Clock missing | Halt Flow placement and request operator review (never invent clock windows). |

## 3. Mandatory Operator Review Flags

```yaml
operator_review_flags:
  overload:
    trigger: "Fixed constraints exceed realistic capacity or require omitted Flows."
    action: "Name affected day/Flows, omission reason, and ask G1 confirmation."
  missing_inputs:
    trigger: "Weekly intent missing, [OP-OFFLINE], or high-risk assumption active."
    action: "List explicit assumption + risk level and tag provenance [src: ...]."
  calendar_uncertainty:
    trigger: "Calendar unavailable, partial, ambiguous event time, or unconfirmed collision."
    action: "Mark calendar_block_proposals tentative; never claim conflict-free status."
  scope_drift:
    trigger: "Request demands PrecapNextDay prompt packets, project execution, status merge, or GCal writes."
    action: "Exclude out-of-scope work and point cleanly to the owning downstream skill."
```
