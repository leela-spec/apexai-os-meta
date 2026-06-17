Yes — your updated understanding is **mostly correct**, with one important correction:

> **Claude Code and Hermes can both run against the same GitHub repo / local clone, but they do not store their own runtime state in the same places.**  
> The repo is the shared work surface. `.claude/` and `~/.hermes/` / Hermes profiles are runtime-specific control layers.

# 1. Where does Claude save files?

Claude Code reads and writes in two broad places.

## A. Project-scoped Claude files inside the repo

Claude Code reads instructions, settings, skills, subagents, rules, workflows, and memory from the project directory and from `~/.claude`. Project-scoped files live in the repo under `.claude/`, while global personal config lives in `~/.claude`; on Windows, `~/.claude` resolves to `%USERPROFILE%\.claude`.

Typical project repo:

```
project-leela/├── CLAUDE.md├── .claude/│   ├── skills/│   │   └── flow-recap/│   │       └── SKILL.md│   ├── agents/│   │   └── reviewer.md│   ├── settings.json│   ├── rules/│   └── workflows/├── .apex/│   ├── status/│   ├── flows/│   ├── planning/│   └── learning/└── actual_project_files/
```

These can be committed to GitHub.

## B. Personal Claude runtime files outside the repo

Claude also uses:

```
~/.claude/
```

for global/user config, transcripts, prompt history, file snapshots, caches, logs, plugins, etc. Claude’s docs explicitly distinguish committed project files from personal/global config and data.

So:

```
claude_repo_files:  committed:    - CLAUDE.md    - .claude/skills/    - .claude/agents/    - .claude/settings.json    - .claude/rules/    - .apex/claude_personal_files:  not_committed:    - ~/.claude/    - transcripts    - prompt_history    - caches    - logs    - personal_settings
```

# 2. Where does Hermes save files?

Hermes has its own home/profile structure. A Hermes profile is a separate Hermes home directory with its own `config.yaml`, `.env`, `SOUL.md`, memories, sessions, skills, cron jobs, and state database.

Typical Hermes runtime on VPS:

```
~/.hermes/├── config.yaml├── .env├── SOUL.md├── skills/├── memories/├── cron/├── sessions/├── state.db└── profiles/    ├── alfred/    │   ├── config.yaml    │   ├── .env    │   ├── SOUL.md    │   ├── skills/    │   ├── memories/    │   ├── cron/    │   └── state.db    └── meta-ops/        └── ...
```

Important:

```
hermes_profile_state:  usually_not_in_project_repo:    - state.db    - sessions    - memory    - .env    - logs    - auth    - gateway statehermes_project_work:  can_happen_inside_repo_clone:    - reading project files    - writing .apex artifacts    - applying patches    - updating status packets    - producing recaps
```

So Hermes should have:

```
/home/lex/repos/project-leela/
```

as a cloned repo **plus**:

```
~/.hermes/
```

as its runtime state.

# 3. Can Claude and Hermes both run on the same repo?

Yes, but with discipline.

## Local laptop

```
C:\Users\Lex\repos\project-leela\
```

Claude Code works here.

## VPS

```
/home/lex/repos/project-leela/
```

Hermes works here.

## GitHub

```
github.com/lex/project-leela
```

is the synchronization source.

The flow:

```
local_claude:  reads:    - project files    - CLAUDE.md    - .claude/skills    - .apex/planning  writes:    - project artifacts    - raw_flow_dump.md    - commits to feature branchgithub:  stores:    - canonical repo state    - branches    - PRshermes_vps:  pulls:    - latest repo state  reads:    - .apex/raw dumps    - .apex/status    - skills/specs  writes:    - .apex/recaps    - .apex/status updates    - bot branches / PRs
```

This is safe if you do **not** let both write to the same branch/file at the same time.

Recommended rule:

```
git_rule:  main: protected  claude_code: works_on_feature_branches  hermes: works_on_bot_branches  merge: human_review_or_explicit_gate
```

# 4. What is actually shared?

The shared substrate is not the Claude runtime and not the Hermes runtime.

The shared substrate is:

```
GitHub repo files
```

Specifically:

```
project-repo/├── CLAUDE.md├── AGENTS.md├── .claude/│   └── skills/├── .apex/│   ├── planning/│   ├── flows/│   ├── recaps/│   ├── status/│   └── learning/└── project files
```

And in the meta repo:

```
apex-orchestration/├── skills-common/│   ├── flow-recap/│   │   └── SKILL.md│   ├── precap-next-day/│   │   └── SKILL.md│   └── status-merge/│       └── SKILL.md├── specs/├── schemas/├── templates/├── adapters/└── evals/
```

