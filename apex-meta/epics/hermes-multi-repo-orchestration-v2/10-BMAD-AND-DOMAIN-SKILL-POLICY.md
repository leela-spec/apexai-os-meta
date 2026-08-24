# 10 — BMAD and Domain-Skill Placement Policy

Status: **D06 VERIFIED / POLICY READY**  
Date: 2026-08-24

## Decision

Do not force all AI capabilities into a global shared layer.

Use three classes:

```text
CLASS A — project framework/state
  install in each repo that actually needs it

CLASS B — project/domain-specific skills
  keep in that repo

CLASS C — genuinely generic reviewed procedures
  eligible for Apex shared-skill promotion
```

Current decisions:

- **BMAD:** project-local in every repo that actually uses BMAD.
- **MarketingSkills:** MasterOfArts only for now.
- **Apex KB:** Apex repo-local.
- **future Investment skills:** Investment repo-local unless later generalized.
- **future ACIM/site skills:** ACIM repo-local unless later generalized.
- **Apex shared skills:** only independently reviewed generic procedures.

## BMAD — verified placement

Current official BMAD installation documentation says:

```bash
npx bmad-method install
```

and the installer asks for an installation directory that defaults to the current working directory. Non-interactive install explicitly supports:

```bash
npx bmad-method install --directory /path/to/project ...
```

BMAD project workflows produce/use project-local `_bmad/` and `_bmad-output/` structures.

Source:
- https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/install-bmad.md
- https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md

### Global BMAD is not production-proven

Open upstream issue #1728 proposes:

```text
--global
bmad-link
bmad-unlink
```

precisely because duplicated per-project installation is a current pain point. The feature remains an **open proposal**, not an installed capability we can rely on.

Source:
https://github.com/bmad-code-org/BMAD-METHOD/issues/1728

Therefore:

```text
DO NOT invent a global BMAD linker.
DO NOT symlink project BMAD state through Apex based on an unmerged issue.
DO install BMAD separately when a repo actually needs BMAD.
```

### Efficiency cost

Upstream issue #1728 estimates duplicated framework files per project as a pain point. That is disk/update duplication, not a reason to compromise project isolation.

For four repos:

```text
repo needs BMAD? yes -> install/update there
repo needs BMAD? no  -> no install
```

The primary token cost comes when BMAD skills/workflows are activated, not from simply having a Git directory in another repo.

### BMAD desired-state record in Apex

Apex may record:

```yaml
project_id: investment
bmad:
  required: true
  installation: repo_local
  modules:
    - bmm
  installed_version: ...
  verified_at: ...
```

Apex does not own/copy Investment's `_bmad` runtime/project state.

## MarketingSkills — current scope MasterOfArts only

Current official MarketingSkills v2 installation supports universal Agent Skills under `.agents/skills/`, Claude-specific install, plugin install, clone/copy, submodule, and SkillKit.

It also moved the product-marketing context to:

```text
.agents/product-marketing.md
```

Source:
https://github.com/coreyhaines31/marketingskills/blob/main/README.md

### v2 policy

```text
MasterOfArts
  MarketingSkills = YES
  product context = MasterOfArts-local

ACIM
  MarketingSkills = NO for now

Investment
  MarketingSkills = NO

Apex
  MarketingSkills = NO
```

Do not install a marketing corpus globally simply because one role profile called `marketing-executive` exists.

If a future repo gets a real marketing workstream, separately decide whether to install:

```text
all MarketingSkills
OR selected skills only
OR no MarketingSkills
```

The upstream CLI supports selected-skill installation, so future scope can stay narrow.

## Why domain skill siloing is healthy

A skill library affects:

- discoverable skill metadata;
- activation choices;
- maintenance/update surface;
- possible tool/environment requirements;
- potential self-modification surface;
- project terminology and assumptions.

Therefore a skill should not be globally available merely because it technically can be.

### User story — MarketingSkills

```text
MasterOfArts task:
  marketing-executive
    -> MasterOfArts project context
    -> MarketingSkills
    -> .agents/product-marketing.md

Investment task:
  research-strategist
    -> Investment project context
    -> Investment skills
    -> no MarketingSkills metadata/no marketing activation
```

This is more efficient and less contaminating than one enormous universal skill catalog.

## Apex KB

The live Apex root `AGENTS.md` currently instructs agents to use:

```text
.claude/skills/apex-kb/SKILL.md
```

for Apex KB operations.

Hermes project-local discovery natively recognizes:

