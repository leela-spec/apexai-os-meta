# APEX Weekly Orchestration — Ranked Folder and File Index

```yaml
index_metadata:
  repository: leela-spec/apexai-os-meta
  branch: main
  indexing_goal: >
    Build a knowledge base that can explain, validate, and improve the complete
    weekly orchestration flow from project state through weekly planning, daily
    execution, recap, durable state update, and the next planning cycle.
  ranking_scale:
    90_to_100: canonical_core
    75_to_89: major_dependency
    55_to_74: architecture_and_build_support
    30_to_54: secondary_or_historical
    0_to_29: exclude_by_default
```

## 1. Canonical loop

```text
Project state / KB
        ↓
PreCapWeek
        ↓
PreCapNextDay
        ↓
Operator executes flow
        ↓
Raw Flow Dump Normalize
        ↓
FlowRecap
        ↓
Model Usage Log
        ↓
Status Merge / APSU
        ↓
Project KB update
        ↓
Project Status Overview
        ↓
Next PreCapWeek / PreCapNextDay
```

The live control file defines the narrower operational sequence as:

```text
PreCapWeek → PreCapNextDay → Operator execution
→ FlowRecap → APSU → next PreCapNextDay
```

It also assigns operator gates to weekly planning, daily planning, flow completion, recap validation, and high-impact state changes.

---

# 2. Ranked folder list

## Tier A — Index completely

These folders define the weekly orchestration system. Index entrypoints, references, manifests, templates, examples, and scripts where present.

|Rank|Score|Folder|Contribution to weekly flow|Index depth|
|--:|--:|---|---|---|
|**1**|**100**|`.claude/`|Repository control plane, active loop, paths, gates, constraints, active-skill registry|Full|
|**2**|**99**|`.claude/skills/project-kb-manager/`|Durable project-state backbone and accepted project memory|Full|
|**3**|**98**|`.claude/skills/PrecapWeek/`|Weekly direction, project priority mapping, capacity and first daily seed|Full|
|**4**|**98**|`.claude/skills/PrecapNextDay/`|Converts state and weekly direction into executable next-day artifacts|Full|
|**5**|**97**|`.claude/skills/flow-recap/`|Converts execution evidence into reviewable recap and candidate deltas|Full|
|**6**|**96**|`.claude/skills/status-merge/`|Reviews and merges accepted recap deltas into project state|Full|
|**7**|**94**|`.claude/skills/raw-flow-dump-normalize/`|Normalizes messy operator evidence before recap|Full|
|**8**|**93**|`.claude/skills/ProjectStatus/`|Compact cross-project status surface for weekly and daily planning|Full|
|**9**|**90**|`.claude/skills/model-usage-log/`|Planned-versus-actual model usage feedback|Full|
|**10**|**89**|`.claude/skills/AIRouting/`|Tool/model/surface route recommendations and usage planning|Full|
|**11**|**87**|`.claude/skills/PromptEngineer/`|Creates the prompt assets used during planned flows|Full|
|**12**|**85**|`.claude/skills/Workflow&Processes/`|Validates workflow stage, process stage, and expected-output fit|Full|

### Why `project-kb-manager` ranks above the planning skills

It maintains the compact schema-governed source for:

- project status,
    
- milestone state,
    
- consumed FlowRecaps,
    
- next PreCap context,
    
- durable project records and registries.
    

It explicitly does **not** create daily or weekly plans, so its information feeds PreCap without overlapping with it.

### Why both PreCap folders must be indexed separately

`PrecapWeek` owns the weekly frame and first daily seed, while excluding detailed daily plans and prompt generation.

`PrecapNextDay` owns the daily plan, flow packets, prompt-pack references, dependency interfaces, review flags, and calendar-write requests. It delegates its detailed schemas to reference files rather than owning project state.

---

## Tier B — Index completely as architecture and operator-design authority

