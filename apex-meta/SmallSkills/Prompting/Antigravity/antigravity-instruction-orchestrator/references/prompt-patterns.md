# Antigravity Prompt Patterns

## Contents

1. Bounded module correction
2. Teamwork plan gate
3. Post-verification hygiene
4. Real-product POC
5. Verification-only preflight
6. Operational multi-module handover
7. Independent report audit

## 1. Bounded module correction

```text
Repair exactly ONE module: <ID>.

Repository: <repo>
Workspace: <path>
Branch: <branch>
Authority: @<authority-file>

Core failure:
<one precise defect>

The named target that must execute is:
<TARGET PRODUCT/LIBRARY + exact interface>

The following do NOT count:
- <substitute 1>
- <substitute 2>

Before implementation define:
1. exact claim;
2. independent oracle;
3. deliberate failing case;
4. actual runtime crossing;
5. pass conditions.

Do not touch <other modules>.
Run relevant tests and independent verifier.
Commit only this module.
STOP.
```

## 2. Teamwork plan gate

```text
/teamwork-preview

Implement exactly <module/capability>.
Use DEVELOPMENT integrity mode.

Authority: @<file>
Also obey: @AGENTS.md @.agents/rules/... @.agents/skills/...

Phase 1 only:
- recheck official docs;
- inspect current code/runtime;
- name exact target APIs;
- define independent oracle;
- define anti-facade negative test;
- identify human gates;
- define exact files/scope/pass conditions.

STOP after the reviewable plan artifact.
Do not implement until I approve the plan.
```

## 3. Post-verification hygiene

```text
<Module> POST-VERIFICATION CORRECTION ONLY.

The core architecture is accepted. Do NOT redesign it.
Do not start another module.

External audit found exactly these residual issues:
1. <issue + required correction>
2. <issue + required correction>

Acceptance:
- existing core tests still pass;
- add independent test for each residual issue;
- update verification report;
- reset task state;
- one follow-up commit;
- STOP.
```

## 4. Real-product POC

```text
POC exactly one real product: <PRODUCT>.

Success requires the ACTUAL product to participate.

First re-open current official docs and determine:
- exact version;
- official install/launch path;
- official import/API/MCP surface;
- official export/backup/restore surface.

Forbidden proof:
- local adapter presented as the product;
- fake MCP/API;
- local dict/JSON called a product backup;
- internal DB writes when supported import exists.

Required proof:
1. real product action;
2. real product observation;
3. independent source fixture comparison;
4. real product-generated export/receipt;
5. negative or permission test.

If operator GUI/account action is required, prepare everything and request the smallest exact action.
Unsupported capability => mark UNSUPPORTED/DEFERRED. Do not recreate it.
```

## 5. Verification-only preflight

```text
VERIFY ONLY. Do not modify implementation code.

Check on the installed Antigravity version:
1. workspace rule discovery/activation;
2. skill discovery;
3. custom verifier discovery;
4. hook config loading;
5. hook command from actual working directory;
6. bounded stop behavior.

Return only a PASS/FAIL matrix plus exact remediation for failed checks.
Do not begin a module.
```

## 6. Operational multi-module handover

Use when the user wants a real end-to-end layer such as email/event intake.

```text
Orchestrate this capability:
<user-visible end-to-end outcome>

Read the authoritative program dependency graph.
Classify every prerequisite as:
EXISTING_AND_HEALTHY | NEEDS_CONFIG | NEEDS_REPAIR | NOT_INSTALLED | BLOCKED

Propose execution order first.
Do not implement the whole graph in one uncontrolled run.
For each approved module:
PLAN -> IMPLEMENT -> TEST -> VERIFY -> COMMIT -> NEXT.

The program can be multi-module; each implementation boundary remains single-module.
Stop at any unsupported interface or human gate rather than inventing a substitute.
```

## 7. Independent report audit

```text
Audit the actual pushed state; do not trust the agent report as authority.

Verify:
- branch head and commit;
- changed-file scope;
- real target runtime call;
- independent oracle;
- negative/denial tests;
- evidence artifacts;
- task state;
- dependency claims.

Return:
PASS | PASS_WITH_LIMITATIONS | CORRECTION_REQUIRED | BLOCKED_HUMAN_GATE | FAIL

For any non-PASS result, give the smallest exact correction prompt.
```
