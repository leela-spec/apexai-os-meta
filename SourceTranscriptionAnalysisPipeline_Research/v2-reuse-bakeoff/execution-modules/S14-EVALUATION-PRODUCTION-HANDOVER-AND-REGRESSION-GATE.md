# S14 — Evaluation, Production Handover, and Regression Gate

**Execute only S14, then stop.**  
**Input:** complete S00-S13 vertical-slice run  
**Next:** no automatic next stage; orchestrator decides regression/repair.

## Outcome

Judge the **actual end product and production chain**, record the selected composition that really ran, and decide whether the first vertical slice is ready to expand to four-source/fresh bilingual/resume regression.

This stage is not permission to build another validator framework.

## Context to load

- this file;
- handoffs S00-S13 for the same run;
- actual compiled knowledge product from S13;
- stage-local selection notes generated during S02/S03/S06/S10/S11;
- `03-BENCHMARK-AND-TEST-SPEC.yaml` only for the specific acceptance dimensions needed here;
- Fabric/Open Notebook/DeepEval component entries only if a bounded comparison is actually run.

Do not reload V1 or all failed-run evidence.

## Evaluation priorities

1. **Product quality first:** useful, faithful, source-specific knowledge.
2. **Real execution:** every required semantic stage came from allowed external CLI transport.
3. **Evidence integrity:** transcript provenance and factual evidence are inspectable.
4. **End-to-end chain:** each stage output is the declared next-stage input.
5. **Operational value:** the selected route is maintainable and resumable.

## Work

1. Reconstruct the exact composition from the stage handoffs; do not trust an old `SELECTION.yaml`.
2. Read the actual knowledge artifact under a realistic operator reading constraint. Evaluate thesis usefulness, Meso coherence, important-insight recall, factual grounding, uncertainty preservation, concision, and obvious omissions.
3. Inspect a sample of source evidence directly.
4. Verify that all semantic Map/Reduce/verification records identify allowed real CLI transports.
5. Summarize retained/conditional/rejected/blocked components based on this run only.
6. Optional: run a bounded Fabric/Open Notebook product comparison or DeepEval metric only if it can respect current transport constraints and adds information; these are not sole authorities.
7. Write a concise production handover containing the exact command/entrypoint, actual selected tools/configurations, current limitations, and unresolved stage decisions.
8. Decide one of:
   - `VERTICAL_SLICE_ACCEPTED_FOR_REGRESSION`;
   - `REPAIR_STAGE_Sxx`;
   - `BLOCKED_OPERATOR_DECISION`.

## Required regression gate after vertical-slice acceptance

Do **not** implement new architecture for regression. Reuse the same S00-S13 modules/configuration to perform, under orchestrator control:

1. four-source semantic regression on the existing benchmark corpus;
2. genuinely fresh English audio -> ASR -> knowledge E2E;
3. genuinely fresh German audio -> ASR -> knowledge E2E;
4. real resume test: unchanged rerun causes zero duplicate valid semantic calls;
5. targeted invalidation: invalidate one Map unit and prove only it plus required downstream work reruns.

Each regression run must produce the same stage handoffs/artifacts. The orchestrator may schedule them as separate sessions/runs after this module.

## Tests / checks

- no stage handoff missing;
- no stage PASS contradicts its actual artifact;
- source/acquisition/ASR chain is real where mode is fresh;
- CLI transport classes conform to Trial-1 lock;
- final product is source-specific and not cross-contaminated;
- selected components match what actually ran;
- limitations remain visible rather than being averaged into PASS.

## Outputs

- `<run>/evaluation/S14-final-evaluation.md`;
- `<run>/evaluation/PRODUCTION-COMPOSITION.yaml`;
- `<run>/FINAL-HANDOVER.md`;
- S14 handoff.

Do not overwrite canonical global `FINAL-REPORT.yaml` with `PASS` merely because one vertical slice passed. Global final promotion occurs only after the orchestrator accepts the required regression suite.

## Git

Commit/push the truthful vertical-slice evaluation/handover. Use a message describing what was actually demonstrated, e.g. `test(transcript): accept V2.1 first vertical slice` only when the product really passes.

## Final response

Return vertical-slice verdict, exact production composition, run/commit SHA, important product findings, limitations, and handover paths. Then **STOP and wait for orchestrator review.**