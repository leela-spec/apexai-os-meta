---
type: ModuleDeepeningResult
title: A01 Intent-Preserving Target Realization & Validation
description: Evidence-backed deepening result for the universal <target> module, including the formerly separate A09 completion-validation responsibility.
status: DONE
updated: 2026-09-04
---

# A01 — Intent-Preserving Target Realization & Validation

## 1. Final decision

- **Module:** A01
- **XML tag:** `<target>`
- **Semantic purpose:** Realize the substantive intended outcome at an appropriate level of depth, rigor, completeness, and effort; prevent proxy completion signals from replacing the actual target; validate the delivered result against that intent before reporting completion.
- **Merged module:** former A09 `<verification>` — Acceptance & Completion Verification.
- **Selected deeper owner:** **No deeper artifact**
- **Established principles:** outcome orientation; stakeholder intent; requirements traceability; validation vs verification; anti-proxy optimization; proportional rigor; success criteria.

### Final root XML

```xml
<target principles="intent-preservation,outcome-orientation,validation,anti-proxy-optimization,proportional-rigor">
  Realize and validate the substantive intended outcome. Treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes for it; use the depth, rigor, completeness, and effort the outcome actually requires.
</target>
```

### Equivalent compact Markdown control

```markdown
**Target — intent-preserving realization & validation:** Realize and validate the substantive intended outcome. Treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes for it; use the depth, rigor, completeness, and effort the outcome actually requires.
```

## 2. Why A01 and A09 are now one module

The previous split treated A01 as target alignment during execution and A09 as completion verification at the end. That separation was tidy but missed the operator's primary failure mode: an agent can remain superficially traceable to a task and pass its mechanical checks while still failing the requested capability or useful result.

Example failure:

```text
requested capability
  -> create a useful reusable Skill

agent proxy
  -> create SKILL.md
  -> satisfy frontmatter/test/checkmark
  -> report success

actual result
  -> semantically trivial file that does not realize the requested capability
```

The governing loop is therefore one continuous responsibility:

```text
intended useful outcome
  -> choose work that realizes it
  -> apply proportionate depth / rigor / completeness
  -> use tests, files, schemas, metrics, and checks as evidence
  -> validate the actual result against the intended outcome
```

A separate universal A09 adds wording and token cost while encouraging the wrong conceptual split between target and completion. Its useful semantics are now absorbed into A01.

## 3. Established grounding

Systems engineering and requirements engineering provide the strongest vocabulary for the merged behavior.

- NASA systems engineering starts from stakeholder expectations, mission objectives, constraints, and criteria for success, then validates realized products against those expectations.
- NASA requirements guidance distinguishes **verification** (building the product right) from **validation** (building the right product for the stakeholder need).
- INCOSE connects needs, requirements, verification, and validation across the lifecycle rather than treating acceptance as an isolated final checkbox.
- Scrum distinguishes the Product Goal from Definition of Done, which is useful evidence that mechanical completion criteria are not themselves the product objective.
- Current agent guidance from OpenAI, GitHub, and Anthropic consistently benefits from explicit outcomes, success criteria, constraints, stopping conditions, and clear expected results.

The added operator correction is important: these completion signals must remain **evidence subordinate to the intended useful outcome**, not optimization targets in their own right.

## 4. Semantic contract

### MUST

- Treat the user's substantive intended outcome as the governing objective.
- Realize the requested capability/result, not merely produce the named artifact or pass the named check.
- Keep material work traceable to the intended outcome and any stated success conditions.
- Scale depth, rigor, completeness, computation, and effort to the value, complexity, and consequences of the target.
- Use tests, files, schemas, metrics, checklists, acceptance criteria, and receipts as evidence about success where relevant.
- Before reporting completion, validate that the actual deliverable substantively satisfies the intended outcome, not only its mechanical proxies.
- Respect later explicit operator clarification as a refinement or replacement of the target.

### MUST NOT

- Substitute a plausible adjacent objective, proxy metric, test result, file existence, schema validity, or checklist state for the requested useful outcome.
- Treat passing automated checks as sufficient proof when the requested capability or substantive content is still inadequate.
- Under-deliver a complex/high-value target because a superficial completion signal is easy to satisfy.
- Over-engineer a simple target merely to demonstrate rigor.
- Invent formal acceptance criteria or a requirements process when the user did not need them.
- Resolve material ambiguity by guessing; A05 `<intent>` owns clarification when ambiguity would materially change the target.
- Expand into non-goals; A02 `<scope>` owns scope boundaries.

