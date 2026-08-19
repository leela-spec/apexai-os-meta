# V3 Execution Modules

These files are **fresh-context work packets** for Antigravity CLI.

One module = one Antigravity context.

Do not concatenate all modules into one giant prompt. That was a major failure mode in the previous implementation effort.

## Execution order

1. `M00-ORCHESTRATION-SMOKE.md`
2. `M01-PROVEN-SYSTEMS-LANDSCAPE-AND-BASELINES.md`
3. `M02-ASR-AND-TRANSCRIPT-BASELINE.md` — conditional
4. `M03-GROUNDED-EXTRACTION-BAKEOFF.md` — conditional
5. `M04-GLOBAL-SYNTHESIS-AND-KNOWLEDGE-BAKEOFF.md` — conditional
6. `M05-EVALUATION-AND-SELECTION.md`
7. `M06-PRODUCTION-INTEGRATION.md`
8. `M07-THREE-SOURCE-E2E-REGRESSION.md`

## Context rule

For each module load only:

- `../CURRENT-WORK.md`;
- the active module file;
- the exact prior result/artifacts and project files named by the module.

Do not preload V1/V2/V2.1 architecture/history unless the module explicitly names one historical evidence file.

## Normal repair behavior

Inside a module the executor owns normal iteration:

`run -> inspect -> fail -> diagnose -> fix -> rerun`

Do not return after every local failure.

After two corrective iterations on the same subsystem without product advancement, stop with `APPROACH_SUSPECT` instead of patching a third time.

## Result

Save:

`../results/Mxx-RESULT.md`

The Git commit is the main handoff. The result file is a compact reconstruction aid, not a second workflow engine.
