---
type: ContinuationHandover
title: Universal AI Instruction System — Integrity Recovery and Continuation
status: READY
created: 2026-09-19
repository: leela-spec/apexai-os-meta
branch: main
verified_main_at_creation: 8032e63ce1fc6c5394b91cd2790b6e3c340d066a
---

# Universal AI Instruction System — Integrity Recovery and Continuation

## Current state

Repository: `leela-spec/apexai-os-meta`  
Branch: `main` only  
Program root: `apex-meta/handoff/universal-ai-instruction-system/`

At handover creation, the live program README shows:

- A01–A13 completed, with A09 merged into A01.
- A13 completed with the current evidence-first grounding rule.
- C01 `<decision>` is `NEXT`.
- C02 and C03 are queued.

The live README remains the authority if the repository has advanced after this handover.

## Integrity recovery completed

A repository-integrity audit found that several earlier AI edits replaced large portions of existing files instead of applying bounded edits, causing useful historical research to disappear from current artifacts.

Recovery packet:

`apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-19-integrity-recovery/`

The recovery patches P01–P05 were applied in:

`8032e63ce1fc6c5394b91cd2790b6e3c340d066a`

Commit message:

`docs(universal-ai-instruction-system): apply integrity recovery patches P01-P05`

The recovery preserved the current decisions while restoring discoverability of superseded research and adding an exact-match mutation-integrity rule to the module handover.

## Important mutation constraint

Existing files should now be changed only through bounded exact-match edits.

The live handover file contains the detailed rule:

`09-MODULE-DEEPENING-HANDOVER.md`

The important operational consequence is:

- no whole-file regeneration for localized changes;
- re-read the live file before editing;
- exact old block must match once;
- inspect the exact diff;
- if the tool cannot guarantee bounded editing, create a patch for a deterministic CLI executor instead of modifying the file directly.

## Current A13 decision

A13 is intended as normal evidence-first web grounding, not a special deep-research workflow.

Current behavior:

```text
actual frame + problem + task + environment
        ↓
normal web search for established best practice
        ↓
at least 3 verified-quality sources by default
        ↓
check whether the sources materially agree
        ↓
reason from the evidence
        ↓
answer / design / implement
```

If reliable sources materially disagree, or the task/environment is materially complex, research can expand proportionately and the disagreement should be surfaced.

The exact three-source floor is a local operating control, not a claim of universal industry standard.

## Source-Governed Execution Contract

Keep this as a separate later synthesis / operational-integration item:

`14-SOURCE-GOVERNED-EXECUTION-CONTRACT-CANDIDATE.md`

It should not be silently absorbed into C01, C02, or A13.

## Graded-rigor question

Separate project-management artifact:

`apex-meta/epics/universal-ai-instruction-system-graded-rigor/epic.md`

Current framing:

- normal grounding is the baseline;
- graded rigor concerns how much additional rigor is needed when ordinary execution is insufficient;
- no custom L1/L2/L3 scale is currently authorized;
- established graded/tailoring approaches remain research inputs.

## Preserved historical research

The integrity recovery added explicit Git-history references for material that had been lost from current files.

Relevant historical snapshots include:

### A01 before A09 merge

```bash
git show 69d16a2d462c0d155770316f0eb63acbe269202d:apex-meta/handoff/universal-ai-instruction-system/module-deepening/A01-target-outcome-alignment/README.md
```

### First complete A13 result

```bash
git show 1fee4df44f4ac87acd2b2074d6b162b0ec430451:apex-meta/handoff/universal-ai-instruction-system/module-deepening/A13-external-grounding-real-world-verification/README.md
```

### A13 grounding-by-default revision

```bash
git show bdc9a657e1237cc02519cc4cfbf0beaa15053f3a:apex-meta/handoff/universal-ai-instruction-system/module-deepening/A13-external-grounding-real-world-verification/README.md
```

### Original graded-rigor research

```bash
git show 571717fc2933d625d3ec2b8e7976387787d722c5:apex-meta/epics/universal-ai-instruction-system-graded-rigor/epic.md
```

These are historical research inputs, not current authority.

## Continuation target

The next chat should first re-read:

1. `README.md`
2. `09-MODULE-DEEPENING-HANDOVER.md`
3. `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
4. the integrity recovery packet README

Then confirm the live `NEXT` module.

At handover creation, that module is:

### C01 — Conditional Decision / Trade-off Discipline

The continuation should execute one module only and then stop.

## Design pressure for C01

C01 should remain lean.

Questions to resolve through current verified research:

- When does a real decision/trade-off need to be surfaced to the operator?
- How should alternatives be presented without forcing formal matrices onto routine work?
- Which established decision methods are already used in mature AI/agent systems?
- How should C01 interact with A13 grounding, A08 evidence quality, A01 target alignment, and the separate graded-rigor question?
- Can the rule stay compact enough for an always-loaded contract?

Avoid inventing a custom scoring/ranking system unless established evidence shows it is needed.

## Operator priorities preserved

- main only;
- one module at a time;
- reuse established/battle-tested methods before invention;
- normal web grounding before model-only best-practice reasoning;
- at least three verified-quality sources by default for A13-style externally knowable work;
- increase research only when complexity/conflict warrants it;
- avoid over-engineering;
- do not drift into adjacent modules/projects;
- use deterministic bounded edits for existing files;
- useful outcome over process/checkmark completion.
