# TEMPLATES

## Purpose

Reusable compact templates for `special_ops__informatics_design`.

Use these templates to preserve file typing, retrieval clarity, terminology stability, appendices-first evidence architecture, and candidate traceability.

## Template selection rule

- **Rule:** Choose the template by function, not by filename, folder, author, or tool.
- **Rule:** Keep detailed source rows, variant comparisons, and evidence tables in appendices.
- **Rule:** Use decision and status templates before moving candidate material across scaffold and appendix boundaries.
- **Constraint:** Do not use templates to bypass validation, promotion, or governance boundaries.

## File function template

```md
# <TITLE>

## Purpose

- **Purpose:** <one sentence stating what this file exists to do>
- **Scope:** <bounded scope>
- **Boundary:** <what this file does not do>

## Main content

- **Rule:** <if the file is rule-bearing>
- **Decision:** <if a decision is accepted within this file scope>
- **Evidence:** <if the file records support>
- **Open Question:** <if unresolved>

## Pointers

- `<appendix-or-source-path>`
```

## Source manifest row template

```md
| source_role | source_path | read_mode | used_for | status |
|---|---|---:|---|---|
| <primary/supporting/evidence/constraint> | `<repo-relative-path>` | <full/skim/targeted/ranked extract> | <use in KB base> | <used/represented/excluded> |
```

## Information ranking row template

```md
| info_id | source_path | source_role | source_section_or_candidate_id | information_unit | agent_relevance | actionability | evidence_strength | reuse_frequency_likelihood | drift_risk | recommended_target_file | appendix_pointer | scaffold_summary_needed | status |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| ID-000 | `<path>` | <primary/supporting/evidence> | <candidate or section> | <unit> | <low/medium/high> | <low/medium/high> | <low/medium/high> | <low/medium/high> | <low/medium/high> | `<file>` | `<appendix>` | <yes/no> | <status> |
```

## Candidate row template

```md
| candidate_id | source_candidate | candidate_summary | target_file | status | validation_pair | notes |
|---|---|---|---|---|---|---|
| CAND-INF-000 | <source id> | <candidate summary> | `<target>` | <candidate/strong_candidate/provisional-boundary/integrated_into_scaffold/deferred/rejected/resolved> | <validator pair> | <notes> |
```

## Candidate decision table template

```md
| candidate_id/source | candidate_summary | evidence_strength | possible_targets | recommendation | reason | operator_decision |
|---|---|---|---|---|---|---|
| <candidate/source> | <summary> | <low/medium/high> | `<file A>`; `<file B>` | <integrate_into_scaffold/integrate_into_appendix/split_between_scaffold_and_appendix/keep_as_candidate/reject_obsolete/needs_operator_decision> | <reason> | <approved/rejected/revise/defer> |
```

- **Rule:** Produce this table before applying scaffold or appendix changes that change candidate status.
- **Rule:** Preserve candidate IDs and source references in later status updates.

## Anti-drift row template

```md
| failure_id | pattern | evidence_basis | drift_effect | countermeasure | scaffold_target |
|---|---|---|---|---|---|
| DRIFT-INF-000 | <failure pattern> | <source/evidence> | <what breaks> | <control> | `<target>` |
```

## Terminology mini-table template

```md
| term | stable meaning | use when | avoid |
|---|---|---|---|
| `<term>` | <definition> | <preferred usage> | <misuse/synonym drift> |
```

## Audit mini-check template

```md
| check | inspect | pass condition | fail condition | severity |
|---|---|---|---|---|
| <check name> | <surface/chunk> | <what good looks like> | <what fails> | <critical/major/minor> |
```

## Compact typed-bullet pattern

Use signal words consistently:

- **Rule:** required behavior inside this file scope.
- **Decision:** accepted bounded resolution.
- **Constraint:** forbidden or limited behavior.
- **Evidence:** source-backed support.
- **Open Question:** unresolved issue.
- **Risk:** drift or failure condition.
- **Action:** next executable step.
- **Pointer:** target file or appendix.
- **Status:** current lifecycle state.

## Appendix architecture template

```text
scaffold file = compact activation / navigation / operating guidance
appendix file = deep evidence / ledgers / variants / tables / source comparisons / research planning
```

- **Rule:** When a scaffold section starts needing more than compact rules, move the detail into an appendix.
- **Rule:** Replace moved detail with a short rule and appendix pointer.
- **Rule:** When a TODO becomes active work, create or update an appendix status section rather than leaving stale future-work prose.

## Status

- **Status:** KB-base templates are accepted for this agent scaffold.
- **Owner:** `special_ops__informatics_design`
- **Validator:** `special_ops__hygiene_clean`
