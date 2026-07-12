# meta_detective Reviewer Doctrine

Purpose: supplemental verification doctrine for the dual-blind reviewer pair — `apex-review-validity` (lens 1) and `apex-review-alignment` (lens 2). Governing contracts stay in `review-wiring.md`, `handoff-schema.md`, and the two agent definitions; this file adds only the verification craft distilled from the old-apex v1 role KB at `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/`. Verdict vocabulary is the current one (`pass | needs_revision | fail | blocked`, criterion-level, deterministic aggregation); no other verdict or confidence scale applies.

## Best practices

- Rule: classify source authority before judging support. Tag each cited source `[PRIMARY]`, `[DERIVED]`, `[WORKING]`, `[SPECULATIVE]`, or `[STALE]`; a criterion resting only on DERIVED/WORKING/STALE material when a PRIMARY source exists is at best `needs_revision`. (BEST_PRACTICES.md DET-BP-001)
- Rule: the primary artifact outranks any summary of it. When a recap, note, or packet body conflicts with the file it summarizes, the file wins and the criterion is non-pass. (MISTAKES.md DET-MIS-002)
- Rule: never infer through silence in an authoritative source — absence of a statement is not evidence that a claim is supported. (ESSENCE.md core constraints)
- Rule: target the load-bearing assumption. For each criterion, identify the single source gap, false assumption, contradiction, or base-rate mismatch that would flip the verdict, and test that hinge first — not the artifact in general. (BEST_PRACTICES.md DET-BP-003)
- Rule: every non-pass criterion names the smallest missing input that would unblock re-review, alongside the defect owner. A verified partial verdict beats a false complete approval. (BEST_PRACTICES.md DET-BP-005, DET-BP-010)
- Check: verify `authority.state` of every prerequisite/source the packet treats as authoritative. Candidate-state material used as if verified is candidate-to-canon leakage and a criterion `fail`. (BEST_PRACTICES.md DET-BP-006; MISTAKES.md DET-MIS-006)
- Check: classify each defect as evidence / contradiction / boundary / risk in the criterion line before assigning the verdict — classification prevents vague "needs work" findings and makes the defect actionable for the producing stage. (BEST_PRACTICES.md DET-BP-008)

## Known failure modes

- Avoid: challenge theater — broad skepticism that names no counter-evidence, kill condition, or decision consequence. Every non-pass must name the concrete way the packet breaks. (MISTAKES.md DET-MIS-005)
- Avoid: silent primary-source conflict resolution — when two primary sources disagree, return the conflict with both sources and authority scopes cited (`fail` or `blocked`); never pick by recency, preference, or narrative fit. (MISTAKES.md DET-MIS-003)
- Avoid: averaging a contradiction into a compromise verdict — two claims that cannot both be true are recorded as an explicit contradiction with severity, never blended by tone or convenience. (MISTAKES.md DET-MIS-010)
- Avoid: retry theater — when reviewing a revised packet after a prior non-pass, require a stated substantive delta from the failed version; if the same defect recurs after revision, `fail` with an uncertainty note flagging the repeat for the operator. (MISTAKES.md DET-MIS-007)

## Verification moves from the five internal modes

- Check (evidence_source_verifier → validity lens): resolve every citation path; confirm the cited span actually contains the claimed support, not merely the topic; flag staleness where evidence predates the state it claims to describe. (APPENDIX_INTERNAL_MODES.md, Evidence & Source Verifier)
- Check (contradiction_logic_auditor → validity lens): hunt five logic-issue types per criterion — contradiction, inference jump, unsupported claim, assumption-as-fact, claim/evidence mismatch — and tag each defect with exactly one. (APPENDIX_INTERNAL_MODES.md, Contradiction & Logic Auditor)
- Check (boundary_authority_guardian → validity lens): envelope-authority pressure — `target_surface` legal for the packet_type, `authority.state` consistent with digest/verification fields, no self-validation (producer marking its own output confirmed or verified). (APPENDIX_INTERNAL_MODES.md, Boundary & Authority Guardian)
- Check (boundary_authority_guardian → alignment lens): role-drift pressure — a packet proposing actions outside its producing stage's ownership, or stepping over a locked operator decision, is a boundary criterion, not a style note. (APPENDIX_INTERNAL_MODES.md, Boundary & Authority Guardian)
- Check (risk_failure_mode_red_teamer → alignment lens): for each proposed next step or delta, run a one-line pre-mortem (how does this fail), a reversibility check (one-way door?), and demand a stop condition; a risky proposal with no usable `stop_condition` is `needs_revision`. (APPENDIX_INTERNAL_MODES.md, Risk & Failure-Mode Red Teamer)
- Rule (verdict_escalation_synthesizer → both lenses): synthesis is deterministic aggregation now, not a reasoning step; what survives is the output discipline — every non-pass states evidence gap plus smallest unblocker, and severity is never softened. (APPENDIX_INTERNAL_MODES.md, Verdict & Escalation Synthesizer)

## Templates worth reusing

- Template: source/evidence checklist table — `| Source | Tag | Authority scope | Evidence strength | Issue |` — internal worksheet feeding validity criterion verdicts. (TEMPLATES.md DET-TPL-001)
- Template: contradiction audit table — `| Claim | Evidence | Logic issue | Severity |` — internal worksheet for decomposing a packet's reasoning chain before verdicting. (TEMPLATES.md DET-TPL-003)
- Template: risk red-team table — `| Failure scenario | Cause | Early warning signal | Kill/revise trigger | Owner |` — internal worksheet for alignment-lens pressure on next-step proposals. (TEMPLATES.md DET-TPL-005)
