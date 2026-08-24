# Hermes Detailed Orchestration Simulation Plan
# 2-Week End-to-End Simulation of the Apex Weekly Orchestration System

```yaml
document_role: detailed_two_week_orchestration_simulation_blueprint
simulation_name: APEX-E2E-SIM-2W-01
canonical_repo: /root/workspaces/apexai-os-meta (branch: main)
portfolio_repos:
  - MasterOfArts
  - Investment
  - acim-secular
  - apexai-os-meta
architecture_backbone:
  - Apex Plan
  - Apex Session
  - Apex Sync
  - ProjectStatus
  - PrecapWeek            # Gate G1
  - PrecapNextDay         # Gate G2
  - Flow Execution        # Gate G3 (raw evidence)
  - raw-flow-dump-normalize
  - flow-recap            # Gate G4
  - status-merge          # Gate G5
  - Apex Session          # mutation
  - Apex Sync             # recomputation
anti_rushing_mandate: >
  A level cannot begin until the preceding level's physical artifacts exist on
  disk and are recorded in simulation-state-ledger.yaml with a checksum.
weekday_scope: Monday_to_Friday_only
time_precision_rule: 15_minute_internal_precision__block_level_human_output
challenge_dynamics: continuous_bmad_marketingskills_triagent_observer_panel
compounding_loop: week1_baseline -> tri_agent_synthesis -> patch_pack -> week2_compounded_run
```

---

## 0. Simulation Directory Layout & Physical Artifact Paths

All simulation state lives under one root so gate checks are pure filesystem checks:

```
/root/workspaces/apexai-os-meta/
└── apex-meta/orchestration/
    ├── docs/
    │   └── HERMES_DETAILED_ORCHESTRATION_SIMULATION_PLAN.md   <- this document
    └── simulation/
        ├── simulation-state-ledger.yaml                       <- single source of truth for gates
        ├── week-01/
        │   ├── l0-init/
        │   │   ├── projectstatus-snapshot.yaml                # per-repo ProjectStatus export
        │   │   ├── active-tasks-{masterofarts,investment,acim-secular,apexai-os-meta}.yaml
        │   │   ├── capacity-model.yaml                        # FreeT budget, operator hours
        │   │   └── init-checklist.md
        │   ├── l1-weekly-brief/
        │   │   ├── weekly-command-brief.md                    # Dual-Matrix brief (Matrix 1 + Matrix 2)
        │   │   ├── g1-checkpoint.yaml                         # signed gate record
        │   │   ├── bmad-review-G1.md
        │   │   ├── marketingskills-review-G1.md
        │   │   └── observer-panel-G1.md                       # 3 sub-reviews in one file
        │   ├── l2-daily-planning/
        │   │   ├── day-{mon..fri}/
        │   │   │   ├── precap-next-day-brief-day{N}.md
        │   │   │   ├── flow-cards-f{1..4}-day{N}.md           # Flow Execution Cards F1–F4
        │   │   │   ├── sprint-prompt-pack-day{N}.md
        │   │   │   └── g2-checkpoint-day{N}.yaml
        │   ├── l3-flow-execution/
        │   │   ├── day-{mon..fri}/flow-f{K}/raw-evidence/     # unmodified dumps, logs, diffs
        │   │   │   └── raw-flow-dump-f{K}-day{N}.{log|diff|md}
        │   │   └── day-{mon..fri}/g3-checkpoint-day{N}.yaml
        │   ├── l3b-normalize/
        │   │   └── day-{mon..fri}/normalized/{f1..f4}.md      # output of raw-flow-dump-normalize
        │   ├── l4-recap-merge/
        │   │   ├── day-{mon..fri}/flow-recap-day{N}.md        # Gate G4 artifact
        │   │   ├── day-{mon..fri}/status-merge-day{N}.yaml    # Gate G5 artifact
        │   │   ├── day-{mon..fri}/g4-g5-checkpoint-day{N}.yaml
        │   │   └── day-{mon..fri}/{bmad,marketingskills,observer-panel}-review-L4-day{N}.md
        │   ├── l5-session-sync/
        │   │   ├── day-{mon..fri}/apex-session-mutation-day{N}.json
        │   │   ├── day-{mon..fri}/apex-sync-recompute-day{N}.yaml
        │   │   └── day-{mon..fri}/l5-closure-record-day{N}.md
        │   └── synthesis/
        │       ├── tri-agent-end-of-week-synthesis-w1.md
        │       ├── evaluation-scorecard-w1.yaml
        │       └── patch-pack-w1-to-w2.md                     # operator-reviewable exact-match patches
        └── week-02/                                           # identical structure; compounded run
            ├── ... (same l0..l5 tree)
            └── final-report/
                ├── compounded-scorecard-w2.yaml
                ├── delta-analysis-w2-vs-w1.md
                └── acceptance-verdict.yaml
```

