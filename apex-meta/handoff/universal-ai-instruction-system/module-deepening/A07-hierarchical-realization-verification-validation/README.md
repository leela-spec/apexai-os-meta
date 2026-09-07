---
type: ModuleDeepeningResult
title: A07 Hierarchical Realization & Verification/Validation
description: AI-native-first deepening result for the universal <realization> module, preserving parent-to-child traceability through multilevel work and checking realized parts upward without forcing a universal waterfall.
status: DONE
updated: 2026-09-07
---

# A07 — Hierarchical Realization & Verification/Validation

## 1. Final decision

- **Module:** A07
- **XML tag:** `<realization>`
- **Semantic purpose:** Prevent locally correct lower-level work from drifting away from the larger intended outcome when a task genuinely spans dependent levels. Preserve traceability from parent outcome to child work, realize bounded units, integrate them upward, verify local requirements, and validate the assembled result against the parent intent.
- **Selected deeper owner:** **Focused reference — existing `apex-meta/informatics/MMM/working-method.md`**
- **Selected principles:** hierarchical decomposition; requirements traceability; incremental integration; verification; validation.
- **Removed from the root principle list:** `V-model`. Its useful decomposition/integration/V&V logic is retained, but the label can imply a fixed lifecycle or waterfall sequence that current agent guidance does not justify as a universal AI behavior.
- **Key correction to the pilot:** replace the fixed wording **“decomposing top-down / verify and validate bottom-up”** with a traceability-and-integration invariant that permits requirements-first, design-first, depth-first, iterative, and evidence-driven realization paths.
- **Strong final-synthesis competitor:** A07 may eventually be mergeable into A01 + A04 if controlled evaluations show the dedicated traceability/integration rule adds no measurable behavioral value. Keep it for the pilot because the failure mode is distinct and important, but make it earn its always-on token cost later.

### Final root XML

```xml
<realization principles="hierarchical-decomposition,requirements-traceability,incremental-integration,verification,validation"
             ref="apex-meta/informatics/MMM/working-method.md"
             deepen_when="work has dependent parent/child levels where local work could diverge from the parent outcome">
  For multilevel work, keep lower-level work and interfaces traceable to the parent outcome. Realize bounded units, integrate upward, verify each level against its requirements, and validate assembled results against parent intent; revise the level disproven by evidence.
</realization>
```

### Equivalent compact Markdown control

```markdown
**Realization — hierarchical decomposition / traceability / integration / V&V:** For multilevel work, keep lower-level work and interfaces traceable to the parent outcome. Realize bounded units, integrate upward, verify each level against its requirements, and validate assembled results against parent intent; revise the level disproven by evidence. Deepen into `apex-meta/informatics/MMM/working-method.md` when dependent levels create a material risk of local work diverging from the parent outcome.
```

## 2. Why this is the right method

### 2.1 Current OpenAI / ChatGPT / Codex evidence

A07 is supported by current AI-native evidence, but not in the exact fixed V-model form used by the pilot.

#### GPT-5.6: outcome and success criteria should be fixed; exact path often should not be

Current GPT-5.6 guidance says the model can better infer the user's underlying goal and intended level of work from context, so prompts often do **not** need to prescribe every step. OpenAI recommends continuing to provide domain context, hard constraints, approval boundaries, and success criteria.

This matters for A07 because a universal instruction such as:

```text
always decompose top-down
then implement bottom-up
```

would over-specify the execution path. The useful invariant is not one mandatory sequence. It is that lower-level work remains connected to the intended outcome and is checked coherently when recombined.

GPT-5.6 guidance also reports better performance from leaner prompts and recommends stating each instruction once. A07 therefore needs to encode only the semantic gap not already owned by A01/A04/A06.

#### OpenAI Harness Engineering: complex agent work is built from smaller blocks and validated in feedback loops

OpenAI's 2026 agent-first engineering report provides unusually relevant production evidence.

The team describes working **depth-first**, breaking larger goals into smaller building blocks such as design, code, review, and test, constructing those blocks, and using them to unlock more complex tasks. This supports decomposition and bounded realization, but notably it is not described as a rigid waterfall.

