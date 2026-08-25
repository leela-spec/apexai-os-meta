# 02-INPUT-CORPUS.md — Phase 2 faithful baseline inputs
> Campaign rule: baselines are generated from REAL inputs, not invented.
> This register records every input source, its provenance class, and its SHA.

## Corpus decision

The repository contains no live operator Session/Sync state (`state/apex-project-status.md`
is empty; no `artifacts/weekly-plans/` packets exist). The richest realistic,
internally consistent portfolio material on `main` is the 5-week progressive
simulation trajectory. Per campaign rules it is used ONLY as **input material**
(scenario facts), never as design authority or output template. All output
artifacts in this phase are produced with the ACTUAL production templates:

| Template | Path | Blob SHA |
| :-- | :-- | :-- |
| Weekly Command Brief | `.claude/skills/PrecapWeek/weekly-command-brief-template.md` | `04ed26629719247f25ae3cc186d157b8d8d33f41` |
| PreCap Next Day Brief | `.claude/skills/PrecapNextDay/templates/precap-next-day-brief-template.md` | `c96747e21fca5a02debcc397a9c88d33c3f0f53c` |
| Flow Execution Card | `.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md` | `ca404e6027e3be60c22a9fd500edc0e82f500255` |
| Prompt Files & Index + single-prompt block | `.claude/skills/PrecapNextDay/templates/prompt-files-and-index-template.md` | `b4e95f47a5b8da3dda38a4488818e825f45ca7e3` |

## Input sources

| ID | Source path | Class | Used for | Notes |
| :-- | :-- | :-- | :-- | :-- |
| IN-1 | `apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md` (131 lines) | historical simulation trajectory | Cases A, B, C primary scenario facts: Lika SSoT inventory/canonicalization week, ACIM content/marketing, Apex hygiene blocks, Investment deferred, Residual bucket; fixed daily blocks (morning routine, lunch protected, evening, day_outro, sleep); conflict-handling table; persona stress tests; gate exit criteria | Real project names and plausible weekly volume; NOT treated as authority |
| IN-2 | `apex-meta/kb/Weekly-Orchestrator/indexes/APEX_Weekly_Orchestration_Index_v3.yaml` | repository KB index | Artifact lifecycle J1-J12 references; authority precedence ranks for provenance fields | Confirms loop stage vocabulary used in receipts |
| IN-3 | `apex-meta/orchestration/simulation/week-01..02/**` (2-week canonical sim) | prior observed outputs | Failure-evidence only (Phase 1 findings). Deliberately NOT reused as baseline content: its artifacts violate production templates | Prevents proxy contamination |
| IN-4 | Production skills: PrecapWeek + PrecapNextDay SKILL.md contracts | live domain authority (rank 1) | Output boundaries, execution modes (calendar_constrained_mode etc.), completion gates | Governs what each artifact may contain |
| IN-5 | `PrecapWeek/calendar-planning-guidance.md`, `weekly-blueprint-standard.md`, `weekly-blueprint-meeting-example.md` | supporting doctrine | Capacity/meeting-deformation semantics for Case B | Read-only support |

## Scenario fact sheets

### Case A — normal week (week_id 2026-W36)
Facts from IN-1 continued one week after W1 lock: Lika canonical set stable;
ACIM marketing rewrite done; Apex gets two hygiene blocks; no meetings beyond
fixed personal blocks. Free capacity ~4 work flows/day. Operator intent:
"Consolidate W1 SSoT lock; start ACIM workshop outline."

### Case B — meeting-heavy / constrained week (week_id 2026-W37)
Same portfolio, but calendar injects: Tue 09:00-12:00 external meetings,
Wed all-day workshop prep + 2h review call, Fri half-day. Available flow time
reduced ~55%. Blueprint deformation applies (full/compressed/minimal/omitted).
Operator intent unchanged from A -> forces visible capacity triage.

### Case C — deadline vs high-impact dependency conflict (week_id 2026-W36 variant)
ACIM workshop outline has a hard external deadline Thursday 17:00 (venue
printing) while Lika canonical-index validation (high-leverage, no external
deadline) needs the same Wed-Thu capacity; ACIM rewrite depends on Lika
vocabulary decisions (dependency direction: Lika -> ACIM).
Operator intent: "Both matter; sequence them honestly."

### Case D — stale / missing source state (week_id 2026-W36 variant)
Session planning feed unavailable (stale by 9 days); Sync reports missing for
Investment; only last-known project set + W1 handoff seed exist. Exercises
PrecapWeek degraded mode + PrecapNextDay confidence marking.
Operator intent: "Plan the week anyway; show me what you had to assume."

### Case E — usage scarcity / routing degradation (week_id 2026-W36 variant)
Normal case-A facts plus: primary recommended AI surface quota exhausted for
the week; fallback surface is slower local model; two of twelve sprint prompts
cannot be routed as recommended. Exercises DEGRADED prompt readiness +
usage-tracking hooks. Operator intent: "Keep the week executable under quota."

## Fabrication guards applied

- No operator approval is recorded anywhere in this phase (all
  `operator_validation` fields = pending/not_requested).
- No elapsed/scannability times appear anywhere.
- Model/profile identity: generation performed by the campaign orchestrator
  agent (ox-alpha via Hermes Agent session, docker workspace `/workspace`);
  recorded per receipt.yaml.
- Deterministic checks (template-section presence, placeholder completeness)
  are labeled mechanical_validation; they are not evidence of quality.
