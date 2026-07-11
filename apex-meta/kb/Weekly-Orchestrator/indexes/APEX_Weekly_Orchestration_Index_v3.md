# APEX Weekly Orchestration — Master Repo and Retrieval Index v3

```yaml
index:
  id: apex-weekly-orchestration-index-v3
  version: "3.0"
  generated_on: "2026-07-11"
  repository: leela-spec/apexai-os-meta
  branch: main
  inspected_head: f4c81bf7fe5ad00b9bab6b83026071a7bb96d884
  purpose: >
    Give another AI a compact, source-ranked map of what the weekly flow is,
    which files define current truth, where every operator artifact lives,
    what should be loaded for each task, and which sources are stale,
    historical, duplicated, or excluded.
```

## 0. Executive update

The previous index correctly identified the major weekly-flow skill families, but the repository has advanced substantially.

### Material changes now reflected

1. **Step 3 is closed out:** the J1–J12 design family, lifecycle language, and state-transition boundaries are recorded.
2. **Step 4 exists:** a production-ready central template family now contains J1–J12 plus J6a.
3. **Step 5 is complete:** all 13 templates were promoted into their owning live skill packages.
4. **Step 6 is active:** 13/13 invocation tests passed, links resolve, lifecycle simulation passed, and the templates are `active_and_ready`.
5. **`apex-sync` and `apex-session` are live packages:** they are no longer extraction-report-only.
6. **A new `fable-orchestrator/` initiative exists:** it is the active future architecture effort, not the current weekly-loop runtime.
7. **A dedicated Weekly-Orchestrator research folder exists:** it preserves the original macro/meso flow and information-process architecture.
8. **The root state layer is not usable as current truth:** both files under `state/` are empty; the actual project registry is under `.claude/kb/`, which is itself incomplete and stale.

## 1. The two loops that must not be confused

### Current operational loop

```text
Project KB / accepted project context
  -> PreCapWeek
  -> PreCapNextDay
  -> Operator executes a planned flow
  -> RawFlowDumpNormalize
  -> FlowRecap
  -> ModelUsageLog
  -> StatusMerge
  -> ProjectKB durable update
  -> ProjectStatus overview
  -> next PreCapWeek or PreCapNextDay
```

### Current operator-artifact lifecycle

```text
Planning:       J1 -> J2 -> J3
Execution:      J3 -> J4 -> J5 -> operator execution -> J6 or J6a
Recap/learning: J6 -> J7 -> J8
Durable state:  J7 -> J9 -> J10 -> J11
Routing:        J8 + J11 -> J12 -> J4/J5 only after operator approval
```

### Future architecture initiative

`apex-meta/fable-orchestrator/` is building the next unified Claude Code orchestration architecture by reconciling:

- `apex-plan` / `apex-sync` / `apex-session`;
- the old Apex agent-swarm knowledge bases;
- the current Claude Code orchestration-design KB.

It is **not** the authority for current weekly-flow execution or J1–J12 template behavior.

## 2. Status and authority precedence

When files disagree, use this order.

| Rank | Authority class | Use | Primary sources |
|---|---|---|---|
| 1 | live_domain_authority | Current behavior, schema ownership, boundaries, and invocation. | `.claude/Claude.md`<br>`.claude/skills/<owner>/SKILL.md or live named entrypoint`<br>`.claude/skills/<owner>/references/*contract*.md` |
| 2 | activation_truth | Whether promoted operator templates are active and validated. | `apex-meta/operator-output-design/step6-activation-validation/00-activation-validation-report.okf.md` |
| 3 | promotion_truth | Exact J1-J12 source-to-owner target mapping. | `apex-meta/operator-output-design/step5-template-promotion/02-template-promotion-map.yaml` |
| 4 | live_package_inventory | Package files, read_when rules, references, examples, and retained templates. | `.claude/skills/<owner>/*manifest*.md` |
| 5 | production_presentation_source | Canonical blank template family, examples, design decisions, and validation. | `apex-meta/operator-output-design/step4-operator-template-system/package-manifest.yaml`<br>`apex-meta/operator-output-design/step4-operator-template-system/00_README.md` |
| 6 | accepted_design_rationale | J1-J12 design rationale, lifecycle relationships, vocabulary, and Round 6 closeout. | `apex-meta/operator-output-design/step3-output-design-system/` |
| 7 | operator_intent_authority | Verified user stories, value language, and locked output jobs. | `apex-meta/operator-output-design/step2-operator-user-stories/` |
| 8 | research_and_provenance | Historical rationale, experiments, handoffs, patch evidence, and superseded designs. | `apex-meta/kb/Weekly-Orchestrator/OperatorResearch/`<br>`apex-meta/handoff/`<br>`apex-meta/patch-packs/`<br>`apex-meta/kb/old-apex-full-orchestration-agent-kb*/` |

