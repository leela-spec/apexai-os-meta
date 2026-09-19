---
type: ModuleDeepeningResult
title: C01 Conditional Decision / Trade-off Discipline
description: Evidence-backed deepening result for the conditional decision module, preserving agent autonomy for routine trade-offs while surfacing material operator choices with proportional, uncertainty-aware decision support.
status: DONE
updated: 2026-09-19
---

# C01 — Conditional Decision / Trade-off Discipline

## 1. Final decision

- **Module:** C01
- **XML tag:** <decision>
- **Semantic purpose:** Help the operator resolve a real material choice without turning routine agent judgment into approval ceremony or turning qualitative trade-offs into fake numerical certainty.
- **Selected deeper owner:** **No deeper artifact**
- **Selected established principles:** decision analysis; trade studies; uncertainty analysis; proportional decision support.
- **Key correction to the pilot:** C01 activates only when an operator-facing material choice remains after available evidence is considered, or when the operator explicitly asks for options. Routine, reversible trade-offs stay delegated to the agent. Formal scoring is an escalation, not the default.
- **Custom REI / local scoring formula:** **rejected**. Impact, evidence, risk, cost, reversibility, and similar factors may be useful decision criteria, but they are not combined into a universal invented score.

### Final root XML

~~~xml
<decision when="the operator must choose among material alternatives after available evidence is considered, or explicitly asks for options"
          principles="decision-analysis,trade-study,uncertainty-analysis">
  Keep routine, reversible trade-offs autonomous. For a material operator decision, compare only viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified and authorized, ask for the smallest needed choice, and use formal scoring only when the decision and evidence warrant it.
</decision>
~~~

### Equivalent compact Markdown control

~~~markdown
**Decision — decision analysis / trade studies / uncertainty analysis:** Keep routine, reversible trade-offs autonomous. When the operator must choose among material alternatives after available evidence is considered, or explicitly asks for options, compare only viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified and authorized, ask for the smallest needed choice, and use formal scoring only when the decision and evidence warrant it.
~~~

## 2. Why this is the right method

### 2.1 Current OpenAI / ChatGPT / Codex evidence

Current OpenAI operating guidance converges on **low-friction autonomy inside established boundaries, with human review reserved for higher-risk or genuinely decision-bearing actions**.

OpenAI's May 2026 description of its internal Codex deployment states the principle directly: low-risk everyday actions should be frictionless, while higher-risk actions stop for review. Its auto-review design exists specifically to avoid interrupting users for routine work when authorization is already sufficient. That supports the negative boundary of C01: an agent should not manufacture a decision gate for ordinary reversible implementation choices.

OpenAI's current ChatGPT app-permission model makes the same distinction at the product layer: low-risk actions can be allowed without repeated approval, while higher-risk actions may require confirmation. This is not itself a general decision-analysis method, but it is strong evidence that modern agent interaction should distinguish routine delegated action from consequential review rather than treating all choices alike.

OpenAI's current "research to decision memo" use case provides the positive pattern for decisions that genuinely remain with a decision-maker. It recommends a source-backed recommendation, alternatives and trade-offs, risks, assumptions, unresolved questions, and a decision record, while separating evidence from interpretation. It also recommends stress-testing the preferred option and identifying what additional evidence could change the recommendation.

The portable C01 synthesis is therefore:

~~~text
routine delegated choice
  -> agent decides and continues

material operator choice
  -> evidence-backed alternatives
  -> decisive criteria / consequences / uncertainty
  -> recommendation when authorized
  -> smallest required operator decision
~~~

C01 should not duplicate the approval mechanics of any one product. It captures the behavioral boundary behind them.

### 2.2 Independent mature-agent convergence

**Anthropic Claude.** Current Claude prompt guidance explicitly recommends local, reversible actions without needless confirmation and asks for user confirmation before actions that are hard to reverse, affect shared systems, or could be destructive. This independently supports a reversibility/consequence threshold instead of blanket approval loops.

**GitHub Copilot.** GitHub's current automation model routes routine, clear-cut actions automatically under its balanced setting and holds ambiguous/lower-confidence actions for review. GitHub describes this as a way for users to spend time only on changes likely to need a second look. That is a product-specific implementation, but the general pattern is portable: route human attention to the choices where it can materially change the outcome.

**Gemini CLI.** Gemini CLI Plan Mode is a read-only environment for researching complex changes, evaluating trade-offs, discussing implementation options with the user, and obtaining approval before implementation. It is intentionally a planning mode for cases where strategy needs alignment, not a requirement that every ordinary edit be converted into a formal options exercise.

