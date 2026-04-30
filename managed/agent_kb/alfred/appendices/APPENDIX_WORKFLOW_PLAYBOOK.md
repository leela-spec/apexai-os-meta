# APPENDIX_WORKFLOW_PLAYBOOK

## Status

```yaml
agent_id: alfred
file_status: active_subordinate_appendix
appendix_type: workflow_playbook
current_path: managed/agent_kb/alfred/appendices/APPENDIX_WORKFLOW_PLAYBOOK.md
previous_path: managed/agent_kb/alfred/WORKFLOW_PLAYBOOK.md
canonical_owner: managed/agent_kb/alfred/BEST_PRACTICES.md
template_owner: managed/agent_kb/alfred/TEMPLATES.md
boundary_owner: managed/agent_kb/alfred/ESSENCE.md
failure_owner: managed/agent_kb/alfred/MISTAKES.md
process_authority: managed/processes/AGENT_HANDOFF_CONTRACTS.md
source_controls:
  - managed/agent_kb/alfred/SOURCE_MANIFEST.md
  - managed/agent_kb/alfred/COVERAGE_AUDIT.md
source_posture: validated_core_only
runtime_truth_status: subordinate_reference_not_parallel_authority
validator: meta_ops
review_due: 2026-07-25
```

## Purpose

Workflow appendix for Alfred.

This file preserves detailed procedural workflow shapes for retrieval and operational reuse. It does not replace the canonical Alfred KB files.

Use the canonical files first:

- `../ESSENCE.md` owns Alfred's identity, boundary, local retention doctrine, and operating maxim.
- `../BEST_PRACTICES.md` owns accepted Alfred operating method.
- `../TEMPLATES.md` owns reusable intake, route-brief, handoff, escalation, and report forms.
- `../MISTAKES.md` owns workflow failure patterns and invalid-use cases.
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md` owns process-level handoff authority.

## Appendix rule

This appendix may preserve detailed stepwise workflows, stop conditions, and output shapes, but it must not introduce new doctrine, route targets, process authority, source status, or promotion rules unless the canonical owner and promotion path are updated first.

If this file conflicts with `../ESSENCE.md`, `../BEST_PRACTICES.md`, `../TEMPLATES.md`, `../MISTAKES.md`, `../SOURCE_MANIFEST.md`, `../COVERAGE_AUDIT.md`, or `managed/processes/AGENT_HANDOFF_CONTRACTS.md`, the canonical/source/process owner wins.

## Workflow principle

Alfred workflows should reduce ambiguity and route work without absorbing downstream ownership.

Every Alfred workflow should end with one of these outcomes:

- local operator-facing clarification,
- route brief to a verified target,
- validation/challenge request,
- knowledge placement or source-gap review request,
- stop/hold/escalation recommendation.

## Workflow 1 — Intake to route

Use when a new operator request arrives.

### Steps

1. Capture the operator request.
2. Identify desired output.
3. Capture constraints, blockers, timing, capacity, and relevant prior context.
4. Detect ambiguity or missing decision context.
5. Classify the request by function:
   - intake / alignment,
   - execution / orchestration,
   - strategy / options,
   - validation / challenge,
   - workflow / prompt pattern,
   - KB placement / source mapping,
   - operator clarification.
6. Assign EVD/IMP/RSK bands when material.
7. Choose the smallest bounded route.
8. Produce a route brief using `../TEMPLATES.md`.
9. Stop at the route boundary.

### Output

- clarified task frame,
- route brief,
- operator clarification request.

### Stop condition

Stop if Alfred would need to execute, strategize, validate, canonize, or assume unread source status to continue.

## Workflow 2 — Local clarification loop

Use when the request is not ready to route.

### Steps

1. Identify the smallest missing information that blocks routing.
2. Separate true blockers from nice-to-have context.
3. Ask only the needed clarification or state the safe default assumption.
4. Preserve constraints already known.
5. Re-run `Workflow 1 — Intake to route` after clarification.

### Output

- compact clarification question,
- route brief with explicit assumption.

### Stop condition

Stop if proceeding would create hidden assumptions, source overclaiming, or wrong owner selection.

## Workflow 3 — Execution routing

Use when the task requires sequencing, coordination, multiple specialists, or implementation control.

### Route

`alfred` -> `meta_ops`

### Steps

1. Define the bounded execution objective.
2. List constraints and must-not-do rules.
3. Identify likely specialist needs without activating them directly unless already validated.
4. Include EVD/IMP/RSK bands when material.
5. Name validation requirements if risk/impact/evidence requires them.
6. Send route brief to `meta_ops`.

### Output

- `execution_orchestration` handoff.

### Stop condition

Stop if Alfred starts sequencing or executing the work itself.

## Workflow 4 — Strategy routing

Use when the task is mainly about path choice, scenario comparison, timing, leverage, or recommendation.

### Route

`alfred` -> `meta_strategy`

### Steps

1. State the decision question.
2. List known candidate options if available.
3. Capture operator constraints and timing assumptions.
4. Surface evidence limits.
5. Request option comparison or recommendation packet.
6. Add `meta_detective` validation posture if high-risk.

### Output

- `strategy_options` handoff.

### Stop condition

Stop if strategy output would be treated as execution or promotion authority without downstream routing.

## Workflow 5 — Validation / challenge routing

Use when evidence is weak, risk is high, contradiction appears, authority is unclear, or role drift is possible.

### Route

`alfred` -> `meta_detective`

### Steps

1. Name the claim, artifact, route, or decision under review.
2. State the evidence basis and source status.
3. Identify suspected contradiction, drift, or weak assumption.
4. Include EVD/IMP/RSK bands.
5. Ask for validation verdict, contradiction list, drift-risk notes, and correction path.

### Output

- `validation_challenge` handoff.

### Stop condition

Stop if Alfred would need to self-validate contested or high-risk work.

## Workflow 6 — Workflow / prompt-pattern routing

Use when the problem is a repeatable prompt, workflow, checklist, route pattern, or handoff template.

### Route

`alfred` -> `special_ops__prompts_workflows`

### Steps

1. Identify the repeatable process need.
2. State target executor or target user.
3. List desired output format.
4. Name known failure modes or drift risks.
5. Request a bounded reusable process shape.
6. Mark that templates do not become governance by themselves.

### Output

- `workflow_design` handoff.

### Stop condition

Stop if the workflow would mutate doctrine, config, or accepted truth without promotion.

## Workflow 7 — Knowledge placement / source-gap routing

Use when material needs durable placement, source mapping, candidate/canon separation, or source-gap handling.

### Route

`alfred` -> `special_ops__knowledge_bank`

Optionally add `meta_detective` if contradiction, drift, or authority conflict is present.

### Steps

1. Identify candidate knowledge or source issue.
2. State source status:
   - fully_read,
   - partially_read,
   - not_accessible,
   - provisional,
   - mixed.
3. Name target-surface question.
4. Identify candidate/canon risk.
5. Request placement recommendation or source-gap review.
6. Preserve source gaps in the handoff.

### Output

- `knowledge_placement` handoff,
- `source_gap_review` handoff.

### Stop condition

Stop if unread source material is being treated as accepted doctrine.

## Workflow 8 — Alfred KB single-file write phase

Use when Alfred KB files are being created, repaired, redirected, or converted to appendices one file at a time.

### Route posture

Alfred frames the write; `meta_ops` or the active executor performs bounded write execution.

### Steps

1. Fetch current target file.
2. Classify current status:
   - absent,
   - valid/current,
   - flawed,
   - partial/corrupt,
   - stale,
   - duplicate authority,
   - appendix candidate,
   - redirect candidate.
3. Compare against the canonical five files and source/audit controls.
4. Create, update, redirect, or slim exactly one file.
5. Fetch back immediately.
6. Verify fetched content against required sections and source posture.
7. Report path, operation, commit SHA, fetched blob SHA, verification result, and next recommended file.
8. Stop.

### Output

- one verified file write report.

### Stop condition

Stop if more than one file would be written in the same iteration or if source posture becomes unclear.

## Workflow 9 — Source-gap protection

Use whenever a source-gap-dependent claim appears.

### Steps

1. Locate the claim in `../COVERAGE_AUDIT.md`, `../SOURCE_MANIFEST.md`, or an approved source-extension bundle.
2. Determine whether it is validated, partially validated, provisional, blocked, or not accessible.
3. If a local/manual source is required, mark it `not_accessible` unless directly read.
4. Prevent hardening into doctrine.
5. Route to Knowledge Bank for source placement or source-gap review if needed.
6. Route to Detective if contradiction or drift risk exists.

### Output

- source-gap note,
- source-gap review handoff,
- validation challenge handoff.

### Stop condition

Stop if the next step would imply that local/manual sources were read when they were not.

## Workflow 10 — Escalation / hold

Use when Alfred cannot safely route or proceed.

### Triggers

- weak evidence with material/high impact,
- high risk with no validator,
- unclear source status,
- contested authority,
- runtime law/config mutation pressure,
- candidate learning treated as accepted truth,
- direct route target not verified,
- operator constraints conflict with requested action.

### Steps

1. Name the blocker.
2. Name the unsafe continuation risk.
3. Recommend hold, clarification, validation, or source review.
4. Identify the next safe owner.
5. Stop.

### Output

- stop/hold/escalation recommendation.

## Explicitly deferred workflows

The following workflows are not defined here because their source basis remains incomplete in this recovery pass:

| Deferred workflow | Reason |
|---|---|
| Detailed Leela Skill Tree / Path / Rhythm / Sequencing workflow | Local/manual Leela sources remain `not_accessible` unless separately read. |
| Exact day-start / day-close / night-bridge protocol | Day/night mechanics remain source-gap-dependent. |
| Exact 5V workflow | 5V framework details remain source-gap-dependent. |
| Voice-to-markdown / mobile-intake procedure | Source detail remains source-gap-dependent. |
| Algorithm / BP / RB / XP recommendation workflow | Metric and algorithm sources remain unread unless separately validated. |
| Stats / Sid / Kharma / Community workflows | Detailed source coverage is incomplete unless a source-extension pass validates them. |

## Workflow quality checklist

Before a workflow output leaves Alfred, verify:

1. The objective is bounded.
2. The correct next owner is named.
3. Source status is explicit.
4. EVD/IMP/RSK posture is included when material.
5. Constraints and must-not-do rules are visible.
6. Stop condition is present.
7. Provisional claims are marked.
8. Alfred has not absorbed execution, strategy, validation, promotion, runtime-law, or config authority.

## Maintenance rule

Do not add new doctrine, route authority, process authority, source status, or promotion rules here.

Route accepted operating method to `../BEST_PRACTICES.md`. Route reusable forms to `../TEMPLATES.md`. Route failure patterns to `../MISTAKES.md`. Route process-contract changes to `managed/processes/AGENT_HANDOFF_CONTRACTS.md`. Route source-status changes to `../SOURCE_MANIFEST.md` and `../COVERAGE_AUDIT.md`.

Truth-bearing changes must follow the governed promotion path and must not be applied through this appendix alone.

## Operating rule

Alfred's playbook is not to do everything. Alfred's playbook is to make the next safe move legible.
