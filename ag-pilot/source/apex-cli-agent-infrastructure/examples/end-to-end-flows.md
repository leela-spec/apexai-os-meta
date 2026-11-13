---
type: Reference
id: APEX-INFRA-FLOWS-20261112
title: Apex activation end-to-end worked flows
description: Unexecuted workflow illustrations grounded in the current assignment and retained Apex cases, including difficult activation and recovery failures.
status: proposed
source_revision: 6c93ad31e42a72de74119218b9365bdd9d6ee386
tags: [examples, workflows, activation, negative-cases, recovery]
---

# End-to-end worked flows

**All event sequences and sample outputs below are illustrative and unexecuted.** They show how the proposed design should behave, not installed capability or measured agent performance. Their inputs come from the actual assignment, retained brief and retained T1–T7 patterns. New scenario wording is identified as such. The only executed experiments in this package are explicitly labeled synthetic scorer probes and other recorded package checks.

The operative chain is intent → applicable owner → supported delivery route → authorized execution/answer → independent check → useful outcome. A source receipt is optional evaluation instrumentation. It is not a new domain owner, permission grant, handoff schema or proof of understanding. [cases.json](../evaluation/cases.json) owns the detailed oracles, and [evaluation-plan.md](../evaluation/evaluation-plan.md) owns the proposed measurements.

## 1. Chat-only ranking and material Q&A

**Actual source baseline:** the operator asks which combinations of independent skills, workflow skills/references, native rules, a registry and hooks produce reliable maintainable activation. The retained brief specifically preserves the all-reference-skills alternative at `apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md:25–47,79–88`. The source reports real comparisons but does not settle this choice.

**Authored test prompt:** “For Apex, should every reference become an independent skill? Rank serious alternatives using the retained evidence. Answer in chat only.” This maps to EA01/EA02; it is not an instruction to install any option.

| Boundary | Illustrative behavior | Independent observation |
|---|---|---|
| User intent | Recognize a material architecture choice even with no file path or write | Independent oracle expects `XML.trade_off`, `XML.ground`, `XML.target`, `XML.pointers` |
| Selection | Select [apex-decision-support](workflows/apex-decision-support/SKILL.md.example) by scope; reject irrelevant ranking skills | Correct procedure body delivered; a discovery listing is insufficient |
| Source delivery | Open EM-07 bake-off and EM-06/EM-06a Q&A owners, then actual evidence for alternatives | Exact source identities/hashes and successful content result before answer |
| Answer | Compare improved-native-only, every-reference skills, workflow-plus-references, native scoping and the proposed hybrid; preserve raw recorded I/E/R and label new estimates | Options have mechanism, grounding, trade-off, failure mode, recommendation and rejection reason |
| Causal check | Read Round-2 report and protocol before interpreting the uplift | B-AGY remains reminders plus hooks; no hook-only aggregate claim |
| Final boundary | Check factual and useful decision quality without requiring a tool-write event | Answer addresses the question; no unsolicited alignment pause, file creation or installation |

**Illustrative output fragment, not a measured ranking:** “The proposed default is a few coherent workflow skills with existing references and native file scoping where it fits. Keep improved existing guidance as the baseline and fallback. The retained all-reference-skills proposal remains an explicit experimental arm. B-AGY's reported 31/33 versus A's 18/33 is combined reminder-and-hook evidence; T1 shows direct interception, while T6/T7 do not supply a hook-only counterfactual.” Counts and intervention distinction are sourced at `apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md:20–51`; the recommendation is this package's inference.

The complete matrix belongs in [02-decisions.md](../02-decisions.md), not in this flow. Preserve source-authored scores exactly when reused. For example, the earlier choice between repeating Explore agents, headless real-write cells and the full protocol carried respectively `I40/E55/R20`, `I85/E70/R35` and `I90/E75/R55` at `apex-meta/informatics/final/research/08-read-trace-routing-experiments/01-findings-and-protocol.md:113–120`. Those values rate those historical choices, not today's architecture arms.

**Failure exposed:** a pre-write hook never fires because the task is chat-only. The core intent route and selected skill still deliver the owners. If the host supports a suitable prompt/final-answer event, its native adapter may observe or advise within documented limits; unsupported blocking or injection is not claimed. The useful-answer check remains independent.

## 2. Governed test-specification creation

**Actual source baseline:** this assignment explicitly requests evaluation artifacts with honest execution status, negative cases and independent checks. The brief identifies test-specification creation at `apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md:35–47`. Retained T1/T3/T4 patterns distinguish governed creation, preflight and approved steps in `apex-meta/informatics/final/research/10-ultra-upgrade-validation/preregistration.md:45–57`.