### Critical precedence examples

- **Template activation:** Step 6 overrides the stale `templates_created: false` field in the Step 3 manifest.
- **Template location:** Step 5 promotion map overrides guesses based on artifact names.
- **Schema and behavior:** the owning live skill and its reference contract override Step 3/4 presentation files.
- **Operator intent:** Step 2 explains why an artifact exists, but does not define its schema.
- **Historical weekly sources:** use them to understand intent and discarded assumptions, not to overwrite current skill contracts.

## 3. Fast retrieval profiles

### A. Understand the system in about one minute

Read only:

1. `.claude/Claude.md`
2. `apex-meta/operator-output-design/step4-operator-template-system/00_README.md`
3. `apex-meta/operator-output-design/step4-operator-template-system/package-manifest.yaml`
4. `apex-meta/operator-output-design/step6-activation-validation/00-activation-validation-report.okf.md`

### B. Run or audit the current weekly loop

Read the root control file, then only the invoked package entrypoint and its manifest:

```text
.claude/skills/project-kb-manager/
.claude/skills/PrecapWeek/
.claude/skills/PrecapNextDay/
.claude/skills/raw-flow-dump-normalize/
.claude/skills/flow-recap/
.claude/skills/model-usage-log/
.claude/skills/status-merge/
.claude/skills/ProjectStatus/
.claude/skills/AIRouting/
```

Load `PromptEngineer/` and `Workflow&Processes/` only when prompt construction or workflow/process validation is required.

### C. Resolve a J1–J12 template owner

Read in this order:

1. Step 6 activation report.
2. Step 5 `02-template-promotion-map.yaml`.
3. The owning package manifest.
4. The promoted live template.
5. The owning entrypoint/contract when field meaning matters.
6. The Step 4 central template only for the retained source form.
7. Step 3 only for design rationale.

### D. Reconstruct the original weekly-flow intent

Read:

```text
apex-meta/kb/Weekly-Orchestrator/OperatorResearch/WeeklyRoutine_Overview_Marco&Meso.md
apex-meta/kb/Weekly-Orchestrator/OperatorResearch/PersonalOrchestrationProcessFlow.md
apex-meta/kb/Weekly-Orchestrator/OperatorResearch/WeeklyRoutine_Detailed.md
```

Do not load the `v2(v1maybestillvalid)` copy separately: it currently has the same blob hash as `WeeklyRoutine_Detailed.md`.

### E. Work on the future unified orchestrator

Start with:

```text
apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md
apex-meta/fable-orchestrator/00-START-HERE.md
```

Then follow the reading order inside `00-START-HERE.md`.

## 4. Complete operator artifact map

