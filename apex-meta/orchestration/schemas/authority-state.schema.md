---
title: "Authority State Schema"
purpose: >
  The one minimal artifact-lifecycle field every consequential artifact carries:
  may this artifact be treated as authoritative input? Distinct from operator_validation
  (may this mutation be applied?). Both must pass for canon-changing writes.
  Translated from the old Apex v2 candidate-vs-canon invariant — one enforced field,
  NOT a state machine.
created: 2026-07-11
source: >
  apex-meta/fable-orchestrator/prompts/PromptAnswers/Role-vs-state permission separation (DEEP).md §4,
  ground-checked in prompts/PromptAnswers/research-integration-note.md §2.
---

# Authority State Schema

## The field

Every consequential artifact (work item, packet, KB candidate, decision input) carries in its frontmatter:

```yaml
authority:
  state: candidate | verified | invalidated
  basis_digest: null | "sha256:<64-hex-digest>"
  verification_ref: null | "<repo-relative path to the independent review artifact>"
```

- **`state`** — may this artifact be treated as authoritative input? `candidate` = produced, not independently reviewed. `verified` = independently reviewed against this exact version. `invalidated` = failed review, contradicted, or stale.
- **`basis_digest`** — sha256 over the canonicalized artifact content plus the content hashes of its declared evidence and dependency references. Binds the review to the exact version, not to a filename.
- **`verification_ref`** — the review-verdict artifact (see `review-verdict.schema.md`) that justified `verified`.

## Transition rules

```yaml
authority_transition_rules:
  on_create:
    state: candidate
    basis_digest: null
    verification_ref: null

  on_content_or_declared_evidence_change:
    # any substantive edit resets authority — a verified artifact edited is a candidate again
    state: candidate
    basis_digest: null
    verification_ref: null

  candidate_to_verified:
    allowed_only_when:
      - "verification_ref resolves to an independent review artifact"
      - "review verdict is pass"
      - "reviewer run differs from the creator run (reviewer never verifies own output)"
      - "review basis_digest equals the current deterministic digest"
    result: { state: verified }

  candidate_or_verified_to_invalidated:
    allowed_when:
      - "review verdict is fail or needs_revision"
      - "a governing source contradiction is recorded"
      - "stored basis_digest no longer matches current content + declared evidence closure"

  invalidated_to_candidate:
    allowed_only_after:
      - "substantive revision or evidence update"
    result: { state: candidate, basis_digest: null, verification_ref: null }

  canon_changing_write:
    allowed_only_when:
      - "operator_validation is confirmed"                                    # the mutation gate
      - "every authoritative input in the mutation's dependency closure has authority.state: verified"
      - "every stored basis_digest matches current content + declared evidence closure"
```

## ONE enforcement surface

The check lives **inside the existing apex-session write path** (the single gated mutation surface — `.claude/skills/apex-session/SKILL.md` steps 5–6, `references/mutation-gate-rules.md`). Before any canon-changing mutation is treated as confirmed:

1. validate the `authority` object of every declared authoritative input;
2. validate the requested transition;
3. recompute and compare `basis_digest`;
4. resolve `verification_ref` and require a passing independent verdict;
5. reject if any dependency is not currently `verified`.

Do **not** add a separate lifecycle engine, git hook, or per-role state machine. This preserves the system's strongest property — one mechanized mutation surface — while adding the one object-state fact role partitioning cannot represent.

## What this prevents / does not prevent

- **Prevents:** missing review, review of the wrong version, stale verification, use of explicitly invalidated material — the "authorized mutation based on an artifact that lacked current authority" break-scenario.
- **Does not prevent:** a verifier making a bad judgment. No state field does; that risk is carried by the falsification contract in `workflows/detective-review.md`.

## Open build item

Digest computation + closure check as code in the apex-session flow (stdlib `hashlib`, canonicalization rule to be fixed at implementation): flagged in `ARCHITECTURE.md` as the one open enforcement-code item, execution per `apex-meta/CODEX_EXECUTION_STANDARD.md`. Until then the schema is enforced procedurally (Meta Ops checks the fields before presenting a mutation for confirmation).
