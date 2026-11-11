# PrecapWeek Input Pipeline — Decision-Support Handover

## Mission

Continue the PrecapWeek input-pipeline review in a new chat, but do **not** ask the operator to decide from abstract architecture language.

The previous audit found several likely context-cost and duplication problems, but the operator explicitly could not answer the questions because the options were not concrete enough.

Your job is therefore to make the choices **visually and operationally understandable first**, then ask the Q&A.

Do not implement production changes in this run.

---

## Operator requirement

For every meaningful decision, first show enough concrete evidence that the operator can understand:

- what PrecapWeek currently receives;
- where each input comes from;
- what the actual content looks like;
- what overlaps with another input;
- how much context/complexity it adds;
- what would be lost if it were removed or made on-demand;
- what the proposed simpler pipeline would look like in practice.

Use **examples, snapshots, before/after payloads, mini diagrams, and real W34 excerpts**.

Only after that explanation should you present the formal Q&A decision block.

---

## Hard constraints

```okf
handover_constraints:
  implementation:
    allowed: false
    production_file_mutation: false

  patch_policy:
    existing_files: patch_only
    this_run: research_and_decision_support_only

  source_priority:
    1: live_production_skill_contracts
    2: current_W34_runtime_artifacts
    3: current_module_design_decisions
    4: historical_material_only_when_needed_for_context

  reasoning_style:
    required:
      - concrete_examples_before_questions
      - value_vs_context_cost_analysis
      - distinguish_duplicate_data_from_complementary_data
      - distinguish_authority_from_projection
      - show_what_is_loaded_by_default_vs_on_demand
      - preserve_current_runtime_boundaries

  forbidden:
    - create_new_architecture_layer_without_need
    - create_new_persisted_input_packet_as_default_solution
    - ask_operator_to_choose_based_only_on_schema_names
    - treat_deterministic_data_as_automatically_high_value
    - assume_more_context_is_safer
    - silently_reopen_already_validated_Module_01_output_decisions
```

---

## Current production pipeline to reconstruct

Start from the current live `PrecapWeek` skill and trace every normal or fallback input to its producer.

At minimum inspect:

1. `.claude/skills/PrecapWeek/SKILL.md`
2. `.claude/skills/PrecapWeek/calendar-planning-guidance.md`
3. `.claude/skills/PrecapWeek/weekly-blueprint-standard.md`
4. `.claude/skills/PrecapWeek/weekly-blueprint-meeting-example.md`
5. `.claude/skills/PrecapWeek/references/validation-checklist.md`
6. `.claude/skills/apex-session/SKILL.md`
7. `.claude/skills/apex-session/references/handoff-and-next-session-contract.md`
8. `.claude/skills/apex-sync/SKILL.md`
9. `.claude/skills/apex-sync/references/sync-cluster-contract.md`
10. `.claude/skills/status-merge/references/next-precaphandoff-context-contract.md`
11. `.claude/skills/ProjectStatus/SKILL.md`
12. `.claude/skills/weekly-orchestrator/SKILL.md`
13. `apex-meta/handoff/planning-feed-20260816-w34.md`
14. `apex-meta/handoff/sync-reports/20260816-w34/next.json`
15. `apex-meta/handoff/sync-reports/20260816-w34/blockers.json`
16. `apex-meta/handoff/sync-reports/20260816-w34/score.json`
17. `artifacts/weekly-plans/project-status-overview-20260816.md`
18. `artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md`
19. `DESIGN-DECISIONS.md` in this Module 01 folder.

If live files have moved or changed, follow current repository truth and record the difference.

---

## Findings from the previous audit that must be verified, not blindly assumed

### Finding A — Session duplication

Current `PrecapWeek` language says the preferred detailed project context is both:

- latest confirmed Apex Session `planning_feed`; and
- `next-session.md`.

The Session contract says `planning_feed` already includes:

- Current Step;
- Open Items;
- Risks;
- Decisions Made;
- Next Actions;
- state delta summary;
- entity update record;
- source references;
- review flags.

Hypothesis: loading both by default is duplicate context by construction.