|Rank|Score|Folder|Contribution|Index depth|
|--:|--:|---|---|---|
|**13**|**88**|`apex-meta/operator-output-design/`|Defines J1–J12 operator jobs, cards, briefs, relationships, and presentation rules|Full|
|**14**|**86**|`apex-meta/kb/claude-code-orchestration-design/`|Conceptual architecture, packet definitions, loop concepts, design rationale|Full|
|**15**|**84**|`state/`|Current accepted state and recap-consumption state|Full, freshness-sensitive|
|**16**|**82**|`artifacts/weekly-plans/`|Historical and current weekly plan instances|Selected + metadata|
|**17**|**82**|`artifacts/next-day-plans/`|Historical and current next-day plan instances|Selected + metadata|
|**18**|**81**|`artifacts/flow-packets/`|Concrete execution-card and flow-packet instances|Selected + metadata|
|**19**|**81**|`artifacts/flow-recap-packets/`|Concrete recap and state-delta evidence|Selected + metadata|
|**20**|**78**|`apex-meta/handoff/WeklyFlow/`|Handoffs, audits, source indexes, architecture decisions and unresolved work|Full, but classify by age|

The active state and artifact locations are declared directly in the root control file:

```yaml
active_paths:
  apex_project_status: state/apex-project-status.md
  consumed_recap_registry: state/consumed-recap-registry.md
  weekly_plan_packets: artifacts/weekly-plans/
  next_day_plans: artifacts/next-day-plans/
  flow_packets: artifacts/flow-packets/
  flow_recap_packets: artifacts/flow-recap-packets/
```

---

## Tier C — Index as project-management and implementation dependencies

These do not define the weekly loop directly, but they influence how it is built, synchronized, validated, and resumed.

|Rank|Score|Folder|Contribution|Index depth|
|--:|--:|---|---|---|
|**21**|**76**|`.claude/skills/apex-plan/`|Decomposition, proposed plans, planning questions and ownership routing|Full|
|**22**|**74**|`.claude/skills/apex-sync/`|Registry synchronization, dependency readiness, drift and ranking logic|Full after canonical files are confirmed|
|**23**|**73**|`.claude/skills/apex-session/`|Session state, controlled mutation, progress and next-session handoff|Full after canonical files are confirmed|
|**24**|**70**|`.claude/skills/apex-kb/`|Source-preserving KB ingestion, retrieval and audit infrastructure|Full|
|**25**|**67**|`.claude/skills/source-authority-and-verdict-packet/`|Evidence authority, confidence and candidate-versus-canonical protection|Full|
|**26**|**58**|`.claude/skills/deterministic-file-promotion/`|Safely promotes selected candidate files into canonical paths|Entrypoint + contracts|
|**27**|**56**|`scripts/`|Deterministic validation, synchronization, indexing or promotion logic|Full code index|
|**28**|**55**|`apex-meta/patch-plans/`|Planned structural repairs and normalization decisions|Metadata + active plans|
|**29**|**52**|`apex-meta/patch-packs/`|Concrete patches that explain intended architecture changes|Metadata + latest validated packs|

---

## Tier D — Index selectively

|Rank|Score|Folder|Use|Index rule|
|--:|--:|---|---|---|
|**30**|**50**|`.claude/skills/prompt-engineering-patterns/`|Generic prompt patterns that may supplement PromptEngineer|Index headings/examples only|
|**31**|**46**|`templates/` outside owning packages|Shared presentation or file templates|Index only referenced templates|
|**32**|**44**|`examples/` outside owning packages|Scenario and test fixtures|Index representative examples|
|**33**|**40**|`validation-reports/`|Historical failures and package audits|Latest reports only|
|**34**|**38**|`_reports/`|Build and migration evidence|Metadata and conclusions|
|**35**|**35**|`_verification/`|Verification traces|Latest relevant verification only|
|**36**|**32**|`.repair-backups/`|Recovery evidence|Do not semantically ingest|
|**37**|**30**|`_recovery_backup_before_apex_package_restore/`|Backup state|File inventory only|
|**38**|**30**|`_restore_staging_apex_packages/`|Temporary migration material|File inventory only|

---

## Tier E — Exclude by default

|Folder|Score|Reason|
|---|--:|---|
|`source-knowledge/`|**5**|Large external source clones; explicitly excluded from normal context and forbidden as a write target|
|generated caches|**0**|No orchestration-definition value|
|binaries and dependency caches|**0**|No semantic indexing value|
|duplicate recovery copies|**0–10**|Cause version and authority contamination|

The root control file explicitly says not to read the recovery, verification, report, validation-report, or `source-knowledge` areas unless specifically requested for recovery or skill conversion.

---

# 3. File-level priority inside every skill folder

Another AI should not index all files with equal weight.