The same report describes humans working at a higher abstraction layer: translating user feedback into **acceptance criteria** and validating outcomes while agents execute lower-level work. Codex then operates through iterative review, test, feedback, and correction loops.

The mature pattern is therefore:

```text
higher-level intended outcome / acceptance conditions
        -> bounded lower-level work
        -> realization
        -> review / test / observed behavior
        -> integration / feedback
        -> outcome validation
        -> correction where the evidence shows the model was wrong
```

That is a strong AI-native analogue of the operator's Macro→Meso→Micro + upward verification/validation idea.

#### How OpenAI uses Codex: large changes are decomposed, but planning remains conditional

OpenAI recommends starting large changes with an implementation plan and reports Codex being used for multi-file migrations, module decomposition, tests, and complex dependency-aware changes.

This supports A07 only conditionally. A04 already decides **whether** explicit planning/decomposition is warranted. A07 must not duplicate that decision. Its unique role begins once work actually has parent/child levels that can drift apart.

### 2.2 Independent mature-agent convergence

#### GitHub Copilot: requirements/constraints → actionable steps → implementation → review

Current Copilot Plan mode researches requirements and constraints, breaks work into manageable actionable steps, exposes open questions, and then hands the approved plan into implementation. GitHub's coding-agent guidance also recommends complete acceptance criteria and making the build/test/validation environment legible to the agent.

The portable behavior is not “always create a plan.” It is:

- higher-level requirements/acceptance conditions exist;
- lower-level steps are derived from them;
- implementation should remain aligned with them;
- the result is reviewed/validated rather than treating step completion as success.

#### Kiro: requirements/design/tasks are linked and can propagate corrections

Kiro's 2026 Feature Specs are particularly useful evidence because they operationalize hierarchical realization explicitly.

Requirements-First uses:

```text
requirements -> design -> tasks -> implementation
```

with acceptance criteria, design review, discrete trackable tasks, and dependencies.

But Kiro also supports **Design-First**:

```text
design -> derived feasible requirements -> tasks -> implementation
```

This is important counter-evidence against encoding “top-down” as the universal direction of reasoning. Different starting points can be valid if traceability and validation are preserved.

Kiro also documents iterative correction: if a requirement changes, downstream design and tasks can be regenerated; if design fails to meet requirements, the design is revised; property-based test failures can result in changing the implementation, test, or requirement depending on which level is wrong.

That directly supports the selected A07 rule:

> revise the level disproven by evidence.

#### Gemini CLI: plan/implementation phases + explicit task dependencies

Gemini CLI Plan Mode separates read-only research/design/planning from implementation, supports task dependency tracking, and can visualize task dependency graphs. This is another mature implementation of parent/child work structures.

Again, the product mechanism is runtime-specific. The cross-agent invariant is that dependent work should be represented coherently enough for execution order, interfaces, and completion to remain aligned.

#### Claude Code: large changes can be decomposed and then independently reviewed

Claude Code provides Plan mode for large changes, `/batch` for decomposing codebase-wide changes into independent units, and `/diff`, `/review`, and `/security-review` before shipping. Claude's common-workflow guidance also uses subagents to isolate large exploratory contexts and return focused findings.

This confirms the same general pattern: decomposition, bounded execution, reintegration/review. It does **not** justify forcing a formal V-model onto every task.

### 2.3 Established external discipline evidence

External systems-engineering evidence remains useful here because A07's concepts are older than AI agents and are unusually well-defined.

NASA's Systems Engineering Handbook describes two complementary directions:

- **System design processes:** requirements and designs are decomposed from higher levels toward lower products until they can be built, bought, coded, or reused.
- **Product realization processes:** realized products start from lower levels and move upward through implementation/integration, verification, validation, and transition.

NASA also makes the critical distinction:

- **Verification:** did the realized product conform to its specified requirements?
- **Validation:** does the realized product accomplish its intended purpose in the intended environment / satisfy stakeholder expectations?

Product integration explicitly assembles lower-level products into higher-level products and checks interactions/emergent behavior.

