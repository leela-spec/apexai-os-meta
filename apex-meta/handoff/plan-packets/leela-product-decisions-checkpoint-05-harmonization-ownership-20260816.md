---
title: "Leela Product Decisions Checkpoint 05 — Harmonization Ownership"
document_role: iterative_decision_evidence_checkpoint
created: 2026-08-16
status: evidence_strongly_narrows_operator_ratification_remains
project: leela-product-decisions
qa_ids: [QA-73]
canonical_mutation_performed: false
---

# QA-73 — Is `harmonization/` a Feature or Migration Scaffolding?

## Evidence read

- prior product-decisions checkpoints
- current QA-73 ledger text
- `docs/ssot/features/index.md`
- `lib/features/harmonization/` directory
- `docs/ssot/features/sequencing/canon/30-conformance/03-current-to-target-migration-map.md`
- current Home/Skill Tree integration checkpoints

## Current repository facts

### The canonical feature catalog remains fixed at 11 feature concepts

`docs/ssot/features/index.md` lists exactly 11 feature specs plus Cross-Feature architecture.

There is no `docs/ssot/features/harmonization/spec.md` and no harmonization owner in the feature catalog.

### The runtime namespace is real and substantial

`lib/features/harmonization/` currently contains, among other things:

- `harmonization_models.dart`
- `harmonization_xp.dart`
- `harmonized_path_screen.dart`
- `harmonized_sequence_builder_screen.dart`
- `harmonized_run_screen.dart`
- `harmonized_stats_screen.dart`
- `leela_read_repository.dart`

This is why simply calling the directory "dead" would be false.

### The current migration map already assigns its semantics away from Harmonization

The normative Sequencing current-to-target migration map is explicit:

- `HarmonizationSession` is a mutable cross-feature bag that conflates authority; target is owner contracts/repositories, with the session retained only as a prototype adapter until cutover.
- `HarmonizedPathScreen` should publish/load a Path-owned `PathDemandSnapshot` and hand off by stable ID/revision.
- `harmonized_sequence_builder_screen` should consume canonical Sequencing Templates/candidates/controllers.
- `harmonized_run_screen` should be replaced/adapted to canonical accepted Instance + Run controller semantics.
- `harmonized_stats_screen` should become Stats consumption of Run facts/actual snapshots.
- `harmonization_xp.dart` is v1 compatibility policy; current scoring ownership belongs to Algorithm under the locked SSOT.
- `leela_read_repository.dart` provides a useful explicit-offline/read pattern, but target repositories are typed and owner-scoped.

Thus current architecture evidence does **not** support a coherent Harmonization domain owner.

## Strongly evidence-supported disposition

The best-fit interpretation is:

> `harmonization/` is a historical integration/prototype namespace and compatibility migration shell. Its individual responsibilities must converge into the existing named owners. The namespace may remain temporarily where adapters are still needed, but it is not a 12th product feature and should not acquire new domain authority.

This is more precise than the original QA-73 choices "12th concept / absorbed into Stats-Sequencing / archived" because different files belong to different owners.

## Operator ratification packet

User-facing question:

> Should we formally treat the current `harmonization/` package as temporary integration/migration scaffolding whose pieces are progressively moved or adapted into the existing feature owners, rather than making Harmonization its own Leela feature?

### A — Migration shell, not a feature — recommended

- keep 11-feature catalog unchanged;
- assign each semantic responsibility to its existing owner;
- permit temporary compatibility adapters under `harmonization/` while migrations are incomplete;
- prohibit new domain truth from being introduced there;
- archive/remove individual harmonization files when their replacement path is proven.

### B — Make Harmonization a 12th feature/domain

- create feature spec and owner;
- define what truth only Harmonization may mutate;
- rewrite current ownership boundaries to prevent overlap.

Evidence problem: no unique domain truth has been identified that requires this new owner; current files are a mixture of Path, Sequencing, Algorithm, Stats, run/persistence, and shared-read behavior.

### C — Archive/delete Harmonization immediately

- remove namespace now and repair every consumer in one migration.

Evidence problem: multiple current flows still compile/use these files. Immediate removal is a migration project, not a semantic answer, and risks deleting useful adapters before canonical replacements exist.

## Recommendation

**A — Migration shell, not a feature.** This matches the current fixed feature catalog and the existing migration map without inventing a new owner or pretending current runtime dependencies are already gone.

Still operator-owned because QA-73 is formally open; this checkpoint does not close it.

## Effect on current Leela Core milestone

QA-73 should **not block** the Home -> bounded Skill Tree -> confirmed scope -> frozen context milestone.

Specifically:

- `SCRSkillCluster` should stop forcing navigation to `HarmonizedPathScreen` for Home-origin scope selection regardless of QA-73;
- the first Home-origin flow returns to Home context under the canonical ScopeSelection contract;
- `SpatialRepository` may temporarily reuse `LeelaReadRepository` as an implementation adapter while its semantic outputs remain Skill Tree-owned;
- no new dependency on `HarmonizationSession` should be introduced.

## QA disposition

```yaml
qa_disposition:
  QA-73:
    classification: evidence_strongly_narrows_operator_ratification_remains
    recommended_candidate: migration_shell_not_feature
    blocks:
      - final_namespace_retirement_policy
      - formal_owner_cleanup_plan
    does_not_block:
      - Home_to_SkillTree_vertical_slice
      - origin_aware_ScopeSelection_handoff
      - bounded_cluster_primary_routing
```

## Next workstep

Consolidate the immediate Core Interaction decision blockers into the `leela-product-decisions` Apex Plan packet, then begin the stale-ledger reconciliation stream with QA-130 as the first proven example and search for additional rows already resolved by newer SSOT-D records.