| ID | Canonical artifact | Live owner | Dominant job | Promoted live path | Downstream |
|---|---|---|---|---|---|
| J1 | Project_State_Success_Card | project-kb-manager | Establish project reality safe for planning. | .claude/skills/project-kb-manager/templates/project-state-success-card-template.md | J2, J3 |
| J2 | Weekly_Command_Brief | PrecapWeek | Turn accepted context into weekly direction. | .claude/skills/PrecapWeek/weekly-command-brief-template.md | J3 |
| J3 | PreCap_Next_Day_Brief | PrecapNextDay | Present tomorrow's compact multi-flow outline. | .claude/skills/PrecapNextDay/templates/precap-next-day-brief-template.md | J4 |
| J4 | Flow_Execution_Card | PrecapNextDay | Make one flow executable as a complete three-sprint workspace. | .claude/skills/PrecapNextDay/templates/flow-execution-card-template.md | J5, operator_execution, J6 |
| J5 | Prompt_Files_and_Index | PrecapNextDay presentation; PromptEngineer owns prompt doctrine | Provide direct prompt-file access without duplicating execution context. | .claude/skills/PrecapNextDay/templates/prompt-files-and-index-template.md | operator_execution |
| J6 | Execution_Evidence_Handoff | raw-flow-dump-normalize | Normalize and organize execution evidence without interpreting project meaning. | .claude/skills/raw-flow-dump-normalize/templates/execution-evidence-handoff-template.md | J7 |
| J6a | Skip_Marker | raw-flow-dump-normalize | Record why a planned flow was not executed. | .claude/skills/raw-flow-dump-normalize/templates/skip-marker-template.md | next_planning_review, J7_when_relevant |
| J7 | FlowRecap_Result_Card | flow-recap | Interpret evidence and expose candidate-only project-state changes. | .claude/skills/flow-recap/templates/flowrecap-result-card-template.md | J8, J9 |
| J8 | Usage_Learning_Card | model-usage-log | Capture evidence-bound planned-versus-actual AI usage learning. | .claude/skills/model-usage-log/templates/usage-learning-card-template.md | J12 |
| J9 | Status_Merge_Decision_Card | status-merge | Record operator disposition of candidate project-state changes. | .claude/skills/status-merge/templates/status-merge-decision-card-template.md | J10 |
| J10 | Project_KB_Update_Card | project-kb-manager | Expose the prepared or actual durable project-KB write and result evidence. | .claude/skills/project-kb-manager/templates/project-kb-update-card-template.md | J11_after_confirmed_write |
| J11 | Project_Status_Overview | ProjectStatus | Project confirmed accepted truth across active projects. | .claude/skills/ProjectStatus/project-status-overview-template.md | J2, J3, J12 |
| J12 | AI_Routing_Card | AIRouting | Recommend an AI route and record the separate operator decision. | .claude/skills/AIRouting/ai-routing-card-template.md | J4_after_approval, J5_after_approval |

### State language that must remain separate

| Stage | Safe meaning | Forbidden collapse |
|---|---|---|
| J6 | Evidence organized | Evidence interpreted as project truth |
| J7 | Flow result and candidate changes | Candidate treated as accepted state |
| J9 | Operator merge disposition | Approval presented as durable write |
| J10 | Prepared/executed write plus result evidence | Prepared update presented as confirmed overview truth |
| J11 | Confirmed accepted overview with freshness | New candidate state |
| J12 | Recommendation plus separate operator route decision | Recommendation treated as execution authorization |

## 5. Ranked folder and file index