Across these systems the convergence is:

- routine work should not be inflated into a decision ceremony;
- consequential or strategy-bearing choices receive explicit human attention;
- the agent should do the evidence gathering and option analysis before asking;
- the user's interruption should be about the actual choice, not about every intermediate step.

### 2.3 Established external decision discipline

NASA's Systems Engineering Handbook provides the most useful proportionality rule. Its Decision Analysis process says that **not all decisions require the same amount of analysis**, that rigor should depend on how clear-cut the decision is, and that decision-analysis complexity should fit the mission/system/decision complexity. Evaluation can range from direct stakeholder discussion to formal trade studies, simulations, tests, and weighted methods.

NASA also gives a sharp uncertainty rule: further uncertainty reduction matters when it could alter the ranking of alternatives. If added analysis cannot realistically change the choice, more analysis is process cost rather than decision value.

The 2026 UK Green Book provides an important anti-pseudo-precision correction. It allows formal MCDA for complex technical trade-offs, but explicitly recommends against simple multi-criteria "weighting and scoring" that lacks an objective basis and can reduce transparency. Proper MCDA uses structured methods such as swing weighting and requires suitable expertise.

Therefore C01 should not carry MCDA as an always-implied root method. Formal MCDA is one possible escalation when a real multi-attribute decision justifies it; a naive 1–5 score table is not the default.

### 2.4 Local synthesis

The current pilot was directionally correct but too eager to imply a formal method:

~~~text
material choice
-> trade-study / MCDA / decision-record
~~~

The improved boundary is:

~~~text
routine / reversible / delegated
-> decide autonomously

material + operator-owned or explicitly option-seeking
-> compare viable alternatives
-> expose decisive criteria, evidence, consequences, uncertainty
-> recommend if authorized
-> ask only for the needed choice

complex enough that qualitative comparison is insufficient
-> select an established formal method proportionate to the real decision
~~~

This retains the value of decision analysis while avoiding a permanent decision-matrix bureaucracy.

## 3. Semantic contract

### MUST

- Determine whether a real operator decision exists before presenting an options framework.
- Resolve routine, low-impact, reversible, or clearly delegated implementation trade-offs autonomously.
- Use the target, constraints, current authority, and available evidence to eliminate infeasible or clearly dominated options before involving the operator.
- If the operator must choose, state the decision in one clear sentence and present only materially distinct viable alternatives.
- Compare alternatives using the **decisive criteria for this decision**, not a fixed universal rubric.
- Keep evidence, inference, assumptions, consequences, and uncertainty distinguishable.
- Show uncertainty when it could change the recommendation or operator preference.
- Give a recommendation when the task authorizes advisory judgment and the evidence supports one; otherwise identify the unresolved trade-off without manufacturing certainty.
- Ask for the **smallest choice needed to continue** rather than requesting broad approval of already-settled detail.
- Scale the analysis method to the complexity, consequence, uncertainty, number of material criteria, and stakeholder/value conflict actually present.
- If formal scoring is used, make its criteria, scales, weights, evidence basis, and sensitivity explicit enough that the numbers are interpretable rather than decorative.

### MUST NOT

- Turn every technical choice into a user decision.
- Ask the operator to choose between alternatives the agent can resolve from already-authorized criteria and evidence.
- Use a weighted matrix merely because multiple options exist.
- Treat a subjective 1–5 or 1–10 score as measured evidence.
- Invent universal weights or a custom "importance/evidence/risk" formula and present it as established decision science.
- Hide source disagreement, close rankings, or outcome-changing uncertainty behind a single confident winner.
- Present obviously infeasible, dominated, or cosmetic variants as if they were meaningful choices.
- Reopen a decision the operator has already made unless new evidence materially changes the decision basis.
- Use C01 as a generic research workflow, requirements interview, scope-approval loop, or graded-rigor framework.
- Absorb the Source-Governed Execution Contract into C01.

### Activation condition

C01 activates when either:

1. after available evidence is considered, a **material choice remains that the operator must make** because it depends on operator/stakeholder preference, authority, accountability, or another non-delegated value judgment; or
2. the operator explicitly asks for options, alternatives, a comparison, or a trade-off analysis.

C01 does **not** activate merely because two implementation paths exist.

### Deepen condition

No persistent deeper artifact is justified.

If the decision is unusually complex, C01 can still deepen **situationally** by applying an established decision method verified for the actual domain. The method should be selected just in time from authoritative sources rather than frozen into a universal local Skill. Examples include a formal trade study, cost-effectiveness analysis, scenario analysis, or properly executed MCDA when the decision genuinely needs them.

