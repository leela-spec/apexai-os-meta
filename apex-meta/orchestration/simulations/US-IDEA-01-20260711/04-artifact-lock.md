# Artifact lock — US-IDEA-01 review (stage 4)

```yaml
artifact_lock:
  run_id: US-IDEA-01-20260711
  artifact:
    path: apex-meta/orchestration/simulations/US-IDEA-01-20260711/01-candidate-entry.md
    version: 1
    sha256: "f70e408ce8f64768bd37bb879ba364c2885c7a6a210dec2c97076350d7de80a7"
  supporting:
    - path: apex-meta/orchestration/simulations/US-IDEA-01-20260711/02-placement-packet.md
      sha256: "ae320da53660892c6331e10fbeccd266e7ea377df6aba4bb97d5f5adeccfa132"
  declared_scope: ["semantic fidelity of candidate entry vs raw source", "placement soundness"]
  review_trigger: "US-IDEA-01 stage 4 — consequential (feeds durable doctrine mutation at gate)"
  author_identity: withheld_from_reviewers
  verdicts_bind_to: sha256, not filename
```

```yaml
artifact_lock_v2:
  artifact:
    path: apex-meta/orchestration/simulations/US-IDEA-01-20260711/01-candidate-entry.v2.md
    version: 2
    sha256: "cd83e576d8e5b2caac3f8d40c11bc6d33482a669a50ed8c80be062ec05a13d54"
  change_basis: "revision order in 07-review-decision.md; deterministic diff = exactly L47-L48 pointer corrections; recorded in 07"
  re_review_scope: "C4 only (diff-proven no adjacent change)"
```