The Agent Skills spec itself supports the idea that skills are portable folders: a skill is a folder with `SKILL.md`, plus optional `scripts/`, `references/`, and `assets/`. Claude Code supports `SKILL.md` skills and discovers them from user/project filesystem locations. Claude Code also states that its skills follow the open Agent Skills standard, while adding Claude-specific extensions like invocation control, subagent execution, and dynamic context injection.

This means:

```
shared_skill_core:  real: true  stable_enough_for_v1: yesshared_runtime_state:  real: false  do_not_attempt: true
```

# 5. Does each system have its own folders?

Yes.

## Claude-specific folders

```
project-repo/.claude/~/.claude/
```

## Hermes-specific folders

```
~/.hermes/~/.hermes/profiles/<profile>/
```

## Shared project/system folders

```
project-repo/.apex/apex-orchestration/skills-common/apex-orchestration/specs/apex-orchestration/schemas/
```

The correct model is:

```
runtime_specific:  claude:    - .claude/    - ~/.claude/  hermes:    - ~/.hermes/    - ~/.hermes/profiles/shared:  - .apex/  - skills-common/  - specs/  - schemas/  - templates/
```

# 6. Is “translation from one system to the other” realistic?

Yes — but phrase it more precisely.

Do not translate **Claude runtime state** into **Hermes runtime state**.

Translate **canonical Apex specs** into both runtime-specific views.

## Better than “Claude → Hermes”

```
best_pattern:  source: apex canonical spec  render_to:    - claude files    - hermes files
```

## Acceptable but weaker

```
weaker_pattern:  source: claude files  render_to:    - hermes files
```

The weaker pattern works if Claude is your authoring environment, but it risks making `.claude/` the real source of truth. I would avoid that. Make `apex-orchestration/` the source of truth.

# 7. Could this become its own skill?

Yes, but split it into two pieces.

## A. Skill: “translation brain”

This is a `SKILL.md` that tells Claude or Hermes how to reason about translation.

Example:

```
skills-common/apex-runtime-adapter/└── SKILL.md
```

Purpose:

```
apex_runtime_adapter_skill:  use_when:    - updating Claude/Hermes runtime files from Apex specs    - checking whether a skill is portable    - deciding whether a process maps to skill, cron, Kanban, or profile  does:    - reads canonical specs    - explains mapping    - proposes changed files    - validates against rules
```

## B. Script: deterministic file transformation

This is actual code:

```
adapters/├── render_claude.py├── render_hermes.py├── validate_skills.py├── validate_paths.py└── promote_learning.py
```

Purpose:

```
adapter_scripts:  render_claude:    input: skills-common/    output: project/.claude/skills/  render_hermes:    input: skills-common/    output: hermes_runtime/skills/ or ~/.hermes/skills/  validate:    input:      - SKILL.md frontmatter      - schemas      - generated manifests    output:      - pass/fail      - diff summary
```

The skill can guide and call the script, but the script should perform the actual repeatable transformation.

# 8. Can Hermes run a cron job that checks for updates and translates them?

Yes, conceptually. But do it in stages.

Hermes supports scheduled automation and has its own learning loop; the docs describe Hermes as self-improving and capable of creating/improving skills from experience. But automatic self-modification of runtime infrastructure is high-risk. Do not let Hermes silently rewrite its own core skills or profiles on `main`.

## Safe v1 cron

```
cron_job:  name: check-apex-updates  cadence: daily  mode: no_or_low_llm  actions:    - git fetch    - detect changes in apex-orchestration/specs    - detect changes in skills-common    - run validate_skills.py    - generate diff report    - notify operator  does_not:    - auto-apply changes    - auto-edit ~/.hermes    - auto-promote learning
```

## v2 cron

```
cron_job:  name: render-runtime-views  cadence: daily  actions:    - git pull apex-orchestration    - run render_claude.py    - run render_hermes.py    - create bot branch    - commit generated files    - open PR or write review report
```

## v3 cron

```
cron_job:  name: promote-approved-learning  cadence: weekly  actions:    - read approved learning candidates    - update canonical specs    - regenerate runtime views    - run evals    - open PR  requires:    - operator approval    - tests passing    - no direct main push
```

So yes, “that’s basically just a script” — **but only the mechanical transformation is just a script**. The governance around what is allowed to change is the hard part.

# 9. Could there be a community plugin?

Possibly later, but I would not assume it exists now.

What is established:

