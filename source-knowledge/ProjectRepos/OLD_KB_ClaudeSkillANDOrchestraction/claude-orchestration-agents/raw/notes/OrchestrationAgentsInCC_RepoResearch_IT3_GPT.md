
## 0. Verification limits

GitHub’s public HTML usually exposes **rounded** stars/forks, not exact integers. I therefore report displayed values like “61.7k” rather than pretending to know exact counts. Some GitHub pages also did not expose a clean last-commit date in the retrieved view; those are marked **unverified** rather than guessed.

---

# 1. Q&A decision flow

|#|Decision question|Why it matters|Options|Recommendation|Confidence|What was / remains to verify|
|--:|---|---|---|---|---|---|
|1|Should Apex prioritize Claude-native repos over general agent frameworks?|Apex is Claude Code + file-native, not a generic SDK platform.|A: Claude-native first / B: general frameworks equal / C: framework-first|**A**|High|Verified `.claude` paths and Claude Code claims.|
|2|Should curated indexes be cloned or read only?|Index repos are discovery hubs, not durable source architecture.|A: clone full / B: read only / C: ignore|**B** for `awesome-claude-code`|High|It describes itself as a curated list of skills, hooks, commands, apps/plugins, and orchestrators, not a standalone architecture. ([GitHub](https://github.com/hesreallyhim/awesome-claude-code "GitHub - hesreallyhim/awesome-claude-code: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic · GitHub"))|
|3|Should `shanraisshan/claude-code-best-practice` be first-batch?|It has actual `.claude` implementation folders.|A: must clone / B: read only / C: defer|**A**|High|`.claude/agents`, `commands`, `hooks`, `rules`, and `skills` were visible in the repo tree. ([GitHub](https://github.com/shanraisshan/claude-code-best-practice/tree/main/.claude "claude-code-best-practice/.claude at main · shanraisshan/claude-code-best-practice · GitHub"))|
|4|Should BMAD be copied structurally or studied as workflow grammar?|BMAD is strong but can overfit Apex toward agile-dev methodology.|A: copy wholesale / B: study + adapt / C: avoid|**B**|High|Current main tree/stats verified; old `bmad-core` path claims are partly stale/inconsistent. ([GitHub](https://github.com/bmad-code-org/BMAD-METHOD "GitHub - bmad-code-org/BMAD-METHOD: Breakthrough Method for Agile Ai Driven Development · GitHub"))|
|5|Should Apex clone plugin/skill libraries?|Large libraries create token noise unless mined narrowly.|A: full clone / B: sparse clone / C: ignore|**B**|Medium|`claude-code-plugins-plus-skills` has large catalog counts and MIT license, but quantity is a noise risk. ([GitHub](https://github.com/jeremylongshore/claude-code-plugins-plus-skills "GitHub - jeremylongshore/claude-code-plugins-plus-skills: 425 plugins, 2,810 skills, 200 agents for Claude Code. Open-source marketplace at tonsofskills.com with the ccpi CLI package manager. · GitHub"))|
|6|Should personal-OS repos be considered despite lower maturity?|Apex is itself a personal orchestration OS.|A: include small repos / B: only high-star repos / C: ignore|**A, selectively**|Medium|`personal-os` has GOALS.md/AGENTS.md/setup flow evidence, but exact stats/license remain unverified in this run. ([GitHub](https://github.com/amanaiproduct/personal-os?utm_source=chatgpt.com "GitHub - amanaiproduct/personal-os: Framework for a local AI agent ..."))|
|7|Should Apex import many subagent collections?|Subagent libraries can bloat `.claude/agents`.|A: many agents / B: 5–10 exemplars / C: none|**B**|High|`iannuttall/claude-agents` is small and template-like; better than large random agent packs. ([GitHub](https://github.com/iannuttall/claude-agents?utm_source=chatgpt.com "GitHub - iannuttall/claude-agents: Custom subagents to use with Claude ..."))|
|8|Should Aider be included?|Its repo-map and atomic Git discipline are useful, but it is not an Apex orchestration model.|A: clone full / B: read docs/code excerpts / C: avoid|**B**|High|Repo-map and auto-commit behavior are relevant; full codebase is not. ([GitHub](https://github.com/Aider-AI/aider?utm_source=chatgpt.com "GitHub - Aider-AI/aider: aider is AI pair programming in your terminal"))|
|9|Should SWE-agent be included?|Useful for agent-computer-interface and issue→fix→validate patterns, but not daily Apex flow.|A: clone full / B: read only / C: avoid|**B**|High|The repo itself says most active development has moved to mini-SWE-agent. ([GitHub](https://github.com/SWE-agent/SWE-agent "GitHub - SWE-agent/SWE-agent: SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] · GitHub"))|
|10|Should OpenHands be included?|It is large, moving, platform-oriented, and not file-native.|A: clone / B: architecture reference / C: avoid for now|**C/B**|High|Current docs indicate source code has moved into other OpenHands repos and Cloud/enterprise context is prominent. ([GitHub](https://github.com/OpenHands/OpenHands?utm_source=chatgpt.com "GitHub - OpenHands/OpenHands: OpenHands: AI-Driven Development"))|
|11|Should CrewAI be included?|SDK-heavy crew/flow abstractions can distort Apex away from local files.|A: clone / B: read only / C: avoid|**C**, maybe B later|High|CrewAI is a Python framework with crews/flows/control-plane logic, not a Claude-native file system. ([GitHub](https://github.com/crewAIInc/crewAI "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub"))|
|12|Should `BMAD-AT-CLAUDE` be used?|It may contain Claude-specific BMAD adaptations, but it is derivative and stale.|A: clone early / B: defer / C: ignore|**B**|Medium|It is a fork with 239 stars/18 forks and latest commit about 11 months ago. ([GitHub](https://github.com/24601/BMAD-AT-CLAUDE/blob/main/bmad-core/user-guide.md?utm_source=chatgpt.com "BMAD-AT-CLAUDE/bmad-core/user-guide.md at main · 24601/BMAD ... - GitHub"))|
|13|Should `agentic-os` be first-batch?|It may be conceptually close, but file tree was not deeply verified.|A: first-batch / B: read only first / C: avoid|**B**|Medium|Search evidence says Claude Code/Codex/OpenClaw compatible and skills-based, but exact tree/stats need direct verification. ([GitHub](https://github.com/itseffi/agentic-os?utm_source=chatgpt.com "GitHub - itseffi/agentic-os: Agentic personal OS to automate high ..."))|
|14|Should we download whole repos or selected folders?|Whole repo ingestion can waste tokens.|A: whole clone all / B: sparse checkout / C: README only|**B**|High|Use sparse checkout for `.claude`, docs, templates, agents, workflows.|
|15|What qualifies as “copyable”?|Apex needs files/templates, not just claims.|A: README claim / B: real path + reusable file / C: popularity|**B**|High|Example: `shanraisshan` real `.claude` paths are verified; BMAD old `bmad-core` paths are not cleanly verified on current main.|
|16|What freshness threshold should matter?|Claude Code patterns are moving quickly.|A: <90 days / B: <12 months / C: timeless only|**A for Claude-specific repos; B for stable concepts**|Medium|BMAD current release v6.9.0 was visible as Jun 22, 2026; stale forks should be deferred. ([GitHub](https://github.com/bmad-code-org/BMAD-METHOD "GitHub - bmad-code-org/BMAD-METHOD: Breakthrough Method for Agile Ai Driven Development · GitHub"))|
|17|Should Apex use official Claude docs as baseline?|Repos should not override product reality.|A: yes / B: repos only / C: no|**A**|High|Official docs describe `.claude` as the place for instructions, settings, hooks, skills, commands, subagents, workflows, rules, and memory. ([Claude](https://code.claude.com/docs/en/claude-directory?utm_source=chatgpt.com "Explore the .claude directory - Claude Code Docs"))|
|18|Should Apex treat setup scripts as executable?|Supply-chain risk is real.|A: run scripts / B: inspect only first / C: never use scripts|**B**|High|Recent public reporting describes repo-based attacks against AI coding agents; treat all cloned code as untrusted until inspected. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness?utm_source=chatgpt.com "AI coding agents can be tricked into installing malware via 'clean' GitHub repositories - Mozilla's 0din team shows how Claude Code can be exploited by its own helpfulness"))|
|19|Should Apex optimize for maximum coverage or small high-signal corpus?|KB quality depends on avoiding source sprawl.|A: maximal library / B: small curated corpus / C: no external repos|**B**|High|First batch should be 3–5 repos, not 15.|
|20|Should general multi-agent orchestration frameworks shape Apex architecture?|They may introduce hidden runtime assumptions.|A: yes / B: only narrow patterns / C: no|**B/C**|High|Use them only for vocabulary/routing examples, not as local architecture foundation.|

---

# 2. Corrected repo decision table

|Repo|Verified status|Category|Clone/download decision|Apex component fit|Copyable patterns|Noise risk|Freshness risk|Verdict|
|---|---|---|---|---|---|---|---|---|
|`shanraisshan/claude-code-best-practice`|Displayed 61.7k stars / 6.2k forks; MIT license visible; `.claude`, `CLAUDE.md`, `implementation`, `orchestration-workflow`, `best-practice` visible. Exact last commit date not captured. ([GitHub](https://github.com/shanraisshan/claude-code-best-practice "GitHub - shanraisshan/claude-code-best-practice: from vibe coding to agentic engineering - practice makes claude perfect · GitHub"))|Claude Code layout/reference|**Must clone and study**|Apex KB, Plan, Session, PromptPack, Claude-native control plane|`.claude/agents`, `.claude/commands`, `.claude/rules`, `.claude/skills`, Command→Agent→Skill chain|Low-medium|Low|**Best first clone.**|
|`bmad-code-org/BMAD-METHOD`|Displayed 49.9k stars / 5.7k forks; MIT; 1,956 commits; release v6.9.0 on Jun 22, 2026; current root shows docs/src/tools/web-bundles. ([GitHub](https://github.com/bmad-code-org/BMAD-METHOD "GitHub - bmad-code-org/BMAD-METHOD: Breakthrough Method for Agile Ai Driven Development · GitHub"))|Agentic agile workflow methodology|**Must clone and study, but not blindly copy old tree claims**|Apex Plan, FlowRecap, Weekly Workflow, PromptPack|Orchestrator/role/team/story/task workflow grammar|Medium|Low|**Strong, but adapt surgically.**|
|`hesreallyhim/awesome-claude-code`|Displayed 47.6k stars / 4.2k forks in search result; curated list of Claude Code skills/hooks/commands/orchestrators/apps/plugins. ([GitHub](https://github.com/hesreallyhim/awesome-claude-code?utm_source=chatgpt.com "GitHub - hesreallyhim/awesome-claude-code: A curated list of awesome ..."))|Curated index|**Read-only reference**|Apex KB source discovery|Discovery map only|Low if read-only; high if ingested wholesale|Medium|**Do not full-ingest.**|
|`jeremylongshore/claude-code-plugins-plus-skills`|MIT; version 4.33.0 last updated 2026-05-25; page reports hundreds of plugins, thousands of skills, hundreds of agents, with inconsistent live counts across sections. ([GitHub](https://github.com/jeremylongshore/claude-code-plugins-plus-skills "GitHub - jeremylongshore/claude-code-plugins-plus-skills: 425 plugins, 2,810 skills, 200 agents for Claude Code. Open-source marketplace at tonsofskills.com with the ccpi CLI package manager. · GitHub"))|Claude plugin/skill/agent marketplace|**Clone selectively**|Apex KB, Session, PromptPack|Skill metadata, marketplace validation, installer/catalog patterns|High|Low-medium|**Mine, do not ingest whole catalog.**|
|`amanaiproduct/personal-os`|README evidence for `setup.sh`, workspace setup, generated `GOALS.md`, Claude Code use via `AGENTS.md`; exact stars/forks/license not verified. ([GitHub](https://github.com/amanaiproduct/personal-os?utm_source=chatgpt.com "GitHub - amanaiproduct/personal-os: Framework for a local AI agent ..."))|Personal AI OS|**Clone selectively**|Weekly Workflow, Apex Plan, Apex KB|GOALS.md + AGENTS.md + setup questionnaire pattern|Low|Medium|**High conceptual fit despite low maturity.**|
|`iannuttall/claude-agents`|Displayed 2.1k stars / 274 forks; MIT; seven-agent set reported. ([GitHub](https://github.com/iannuttall/claude-agents?utm_source=chatgpt.com "GitHub - iannuttall/claude-agents: Custom subagents to use with Claude ..."))|Minimal Claude subagents|**Clone selectively**|Apex Session, Meta roles|Clean `.claude/agents` install/template pattern|Low|Medium|**Good small template source.**|
|`24601/BMAD-AT-CLAUDE`|Fork of BMAD; displayed 239 stars / 18 forks; latest commit about 11 months; paths include `bmad-core`, `agents`, `agent-teams`, `dist`, `docs`. ([GitHub](https://github.com/24601/BMAD-AT-CLAUDE/blob/main/bmad-core/user-guide.md?utm_source=chatgpt.com "BMAD-AT-CLAUDE/bmad-core/user-guide.md at main · 24601/BMAD ... - GitHub"))|BMAD Claude adaptation|**Defer / inspect only after BMAD**|Apex Plan, Session|Claude-specific BMAD adaptation clues|Medium|High|**Derivative and stale.**|
|`itseffi/agentic-os`|Evidence says it targets Claude Code/Codex/Pi/OpenClaw and uses Agent Skills/subagents; exact stats/license/tree not fully verified. ([GitHub](https://github.com/itseffi/agentic-os?utm_source=chatgpt.com "GitHub - itseffi/agentic-os: Agentic personal OS to automate high ..."))|Personal agent OS|**Read-only first**|Weekly Workflow, Apex KB, Session|File-based memory/state ideas|Medium|Medium|**Potentially useful; not first-batch.**|
|`Aider-AI/aider`|Displayed 46.7k stars / 4.7k forks in source view; repo-map implementation and docs verified; auto-commit pattern verified via docs. ([GitHub](https://github.com/Aider-AI/aider?utm_source=chatgpt.com "GitHub - Aider-AI/aider: aider is AI pair programming in your terminal"))|Git-native AI coding|**Read-only reference / sparse docs**|Apex Sync, Session|Repo-map, atomic commits, rollback discipline|High if cloned full|Low|**Reference only, not Apex foundation.**|
|`princeton-nlp/SWE-agent`|MIT visible; repo says active development mostly moved to mini-SWE-agent. ([GitHub](https://github.com/SWE-agent/SWE-agent "GitHub - SWE-agent/SWE-agent: SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] · GitHub"))|Coding-agent research|**Read-only reference**|Apex Session validation, ACI|Issue→fix→validate, ACI|Medium-high|Medium|**Use conceptually, not as source corpus.**|
|`crewAIInc/crewAI`|Displayed 54.7k stars / 7.7k forks in search; MIT; active; Python framework for crews/flows/tools/orchestration. ([GitHub](https://github.com/crewAIInc/crewAI?utm_source=chatgpt.com "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing ..."))|Agent framework|**Avoid/defer**|Only abstract routing vocabulary|Crew/flow distinction|High|Low|**Too framework-heavy for Apex V1.**|
|`OpenHands/OpenHands`|Displayed ~78.7k stars / 10k forks; recent release 1.40.0 on 2026-06-26; source code has moved into other OpenHands repos; MIT except enterprise directory. ([GitHub](https://github.com/OpenHands/OpenHands?utm_source=chatgpt.com "GitHub - OpenHands/OpenHands: OpenHands: AI-Driven Development"))|Full coding-agent platform|**Avoid/defer**|Maybe sandbox/security reference later|Platform architecture, not files|Very high|Low|**Do not use as Apex KB source now.**|
|`OpenHands/extensions`|Active first-party extension registry with `.agents/skills`, `.plugin`, plugins, skills, tests, MIT. ([GitHub](https://github.com/OpenHands/extensions?utm_source=chatgpt.com "GitHub - OpenHands/extensions: Public registry for OpenHands extensions ..."))|Extension/skills registry|**Later read-only/sparse**|Apex KB, Skill package validation|Skill/extension layout|Medium|Low|**New gap-fill candidate, not first-batch.**|

---

# 3. Corrected shortlist

```yaml
shortlist:
  must_clone_and_study:
    - repo: shanraisshan/claude-code-best-practice
      why: "Most directly verified Claude Code `.claude/` layout source."
      include_paths:
        - ".claude/"
        - "CLAUDE.md"
        - "best-practice/"
        - "implementation/"
        - "orchestration-workflow/"
      exclude_paths:
        - ".git/"
        - "presentation/"
        - "reports/"
      apex_use:
        - "Claude-native file layout"
        - "Command→Agent→Skill routing"
        - "rules/skills/agents conventions"
      risk: "Do not copy all patterns blindly; map them to Apex loop artifacts."

    - repo: bmad-code-org/BMAD-METHOD
      why: "Strongest workflow/team/orchestrator grammar, but current tree differs from older report."
      include_paths:
        - "docs/"
        - "src/"
        - "tools/"
        - "web-bundles/"
        - "AGENTS.md"
        - "README.md"
      exclude_paths:
        - "website/"
        - "test/"
        - ".github/"
        - "node_modules/"
      apex_use:
        - "Plan/story/task workflow"
        - "Role-based orchestration grammar"
        - "Operator-gated execution models"
      risk: "Old `bmad-core/` path assumptions must be rechecked after clone."

  clone_selectively:
    - repo: amanaiproduct/personal-os
      why: "Closest personal-OS file grammar: GOALS.md, AGENTS.md, setup flow."
      include_paths:
        - "README.md"
        - "AGENTS.md"
        - "GOALS.md"
        - "setup.sh"
        - "templates/"
        - "workspace/"
      exclude_paths:
        - ".git/"
      apex_use:
        - "Weekly Workflow"
        - "Apex Plan"
        - "operator-facing personal OS setup"
      risk: "Low public validation; exact license/stats not verified."

    - repo: iannuttall/claude-agents
      why: "Small, low-noise agent template set."
      include_paths:
        - "agents/"
        - "README.md"
      exclude_paths:
        - ".git/"
      apex_use:
        - "Apex Session"
        - "custom subagent formatting"
      risk: "Limited scope; do not overuse agent roster."

    - repo: jeremylongshore/claude-code-plugins-plus-skills
      why: "Useful for skill/plugin metadata and validation patterns; too large for full ingest."
      include_paths:
        - "README.md"
        - "catalog or marketplace metadata if present"
        - "selected agents/"
        - "selected skills/"
      exclude_paths:
        - "bulk marketplace payloads unless specifically needed"
        - "node_modules/"
        - ".git/"
      apex_use:
        - "Apex KB"
        - "PromptPack"
        - "skill package validation"
      risk: "High token-noise from catalog size."

  read_only_reference:
    - repo: hesreallyhim/awesome-claude-code
      why: "Discovery hub, not source architecture."
      read_sections:
        - "hooks"
        - "skills"
        - "orchestrators"
        - "session management"
      apex_use:
        - "Find additional candidates later"
      risk: "Link curation can be stale."

    - repo: Aider-AI/aider
      why: "Repo-map and atomic Git commit discipline are transferable."
      read_sections:
        - "repo-map docs"
        - "commit workflow docs"
        - "selected repomap implementation"
      apex_use:
        - "Apex Sync"
        - "Apex Session"
      risk: "Full repo is coding-tool noise."

    - repo: princeton-nlp/SWE-agent
      why: "ACI / issue→fix→validate reference."
      read_sections:
        - "README"
        - "docs"
        - "mini-SWE-agent migration notes"
      apex_use:
        - "validation loop vocabulary"
      risk: "Original repo partly superseded."

    - repo: itseffi/agentic-os
      why: "Potentially relevant personal agent OS; needs deeper tree verification."
      read_sections:
        - "README"
        - "skills/"
        - "subagents/"
        - "memory/state docs"
      apex_use:
        - "future file-backed OS patterns"
      risk: "Unverified maturity."

  avoid_or_defer:
    - repo: OpenHands/OpenHands
      why: "Large platform, source moved into multiple repos, not a small Claude-native file system."
      risk: "Enterprise/platform/noise risk."

    - repo: crewAIInc/crewAI
      why: "Python SDK framework, crew/flow abstraction, not Apex’s file-native Claude layer."
      risk: "Architecture drift toward generic agent framework."

    - repo: 24601/BMAD-AT-CLAUDE
      why: "Derivative and stale compared with official BMAD; inspect only if BMAD current tree lacks Claude-specific examples."
      risk: "Stale fork risk."
```

---

# 4. Corrected source download manifest

```yaml
sources:
  - name: claude-code-best-practice
    url: https://github.com/shanraisshan/claude-code-best-practice
    type: github_repo
    decision: must_clone_and_study
    priority: 1
    verification:
      stars: "61.7k displayed"
      forks: "6.2k displayed"
      last_commit: "unverified_exact_date_from_retrieved_view"
      license: "MIT visible"
      archived: "not indicated in retrieved view"
      verified_paths:
        - ".claude/"
        - ".claude/agents/"
        - ".claude/commands/"
        - ".claude/hooks/"
        - ".claude/rules/"
        - ".claude/skills/"
        - "CLAUDE.md"
        - "best-practice/"
        - "implementation/"
        - "orchestration-workflow/"
      missing_or_unverified_paths:
        - "orchestration/ # report path appears corrected to orchestration-workflow/"
    why: "Best verified Claude-native source for `.claude` file layout and command-agent-skill routing."
    recommended_download:
      method: sparse_checkout
      include_paths:
        - ".claude/"
        - "CLAUDE.md"
        - "best-practice/"
        - "implementation/"
        - "orchestration-workflow/"
      exclude_paths:
        - ".git/"
        - "presentation/"
        - "reports/"
    apex_component_fit:
      - Apex KB
      - Apex Plan
      - Apex Session
      - Weekly Workflow
      - PromptPack
    risk_flags:
      - "copy_only_after_mapping_to_apex_loop"
    verdict: "first_batch_to_clone"

  - name: BMAD-METHOD
    url: https://github.com/bmad-code-org/BMAD-METHOD
    type: github_repo
    decision: must_clone_and_study
    priority: 1
    verification:
      stars: "49.9k displayed"
      forks: "5.7k displayed"
      last_commit: "current activity visible; latest release v6.9.0 Jun 22 2026"
      license: "MIT"
      archived: "not indicated in retrieved view"
      verified_paths:
        - "docs/"
        - "src/"
        - "tools/"
        - "web-bundles/"
        - "AGENTS.md"
        - "README.md"
        - "LICENSE"
      missing_or_unverified_paths:
        - "bmad-core/agents/ # old report claim not cleanly verified on current main"
        - "bmad-core/tasks/"
        - "bmad-core/templates/"
        - "bmad-core/workflows/"
        - ".claude/agents/"
    why: "Best workflow-methodology source for role-based planning/story/task orchestration."
    recommended_download:
      method: sparse_checkout
      include_paths:
        - "docs/"
        - "src/"
        - "tools/"
        - "web-bundles/"
        - "AGENTS.md"
        - "README.md"
      exclude_paths:
        - "website/"
        - "test/"
        - ".github/"
        - "node_modules/"
    apex_component_fit:
      - Apex Plan
      - Apex Session
      - Weekly Workflow
      - FlowRecap
      - PromptPack
    risk_flags:
      - "tree_changed_since_report"
      - "do_not_copy_bmad_core_claims_without_local_tree_check"
    verdict: "clone_and_study_as_workflow_grammar"

  - name: awesome-claude-code
    url: https://github.com/hesreallyhim/awesome-claude-code
    type: github_repo
    decision: read_only_reference
    priority: 2
    verification:
      stars: "47.6k displayed in search result"
      forks: "4.2k displayed in search result"
      last_commit: "2 months ago in search result"
      license: "unverified_exact_license_in_this_run"
      archived: "not indicated"
      verified_paths:
        - "README.md"
      missing_or_unverified_paths:
        - "all linked repo paths are external and must be independently verified"
    why: "Discovery hub for Claude Code patterns; not itself an architecture source."
    recommended_download:
      method: read_only
      include_paths:
        - "README.md"
      exclude_paths:
        - ".git/"
    apex_component_fit:
      - Apex KB
      - Apex Session
      - Apex Sync
    risk_flags:
      - "curation_only"
      - "link_rot_possible"
    verdict: "read_first_do_not_ingest"

  - name: claude-code-plugins-plus-skills
    url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills
    type: github_repo
    decision: clone_selectively
    priority: 2
    verification:
      stars: "not_reliably_captured_in_this_run"
      forks: "not_reliably_captured_in_this_run"
      last_commit: "page reports version 4.33.0 last updated 2026-05-25"
      license: "MIT"
      archived: "not indicated"
      verified_paths:
        - "README.md"
        - "catalog/marketplace claims visible"
      missing_or_unverified_paths:
        - "agents/"
        - "skills/"
        - "plugins/"
        - "workspace/lab/ORCHESTRATION-PATTERN.md"
    why: "Large skill/plugin/agent catalog; useful for metadata and installer patterns."
    recommended_download:
      method: sparse_checkout
      include_paths:
        - "README.md"
        - "selected agents/"
        - "selected skills/"
        - "selected plugins/"
        - "catalog metadata"
      exclude_paths:
        - "bulk marketplace payloads"
        - "node_modules/"
        - ".git/"
    apex_component_fit:
      - Apex KB
      - Apex Session
      - PromptPack
    risk_flags:
      - "high_catalog_noise"
      - "live_counts_inconsistent_across_page"
    verdict: "mine_after_first_batch"

  - name: personal-os
    url: https://github.com/amanaiproduct/personal-os
    type: github_repo
    decision: clone_selectively
    priority: 2
    verification:
      stars: "unverified"
      forks: "unverified"
      last_commit: "unverified"
      license: "unverified"
      archived: "not indicated in retrieved snippets"
      verified_paths:
        - "GOALS.md # README evidence"
        - "AGENTS.md # README evidence"
        - "setup.sh # README evidence"
        - "workspace/ # README evidence"
        - "templates/ # README evidence"
      missing_or_unverified_paths:
        - "exact tree still requires local clone"
    why: "Closest personal OS analogy to Apex’s operator-facing file system."
    recommended_download:
      method: sparse_checkout
      include_paths:
        - "README.md"
        - "GOALS.md"
        - "AGENTS.md"
        - "setup.sh"
        - "templates/"
        - "workspace/"
      exclude_paths:
        - ".git/"
    apex_component_fit:
      - Apex KB
      - Apex Plan
      - Weekly Workflow
    risk_flags:
      - "low_maturity_or_low_visibility"
      - "license_unverified"
    verdict: "small_selective_clone"

  - name: iannuttall-claude-agents
    url: https://github.com/iannuttall/claude-agents
    type: github_repo
    decision: clone_selectively
    priority: 2
    verification:
      stars: "2.1k displayed"
      forks: "274 displayed"
      last_commit: "unverified_exact_date"
      license: "MIT"
      archived: "not indicated"
      verified_paths:
        - "agents/ # reported in source snippets"
        - "README.md"
      missing_or_unverified_paths:
        - "exact agent filenames should be checked after clone"
    why: "Small low-noise subagent template set."
    recommended_download:
      method: github_zip
      include_paths:
        - "agents/"
        - "README.md"
      exclude_paths:
        - ".git/"
    apex_component_fit:
      - Apex Session
      - PromptPack
    risk_flags:
      - "limited_agent_scope"
    verdict: "clone_small_template_source"

  - name: aider
    url: https://github.com/Aider-AI/aider
    type: github_repo
    decision: read_only_reference
    priority: 3
    verification:
      stars: "46.7k displayed in source result"
      forks: "4.7k displayed in source result"
      last_commit: "repomap file last touched about 4 months ago in retrieved source view"
      license: "unverified_in_this_run"
      archived: "not indicated"
      verified_paths:
        - "README.md"
        - "docs/"
        - "aider/repomap.py"
      missing_or_unverified_paths:
        - "full workflow docs not fetched"
    why: "Repo-map and atomic commit discipline are transferable to Apex Sync/Session."
    recommended_download:
      method: read_only
      include_paths:
        - "docs/"
        - "README.md"
        - "aider/repomap.py"
      exclude_paths:
        - "full source tree"
        - ".git/"
    apex_component_fit:
      - Apex Sync
      - Apex Session
    risk_flags:
      - "not_orchestration_native"
      - "codebase_noise"
    verdict: "read_concepts_only"

  - name: SWE-agent
    url: https://github.com/princeton-nlp/SWE-agent
    type: github_repo
    decision: read_only_reference
    priority: 3
    verification:
      stars: "unverified_in_this_run"
      forks: "unverified_in_this_run"
      last_commit: "unverified_exact_date"
      license: "MIT"
      archived: "not indicated"
      verified_paths:
        - "README.md"
        - "docs/"
      missing_or_unverified_paths:
        - "agent-computer-interface exact files not fetched"
    why: "Useful ACI and validation-loop reference; original project partly superseded by mini-SWE-agent."
    recommended_download:
      method: read_only
      include_paths:
        - "README.md"
        - "docs/"
      exclude_paths:
        - "full sweagent source"
    apex_component_fit:
      - Apex Session
      - FlowRecap
    risk_flags:
      - "superseded_by_mini_swe_agent_for_active_development"
      - "research_coding_agent_not_daily_workflow"
    verdict: "reference_only"

  - name: agentic-os
    url: https://github.com/itseffi/agentic-os
    type: github_repo
    decision: read_only_reference
    priority: 3
    verification:
      stars: "unverified"
      forks: "unverified"
      last_commit: "unverified"
      license: "unverified"
      archived: "not indicated"
      verified_paths:
        - "README evidence for Claude Code/Codex/OpenClaw compatibility"
        - "README evidence for Agent Skills/subagents"
      missing_or_unverified_paths:
        - "skills/"
        - "evals/"
        - "subagents/"
        - "state or memory files"
    why: "Possibly relevant personal multi-agent OS; needs real tree verification first."
    recommended_download:
      method: read_only
      include_paths:
        - "README.md"
        - "docs if present"
      exclude_paths:
        - "full repo until verified"
    apex_component_fit:
      - Apex KB
      - Apex Session
      - Weekly Workflow
    risk_flags:
      - "unverified_tree"
      - "possible_runtime_drift"
    verdict: "read_only_until_verified"

  - name: BMAD-AT-CLAUDE
    url: https://github.com/24601/BMAD-AT-CLAUDE
    type: github_repo
    decision: avoid_or_defer
    priority: 4
    verification:
      stars: "239 displayed"
      forks: "18 displayed"
      last_commit: "about 11 months ago in retrieved source"
      license: "unverified"
      archived: "not indicated"
      verified_paths:
        - "bmad-core/"
        - "agents/"
        - "agent-teams/"
        - "dist/"
        - "docs/"
      missing_or_unverified_paths:
        - "current compatibility with BMAD v6 not verified"
    why: "Claude-specific derivative of BMAD, but stale compared with official BMAD."
    recommended_download:
      method: read_only
      include_paths:
        - "README.md"
        - "agents/"
        - "bmad-core/"
      exclude_paths:
        - "full repo unless official BMAD lacks needed Claude examples"
    apex_component_fit:
      - Apex Plan
      - Apex Session
    risk_flags:
      - "too_unmaintained"
      - "derivative"
    verdict: "defer"

  - name: crewAI
    url: https://github.com/crewAIInc/crewAI
    type: github_repo
    decision: avoid_or_defer
    priority: 4
    verification:
      stars: "54.7k displayed in search result"
      forks: "7.7k displayed in search result"
      last_commit: "active within hours in search result"
      license: "MIT"
      archived: "not indicated"
      verified_paths:
        - "README.md"
        - "docs/"
      missing_or_unverified_paths:
        - "not relevant to `.claude` path verification"
    why: "Python SDK framework with crews/flows; not file-native Claude Code."
    recommended_download:
      method: read_only
      include_paths:
        - "README.md"
        - "concept docs only"
      exclude_paths:
        - "full source"
    apex_component_fit:
      - "routing vocabulary only"
    risk_flags:
      - "framework_abstraction_drift"
      - "enterprise_control_plane_noise"
    verdict: "do_not_use_for_apex_v1"

  - name: OpenHands
    url: https://github.com/OpenHands/OpenHands
    type: github_repo
    decision: avoid_or_defer
    priority: 4
    verification:
      stars: "78.7k displayed in release result"
      forks: "10k displayed in release result"
      last_commit: "active; release 1.40.0 on 2026-06-26"
      license: "MIT except enterprise directory"
      archived: "not indicated"
      verified_paths:
        - "README.md"
        - "docs/"
      missing_or_unverified_paths:
        - "source moved to OpenHands/software-agent-sdk and agent-canvas"
    why: "Large platform; not a compact Claude-native orchestration source."
    recommended_download:
      method: read_only
      include_paths:
        - "selected architecture/security docs only"
      exclude_paths:
        - "full repo"
        - "cloud/server stack"
    apex_component_fit:
      - "later sandbox/security reference only"
    risk_flags:
      - "too_enterprise"
      - "source_tree_moving"
      - "high_token_noise"
    verdict: "do_not_use_for_now"
```

---

# 5. Final recommendation

```yaml
final_recommendation:
  first_batch_to_clone:
    - "shanraisshan/claude-code-best-practice"
    - "bmad-code-org/BMAD-METHOD"
    - "amanaiproduct/personal-os"
    - "iannuttall/claude-agents"

  first_batch_to_read_only:
    - "hesreallyhim/awesome-claude-code"
    - "Aider-AI/aider"
    - "princeton-nlp/SWE-agent"

  defer_until_later:
    - "jeremylongshore/claude-code-plugins-plus-skills"
    - "itseffi/agentic-os"
    - "24601/BMAD-AT-CLAUDE"
    - "OpenHands/extensions"

  do_not_use_for_now:
    - "OpenHands/OpenHands"
    - "crewAIInc/crewAI"

  recommended_next_operator_action:
    - "Create a local folder such as source-knowledge/ProjectRepos/apex-claude-orchestration-candidates/."
    - "Sparse-clone only the first four repos."
    - "Run deterministic file inventory before any LLM ingest: file tree, sizes, markdown count, path list, license file, and `.claude` path presence."
    - "Create a one-page local verification ledger before copying any patterns into Apex."
```

**Operational verdict:** clone **two foundations** first: `shanraisshan/claude-code-best-practice` for Claude-native file layout, and `bmad-code-org/BMAD-METHOD` for workflow/orchestrator grammar. Add `personal-os` and `iannuttall/claude-agents` as small, low-noise structure/template references. Everything else should be read-only or deferred until Apex has its first working Claude-native loop slice.