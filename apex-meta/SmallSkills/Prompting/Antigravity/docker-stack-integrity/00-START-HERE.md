# Docker Stack Integrity Correction — START HERE

Repository: `leela-spec/apexai-os-meta`  
Branch: `main`  
Executor: Google Antigravity  
Program type: bounded post-verification correction program

## Purpose

Correct the 13 concrete integrity defects found after the `ki-basis` Docker stack implementation without redesigning the accepted runtime architecture.

This is not a new architecture project. The existing stack remains the baseline unless a module proves that one specific implementation claim is false.

## Authority order

For every module, read in this order:

1. `../antigravity-instruction-orchestrator/SKILL.md`
2. `../antigravity-instruction-orchestrator/references/lessons-learned.md`
3. `../antigravity-instruction-orchestrator/references/prompt-patterns.md`
4. `01-PROGRAM-ORCHESTRATOR.md`
5. `02-ACTIVE-CONTEXT-RESOURCE-PROTOCOL.md`
6. exactly ONE active module file from this folder
7. only the repository/runtime resources named by that module

Do **not** load all 13 module files into active implementation context.

## Baseline

The correction program begins from the currently accepted implementation line ending at the M9 integration commit. Treat live GitHub `main` and live Docker runtime evidence as authority over old chat summaries or stale reports.

## Integrity law

For existing files use patch/minimal-edit semantics. Do not rewrite unrelated sections merely to normalize style.

For each module:

`GROUND -> LOAD MINIMUM CONTEXT -> PATCH -> TEST -> ADVERSARIAL VERIFY -> WRITE RESULT -> COMMIT -> CONTEXT RESET -> NEXT MODULE`

Each module receives its own commit. A program-level run may continue automatically after a module returns PASS, but must perform the context reset defined in `02-ACTIVE-CONTEXT-RESOURCE-PROTOCOL.md` before the next major task.

STOP the whole program on:

- destructive data migration not explicitly authorized;
- secret exposure or uncertainty about secret provenance;
- architecture ambiguity that changes ownership or runtime topology;
- unsupported upstream interface;
- human/account/GUI action that Antigravity cannot perform safely;
- failure of an independent verification gate after one bounded correction attempt.

## The 13 modules

1. `03-M01-ENV-GITIGNORE.md` — protect the real `ki-basis/.env`
2. `04-M02-SECRET-FAIL-CLOSED.md` — remove fail-open secret defaults
3. `05-M03-IMAGE-PINNING.md` — pin tested images/versions
4. `06-M04-HERMES-PORT-SEMANTICS.md` — make Hermes port names/labels truthful
5. `07-M05-REPAIR-MOVED-ANTIGRAVITY-LINKS.md` — repair broken relative authority links
6. `08-M06-CANONICALIZE-PLAN-FAMILIES.md` — eliminate competing plan authority
7. `09-M07-OPENPROJECT-VOLUME-HYGIENE.md` — resolve unused OpenProject volume declaration
8. `10-M08-HERMES-CONNECTOR-PERSISTENCE.md` — persist reproducible Hermes connector definitions
9. `11-M09-BACKUP-COVERAGE.md` — back up all required stateful volumes/data
10. `12-M10-APPLICATION-LEVEL-RESTORE.md` — prove restore through the actual application interface
11. `13-M11-NGINX-ROUTE-PROOF.md` — prove or remove/fix nginx application proxy routes
12. `14-M12-ARCHITECTURE-DOC-INTEGRITY.md` — reconcile architecture documentation with implemented truth
13. `15-M13-INDEPENDENT-FINAL-VERIFIER.md` — independent final audit and corrected verdict

## Execution mode

Use Antigravity Teamwork/development behavior for implementation. Planning is a bounded preflight inside each module, not a separate long-lived plan that accumulates all program context.

The coordinator should retain only program state, not detailed implementation history.
