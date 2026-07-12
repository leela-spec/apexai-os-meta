# Weekly Orchestrator — Execution Trace + Verification Record

Status: real checks executed 2026-07-11 against the live repo (per `apex-meta/fable-orchestrator/build-plan.md` simulation definition: actual attempt, actual result, honest verdict — not a hypothetical walkthrough).

## 1. Automated file-level verification (executed)

Script run over the full execution surface. Result: **ALL CHECKS PASS**.

```yaml
checks_executed:
  agent_frontmatter_lint:
    scope: all 8 files under .claude/agents/
    asserts: [valid YAML frontmatter, name present, description present, every skills-preload entry resolves to .claude/skills/<entry>/SKILL.md]
    result: pass
  skill_frontmatter_lint:
    scope: all 11 SKILL.md entrypoints in the loop + dependencies + orchestrator
    asserts: [frontmatter fences valid, name and description parse]
    result: pass          # six entrypoints were repaired this session — see 02-meso-file-map.md skill layer notes
  path_reference_resolution:
    scope: every repo path cited in the 14 new/changed control-plane, agent, and architecture files
    result: pass
  no_draft_language:
    scope: same 14 files
    asserts: no TODO / TBD / skeleton / draft / placeholder / to-be-defined
    result: pass
```

Registration evidence: after the entrypoint repairs, all six previously-broken skills (PrecapWeek, PrecapNextDay, ProjectStatus, AIRouting, PromptEngineer, Workflow&Processes) and the new weekly-orchestrator skill registered in the live skill list with clean descriptions — confirmed in-session, not assumed.

## 2. Real loop-position run (orchestrator procedure step 1, executed)

```yaml
executed: list artifacts/* families + read state files
observed:
  artifacts/weekly-plans/: empty
  artifacts/next-day-plans/: empty
  artifacts/flow-packets/: empty
  artifacts/flow-recap-packets/: empty
  artifacts/reviews/: created this session (empty)
  state/apex-project-status.md: 0 bytes
  state/consumed-recap-registry.md: 0 bytes
correct_orchestrator_behavior_per_contract:
  loop_position: pre-first-cycle (no confirmed packet exists)
  next_stage: precap_week (G1) — or precap_next_day in bootstrap_mode if the operator wants a day plan before a weekly plan
  degraded_flags: [state_files_empty (known issue G01: parallel registry under .claude/kb/), first_run_no_recap_history]
verdict: pass — the failure-behavior contract covers the actual observed repo state without any undefined case.
```

## 3. Stage-dispatch trace (one full cycle, against real paths)

| # | step | actor | reads (real, resolvable) | writes | gate |
|---|---|---|---|---|---|
| 1 | locate loop | main thread (weekly-orchestrator) | state/*, artifacts/* listings | — | — |
| 2 | weekly plan | apex-precap-week (preloads PrecapWeek) | state/apex-project-status.md, prior recaps, operator intent | artifacts/weekly-plans/weekly_plan_packet-*.md | G1 |
| 3 | daily plan | apex-precap-next-day (preloads PrecapNextDay; Skill tool → PromptEngineer/AIRouting/Workflow&Processes) | confirmed weekly packet, status, recaps | artifacts/next-day-plans/*, artifacts/flow-packets/<date>/* incl. prompt-packs/ | G2 |
| 4 | execution | operator (human) | flow packet + prompt packs | raw notes / skip signal | G3 |
| 5 | normalize | apex-evidence-normalize (preloads raw-flow-dump-normalize) | raw notes + flow packet | artifacts/flow-packets/<date>/normalized-raw-flow-dump-*.md | — |
| 6 | recap | apex-flow-recap (preloads flow-recap, model-usage-log) | flow packet + dump | artifacts/flow-recap-packets/flow_recap_packet-*.md | G4 |
| 7 | merge proposal | apex-status-merge (preloads status-merge) | G4-confirmed recaps, state files, registry | artifacts/flow-recap-packets/status_merge_packet-*.md | G5 |
| 8 | review (if consequential) | apex-review-validity ∥ apex-review-alignment | frozen packet + sources / anchors | artifacts/reviews/review-*.md (verdict recorded by main thread) | review |
| 9 | durable write | main thread only | confirmed merge packet | append to state/apex-project-status.md + state/consumed-recap-registry.md, fetch-back verified | post-G5 |
| 10 | overview | apex-project-status (preloads ProjectStatus) | state/apex-project-status.md | artifacts/weekly-plans/project-status-overview-*.md | — |
| 11 | next cycle | operator trigger → step 3 (or step 2 at week start) | — | — | — |

Every read/write column entry resolves to a path in `02-meso-file-map.md`; every gate resolves to the gate map in `handoff-schema.md`; steps 8–9 enforce the D-M4/D-M5 permission and review model. No step depends on agent memory — a killed session resumes from step 1.

## 4. Honest residuals (not blockers, tracked)

- `state/` files are empty and `.claude/kb/` holds a parallel registry (index gap G01). The orchestrator's degraded mode handles it; durable resolution belongs to the later apex-kb/project-kb connection (declared out of scope by the operator).
- The first real operator-executed cycle (G3 evidence from a genuinely worked flow) is by definition the operator's step; steps 1–2 of this trace were executed for real, steps 3–11 are contract-verified against real paths.

## 5. Live stage-agent behavioral tests (executed 2026-07-11)

```yaml
behavioral_tests:
  T1_apex-evidence-normalize:
    dispatch: synthetic F3 raw notes, no flow_packet on disk, run_date passed in dispatch
    result: pass — full envelope, correct unmatched_flow uncertainty, refused interpretation, envelope+4-line return
    cost: {subagent_tokens: 22887, tool_uses: 4}
    output: artifacts/flow-packets/20260711/normalized-raw-flow-dump-F3.md (test artifact, removed after recording)
  T2_apex-precap-week:
    dispatch: G1 bootstrap, empty state file, operator intent + calendar constraints, week-id passed
    result: pass — correct degraded/bootstrap behavior, all assumptions flagged, envelope complete
    cost: {subagent_tokens: 36749, tool_uses: 9}
    output: artifacts/weekly-plans/weekly_plan_packet-20260711-2026-W29.md (test artifact, removed after recording)
finding_that_drove_P01:
  target_surface_ambiguity: both test agents set target_surface to their own output path; schema means
    "durable surface this packet proposes to affect" — fixed in handoff-schema field_rules + all agent
    envelope instructions (patch wave 1).
```

```yaml
behavioral_tests_meta_ops_integration:              # executed 2026-07-12
  T3_apex-sync-ops:
    dispatch: next + blockers subcommands, run_date passed in dispatch
    result: pass — envelope correct, raw JSON reports preserved unaltered, dry-run kept, zero files
      written, authority.state verified on exit 0 + empty review_flags; 8 real task files computed,
      1 actionable candidate, 7 blocked via depends_on chains
    cost: {subagent_tokens: 51872, tool_uses: 4}
  T4_apex-plan-ops:
    dispatch: capture project orchestrator-regression-suite (build-plan regression goal), run_date passed
    result: pass — full envelope, target_surface none, 5 proposed task records with dependency plan,
      no state mutated, exact ranking correctly routed to apex-sync; surfaced real finding —
      apex-meta/registry/index.md does not exist (id-space unreadable)
    cost: {subagent_tokens: 68122, tool_uses: 11}
    output: apex-meta/handoff/plan-packets/apex_plan_packet-20260712-orchestrator-regression-suite.md
      (kept — real pending proposal, operator_validation not_requested)
```
