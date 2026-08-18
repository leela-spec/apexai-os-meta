# Build Instruction — Top 5 Weekly Command Brief Visualization Prototypes

```okf
instruction:
  id: module01-build-top5-week-visualizations
  status: execution_ready
  purpose: >
    Build five genuinely different, browser-viewable prototypes for the
    Weekly Command Brief week-architecture visualization so the operator can
    choose by direct visual comparison rather than by prose descriptions.

  mode: prototype_only
  production_mutation: forbidden
  branch: main

  source_inputs:
    required:
      - GPT.md
      - CLIGEM.md
      - apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md
      - .claude/skills/PrecapWeek/weekly-command-brief-template.md
      - .claude/skills/PrecapWeek/weekly-blueprint-standard.md
      - .claude/skills/PrecapWeek/weekly-blueprint-meeting-example.md
      - artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md
    source_rule: >
      Use GPT.md and CLIGEM.md as research evidence. Use DESIGN-DECISIONS.md
      and live PrecapWeek files as semantic authority. Do not silently import
      old/superseded schema rules from archived material.

  locked_semantics:
    - PrecapWeek owns Monday-Friday week architecture
    - PrecapNextDay owns exact next-day operationalization and intra-day sequence
    - every active project remains visible
    - deferred work remains visible with compact reason
    - project work is weekly target plus actionable work, not sprint/prompt depth
    - metrics appear only inline as Task (I94/R25/E9)
    - I means impact 1-100
    - R means risk 1-100
    - E means evidence strength 1-100
    - no synthetic combined score
    - no separate metric columns
    - show deadlines, meetings, dependencies, capacity and deliberate deferrals only when consequential
    - Markdown Weekly Command Brief remains canonical; prototypes are visual experiments only

  patch_policy:
    existing_files: do_not_modify
    new_files: allowed
    production_files: forbidden
    rule: >
      Create new prototype artifacts only. Do not update SKILL.md, templates,
      handovers, decisions, runtime contracts, or any other existing file in
      this run. Existing-file edits require a separate surgical patch phase.
```

## 1. Build exactly these five candidates

```okf
candidates:
  01_project_week_matrix:
    research_origin: GPT primary recommendation
    structure: projects_as_rows_days_as_columns
    goal: >
      Answer both "what happens Tuesday?" by column scanning and
      "what happens to Leela this week?" by row scanning in one surface.

  02_two_tier_ribbon_plus_matrix:
    research_origin: CLIGEM primary recommendation
    structure:
      - compact_day_capacity_ribbon
      - project_by_day_trajectory_matrix
    goal: >
      Separate day-level capacity/constraint awareness from project trajectory
      while keeping them visually adjacent.

  03_week_strip_plus_project_arcs:
    research_origin: GPT Candidate C / strong fallback
    structure:
      - five_day_capacity_strip
      - one_horizontal_project_trajectory_per_project
    goal: >
      Maximize project continuity and dependency readability while preserving
      a compact week rhythm strip.

  04_day_agenda_cards:
    research_origin: GPT Candidate B / CLIGEM vertical-day-card family
    structure: five_day_cards_or_rows
    goal: >
      Optimize day-by-day comprehension and narrow-screen resilience without
      turning the view into an hourly scheduler.

  05_strategic_swimlane_critical_path:
    research_origin: CLIGEM Candidate 5 family
    structure:
      - weekday_axis
      - project_swimlanes_or_dependency_paths
      - explicit_deadline_and_dependency_cues
    goal: >
      Optimize sequencing, dependencies and strategic critical-path visibility
      without claiming exact intra-day timing.

  explicitly_excluded:
    - flow_slot_time_grid
    - hourly_calendar
    reason: >
      These visually imply exact intra-day slots/order and therefore trespass
      on PrecapNextDay ownership.
```

## 2. Use one identical comparison dataset

Do not make one candidate look better by giving it cleaner data.

Use one shared W34-derived fixture across all five prototypes.

