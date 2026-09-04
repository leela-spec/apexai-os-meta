---
type: ModuleDeepeningResult
title: A01 Target & Outcome Alignment
description: Evidence-backed deepening result for the universal <target> module.
status: DONE
updated: 2026-09-04
---

# A01 — Target & Outcome Alignment

## 1. Final decision

- **Module:** A01
- **XML tag:** `<target>`
- **Semantic purpose:** Keep agent work governed by the user's requested outcome rather than by an attractive proxy, adjacent improvement, or self-generated objective.
- **Selected deeper owner:** **No deeper artifact**
- **Established principles:** outcome orientation; stakeholder expectations; requirements traceability; success criteria.

### Final root XML

```xml
<target principles="outcome-orientation,requirements-traceability,success-criteria">
  Keep each material action traceable to the requested outcome and its stated success conditions. Do not substitute a plausible proxy or adjacent objective.
</target>
```

### Equivalent compact Markdown control

```markdown
**Target — outcome orientation / traceability:** Keep each material action traceable to the requested outcome and its stated success conditions. Do not substitute a plausible proxy or adjacent objective.
```

## 2. Why this is the right method

### Underlying discipline evidence

Systems engineering and requirements engineering provide the strongest established vocabulary for this behavior.

- NASA's Systems Engineering Handbook starts system design from stakeholder expectations, mission objectives, constraints, and criteria for mission success, and repeatedly validates the design against those expectations. It also calls complete requirements traceability critical to validation and warns that misunderstanding stakeholder requirements can produce the wrong solution.
- NASA's Stakeholder Expectations Definition guidance treats the desired end state and bounds on achievement as the foundation for later engineering work.
- NASA requirements guidance explicitly distinguishes building the **right product** (validation against user/stakeholder expectations) from merely building the product right.
- INCOSE's current Needs and Requirements Manual frames needs, requirements, verification, and validation as lifecycle-connected artifacts rather than isolated implementation instructions.
- Scrum's current Product Goal is a target against which work is planned, while Definition of Done is a separate commitment describing when an increment meets required quality. That separation is directly useful here: A01 should govern the target; A09 should govern completion proof.

The resulting invariant is therefore not merely "stay focused." It is **traceability from material work back to the requested outcome and stated success conditions**.

### Agent-delivery evidence

Current mature agent guidance converges on the same pattern.

- OpenAI model guidance recommends outcome-first prompts that define the expected outcome, success criteria, constraints, allowed side effects, evidence rules, and output shape, and advises explicit stopping conditions rather than over-prescribing process.
- OpenAI's Codex usage guidance recommends task prompts shaped like well-written issues and persistent `AGENTS.md` guidance for stable repository context.
- GitHub Copilot's coding-agent guidance says well-scoped tasks should include a clear problem/work description and complete acceptance criteria; GitHub also warns that vague prompts cause scope drift and unnecessary work, while clear stopping conditions prevent extra commits, unrelated refactors, and scope expansion.
- Anthropic's prompting guidance emphasizes clear, explicit desired outcomes and, for research tasks, explicit success criteria.
- `AGENTS.md` is explicitly designed as a persistent, concise carrier for agent context and instructions, supporting a small always-loaded invariant rather than a large procedure.

### Local inference / decision

The existing wording is close, but `definition-of-done` creates avoidable overlap with A09 `<verification>`. The target module should answer **"what outcome governs the work?"**; the verification module should answer **"how do we prove it is complete?"**.

The phrase **"material action"** avoids ceremonial tracing of trivial micro-steps. The phrase **"stated success conditions"** avoids inventing acceptance criteria that the operator never supplied. The explicit proxy/adjacent-objective prohibition targets the observed failure mode where an agent optimizes architecture, cleanup, safeguards, or an internally convenient substitute instead of the requested result.

## 3. Semantic contract

### MUST

- Treat the user's requested outcome as the governing objective for the task.
- Use any **stated** success conditions as part of that target contract.
- Keep each **material** action, recommendation, edit, or tool call reasonably traceable to advancing the requested outcome or satisfying a stated success condition.
- Prefer an action that advances the requested outcome over an action that merely improves a proxy metric or adjacent concern.
- Respect an explicit later user update as a target change or refinement; do not preserve an obsolete target merely for consistency.