```text
<repo>/.hermes/skills/
<repo>/.agents/skills/
```

after project trust.

Therefore Apex onboarding requires a deliberate interoperability decision:

### Preferred goal

One authoritative Apex-KB skill source that can be consumed by the AI clients we actually use without maintaining behaviorally divergent copies.

### Acceptable implementation classes

1. move/re-home the authoritative skill into `.agents/skills/apex-kb/` **only after** verifying Claude Code/Codex/Hermes compatibility and adjusting existing Apex AGENTS references;
2. retain `.claude/skills/apex-kb/` as source and use a deterministic generated/symlinked adapter if every target runtime supports the mechanism reliably;
3. package a compatible Hermes project-local skill separately only if exact semantic equivalence is tested and source ownership remains explicit.

Do not silently copy the skill and let two versions drift.

This interoperability work deserves its own implementation gate because Apex-KB is project-specific and important.

## Generic shared skills — high bar

A procedure becomes Apex-shared only when all are true:

```yaml
generalizable: true
used_or_needed_across_multiple_projects_or_roles: true
contains_project_facts: false
contains_secrets: false
trigger_is_clear: true
verification_is_defined: true
overlap_checked: true
reviewed: true
```

Examples likely eligible:

```text
source-authority-check
exact-match-patch-generation
research-evidence-verification
context-handover-checkpointing
```

Examples not eligible:

```text
Apex-KB control process
ACIM canonical-content pipeline
Investment IPOS method
MasterOfArts product positioning
```

unless they are deliberately generalized into a new procedure with the original project facts removed.

## Skill precedence and collision risk

Hermes supports:

```text
project-local skills > profile-local skills > external shared skills
```

This is useful because a project may deliberately override a generic method.

But same-name collisions should be explicit in the Apex registry:

```yaml
skill_name: source-verification
shared_version: 1.2.0
project_overrides:
  - project: investment
    reason: financial-evidence requirements are stricter
```

Do not create accidental same-name shadowing.

## Cross-client portability

The Agent Skills standard provides the best current common denominator for reusable procedure directories, but client discovery paths differ.

### Hermes

Supports `.agents/skills`, `.hermes/skills`, profile-local skills and external dirs.

### Claude Code

MarketingSkills' official installer explicitly distinguishes `.claude/skills/` from universal `.agents/skills/`; agent/tool-specific installation must be verified rather than assumed.

### Codex

Do not claim every Agent Skill path is automatically consumed by Codex without checking the current Codex feature/tool integration at implementation time.

### Policy

```text
canonical procedure format = Agent Skills where feasible
runtime adapter/install     = explicit per client
canonical source            = one owner
```

Do not compromise one-source authority to chase identical folder layouts across every CLI.

## Version/update process

Third-party domain frameworks:

```text
verify upstream release/docs
  -> update one target repo
  -> run that repo's acceptance test
  -> record version in Apex desired-state registry
  -> update another repo later only if it independently uses the framework
```

Do not mass-update every repo because one upstream dependency changed.

## Acceptance tests

### BMAD

For each repo using BMAD:

- [ ] `npx bmad-method install` current official path verified;
- [ ] exact module selection recorded;
- [ ] tool/client target recorded;
- [ ] project-local `_bmad` / output behavior verified;
- [ ] basic `bmad-help` / chosen workflow works from that repo;
- [ ] no dependency on unmerged global-link feature;
- [ ] update path tested before enabling unattended updates.

### MarketingSkills

MasterOfArts only:

- [ ] installed version/source recorded;
- [ ] only actually useful skill set retained if all 49 are unnecessary;
- [ ] `.agents/product-marketing.md` remains MasterOfArts-specific;
- [ ] no other repo gets MarketingSkills by shared-profile accident.

### Apex KB

- [ ] identify one authoritative Apex-KB skill source;
- [ ] test current Claude Code behavior;
- [ ] test Hermes project-local discovery;
- [ ] test Codex behavior separately;
- [ ] choose one-source/adapters without content drift;
- [ ] root AGENTS references current authoritative path.

## Primary sources

- BMAD install: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/install-bmad.md
- BMAD README/CI install: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md
- BMAD global-link proposal #1728: https://github.com/bmad-code-org/BMAD-METHOD/issues/1728
- BMAD command reference: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/reference/commands.md
- MarketingSkills README: https://github.com/coreyhaines31/marketingskills/blob/main/README.md
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Agent Skills specification: https://agentskills.io/specification