### 0.1 State Ledger Tracking Schema — `simulation-state-ledger.yaml`

```yaml
ledger_schema_version: "1.0"
simulation_id: APEX-E2E-SIM-2W-01
updated_at: "<ISO8601>"
current_week: 1|2
current_day: mon|tue|wed|thu|fri|synthesis
current_level: L0|L1|L2|L3|L3b|L4|L5
gate_status:
  G1_weekly_brief:    {state: pending|open|passed|failed, evidence_path: str?, sha256: str?, decided_at: ts?, decision_note: str?}
  G2_daily_planning:  {per_day: {mon: {...}, tue: {...}, wed: {...}, thu: {...}, fri: {...}}, same fields}
  G3_raw_evidence:    {per_day_per_flow: {"day-mon/f1": {...}}, same fields}
  G4_flow_recap:      {per_day: {...}, same fields}
  G5_status_merge:    {per_day: {...}, same fields}
artifacts:                      # every physical artifact, append-only
  - id: ART-0001
    level: L1
    path: apex-meta/orchestration/simulation/week-01/l1-weekly-brief/weekly-command-brief.md
    kind: weekly_command_brief
    produced_by: PrecapWeek
    sha256: "<checksum>"
    created_at: "<ts>"
    reviewed_by: [bmad, marketingskills, experience_designer, code_architect, orchestration_practitioner]
    review_verdicts: {bmad: pass|fail|conditional, marketingskills: ..., observers: ...}
repos_state:
  masterofarts:   {projectstatus_ref: path, open_tasks: N, capacity_allocated_pct: N}
  investment:     {...}
  acim_secular:   {...}
  apexai_os_meta: {...}
token_economics:
  per_day: {day: str, prompt_tokens: N, completion_tokens: N, challenge_overhead_tokens: N, total: N}
  cumulative: {week_1_total: N, week_2_total: N}
metrics_baseline_w1:
  scannability_seconds: null      # Experience Designer <60s target
  value_prop_strength_score: null # MarketingSkills 1–10
  determinism_pass_rate: null     # Code Architect % of deterministic scripts fail-closed clean
  gate_integrity_violations: N    # Orchestration Practitioner count of zero-fact-bleed breaches
  rerun_count_due_to_errors: N
metrics_compounded_w2:
  same_fields_as_baseline: null
patch_pack:
  status: draft|operator_review|approved|applied
  blocks: [{file: path, old_excerpt_sha256: str, new_excerpt_sha256: str}]
  applied_at: ts?
gate_rule: |
  HARD RULE: current_level may only advance when every artifact required by the
  level-entry checklist exists on disk AND its sha256 is registered under
  `artifacts`. Any attempt to advance with missing artifacts = gate integrity
  violation, logged by the Orchestration Practitioner.
```

---

## 1. Standing Roles & Challenge Contracts (apply at every level)

| Agent | Enforce | Fail Condition |
|---|---|---|
| BMAD Agile Framework | Structural spec conformance, user-story acceptance criteria, technical mechanics of scripts/schemas | Any story lacking verifiable AC; any schema drift from ProjectStatus/PrecapWeek/PrecapNextDay contracts |
| MarketingSkills | Human-facing card priority, value propositions, hook strength, visual clarity of the Command Brief & Flow Cards | Cards unreadable in <60s, no explicit deliverable value statement, weak hooks on F1–F4 cards |
| Observer: Experience Designer | Visual hierarchy, cognitive load, <60s scannability | Scannability test fails or hierarchy inverted (detail above priority) |
| Observer: Code Architect | Deterministic Python/DuckDB scripts, schemas, fail-closed error handling | Non-deterministic output, silent failure paths, schema mismatch vs ledger |
| Observer: Orchestration Practitioner | Gate integrity G1–G5, zero fact bleed across repos, token economics | Fact bleed between repos, gate skipped, challenge overhead >35% of daily tokens |

