# S13 — Deterministic Compilation and Product QA

**Execute only S13, then stop.**  
**Input:** S11 Reduce + S12 verification results/state  
**Next:** S14

## Outcome

Compile the canonical machine knowledge and human-readable wiki using TTK, then inspect the actual product for obvious semantic/source failures before evaluation.

## Context to load

- this file;
- S11 and S12 handoffs;
- TTK compiler/complete-validator code and tests;
- actual Reduce/verify artifacts;
- generated wiki only after compilation.

No external AI is needed to perform compilation.

## Tool

Existing TTK compiler. Do not introduce a UI/RAG framework here.

Typical command pattern:

```powershell
python .claude/skills/transcript-to-knowledge/scripts/ttk.py compile <run>\ttk
python .claude/skills/transcript-to-knowledge/scripts/ttk.py validate <run>\ttk --complete
```

Use current supported syntax.

## Work

1. Verify S11/S12 hashes match current TTK state.
2. Compile the wiki/machine artifact from current valid state.
3. Run complete validation.
4. Inspect generated index, Macro, every Meso module title/summary, and a representative set of Micro claims/concepts/entities.
5. Cross-check at least several factual claims against their cited transcript evidence.
6. Inspect source identity/title/language throughout the output.
7. Search for obvious cross-source contamination, generic process boilerplate, orphan links, stale pages, or duplicate artifacts.
8. If compilation exposes a semantic defect, do not patch Markdown manually. Record the defect and return the stage to the owning upstream module through the orchestrator.

## Tests

Mechanical:

- TTK compile succeeds;
- `validate --complete` succeeds where verification state permits;
- generated links resolve;
- stale generated pages are handled correctly;
- output hashes/state point to current Reduce/verify inputs.

Product QA:

- Macro answers what the source is actually about;
- Meso modules form a coherent semantic map;
- Micro claims are useful and traceable;
- no content from another source is present;
- German source remains linguistically coherent where appropriate;
- output is useful to read, not merely structurally complete.

## Outputs

- canonical TTK wiki/machine artifacts;
- `<run>/evaluation/S13-product-qa.md` with concrete inspected examples and any defects;
- S13 handoff.

Handoff must name wiki/index/Macro paths, compile/complete-validation results, product QA verdict, and any upstream repair stage needed.

## Acceptance

PASS requires both structural completion and a sane actual knowledge product. A validator PASS cannot override an obviously wrong-source or meaningless wiki.

Commit/push relevant compiler/test fixes and product artifacts according to repo policy, return handoff, **STOP.**