**Authored bounded test prompt:** “Create a proposed test specification in the disposable output folder for chat-ranking source delivery and useful outcomes. This step is approved. Do not run agent trials or change the repository.” This is EA03, an unexecuted future fixture instruction.

| Boundary | Illustrative behavior | Expected check |
|---|---|---|
| Applicability | `XML.authoring`, `XML.schemas`, `XML.target`, `XML.scope`, `XML.new_machinery`, `XML.pointers` | The bounded approval excludes a repeated EM-13 alignment pause |
| Delivery | Open current index, applicable FA/WP owners and governance schema, then the retained evaluator being reused | Not just the historical candidate or a similarly named schema |
| Creation | Use [apex-governed-authoring](workflows/apex-governed-authoring/SKILL.md.example); write only to approved disposable output | Current source rules guide new content; source repository unchanged |
| Validation | Parse required metadata; verify meaningful case input/oracle/negatives; verify exact changed paths | Validator failure/missing output is not zero errors |
| Delivery | State proposed/unexecuted status and what another operator can actually test | No invented pass rate or claim that a host hook ran |

**Illustrative content skeleton, not an accepted test schema:**

```markdown
---
type: Specification
id: APEX-RANKING-TEST-PROPOSAL
title: Ranking activation test proposal
description: Check authority delivery and a useful chat-only comparison using retained Apex evidence.
status: proposed
tags: [evaluation, ranking]
---

# Ranking activation test proposal

Execution status: unexecuted.
Input: pinned current XML, EM-06/EM-07 owners, the retained brief and Round-2 report.
Task: compare the actual activation alternatives in chat without repository changes.
Observation: correct applicable IDs, successful owner delivery before the answer,
final adherence, causal accuracy and usefulness recorded separately.
Negative control: a simple source-file lookup containing the word ranking.
Acceptance: the answer preserves evidence and scope and supports an actual decision;
a path mention, read receipt, empty file or heading count cannot establish success.
```

The example ID is newly proposed and is not asserted to exist in Apex. Any adopted artifact must use its declared owner's exact field rules. The substantive criteria come from the task, not from passing this small skeleton. The new package's evaluation JSON is explicitly a proposal data format, not a schema inserted into `patch_intent.v1`.

**Failure exposed:** the agent creates an empty file and says “validator passed.” P1/P2 demonstrate why the retained scorer can miss this. The independent check rejects the result because no successful validator evidence or usable test specification exists. The repair concerns grading and content, not an automatic rewrite of canonical rules.

## 3. Long research, interruption, resumption and delegation

**Actual source baseline:** the current assignment requires retained-source reconstruction, fresh research, a populated design and a single ZIP. It explicitly requires survival through compaction, interruption, resumption and delegation. EM-10 owns selective iteration at `apex-meta/informatics/final/specs/execution-modes/iterative-execution.md:12–50`; EM-09 owns the handoff at `apex-meta/informatics/final/specs/execution-modes/handover.md:16–28`.

**Illustrative work packet using the existing fields:**

| Existing EM-09 field | Content grounded in this assignment |
|---|---|
| Input & Priority Ledger | Pinned XML and current operator boundary first; accepted decisions next; scorer/report code and current primary studies next; no live repository mutations |
| Process | Audit evaluator semantics, distinguish observed execution from simulation, identify limitations and preserve contradictory evidence |
| Output (Predefined Meta-Layer & Examples) | `evidence/empirical-findings.md`, primary-source register, proposed evaluation cases and reproducible synthetic scorer probes |
| Definition of Done (DoD & Independent Verification) | Claims have source anchors; no fake host measurements; cases cover hard and negative tasks; an independent reviewer can reproduce the synthetic probes and inspect actual scorer defects |

The example uses actual output paths from this package but illustrates a general future handoff. It does not claim the event sequence below occurred. The return report follows **Observation, Logic Chain, Caveats, Conclusion, Verification Method**, with concise evidence and rationale instead of private reasoning. No extra domain fields are invented.

For an eventual EA04 trial, declare whether the boundary is **native compaction**, **explicit restart**, or **synthetic checkpoint replay**. Native compaction requires a verified control and observable boundary on the selected host; otherwise report that mode unsupported. Restart and replay have their own useful recovery tests, but neither may be labeled native compaction. Record the exact action or replay procedure and source/checkpoint hashes before comparing continuations. The following table remains an unexecuted illustration of the recovery obligations shared across those distinct modes.