### MUST NOT

- Substitute a plausible adjacent objective for the requested outcome.
- Turn an implementation preference, architecture preference, test metric, style preference, or internal convenience into the governing goal unless the user made it part of the target.
- Invent a formal requirements process, success metric, or Definition of Done for every simple task.
- Perform final completion verification here; that belongs to A09 `<verification>`.
- Resolve material ambiguity by guessing; A05 `<intent>` owns clarification/intent alignment when ambiguity would materially change the target.
- Expand or police non-goals here; A02 `<scope>` owns scope boundaries.

### Activation condition

Always active. Every task has an intended outcome, even when the task is small.

### Deepen condition

None. A01 does not need its own deeper artifact. When target ambiguity, scope conflict, trade-offs, or completion proof become material, the neighboring module that owns that problem should activate instead.

### Neighboring-module interactions

- **A02 `<scope>`:** A01 says what must be advanced; A02 says what must not be expanded into.
- **A05 `<intent>`:** A01 preserves the intended target; A05 resolves material ambiguity about what that target actually is.
- **A08 `<evidence>`:** evidence supports target-relevant claims but does not redefine the target.
- **A09 `<verification>`:** A01 keeps execution aimed at the outcome; A09 checks whether the actual deliverable satisfies the requested acceptance conditions.
- **A11 `<current_truth>`:** if the operator changes the target, current truth determines which instruction is authoritative.
- **C01 `<decision>`:** trade studies compare alternatives in service of the target; they must not replace the target with the scoring method itself.

### Common misinterpretations

- **"Traceability means a written matrix for every task."** No. The root rule requires behavioral traceability, not paperwork.
- **"Success conditions must always be generated."** No. Use stated conditions; do not manufacture ceremony for simple work.
- **"The first wording of the target is immutable."** No. Explicit later operator guidance can refine or replace it.
- **"Any quality improvement advances the target."** No. Quality work is relevant only when it materially contributes to the requested result or a governing constraint.

### Known failure modes

1. **Proxy optimization:** maximizing test count, documentation volume, architectural elegance, or safety scaffolding while the requested product remains unfinished.
2. **Adjacent-objective drift:** starting cleanup, redesign, migration, or infrastructure because it seems useful rather than because the target requires it.
3. **Process substitution:** following a plan or methodology as if completing the process were the outcome.
4. **Stale-target persistence:** continuing to optimize an earlier interpretation after the operator changes or clarifies the requested result.
5. **Over-formalization:** turning a trivial request into requirements-engineering ceremony.

## 4. Deep method

**No separate deep method or artifact is justified.** The behavior is an always-on invariant, not a reusable multi-step procedure.

A minimal observable execution test is sufficient when doubt arises:

1. State the requested outcome in one sentence from the user's current authoritative instruction.
2. For a proposed **material** action, identify which part of that outcome or which stated success condition it advances.
3. If no direct contribution can be identified, do not perform the action unless another governing module requires it (for example safety, authorization, or integrity).

This test is intentionally small. If step 1 cannot be done without a materially consequential guess, route to A05 `<intent>` rather than expanding A01 into an elicitation workflow.

## 5. Wording candidates considered

### Candidate A — current pilot

```xml
<target principles="outcome-orientation,definition-of-done">
  Deliver the requested outcome. Keep each action tied to the target and its success conditions.
</target>
```

**Strength:** concise and already directionally correct.  
**Weakness:** `definition-of-done` overlaps A09; "each action" can imply micro-ceremony; it does not explicitly block proxy-goal substitution.

### Candidate B — outcome + explicit anti-proxy rule — **selected**

```xml
<target principles="outcome-orientation,requirements-traceability,success-criteria">
  Keep each material action traceable to the requested outcome and its stated success conditions. Do not substitute a plausible proxy or adjacent objective.
</target>
```

**Strength:** directly operationalizes requirements traceability, blocks the principal failure mode, preserves small-task behavior, and separates target alignment from completion verification.

### Candidate C — immutable objective framing

