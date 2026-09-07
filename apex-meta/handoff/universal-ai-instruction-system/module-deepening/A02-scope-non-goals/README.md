---
type: ModuleDeepeningResult
title: A02 Scope & Non-goals
description: Evidence-backed deepening result for the universal <scope> module, balancing scope control against scope-induced under-delivery.
status: DONE
updated: 2026-09-07
---

# A02 — Scope & Non-goals

## 1. Final decision

- **Module:** A02
- **XML tag:** `<scope>`
- **Semantic purpose:** Determine what work belongs inside the authorized/requested task and what must remain outside it, while allowing materially enabling/supporting work and respecting governing constraints.
- **Selected deeper owner:** **No deeper artifact**
- **Selected established principles:** scope control; non-goals; change control; systems-engineering enabling work/products.
- **Rejected as universal anchor:** YAGNI. It remains useful for speculative future software capability, but is too software-specific and too narrow to govern universal task scope.

### Final root XML

```xml
<scope principles="scope-control,non-goals,change-control">
  Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
</scope>
```

### Equivalent compact Markdown control

```markdown
**Scope — scope control / non-goals:** Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
```

### Alternative B — AI-native authorization/autonomy candidate

**Status:** unselected comparison candidate from `../../10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md`. The final root XML above remains the completed baseline / Alternative A until later evaluation selects a winner.

```xml
<scope principles="authorization-mode,autonomy-boundaries,non-goals">
  Match action to the request: analysis/review/planning does not authorize implementation; change/build/fix requests authorize in-scope local changes and relevant non-destructive validation without asking. Keep incidental improvements separate and confirm before destructive, external, costly, or materially scope-expanding actions.
</scope>
```

Equivalent compact Markdown:

```markdown
**Scope — authorization mode / autonomy boundaries / non-goals:** Match action to the request: analysis/review/planning does not authorize implementation; change/build/fix requests authorize in-scope local changes and relevant non-destructive validation without asking. Keep incidental improvements separate and confirm before destructive, external, costly, or materially scope-expanding actions.
```

**Why retain this alternative:** current OpenAI guidance frames useful autonomy positively: permit safe in-scope local work and relevant non-destructive validation without repeated approval, but stop before destructive, external, costly, or materially scope-expanding actions. This gives A02 a positive execution role instead of only constraining adjacent work.

**Evaluation question:** does Alternative B reduce permission loops and under-execution without increasing scope creep or unsafe boundary crossing relative to Alternative A?

## 2. Why this is the right method

### 2.1 Underlying discipline evidence

The strongest established model is **scope control with explicit boundaries and controlled change**, not “do only the smallest literally requested action.”

- PMI scope-management guidance defines scope in terms of the work and resulting products required to achieve project objectives, then distinguishes authorized work from later changes. Its established control pattern is: define the objective/work boundary, authorize it, and control additions rather than letting them enter silently.
- PMI’s scope-creep literature identifies uncontrolled additions and developer “gold plating” as failures, but also documents the opposite failure, **scope kill**: a rigid boundary process can reject valid beneficial changes instead of surfacing them to the authorized decision-maker. This directly matches the program’s need to avoid both scope creep and artificial minimalism.
- NASA systems engineering explicitly includes **enabling products**—test, deployment, training, maintenance, infrastructure, services, and other support needed to progress or use an end product—as legitimate system work. This is strong evidence that supporting work can belong even when it was not the named end product.
- NASA requirements management requires bidirectional traceability, treats untraceable self-derived requirements as potential gold plating unless justified/concurred, and subjects baseline changes to impact assessment and approval. This maps cleanly to an agent rule: direct/enabling work may proceed inside the authorized task; genuinely new adjacent scope needs authorization.
- YAGNI, by contrast, originates in Extreme Programming and specifically argues against building **presumptive future software capability** before it is needed. It is valuable evidence against speculative infrastructure, but it does not define universal task scope and can wrongly suggest that legitimate enabling work should be excluded.

The resulting semantic model is therefore:

```text
authorized task
  -> direct target work                    IN
  -> materially enabling/supporting work  IN
  -> governing constraints                MUST RESPECT
  -> genuinely adjacent improvements      OUT unless authorized
  -> opportunistic cleanup/redesign       OUT unless it becomes enabling work
  -> speculative future capability        OUT unless authorized
  -> explicitly broad exploration         IN to the breadth actually authorized
```