### Finding B — ProjectStatus may be a high-cost redundant projection

The W34 `project-status-overview-20260816.md` expands the portfolio into roughly 62 tasks plus ranking, blockers, metadata, and synthetic `[priority/urgency/date]` ratings.

Its own skill contract says it is:

- a readable projection of confirmed state;
- not a second state authority;
- not required after every mutation.

Hypothesis: it should be fallback/on-demand for PrecapWeek, not a normal input when Session + Sync exist.

### Finding C — Sync reports may be over-read

`next.json`, `blockers.json`, and `score.json` repeat large task objects and graph metadata.

Hypothesis: weekly planning normally needs:

- actionable next candidates;
- consequential blockers/dependencies for plausible weekly work;
- not the full scored task universe.

### Finding D — recent recap evidence may be double-processed

Current PrecapWeek accepts recent FlowRecap packets / skip markers.

StatusMerge's next-PreCap contract says planning should consume:

1. confirmed Session planning feed first;
2. supplied Sync reports second;
3. carry-forward items / unresolved risks where relevant.

Hypothesis: individual recap packets should normally be on-demand evidence, not always-loaded weekly context.

### Finding E — calendar contract may be too detailed for weekly planning

Current calendar reference includes:

- 15-minute internal precision;
- normalized event fields;
- fixed/planned block logic;
- detailed `calendar_block_proposals` with IDs, start/end times, block type, project, capacity shape, source basis, conflict state, and approval status.

Validated Module 01 ownership says:

- PrecapWeek designs the Monday-Friday week architecture;
- PrecapNextDay operationalizes one specific day.

Hypothesis: PrecapWeek only needs planning-relevant fixed windows, deadlines/constraints, capacity effects, and uncertainty at weekly level; exact discretionary block proposals likely belong downstream.

### Finding F — calendar source precedence is ambiguous

Current files accept:

- connected calendar events;
- manually pasted blocks;
- operator-named fixed commitments;
- unavailable windows;
- travel/buffer requirements;
- calendar access status.

But source precedence / resolution is not clearly defined.

Hypothesis: define precedence directly rather than introducing another Calendar Adapter stage.

### Finding G — weekly blueprint mixes useful grammar with stale priority assumptions

The current standard blueprint contains useful invariants:

- fixed life anchors;
- capacity/deformation patterns;
- standard/compressed/minimal/omitted flow logic.

It also contains a default project ordering:

`Leela -> MasterOfArts -> Apex -> Investment -> Residual`

Current PrecapWeek design says the active project set should derive from confirmed current context and weekly intent.

Hypothesis: retain the weekly rhythm/capacity grammar, remove project priority/order authority from the blueprint.

### Finding H — validation checklist duplicates owning contracts

Current validation checklist repeats substantial portions of:

- accepted input definitions;
- calendar behavior;
- fixed blocks;
- capacity shapes;
- output sections;
- failure modes.

Hypothesis: keep the conditional validation file, but reduce it to invariant assertions rather than another full specification.

### Finding I — do not solve bloat with another permanent packet

The weekly orchestrator already dispatches forked skills by passing paths/references rather than copying packet content.

Hypothesis: the correct pattern is selective retrieval into an ephemeral working set, not a new persisted `PrecapWeek-input-packet` schema.

---

## Required explanation format before any Q&A

For each topic, use this sequence.

### 1. Current mechanism

Explain in plain operator language.

Example:

> Today PrecapWeek is told to read `planning_feed` and `next-session.md`. The planning feed already contains the five sections from next-session plus additional confirmed state. So the AI can receive the same Current Step/Open Items/Risks/Decisions/Next Actions twice.

### 2. Actual source snapshot

Show small real excerpts or concise faithful reconstructions from W34.

Example:

```text
planning_feed
- Current Step: Apex Session canonicalization complete...
- Open Items: ProjectStatus, W34 context capture, PreCap Week G1...
- Risks: preserve operator blockers...
- Decisions Made: 62 tasks validated...
- Next Actions: ProjectStatus -> context capture -> PreCap Week

next-session.md
- Current Step: [same continuation state]
- Open Items: [same unresolved work]
- Risks: [same risk family]
- Decisions Made: [same durable decisions]
- Next Actions: [same continuation actions]
```