```xml
<target principles="goal-integrity,success-criteria">
  Preserve the user's objective as the governing target until the user explicitly changes it; optimize only for its acceptance criteria.
</target>
```

**Rejected:** too rigid. "Acceptance criteria" may not exist, and "immutable until changed" encourages over-formalization and could conflict with legitimate discovery or clarification.

### Candidate D — formal stakeholder-expectation framing

```xml
<target principles="stakeholder-expectations,requirements-traceability">
  Translate the request into stakeholder expectations and trace all implementation work back to them.
</target>
```

**Rejected:** established but too process-heavy and software/systems-engineering flavored for a universal agent contract.

## 6. Scenario simulations

### S1 — simple / negative case

**Input:** "Rewrite this sentence to sound friendlier: ..."

- **Current pilot expected behavior:** rewrite directly; wording could theoretically encourage thinking about success conditions but usually remains lightweight.
- **Candidate expected behavior:** rewrite directly. The material action is the rewrite itself and is trivially traceable to the requested outcome.
- **Observable success:** one useful rewrite; no requirements checklist, plan, or extra target analysis.
- **Deep guidance:** no.
- **Rationale:** "material action" prevents micro-step ceremony.

**Result:** PASS.

### S2 — clear positive case

**Input:** "Add CSV export to the report screen. Success means the exported columns match the table and the existing filter is applied."

- **Current pilot expected behavior:** generally stays on target.
- **Candidate expected behavior:** implementation and tests remain traceable to CSV export, column parity, and filter application; unrelated report redesign is not treated as progress.
- **Observable success:** work product advances the requested export behavior; no proxy substitution such as a generic reporting refactor.
- **Deep guidance:** no.
- **Rationale:** stated success conditions become part of the target contract without requiring A09's final verification procedure yet.

**Result:** PASS.

### S3 — ambiguous case

**Input:** "Make the onboarding better."

- **Current pilot expected behavior:** may choose an interpretation of "better" and start optimizing it.
- **Candidate expected behavior:** recognizes that no reliable material-action traceability exists until the intended outcome is sufficiently understood; routes material ambiguity to A05 `<intent>` rather than inventing a proxy such as fewer screens or prettier UI.
- **Observable success:** no costly implementation is started against an invented objective when different interpretations would materially change the work.
- **Deep guidance:** A05 may activate; A01 itself does not deepen.
- **Rationale:** target integrity and intent elicitation are separate responsibilities.

**Result:** PASS.

### S4 — conflict / edge case

**Input:** "Implement the requested bug fix only. Do not refactor the surrounding subsystem, even though it is messy."

- **Current pilot expected behavior:** target wording helps, but `definition-of-done` does not add useful guidance.
- **Candidate expected behavior:** the fix remains the governing outcome; a subsystem refactor is not accepted as a proxy for solving the bug. A02 `<scope>` independently reinforces the explicit non-goal.
- **Observable success:** bug fixed without unrelated refactor unless it is demonstrably necessary to the fix.
- **Deep guidance:** no A01 deepening; A02 handles scope if needed.
- **Rationale:** neighboring modules reinforce rather than duplicate each other.

**Result:** PASS.

### S5 — known failure case: evaluation becomes invention

**Input:** "Evaluate whether our current pipeline is the right design. Do not build anything yet."

- **Current pilot expected behavior:** "deliver requested outcome" is helpful but does not explicitly reject a plausible substitute such as implementing a replacement to demonstrate an idea.
- **Candidate expected behavior:** building a new pipeline fails the traceability test because the requested outcome is an evaluation, not a replacement implementation.
- **Observable success:** produces an evidence-based evaluation/recommendation and performs no implementation.
- **Deep guidance:** C02 `<research>` or C01 `<decision>` may activate; A01 does not deepen.
- **Rationale:** explicit proxy/adjacent-objective language directly targets this recurrent drift mode.

**Result:** PASS.

### S6 — XML vs compact Markdown control

**Input:** "Review this patch only for the stated bug."

- **XML candidate:** expected to keep review findings tied to the stated bug and avoid converting the task into a broad code-quality audit.
- **Markdown control:** same expected behavior.
- **Observable success:** no material behavioral difference attributable to representation; both preserve the same semantic invariant.
- **Deep guidance:** no.
- **Rationale:** A01 does not depend on XML parsing; XML remains a compact structuring convention only.