| Rank | Priority | Path | Authority | Freshness | Role | Index depth |
|---|---|---|---|---|---|---|
| 1 | 100 | .claude/Claude.md | live_control_plane | current_with_known_drift | Defines the active loop, trigger phrases, skill paths, artifact paths, gates, and repository constraints. | full |
| 2 | 99 | apex-meta/operator-output-design/step6-activation-validation/ | activation_truth | current | Proves that all 13 promoted templates are present, linked, invocation-tested, and lifecycle-valid. | full |
| 3 | 99 | apex-meta/operator-output-design/step4-operator-template-system/ | production_presentation_source | current | Production-ready J1-J12 plus J6a template family, design decisions, examples, lifecycle, and validation. | full |
| 4 | 98 | apex-meta/operator-output-design/step5-template-promotion/ | promotion_truth | current | Maps each central template to its owning live skill package and target path. | full |
| 5 | 98 | .claude/skills/project-kb-manager/ | live_domain_authority | current_with_manifest_cleanup_needed | Durable project memory, project schema, recap idempotency, orchestration-state handoff, J1, and J10. | full |
| 6 | 97 | .claude/skills/PrecapWeek/ | live_domain_authority | partial | Weekly direction, calendar/capacity framing, first next-day seed, and J2. | full_except_missing_refs |
| 7 | 97 | .claude/skills/PrecapNextDay/ | live_domain_authority | current_with_path_drift | Daily planning, flow packets, prompt indexes, flow execution cards, and J3-J5. | full |
| 8 | 96 | .claude/skills/raw-flow-dump-normalize/ | live_domain_authority | current | Evidence normalization, source capture, completion-state normalization, J6, and J6a. | full |
| 9 | 96 | .claude/skills/flow-recap/ | live_domain_authority | current | Flow interpretation, recap packet, candidate project-state delta, candidate usage delta, and J7. | full |
| 10 | 95 | .claude/skills/status-merge/ | live_domain_authority | current | Candidate-delta review, conflict surfacing, merge proposal, next-day context, and J9. | full |
| 11 | 94 | .claude/skills/model-usage-log/ | live_domain_authority | current | Post-execution usage delta, usage summary, route reuse/avoid learning, and J8. | full |
| 12 | 94 | .claude/skills/ProjectStatus/ | live_domain_authority | current_with_path_drift | Compact cross-project confirmed overview and J11; not a durable database or planner. | full |
| 13 | 93 | .claude/skills/AIRouting/ | live_domain_authority | current_with_build_residue | Advisory route selection, planned usage context, scarcity/cost tradeoffs, and J12. | full |
| 14 | 92 | .claude/skills/PromptEngineer/ | live_domain_authority | current_with_formatting_debt | Owns prompt packets, copy-paste prompt doctrine, provider adaptation, and prompt-quality review. | full |
| 15 | 91 | .claude/skills/Workflow&Processes/ | live_domain_authority | current_with_build_residue | Workflow/process taxonomies, expected-output types, workflow records, and prompt-process alignment. | full |
| 16 | 90 | .claude/kb/ | live_state_data | incomplete_and_stale | Actual project registry and recap-idempotency data used by project-kb-manager. | targeted |
| 17 | 89 | apex-meta/operator-output-design/step3-output-design-system/ | accepted_design_rationale | mixed | J1-J12 design rationale, shared anatomy, relationships, vocabulary, Round 6 reconciliation, and Step 4 handoff. | targeted_by_artifact |
| 18 | 88 | apex-meta/operator-output-design/step2-operator-user-stories/ | operator_intent_authority | verified | Operator-verified user stories, value language, output jobs, and Step 3 handoff. | targeted |
| 19 | 87 | apex-meta/kb/Weekly-Orchestrator/OperatorResearch/ | weekly_flow_research_source | historical_design_source | Macro/meso routine, artifact-flow architecture, fixed-flow assumptions, and pre-runtime design work. | targeted |
| 20 | 86 | .claude/skills/apex-plan/ | live_support_skill | current | Project capture, decomposition, qualitative priority/urgency, and provisional focus rationale. | full |
| 21 | 86 | .claude/skills/apex-sync/ | live_support_skill | current | Deterministic next-action, blocker, drift, registry, stale-task, and scoring reports. | full |
| 22 | 86 | .claude/skills/apex-session/ | live_support_skill | current | Gated status mutation records, session handoffs, state deltas, and next-session planning feed. | full |
| 23 | 83 | apex-meta/kb/claude-code-orchestration-design/ | primary_best_practice_kb | live_compiled | General Claude Code orchestration doctrine and weekly-routine case-study summaries. | wiki_summaries_first |
| 24 | 82 | apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md | repo_orientation_index | current_but_incomplete | Maps orchestration KBs, handoff clusters, core skills, superseded sources, and known overlaps. | full |
| 25 | 80 | apex-meta/fable-orchestrator/ | future_architecture_initiative | active_milestone_1 | Decision-locked future effort to reconcile old agent-swarm and plan/sync/session systems into a final Claude Code orchestration architecture. | follow_00_START_HERE |
| 26 | 75 | apex-meta/handoff/ | provenance_and_continuation | mixed | Handoffs, recovery notes, research syntheses, and next-chat continuation instructions. | targeted_only |
| 27 | 70 | apex-meta/patch-packs/ | implementation_evidence | mixed | Validated patch artifacts and application evidence, including Step 5 promotion and Step 6 activation. | manifest_and_validation_first |
| 28 | 65 | apex-meta/kb/old-apex-full-orchestration-agent-kb*/ | historical_load_bearing_evidence | historical | Old agent-swarm roles, handoff rules, state-machine lessons, and source doctrine cited by live specs. | targeted |
| 29 | 20 | state/ | declared_placeholder_paths | empty | Root control file declares project status and recap registry here, but both current files are empty. | metadata_only |
| 30 | 10 | source-knowledge/ and recovery/report folders | excluded_or_archival | mixed | Large cloned sources, backups, recovery snapshots, and generated reports. | none |

## 6. Core package navigation

### 6.1 Project state and durable memory

#### `.claude/skills/project-kb-manager/`

Read first:

```text
SKILL.md
package-manifest.md
references/project-schema.md
references/apex-orchestration-state-packet-contract.md
references/write-rules.md
```