Do not fabricate excerpts. Read the actual current files.

### 3. What value it adds

Use a compact value table:

| Input | Unique weekly value | Duplicate value | Typical cost / complexity | Authority |
|---|---|---|---|---|
| planning_feed | ... | ... | ... | confirmed |
| next-session | ... | ... | ... | confirmed subset |

Cost does not need exact token counts unless measurable. Relative levels (`low`, `medium`, `high`, `very high`) are acceptable when explained.

### 4. Before vs after snapshot

Show what PrecapWeek would effectively reason over.

Example:

```text
CURRENT DEFAULT
planning_feed
+ next-session
+ ProjectStatus full portfolio
+ Sync next
+ Sync blockers
+ Sync score
+ calendar normalization/proposals
+ recent recap packets

LEAN TARGET
planning_feed
+ weekly intent
+ Sync next candidates
+ only blockers/dependencies for plausible weekly work
+ compact weekly calendar constraints
+ on-demand deeper evidence by reference
```

### 5. Loss test

Answer explicitly:

> If we remove this from default context, what important weekly decision can no longer be made?

If the answer is "none, because the same information exists elsewhere," say so.

If there is a real loss, demonstrate it with one concrete W34 example.

### 6. Recommendation

Only now state the preferred mechanism.

### 7. Formal Q&A

Then use the operator's exact required format below.

---

## Required Q&A format

For every real decision:

- *Topic:* NN_short_slug
- *Detail Level:* Tier X (definitions at end of file)
- *Question:* the exact problem/decision being resolved
- *Options:* letter, mechanism (2-4 lines), REI: R/E/I, Grounding (process/user story/example) — one such line per option, as many options as needed
- *Recommendation:* letter
- *Reasoning:* dense justification for the recommended option
- *Notes:* letter — rejection reason, one line per rejected option

REI = Risk (failure probability × blast radius) / Evidence (empirical backing) / Impact (strategic upside). Scale 1-100.

---

## Decision topics to cover

At minimum cover these topics, but merge or split them if the evidence shows a cleaner decision surface:

1. `single_confirmed_context_source`
2. `projectstatus_default_vs_fallback`
3. `sync_read_minimization`
4. `recent_execution_evidence_scope`
5. `weekly_calendar_input_shape`
6. `calendar_source_resolution`
7. `blueprint_scope_and_priority_authority`
8. `operator_intent_intake_shape`
9. `validation_checklist_deduplication`
10. `ephemeral_working_set_vs_new_packet`

Do not ask all ten at once if that would overload the operator. Group into 2-4 decision rounds.

---

## Required visual artifacts in the answer

The response must contain all of these:

### A. Current pipeline map

One diagram showing producers -> inputs -> PrecapWeek.

### B. Proposed lean pipeline map

One diagram showing normal inputs vs on-demand references.

### C. Input inventory

A compact table with columns:

- input;
- producer;
- normal/fallback/on-demand;
- unique value;
- overlap;
- context cost;
- current issue.

### D. Three concrete W34 snapshots

At least:

1. `planning_feed` vs `next-session` overlap;
2. `ProjectStatus` full projection vs the smaller planning-relevant subset;
3. full Sync blocker/score payload vs the fields actually needed to choose weekly work.

### E. Calendar snapshot

Show one current detailed calendar-normalization/proposal example and one proposed weekly-only representation of the same information.

Example shape only:

```text
CURRENT
proposal_id: CBP-WED-001
start_time: 13:15
end_time: 15:15
block_type: work_flow
related_project: Leela
capacity_shape: compressed_flow_2_sprints
source_basis: calendar_gap
conflict_status: no_known_conflict
operator_approval_required: true

LEAN WEEKLY
Wed — COMPRESSED
Fixed: 10:00-15:00 meetings
Available deep-work capacity: ~1 meaningful project movement
Reason: fixed calendar load
```

Use actual repository semantics; do not pretend this exact proposal exists if it does not.

