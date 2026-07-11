# Adversarial Review Wiring (meta_detective step)

Rule: a single same-family reviewer is not sufficient independent validation for consequential outputs — context isolation removes conversational contamination, not shared model priors. Consequential outputs get the dual-blind wiring below; everything else gets no formal review step (gate G1–G5 coverage is enough).

Applies when: a packet is `consequential` — it proposes a canon-changing write (`state/`, `.claude/kb/`), carries `unresolved_risk` other than none, contains a cross-project conflict, or the operator explicitly requests review. Everything else: Do not invoke reviewers.

## procedure

1. **Freeze the subject.** Compute `basis_digest` (sha256 over canonicalized packet content + content hashes of its declared `sources`). All verdicts bind to the digest, not the filename. If any source path fails to resolve → `hold`, no reviewer invoked.
2. **Construct two blind packets.** Each reviewer receives: the frozen artifact, source paths, explicit assumptions, uncertainties, stop conditions. Each reviewer must NOT receive: the producer's proposed verdict, persuasive rationale, effort descriptions, the other reviewer's output, or any approval-oriented language.
3. **Run two lens-isolated reviewers in parallel** (subagents `apex-review-validity` and `apex-review-alignment`, read-only tools):
   - validity lens: is each claim actually supported by the cited evidence? For every critical criterion, first construct the strongest plausible case that the artifact is wrong, then test it against the evidence. Criterion-level verdicts, not one holistic score. No strategic judgment.
   - alignment lens: does the packet serve the weekly intent, project priorities, and the operator's locked decisions? No validity judgment.
4. **Aggregate deterministically.** No LLM resolves the two verdicts. Policy:

```yaml
review_aggregation:
  pass:            validity=pass AND alignment=pass
  needs_revision:  any criterion verdict is needs_revision and none is fail
  fail:            any criterion verdict is fail
  hold:            preflight failed | either reviewer returned blocked
  result_field_updates:
    on_pass: {authority.state: verified, verification_ref: <verdict_artifact_path>}
    on_fail_or_needs_revision: {authority.state: invalidated}
```

5. **Record.** Verdict artifact written to `artifacts/reviews/review-<packet_id>.md` using the handoff envelope (`packet_type: review_verdict`); it lists per-criterion verdict, evidence pointer, defect owner, unresolved uncertainty.

## constraints

- Constraint: reviewers cannot implement fixes; defects route back to the producing stage (named defect owner).
- Constraint: reviewer run must differ from producer run (fresh subagent invocation).
- Constraint: a packet whose digest changed after review reverts to `candidate` automatically — review of the wrong version is the primary failure this wiring exists to prevent.
- Stop: if both reviewers disagree at criterion level on the same criterion, the packet goes to the operator with both verdicts attached; the orchestrator never casts a tiebreak.