```yaml
skill_file_priority:
  P0:
    - SKILL.md
    - Skill_*.md
    - "*_SKILL*.md"
    reason: invocation_contract_and_ownership

  P1:
    - package-manifest.md
    - "*package-manifest*.md"
    reason: folder_map_and_declared_boundaries

  P2:
    - references/*contract*.md
    - references/*schema*.md
    - references/*rules*.md
    - references/*validation*.md
    reason: canonical_machine_and_handoff_definitions

  P3:
    - templates/*.md
    reason: operator_and_artifact_presentation

  P4:
    - examples/**/*.md
    reason: scenario_and_schema_interpretation

  P5:
    - scripts/*
    reason: deterministic_behavior_and_validation

  P6:
    - "*audit*.md"
    - "*handoff*.md"
    - "*extraction-report*.md"
    reason: history_and_candidate_information_not_automatic_canon
```

---

# 4. Exact high-priority files

## Control and state

```text
.claude/Claude.md
state/apex-project-status.md
state/consumed-recap-registry.md
```

## Weekly planning

```text
.claude/skills/PrecapWeek/Skill_Precap-Week.md
.claude/skills/PrecapWeek/package-manifest.md
.claude/skills/PrecapWeek/references/
```

## Daily planning

```text
.claude/skills/PrecapNextDay/Skill_precap-next-day.md
.claude/skills/PrecapNextDay/package-manifest.md
.claude/skills/PrecapNextDay/references/
.claude/skills/PrecapNextDay/templates/
.claude/skills/PrecapNextDay/examples/
```

The PreCapNextDay entrypoint identifies these schema authorities:

```text
references/input-intake-and-resilience-contract.md
references/daily-plan-output-contract.md
references/flow-packet-contract.md
references/flow-prompt-pack-contract.md
references/prompt-engineering-dependency-contract.md
references/usage-tracking-dependency-contract.md
references/calendar-event-write-contract.md
references/workflow-process-validation-contract.md
references/validation-checklist.md
```

## Execution and recap

```text
.claude/skills/raw-flow-dump-normalize/SKILL.md
.claude/skills/raw-flow-dump-normalize/references/
.claude/skills/raw-flow-dump-normalize/templates/

.claude/skills/flow-recap/SKILL.md
.claude/skills/flow-recap/references/
.claude/skills/flow-recap/templates/
.claude/skills/flow-recap/examples/
```

## State mutation and durable memory

```text
.claude/skills/status-merge/SKILL.md
.claude/skills/status-merge/references/
.claude/skills/status-merge/templates/

.claude/skills/project-kb-manager/SKILL.md
.claude/skills/project-kb-manager/references/
.claude/skills/project-kb-manager/templates/
.claude/skills/project-kb-manager/examples/
.claude/skills/project-kb-manager/package-manifest.md
```

The project KB package specifically points to:

```text
references/project-schema.md
references/domain-overlay-rules.md
references/milestone-logic.md
references/write-rules.md
templates/project-record-template.md
examples/project-record-example.md
package-manifest.md
```

## Cross-project view and feedback

```text
.claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md
.claude/skills/model-usage-log/SKILL.md
.claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md
```

## Prompt and workflow dependencies

```text
.claude/skills/PromptEngineer/SKILL_prompt-engineering.md
.claude/skills/PromptEngineer/references/
.claude/skills/Workflow&Processes/workflow-process-design-SKILL.md
.claude/skills/Workflow&Processes/references/
```

---

# 5. Recommended indexing batches

## Batch 1 — Canonical operational truth

```yaml
include:
  - .claude/Claude.md
  - .claude/skills/project-kb-manager/
  - .claude/skills/PrecapWeek/
  - .claude/skills/PrecapNextDay/
  - .claude/skills/raw-flow-dump-normalize/
  - .claude/skills/flow-recap/
  - .claude/skills/model-usage-log/
  - .claude/skills/status-merge/
  - .claude/skills/ProjectStatus/
  - state/
```

**Purpose:** Reconstruct the actual end-to-end weekly loop and authority boundaries.

## Batch 2 — Execution intelligence

```yaml
include:
  - .claude/skills/AIRouting/
  - .claude/skills/PromptEngineer/
  - .claude/skills/Workflow&Processes/
  - artifacts/weekly-plans/
  - artifacts/next-day-plans/
  - artifacts/flow-packets/
  - artifacts/flow-recap-packets/
```

**Purpose:** Explain how plans become executable prompts, routes, flows and evidence.

## Batch 3 — Operator-facing architecture

