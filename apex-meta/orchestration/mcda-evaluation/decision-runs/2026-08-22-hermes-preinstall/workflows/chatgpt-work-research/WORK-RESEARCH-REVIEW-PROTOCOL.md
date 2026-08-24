# ChatGPT Work Research Review Protocol

Status: **PRE-INSTALL RESEARCH QA**

Use this after a Work thread has produced a complete Rxx draft and before writing the result to GitHub.

## 1. Preferred review setup

Use a **separate Work thread** for review.

Input only:

- the authoritative Rxx specification;
- the draft result;
- current ADR-002/state where needed;
- the load-bearing official sources cited by the draft.

Do not ask the reviewer to rely on the producing thread's explanations.

Because ChatGPT Projects can carry memory across project chats, this is not guaranteed to be a cryptographically independent reviewer. If strict independence becomes necessary for a consequential decision, run the review in a separate ChatGPT Project or with another independent research AI. For the current high-level pre-install research, the minimum requirement is a fresh Work thread that re-checks the evidence directly.

## 2. Review launcher

```text
Use ChatGPT Work as an evidence reviewer.

Repository: leela-spec/MasterOfArts
Branch: main

AUTHORITATIVE RESEARCH SPEC:
<RESEARCH_SPEC_PATH>

DRAFT RESULT:
<DRAFT_OR_RESULT_PATH_OR_ATTACHED_DRAFT>

Review the draft independently against the specification and current official sources.

Do not improve the architecture or fill gaps with your own design.
Do not accept a connection merely because it sounds plausible.
Re-open the load-bearing official sources and verify the claims they are cited for.

Check:
1. every required research task was answered;
2. every Required output item is present;
3. the Pass standard is actually met or explicitly failed;
4. official sources are current enough for the claim;
5. source text supports the exact capability claimed;
6. native vs official integration vs established package vs configuration vs custom is classified correctly;
7. no custom interconnection was silently invented;
8. inputs, outputs and persistent state are explicit;
9. API/network/local execution and data egress are explicit where relevant;
10. deterministic vs AI/hybrid execution is explicit where relevant;
11. contradictions and unresolved claims are preserved;
12. repo-specific conclusions are supported by current repository evidence;
13. the result does not replace a full required capability with a toy/MVP/reduced substitute;
14. the final decision follows from the evidence.

Return exactly:

VERDICT: PASS | REVISE | BLOCK

CRITICAL_FINDINGS:
- ...

UNSUPPORTED_OR_OVERSTATED_CLAIMS:
- claim
  evidence problem
  required correction

MISSING_REQUIRED_OUTPUTS:
- ...

STALE_OR_WEAK_SOURCES:
- ...

CONTRADICTIONS_OR_OPEN_QUESTIONS:
- ...

REQUIRED_REVISIONS_BEFORE_PERSISTENCE:
- ...

If PASS, state why the report is decision-usable.
If REVISE, do not rewrite the whole report; identify exact required corrections.
If BLOCK, identify the decision-changing evidence gap.
```

## 3. Persistence rule

Only persist after:

- the draft has a `PASS` review or all `REVISE` items have been corrected and re-reviewed;
- the operator approves saving the result;
- the result path matches `WORK-RESEARCH-LAUNCHERS.md`;
- no research prompt, ADR or install state is changed as a side effect.

The GitHub write should create/update only the designated Rxx result file unless the operator explicitly authorizes another state change.

## 4. Human review points

Human review is required when the research concludes any of the following:

- a locked target component cannot meet its required function;
- installation would require unsupported/custom infrastructure;
- a security/privacy trade-off requires accepting data egress or broader host access;
- the evidence conflicts materially with ADR-002;
- the research proposes changing the macro/meso/micro operating model;
- the report would authorize installation or migration.

Routine source corrections and wording fixes do not require a separate architecture decision.

## 5. Converting this review into a ChatGPT Skill

Do not create the Skill from this document alone.

OpenAI's current guidance is to test a workflow on real work and then save the version that actually works. After this protocol has reviewed at least one real Rxx result successfully, use Work's Skill creation flow to save the reusable review method as:

`moa-research-evidence-review`

Tell Work to preserve the checks and verdict format, but **not** the Rxx-specific findings, URLs or conclusions from the test run.