Standing rule: challenges are issued **at each level before its gate closes**; unresolved challenges block the gate unless the operator records an explicit waiver with reason in the checkpoint YAML.

---

## 2. Week 1 — Baseline Execution: Day-by-Day Level Gate Procedures

Each simulated day runs levels L0–L5 in strict order. Levels already satisfied earlier in the week (e.g., L1 on Mon) are re-verified cheaply ("drift check") rather than re-produced.

### MONDAY — Full Chain Cold Start

**L0 — State Initialization (Gate precondition for everything)**
1. Export ProjectStatus snapshots for all four repos into `week-01/l0-init/projectstatus-snapshot.yaml`.
2. Enumerate active repo tasks (`active-tasks-*.yaml`); build `capacity-model.yaml` with FreeT budget per day and per-flow allocation.
3. Run `init-checklist.md`: all four repos present, no stale task states, ledger initialized.
4. Challenge prompts (below) fire on the snapshot; verdicts logged.
5. Artifact check → register checksums in ledger. No L1 without this.

**L1 — Weekly Command Brief (Gate G1)**
1. Execute PrecapWeek against L0 snapshots.
2. Produce `weekly-command-brief.md` with BOTH matrices:
   - Matrix 1: Projects → Targets → Deliverables (human-first).
   - Matrix 2: F1–F4 × Mon–Fri schedule grid with FreeT blocks and S1/S2/S3 goals.
3. Fire G1 challenge round (BMAD structure, MarketingSkills card priority, full Observer triad).
4. Resolve or waive challenges → sign `g1-checkpoint.yaml`.

**L2 — Monday Daily Planning (Gate G2-Mon)**
1. Execute PrecapNextDay for Tuesday using L1 brief + Monday calendar context.
2. Outputs: `precap-next-day-brief-mon.md`, `flow-cards-f1..f4-mon.md`, `sprint-prompt-pack-mon.md`.
3. G2 challenge round → sign `g2-checkpoint-mon.yaml`.

**L3 — Flow Execution Monday (Gate G3-Mon)** For each scheduled flow F1–F4:
1. Run sprint prompt pack against the target repo (mapping fixed in Matrix 2).
2. Capture RAW evidence only into `raw-evidence/` — never normalized, never edited.
3. Sign `g3-checkpoint-mon.yaml` per flow: evidence path + sha256 + target repo + fact-bleed scan result.

**L3b — Normalize**
Run `raw-flow-dump-normalize` over each raw dump → `normalized/f{k}.md`. Normalizer must be deterministic (Code Architect verifies: same input → byte-identical output).

**L4 — FlowRecap & StatusMerge (Gates G4/G5-Mon)**
1. `flow-recap` consumes normalized dumps → `flow-recap-mon.md`.
2. `status-merge` merges recap deltas back into per-repo ProjectStatus → `status-merge-mon.yaml`.
3. L4 challenge round (recap fidelity, merge correctness, zero fact bleed).
4. Sign `g4-g5-checkpoint-mon.yaml`.

**L5 — Apex Session Mutation & Sync**
1. Apply session mutations → `apex-session-mutation-mon.json`.
2. Recompute Apex Sync → `apex-sync-recompute-mon.yaml`; diff against expectations.
3. Write `l5-closure-record-mon.md`; update ledger; day closed.

### TUESDAY — First Steady-State Loop (L0 becomes drift-check)
- L0: diff ProjectStatus vs Monday's post-merge state; ledger drift report. Full re-init only on mismatch.
- L1: G1 already passed — verify brief still matches merged reality (cheap consistency probe, not regeneration). If drift >threshold, PrecapWeek partial refresh is allowed ONLY via recorded waiver.
- L2: PrecapNextDay for Wednesday (full pipeline, G2-Tue).
- L3/L3b/L4/L5: Tuesday flows → normalize → recap → merge → session/sync. Same gate discipline as Monday.