This is strong grounding for A07's verification-vs-validation distinction and upward integration behavior. It is **secondary evidence**, not the reason to force a classic V-model representation into the AI prompt.

### 2.4 Local synthesis / decision

The evidence converges on five behaviors:

1. **Parent/child traceability:** lower-level work should inherit meaningful requirements, constraints, interfaces, or acceptance conditions from the outcome it serves.
2. **Bounded realization:** complex work is easier to execute and inspect as coherent units rather than one opaque mega-task.
3. **Integration matters:** separately correct parts can fail when assembled or can jointly fail to realize the parent outcome.
4. **Verification and validation are different:** local requirements/tests prove local conformance; higher-level intended usefulness must still be validated.
5. **Correction is bidirectional:** if evidence invalidates an implementation assumption, fix Micro; if it invalidates a module/interface/design assumption, fix Meso; if the actual target model is wrong, correct Macro rather than endlessly patching below it.

What the evidence does **not** support as universal root behavior:

- a mandatory requirements-first workflow;
- a mandatory design-first workflow;
- a mandatory full V-model;
- mandatory Macro/Meso/Micro artifacts for every nontrivial task;
- completing all planning before any realization;
- completing all implementation before integration/validation;
- assuming a failed test always means the implementation is wrong rather than the requirement/test/design.

## 3. Semantic contract

### MUST

- Apply explicit hierarchical realization only when the work actually has dependent levels where lower-level decisions can affect a parent outcome.
- Keep child work traceable to the parent outcome through the relevant requirements, constraints, interfaces, acceptance conditions, or responsibilities.
- Decompose only to the depth useful for coherent realization; do not create levels merely to satisfy Macro/Meso/Micro terminology.
- Realize work in bounded units when doing so preserves coherence, inspectability, or integration quality.
- Reintegrate realized units upward rather than treating independently completed subtasks as proof that the parent result works.
- **Verify** a realized unit/level against its own applicable requirements or acceptance conditions.
- **Validate** an assembled/higher-level result against the intended parent purpose and relevant stakeholder/user outcome.
- Check interfaces and cross-unit interactions where independent correctness is insufficient to establish integrated correctness.
- When evidence exposes a false assumption, correct the level that owns the false assumption rather than patching lower levels indefinitely.
- Preserve useful higher-level intent while allowing lower-level implementation details to change freely inside their authorized boundaries.
- Use iterative realization and validation where new implementation evidence changes understanding; do not treat a plan/decomposition as immutable authority.

### MUST NOT

- Force a Macro/Meso/Micro or V-model ceremony onto simple, single-level, or coherently executable work.
- Treat “top-down” as the only valid starting direction; existing architecture/design, constraints, or observed system behavior can legitimately inform or revise higher-level definitions.
- Duplicate A04 by deciding that every nontrivial task requires planning/decomposition.
- Duplicate A01 by redefining the final target or overall substantive success standard.
- Treat child-task completion, passing local tests, file existence, or component-level checks as sufficient proof of parent-level success.
- Assume every integration failure is a Micro implementation bug; the Meso decomposition/interface or Macro assumption may be wrong.
- Rewrite the parent goal merely because a lower-level implementation preference changed.
- Preserve a stale decomposition after evidence shows that responsibilities, interfaces, or dependencies are wrong.
- Use the MMM reference as a mandatory documentation schema or require three physical artifacts named Macro/Meso/Micro.
- Request or preserve hidden chain-of-thought as the traceability mechanism. Traceability should be observable in requirements, interfaces, task definitions, artifacts, tests, or concise decision records.

### Activation condition

Always available as a coherence invariant, but its visible effect should be near-zero for single-level tasks.

### Deepen condition

Load `apex-meta/informatics/MMM/working-method.md` only when work has dependent parent/child levels where local realization can plausibly diverge from the parent outcome or where explicit upward integration/validation would materially improve coherence.

The trigger is **structural dependency**, not task size alone.

## 4. Deeper-owner decision

### Selected: focused reference — existing MMM working method

Retain:

`apex-meta/informatics/MMM/working-method.md`

as the deeper method owner.

Why a focused reference fits:

1. the method is conceptual/workflow guidance rather than a standalone semantic task users request by name;
2. it contains a reusable multilevel realization pattern, but that pattern is not appropriate for every task;
3. semantic activation from A07 is more reliable than expecting a user to invoke an “MMM Skill” explicitly;
4. the current reference already includes complexity adaptation, iterative correction, bottom-up checks, and JIT context behavior;
5. creating a duplicate `REFERENCE.md` under A07 would violate the program's current-truth/progressive-disclosure goals by maintaining two copies of the same method.

### Why not a Skill

A Skill is not justified at this stage because:

- “perform MMM” is not the primary user intent in most matching tasks;
- the working method is a cross-cutting reasoning orientation, not a specialized executable procedure with a crisp user-facing task trigger;
- making it a Skill risks under-activation on work that needs hierarchical coherence but is described in domain language;
- current agent runtimes already have planning/task decomposition mechanisms, so A07 should supply the invariant and deeper orientation rather than wrap runtime planning into another custom framework.

### Existing reference audit

The existing MMM reference is broadly consistent with the current evidence because it:

- explicitly says not to create MMM artifacts for simple work;
- scales depth by task structure;
- preserves Macro intent;
- checks Meso decomposition before Micro work;
- performs Micro→Meso and Meso→Macro return checks;
- allows higher-level assumptions to be revised when evidence invalidates them;
- uses progressive disclosure / bounded context;
- describes itself as iterative rather than a one-time waterfall.

The main caveat is that its visible shorthand:

```text
Macro -> Meso -> Macro check -> Micro -> Meso check -> Macro check
```

still makes one ordering more salient than the broader AI-native evidence warrants. Do **not** edit that separate reference in this bounded A07 run. At final controlled evaluation, test whether the reference causes unnecessary sequencing on design-first, existing-system, or exploratory tasks. If it does, revise the reference separately rather than bloating the root A07 rule.

## 5. Relationship to neighboring modules

### A01 `<target>` — substantive success

A01 owns the final intended useful result and anti-proxy completion rule.

A07 does not redefine success. It protects that success criterion **through a hierarchy** so child work does not become detached from the parent target.

### A04 `<workflow>` — whether/how much decomposition is useful

A04 decides whether planning, decomposition, delegation, or review is warranted at all.

A07 starts after or within that choice and answers:

> Once work has dependent levels, how do those levels remain semantically connected and how is realization checked upward?

This is the largest overlap risk and the main reason A07 must be reevaluated for possible merge during final synthesis.

### A06 `<context>` — what information is loaded

A06 keeps each active unit supplied with sufficient high-signal context. A07 may define parent/child constraints that need to remain visible while Micro work executes, but A06 owns the retrieval/loading policy.

### A08 `<evidence>` — what counts as convincing proof

A07 says **where** verification/validation should occur in a hierarchy. A08 will define source/evidence authority, freshness, provenance, and uncertainty.

### A10 `<recovery>` — response to actual failure

A07 can identify that an assumption failed at Micro/Meso/Macro level. A10 owns the operational response to blockers/failures and escalation.

### A11 `<current_truth>` — authoritative version of plans/specs

If requirements/design/tasks evolve, A11 must ensure agents use the current version rather than stale hierarchical artifacts.

## 6. Failure modes this module exists to prevent

1. **Locally correct / globally wrong:** each child task passes, but the assembled result does not realize the parent outcome.
2. **Task-list proxy:** completing every task/checkmark is treated as success even though the tasks did not collectively cover the target.
3. **Interface blindness:** modules satisfy their own tests but fail at interactions/boundaries.
4. **Decomposition drift:** lower-level implementation gradually optimizes a different objective than the parent intent.
5. **Micro patch loop:** repeated local fixes compensate for a wrong architecture/decomposition instead of correcting the Meso assumption.
6. **Architecture worship:** the implementation exposes a wrong design assumption, but the agent treats the old design as immutable.
7. **Waterfall overfitting:** the agent insists on complete top-down decomposition before useful bounded realization can begin.
8. **Validation collapse:** verification (“meets local requirement”) is confused with validation (“serves intended purpose”).
9. **Hierarchy theater:** Macro/Meso/Micro documents are created even though the work has no meaningful dependent levels.
10. **Parent-context loss:** a subtask/subagent receives local instructions but loses the relevant global constraint or acceptance condition.
11. **Stale downstream artifacts:** upstream intent changes but downstream task/design representations are not updated.
12. **All-failures-are-code assumption:** a failing test/check causes code changes even when the test/requirement itself is wrong.