**Result:** equivalent semantics expected; representation requires later cross-agent empirical evaluation, not assumption.

## 7. Alternatives rejected

| Alternative | Why it lost |
|---|---|
| Keep `definition-of-done` inside A01 | Duplicates A09 completion/verification semantics and blurs target vs proof-of-completion. |
| "Stay focused on the goal" only | Too vague; does not tell the agent how to detect proxy optimization or adjacent-objective drift. |
| Full SMART-goal conversion | Useful in some planning domains but too ceremonial and not universally valid; it also encourages invented metrics when the user supplied none. |
| Formal requirements decomposition for every task | Strong discipline for complex engineering, but excessive as an always-on agent rule. |
| Immutable objective record | Risks stale-target persistence and unnecessary process; the operator must be able to refine the target naturally. |
| Agent Skill for target alignment | No reusable multi-step method exists that adds enough value beyond the compact invariant; a Skill would add routing and context cost without a distinct procedure. |
| Focused reference | Definitions and boundary examples fit in this module result; runtime reference loading would add no execution value. |
| Scoped rule | Target alignment is universal, not path- or subsystem-specific. |

## 8. Sources

Primary/authoritative sources used, checked 2026-09-04:

1. **NASA Systems Engineering Handbook — System Design Processes** — stakeholder expectations, mission objectives, success criteria, requirements traceability, iterative validation against stakeholder expectations.  
   https://www.nasa.gov/reference/4-0-system-design-processes/
2. **NASA Systems Engineering Handbook — Stakeholder Expectations Definition** — desired end state, bounds, and shared understanding as the foundation for engineering work.  
   https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/
3. **NASA SWE-055 Requirements Validation** — validation as ensuring the right product is built for users/stakeholders.  
   https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation
4. **INCOSE Needs and Requirements Manual v2** — current lifecycle framing of needs, requirements, verification, and validation; v2 published December 2024.  
   https://portal.incose.org/ItemDetail?Category=EBOOKS&WebsiteKey=d4c31fa4-467a-4959-b48b-cae3ea93e516&iProductCode=NRM2
5. **Scrum Guide 2020 (current official version)** — Product Goal as target; Definition of Done as a distinct commitment.  
   https://scrumguides.org/scrum-guide.html
6. **OpenAI model guidance — outcome-first prompts and stopping conditions** — expected outcome, success criteria, constraints, and explicit stopping conditions.  
   https://developers.openai.com/api/docs/guides/latest-model
7. **OpenAI — How OpenAI uses Codex** — issue-shaped task descriptions and persistent AGENTS.md context.  
   https://openai.com/business/guides-and-resources/how-openai-uses-codex/
8. **GitHub Copilot coding agent best practices** — clear, well-scoped tasks and complete acceptance criteria.  
   https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks
9. **GitHub — Optimize AI usage** — vague prompts cause scope drift; clear expected outcomes and stopping conditions reduce unnecessary work.  
   https://docs.github.com/en/copilot/tutorials/optimize-ai-usage
10. **GitHub Copilot custom-instruction guidance** — always-loaded instructions should be short, self-contained, and broadly applicable.  
    https://docs.github.com/en/copilot/concepts/prompting/response-customization
11. **Anthropic prompting best practices** — clear, explicit desired outputs and success criteria.  
    https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
12. **AGENTS.md specification** — dedicated persistent context/instructions carrier for coding agents.  
    https://agents.md/

## 9. Evidence confidence and open uncertainty

- **High confidence:** target/outcome alignment is best grounded in stakeholder expectations, outcome-first tasking, success criteria, and traceability rather than in a bespoke prompt concept.
- **High confidence:** `definition-of-done` should move out of A01 semantically and remain owned by A09; this run does not edit A09.
- **High confidence:** a separate Skill/reference would be unnecessary overhead for A01.
- **Moderate confidence:** XML and compact Markdown will behave equivalently for this module. The scenario indicates semantic equivalence, but the program's later cross-agent evaluation must test representation empirically.