### F. "What would the AI actually read?" snapshots

For the most important options, show approximate effective prompt/input composition.

Example:

```text
OPTION A — current broad loading
[planning_feed]
[next-session]
[ProjectStatus 62-task overview]
[next_action_report]
[blocker_report]
[score_report]
[calendar guidance + proposals]
[recap packets]

OPTION B — selective retrieval
[planning_feed]
[weekly intent]
[next_action candidates]
[3 relevant blocker/dependency excerpts]
[weekly calendar constraints]
[blueprint grammar]
```

The operator should be able to see the difference without knowing the internal architecture.

---

## Value-vs-cost detective criteria

For every input ask:

```okf
input_value_test:
  authority:
    question: is_this_confirmed_truth_projection_or_raw_evidence

  unique_information:
    question: what_weekly_decision_requires_this_input_that_no_cheaper_source_supports

  duplication:
    question: is_the_same_information_already_present_in_a_higher_authority_or_smaller_source

  timing:
    question: is_this_needed_at_weekly_planning_time_or_only_after_a_candidate_is_selected

  granularity:
    question: is_the_input_more_detailed_than_the_weekly_decision_requires

  context_cost:
    question: how_much_material_must_the_model_parse_to_extract_the_useful_signal

  drift_risk:
    question: can_this_projection_or_duplicate_source_disagree_with_the_authoritative_source

  decision_value:
    question: does_it_change_weekly_allocation_sequencing_capacity_or_operator_review
```

Use these tests explicitly.

---

## Expected likely target architecture — hypothesis only

Do not present this as already approved. Test it against repository evidence.

```text
PrecapWeek dispatch
│
├─ run_date + week_id
├─ operator weekly intent
│
├─ Apex Session planning_feed             PRIMARY CONFIRMED CONTEXT
│   └─ deeper Session files               ON DEMAND
│
├─ Apex Sync next_action candidates       NORMAL
│   ├─ consequential blockers/dependencies ON DEMAND
│   └─ score_report                       NOT DEFAULT
│
├─ ProjectStatus                          FALLBACK / HUMAN-REQUEST ONLY
│
├─ recent FlowRecap / skip evidence       ON DEMAND
│   └─ prefer Session carry-forward first
│
├─ weekly calendar constraints            NORMAL
│   └─ fixed windows + deadlines + capacity effect + uncertainty
│
└─ slim weekly blueprint                  NORMAL REFERENCE
    └─ life anchors + capacity/deformation grammar only
```

Core design principle:

> Do not solve context bloat by creating another permanent summary file. Prefer authority-first references plus selective retrieval into an ephemeral working set.

---

## Operator-intent question

Pay special attention to the operator-intent path.

The previous W34 flow asked separately for multiple items such as:

- weekly intent;
- minimum success;
- capacity/calendar constraints;
- Dating allocation;
- priority overrides.

The operator has already validated an adaptive-hybrid conversation model for Module 01:

- infer what evidence safely supports;
- ask only consequential non-inferable weekly decisions;
- avoid form-like schema filling when natural intent is enough.

Use examples showing both approaches before asking whether that should become the formal intake rule.

---

## Tier definitions

- **Tier 1 — Architecture / high leverage:** determines authority, normal dataflow, major context cost, or planning correctness. Wrong choice causes systemic drift or repeated weekly waste.
- **Tier 2 — Contract / implementation:** supporting contract or information-shape decision. Wrong choice causes recurring inefficiency or ambiguity but is locally repairable.
- **Tier 3 — Optimization:** naming, presentation, micro-schema, or convenience refinement with limited architectural blast radius.

---

## Success condition

The operator should not have to understand terms such as `planning_feed`, `ProjectStatus`, `score_report`, or `calendar_block_proposal` before making the decision.

The response succeeds when the operator can instead reason from concrete statements like:

> "These two files tell the AI almost the same thing, so keep only the richer one by default."

or:

> "I can see that the weekly planner only needs to know Wednesday is compressed; it does not need a full exact work-block object."

Only then should the operator be asked to approve or reject the architectural simplification.