### Activation condition

Always active. Every task has an intended useful outcome, even when small.

### Deepen condition

None. This is an always-on invariant rather than a reusable procedure. Other modules deepen only when their distinct trigger applies.

### Neighboring-module interactions

- **A02 `<scope>`:** bounds what work may be added while A01 governs what useful result must be realized.
- **A05 `<intent>`:** resolves material uncertainty about what the intended outcome actually is.
- **A07 `<realization>`:** supplies hierarchical decomposition and bottom-up V&V for work with dependent system/module/implementation levels.
- **A08 `<evidence>`:** governs source authority, provenance, freshness, and uncertainty for claims; evidence does not redefine the target.
- **A11 `<current_truth>`:** determines the authoritative target when later instructions supersede earlier ones.
- **C01 `<decision>`:** compares alternatives in service of the target rather than allowing the scoring method to become the goal.

## 5. Failure modes this module exists to prevent

1. **Proxy completion:** file exists, checkbox is marked, test passes, schema validates — but the useful requested capability is absent.
2. **Specification gaming:** the agent satisfies the literal measurable condition while defeating the intended purpose.
3. **Adjacent-objective drift:** architecture, cleanup, safeguards, redesign, or documentation become the work because they are easier to optimize than the requested result.
4. **Process substitution:** completing the prescribed workflow is mistaken for completing the target.
5. **Under-realization:** content or implementation is technically present but too shallow to serve its intended use.
6. **Over-realization:** a simple request receives disproportionate analysis, infrastructure, or ceremony.
7. **Mechanical validation fallacy:** automated verification is treated as sufficient evidence that the right outcome was produced.
8. **Stale-target persistence:** work continues against an obsolete interpretation after the operator clarifies the target.

## 6. Minimal observable execution test

When substantive adequacy is in doubt:

1. State the intended useful outcome from the current authoritative instruction.
2. Ask whether the proposed material work directly helps realize that outcome or a governing constraint.
3. Judge whether the planned depth, rigor, completeness, and effort are proportionate to the target.
4. Treat mechanical checks as evidence, not as the target.
5. Before reporting completion, inspect the actual deliverable and ask whether it substantively realizes the intended outcome.

If step 1 requires a materially consequential guess, route to A05 `<intent>` rather than expanding this module into an elicitation workflow.

## 7. Wording decision

### Previous A01

```xml
<target principles="outcome-orientation,requirements-traceability,success-criteria">
  Keep each material action traceable to the requested outcome and its stated success conditions. Do not substitute a plausible proxy or adjacent objective.
</target>
```

**Problem:** useful anti-drift behavior, but insufficient against superficial realization. A two-line placeholder artifact can still be "traceable" to a request to create the artifact.

### Previous A09

```xml
<verification principles="acceptance-criteria,definition-of-done">
  Verify the actual deliverable against the requested acceptance conditions before reporting completion.
</verification>
```

**Problem:** useful final check, but acceptance conditions can themselves be incomplete proxies. Keeping it separate also costs another universal module and reinforces a false target-vs-validation separation.

### Merged candidate — selected

```xml
<target principles="intent-preservation,outcome-orientation,validation,anti-proxy-optimization,proportional-rigor">
  Realize and validate the substantive intended outcome. Treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes for it; use the depth, rigor, completeness, and effort the outcome actually requires.
</target>
```

**Why it wins:** it covers target orientation, substantive realization, proportional adequacy, anti-proxy behavior, and final validation in one compact always-loaded invariant.

## 8. Scenario simulations

### S1 — simple / negative case

**Input:** "Rewrite this sentence to sound friendlier."

Expected behavior: rewrite directly. No requirements ceremony, extra testing, or deep analysis. The requested useful outcome is obvious and low-risk.

**Result:** PASS.

### S2 — clear positive case

**Input:** "Create a reusable Skill that teaches an agent how to perform X."

Bad proxy behavior: create a syntactically valid `SKILL.md` containing a token description and stop because the file exists.

Merged A01 behavior: produce enough substantive instruction, structure, triggers, method, and examples/evidence as required for the Skill to actually teach the requested capability; syntax checks are evidence, not the target.

