---
lock_note:
  run_id: US-SEQ-01-20260712
  stage: "2 correction + scoped re-review"
  version: 2
  frozen_artifact:
    path: apex-meta/orchestration/simulations/US-SEQ-01-20260712/01-strategy-options.v2.md
    supersedes: "01-strategy-options.md @ sha256 886fb532… (v1)"
    sha256: "24fb973f1bcad57f536c22659cb922b62bf10184890de2da874de2aa639ec6a0"
    digest_rule: "sha256 over LF-normalized file bytes"
  correction_ownership: "meta_strategy (spawned, read-only; returned corrections message-borne, meta_ops applied — DL-5)"
  diff_proof:
    method: "unified diff v1 -> v2, recorded in commit; exactly the defect-fix regions changed"
    regions_changed:
      - "C1a: frontmatter sources_evidence L15 (pass_condition L796 + fail_condition L797 text added)"
      - "C1a: R2 unresolved_risk L30 (fail_condition L797 -> pass_condition negated L796)"
      - "C1a: Thesis A Key risks L60 (L797 -> L796 pass_condition negated)"
      - "C1b: Thesis B Core value L67 (phase arcs L160 -> L139)"
      - "C2/C5: new uncertainty U7 added; Thesis B Audience/Leverage/Timing re-scoped to hypothesis + U7 hedge"
      - "C3: Recommendation rationale narrowed (reversibility = the act, not A's specific content; 'tightest alignment' qualified vs C L150/L34)"
    nothing_else_changed: true
  rereview_scope:
    criteria: [C1, C2, C3, C5]
    carried_forward:
      - "C4 (scope/boundary) PASSED on v1; the diff proves none of C4's supporting text (Leela language L58/L79/L94, stop_condition L33, R2 app-free) changed in substance — R2's edit is an anchor correction, not a scope change. C4 carries forward per detective-review.md step 8 diff-scope rule."
    protocol: "fresh reviewer context; prior defect IDs supplied; producer's why-it-now-passes rationale withheld; re-review the artifact, not the correction claim"
  reviewer_family: claude
---

# v2 freeze + scoped re-review scope

v2 (`24fb973f…`) supersedes v1 (`886fb532…`). The correction is diff-proven: exactly the C1/C2/C3/C5
defect-fix regions changed, nothing else. Re-review is criterion-scoped to C1, C2, C3, C5 with a fresh
Detective context. C4 (scope/boundary) passed on v1 and its supporting text is provably unchanged, so
it carries forward.
