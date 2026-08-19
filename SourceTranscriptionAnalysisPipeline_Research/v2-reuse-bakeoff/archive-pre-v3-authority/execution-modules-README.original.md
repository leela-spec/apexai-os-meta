# V2.1 Modular Execution Packet

This directory is the **direct execution surface** for the first V2.1 implementation.

Do not give a CLI AI the entire V2/V2.1 corpus. Give it:

1. `00-ORCHESTRATOR-GUIDE.md` only for the first session or when protocol is unclear;
2. exactly one active `Sxx-*.md` module;
3. the previous stage handover, if any;
4. only the input artifacts and owning code/contracts named by that module.

The CLI executes one module, tests it, saves its artifacts, writes the required handover, commits/pushes that stage if the module says it is ready, and **stops**. It may not continue to the next module.

Sequence:

- S00 Trigger and run initialization
- S01 Source acquisition
- S02 ASR and ASR selection
- S03 Conditional alignment/diarization
- S04 TTK canonical custody
- S05 TTK processing windows
- S06 Optional local pre-extraction
- S07 Grounded semantic Map
- S08 Structured output and retry seam
- S09 Deterministic Map validation / evidence ledger
- S10 Advisory source-support checks
- S11 Global Reduce / synthesis
- S12 Selective external verification
- S13 Deterministic compilation / product QA
- S14 Evaluation, production handover, and regression decision

The orchestrator verifies each returned handover before the operator starts the next module.