Read conditionally:

```text
references/domain-overlay-rules.md
references/milestone-logic.md
templates/project-record-template.md
templates/apex-orchestration-state-packet-template.md
examples/project-record-example.md
examples/four-project-orchestration-state-packet-example.md
```

Default promoted human views:

```text
templates/project-state-success-card-template.md       # J1
templates/project-kb-update-card-template.md           # J10
```

Data paths declared by the package:

```text
.claude/kb/registry.md
.claude/kb/projects/<project-id>.md
.claude/kb/consumed-recap-registry.md
.claude/kb/next-precap-context.md
```

Current data warning: only the registry and consumed-recap registry were verified. The project record and next-precap context are absent.

### 6.2 Weekly planning

#### `.claude/skills/PrecapWeek/`

```text
Skill_Precap-Week.md
package-manifest.md
weekly-command-brief-template.md                       # J2
references/calendar-planning-guidance.md               # declared
references/weekly-plan-output-contract.md              # declared, currently missing
references/weekly-blueprint-standard.md                 # declared
references/weekly-blueprint-meeting-example.md         # declared
references/validation-checklist.md                      # declared
```

Use the entrypoint and J2 template now. Treat the missing weekly output contract as a blocking source gap for strict schema validation.

### 6.3 Next-day and flow preparation

#### `.claude/skills/PrecapNextDay/`

Control and contracts:

```text
Skill_precap-next-day.md
precap-next-day-package-manifest.md
references/input-intake-and-resilience-contract.md
references/daily-plan-output-contract.md
references/flow-packet-contract.md
references/flow-prompt-pack-contract.md
references/prompt-engineering-dependency-contract.md
references/usage-tracking-dependency-contract.md
references/calendar-event-write-contract.md
references/workflow-process-validation-contract.md
references/validation-checklist.md
references/operator-output-format-design.md
```

Promoted current human views:

```text
templates/precap-next-day-brief-template.md             # J3
templates/flow-execution-card-template.md               # J4
templates/prompt-files-and-index-template.md            # J5
```

Older package-specific presentation files remain useful only for contract-oriented comparison:

```text
templates/next-day-plan-operator-template.md
templates/flow-packet-template.md
templates/flow-prompt-pack-template.md
templates/capture-and-handoff-template.md
templates/calendar-event-write-request-template.md
templates/usage-tracking-summary-template.md
examples/apex-only-template-example/
```

### 6.4 Evidence, recap, learning, merge

#### `.claude/skills/raw-flow-dump-normalize/`

```text
SKILL.md
package-manifest.md
references/raw-flow-dump-contract.md
references/skipped-flow-marker-contract.md
templates/raw-flow-dump-template.md
templates/execution-evidence-handoff-template.md         # J6 default human view
templates/skip-marker-template.md                       # J6a
examples/apex-minimal-raw-flow-dump-example.md
```

#### `.claude/skills/flow-recap/`

```text
SKILL.md
package-manifest.md
references/flow-recap-packet-contract.md
references/project-status-delta-contract.md
templates/flow-recap-packet-template.md
templates/flowrecap-result-card-template.md             # J7 default human view
examples/apex-minimal-flow-recap-example.md
```

#### `.claude/skills/model-usage-log/`

```text
SKILL.md
package-manifest.md
references/model-usage-delta-contract.md
references/usage-summary-contract.md
templates/model-usage-delta-template.md
templates/usage-learning-card-template.md               # J8 default human view
examples/apex-minimal-model-usage-example.md
```

#### `.claude/skills/status-merge/`

```text
SKILL.md
package-manifest.md
references/status-merge-packet-contract.md
references/next-precaphandoff-context-contract.md
templates/status-merge-packet-template.md
templates/status-merge-decision-card-template.md        # J9 default human view
examples/apex-minimal-status-merge-example.md
```

### 6.5 Confirmed overview and routing

#### `.claude/skills/ProjectStatus/`

```text
project-status-overview_SKILL_v3.md
package-manifest.md
project-status-overview-contract_v2_fixed.md
ranking-and-validation-rules*.md
current-project-status-overview-template*.md
project-status-overview-template.md                     # J11 default human view
starter-manual-test-overview*.md
```

#### `.claude/skills/AIRouting/`