```okf
fixture:
  week: 2026-W34
  projects:
    - Leela
    - MasterOfArts
    - Apex
    - Investment
    - Residual

  day_roles:
    Monday: start
    Tuesday: build
    Wednesday: build
    Thursday: review
    Friday: buffer

  capacity:
    Monday: standard
    Tuesday: standard
    Wednesday: standard
    Thursday: standard
    Friday: standard

  weekly_context:
    - Leela, MasterOfArts, Apex and Investment are equal primary categories
    - MasterOfArts website is a named weekly focus
    - Residual is recovery/overflow support
    - calendar was unavailable in the historical W34 packet

  task_data_policy: >
    Prefer task names and dependency chains supported by repository/project
    material used in the research reports. Clearly mark research-fixture I/R/E
    values as prototype values when they were not historical facts.
```

Use the same concise task strings in all prototypes wherever structurally possible.

Example syntax:

```text
Verify Home runtime (I90/R20/E95)
Locate website source (I92/R15/E85)
Re-baseline ApexKB (I88/R20/E90)
Collect branch input (I82/R15/E60)
```

## 3. Prototype format

Build actual visual artifacts, not Markdown descriptions of what they could look like.

```okf
artifact_format:
  primary: standalone_HTML
  dependencies: none
  network_calls: forbidden
  frameworks: forbidden
  build_step: none
  fonts: system_only
  javascript: optional_but_minimal
  css: embedded
  responsive: required
  source_of_truth: embedded_shared_fixture

  visual_style:
    - minimalist
    - high_information_density
    - restrained
    - no_decorative_dashboard_chrome
    - no_gradients
    - no_excessive_color
    - no_icon_flood
    - readable_without_color
    - clear_hierarchy
    - compact_spacing
```

Do not use a design framework, React, Vue, FullCalendar, Mermaid, external fonts, CDN assets, npm packages, or an external planning service. The point is to evaluate information architecture, not library styling.

## 4. Required files

Create only new files under:

```text
apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/prototypes/
```

Required outputs:

```text
00-index.html
01-project-week-matrix.html
02-two-tier-ribbon-matrix.html
03-week-strip-project-arcs.html
04-day-agenda-cards.html
05-strategic-swimlane-critical-path.html
prototype-data.js
README.md
```

### `00-index.html`

Create a visual comparison launcher with:

- five large links/cards, one per prototype;
- candidate name;
- one-sentence structural description;
- no recommendation/ranking shown initially, so operator judgment is not primed;
- links opening each candidate in the same browser tab or a new tab;
- a compact link to a comparison section at the bottom.

At the bottom, after the five links, show a neutral comparison checklist only:

- understand whole week in 10 seconds;
- understand one day quickly;
- understand one project's trajectory quickly;
- see meetings/capacity effects;
- see dependencies/deadlines;
- see deliberate deferrals;
- feels minimal rather than dashboard-heavy;
- would want to use every Sunday.

Do not display the research scores until after the visual options.

### `prototype-data.js`

Store the shared fixture once so the five views do not drift semantically.

All five HTML files must consume the same dataset or a mechanically identical embedded representation.

## 5. Visual constraints common to all candidates

```okf
common_visual_rules:
  metrics:
    syntax: "(I#/R#/E#)"
    same_line_as_task: true
    separate_columns: forbidden
    labels_repeated_per_task: forbidden

  temporal_scope:
    days: [Monday, Tuesday, Wednesday, Thursday, Friday]
    exact_discretionary_work_times: forbidden
    fixed_meeting_or_deadline_times: allowed_when_material

  capacity_vocabulary:
    - STANDARD
    - COMPRESSED
    - MINIMAL
    - OVERLOADED

  exceptions:
    dependency: use_small_local_cue
    deadline: use_small_local_cue
    deliberate_deferral: visible_with_short_reason
    calendar_uncertainty: visible_once_when_global

  forbidden:
    - sprint_counts_as_primary_visual_structure
    - prompt_content
    - Flow_Execution_Card_detail
    - exact_project_execution_order_inside_a_day
    - synthetic_priority_score
    - hidden_projects
    - blank_cells_for_material_deliberate_deferral
    - large_legends_that_require_learning_a_symbol_language
```

## 6. Candidate-specific build requirements

### 01 — Project × Week Matrix

- Projects = rows.
- Monday-Friday = columns.
- Day header contains role + capacity.
- Each cell contains one concise leading movement or a visible deferral.
- Local dependency/deadline notes may sit on a second compact line.
- Do not add a second duplicate lens.

