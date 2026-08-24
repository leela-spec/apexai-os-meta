# D06 Appendix — BMAD and Domain-Specific Skill Placement

**Decision status:** ACCEPTED  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject file:** `../10-BMAD-AND-DOMAIN-SKILL-POLICY.md`

## Decision

- BMAD stays project-local in every repo that actually uses it.
- MarketingSkills remains MasterOfArts-only until another repo has a demonstrated marketing requirement.
- Apex KB remains Apex-specific.
- Do not invent a global BMAD linker or globalize irrelevant domain skill libraries.

## Forces

- some skills/frameworks carry project-local state and assumptions;
- user explicitly prefers siloing where domains differ;
- BMAD's current supported installer model is project-oriented;
- a global BMAD linking feature exists as an upstream proposal rather than a proven production feature;
- unnecessary skills increase maintenance, discovery noise and potential context/selection cost.

## Placement law

```text
generic procedure used across domains
  -> candidate for D05 shared-skill layer

domain method needed in one repo
  -> keep repo/profile scoped

framework with project state
  -> install/manage in that repo
```

## Current placement

| Capability | Scope |
|---|---|
| BMAD | repo-local where actually used |
| MarketingSkills | MasterOfArts only |
| Apex KB | Apex only |
| generic source verification / patching / review procedures | potential reviewed shared skills under D05 |

## Risks

- per-repo BMAD installs duplicate files and require per-repo updates;
- separate installs can drift in version;
- Apex KB currently has client/path compatibility questions between Claude-oriented source and Hermes project-skill discovery;
- moving a domain skill into the global layer later can accidentally expose project assumptions elsewhere.

## Shortcomings

- no single-update global BMAD estate today;
- framework versions must be inventoried per participating repo;
- some method duplication is accepted in exchange for proven behavior and clear ownership.

## Rejected alternatives

1. **Custom global BMAD symlink/linker** — rejected: upstream global-link behavior is not yet proven production functionality.
2. **Install MarketingSkills everywhere** — rejected: no current need outside MasterOfArts.
3. **Move Apex KB into shared generic skills** — rejected: Apex-specific governance/procedure.

## Implementation consequence

Maintain a small capability registry in Apex recording which repos use which major framework/skill package and version. Do not synchronize package contents between repos automatically unless the upstream tool provides a supported update mechanism.

## Watch / revisit conditions

Revisit BMAD deduplication only if upstream ships a supported global/shared installation feature and it passes multi-repo rollback/version-isolation tests.

## Evidence links

- BMAD install: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/install-bmad.md
- BMAD global-link proposal #1728: https://github.com/bmad-code-org/BMAD-METHOD/issues/1728
- MarketingSkills: https://github.com/coreyhaines31/marketingskills/blob/main/README.md
- Current policy: `../10-BMAD-AND-DOMAIN-SKILL-POLICY.md`