```text
ai-routing-and-usage-tracking-SKILL.md
ai-routing-and-usage-tracking-package-manifest.md
routing-recommendation-packet-contract.md
AI-surface-inventory-contract.md
monthly-quota-map-contract.md
routing-decision-contract.md
planned-usage-budget-contract.md
usage-delta-contract.md
cost-class-and-scarcity-rules.md
starter-usage-routing-example.md
ai-routing-card-template.md                             # J12
```

### 6.6 Prompt and workflow dependencies

#### `.claude/skills/PromptEngineer/`

```text
SKILL_prompt-engineering.md
package-manifest.md
references/prompt-packet-contract.md
references/prompt-task-taxonomy.md
references/iteration-loop-patterns.md
references/provider-style-contract-chatgpt.md
references/provider-style-contract-claude.md
references/provider-style-contract-gemini.md
references/provider-style-contract-openrouter-todo.md
references/prompt-quality-validation.md
references/prompt-learning-feedback-contract.md
examples/starter-prompt-pack-example.md
```

#### `.claude/skills/Workflow&Processes/`

```text
workflow-process-design-SKILL.md
workflow-process-design-package-manifest.md
workflow-stage-taxonomy.md
process-stage-taxonomy.md
expected-output-type-contract.md
workflow-record-contract.md
prompt-process-alignment-validation.md
operator-validation-and-conflict-resolution.md
starter-workflow-process-example.md
```

## 7. Operator-output design chain

### Step 2 — verified operator intent

`apex-meta/operator-output-design/step2-operator-user-stories/`

- `00-package-manifest.okf.yaml`
- `01-verification-decisions.okf.yaml`
- `02-macro-loop-and-value-frame.okf.yaml`
- `03-planning-side-user-stories.okf.yaml`
- `04-execution-recap-user-stories.okf.yaml`
- `05-status-learning-user-stories.okf.yaml`
- `06-output-jobs-and-artifact-family.okf.yaml`
- `07-step3-handoff-brief.okf.md`
- `08-step3-next-chat-handover.okf.md`

### Step 3 — accepted design rationale

`apex-meta/operator-output-design/step3-output-design-system/`

Load by need, not all at once:

- `00-package-manifest.okf.yaml`: inventory only.
- `01`–`19`: artifact and relationship designs.
- `20-round6-cross-cutting-consistency-resolution.okf.yaml`: vocabulary translation.
- `21-canonical-artifact-family-and-lifecycle-map.okf.yaml`: canonical navigation/lifecycle.
- `22-round6-decision-and-verification-record.okf.yaml`: closeout and mutation boundary.
- `23-step4-template-implementation-handoff.okf.md`: historical implementation handoff.

### Step 4 — production template source

`apex-meta/operator-output-design/step4-operator-template-system/`

This is the central retained template family. Use the promoted owner copy for live invocation and the Step 4 copy for family-level comparison, examples, research, and validation.

### Step 5 — promotion proof

`apex-meta/operator-output-design/step5-template-promotion/`

- `01-live-owner-inventory.md`: pre-promotion snapshot; historical.
- `02-template-promotion-map.yaml`: canonical owner/target map.
- `03-static-lifecycle-simulation.md`: static lifecycle check.

### Step 6 — activation proof

`apex-meta/operator-output-design/step6-activation-validation/`

The activation report is the current status authority: 13 templates found, 13 passed, no failures, lifecycle pass, `active_and_ready`.

## 8. Gap and drift register

| ID | Severity | Issue | Required index behavior |
|---|---|---|---|
| G01 | high | Root state authority is split and unusable as written. | Prefer .claude/kb for project-state retrieval; label root state paths as placeholders. |
| G02 | high | PrecapWeek package manifest references files absent from main. | Do not claim the full weekly output contract is live; use entrypoint + J2 template + historical weekly research with a gap flag. |
| G03 | medium | Step 3 manifest has stale implementation status. | Use Step 6 for activation status and Step 3 only for design rationale. |
| G04 | medium | Root skill count is stale. | Index the ten named entries; retain the count mismatch as a control-file defect. |
| G05 | medium | Path and filename casing drift remains. | Store both actual_path and canonical_target; resolve reads to actual_path. |
| G06 | medium | Template layers overlap. | Use promoted J-card as default human view; use original template for contract-oriented drafting or legacy comparison. |
| G07 | medium | State KB is incomplete and stale. | Mark project-state outputs low confidence until refreshed. |
| G08 | low | Historical weekly detailed files are duplicates. | Index one canonical content record and store the second path as alias. |
| G09 | medium | Several package files retain generation residue or formatting debt. | Treat semantic content as usable but quality status as needs_cleanup. |