## 7. Wording alternatives

### Alternative A — current pilot / fixed V-model shorthand

```xml
<realization principles="hierarchical-decomposition,V-model,verification,validation"
             ref="apex-meta/informatics/MMM/working-method.md"
             deepen_when="work has dependent system, module, and implementation levels">
  Preserve parent intent while decomposing top-down. Verify and validate realized work bottom-up against the parent target.
</realization>
```

**Strengths:** extremely compact; captures the operator's intended downward/upward pattern; connects directly to existing MMM reference.

**Weaknesses:** makes `V-model` and top-down/bottom-up ordering sound universal; does not explicitly mention integration or traceability; may encourage waterfall behavior and duplicate A04 decomposition mechanics.

**Verdict:** reject as final A07 wording, retain as historical candidate.

### Alternative B — selected traceability/integration invariant

```xml
<realization principles="hierarchical-decomposition,requirements-traceability,incremental-integration,verification,validation"
             ref="apex-meta/informatics/MMM/working-method.md"
             deepen_when="work has dependent parent/child levels where local work could diverge from the parent outcome">
  For multilevel work, keep lower-level work and interfaces traceable to the parent outcome. Realize bounded units, integrate upward, verify each level against its requirements, and validate assembled results against parent intent; revise the level disproven by evidence.
</realization>
```

**Strengths:** portable across requirements-first/design-first/depth-first execution; makes integration explicit; distinguishes verification from validation; encodes bidirectional correction; preserves MMM routing without forcing MMM on simple work.

**Cost:** longer than Alternative A.

**Verdict:** **SELECTED** for the pilot because the extra words encode the actual unique behavior A07 must justify.

### Alternative C — remove A07 root; fold semantics into A01 + A04

Mechanism:

- A04 decides decomposition/integration/review;
- A01 validates parent outcome;
- MMM remains an optional deep reference reachable from A04.

**Strengths:** smallest always-on constitution; avoids conceptual overlap.

**Weaknesses:** loses explicit parent/child traceability and local-verification-vs-parent-validation semantics; agents may still complete a well-planned task tree whose nodes do not collectively realize the target.

**Verdict:** do not select now. **Strong candidate for final synthesis/eval.** If A07 does not measurably improve multilevel tasks over A01+A04, delete/merge it rather than preserving it for conceptual neatness.

### Alternative D — mandatory full MMM procedure for all nontrivial work

**Strengths:** predictable structure and explicit checkpoints.

**Weaknesses:** current OpenAI guidance discourages unnecessary step-by-step process prescription; would create planning artifacts/ceremony on tasks that current agents can solve directly; overlaps A04/A06; high context cost.

**Verdict:** reject.

## 8. Scenario simulations

### Scenario A — simple negative case: one-line typo

**Input:** “Fix the typo in this README heading.”

**Current-pilot risk:** `deepen_when` should not trigger, but words such as V-model/hierarchical decomposition can still prime unnecessary structure.

**Selected candidate behavior:** execute directly under A04. No MMM reference, hierarchy, interface model, or extra validation ceremony.

**Success:** one bounded edit and relevant verification only.

**Deep guidance:** NO.

### Scenario B — multilevel feature

**Input:** “Add team invitations to the SaaS app,” requiring UI, API, persistence, email flow, permissions, and tests.

**Expected behavior:**

- preserve the user-level invitation outcome and permissions constraints;
- derive component responsibilities/interfaces;
- realize bounded parts;
- verify each component's requirements;
- integrate flows;
- validate the actual invitation journey end-to-end against the parent outcome.

**Known failure without A07:** every component test passes but the invited user cannot complete onboarding because API/UI/email assumptions disagree.

