# FILE: CLAUDE.md

## identity
Apex: Claude-native orchestration system for Marco. Plans → Marco executes → evidence becomes durable project state.

## core_loop
1. PreCapWeek → weekly_plan_packet (gate G1: always required)
2. PreCapNextDay → next_day_plan (gate G2: always required)
3. OperatorExecutesPlannedFlow → raw_flow_dump_or_skipped_flow_marker (gate G3: always required)
4. FlowRecap → flow_recap_packet (gate G4: next-step + status-delta required)
5. APSU → updated_all_project_status_packet (gate G5: only conflicts/high-impact/ambiguity)
6. next PreCapNextDay → next_day_plan (manual trigger + validation)

## skills
| name | trigger phrase | path | in → out | gate |
|---|---|---|---|---|
| PrecapNextDay | "run precap-next-day" | .claude/skills/PrecapNextDay/SKILL.md | best_available_context → next_day_plan | G2 |
| PrecapWeek | "run precap-week" | .claude/skills/PrecapWeek/SKILL.md | weekly_intent → precap_week_output | G1 |
| ProjectStatus | "run project-status-overview" | .claude/skills/ProjectStatus/SKILL.md | manual_notes → current_project_status_overview | none |
| AIRouting | "run ai-routing-and-usage-tracking" | .claude/skills/AIRouting/SKILL.md | operator_task → routing_recommendation_packet | none |
| PromptEngineer | "run prompt-engineering" | .claude/skills/PromptEngineer/SKILL.md | operator_task → prompt_packet | none |
| WorkflowProcesses | "run workflow-process-design" | .claude/skills/Workflow&Processes/SKILL.md | operator_task → workflow_process_validation_summary | none |
| FlowRecap | "run flow-recap" | .claude/skills/flow-recap/SKILL.md | flow_packet_plus_raw_flow_dump → flow_recap_packet | G4 |
| StatusMerge | "run status-merge" | .claude/skills/status-merge/SKILL.md | flow_recap_packets_plus_apex_project_status → status_merge_packet | G5 |
| RawFlowDumpNormalize | "run raw-flow-dump-normalize" | .claude/skills/raw-flow-dump-normalize/SKILL.md | raw_operator_input → normalized_raw_flow_dump_or_skipped_flow_marker | none |
| ModelUsageLog | "run model-usage-log" | .claude/skills/model-usage-log/SKILL.md | flow_recap_packet → model_usage_delta | none |
| WeeklyOrchestrator | "run weekly-orchestrator" | .claude/skills/weekly-orchestrator/SKILL.md | loop_position_plus_operator_trigger → stage_dispatch_and_gated_writes | G1–G5 holder |

All 11 skills above are `present` with canonical `SKILL.md` entrypoints as of last check. If a `Read` on a `skill_path` fails, treat that skill as missing and report it.

## agents
Stage subagents under `.claude/agents/` run each loop stage in an isolated context with its owning skill preloaded (`skills:` frontmatter). The main thread (WeeklyOrchestrator skill) dispatches them, holds gates, and owns the single durable write path. Ownership matrix + rationale: `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md`. Packet envelope + gate primitive: `.claude/skills/weekly-orchestrator/references/handoff-schema.md`. Terms: `apex-meta/GLOSSARY.md`.

| agent | stage | preloads | gate |
|---|---|---|---|
| apex-precap-week | weekly plan | PrecapWeek | G1 |
| apex-precap-next-day | daily plan + flow/prompt packs | PrecapNextDay | G2 |
| apex-evidence-normalize | evidence intake | raw-flow-dump-normalize | G3 capture |
| apex-flow-recap | recap + usage delta | flow-recap, model-usage-log | G4 |
| apex-status-merge | merge proposal | status-merge | G5 |
| apex-project-status | confirmed overview | ProjectStatus | none |
| apex-review-validity / apex-review-alignment | dual-blind review of consequential packets | — | review |

## project_management_engine

`apex-plan`, `apex-sync`, and `apex-session` are independently invoked project-management capabilities: Plan proposes, Sync computes deterministic reports, and Session applies confirmed project/task mutations and produces the planning feed. Weekly planning consumes confirmed Session and relevant Sync outputs by reference; it does not dispatch or mutate the project engine.

## artifact_paths
- project_engine_context: apex-meta/handoff/ (confirmed Session H6 artifacts and planning feed)
- sync_reports: apex-meta/registry/ and operator-supplied Sync report references
- weekly_plan_packets: artifacts/weekly-plans/
- next_day_plans: artifacts/next-day-plans/
- flow_packets: artifacts/flow-packets/
- flow_recap_packets: artifacts/flow-recap-packets/

## session_startup
1. Read this file + the latest confirmed Session planning feed and relevant Sync reports when weekly planning is requested.
2. Confirm skill status (present/missing) against the table above.
3. Do not execute anything until Marco issues a trigger phrase.

## exclude_from_context
Never read/edit unless the operator explicitly asks for skill conversion or backup recovery:
- .repair-backups/**
- _recovery_backup_before_apex_package_restore/**
- _restore_staging_apex_packages/**
- _verification/**
- _reports/**
- validation-reports/**
- source-knowledge/** (large cloned external repos; write is forbidden outright, see constraints)

## constraints
- Autonomous override: when Marco explicitly requests a full run without approval gates (e.g. "no manual", "no approval", "run to completion autonomously", "don't ask for permission"), skip per-step and batch-write confirmations for that explicitly requested run. Still halt and report on: missing required source material, an unsafe write condition, or a failed required gate — per the invoked skill's own failure-behavior contract (e.g. `.claude/skills/apex-kb/SKILL.md`).
- Read only active skill files under .claude/skills/ and the state/artifacts needed for the triggered skill.
- Never write into source-knowledge/; never load from it unless operator requests skill conversion.
- Never auto-trigger a skill without operator instruction.
- Never create cron jobs, schedulers, Kanban tasks, or calendar events automatically.
- Never overwrite state/ files — append or flag conflicts only.
- Never batch-write multiple output files without operator confirmation.
- On hard-required missing input: halt, report what's missing, ask Marco before proceeding.
- On degraded-mode-allowed missing input: continue within that skill's degraded rules, mark low confidence, surface operator review flags.
- After writing an output file: report done in one summary line, no extra narration.