### 02 — Two-Tier Ribbon + Matrix

Tier 1 must be extremely compact. It may include only:

- day role;
- capacity;
- material fixed meetings/deadlines;
- active-flow/project count or compact roster if useful.

Tier 2 is project × weekday trajectory.

Do not duplicate every task in both tiers.

### 03 — Week Strip + Project Arcs

- Top strip = five days with role/capacity/constraint.
- Below = one project line each.
- Project line visually traverses Mon→Fri.
- Dependencies should read naturally left-to-right.
- Must remain understandable when a project is deferred midweek.

### 04 — Day Agenda Cards

- Five equal-weight day cards on desktop when width allows.
- Collapse to vertical cards on narrow screens.
- Each card shows day role, capacity, material constraint, then project movements.
- Include enough project labeling that the operator can still trace a project across the week.
- Do not introduce hourly slots.

### 05 — Strategic Swimlane / Critical Path

- Horizontal time axis = Monday-Friday only.
- One swimlane per project.
- Show dependency progression and hard deadline cues clearly.
- Use compact blocks/segments, not duration-precise Gantt bars.
- A block means "intended on this day", not "runs for this exact duration".
- Avoid arrows crossing the entire visualization if they create clutter; local dependency IDs or connectors are acceptable.

## 7. Stress state in every prototype

Each prototype must include a simple UI control labeled `Normal W34` / `Stress Week`.

Stress Week uses the same projects and overall task semantics but applies:

```okf
stress_week:
  Tuesday:
    capacity: compressed
    fixed_constraint: meetings 14:00-17:00
  Wednesday:
    capacity: minimal
    fixed_constraint: meetings 10:00-16:00
  Thursday:
    capacity: compressed
    fixed_constraint: website checkpoint 13:00
  Friday:
    deadline: MasterOfArts website readiness due 12:00

  consequences:
    - at least one high-impact Leela item deliberately deferred
    - Investment reduced/deferred where capacity loses
    - MasterOfArts sequential deadline path remains visible
```

The normal/stress toggle is for prototype comparison only. It does not define production runtime behavior.

## 8. Responsive requirement

Test each view at approximately:

- 1440 px desktop;
- 1024 px laptop/tablet landscape;
- 430 px narrow/mobile.

The mobile view may transform structurally if needed, but must preserve semantics.

Examples:

- matrix may become horizontally scrollable with sticky first column;
- day cards may stack vertically;
- project arcs may become compact project sections.

Do not solve narrow width by shrinking text until unreadable.

## 9. README requirements

`README.md` must contain only:

1. how to open `00-index.html`;
2. list of five candidates;
3. statement that all use the same fixture;
4. statement that no production files were modified;
5. operator scoring form:

```text
1. Project × Week Matrix: __/10
2. Two-Tier Ribbon + Matrix: __/10
3. Week Strip + Project Arcs: __/10
4. Day Agenda Cards: __/10
5. Strategic Swimlane / Critical Path: __/10

Winner:
What I like:
What I dislike:
Elements worth combining:
```

Do not insert a long research report into the README.

## 10. Validation before completion

```okf
validation:
  semantic:
    - all five consume same fixture
    - Monday-Friday visible in all
    - every active project visible in all
    - inline metric notation exact
    - no combined score
    - no intra-day discretionary timing
    - deliberate deferrals visible
    - dependencies/deadlines visible where material

  visual:
    - no broken overflow at 1440px
    - usable at 1024px
    - usable or intentionally transformed at 430px
    - no cell becomes paragraph-like in normal state
    - no candidate depends on color alone

  scope:
    - only new files under research/prototypes created
    - no existing file changed
    - no production integration performed
```

## 11. Completion output to operator

After building, return only:

```okf
completion:
  created:
    - paths_to_8_new_files
  open_first: path_to_00-index.html
  validation:
    semantic: PASS_or_FAIL
    desktop: PASS_or_FAIL
    narrow: PASS_or_FAIL
  production_files_modified: false
  next_operator_action: visually_compare_and_select_or_hybridize
```

Do not choose the winner on behalf of the operator in this run.
Do not patch production files after the prototypes are built.
Do not ask for another approval before building; this instruction is the execution authorization for prototype creation only.
