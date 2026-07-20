# Apex KB Phase 0 Live-Test Failure Learning Extension

```yaml
document_id: apex-kb-phase0-live-test-failure-learning-extension
extends: PHASE-0-LIVE-TEST-CONTINUATION-HANDOVER.md
repository: leela-spec/apexai-os-meta
branch: main
created_date: 2026-07-19
status: corrective_learning_and_execution_gate
current_runtime_state: start_routing_not_installed_on_main
```

## 1. Why this extension exists

The Phase 0 canary did not fail because Codex misunderstood the request. It failed because the live repository still contained the old Apex KB activation path.

The exact observed response was:

> Can the executor run repository Python commands in a live worktree and capture the command, exit status, stdout, and stderr?

That sentence is still present in the live `.claude/skills/apex-kb/SKILL.md`, where it is explicitly required before procedure or file navigation. The same live file still routes terminal-backed work to `apex_kb.py control` instead of the intended operator-facing Start workflow.

The canary therefore exercised the old checked-in behavior correctly. It did not exercise the intended new process.

## 2. Direct acknowledgement of the failure

The operator was repeatedly told that the Start-routing repair had landed or that the live test could proceed. That was not proven true.

The actual repository state was:

- some Start runtime components existed;
- some patch-pack and handover files existed;
- the live skill entrypoint was still old;
- root Codex dispatch was still not wired to Start;
- documentation and tests were still contradictory;
- the public Start wrapper still did not expose all documented flags;
- the continuation handover committed to `main` was truncated.

This is not a small wording mistake. It is a failure to distinguish between **designed**, **patched**, **committed**, **merged**, **installed**, and **behaviorally proven**.

## 3. Is this a fundamental Apex KB architecture problem?

### Verdict

The primary failure is **not** that the core Apex KB architecture is incomprehensible or fundamentally wrong.

The primary failure is the **change-delivery and verification architecture around it**.

The system currently allows several states to be confused:

| State | Meaning |
|---|---|
| `designed` | A document describes the desired behavior. |
| `patch_authored` | A patch pack proposes edits. |
| `committed_elsewhere` | Files exist in a workpack or another branch. |
| `merged_to_main` | The live target branch contains the change. |
| `installed` | Every runtime, skill, manifest, contract, and test surface agrees. |
| `behaviorally_proven` | A fresh user invocation produces the intended behavior. |

Only the final two states justify telling the operator that a workflow is ready.

### Architectural weakness that must be corrected

Apex KB currently has multiple representations of one feature:

- research guidance;
- mechanistic workpack;
- exact-match patch files;
- live skill instructions;
- Python runtime;
- package manifest;
- command contract;
- examples and runbooks;
- tests;
- handovers.

That can be valid, but there is no enforced closure mechanism proving that all required representations changed together. This creates instruction drift.

The corrective principle is:

> One operator-facing behavior is not complete until its live entrypoint, runtime, contracts, package inventory, tests, and fresh canary all agree.

## 4. The specific failure pattern

### 4.1 Overengineering replaced the target

The target was simple:

> A new Apex KB invocation must begin with the new Start process, not the old executor-capability question.

Instead of closing that one behavior end to end, work expanded across architecture maps, patch packs, downstream handovers, test protocols, branch analysis, and documentation. Those artifacts were often useful, but they became a substitute for proving the target behavior.

### 4.2 Artifacts were mistaken for implementation

The presence of these items was incorrectly treated as evidence of completion:

- `apex_kb_start.py`;
- `start-input.schema.json`;
- a Start subcommand;
- patch-pack files;
- Start Q&A guidance;
- handover documents.

None of them overrides the live `SKILL.md` activation rule. The first user-visible sentence remained old, so the feature was not installed.

### 4.3 Verification stopped one layer too early

The verification chain repeatedly checked whether files or commits existed, but did not always check the final user-facing behavior.

The missing final assertion was:

```text
Given a fresh Codex conversation at current main,
when the operator invokes $apex-kb for a new KB,
then the first response is the Start intake surface,
and the old capability question is absent.
```

### 4.4 Handover creation was reported without rereading the stored file

`PHASE-0-LIVE-TEST-CONTINUATION-HANDOVER.md` was committed in a truncated state and ended at:

```text
Reconcile the actual landed files
```

This proves that successful write confirmation is not sufficient. Every created or replaced handover must be fetched and reread from the repository before it is reported complete.

### 4.5 Work was allowed to continue after the primary acceptance check failed

Once a fresh canary returned the old first question, the correct status was immediately:

```yaml
status: target_not_implemented
next_action: repair_live_entrypoint
```

No additional live-test orchestration should have been presented as though the Start workflow were active.

## 5. Binding learning rules

These rules apply to all continuation work on Phase 0 and should be reused for later Apex modules.

### Rule 1 — Define one observable target before editing

For this repair, the target is exactly:

```text
A fresh new-KB invocation enters the Start workflow without asking the generic executor-capability question.
```

Do not widen scope until that behavior passes.

### Rule 2 — Use a vertical-slice completion checklist

A change to the Start experience is complete only when all applicable surfaces pass:

1. root dispatch;
2. live `SKILL.md` routing;
3. Start workflow reference;
4. Start configuration template;
5. package manifest;
6. public CLI wrapper;
7. command contract;
8. runbook and examples;
9. regression tests;
10. fresh canary.

A missing item means the feature is incomplete.

### Rule 3 — Never use “landed” without evidence

Use these exact status terms:

- `AUTHORED_NOT_APPLIED`
- `APPLIED_NOT_TESTED`
- `TESTED_COMPONENT_ONLY`
- `MERGED_NOT_CANARY_PROVEN`
- `CANARY_PROVEN`

