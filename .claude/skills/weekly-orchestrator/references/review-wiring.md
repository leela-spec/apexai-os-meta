# Consequential-Packet Review

Run independent review only when a packet proposes a confirmed Apex Session project/task mutation, carries an unresolved material risk, contains a cross-project conflict, or the operator requests review. Otherwise, use the normal operator gate; do not add a review flight.

```yaml
review_procedure:
  1: Freeze the status-merge packet and declared evidence references with a basis_digest.
  2: Give independent validity and alignment reviewers the frozen basis, not each other's conclusions.
  3: Record pass, needs_revision, fail, or hold against named criteria.
  4: Treat any fail or hold as non-routable to Apex Session; preserve the proposal for operator review.
  5: Route a passing, operator-confirmed proposal to Apex Session.
```

```yaml
constraints:
  reviewers_are_read_only: true
  no_llm_tiebreak: true
  changed_packet_requires_new_review: true
  no_review_for_routine_nonconsequential_packets: true
```