### 2.2 Proven agent implementations

No mature agent runtime found exposes this exact semantic rule as one named feature. Mature systems instead converge on **explicit scope, layered instructions, and bounded authority**, which supports keeping A02 as a small always-on semantic invariant rather than inventing a new scope framework.

- **OpenAI Codex / AGENTS.md:** Codex applies folder-scoped instructions only to files inside their directory tree; more specific instructions win, and direct prompt instructions outrank repository guidance. OpenAI also recommends using the task queue/backlog for tangential ideas or incidental fixes instead of forcing every side finding into the active task.
- **OpenAI Codex safety controls:** managed configuration, constrained execution, network policy, approvals, and telemetry establish hard action boundaries separately from semantic task reasoning. A02 should respect such governing constraints, not replace them.
- **Claude Code:** permissions use deterministic deny/ask/allow-style rules and PreToolUse hooks that can block concrete actions. Working-directory/additional-directory rules also bound accessible resources. These are hard authorization controls; A02 remains the semantic “does this work belong to the task?” layer above them.
- **GitHub Copilot:** repository, path-specific, and agent instructions let guidance apply only where relevant rather than globally. Copilot agent work is assigned from a concrete issue/task, reinforcing the value of a bounded active mandate.
- **Cursor:** project rules can be Always, Auto Attached by glob, Agent Requested, or Manual; nested rules scope guidance to relevant subtrees. This is a mature example of explicit applicability rather than universalizing every useful rule.
- **Kiro:** steering supports `always`, `fileMatch`, `manual`, and `auto` inclusion. Specialized guidance can remain dormant until the request/file scope matches.
- **Windsurf:** Rules distinguish `always_on`, `glob`, `model_decision`, and `manual`; AGENTS.md in subdirectories is automatically scoped to that directory. Windsurf separately positions Skills for multi-step procedures and Rules for behavioral constraints.
- **Gemini CLI:** `GEMINI.md` is hierarchical and can load more-specific context just in time when tools access a directory, again showing that applicability boundaries and local relevance are first-class mechanisms.
- **Agent Skills:** skills are loaded on demand for reusable multi-step capability. A02 does not contain such a method; packaging it as a Skill would make a universal boundary dependent on optional activation.

These systems mostly control **where instructions/actions apply**, not the semantic distinction between direct, enabling, and adjacent work. That is precisely why a concise cross-agent A02 rule is still useful.

### 2.3 Local inference / decision

The pilot’s phrase **“unless they are necessary for the target”** is too restrictive.

“Necessary” can be read as strict logical indispensability. That would incorrectly exclude legitimate supporting work such as a compatibility migration, validation step, safeguard, test fixture, or project structure that materially enables the authorized outcome but was not enumerated literally.

The replacement uses three controls together:

1. **Authorized task** — the mandate defines the boundary, including explicit broad mandates such as “think ahead” or “include all work required for transition.”
2. **Direct or materially enabling work** — prevents literalism from blocking legitimate support while requiring a meaningful relationship to the target.
3. **Explicit exclusion of adjacent/cleanup/redesign/speculative work** — prevents “this might be useful” from becoming self-authorization.

This is deliberately not “minimum change,” “smallest process,” or “do only what was literally listed.” Those would overlap A04 and recreate scope-induced under-delivery.

## 3. Semantic contract

### MUST

- Treat the current authorized/requested task as the work boundary.
- Include work that directly realizes the target.
- Include supporting/enabling work when it materially contributes to realizing the authorized target, even if the user did not enumerate that action literally.
- Respect governing constraints, prohibitions, safety boundaries, compatibility requirements, and explicit non-goals that apply to the task.
- Preserve the breadth of an explicitly broad mandate; repository-wide migrations, complete transitions, or authorized “think ahead” work must not be artificially narrowed.
- Distinguish authorization to **analyze/recommend** broader work from authorization to **implement** it.
- When a genuinely adjacent issue is material, report or recommend it without silently implementing it unless broader action is authorized.

### MUST NOT