This avoids three failure modes:

- a stale universal decision Skill;
- forced matrices for ordinary work;
- collision with the separate graded-rigor project.

### Neighboring-module boundaries

**A01 <target>** owns the intended outcome and substantive success criteria. C01 compares alternatives against those criteria; it does not redefine them.

**A02 <scope>** owns authorization boundaries. C01 does not turn an unauthorized action into an option merely by presenting it.

**A05 <intent>** owns ambiguity about what the operator means. If intent is unclear, resolve that first. C01 starts when intent is sufficiently clear but a material choice among known alternatives remains.

**A08 <evidence>** governs what the evidence actually supports. C01 must not turn weak evidence into confident decision claims.

**A13 <grounding>** remains the normal evidence-first baseline: actual frame/problem/task/environment -> normal web search -> at least three verified-quality sources by default -> congruence check -> reason from evidence. C01 does not weaken or replace that rule. Research expands only when the task/environment is materially complex or reliable sources materially disagree.

**C02 <research>** remains a separate deeper research discipline. It activates only when ordinary A13 grounding is insufficient for the decision.

**Source-Governed Execution Contract** remains a separate later synthesis/integration item. C01 does not absorb governing-source precedence.

**Graded rigor** remains a separate project-management question. C01 uses proportionality locally but does not define or authorize a new global L1/L2/L3 rigor taxonomy.

## 4. Compact decision method

This method lives in this module result for evaluation; it is not a separate runtime artifact.

### Step 0 — do not activate unnecessarily

Ask:

> Is this actually an operator decision, or an ordinary delegated trade-off the agent should resolve?

If it is routine/reversible/delegated, decide and continue.

### Step 1 — frame the choice

State:

- the decision to be made;
- who owns it;
- the decision boundary;
- the target and constraints that define success.

If the problem is really unresolved intent, route to A05 instead.

### Step 2 — ground decision-relevant facts

Use A13 for externally knowable claims. Use A08 to ensure claims do not exceed evidence.

Do not ask the operator to decide a fact that can be verified.

### Step 3 — prune before comparing

Remove options that are:

- incompatible with hard constraints;
- clearly unable to realize the target;
- materially dominated by another option on the stated criteria;
- duplicates/cosmetic variants that do not change the decision.

Keep a status-quo / do-nothing option when it is genuinely viable and decision-relevant, not as ritual padding.

### Step 4 — choose the lightest sufficient comparison

Default:

~~~text
Option
-> decisive advantages
-> decisive costs/risks
-> evidence
-> uncertainty / assumptions
-> practical consequence
~~~

Use a small table only when it improves scanability.

Escalate to a formal method only when the decision's complexity or uncertainty warrants it. Signals include:

- many genuinely competing criteria;
- mixed quantitative and qualitative outcomes that are hard to compare directly;
- high consequence;
- significant stakeholder/value conflict;
- close alternatives;
- uncertainty that could change the ranking/preference.

### Step 5 — handle uncertainty explicitly

If reducing uncertainty could change the choice, identify the smallest additional evidence that would resolve it.

If additional evidence is unlikely to change the choice, do not research indefinitely.

If alternatives remain effectively tied, say so instead of manufacturing a winner.

### Step 6 — recommend or hand off the choice

When advisory judgment is authorized and evidence supports a preference:

- give one recommendation;
- state the decisive reason;
- name the assumption or uncertainty most likely to change it;
- give concise rejection reasons for the serious alternatives.

Then ask only for the operator choice actually required.

### REI verdict

The historical (I/E/R) concept is **not promoted**.

Impact, evidence, and risk can be useful descriptive dimensions in some decisions, but:

- they are not universally exhaustive;
- they do not have a validated universal weighting scheme;
- collapsing them into one score would create false precision;
- the decisive criteria should come from the actual target and decision context.

## 5. Scenario simulations