## 9. Deduplication and token-efficiency rules

1. Index one canonical live path per semantic source.
2. Store aliases instead of indexing byte-identical duplicates.
3. Use package manifests for navigation, not as a substitute for contracts.
4. Use the promoted J-card as the default operator view.
5. Keep the original package template as a secondary contract-oriented view.
6. Do not ingest central Step 4 and promoted live copies as unrelated knowledge; link them by `artifact_id`.
7. Do not treat Step 2/3 prose as live schema authority.
8. Do not index patch bodies unless the question concerns implementation history.
9. Do not semantically index generated `.sqlite`, `.json`, or `.ndjson` retrieval indexes when their source wiki pages are already indexed.
10. Exclude backups, recovery folders, `source-knowledge/`, and old-version copies unless a live source explicitly cites them.
11. Preserve the old non-v2 orchestration KB as targeted evidence because live specs cite it.
12. Keep candidate, approved, written, and confirmed state as separate retrieval concepts.

## 10. Recommended chunk metadata

```yaml
required_metadata:
  repository: leela-spec/apexai-os-meta
  branch: main
  inspected_head: f4c81bf7fe5ad00b9bab6b83026071a7bb96d884
  path: exact_repo_path
  record_type: file | folder | artifact | contract | template | example | state | provenance
  authority_class: live_domain_authority | activation_truth | promotion_truth | presentation_source | design_rationale | operator_intent | provenance
  freshness: current | partial | stale | historical | empty | unknown
  artifact_id: J1_to_J12_or_J6a_or_none
  owner_package: package_or_none
  loop_stage: project_state | weekly | daily | execution | evidence | recap | learning | merge | durable_write | overview | routing | support
  candidate_state: accepted | candidate | proposal | confirmed | not_applicable
  canonical_path: exact_current_path
  aliases: []
  upstream: []
  downstream: []
  read_when: compact_trigger
  do_not_use_when: compact_negative_trigger
  source_hash_or_commit: optional
```

## 11. Final indexing batches

### Batch A — current operational truth

```text
.claude/Claude.md
.claude/skills/project-kb-manager/
.claude/skills/PrecapWeek/
.claude/skills/PrecapNextDay/
.claude/skills/raw-flow-dump-normalize/
.claude/skills/flow-recap/
.claude/skills/model-usage-log/
.claude/skills/status-merge/
.claude/skills/ProjectStatus/
.claude/skills/AIRouting/
.claude/skills/PromptEngineer/
.claude/skills/Workflow&Processes/
.claude/kb/
```

### Batch B — active operator-output system

```text
apex-meta/operator-output-design/step4-operator-template-system/
apex-meta/operator-output-design/step5-template-promotion/
apex-meta/operator-output-design/step6-activation-validation/
```

### Batch C — intent and rationale

```text
apex-meta/operator-output-design/step2-operator-user-stories/
apex-meta/operator-output-design/step3-output-design-system/
apex-meta/kb/Weekly-Orchestrator/OperatorResearch/
```

### Batch D — planning/session support

```text
.claude/skills/apex-plan/
.claude/skills/apex-sync/
.claude/skills/apex-session/
.claude/skills/apex-kb/
```

### Batch E — architecture and future system

```text
apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md
apex-meta/kb/claude-code-orchestration-design/
apex-meta/fable-orchestrator/
apex-meta/handoff/agent-skill-system-research/
```

### Provenance only

```text
apex-meta/patch-packs/
apex-meta/handoff/
apex-meta/kb/old-apex-full-orchestration-agent-kb*/
```

### Exclude by default

```text
source-knowledge/
.repair-backups/
_recovery_backup_before_apex_package_restore/
_restore_staging_apex_packages/
_verification/
_reports/
validation-reports/
ApexDefinition&OldVersions/
generated bytecode and dependency caches
```

## 12. Companion machine files

- `APEX_Weekly_Orchestration_Index_v3.yaml`: hierarchical machine index.
- `APEX_Weekly_Orchestration_Index_v3.jsonl`: one retrieval record per authority rule, profile, artifact, resource, and gap.
