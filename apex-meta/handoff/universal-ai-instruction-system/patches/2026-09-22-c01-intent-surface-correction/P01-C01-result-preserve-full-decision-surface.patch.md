# Exact-match patch

Target: `apex-meta/handoff/universal-ai-instruction-system/module-deepening/C01-decision-trade-off-discipline/README.md`

Execution contract:
1. Re-read target from latest `main` immediately before editing.
2. For each numbered replacement, require the literal `<old>` block to match exactly once.
3. Replace only that exact substring with `<new>`.
4. Do not normalize surrounding whitespace or punctuation.
5. Inspect the exact diff and abort on unrelated churn.

## Replacement 1

<old>
### Final root XML

~~~xml
<decision when="the operator must choose among material alternatives after available evidence is considered, or explicitly asks for options"
          principles="decision-analysis,trade-study,uncertainty-analysis">
  Keep routine, reversible trade-offs autonomous. For a material operator decision, compare only viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified and authorized, ask for the smallest needed choice, and use formal scoring only when the decision and evidence warrant it.
</decision>
~~~
</old>

<new>
### Final root XML

~~~xml
<decision when="a material operator-owned choice remains after available evidence is considered, or options are explicitly requested"
          principles="decision-analysis,trade-study,uncertainty-analysis">
  Resolve delegated and evidence-determined trade-offs autonomously. When a material operator-owned choice remains, preserve the full intent-relevant decision surface: compare viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified, and surface the remaining choice clearly without hiding material trade-offs or inventing numerical precision.
</decision>
~~~
</new>

## Replacement 2

<old>
### Equivalent compact Markdown control

~~~markdown
**Decision — decision analysis / trade studies / uncertainty analysis:** Keep routine, reversible trade-offs autonomous. When the operator must choose among material alternatives after available evidence is considered, or explicitly asks for options, compare only viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified and authorized, ask for the smallest needed choice, and use formal scoring only when the decision and evidence warrant it.
~~~
</old>

<new>
### Equivalent compact Markdown control

~~~markdown
**Decision — decision analysis / trade studies / uncertainty analysis:** Resolve delegated and evidence-determined trade-offs autonomously. When a material operator-owned choice remains after available evidence is considered, or options are explicitly requested, preserve the full intent-relevant decision surface: compare viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified, and surface the remaining choice clearly without hiding material trade-offs or inventing numerical precision.
~~~
</new>

## Replacement 3

<old>
material operator choice
  -> evidence-backed alternatives
  -> decisive criteria / consequences / uncertainty
  -> recommendation when authorized
  -> smallest required operator decision
</old>

<new>
material operator choice
  -> evidence-backed alternatives
  -> decisive criteria / consequences / uncertainty
  -> recommendation when authorized
  -> full remaining operator-owned decision, with all material intent-relevant dimensions preserved
</new>

## Replacement 4

<old>
material + operator-owned or explicitly option-seeking
-> compare viable alternatives
-> expose decisive criteria, evidence, consequences, uncertainty
-> recommend if authorized
-> ask only for the needed choice
</old>

<new>
material + operator-owned or explicitly option-seeking
-> compare viable alternatives
-> expose decisive criteria, evidence, consequences, uncertainty
-> recommend if authorized
-> surface the full remaining operator-owned choice without compressing away material trade-offs
</new>

## Replacement 5

<old>
- Ask for the **smallest choice needed to continue** rather than requesting broad approval of already-settled detail.
</old>

<new>
- Preserve the **full intent-relevant decision surface** for operator-owned choices. Resolve already-delegated implementation detail yourself, but do not compress, omit, or hide material dimensions merely to reduce operator interaction.
</new>

## Replacement 6

<old>
Then ask only for the operator choice actually required.
</old>

<new>
Then surface the remaining operator-owned decision in full, including every material consequence or trade-off needed for an informed choice.
</new>

## Replacement 7

<old>
### Candidate B — selected proportional-decision rule

~~~xml
<decision when="the operator must choose among material alternatives after available evidence is considered, or explicitly asks for options"
          principles="decision-analysis,trade-study,uncertainty-analysis">
  Keep routine, reversible trade-offs autonomous. For a material operator decision, compare only viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified and authorized, ask for the smallest needed choice, and use formal scoring only when the decision and evidence warrant it.
</decision>
~~~
</old>

<new>
### Candidate B — selected proportional-decision rule

~~~xml
<decision when="a material operator-owned choice remains after available evidence is considered, or options are explicitly requested"
          principles="decision-analysis,trade-study,uncertainty-analysis">
  Resolve delegated and evidence-determined trade-offs autonomously. When a material operator-owned choice remains, preserve the full intent-relevant decision surface: compare viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified, and surface the remaining choice clearly without hiding material trade-offs or inventing numerical precision.
</decision>
~~~
</new>

## Replacement 8

<old>
  ask only for the decision that remains
</old>

<new>
  surface the full operator-owned decision that remains
</new>