- Treat “only the literal action named” as the universal definition of scope.
- Forbid a safeguard, migration, validation step, compatibility change, or other support merely because it was not explicitly enumerated, when it materially enables the authorized outcome.
- Add architecture, cleanup, refactoring, redesign, safeguards, documentation, or infrastructure merely because they seem beneficial.
- Build speculative future capability without current authorization.
- Convert “think ahead” into permission to implement arbitrary future infrastructure.
- Convert a bounded research/evaluation mandate into implementation.
- Use scope control to choose the cheapest, shallowest, or least rigorous realization; A01 owns substantive adequacy and proportional rigor.
- Use A02 as a reuse method, workflow/minimal-process rule, ambiguity resolver, or recovery procedure; those belong to A03, A04, A05, and A10 respectively.

### Activation condition

Always active. Every task has a work boundary, even when the boundary is broad.

### Deepen condition

None. A02 is a universal classification invariant. Material ambiguity about the boundary routes to A05 rather than to a separate scope procedure.

## 4. Scope classification model

This model is explanatory evidence for the README, not a mandatory runtime ceremony.

| Work class | Default A02 treatment | Test |
|---|---|---|
| **1. Direct target work** | In scope | Does it directly produce/alter the requested result? |
| **2. Materially enabling/supporting work** | In scope | Would it materially support correctness, integration, reliable operation, transition, or completion of the authorized result? |
| **3. Governing constraints** | Must be respected | Is it imposed by the active instruction, safety/authorization boundary, compatibility contract, or other governing rule? |
| **4. Genuine adjacent improvement** | Do not implement by default | Useful, but the authorized result works without taking on this separate improvement. Report if material. |
| **5. Opportunistic cleanup/redesign** | Out by default | Is the agent improving nearby structure mainly because it prefers a different design? |
| **6. Speculative future infrastructure** | Out by default | Is it being built for a presumed future need rather than the current mandate? |
| **7. Explicitly broad exploration / “think ahead”** | In scope to the authorized mode/breadth | Does the mandate ask for forward-looking analysis/structure? If so, do that; do not infer authorization for unrelated implementation. |

A supporting action stops being “support” and becomes a scope change when its main purpose is an independently valuable adjacent outcome rather than materially enabling the requested one.

## 5. Neighboring-module boundaries

### A01 `<target>` — intended outcome and adequacy

A01 determines the substantive useful outcome, proportional rigor, and whether the delivered result is adequate. A02 does **not** redefine what “good enough” means; it only classifies whether proposed work belongs inside the authorized task.

Example: if a high-value feature needs substantial validation to be substantively adequate, A01 explains why the rigor matters; A02 permits the validation because it materially enables the authorized outcome rather than dismissing it as “extra.”

### A03 `<reuse>` — reuse before invention

Once A02 says a capability/work item belongs, A03 decides whether it should be satisfied by reusing a proven solution or by custom construction. A02 must not turn “avoid extra work” into a build-vs-reuse methodology.

### A04 `<workflow>` — execution complexity

A02 does not require the smallest process. A04 decides whether planning, decomposition, delegation, or review are warranted. A simple task can have a tight scope and direct execution; a complex task can have the same clear scope and a substantial workflow.

### A05 `<intent>` — material ambiguity

A02 must not resolve ambiguous scope by silently choosing the narrowest reading. If ambiguity about the authorized boundary would materially change the work, A05 resolves it from evidence or operator clarification.

### A10 `<recovery>` — incidental failure handling

A10 chooses the recovery behavior. A02 does not prohibit recovery work merely because it was absent from the original wording: an incidental repair/workaround can be in scope when it materially enables continuation of the authorized task. Recovery must still not become an unrelated redesign program.

## 6. Failure modes this module exists to prevent

1. **Scope creep:** adjacent useful work silently becomes part of the task.
2. **Gold plating:** the agent adds features/architecture because it prefers them, not because the authorized outcome calls for them.
3. **Scope kill / artificial minimalism:** a rigid boundary excludes legitimate supporting work and causes under-delivery.
4. **Literal-enumeration trap:** an unlisted but materially enabling step is treated as forbidden.
5. **Research-to-build drift:** evaluation/recommendation authorization is mistaken for implementation authorization.
6. **Opportunistic refactor:** a bounded fix becomes a subsystem redesign.
7. **Future-proofing drift:** speculative infrastructure is built for presumed later needs.
8. **Broad-mandate truncation:** “complete migration” or “think ahead” is incorrectly compressed into the smallest local edit.
9. **Authorization-mode confusion:** permission to analyze, recommend, or design is mistaken for permission to mutate/implement.
10. **Scope laundering through another module:** reuse, workflow, recovery, or rigor language is used to justify unrelated expansion.

