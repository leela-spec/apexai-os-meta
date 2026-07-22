# Delegation and reconciliation contract

## Purpose

The orchestrator preserves the target and delegates bounded work. It does not perform long research, implementation, or canary execution itself when those activities would overload its context.

Every delegated task must produce an inspectable artifact. A worker's prose claim is never enough to advance the orchestration state.

## Worker types

| Worker | May read | May write | May commit/push | Primary output |
|---|---|---|---|---|
| Research worker | Exact live files and selected decision sources | One report path named by task, or chat report when read-only | No | Evidence ledger, value matrix, minimal recommendation |
| Patch author | Exact live files and approved gap report | Patch pack only | No | Exact-match patches or complete new-file content |
| Execution worker | Exact branch and approved patch pack | Explicit allowlisted files | Approved task branch only | Commit, tests, canary evidence, result envelope |
| Independent verifier | Result branch, commit and evidence | Verification report only | No unless explicitly authorized | Pass/fail against acceptance criteria |
| Browser semantic worker | Exact repository/ref and run-specific prompt | Exact semantic artifact paths named by prompt | Yes, as part of the bounded prompt | Semantic artifacts plus commit/push completion response |

Only one execution worker may be active at a time.

## Required task packet

Every task must contain:

```yaml
task_id: stable-short-id
mode: research | patch_authoring | execution | verification | browser_semantic
repository: leela-spec/apexai-os-meta
branch: exact-branch
expected_start_commit: exact-sha
product_outcome: one sentence
why_this_matters: one paragraph
must_read:
  - exact paths
selected_decisions:
  - exact locked decisions relevant to task
allowed_writes:
  - exact paths or none
forbidden_scope:
  - explicit exclusions
validation:
  - exact checks
stop_conditions:
  - exact blockers
return_contract:
  - exact artifact paths and evidence
```

A task missing repository, branch, expected commit, allowed writes, or stop conditions is invalid.

## Iteration size

A valid implementation iteration must satisfy all of these:

- one primary product outcome;
- at most one adjacent compatibility change;
- explicit file allowlist;
- focused tests plus relevant full suite;
- a canary that exercises the changed user path;
- no speculative extension into another phase.

When a proposed iteration touches more than one phase, the worker must split it before implementation unless the cross-phase edit is the smallest possible end-to-end slice.

## Research worker contract

Research is for resolving a live uncertainty, not restarting architecture.

A research report must contain:

1. exact branch and commit read;
2. exact files read completely or targeted functions read;
3. selected target behavior;
4. current implementation behavior;
5. a difference matrix;
6. value/cost/drift ranking;
7. minimal recommended patch boundary;
8. deferred and rejected ideas;
9. unresolved evidence gaps.

Research workers may search the web only for a narrow technical fact not settled by repository evidence. Web patterns never override operator decisions.

## Patch-author contract

Patch authors must:

- fetch exact current file bytes from the task branch;
- create one change per exact-match block for existing files;
- provide complete content for new files;
- avoid claims that patches were applied;
- include focused test additions;
- include a patch manifest listing every intended changed path;
- stop rather than guess an exact anchor.

## Execution worker contract

Before writes, execution workers perform the startup probe in `02-LIVE-STATE-AND-BRANCH-SAFETY.md`.

Then they must:

1. create the explicitly named iteration branch from the expected base;
2. apply only the approved patch paths;
3. preserve all unrelated changes;
4. stage only explicit paths;
5. show the staged path list and diff summary;
6. run focused tests, relevant full tests, compilation, and canary;
7. commit tersely;
8. push the iteration branch;
9. return exact commit and validation evidence;
10. never merge to `main`.

## Browser semantic worker contract

The generated prompt must contain all execution authority needed for one browser run:

- repository full name;
- exact branch and starting commit;
- exact deterministic artifact paths;
- exact source paths or sections to read;
- locked topic and questions;
- exact output paths;
- allowed and forbidden writes;
- required self-review;
- expected changed-file list;
- commit message;
- push target;
- exact completion response.

The browser worker must not select the next lifecycle stage. Commit and push are part of its one prompt, not separate handoffs.

## Reconciliation procedure

The orchestrator must reconcile every returned result in this order:

1. Confirm the reported branch and commit exist remotely.
2. Read the actual changed-file list.
3. Compare changed paths to the task allowlist.
4. Inspect the material diff, not only test output.
5. Read test and canary artifacts.
6. Check every acceptance criterion.
7. Record unexpected files, scope expansion, or omitted requirements.
8. Update `CURRENT-STATE.yaml` only after evidence passes.
9. Create the next bounded task or stop with a reason-coded blocker.

## Result envelope

Every worker returns:

```yaml
schema: apex.kb.orchestration-result.v1
task_id: "..."
status: completed | partial | blocked | failed
repository: leela-spec/apexai-os-meta
branch: "..."
start_commit: "..."
result_commit: "..." # null for read-only work
files_read:
  - "..."
files_written:
  - "..."
commands_or_actions:
  - "..."
validation:
  - check: "..."
    result: pass | fail | not_run
artifacts:
  - "..."
blockers:
  - code: "..."
    detail: "..."
scope_deviations:
  - "..."
recommended_next_action: "..."
```

The orchestrator may reject a result that omits evidence even when the worker says `completed`.

## Stable blocker codes

- `WRONG_REPOSITORY_SURFACE`
- `WRONG_BRANCH_OR_COMMIT`
- `DIRTY_TREE_CONFLICT`
- `PATCH_ANCHOR_MISMATCH`
- `UNEXPECTED_CHANGED_PATH`
- `TEST_FAILURE`
- `CANARY_NOT_REPRESENTATIVE`
- `TARGET_DECISION_CONFLICT`
- `INSUFFICIENT_REPOSITORY_EVIDENCE`
- `REAL_PLATFORM_LIMITATION`