```
established:  - SKILL.md standard  - Claude filesystem skill loading  - Hermes profile directories  - Hermes skills  - GitHub as shared repo substrate
```

What is not yet established as a mature off-the-shelf solution:

```
not_established:  - full Claude-to-Hermes runtime migration  - automatic Claude subagent to Hermes profile conversion  - automatic Claude hooks to Hermes cron conversion  - safe universal self-learning promotion across runtimes
```

A future community plugin might do:

```
possible_plugin:  name: claude-hermes-sync  functions:    - copy compatible SKILL.md folders    - validate frontmatter    - strip Claude-only metadata for Hermes    - generate Hermes skill manifests    - generate Claude skill copies
```

But I would treat that as convenience, not architecture.

# 10. The exact architecture I would use

```
GitHub└── apex-orchestration/    ├── skills-common/    │   ├── flow-recap/    │   ├── precap-next-day/    │   └── status-merge/    ├── specs/    │   ├── role-specs/    │   ├── process-specs/    │   └── artifact-contracts/    ├── adapters/    │   ├── render_claude.py    │   ├── render_hermes.py    │   └── validate.py    └── generated/        ├── claude/        └── hermes/
```

Then project repo:

```
project-leela/├── CLAUDE.md├── AGENTS.md├── .claude/│   └── skills/├── .apex/│   ├── planning/│   ├── flows/│   │   ├── planned/│   │   ├── raw/│   │   └── recaps/│   ├── status/│   └── learning/└── actual app files
```

Hermes VPS:

```
/home/lex/repos/├── apex-orchestration/├── project-leela/├── project-master-of-arts/└── project-investment/~/.hermes/├── profiles/├── skills/├── cron/├── memories/└── state.db
```

# 11. What happens in a real update cycle?

## You improve a skill locally with Claude

```
step_1:  actor: Claude Code  location: laptop  edits:    - apex-orchestration/skills-common/flow-recap/SKILL.md    - apex-orchestration/schemas/flow-recap.schema.yaml  commits:    - branch: feat/improve-flow-recap
```

## GitHub receives PR

```
step_2:  actor: GitHub  role:    - stores diff    - runs validation    - protects main
```

## Hermes detects new approved update

```
step_3:  actor: Hermes cron  location: VPS  actions:    - git pull apex-orchestration    - run adapter validation    - generate Hermes runtime copy    - produce report
```

## Hermes runtime gets updated

```
step_4:  actor: adapter script  output:    - ~/.hermes/skills/flow-recap/SKILL.md  gate:    - only after approved merge or explicit operator command
```

## Project repos receive updated Claude skill copy

```
step_5:  actor: adapter script  output:    - project-leela/.claude/skills/flow-recap/SKILL.md    - project-master-of-arts/.claude/skills/flow-recap/SKILL.md
```

# 12. Final answer to your current hypothesis

Your hypothesis:

> We can let both run on the same repo, each has its own folders, and we can create translation from one system to the other, maybe as a skill/script/cron.

Verdict:

```
verdict:  both_run_on_same_repo:    answer: yes    caveat: use Git branches and do not write same files concurrently  claude_has_own_folders:    answer: yes    folders:      - project/.claude/      - ~/.claude/  hermes_has_own_folders:    answer: yes    folders:      - ~/.hermes/      - ~/.hermes/profiles/  shared_files:    answer: yes    folders:      - .apex/      - skills-common/      - specs/      - schemas/  translation_possible:    answer: yes    best_direction: canonical Apex spec -> Claude view + Hermes view    weaker_direction: Claude -> Hermes  can_be_a_skill:    answer: yes_for_reasoning_and_guidance    caveat: deterministic scripts should do actual file rendering  can_be_a_cron:    answer: yes    caveat: start with report-only cron, then PR-generating cron, then controlled apply  community_plugin:    answer: possible_later    caveat: do_not_depend_on_it_now
```

The safest next implementation target is:

```
next_build:  1_create:    - apex-orchestration/skills-common/flow-recap/SKILL.md    - adapters/validate_skills.py    - adapters/sync_to_claude.py    - adapters/sync_to_hermes.py  2_test:    - copy flow-recap to .claude/skills/    - copy flow-recap to ~/.hermes/skills/    - run same raw-flow-dump input in both systems    - compare outputs  3_only_then:    - add cron-based update detection    - add bot PR flow    - add learning promotion
```

The core architecture is viable. The critical rule is: **GitHub owns the truth; Claude and Hermes own their runtime folders; adapters copy/render validated truth into each runtime.**