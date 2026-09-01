# Program Orchestrator — 13-Module Docker Stack Integrity Correction

## Program objective

Bring the implemented `ki-basis` stack from `CORRECTION_REQUIRED` to evidence-backed `PASS` by fixing exactly 13 post-verification integrity defects. Preserve the accepted runtime topology unless a module's independent proof demonstrates that a specific assumption is false.

## Program baseline resources

These are global references, not all-active context:

- `ki-basis/compose.yaml`
- `ki-basis/.env.example`
- `.gitignore`
- `ki-basis/docker/nginx/default.conf`
- `ki-basis/docker/postgres/init/01-init-databases.sh`
- `apex-meta/Alpine/INTEGRATION-ACCEPTANCE-REPORT.md`
- `apex-meta/Alpine/ARCHITEKTUR-BASIS.md`
- `apex-meta/Alpine/ImplementationPlans/`
- Antigravity instruction-orchestrator skill and references

The final acceptance report is evidence from the prior run, not unquestionable authority. Re-check live runtime and Git state whenever a module depends on a runtime claim.

## Coordinator state

During execution maintain one compact durable state file:

`apex-meta/Alpine/INTEGRITY-CORRECTION-STATE.md`

Keep it short. Required fields:

```yaml
program: docker-stack-integrity-correction
status: ACTIVE | BLOCKED | COMPLETE
baseline_head: <sha>
accepted_through: M00 | M01 ... M13
active_module: M01 ... M13 | null
last_commit: <sha>
last_result: PASS | PASS_WITH_LIMITATIONS | BLOCKED_HUMAN_GATE | CORRECTION_REQUIRED | FAIL
blocker: <one line or null>
next_module: <id or null>
runtime_snapshot: <one-line health summary>
evidence: <current result file path>
```

Do not turn this file into a narrative log. Module evidence belongs in module result files.

## Result files

Each module writes one compact result under:

`apex-meta/Alpine/IntegrityResults/MXX-RESULT.md`

Every result must contain:

- exact pre-module branch head;
- changed files;
- commands/runtime actions actually executed;
- positive proof;
- negative/adversarial proof;
- any limitation;
- resulting commit SHA;
- final module verdict.

No self-authored `PASS` counts without the named evidence.

## Execution sequence and dependencies

| Module | Target | Depends on |
|---|---|---|
| M01 | `.env` Git protection | baseline only |
| M02 | fail-closed required secrets | M01 |
| M03 | tested image pinning | M02 |
| M04 | Hermes port semantics | M03 |
| M05 | repair moved Antigravity links | baseline only; run after M04 for orderly sequence |
| M06 | canonical plan authority | M05 |
| M07 | OpenProject volume hygiene | M03 |
| M08 | durable Hermes connectors | M02, M04 |
| M09 | complete backup coverage | M07, M08 |
| M10 | application-level restore proof | M09 |
| M11 | nginx route proof | M04, current app runtime |
| M12 | architecture documentation integrity | M01-M11 accepted |
| M13 | independent final verifier | M01-M12 accepted |

## Autonomous iteration rule

The program may continue M01 -> M13 without operator approval when all of the following are true:

- current module scope is fully defined;
- no secret value is being committed or exposed;
- no destructive migration is required;
- no architectural ownership/topology decision is being changed;
- module verification returns PASS;
- one bounded module commit is complete;
- coordinator state is updated;
- active context is reset before the next module.

If any condition fails, stop with the smallest exact operator gate.

## Patch discipline

- Existing files: minimal patches only.
- New files: only when needed for durable configuration, evidence, or missing authority.
- Do not reformat entire YAML/Markdown files as collateral change.
- Do not rename services, volumes, ports, folders, or authority files outside the active module.
- Preserve persistent volumes and user data.

## Verification doctrine

Every module must include at least one check that would fail if the intended correction were bypassed. Prefer live runtime, Git diff, deterministic command receipts, and actual application APIs over implementation-owned status text.

## Final success

The program is COMPLETE only when M13 independently verifies all 13 corrections against live Git state and, where relevant, the actual running Docker stack, then records the corrected overall verdict.