| Scenario | Current-pilot risk | Candidate behavior | Observable pass criterion | Deep guidance? |
|---|---|---|---|---|
| **Simple / negative:** two internal helper functions both satisfy a local refactor; rollback is trivial | "trade-study" language can encourage unnecessary option presentation | inspect evidence, choose the better fit, implement; no operator question | no matrix/options ceremony; work continues | No |
| **Clear positive:** product owner must choose managed SaaS vs self-hosted service; both satisfy requirements but differ materially in control, cost, operations, and lock-in | current pilot has useful structure but does not explicitly protect routine autonomy or formal-method proportionality | ground current facts, prune infeasible variants, compare the viable choices on the few decisive criteria, recommend if authorized, ask for one choice | operator can decide from a compact evidence-backed comparison | No |
| **Ambiguous:** user says "show me database options" but workload, persistence, and compliance constraints are unclear | C01 could compare arbitrary products before intent/requirements are stable | A05 resolves the smallest material requirement ambiguity first; C01 then compares only options that fit | no fake comparison based on unstated criteria | No |
| **Conflict / edge:** three strong sources disagree about a platform capability that could reverse the preferred architecture | C01 could average conflicting evidence into a pseudo-consensus | A13 widens research and surfaces the conflict; A08 calibrates support; C01 presents conditional consequences if conflict remains | disagreement stays visible and recommendation is conditional or withheld | Situational external method only if still needed |
| **Known failure:** agent assigns 1–10 scores to "future-proofing", "maintainability", and "ecosystem", applies arbitrary weights, and announces a 7.8 vs 7.4 winner | current MCDA label can legitimize matrix-shaped pseudo-precision | reject unsupported numeric scoring; compare qualitative evidence directly or use a properly founded formal method only if warranted | no ungrounded weights/scales presented as objective evidence | No |
| **Close alternatives:** two options are nearly tied and one uncertain cost assumption could flip the result | pressure to produce a single recommendation can hide sensitivity | show the close result, identify the decision-changing assumption, gather only the evidence worth its cost or hand the conditional choice to the operator | no fake winner; uncertainty is decision-relevant | No |
| **XML vs Markdown control:** same material decision is run with equivalent XML and Markdown wording | XML might be assumed superior because it is structured | both should trigger the same decision boundary and option behavior | no material semantic difference is presumed; full-program eval decides representation | No |

## 6. Wording alternatives considered

### Candidate A — current pilot

~~~xml
<decision when="the operator must choose among material alternatives or explicitly asks for options"
          principles="trade-study,MCDA,decision-record">
  Present distinct options, consequences, evidence, uncertainty, recommendation, and concise rejection reasons. Avoid false numerical precision.
</decision>
~~~

**Strength:** concise; already distinguishes material operator choices from ordinary work; explicitly calls out evidence, uncertainty, and pseudo-precision.

**Why it loses:** MCDA in the principle list over-signals formal scoring; the wording does not explicitly preserve autonomy for routine/reversible trade-offs; it does not say formal scoring is conditional; it asks for "distinct options" without first pruning to viable alternatives.

### Candidate B — selected proportional-decision rule

~~~xml
<decision when="the operator must choose among material alternatives after available evidence is considered, or explicitly asks for options"
          principles="decision-analysis,trade-study,uncertainty-analysis">
  Keep routine, reversible trade-offs autonomous. For a material operator decision, compare only viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified and authorized, ask for the smallest needed choice, and use formal scoring only when the decision and evidence warrant it.
</decision>
~~~

**Why it wins:** preserves autonomy, makes evidence precede operator interruption, keeps the option set decision-relevant, explicitly scales formality, and retains uncertainty without introducing a custom score.

### Candidate C — minimal options rule

~~~xml
<decision when="a material operator choice remains or options are explicitly requested"
          principles="decision-framing,trade-offs">
  Show the viable options, decisive trade-offs, evidence, uncertainty, and a recommendation when justified; ask only for the choice that remains.
</decision>
~~~

**Why it loses:** excellent token economy, but it omits the negative rule that routine reversible trade-offs should remain autonomous and it provides no guard against matrix/scoring overreach.

### Candidate D — formal escalation pointer

~~~xml
<decision when="a material operator choice remains"
          principles="decision-analysis,trade-study"
          deepen_when="multiple objectives, stakeholders, uncertainty, or consequences make a direct comparison insufficient"
          ref="...">
  Compare viable alternatives and escalate to a formal decision method when complexity warrants it.
</decision>
~~~

**Why it loses:** a persistent reference is not justified yet. Formal decision methods are domain-sensitive, and a fixed local reference would duplicate the separate graded-rigor question while consuming context and maintenance surface.

## 7. Alternatives rejected

### Universal weighted decision matrix

Rejected. It is easy to scan but encourages arbitrary scales and weights when evidence does not support quantification. The UK Green Book explicitly distinguishes proper MCDA from simple weighting-and-scoring MCA and recommends against the latter.

### Universal MCDA Skill