**Success:** child-level correctness plus integrated parent-level usefulness.

**Deep guidance:** YES — MMM is useful.

### Scenario C — existing architecture / design-first

**Input:** “Implement this already-approved event-sourcing architecture for audit history.”

**Current pilot risk:** “decomposing top-down” may encourage the agent to regenerate a requirements-first architecture instead of starting from the authoritative design.

**Selected candidate behavior:** use the existing design as current evidence, identify the parent outcome/constraints it serves, derive implementation tasks/interfaces, and validate upward. Do not force requirements-first sequencing.

**Success:** traceability preserved without recreating the design process.

**Deep guidance:** MAYBE, depending on number/coupling of implementation levels.

### Scenario D — locally passing components, globally failing product

**Input:** three modules each pass unit tests, but an end-to-end workflow violates a latency or user-facing requirement.

**Selected behavior:** local tests establish verification at component level only. Inspect integration/interfaces and validate the assembled system against the parent requirement. Correct the responsible level.

**Failure:** reporting completion because all unit tests pass.

**Deep guidance:** YES if the failure spans levels.

### Scenario E — architecture assumption is wrong

**Input:** Micro implementation repeatedly fails because a Meso interface assumes synchronous delivery, while the actual upstream system is eventually consistent.

**Selected behavior:** do not keep patching Micro retries around a false interface contract. Revise the Meso architecture/interface, then update affected Micro work and revalidate Macro outcome.

**Success:** correction occurs at the level disproven by evidence.

**Deep guidance:** YES.

### Scenario F — requirement/test is wrong

**Input:** implementation behaves correctly according to the actual user requirement, but a stale test asserts old behavior.

**Selected behavior:** trace the failing test to the governing requirement/current truth. If the test is stale, update the test rather than distorting correct implementation to satisfy a proxy.

**Boundary:** A11 determines authoritative current truth; A07 only preserves hierarchical traceability.

**Deep guidance:** MAYBE.

### Scenario G — hierarchical research/document deliverable

**Input:** “Produce a market report with an executive thesis, three sector analyses, and recommendations.”

**Selected behavior:** each sector analysis must support the report-level thesis/questions; local completeness is not enough if the assembled report omits a required comparison or recommendation. Validate the combined report against the requested purpose.

**Success:** A07 generalizes beyond code without forcing software-specific V-model artifacts.

**Deep guidance:** only if the report is complex enough to benefit from explicit MMM structure.

### Scenario H — XML vs Markdown control

Run Scenarios B, D, and E with the selected XML and equivalent compact Markdown.

**Expected:** same core behavior—parent/child traceability, upward integration, local verification, parent validation, correction at the failed level.

Representation should not be treated as the behavioral mechanism itself.

## 9. Evaluation targets for final synthesis

A07 has more overlap with neighboring modules than A06 and therefore needs explicit evidence before surviving into the final always-on constitution.

### Test 1 — incremental value over A01 + A04

Compare:

1. A01 + A04 only;
2. A01 + A04 + A07 selected candidate.

Use multilevel tasks where all local tests can pass while end-to-end intent fails.

Measure:

- child-to-parent traceability;
- missed interfaces;
- local-test proxy completion;
- end-to-end validation quality;
- unnecessary planning verbosity;
- total prompt/context cost.

If A07 produces no material improvement, merge/delete it.

### Test 2 — sequencing bias

Compare current Alternative A vs selected Alternative B on:

- requirements-first greenfield work;
- design-first existing architecture;
- bug diagnosis starting from observed behavior;
- iterative research/design work.

Measure whether “top-down” causes unnecessary restarting or over-planning.

### Test 3 — MMM reference activation

Check both failure directions:

- **under-activation:** agent stays local and misses parent coherence;
- **over-activation:** agent opens MMM for ordinary coherent tasks and produces process artifacts.

### Test 4 — correction-level discipline

Create paired failures where the defect is deliberately placed at:

- Micro implementation;
- Meso interface/decomposition;
- Macro target/assumption;
- stale test/evidence.

Success means the agent changes the owning level rather than always patching implementation.

