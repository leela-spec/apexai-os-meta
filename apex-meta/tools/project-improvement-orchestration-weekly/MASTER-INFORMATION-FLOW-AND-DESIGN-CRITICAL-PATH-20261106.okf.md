---
okf_version: "0.2"
type: orchestrator-design-handover
durable_id: WEEKLY-MASTER-MACRO-MESO-20261106
title: "Weekly Orchestrator — current information flow, reuse-first capability audit, and design critical path"
description: "Macro-first design control map; sources, responsibilities, current gaps, cross-module dependencies, decisions, and evidence gates."
status: DESIGN_AUDIT_ACTIVE_NOT_PRODUCTION_AUTHORITY
created: 2026-11-06
repository: leela-spec/apexai-os-meta
starting_commit: 8b8ed45b260cd7d8b6a5b42a66f8545c4284a7ed
role: temporary_master_improvement_orchestrator
runtime_owner: .claude/skills/weekly-orchestrator/SKILL.md
production_contract_mutation: false
openproject_live_verified: false
calendar_live_verified: false
---

# Macro-first Weekly Orchestration handover and execution path

## 0. Operator correction and mission

The operator rejected the previous design order: **do not design Matrix 1 / Matrix 2 surfaces or create a new sequencing skill before reconstructing the entire working system**. First establish the operating process, how information flows, producer/consumer relationships, state authorities and existing capabilities. Then resolve high-impact cross-module decisions. Only then design individual artifacts and run bounded module implementation.

This handover is an orchestration/decision navigation document, **not** a parallel runtime orchestrator, new PM backend, new role hierarchy, or replacement of existing contracts. Its source baseline is GitHub main; user-local Windows/WSL runtime was not accessed.

## 1. Existing master architecture (already built)

