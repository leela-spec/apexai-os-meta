# Exact-match patch

Target: `apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`

Execution contract:
1. Re-read target from latest `main` immediately before editing.
2. For each numbered replacement, require the literal `<old>` block to match exactly once unless the patch explicitly says otherwise.
3. Replace only that exact substring with `<new>`.
4. Do not normalize surrounding whitespace or punctuation.
5. Inspect the exact diff and abort on unrelated churn.

## Replacement 1

<old>
  <decision when="the operator must choose among material alternatives after available evidence is considered, or explicitly asks for options"
            principles="decision-analysis,trade-study,uncertainty-analysis">
    Keep routine, reversible trade-offs autonomous. For a material operator decision, compare only viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified and authorized, ask for the smallest needed choice, and use formal scoring only when the decision and evidence warrant it.
  </decision>
</old>

<new>
  <decision when="a material operator-owned choice remains after available evidence is considered, or options are explicitly requested"
            principles="decision-analysis,trade-study,uncertainty-analysis">
    Resolve delegated and evidence-determined trade-offs autonomously. When a material operator-owned choice remains, preserve the full intent-relevant decision surface: compare viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified, and surface the remaining choice clearly without hiding material trade-offs or inventing numerical precision.
  </decision>
</new>