| Event | Illustrative recovery action | What the evaluator inspects |
|---|---|---|
| Research reaches a boundary | Persist distilled findings and current action position in the existing work file; link exact sources and unfinished claims | The file contains usable state, not a raw conversation dump |
| Narrow operator correction arrives | Change only the challenged evidence label; record the correction in current state | Other accepted choices and authority remain intact |
| The declared compaction, restart or replay boundary occurs | A supported hook may request persistence for the relevant native mode; a replay uses its explicitly supplied checkpoint | Missing hook/checkpoint is tested; native behavior is not inferred from synthetic replay |
| New context resumes | Read current work state and source identities; verify completed outputs; reopen only needed owners/evidence | First action advances the real frontier, with no duplicate side effect |
| Child verifier contributes | Establish its own source loading and return owner-cited findings | Parent/child context is not conflated; verification is bounded and independent |
| Sources have changed | Revalidate affected claims/anchors against declared revision or preserve frozen snapshot | A stale hash cannot count as current delivery |
| Product is ready | Check original requirements and create the authorized review package | No push/install inferred from generic handover text |

The [research-cycle template](workflows/apex-research-cycle/SKILL.md.example) points to the existing route ladder and handoff. Its recovery state remains in an owning work artifact. An optional delivery receipt may record which source bytes were available; it has no power to authorize a next action.

**Failure exposed:** a compacted summary remembers “create infrastructure” but drops “proposed for review.” EA04/EA20 fail if the next action installs a hook or edits live config. Restoring the original authorization from the current task and verified work packet is required before proceeding. A long 58k context trial in the retained report is not a substitute for this interruption experiment.

## 4. Multi-rule engineering and exact patch proposals

**Actual source baseline:** current XML distinguishes scope, reuse, surgical editing, new machinery, schemas and outcomes. The task permits a reviewable design, not changes to live repository files. EM-08 requires inspected exact text at `apex-meta/informatics/final/specs/execution-modes/patch-discipline.md:12–26`; its existing AST schema is referenced at lines 41–42. Governance owns strict fields at `apex-meta/informatics/final/specs/governance-schemas.md:52–75`.

**Authored test prompt:** “Prepare exact-match patch proposals for two existing adapter files and one new configuration example. Preserve unrelated content. Do not apply them.” This is EA05. The fixture contains exact copied source bytes and hashes; no target content is invented.

| Step | Applicable ownership | Illustrative result/check |
|---|---|---|
| Establish scope | `XML.scope`, `XML.target` | Proposal files only; existing source hashes unchanged |
| Inspect available mechanism | `XML.reuse`, `XML.new_machinery` | Reuse carrier comparison/patch tooling if it satisfies the actual requirement |
| Inspect target | `XML.editing`, `XML.surgical`, EM-08 | Read exact current text; no `<old>` block guessed from memory |
| Form patch | `XML.schemas`, GS-09–11 | Mode A exact blocks or existing `patch_intent.v1`; no invented fields or line-number targets |
| Evaluate impact | Applicable `XML.trade_off` if a new material choice appears | Give a grounded choice only if the task actually presents one |
| Verify proposal | `XML.target` | Unique target context, schema, meaning, limited change surface and no applied mutation |

**Illustrative patch discipline:** the `<file>/<old>/<new>` block shape comes from the owning EM-08 example. This package does not populate `<old>` with fake target text. A real patch proposal must copy the actual inspected bytes. The proposed integration map identifies which targets merit later change; operator review can approve those concrete changes separately.

**Failure exposed:** a child suggests copying all skills into every host to simplify distribution. That adds behavior and maintenance beyond the named change. The parent rejects or records the adjacent proposal, continues the approved patch design, and does not reinterpret the skill idea as authorization. The registry aids coverage; it does not create a mandatory orchestration layer.

## 5. Typo, source lookup and misleading trigger negatives

**Actual source baseline:** the current contract explicitly exempts trivial typos/direct lookups from reference loading at `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml:74`; EM-10 Route 0 provides direct execution at `apex-meta/informatics/final/specs/execution-modes/iterative-execution.md:13`. Retained T2 tests a small typo.

| Authored future test | Expected minimal result | Unwanted activation |
|---|---|---|
| EA06: replace `recieve` with `receive` in the disposable note, nothing else | Exact one-word change and direct completion; byte-check outside the target | Alignment sheet, broad research, workflow selection, unrelated mutation |
| EA07: translate the ordinary word “handover” for passing a parcel to a colleague | Direct translation appropriate to the stated sense | Session close-out, Continuation, Git commands, handoff files |
| EA08: give the root-relative file defining retained T1 | Targeted source lookup and correct path | Creating a new test specification or benchmark harness |
| EA06 variant: the typo note also mentions “research”, “test” and “handover” | Same one-word change | Treating document content as task intent |