Do not say “landed,” “installed,” “ready,” or “fixed” without naming the exact commit and proof level.

### Rule 4 — Runtime truth outranks workpacks and handovers

For operator behavior, the authority order is:

1. fresh behavioral canary;
2. executed tests and command output;
3. live runtime and live skill on target branch;
4. live contracts and package manifest;
5. patch packs and workpacks;
6. handovers and chat summaries.

A lower layer must never be used to claim a higher layer is complete.

### Rule 5 — Read back every repository write

After creating or updating a file through the connector:

1. fetch the stored file;
2. verify it has a valid ending;
3. verify required sections are present;
4. verify no truncation occurred;
5. only then report success.

### Rule 6 — Test the simplest user path first

Before broad suites or downstream analysis, run the smallest decisive check:

```text
fresh invocation -> correct first response
```

If that fails, stop and repair the entrypoint. Do not proceed into deeper lifecycle testing.

### Rule 7 — Do not create compensating orchestration around a broken entrypoint

A handover, test protocol, or operator instruction must not teach the user how to bypass a broken product path when the stated target is to repair that product path.

### Rule 8 — Keep the repair minimal

Do not redesign Phase 0. Preserve the current control plane and Start adapter where sound. Correct only the surfaces required to make the intended Start behavior real and consistent.

## 6. Correct current diagnosis

```yaml
current_diagnosis:
  core_control_plane: reusable
  start_adapter: partially_present
  start_schema: present
  live_skill_start_routing: absent
  root_codex_dispatch: absent
  package_inventory_alignment: absent
  command_contract_alignment: absent
  wrapper_flag_alignment: incomplete
  regression_proof: incomplete
  fresh_canary: failed_old_behavior
  overall_status: MERGED_NOT_CANARY_PROVEN
```

The overall status may be even earlier than `MERGED_NOT_CANARY_PROVEN` for individual repair files. The next executor must classify each required change separately.

## 7. Narrow recovery plan

The next chat must not restart architecture research. It must close the existing Start-routing vertical slice.

### Step A — Establish exact target-branch truth

Read from current `main`:

- `AGENTS.md`;
- `.claude/skills/apex-kb/SKILL.md`;
- `.claude/skills/apex-kb/package-manifest.md`;
- `.claude/skills/apex-kb/references/start-workflow.md`;
- `.claude/skills/apex-kb/templates/start-config-template.yaml`;
- `.claude/skills/apex-kb/references/start-input.schema.json`;
- `.claude/skills/apex-kb/references/script-command-contract.md`;
- `.claude/skills/apex-kb/examples/lifecycle-runbook.md`;
- `.claude/skills/apex-kb/examples/powershell-commands.md`;
- `.claude/skills/apex-kb/references/acceptance-tests.md`;
- `apex-meta/scripts/apex_kb.py`;
- `apex-meta/scripts/apex_kb_start.py`;
- `apex-meta/scripts/tests/test_apex_kb_start.py`.

Classify every file as:

- correct;
- stale;
- missing;
- contradictory.

### Step B — Apply one coherent repair

The repair must make these truths agree:

```yaml
new_kb_entry:
  operator_surface: start
  public_command: python apex-meta/scripts/apex_kb.py start
  old_capability_question_first: false
existing_controlled_kb:
  lifecycle_surface:
    - control next
    - control run
    - control reconcile
```

Do not create another parallel command path.

### Step C — Repair the public Start wrapper

The documented Start invocation must expose and forward:

- `--config`;
- `--repo-root`;
- `--allow-write`;
- `--dry-run`;
- `--strict`;
- `--json`.

Flag placement after `start` must work consistently with the command contract.

### Step D — Run component acceptance

Required evidence:

1. Start unit tests pass;
2. control-plane tests pass;
3. `apex_kb.py start --help` exposes the intended flags;
4. preview-only synthetic Start succeeds;
5. preview creates no KB files;
6. package manifest inventories every Start asset;
7. no live reference still instructs a new KB to begin with manual `control init`.

### Step E — Run the decisive fresh canary

Use a new Codex conversation and only:

```text
$apex-kb Create a new Apex KB from the Leela source corpus. Run only Setup and Phase 0, and stop at the Phase 1 boundary.
```

Immediate pass condition:

```yaml
first_response:
  old_capability_question_present: false
  start_intake_or_start_configuration_surface_present: true
```

If the first response fails, stop. Do not answer the old question. Do not continue the run.

## 8. Required reporting discipline

The continuation chat must report in this order:

1. **Target behavior**
2. **Current proof level**
3. **Exact files changed**
4. **Executed test evidence**
5. **Fresh-canary first response**
6. **Remaining blocker**

It must not report broad architectural progress as a substitute for the target behavior.

## 9. Completion gate

Phase 0 Start routing is complete only when all statements below are true:

```yaml
completion_gate:
  main_contains_complete_repair: true
  stored_files_reread_after_write: true
  start_help_exposes_documented_flags: true
  preview_is_no_write: true
  start_tests_pass: true
  control_tests_pass: true
  fresh_canary_uses_start: true
  fresh_canary_omits_old_capability_question: true
  no_phase1_work_started: true
```

Until then, the truthful status is:

```text
START ROUTING NOT PROVEN
```

## 10. Operator trust rule

The operator should never again be asked to infer whether a proposed repair is active.

The executor must provide one of two clear outcomes:

```text
CANARY PROVEN — the fresh invocation produced the intended Start behavior.
```

or:

```text
NOT PROVEN — here is the exact failing file, command, or first response.
```

No intermediate artifact count, commit count, or architecture explanation substitutes for that proof.
