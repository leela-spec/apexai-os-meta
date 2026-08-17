# Fresh Runtime Test Protocol

## Purpose

Verify that the real production Weekly Orchestration implementation works from encoded repository instructions rather than design-chat context.

## Preconditions

A module may enter fresh testing only when:

1. its detailed design has been integrated into active production files;
2. the module chat has returned implementation evidence;
3. the Master has inspected actual changes and issued integration PASS;
4. no unresolved interface contradiction blocks execution.

## Fresh-context rule

The test context must not receive the module design discussion, desired example wording or repair rationale.

It receives only what a normal runtime invocation would legitimately have:

- the actual production skill/agent environment;
- the normal invocation/trigger;
- the frozen W34/example inputs or paths;
- normal run date/week parameters when required.

If the output is wrong, fix the production implementation. Do not enrich the test prompt with hidden design instructions.

## Initial regression fixture

Use the existing W34 artifacts/source context already created during the previous weekly run. Module 00 must identify the exact input set appropriate for each stage and record it in that module's handover/test note.

## Evaluation dimensions

### Runtime
- correct skill/agent is selected;
- correct inputs are loaded;
- no design-chat-only knowledge is required;
- expected output is materialized at the real production path;
- downstream interface remains valid.

### Operator
- primary result is understandable quickly;
- next action is obvious;
- review questions are decision-relevant;
- machine plumbing does not dominate the surface;
- flow/prompt outputs are actually executable where applicable.

### Integrity
- plan is not reported as execution;
- candidate is not reported as confirmed truth;
- blockers/dependencies are preserved when real;
- consequential mutation remains appropriately controlled;
- no duplicate truth source is introduced.

## Result

Record only:

- PASS / FAIL;
- generated output paths;
- observed failure(s) if any;
- operator verdict;
- next action.

Do not create a large validation dossier unless a concrete failure requires deeper diagnosis.
