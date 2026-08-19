# M06 — Production Integration

## TARGET

Implement only the production composition frozen at R2 and expose one simple source-to-knowledge execution path.

## Read only

- `../CURRENT-WORK.md`
- R2-approved M05 selection report
- code/components named by that selection
- exact winning candidate artifacts/tests needed for regression

Do not reread all V2/V3 research.

## Required behavior

The selected production path must accept the source forms justified by R2, such as:

- URL/video/audio;
- transcript input when supported.

It must produce the selected canonical knowledge artifact with source/timestamp traceability.

## Implementation rules

- reuse winner code/project/components directly where practical;
- prefer configuration or a light fork over wrapper stacks;
- preserve only custom TTK pieces that R2 proved necessary;
- remove or keep off-path experimental candidates that did not win;
- do not build a new orchestration/state framework;
- normal local repair iteration is allowed inside this module.

## New custom code gate

Before any new abstraction, record in the code/result:

```text
Existing solution tried:
Observed failure:
Why configuration/light fork is insufficient:
Smallest custom addition:
```

If this cannot be filled from observed evidence, do not build the abstraction.

## Tests

Test the actual user-facing path, not only adapters/schemas.

At minimum:

- one real representative source reaches final knowledge output;
- selected transcript/semantic workers actually run;
- final artifact is source-specific and opens correctly;
- references/timestamps resolve at the level promised by R2;
- failure does not silently create a fake successful artifact;
- rerun/recovery requires no manual hidden state surgery.

## Output

- production runner/config/code selected by R2;
- one real vertical-slice artifact;
- `../results/M06-RESULT.md`.

End with one:

- `PASS: READY_FOR_M07`
- `APPROACH_SUSPECT`
- `BLOCKED`
- `OPERATOR_DECISION`

## Stop-loss

If the selected composition needs two non-product repair cycles on the same integration seam, stop and report `APPROACH_SUSPECT`; do not grow another framework around it.