## 10. Important uncertainties

### 10.1 Does A07 earn a separate always-on module?

**Moderate uncertainty.** The failure mode is real, and A07 captures a distinct hierarchy-preservation invariant, but A01 already owns substantive outcome validation and A04 already owns decomposition/review. The only justification for a separate root module is measurable improvement on multilevel coherence.

### 10.2 Is the MMM reference too sequence-prescriptive?

**Moderate uncertainty.** Its prose is iterative and complexity-adaptive, but the Macro→Meso→Micro shorthand may still bias current models toward a fixed order. Controlled evaluation should decide whether the deeper reference needs a later standalone revision.

### 10.3 Exact principle labels

**Low-to-moderate uncertainty.** `hierarchical-decomposition`, `requirements-traceability`, `verification`, and `validation` are established. `incremental-integration` is also established practice, but cross-domain tasks may interpret “integration” less uniformly than engineering tasks. The local semantic sentence disambiguates it sufficiently for the pilot.

## 11. Sources

Primary/authoritative sources checked 2026-09-07.

### Current OpenAI / ChatGPT / Codex — primary AI-native layer

1. OpenAI — GPT-5.6 Model Guidance  
   https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6
2. OpenAI — Harness engineering: leveraging Codex in an agent-first world  
   https://openai.com/index/harness-engineering/
3. OpenAI — How OpenAI uses Codex  
   https://openai.com/business/guides-and-resources/how-openai-uses-codex/

### Independent mature-agent convergence

4. GitHub Copilot — Asking Copilot questions in your IDE / Plan mode  
   https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide
5. GitHub Copilot — Best practices for using Copilot to work on tasks  
   https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks
6. GitHub Copilot — Optimizing AI usage / research-plan-implement phases  
   https://docs.github.com/en/copilot/tutorials/optimize-ai-usage
7. Kiro — Requirements-First Feature Specs  
   https://kiro.dev/docs/specs/feature-specs/requirements-first/
8. Kiro — Design-First Feature Specs  
   https://kiro.dev/docs/specs/feature-specs/tech-design-first/
9. Kiro — Feature Specs  
   https://kiro.dev/docs/specs/feature-specs/
10. Kiro — Correctness / property-based testing  
    https://kiro.dev/docs/specs/correctness/
11. Gemini CLI — Plan Mode  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/plan-mode.md
12. Gemini CLI — Tool reference / task dependency tracking  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md
13. Claude Code — Commands  
    https://code.claude.com/docs/en/commands
14. Claude Code — Common workflows  
    https://code.claude.com/docs/en/common-workflows

### Established external discipline — secondary grounding

15. NASA Systems Engineering Handbook — Fundamentals of Systems Engineering  
    https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/
16. NASA Systems Engineering Handbook — Logical Decomposition  
    https://www.nasa.gov/reference/4-3-logical-decomposition/
17. NASA Systems Engineering Handbook — Product Integration  
    https://www.nasa.gov/reference/5-2-product-integration/
18. NASA Systems Engineering Handbook — Product Verification  
    https://www.nasa.gov/reference/5-3-product-verification/
19. NASA Systems Engineering Handbook — Product Validation  
    https://www.nasa.gov/reference/5-4-product-validation/

### Local deeper method examined

20. Apex Meta — `apex-meta/informatics/MMM/working-method.md`  
    Existing candidate focused method; not modified in this A07 run.

## 12. Final recommendation

Keep A07 in the current pilot, but sharpen it from a **V-model sequence** into a **hierarchical coherence invariant**:

```text
parent outcome
  -> traceable lower-level responsibilities / interfaces
  -> bounded realization
  -> upward integration
  -> local verification
  -> parent-level validation
  -> revise the level invalidated by evidence
```

Retain the existing MMM working method as the conditional focused reference. Do not create a new Skill or duplicate reference.

Most importantly, do **not** consider A07 permanently justified merely because the method is intellectually coherent. During final cross-module synthesis, test whether it measurably prevents locally-correct/globally-wrong outcomes beyond what A01 + A04 already achieve. If not, merge it out to protect the always-on context budget.
