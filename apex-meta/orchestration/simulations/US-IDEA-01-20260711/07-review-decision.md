# Review decision (deterministic aggregation — Meta Ops applies the rule, does not re-judge)

```yaml
review_decision:
  run_id: US-IDEA-01-20260711
  artifact_sha256: "f70e408ce8f64768bd37bb879ba364c2885c7a6a210dec2c97076350d7de80a7"
  inputs: { validity: revise, strategic_alignment: pass }
  precedence_rule: "escalate > needs_input > hold > revise > pass"
  overall: revise
  blocking: "C4 (major, minor-severity pointer defects)"
  revision_order:
    owner: source_owner   # the entry author = Meta Ops-authored record; correction executed by owner, NOT by either reviewer
    changes_allowed: exactly the two C4 corrections; all adjacent changes prohibited per verdict
    re_review_scope: "criterion-scoped (C4 only) — permitted iff deterministic diff proves nothing else changed (detective-review.md step 8)"
  note: "v1 artifact and both verdicts remain immutable; correction = new version 01-candidate-entry.v2.md, new hash, new lock entry"
```