**Authority precedence:** Current \`.claude/skills/\` runtime contracts and accepted D012/D013 decisions supersede earlier wrapper-agent architecture under \`apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md\`. That July document says "locked" but documents the historically replaced wrapper stage agents. Preserve it for provenance; do not reintroduce wrappers.

- **Improvement Master role:** \`apex-meta/tools/project-improvement-orchestration-weekly/ORCHESTRATOR-DEFINITION.md\` explicitly defines Master as temporary architecture/integration expert and prohibits a second runtime control plane.
- **Improvement process:** \`apex-meta/tools/project-improvement-orchestration-weekly/PROCESS.md\` requires macro architecture -> bounded module work -> independent Master verification -> fresh runtime test -> operator acceptance.
- **Live runtime:** \`.claude/skills/weekly-orchestrator/SKILL.md\` routes PrecapWeek (G1), PrecapNextDay (G2), operator execution (G3), conditional raw evidence normalize, flow-recap (G4), status-merge (G5), optional ProjectStatus. Six stage Skills use context forks, with two independent review subagents. Session/Sync are separate, still wired as Apex-native backbone.
- **Lifecycle intent:** \`apex-meta/operator-output-design/step3-output-design-system/21-canonical-artifact-family-and-lifecycle-map.okf.yaml\` catalogs J1–J12 as a *navigation projection*, not as an active replacement contract.
- **Existing workflow helper:** \`.claude/skills/Workflow&Processes/SKILL.md\`, name \`workflow-process-design\`, already handles workflow/process classification, sequence/iteration fit, sprint_structure_review and prompt_workflow_alignment_review. Current D012 still has O002 open about whether to add it to the on-demand registry.
- **Daily flow/sprint contracts:** \`.claude/skills/PrecapNextDay/SKILL.md\`, \`references/daily-plan-output-contract.md\`, \`references/flow-packet-contract.md\`, \`templates/precap-next-day-brief-template.md\`, \`templates/flow-execution-card-template.md\` already prescribe daily flows and S1–S3. Some contracts assume fixed F1–F4 and singular project per FlowCard; these require cross-module audit for mixed projects.
- **Recap:** \`.claude/skills/flow-recap/SKILL.md\` generates per-flow candidate_project_status_delta and next-step proposals, **never** confirmed state.
- **Merge:** \`.claude/skills/status-merge/SKILL.md\` merges candidate deltas and emits a next_PreCapNextDay_input_context; current mutation request targets Apex Session (needs owner-aware OP integration).
- **OP:** \`leela-spec/agent-skills\` (\`master\`) \`skills/openproject/SKILL.md\` provides private API v3 read/write client, read-only identity/project/WP commands and per-action confirmed writes; project enrollment must be checked before state authority is claimed.
- **W34 files and original macro/micro OperatorResearch:** fixtures and history, not current source authority. Some old sources explicitly say required RecapDay was removed from the core loop; "DayRecap" should not be created on name resemblance alone.

## 2. Plain-language information-flow map (current / target deltas)

| Transition | Producer -> consumer | Information passed | Fact type / authority | Current gap |
|---|---|---|---|---|
| A. Source intake | OpenProject/repo/Session-Sync/cycle evidence/operator/calendar -> PrecapWeek | Current commitments, real implementation, dependencies, last results, intent, free windows | Different owners for PM, build, decisions and calendar | Active PrecapWeek incorrectly asserts universal OP authority; live enrollment unverified; fallback sources overlap |
| B. Weekly decision | PrecapWeek -> operator -> Weekly Command Brief | Matrix 1 non-temporal strategy; Matrix 2 Mon-Sat allocation; uncertainty and one embedded presentation_handoff | Proposed until G1 approval | Current template uses "Seq" as project lanes, but operator defines sequence as variable time block; Saturday excluded in live scope |
| C. Next day | Approved Brief + latest PM/recap/calendar -> PrecapNextDay | Next-day priorities, constraints and selected work references | Current reality + week direction | FlowCard singular Project / F1–F4 / 3-sprint assumptions may prevent multi-project sequence and sprint without design |
| D. Execution preparation | PrecapNextDay -> Flow Execution Cards + Prompt Files | Actual flow/sprint workspaces, dependencies, executable prompts | Plan, not completion evidence | Need define sequence vs flow mapping and whether multi-project evidence belongs to one or multiple Flow Cards |
| E. Actual work | Operator/external surface -> raw evidence/skip marker | Outcomes, produced assets, issues, decisions | Untrusted until normalized/reviewed; plan is not proof | Evidence capture and conditional normalization must retain per-work-item identity |
| F. Evidence interpretation | raw evidence + flow source -> FlowRecap | True result + per-work-item *candidate* PM deltas | Candidate, not confirmed status | Existing one-flow recap needs test for mixed-project sequence/flow coverage |
| G. Reconciliation | FlowRecap -> StatusMerge/G5 -> owner-aware write authority | Accepted/deferred/rejected deltas + evidence and operator decision | Confirmed only after authorized write and reread | Currently points exclusively to Apex Session; for enrolled OP tasks use OP skill, leave Apex-native records in Session |
| H. Feedback | Confirmed mutation receipt and last recap -> PrecapNextDay / PrecapWeek | Fresh state, carry-forward, next task/goal, blockers | Read current owner state; don't elevate stale summaries | Design exact post-write next-day intake; no duplicate PM stores |

Core loop:
\`\`\`text
Source-truth and constraints (PM + code evidence + operator + calendar)
  -> PrecapWeek: Matrix 1 strategy -> Matrix 2 proposed week allocation
  -> one Weekly Command Brief + operator G1
  -> PrecapNextDay (revalidate) -> sequence/flow/sprint execution plan + prompts (G2)
  -> operator execution/skip (G3) -> raw evidence/normalization
  -> FlowRecap per flow, candidate only (G4)
  -> StatusMerge / G5, grouped by owning work package
  -> canonical OP (for enrolled WPs) or Apex Session (Apex-native only), confirmed reread
  -> fresh PrecapNextDay or next PrecapWeek
\`\`\`

## 3. Vocabulary and current assumptions (do not silently promote)

- **Project:** durable organizational domain, owned by actual project/repo and/or enrolled OP project. May appear in multiple blocks per day.
- **Epic/task/WP:** work identity and non-temporal dependency. Canonical OP-WP#ID only if verified, otherwise explicit OP-UNRESOLVED with local source ref.
- **Sequence:** OPERATOR-CONFIRMED = variable time/capacity block, **not** project. It can contain multiple projects and moves across time/day.
- **Sprint:** a smaller segment inside a sequence. It **may** contain several projects. Mixing strategy, length and project-switch cost remain OPEN. Detailed sprint cards are PrecapNextDay's job.
- **Flow:** existing daily execution/recap unit under PrecapNextDay/FlowRecap. Its relation to sequence remains OPEN (1:1, one sequence -> several flows, or independently shaped structures). Do not assume sequence = flow.
- **Daily Recap:** the existing macro sources and live topology do **not** expose a distinct mandatory RecapDay stage. Existing FlowRecap + StatusMerge may already achieve the desired day-level consolidation. Confirm actual consumer before adding another step.
- **Workday:** Saturday is operator-confirmed normal workday; Sunday OFF by default with explicit exception. Some current live skills still encode Mon–Fri, and a Sunday weekly Precap trigger; that timing conflict requires a deliberate decision.

## 4. Provenance and conflict ledger (do not paper over)

| ID | Current issue | Evidence source | Needed resolution |
|---|---|---|---|
| X01 | Universal OP authority in active PrecapWeek vs enrolled-project-only OP decision candidate | PrecapWeek/SKILL.md; Nov 6 OP decision 01, conflict log C01-C15 | Enrollment + per-fact owner map; read-only live project/WP coverage, pagination and freshness |
| X02 | Apex Session-only durable write vs OP current PM | weekly-orchestrator/SKILL.md; status-merge/SKILL.md | Route approved candidate to owning OP WP or Apex-native control; never mirror |
| X03 | Seq 1-4 hardcoded project lanes vs operator-defined variable multi-project time blocks | Current v4.1 spec/template + user Q06 correction | Vocabulary, sequence-to-flow interface, project membership, mixed sprint policy |
| X04 | Existing FlowCard single "Project", fixed F1-F4 and S1-S3 vs mixed project work | PrecapNextDay templates and flow-packet-contract.md | Traceability, recap attribution and revised flow/sequence boundaries |
| X05 | Live scope excludes Saturday while operator chose Saturday normal | PrecapWeek and validation/blueprint; Q09 correction | Weekday scope and calendar policy patch |
| X06 | Current Sunday weekly PreCap assumption vs Sunday off | weekly-orchestrator schedule/PrecapWeek; Q09 correction | Define when weekly Precap happens and whether it counts as an explicit Sunday exception |
| X07 | 2026 W45 draft 38h despite 7h/day x5=35h visible windows and unverified meetings | WEEKLY_PRECAP_DRAFT_W45.md/.html | Real interval-based capacity calculation and calendar source flags |
| X08 | Partial HTML/Markdown alternatives being designed before canonical information contract | Q13 decision left open; HTML prototype in research | Choose single source model after real same-fixture comparisons; do not optimize presentation first |
| X09 | "Workflow&Processes" already handles process/sprint-fit but O002 not resolved | Workflow&Processes/SKILL.md; DECISIONS.md | Reuse audit and named-consumer test before new sequencing Skill |
| X10 | Older "locked" macro architecture references archived wrappers | architecture/01-macro-architecture-decision.md vs D012/D013 | Label history/provenance; active D012 remains truth |
| X11 | Broad Session/Sync/ProjectStatus input duplication | PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md | Selective read-on-demand after outputs/authority are coherent |
| X12 | What exactly is the day-level recap and fresh next-day state feed? | historical OperatorResearch, flow-recap, status-merge | Trace existing flow recap + day aggregation and mutation receipt; no new stage until gap confirmed |

## 5. Critical path and ownership — macro BEFORE matrix detail

| Phase | Work package | Blocks | Concrete deliverable | Exit / evidence gate |
|---|---|---|---|---|
| **P0 — system inventory** | Current source hierarchy, stage owner, input/output map, old vs active behavior, reuse-first audit | Everything else | This macro handover, verified source inventory, conflict ledger | Master can explain complete loop and each major handoff in plain language |
| **P1 — information authority** | Resolve OP enrolled PM, repo evidence, Apex-native decisions, calendar, approvals, freshness, failed reads; no duplicated PM state | Every stateful module, especially Matrix 1 and status updates | Source-of-truth matrix + mutation routing decision | Live OP read or explicit unverified boundary; owner for each work-ref type |
| **P2 — vocabulary and stage interfaces** | Sequence vs flow vs sprint vs task; multiple projects inside sequence/sprint; exact recap/day handoff; Sunday planning exception; reuse Workflow&Processes | Both matrices and NextDay/FlowRecap compatibility | End-to-end producer->consumer mini-contract and mixed-project fixture | One task can be traced from Matrix 1 through daily execution to correct PM delta without ID drift |
| **P3 — Matrix 1 design** | Project process progression, epic, dependency, selective detail, shortlist/longlist, provenance | Matrix 2 task selection | Bounded Matrix 1 design handover, accepted Q&A and output fixture | All planned work has actual owner and outcome; no day/time in M1 |
| **P4 — Matrix 2 design** | Capacity, Mon-Sat calendar, movable sequences, variable blocks, mix policy, buffers, dependency-aware weekly allocation | PrecapNextDay and visual Q13 choices | Bounded Matrix 2 design handover, realistic weekly fixture | Arithmetic correct; selected Matrix 1 refs preserved; no fictitious meetings or default-four-per-day requirement |
| **P5 — downstream compatibility** | NextDay sequence -> flow/sprint/cards/prompts -> raw evidence -> recap -> status merge -> OP writeback -> next-day refresh | Production promotion | Cross-stage interface/approval handover with tests and patch targets | Mixed-project fixture passes traceability, candidate/confirmed separation and approved write policy |
| **P6 — presentation decision** | Compare multiple candidate UX/renderings using SAME accepted data and operator user stories (Q13) | Final visual implementation | Accepted single canonical source/view approach and tested prototype | Operator can understand and edit weekly strategy/sequence allocation without touching machine plumbing |
| **P7 — patch integration and fresh trial** | Narrow patches to existing skills/contracts/templates and OpenProject owner routing, not whole-file replacement; fresh-context run and independent reviewers | Final acceptance | Patch packets, actual diffs, real-week + next-day trial, operator signoff | No live stale instructions, no duplicate PM records, no invented source IDs or calendar writes |

Parallelism: P1 (state ownership) and P2 (vocabulary/skill reuse audit) can proceed in parallel **after P0**; P3 and P4 should not freeze production interfaces before both are resolved. P5 may be design-tested concurrently with P3/P4 for consumer feasibility; full P7 integration is gated.

## 6. Decisions that matter BEFORE more Matrix 1/2 Q&A

### Macro Round M-A — authority and recap (cross-feature, L3)
1. **M01**: For each project actually enrolled in OP, which exact WP fields and timestamps are authoritative for priority, status and dependencies, and what is only a repo-derived implementation fact? Need real OP read. Already have preliminary Q01/Q02 operator answers; need enrollment evidence, not a new philosophical debate.
2. **M02**: What is the exact handoff of approved FlowRecap/StatusMerge changes to OP, including approval granularity, failed writes, rereread and next-day refresh? Need current skill route audit. Operator explicitly says reuse existing recap.
3. **M03**: Is "RecapDay" an existing composite workflow or simply the completion of FlowRecap+StatusMerge? Search actual producing and consuming files before creating a new component.

### Macro Round M-B — sequence semantics (cross-feature, L3)
4. **M04**: Can one sequence contain multiple execution flows; can one flow span multiple sequences; and what is the evidence unit when one sprint includes two projects? Decide from current flow contracts and concrete mixed-project fixture.
5. **M05**: Do we actually need a new stateless Sequencing Skill, or can Workflow&Processes + PrecapNextDay + a deterministic interval calculator do the job? Reuse-first comparison, no new wrapper agent.
6. **M06**: Sunday off: on what day does weekly Precap normally run, or is weekly planning on Sunday an explicit operator-controlled exception? Don't silently schedule Sunday.

### Macro Round M-C — output UX (after interfaces, L2/L3)
7. **M07**: What source data model and single-authority artifact will drive Matrix 1/2/NextDay? User Q13 remains OPEN; separate visual variants from source-of-truth choice.
8. **M08**: What is the minimum Matrix 1 granularity and Matrix 2 weekly allocation that preserves an effective daily execution handoff without copying sprint microtasks?
9. **M09**: What constitutes a valid real-week and next-day test with actual OP/calendar evidence and operator comprehension? Reuse W34 and W45 as historical fixtures, not live status.

Decision scales I/E/R and level L0-L3 follow the operator's 2026-11-06 Q&A contract. Existing accepted answers Q01-Q14 remain accepted subject to operator corrections in the new delta; do not re-question decided topics.

## 7. Exact repository sources / ranked read order

### Authority, routing, and project continuity (read first)
1. \`apex-meta/tools/project-improvement-orchestration-weekly/ORCHESTRATOR-DEFINITION.md\`
2. \`apex-meta/tools/project-improvement-orchestration-weekly/PROCESS.md\`
3. \`apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md\` D012/D013 and O002
4. \`apex-meta/tools/project-improvement-orchestration-weekly/CURRENT-STATE.md\`
5. \`apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md\`
6. \`.claude/skills/weekly-orchestrator/SKILL.md\`
7. \`apex-meta/operator-output-design/step3-output-design-system/21-canonical-artifact-family-and-lifecycle-map.okf.yaml\` navigation only
8. \`apex-meta/handoff/weekly-precap-evolution-and-version-audit-handover-20261105.okf.md\` historical-to-current lineage

### Stage contracts to trace, without blindly loading every support file
9. \`.claude/skills/PrecapWeek/SKILL.md\`; \`.claude/skills/PrecapWeek/weekly-command-brief-template.md\`; \`.claude/skills/PrecapWeek/calendar-planning-guidance.md\`
10. \`.claude/skills/PrecapNextDay/SKILL.md\`; \`templates/precap-next-day-brief-template.md\`; \`templates/flow-execution-card-template.md\`; \`references/flow-packet-contract.md\`
11. \`.claude/skills/Workflow&Processes/SKILL.md\`; \`process-stage-taxonomy.md\`; \`workflow-record-contract.md\`
12. \`.claude/skills/raw-flow-dump-normalize/SKILL.md\` conditional evidence normalization
13. \`.claude/skills/flow-recap/SKILL.md\`; \`.claude/skills/flow-recap/references/project-status-delta-contract.md\`
14. \`.claude/skills/status-merge/SKILL.md\`; \`.claude/skills/weekly-orchestrator/references/review-wiring.md\`
15. \`.claude/skills/ProjectStatus/SKILL.md\` derived/optional, not separate authority

### Proposed OP transition and existing matrix handovers (after current runtime is understood)
16. \`apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md\`
17. \`apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/02-CONFLICT-AND-DECISION-LOG.okf.md\`
18. \`leela-spec/agent-skills\` master: \`skills/openproject/SKILL.md\`, \`references/write-policy.md\`, \`client/opCall.js\`
19. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md\` explicit operator corrections
20. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md\` TODO, *not* a confirmed missing component
21. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/ORCHESTRATOR-MATRIX-1-DESIGN-HANDOVER-20261106.okf.md\` and \`ORCHESTRATOR-MATRIX-2-DESIGN-HANDOVER-20261106.okf.md\` **earlier design proposals, now awaiting macro/interface reconciliation**
22. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md\` v4.1 layout accepted but detail conflicts
23. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.md\` and \`.html\` **illustrative fixture**, not live task/calendar truth
24. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/Q13-THREE-SEQUENCING-VIEW-VARIANTS-20261106.html\` UX prototypes, **not selected or promoted**.

### Historical sources (load only to understand rationale)
25. \`apex-meta/kb/Weekly-Orchestrator/OperatorResearch/PersonalOrchestrationProcessFlow.md\` old macro/meso loop, says required RecapDay is removed.
26. \`apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md\` older wrapper-agent topology (superseded by D012).
27. \`apex-meta/kb/Weekly-Orchestrator/indexes/APEX_Weekly_Orchestration_Index_v3.md\` old ranking projection, snapshot dated 2026-07-11, not current authority.

## 8. Immediate next action and execution policy

**NEXT:** Explain this macro loop to operator in a compact diagram/table, verify their understanding at high-level, resolve M04 "sequence vs flow" and M02 "end-of-day merge target" using **real existing skill contracts**. Do not ask the operator to reapprove Q01-Q14. Then turn the accepted macro into a short producer/consumer contract map and **only afterward** refine the Matrix 1/2 handovers.

All existing production-file modifications must be exact-context patch-only with independent diff verification. New design files are allowed as proposed documents; they do not change live behavior. No OpenProject/Calendar mutations or synthetic numeric identifiers.