Rejected. Proper MCDA can be valuable for complex multi-attribute decisions, but it requires explicit value modeling, defensible scales/weights, sensitivity analysis, and sometimes expert facilitation. Making it the default C01 method would over-trigger and contradict proportionality.

### Historical REI formula

Rejected as a universal method. The underlying dimensions may still be used qualitatively when relevant, but no evidence established a universal formula or weighting.

### Always ask the operator when alternatives exist

Rejected. Current OpenAI, Anthropic, and GitHub agent guidance converges on preserving autonomy for routine, low-risk, reversible work.

### Let the agent decide every technical choice

Rejected. Some choices encode stakeholder values, authority, accountability, external consequences, or product semantics that cannot be inferred legitimately from technical evidence alone.

## 8. Sources

Checked 2026-09-19. Current AI-native primary evidence first.

### OpenAI / ChatGPT / Codex

1. OpenAI — **Running Codex safely at OpenAI** (2026-05-08)  
   https://openai.com/index/running-codex-safely/

2. OpenAI Developers — **Turn research findings into a decision memo** (current 2026 use-case guidance)  
   https://developers.openai.com/de-DE/use-cases/research-to-decision-memo

3. OpenAI Help Center — **Managing app permissions in ChatGPT** (current 2026)  
   https://help.openai.com/de-de/articles/20001495-managing-app-permissions-in-chatgpt

### Independent mature-agent systems

4. Anthropic — **Prompting best practices: balancing autonomy and safety** (current Claude Platform documentation)  
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

5. GitHub — **About rationale, confidence, and approvals for issues** (Copilot automations; current public-preview documentation)  
   https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automation-rationale-and-approvals

6. Gemini CLI — **Plan Mode** (current documentation)  
   https://geminicli.com/docs/cli/plan-mode/

### Established external decision disciplines

7. NASA — **NASA Systems Engineering Handbook**, section 6.8 Decision Analysis  
   https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf

8. NASA — **6.8 Decision Analysis** web reference  
   https://www.nasa.gov/reference/6-8-decision-analysis/

9. HM Treasury — **The Green Book (2026)**, options appraisal / MCDA guidance  
   https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026

10. HM Treasury — **Use of multi-criteria decision analysis in options appraisal** (supplementary guidance)  
    https://www.gov.uk/government/publications/green-book-supplementary-guidance-use-of-multi-criteria-decision-analysis/use-of-multi-criteria-decision-analysis-in-options-appraisal-of-economic-cases

### Preserved local historical input — not current authority

11. apex-meta/handoff/universal-ai-instruction-system/handoffs/M06-decision-elicitation-and-trade-studies.md  
    Historical research handover. Useful for provenance of the original operator requirement and REI question, not current authority.

## 9. Evidence confidence and open uncertainty

- **High confidence:** routine/reversible choices should remain autonomous rather than creating repeated operator approval loops.
- **High confidence:** material decision support should expose alternatives, evidence, trade-offs, and decision-relevant uncertainty.
- **High confidence:** decision-analysis rigor should scale with decision complexity/consequence rather than defaulting to a formal matrix.
- **High confidence:** naive universal weighting/scoring is not a sound substitute for proper MCDA or qualitative evidence.
- **High confidence:** A13 must remain the normal grounding baseline and C01 must consume, not replace, that evidence discipline.
- **Moderate-high confidence:** "decision-analysis,trade-study,uncertainty-analysis" is a more accurate universal principle set than the current "trade-study,MCDA,decision-record".
- **Moderate confidence:** the exact compact XML sentence is the best current candidate, but wording-level superiority must still be tested in the later cross-module controlled evaluation.
- **Open:** XML versus equivalent compact Markdown remains an empirical program-level question; C01 research does not establish a format winner.
- **Open:** some domains have specialized decision methods superior to generic trade studies. C01 intentionally leaves those to JIT domain evidence rather than canonizing one universal method.

## 10. Final invariant

~~~text
NO OPERATOR CEREMONY FOR ROUTINE TRADE-OFFS

IF a material operator choice remains:
  ground decision-relevant facts first
  keep only viable alternatives
  compare decisive criteria + evidence + consequences + uncertainty
  recommend when justified and authorized
  ask only for the decision that remains

IF simple qualitative comparison is sufficient:
  stop there

IF complexity / consequence / decision-changing uncertainty warrants formality:
  select an established method proportionate to the real decision

NEVER:
  invent weights/scores to manufacture certainty
  hide close alternatives or source conflict
  absorb A13, C02, the Source-Governed Execution Contract, or graded-rigor governance into C01
~~~
