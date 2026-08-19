# S11 — Global Reduce and Synthesis

**Execute only S11, then stop.**  
**Input:** validated S09 evidence ledger + optional S10 advisory warnings  
**Next:** S12

## Outcome

Produce the source's real Macro/Meso/Micro knowledge structure through a **real allowed subscription CLI**, using the validated evidence ledger rather than rereading the entire raw transcript.

## Context to load

- this file;
- S09 handoff and exact Reduce/evidence packet;
- S10 handoff only if advisory warnings were retained;
- TTK Reduce result contract and validator;
- S08 hardened semantic adapter;
- `06-TRIAL1-TRANSPORT-LOCK.yaml`;
- DocETL registry entry only if running the bounded challenger.

Do not load the full transcript unless a concrete contract/debug issue requires a narrow source check. The semantic Reduce input is the validated compact ledger.

## Recommended route

**Production reference:** direct real subscription-CLI Reduce.  
**Challenger:** fixed DocETL Reduce/orchestration with optimizer OFF, only if it can use an allowed Trial-1 CLI adapter without disproportionate work.

If DocETL cannot meet the transport rule, mark it `BLOCKED_FOR_TRIAL1`; do not use an API and do not build a fake DocETL substitute.

## Semantic target

Reduce must create:

- a useful source-specific Macro thesis and major takeaways;
- real semantic Meso modules independent of processing-window boundaries;
- refined Micro claims with lineage back to validated evidence;
- mechanisms/protocols/arguments/caveats where meaningful;
- important disagreements, corrections, uncertainty, and low-confidence material appropriately labeled;
- coverage across the whole source, including later windows.

It must keep transcript `source_support` separate from external-world truth.

## Work

1. Verify evidence-ledger hash matches S09.
2. Invoke the same real allowed CLI class established in S07/S08 unless there is a documented orchestrator-approved change.
3. Produce one Reduce result matching current TTK contract.
4. Validate it deterministically.
5. Inspect the actual knowledge structure, not just schema.
6. If DocETL is a material challenger and transport-compliant, run a small fixed comparison using the same validated evidence. Keep optimizer off for attribution.
7. Choose the reference Reduce route for this first implementation based on product quality + complexity, not framework prestige.

## Tests

Mechanical:

- actual external CLI subprocess proves semantic execution;
- Reduce references resolve to existing validated claims/evidence;
- raw full transcript was not silently used as a substitute input;
- schema/TTK validator passes;
- failed CLI does not generate fake Reduce output.

Product:

- Macro is informative and source-specific;
- Meso headings are semantic, not fixed quartiles/templates;
- important later-source themes are represented;
- claims are not indiscriminately stamped supported;
- uncertainty/contradictions survive;
- no content from a different benchmark source appears.

The wrong-source mixture previously observed in `oZIsMX6WgFs` is an automatic product FAIL.

## Outputs

- actual TTK Reduce result;
- optional DocETL comparison artifact if genuinely run;
- `<run>/evaluation/S11-reduce-decision.yaml`;
- S11 handoff.

Handoff must name Reduce path/hash, actual provider/executable/transport, selected route, challenger status, validation result, and a concise product-quality inspection.

Commit/push, return handoff, **STOP. Do not verify externally or compile.**