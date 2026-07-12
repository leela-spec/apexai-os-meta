# Weekly Orchestrator — Meso File Map (execution surface)

Rule: this is the complete file inventory of the execution-ready weekly orchestration flow. If a path here fails to resolve, the system is degraded — report it, per `weekly-orchestrator` failure behavior.

## control plane

```yaml
control_plane:
  root_instruction: .claude/CLAUDE.md                                   # identity, core_loop, skills table, agents table, constraints
  orchestrator_skill: .claude/skills/weekly-orchestrator/SKILL.md      # stage routing, gate holding, project-engine handoffs
  handoff_schema: .claude/skills/weekly-orchestrator/references/handoff-schema.md   # one envelope for every packet + gate primitive + authority object
  review_wiring: .claude/skills/weekly-orchestrator/references/review-wiring.md     # dual-blind review procedure + deterministic aggregation
  glossary: apex-meta/GLOSSARY.md                                       # canonical meaning for drifted terms
```

## agent layer (durable definitions, ephemeral invocations)

```yaml
agents:
  - .claude/agents/apex-precap-week.md
  - .claude/agents/apex-precap-next-day.md
  - .claude/agents/apex-evidence-normalize.md
  - .claude/agents/apex-flow-recap.md
  - .claude/agents/apex-status-merge.md
  - .claude/agents/apex-project-status.md
  - .claude/agents/apex-review-validity.md
  - .claude/agents/apex-review-alignment.md
```

## skill layer (owned bases; canonical SKILL.md entrypoints)

```yaml
weekly_loop_skills:
  - .claude/skills/PrecapWeek/SKILL.md
  - .claude/skills/PrecapNextDay/SKILL.md
  - .claude/skills/raw-flow-dump-normalize/SKILL.md
  - .claude/skills/flow-recap/SKILL.md
  - .claude/skills/model-usage-log/SKILL.md
  - .claude/skills/status-merge/SKILL.md
  - .claude/skills/ProjectStatus/SKILL.md
dependency_skills:                                     # invoked via Skill tool by apex-precap-next-day when needed
  - .claude/skills/PromptEngineer/SKILL.md
  - .claude/skills/AIRouting/SKILL.md
  - .claude/skills/Workflow&Processes/SKILL.md
external_project_engine:
  - .claude/skills/apex-plan/SKILL.md                  # project proposal capability; independently invoked
  - .claude/skills/apex-sync/SKILL.md                  # deterministic project reports; independently invoked
  - .claude/skills/apex-session/SKILL.md               # confirmed project/task mutation and planning-feed owner
optional_knowledge_context: [project-kb-manager]
```

Each skill package keeps its `references/` (read_when-gated), `templates/` (J1–J12 promoted cards), and `examples/` in place — declared ownership by agent preload, no folder moves.

## state and artifact layer (where resilience lives)

```yaml
project_engine_state:                # canonical project/task state; Apex Session writes after approval
  - apex-meta/handoff/               # confirmed H6 artifacts and planning feed
  - apex-meta/registry/              # Apex Sync report outputs when produced
artifact_families:                   # proposals/computed packets; stage agents write here only
  weekly_plans: artifacts/weekly-plans/            # weekly_plan_packet, project-status-overview
  next_day_plans: artifacts/next-day-plans/        # next_day_plan
  flow_packets: artifacts/flow-packets/<YYYYMMDD>/ # flow packets, prompt-packs/, normalized dumps, skip markers
  flow_recap_packets: artifacts/flow-recap-packets/ # recap packets, status_merge_packet
  reviews: artifacts/reviews/                       # review verdict artifacts
knowledge_context: ".claude/kb/ may be read as supporting knowledge but does not override confirmed Session or Sync output."
```

## write-permission matrix

| surface | who writes | condition |
|---|---|---|
| `artifacts/<own family>/` | the producing stage agent | always allowed within its family |
| project/task state | Apex Session | confirmed J9 proposal + operator validation + verified-input closure |
| `.claude/kb/*` | project-kb-manager when invoked | supporting knowledge only; never weekly project-state canon |
| `.claude/skills/`, `.claude/agents/`, control plane | operator-directed sessions only | never during loop runs |
| reviewers | nothing | read-only |