### WEDNESDAY — Midweek Stress Variant
Same loop, plus deliberate stress injection at L3: one flow executes with a degraded input (missing file / malformed dump) to exercise fail-closed behavior.
- Code Architect must confirm: normalizer and recap FAIL CLOSED with clear error, no silent partial output.
- Resilience result logged in ledger under `metrics_baseline_w1.rerun_count_due_to_errors`.
- All other gates unchanged.

### THURSDAY — Cross-Repo Day
Matrix 2 schedules flows touching ≥2 repos (e.g., F1 Investment, F2 acim-secular, F3 MasterOfArts, F4 apexai-os-meta tooling).
- Zero-fact-bleed audit is mandatory at L4: Orchestration Practitioner greps each repo's recap section for foreign-repo facts.
- Token economics recorded per flow; challenge overhead ratio computed.

### FRIDAY — Close-Out & Synthesis Prep
- Morning: standard loop through L4/L5 for Friday flows.
- Afternoon: freeze Week 1 — all artifacts checksummed; ledger `current_day: synthesis`.
- Kick off End-of-Week Tri-Agent Synthesis (Section 4).

### Per-Level Prompt Contracts (issued identically each day, parameterized by level/day)

**BMAD (structural enforcement):**
```
ROLE: BMAD Agile Framework enforcer for APEX-E2E-SIM-2W-01, Week 1, {DAY}, Level {LEVEL}.
INPUT: {artifact paths for this level} + relevant sections of simulation-state-ledger.yaml.
CHECKS:
 1. Does every user story implied by today's Flow Cards have verifiable acceptance criteria?
 2. Do technical mechanics conform to the governing package contracts
    (ProjectStatus schema, PrecapWeek dual-matrix format, PrecapNextDay
    next_day_plan/flow_packet/prompt_pack schemas)?
 3. Is every artifact path exactly as defined in the layout (Section 0)?
OUTPUT: verdict pass|fail|conditional per check + blocking findings list.
HARD RULE: You do not evaluate style or value. Structure and mechanics only.
```

**MarketingSkills (human-facing enforcement):**
```
ROLE: MarketingSkills enforcer, Week 1, {DAY}, Level {LEVEL}.
INPUT: human-facing artifacts only (Weekly Command Brief matrices, Flow Cards F1–F4,
       Next-Day Brief headline sections).
CHECKS:
 1. Card priority: are the highest-value cards visually first in each matrix/card set?
 2. Value proposition: does every card state what the operator GETS, not just what is done?
 3. Hook strength: does the day's top line survive the "why care in 5 seconds" test?
 4. Visual clarity: tables/cards renderable without explanation?
OUTPUT: 1–10 score per check + rewrite suggestions as exact replacement text.
```

**Observer Panel (three independent reviews, then one joint verdict):**
```
EXPERIENCE DESIGNER: Perform a <60-second scannability test on {artifact}.
  Report: time-to-core-message, hierarchy violations, cognitive-load hotspots,
  fix list ranked by load reduction per edit.
CODE ARCHITECT: Audit {deterministic scripts/schemas at this level}.
  Report: determinism proof (rerun hash match), fail-closed verification,
  schema conformance vs ledger, error-path inventory.
ORCHESTRATION PRACTITIONER: Audit gate integrity G1–G5 for {DAY}.
  Report: gate order compliance, artifact existence + checksum verification,
  zero-fact-bleed scan results, token economics ({prompt}/{completion}/
  {challenge_overhead}), violation list.
JOINT VERDICT: continue | remediate-first (list) | halt (reason).
```

---

## 3. Week 1 → Week 2 Transition Protocol

### 3.1 End-of-Week Tri-Agent Synthesis (Friday PM / weekend)
Inputs: all Week 1 review files + scorecard + ledger token economics.
Output: `tri-agent-end-of-week-synthesis-w1.md` containing:
1. Five-axis findings: Design (Experience Designer), Value (MarketingSkills), Determinism (Code Architect), Efficiency (Practitioner token economics), Resilience (stress-test outcomes).
2. Ranked improvement backlog (impact × effort).