```yaml
include:
  - apex-meta/operator-output-design/
  - apex-meta/kb/claude-code-orchestration-design/
  - apex-meta/handoff/WeklyFlow/
```

**Purpose:** Capture the J1–J12 artifact system, presentation decisions, user stories, and architecture rationale.

## Batch 4 — Build and governance support

```yaml
include:
  - .claude/skills/apex-plan/
  - .claude/skills/apex-sync/
  - .claude/skills/apex-session/
  - .claude/skills/apex-kb/
  - .claude/skills/source-authority-and-verdict-packet/
  - .claude/skills/deterministic-file-promotion/
  - scripts/
  - apex-meta/patch-plans/
```

**Purpose:** Explain how the orchestration system itself is planned, audited, synchronized and safely changed.

---

# 6. Metadata every indexed chunk should carry

```yaml
required_chunk_metadata:
  repository: leela-spec/apexai-os-meta
  branch: main
  path: exact_repo_path
  folder_role:
    allowed:
      - control_plane
      - project_state
      - weekly_planning
      - daily_planning
      - execution_support
      - evidence_normalization
      - recap
      - usage_feedback
      - status_merge
      - durable_memory
      - operator_output_design
      - build_support
      - historical
  authority_status:
    allowed:
      - canonical_live
      - canonical_reference
      - active_template
      - active_example
      - candidate
      - extraction_report_only
      - historical
      - backup
  artifact_owner: owning_skill_or_package
  artifact_type: skill_contract_or_reference_or_template_or_example_or_state
  loop_stage: P0_to_P9_or_cross_cutting
  valid_from: commit_or_last_modified_date
  freshness:
    allowed:
      - current
      - potentially_stale
      - historical
      - unknown
  mutation_authority: skill_or_operator_gate
  upstream_dependencies: []
  downstream_consumers: []
  candidate_vs_accepted:
    allowed:
      - accepted
      - candidate
      - mixed
      - not_applicable
```

---

# 7. Important audit warnings

## A. Current root authority supersedes older indexes

Older project-source indexes described several loop skills as missing or candidate-only. The live root file now states that all nine core skills are present. Use the live root and actual skill files as current authority.

## B. High-value files still contain formatting defects

`PrecapWeek` currently contains collapsed machine blocks, although its planning logic is clear.

`PrecapNextDay` is still wrapped in an outer Markdown code fence.

These files remain important indexing sources, but the KB must record:

```yaml
formatting_status:
  semantic_content_valid: likely
  final_entrypoint_format_valid: false_or_needs_review
```

## C. Do not collapse candidate and accepted state

The index must distinguish:

- FlowRecap candidate changes,
    
- Status Merge proposals,
    
- operator-approved changes,
    
- durable KB records,
    
- compact Project Status views.
    

Otherwise retrieval will present proposals as accepted facts.

## D. Avoid duplicate ingestion

Do not ingest the same contract independently from:

- active skill folders,
    
- handover copies,
    
- patch-plan excerpts,
    
- backup directories,
    
- extraction reports.
    

Use the active skill path as canonical and keep other copies as provenance links only.

---

# 8. Final indexing priority

```yaml
final_priority:
  index_first:
    - .claude/Claude.md
    - .claude/skills/project-kb-manager/
    - .claude/skills/PrecapWeek/
    - .claude/skills/PrecapNextDay/
    - .claude/skills/raw-flow-dump-normalize/
    - .claude/skills/flow-recap/
    - .claude/skills/status-merge/
    - .claude/skills/ProjectStatus/
    - state/

  index_second:
    - .claude/skills/model-usage-log/
    - .claude/skills/AIRouting/
    - .claude/skills/PromptEngineer/
    - .claude/skills/Workflow&Processes/
    - apex-meta/operator-output-design/
    - artifacts/

  index_third:
    - apex-meta/kb/claude-code-orchestration-design/
    - .claude/skills/apex-plan/
    - .claude/skills/apex-sync/
    - .claude/skills/apex-session/
    - .claude/skills/apex-kb/
    - scripts/

  provenance_only:
    - apex-meta/handoff/WeklyFlow/
    - apex-meta/patch-plans/
    - apex-meta/patch-packs/
    - validation-reports/
    - _reports/
    - _verification/

  exclude:
    - source-knowledge/
    - .repair-backups/
    - _recovery_backup_before_apex_package_restore/
    - _restore_staging_apex_packages/
    - dependency_caches
    - generated_binaries
```