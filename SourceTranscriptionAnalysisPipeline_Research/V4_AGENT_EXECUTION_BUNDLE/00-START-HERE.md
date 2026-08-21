# V4 Direct Local Transcript-to-Knowledge — START HERE

## ROLE

You are the **lead execution orchestrator**.

Your job is to execute the V4 local transcript-to-knowledge implementation to real output.  
You own sequencing, delegation, integration decisions, verification, and the final handoff.

Do **not** turn this into another architecture-research exercise.

## READ ORDER

Read only these files at startup:

1. `01-EXECUTION-MAP.yaml`
2. `02-AGENT-CONTRACTS.yaml`
3. `03-TEST-CORPUS.yaml`
4. `04-EXECUTION-STATE.yaml`
5. the YAML file for the module you are about to execute

Do not preload all module files into context.

## AUTHORITY

For this execution:

1. current operator instruction;
2. this V4 execution bundle;
3. current repository code and installed-tool reality;
4. `SourceTranscriptionAnalysisPipeline_Research/current-decision-workspace/02-DECISIONS.md` only where it does not conflict with this V4 execution bundle;
5. older V1/V2/V3 material is reference-only and must not become execution authority.

## EXECUTION MODE

- Work directly on `main`. Do not create a branch.
- Prefer native subagents/workers when available.
- The lead keeps the global context.
- Workers receive one bounded module packet, not the whole project history.
- Workers return structured results; the lead independently verifies the module.
- Use one writer worker at a time unless two workers have provably disjoint write scopes.
- Do not allow nested subagents unless the lead explicitly decides a module requires it.
- Do not ask the operator for routine next steps. Continue through the DAG.
- Ask the operator only for a genuine permission/credential/irreversible decision not covered by the plan.

## START COMMAND

Begin with `modules/M00-PREFLIGHT.yaml`.

After each module:
1. verify its acceptance observations yourself;
2. update `04-EXECUTION-STATE.yaml`;
3. continue to the next ready module.

The target is not a passing test suite.

The target is three real `knowledge.md` artifacts from the declared corpus, or a precise blocker showing which fixed pipeline component prevented that outcome.