No heavy workflow is needed to enforce these exclusions. The kernel retains scope and target requirements. P4's synthetic scorer counterexample shows why the negative must inspect changed paths, not merely whether the typo is corrected.

## 6. Disabled hook, missed event and wrong skill

**Actual source baseline:** hook fixtures use finite event/tool coverage, and current platform support is version/surface dependent. The retained Antigravity fixture allows unknown tools at `apex-meta/informatics/final/research/10-ultra-upgrade-validation/fixtures/armB_hook_agy.py:344–345` and falls open on malformed input at lines 468–475. The package's [compatibility specification](../compatibility/compatibility.md) owns current native behavior.

| Injected fault, unexecuted | Required visible state | Fallback and outcome |
|---|---|---|
| EA09 hook disabled or timed out | Adapter health says disabled/failed; no “enforced” claim | Directly deliver applicable owners for the read-only answer; perform independent final check |
| EA14 unknown tool/event/payload schema | Coverage `unknown` or `unsupported`; preserve actual payload evidence | Use documented native permission boundary for restricted actions; do not parse a guessed schema or claim a hook blocked |
| EA10 wrong ranking skill selected | Body scope does not fit infrastructure comparison | Reject selection, open correct decision-support procedure/owners, then answer; extra invocation recorded as routing failure |
| EA15 Glob finds nothing | No content delivered | Open the actual source successfully or mark the affected claim unresolved; search alone cannot satisfy the read gate |
| EA19 source inaccessible | Exact attempted locator and access failure preserved | Continue independent work; bounded answer states what cannot be established; no fabricated absence claim |

This flow distinguishes a recovered useful answer from a perfect route: a wrong first skill remains a selection failure even if recovery succeeds. It also distinguishes advisory continuity from hard enforcement. A disabled hook cannot enforce a restricted operation, and direct prose does not become a substitute permission sandbox.

## 7. Narrow correction and preserved authority

**Actual source baseline:** `XML.hold_position` at `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml:22` requires treating narrow corrections narrowly; `XML.scope` at line 18 limits action. EM-11 at `apex-meta/informatics/final/specs/execution-modes/iterative-execution.md:50` requires changing only the architectural layer invalidated by evidence.

**Authored test prompt:** “Change only the label saying this was executed; it was illustrative. Keep the rest of the accepted design.” This is EA11. The case does not assert that a real operator has accepted this package; its fixture supplies the scoped prior decision.

The illustrative agent corrects the challenged label, checks references depending on that label, and preserves unrelated accepted choices. It does not reinterpret the correction as “abandon all hooks”, rewrite the entire design or expand its deployment authority. A verifier compares exact before/after deltas and separately checks whether any dependent claim still asserts execution.

For EA17, a retained handover says to push while the current task says read-only. The current task wins. For EA18, an archived candidate differs from current XML. The live owner wins within its scope; the historical candidate remains evidence. For EA20, a resumed child recommends installation. The parent retains the original review boundary. These are authority/recovery negatives, not an opportunity to add another confirmation loop to already authorized ordinary work.

## 8. Product-first pivot and authorized-sync boundary

EA21 supplies an explicitly synthetic fixture in which an optional routing helper has failed twice, while direct access to the authoritative files still works. The useful illustrative response is to stop repairing that helper, read the owners directly and finish the already-authorized architecture comparison. A third helper repair, replacement framework or repair report without the actual comparison fails the case. This tests `XML.product_first` and `XML.stop_repairing` together as consequential behavior rather than ID coverage: `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml:16,26–32,42–47`.

EA22 separately tests the positive `XML.sync` trigger in a **future, separately authorized disposable Git repository with a disposable local remote**. The operator fixture explicitly authorizes committing/pushing one prepared path and leaving unrelated files unchanged. The harness inspects the actual resulting local commit/tree/ref and unrelated hashes. Current explicit scope wins over conflicting general unrelated-file prose. Basis: `AGENTS.md:13–20`; `apex-meta/informatics/final/specs/execution-modes/git-sync.md:12–15`; retained T6 at `apex-meta/informatics/final/research/10-ultra-upgrade-validation/preregistration.md:56`. This case has not run, calls no external account, and supplies no authorization for the present research run to execute Git commands.

**Failure guard:** examples are review aids. No illustrative event, template, fixture prompt, successful recovery story or proposed case authorizes a live edit or supplies evidence that a host actually loaded or enforced the design.