**Result:** PASS.

### S3 — test/checkmark gaming

**Input:** "Implement the feature; the Python test must pass."

Bad proxy behavior: alter or narrowly satisfy the test without realizing the user-facing behavior.

Merged A01 behavior: implement the intended feature, use the test as evidence, and validate the actual behavior before completion.

**Result:** PASS.

### S4 — ambiguous target

**Input:** "Make onboarding better."

Expected behavior: do not invent a proxy such as fewer screens or prettier UI. Route material ambiguity to A05 before costly execution.

**Result:** PASS.

### S5 — complexity proportionality

**Input A:** "Correct this typo."  
Expected: one small edit; no architecture review.

**Input B:** "Design the canonical authorization layer used by multiple agent runtimes."  
Expected: materially more research, comparison, rigor, validation, and evidence because superficial implementation would not realize the target.

**Result:** PASS.

### S6 — known project failure

**Input:** "Evaluate whether our current pipeline is the right design. Do not build anything yet."

Bad proxy behavior: build a replacement or produce validation receipts that do not answer whether the pipeline is the right design.

Merged A01 behavior: the useful outcome is an evidence-based evaluation and recommendation; implementation is not progress toward that target unless explicitly authorized.

**Result:** PASS.

### S7 — XML vs Markdown control

Equivalent compact Markdown is expected to preserve the same semantics. XML remains a structuring convention, not parser authority. Representation still requires later cross-agent empirical evaluation.

**Result:** semantically equivalent by inspection; empirical representation test remains later program work.

## 9. Deepening-owner decision

**No separate Skill, reference, or scoped rule.**

Reason:

- the merged behavior is universal and always active;
- its core method fits in one compact invariant plus the neighboring module boundaries;
- a deeper runtime artifact would add routing/context cost without a distinct reusable procedure;
- complex hierarchical realization remains owned by A07 rather than being duplicated here.

## 10. Program-level consequence

- A09 `<verification>` is removed from the universal module set.
- Its substantive completion-validation responsibility is now part of A01 `<target>`.
- Mechanical verification remains available wherever task-specific tests/checks are relevant and through A07/A08 as appropriate, but it is subordinate to substantive validation of the requested outcome.
- The module set becomes smaller without removing the capability A09 was meant to protect.

## 11. Sources

Primary/authoritative sources used in the original A01 research, checked 2026-09-04:

1. NASA Systems Engineering Handbook — System Design Processes  
   https://www.nasa.gov/reference/4-0-system-design-processes/
2. NASA Systems Engineering Handbook — Stakeholder Expectations Definition  
   https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/
3. NASA SWE-055 Requirements Validation  
   https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation
4. INCOSE Needs and Requirements Manual v2  
   https://portal.incose.org/ItemDetail?Category=EBOOKS&WebsiteKey=d4c31fa4-467a-4959-b48b-cae3ea93e516&iProductCode=NRM2
5. Scrum Guide 2020  
   https://scrumguides.org/scrum-guide.html
6. OpenAI model guidance — outcome-first prompts and stopping conditions  
   https://developers.openai.com/api/docs/guides/latest-model
7. OpenAI — How OpenAI uses Codex  
   https://openai.com/business/guides-and-resources/how-openai-uses-codex/
8. GitHub Copilot coding agent best practices  
   https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks
9. GitHub — Optimize AI usage  
   https://docs.github.com/en/copilot/tutorials/optimize-ai-usage
10. GitHub Copilot custom-instruction guidance  
    https://docs.github.com/en/copilot/concepts/prompting/response-customization
11. Anthropic prompting best practices  
    https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
12. AGENTS.md specification  
    https://agents.md/

## 12. Evidence confidence and open uncertainty

- **High confidence:** the operator-identified failure is not adequately controlled by traceability plus a separate acceptance-check module; anti-proxy substantive realization must be explicit.
- **High confidence:** validation belongs in the same governing loop as target realization for this compact universal contract.
- **High confidence:** removing standalone A09 reduces always-loaded complexity without losing its useful semantics.
- **Moderate confidence:** the exact final wording is compact enough while preserving all five concepts; later cross-agent evaluation should test whether `proportional-rigor` and the anti-proxy examples produce the intended behavior without over-analysis.