### 3.2 Evaluation Scorecard — `evaluation-scorecard-w1.yaml`
```yaml
scorecard_version: "1.0"
axes:
  design:       {metric: scannability_seconds, w1_value: N, target_w2: "<60", owner: experience_designer}
  value:        {metric: avg_card_value_score, w1_value: N, scale: "1-10", target_w2: ">=7.5", owner: marketingskills}
  determinism:  {metric: deterministic_script_pass_rate_pct, w1_value: N, target_w2: 100, owner: code_architect}
  efficiency:   {metric: challenge_overhead_token_pct, w1_value: N, target_w2: "<=25", owner: orchestration_practitioner}
  resilience:   {metric: stress_injection_clean_failures_pct, w1_value: N, target_w2: 100, owner: code_architect}
  integrity:    {metric: gate_violation_count, w1_value: N, target_w2: 0, owner: orchestration_practitioner}
```

### 3.3 Automated Patch Pack Protocol
1. Each finding converts to ONE exact-match patch block in `patch-pack-w1-to-w2.md`, targeting templates/cards/scripts (e.g., Flow Card template, Weekly Brief matrix template, normalizer script, PrecapWeek checklist).
2. Block format: literal `<file>`, `<old>` (byte-for-byte from live target, verified unique), `<new>`.
3. Status lifecycle: `draft → operator_review → approved → applied`.
4. HARD RULE (Apex KB Patch Safety): nothing is committed or auto-applied without explicit operator approval; application requires the executor's exact-match success result plus test evidence (deterministic rerun hash, schema validation, scannability retest) recorded in the ledger.
5. Only after `applied` + evidence does `current_week: 2` unlock in the ledger.

---

## 4. Week 2 — Compounded Execution

Identical L0–L5 daily loop, Mon–Fri, with three differences:
1. All execution uses patched templates/cards/scripts from the approved patch pack.
2. Same stress injections (Wed) and cross-repo day (Thu) for apples-to-apples comparison.
3. Every day, reviewers score against W2 targets, not just pass/fail.

### 4.1 Measurable Acceptance Criteria — Compounded Run (all must hold)

| Axis | Metric | W1 Baseline | W2 Acceptance |
|---|---|---|---|
| Design | Scannability of Weekly Brief + Flow Cards (Experience Designer timed test) | measured | ≤60s every day; ≥20% reduction vs W1 |
| Value | Avg card value-prop/hook score (MarketingSkills) | measured | ≥7.5/10 every day; no card below 6 |
| Determinism | Normalizer + recap scripts rerun-hash pass rate | measured | 100% (byte-identical reruns), 100% fail-closed on Wed stress |
| Efficiency | Challenge-overhead token share of daily tokens | measured | ≤25%; total W2 tokens ≤ W1 despite added scoring |
| Resilience | Stress-injection clean-failure rate; unplanned reruns | measured | 100% clean failures; reruns ≤ W1 count −1 |
| Integrity | Gate violations (order, checksum, fact bleed) | counted | 0 for the entire week |
| Patch efficacy | Patch-pack blocks applied with passing evidence | n/a | 100% of approved blocks; zero regressions flagged by any reviewer |

Verdict: `acceptance-verdict.yaml` = PASS only if all seven rows hold; any single miss requires a named remediation patch pack v2 proposal (not a waiver-by-default).

Final artifacts: `compounded-scorecard-w2.yaml`, `delta-analysis-w2-vs-w1.md`, `acceptance-verdict.yaml`, plus the frozen two-week ledger.

---

## 5. Execution Notes
- The simulation directory tree is scaffolded at sim start; ledger is created empty with `gate_status` all `pending`.
- Gate checks are mechanical: filesystem existence + sha256 + ledger registration. Reviewer verdicts are advisory-to-blocking only via the checkpoint YAMLs.
- Leela app development remains out of scope everywhere (Leela-Cloud-2026 owns it); if a flow surfaces a Leela item it is routed out, never planned.
