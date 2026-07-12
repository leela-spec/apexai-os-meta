# Promotion gate record (stage-4 close)

```yaml
promotion_gate:
  run_id: US-IDEA-01-20260711
  artifact:
    path: 01-candidate-entry.v2.md
    version: 2
    sha256: "cd83e576d8e5b2caac3f8d40c11bc6d33482a669a50ed8c80be062ec05a13d54"
    hash_recomputed_by_orchestrator: true   # closes the reviewer's PROBABLE-identity caveat
  authority_promotion:
    state: verified            # candidate → verified per schemas/authority-state.schema.md
    basis_digest: "sha256:cd83e576d8e5b2caac3f8d40c11bc6d33482a669a50ed8c80be062ec05a13d54"
    verification_ref_chain:
      - 06-validity-verdict.md          # v1: C1,C2,C3 pass; C4 revise
      - 05-alignment-verdict.md         # v1: A1,A2,A3 pass
      - "scoped C4 re-review of v2: pass (recorded below)"
    alignment_carry_forward_basis: >
      alignment verdict binds to v1; the v1→v2 diff (recorded in 07) touched only the two
      C4 pointer strings on L47-L48 — the action structure and link-vs-action character A2
      evaluated are unchanged; carried forward per detective-review.md step 8 diff-scope rule.
  reviewer_families: [claude, claude]   # recorded limitation per review-verdict.schema.md
  lens_separation: blind_parallel_confirmed
  revision_cycles: 1
  scoped_re_review_verdict: pass        # D1 resolved (§8 verified correct), D2 resolved (path exists, deep-research section at L24/L56)
  operator_escalation: none
  NOTE_authority_fields_left_in_v2_frontmatter: >
    v2's own frontmatter still reads authority.state: candidate — DELIBERATELY not edited,
    because editing the artifact would change its hash and break every verdict binding.
    Verified status is carried by THIS sidecar record bound to the hash. Design lesson
    DL-1 in the simulation record: basis_digest must be defined over content excluding
    the authority block, or authority must live in a sidecar — current schema has a
    self-invalidation loop. Feeds the enforcement-code build item (ARCHITECTURE §7.1).
```

**Gate consequence:** the artifact is review-verified. It may now feed a canon-changing write **only** with `operator_validation: confirmed` — see 09-gate-presentation.md.