## 7. Wording decision

### Candidate A — strict necessity

```xml
<scope principles="non-goals,YAGNI">
  Do not expand into adjacent cleanup, redesign, infrastructure, or safeguards unless they are necessary for the target.
</scope>
```

**Strength:** strong anti-creep signal; compact.

**Why it loses:** `necessary` is too restrictive for legitimate enabling work; `YAGNI` specifically targets presumptive future software capability rather than universal scope; “safeguards” can be wrongly suppressed even when they materially enable the requested result.

### Candidate B — material contribution only

```xml
<scope principles="scope-control,non-goals">
  Perform work that directly realizes or materially contributes to the target; leave unrelated improvements out.
</scope>
```

**Strength:** avoids literal minimalism and recognizes supporting work.

**Why it loses:** “materially contributes” alone is too permissive. Agents can rationalize a preferred refactor or architecture change as broadly helpful, and it does not explicitly preserve authorization/type boundaries.

### Candidate C — authorized scope + enabling work + controlled expansion — SELECTED

```xml
<scope principles="scope-control,non-goals,change-control">
  Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
</scope>
```

**Why it wins:** it pairs a positive inclusion test with explicit exclusions and an authorization boundary. It permits support without turning relevance into carte blanche.

### Candidate D — formal change-control gate

```xml
<scope principles="scope-baseline,change-control">
  Baseline the task scope before execution and raise a change request for any work not explicitly listed.
</scope>
```

**Strength:** very clear governance for formal projects.

**Why it loses:** creates ceremony on trivial tasks, wrongly treats every implied action as a change, and collapses semantic scope into project-management process.

## 8. Required scenario simulations

### Scenario A — opportunistic refactor

**Input:** Fix one bounded bug. Agent notices nearby architecture it dislikes.

- **Current pilot risk:** “necessary” may either block a small enabling refactor that is genuinely required, or be rationalized broadly because the agent claims the redesign is “necessary.”
- **Candidate behavior:** fix the bug and any materially enabling local change. Do not redesign the subsystem merely because it would be nicer. If the architectural issue is materially important but not needed for the requested fix, report it separately.
- **Observable PASS:** bounded bug is fixed; unrelated subsystem refactor is absent; any material adjacent concern is surfaced without implementation.
- **Deep guidance:** no.

### Scenario B — “think ahead”

**Input:** “Create the project and think ahead about what we will need.”

- **Current pilot risk:** YAGNI/necessity can suppress useful forward-looking structure; the opposite failure is treating “think ahead” as unlimited implementation authority.
- **Candidate behavior:** create the project and include forward-looking structure/recommendations that materially serve that explicit mandate. Do not build arbitrary future infrastructure unrelated to the project’s foreseeable authorized needs.
- **Observable PASS:** useful anticipated structure is present and traceable to the mandate; speculative systems are not silently implemented.
- **Deep guidance:** no; A05 only if the breadth becomes materially ambiguous.

### Scenario C — safeguard/supporting requirement

**Input:** A consequential implementation needs a migration, validation step, compatibility change, or safeguard to work correctly.

- **Current pilot risk:** strict literal/necessity interpretation may classify these as forbidden extras, especially if “necessary” is read as logically indispensable rather than materially enabling.
- **Candidate behavior:** include the supporting work when it materially enables the authorized outcome and respects governing constraints. Do not expand into a general hardening program.
- **Observable PASS:** requested outcome works with the materially relevant support; unrelated safeguards remain out.
- **Deep guidance:** no.

### Scenario D — research vs implementation

**Input:** “Evaluate which architecture is best. Do not implement anything.”

- **Current pilot:** should prohibit implementation, but its focus on adjacent work does not state the authorization-mode distinction clearly.
- **Candidate behavior:** research/evaluate/recommend only. Creating the recommended architecture is outside the authorized task.
- **Observable PASS:** no implementation/mutation artifacts are created; deliverable is the evaluation.
- **Deep guidance:** no.

### Scenario E — incidental cleanup

**Input:** During a bounded edit the agent finds unrelated stale files or formatting problems.

