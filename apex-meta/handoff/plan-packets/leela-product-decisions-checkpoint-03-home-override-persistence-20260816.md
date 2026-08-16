---
title: "Leela Product Decisions Checkpoint 03 — Home Override Persistence"
document_role: iterative_decision_evidence_checkpoint
created: 2026-08-16
status: evidence_narrowed_operator_choice_remains
project: leela-product-decisions
qa_ids: [QA-100]
related_not_merged: [QA-131]
canonical_mutation_performed: false
---

# QA-100 — Home Scope/Duration Override Persistence

## Evidence read

- prior product-decisions checkpoints
- current `OPEN_QUESTIONS.md` / registry
- `docs/ssot/screens/home-today.md`
- `lib/main.dart`
- `lib/globals/g_s_spark.dart` from prior Home evidence pass
- current Home/Skill Tree scope integration checkpoints

## Contract truth

Home is a non-owning screen. Its local interaction state includes:

- draft scope selection
- draft maximum duration
- active mode
- selected preview tab
- hero index
- upcoming expansion

Applying scope/mode/duration narrowing must create a fresh resolution context. Home may not widen the owner-authorized time/scope or become a resolver.

The current Home screen contract deliberately does **not** state how long the user's narrowing survives.

## Current runtime behavior

`GS_Spark` is created once at the application `MultiProvider` root in `lib/main.dart`.

Therefore, absent an explicit clear/reset:

- scope/duration state survives navigation away from and back to Home;
- state can be seen by other screens using the same Provider;
- state resets when the process/provider tree is recreated;
- no evidence was found that scope/duration overrides are durably persisted to SharedPreferences/Supabase as user settings.

This is an accidental/current runtime lifetime, not an operator-ratified Home interaction contract.

Additionally, the current `GS_Spark` starts with fake seeded scope/resolved-scope values, so current behavior cannot be adopted wholesale as evidence for intended persistence.

## Relationship to QA-131

Do **not** merge QA-100 with QA-131.

- QA-100: lifetime of the user's Home request narrowing (scope/duration interaction state).
- QA-131: persistence semantics of a `ResolvedScope.containsManualOverride` flag in the older/transitional resolution DTO.

The first Home -> Skill Tree milestone is removing/quarantining `ResolvedScope` as authority, so QA-131 may later become obsolete or be re-scoped. It does not determine QA-100.

## Operator decision packet

User-facing question:

> If you narrow Home to a specific Skill Tree scope or maximum duration, how long should that narrowing remain active before Home returns to its default context?

### A — One resolution request only

- scope/duration narrowing applies to the next resolution;
- after the request/result lifecycle completes, Home returns to default current-window behavior.

**Effect:** least sticky; every new Home request starts broad unless narrowed again.

### B — Current Home visit/session — recommended candidate

- narrowing remains while the user stays in the current Home interaction session and while temporarily visiting Skill Tree/pickers to edit it;
- leaving the Home flow intentionally and returning later starts from the default context;
- not persisted as a durable user preference.

**Effect:** supports iterative browse/adjust/browse without making yesterday's filter silently control a later recommendation.

### C — Sticky until explicitly cleared

- narrowing persists across Home visits during the app/session, possibly later durable persistence if explicitly designed;
- UI requires a clear/reset affordance and visible indication that filtering remains active.

**Effect:** useful for sustained focus on one Epic/Block, but high risk of hidden stale filtering unless the active override is prominent.

### D — Durable personal default

- scope/duration becomes a saved user preference across app restarts/devices until changed.

**Effect:** turns a request parameter into profile/configuration state; requires a named persistence owner and synchronization semantics. No current evidence supports making this the default.

## Recommendation basis

**Candidate B** best fits the current screen contract's language of *draft interaction state* while preserving the practical Home -> Skill Tree -> Home editing loop.

It also avoids treating the current app-global `GS_Spark` lifetime as product truth and avoids introducing durable preference infrastructure into the first milestone.

This is a recommendation only; QA-100 remains operator-owned.

## Downstream effects after decision

- Home screen contract local-state lifecycle
- GS_Spark replacement/refactor boundary
- Home -> Skill Tree origin/return behavior
- reset/clear UI requirements
- tests for leaving/re-entering Home
- resolution-context fingerprint creation timing
- QA-100 ledger/registry and new decision record

## Planning disposition

```yaml
qa_disposition:
  QA-100:
    classification: genuinely_operator_only
    recommended_candidate: B_current_home_interaction_session
    blocks:
      - final_home_scope_state_lifecycle
    does_not_block:
      - bounded_skill_tree_runtime_verification
      - canonical_scope_contract_definition
      - removal_of_fake_seed_state
```

## Next workstep

Evidence-sweep QA-138: accessible non-spatial Skill Tree fallback. Determine what accessibility contracts, tests, and current spatial semantics actually require before proposing operator versions.