- **Current pilot:** usually leaves them alone, but may be unclear when cleanup is partly entangled with the requested edit.
- **Candidate behavior:** leave unrelated cleanup alone. Handle only the portion that materially enables the authorized change; report a materially risky adjacent issue without silently fixing it.
- **Observable PASS:** diff contains no opportunistic cleanup; blocking/enabling cleanup is bounded to the requested result.
- **Deep guidance:** no; A10 applies only if the stale state causes an incidental failure.

### Scenario F — explicitly broad mandate

**Input:** “Perform a repository-wide migration and include all work required for a complete transition.”

- **Current pilot risk:** “necessary”/YAGNI can bias the agent toward a narrow patch even though the authorized scope is broad.
- **Candidate behavior:** preserve repository-wide breadth and include materially enabling transition work such as compatibility changes/migrations when they belong to completion. Still avoid unrelated modernization.
- **Observable PASS:** all affected authorized surfaces are handled; breadth is not reduced to a token example; unrelated redesign stays out.
- **Deep guidance:** no; A04/A07 may deepen because of complexity, not because scope itself needs a method.

### Scenario G — interaction with A01 proportional rigor

**Input:** A high-value target requires substantial supporting work.

- **Current pilot risk:** scope language can fight A01 and suppress the work, causing a superficially small but inadequate delivery.
- **Candidate behavior:** A01 determines that substantial rigor is required; A02 permits the supporting work that materially enables that outcome while excluding unrelated expansion.
- **Observable PASS:** supporting work is present where tied to the authorized outcome; unrelated hardening/architecture is absent.
- **Deep guidance:** no; A01/A07 govern adequacy/realization.

### Scenario H — simple task

**Input:** “Fix this typo.”

- **Current pilot:** direct edit expected.
- **Candidate behavior:** direct typo fix. No scope statement, planning document, change-control ceremony, cleanup sweep, or discussion.
- **Observable PASS:** only the typo-relevant change is made and the task finishes.
- **Deep guidance:** no.

### Scenario I — XML vs Markdown control

**Input:** Run Scenario A or D with the XML wording versus the compact Markdown equivalent.

- **Expected:** same semantic boundary: direct/materially enabling work allowed; adjacent implementation blocked without authorization.
- **Observable PASS:** no material behavioral distinction caused by representation alone.
- **Deep guidance:** no.
- **Status:** semantically equivalent by inspection; empirical cross-agent representation testing remains for the later synthesis/evaluation phase.

## 9. Deepening-owner decision

**No deeper artifact.**

Reason:

- A02 is an always-on semantic boundary, not a reusable multi-step workflow.
- The key distinction fits in one compact invariant.
- A reference would mostly restate examples already captured in this research result and add JIT-routing cost without a separate operating method.
- A scoped rule is inappropriate because task scope is semantic, not reliably determined by repository path.
- A Skill is inappropriate because optional activation would weaken a universal constraint and there is no reusable procedure/scripts/templates to execute.

If later cross-agent evaluation shows that models systematically abuse “materially enables” to rationalize expansion, the correct fix is to tighten the root semantic wording or add a small evaluation example—not to create a scope-management Skill by default.

## 10. Alternatives rejected

| Alternative | Why rejected |
|---|---|
| **YAGNI as primary universal principle** | Strong for speculative future software capability; too narrow/software-specific for research, documentation, migrations, operations, or legitimate enabling work. |
| **KISS / smallest-change rule** | Optimizes implementation/process simplicity, not authorized work boundaries; risks A04 overlap and artificial minimalism. |
| **“Only explicitly requested actions”** | Fails implied/enabling work and consequential support requirements. |
| **Pure “material relevance” test** | Too permissive; agents can rationalize preferred adjacent improvements as helpful. |
| **Formal change-control process on every task** | Correct in governed projects, excessive as an always-on agent procedure; violates the simple-task requirement. |
| **Skill/reference for scope decisions** | No distinct multi-step reusable method justifies extra routing/context. |

## 11. Authoritative sources

Primary/authoritative sources checked 2026-09-07:

### Scope, requirements, enabling work

1. Project Management Institute — Scope Management  
   https://www.pmi.org/learning/library/scope-management-9099
2. Project Management Institute — Controlling scope creep  
   https://www.pmi.org/learning/library/controlling-scope-creep-4614
3. Project Management Institute — Top Five Causes of Scope Creep (includes gold plating and “scope kill”)  
   https://www.pmi.org/learning/library/top-five-causes-scope-creep-6675
4. NASA Systems Engineering Handbook — System Design Processes / Identify Enabling Products  
   https://www.nasa.gov/reference/4-0-system-design-processes/
5. NASA Systems Engineering Handbook — Technical Requirements Definition  
   https://www.nasa.gov/reference/4-2-technical-requirements-definition/
6. NASA Systems Engineering Handbook — Requirements Management  
   https://www.nasa.gov/reference/6-2-requirements-management/
7. NASA Systems Engineering Handbook — Stakeholder Expectations Definition  
   https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/
8. NASA NPR 7123.1D — Systems Engineering Processes and Requirements  
   https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Preface
9. Martin Fowler — Yagni (origin/scope in Extreme Programming and presumptive future software capability)  
   https://martinfowler.com/bliki/Yagni.html

### Mature agent implementations

10. OpenAI — Introducing Codex (published Codex system-message / AGENTS.md scope semantics)  
    https://openai.com/index/introducing-codex/
11. OpenAI — How OpenAI uses Codex (issue-shaped tasks; task queue for tangential/incidental work)  
    https://openai.com/business/guides-and-resources/how-openai-uses-codex/
12. OpenAI — Running Codex safely at OpenAI (technical boundaries / managed policy / approvals)  
    https://openai.com/index/running-codex-safely/
13. OpenAI — Unrolling the Codex agent loop (permissions and hierarchical instructions)  
    https://openai.com/index/unrolling-the-codex-agent-loop/
14. Claude Code — Configure permissions  
    https://code.claude.com/docs/en/permissions
15. Claude Code — Hooks guide  
    https://code.claude.com/docs/en/hooks-guide
16. GitHub Copilot — Custom instructions support  
    https://docs.github.com/en/copilot/reference/custom-instructions-support
17. GitHub Copilot — Customization cheat sheet  
    https://docs.github.com/en/copilot/reference/customization-cheat-sheet
18. Cursor — Rules  
    https://docs.cursor.com/context/rules
19. Kiro — Steering  
    https://kiro.dev/docs/steering/
20. Windsurf — Memories & Rules  
    https://docs.windsurf.com/windsurf/cascade/memories
21. Gemini CLI — Provide context with GEMINI.md files  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
22. Agent Skills — Claude Platform overview / best practices  
    https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview  
    https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
23. AGENTS.md — open convention / nested instruction scope  
    https://agents.md/

## 12. Evidence confidence and uncertainty

- **High confidence:** the pilot’s strict “unless necessary” wording is too narrow for a universal scope invariant because established systems engineering explicitly recognizes enabling/supporting work and PMI documents the opposite failure of overly rigid scope control.
- **High confidence:** YAGNI should not be the primary universal scope anchor; its established meaning is presumptive future software capability, not all task-boundary behavior.
- **High confidence:** A02 should distinguish semantic task membership from hard runtime authorization/permissions; mature agent systems layer these concerns rather than using one mechanism for both.
- **High confidence:** no separate Skill/reference is justified at this stage.
- **Moderate-high confidence:** `materially enables` is the best compact positive inclusion test found. It is intentionally stronger than “helpful” and broader than strict “necessary.”
- **Primary uncertainty for final cross-agent evaluation:** capable agents may still rationalize preferred refactors as “materially enabling.” Evaluation should therefore stress opportunistic refactors, broad safeguards, and future-proofing to see whether the explicit adjacent-work prohibition is strong enough.
- **Secondary uncertainty:** “authorized task” relies on the broader instruction hierarchy/current-truth system to identify which instruction is authoritative. A02 should not duplicate that precedence logic; A11/final synthesis should ensure the contract has one clear authority model.

## 13. Neighboring dependency note for later synthesis

No neighboring module should be edited now.

For later synthesis/evaluation, specifically test:

- A01+A02 together on high-rigor targets to ensure scope does not suppress substantive adequacy;
- A02+A05 on ambiguous breadth to ensure agents do not default to the narrowest reading;
- A02+A10 on incidental failures to ensure bounded recovery remains allowed;
- A02+A03/A04 to ensure “avoid extra work” does not mutate into reuse policy or process minimalism.

No merge or module-count reduction is recommended from A02 research.
