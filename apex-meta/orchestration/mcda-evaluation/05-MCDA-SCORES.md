# 05 — MCDA Scores and Sensitivity Analysis

Status: **desk-score complete / finalists require pilots**  
Date: **2026-08-21**

## 1. Scoring boundary

Only candidates surviving the hard-gate screen in `04-EVIDENCE-MATRIX.md` are quantitatively scored as production-core candidates:

1. **GitHub Spec Kit + built-in GitHub Issues bridge**
2. **GitHub Issues/Projects + portable Agent Skills** (complexity control)
3. **Beads**

Other candidates remain eligible as upstream methodology/skill/runtime donors but are not scored as the portfolio core because they fail one or more load-bearing hard gates against the Master of Arts scope.

## 2. Balanced-weight scores

Scale: 0–5. Weighted total is normalized to 100.

| Criterion | Weight | Spec Kit + GitHub | Evidence | GitHub control | Evidence | Beads | Evidence |
|---|---:|---:|---|---:|---|---:|---|
| C1 Proven maturity & ecosystem | 12 | 5.0 | A | 5.0 | A | 4.0 | A |
| C2 Cross-agent/client interoperability | 15 | 4.5 | B | 5.0 | A | 3.5 | B |
| C3 Durable project/task orchestration | 12 | 4.5 | B | 4.0 | A | 5.0 | A |
| C4 Human governance & review | 10 | 4.5 | B | 4.0 | B | 4.0 | B |
| C5 Skill/workflow framework quality | 10 | 5.0 | A/B | 3.0 | B | 4.0 | A/B |
| C6 Knowledge/SSOT efficiency | 10 | 4.5 | B | 3.5 | B | 4.5 | A/B |
| C7 Deterministic automation leverage | 8 | 5.0 | A | 4.5 | A | 4.5 | A |
| C8 Non-software business fit | 8 | 4.0 | B/C | 5.0 | A | 3.0 | C |
| C9 Operational simplicity | 7 | 4.0 | B | 5.0 | A | 3.0 | B |
| C10 Token/context efficiency | 5 | 4.5 | B | 3.5 | B | 5.0 | A/B |
| C11 Security/permissions | 3 | 4.0 | B | 5.0 | A | 3.5 | B |
| **Balanced total** | **100** | **91.2** |  | **86.3** |  | **80.4** |  |

## 3. Why Spec Kit currently leads

The lead is not from popularity alone. It comes from owning more of the required responsibility set without introducing a second custom subsystem:

- intent/specification artifacts;
- reusable workflows;
- deterministic shell/command steps;
- human gates;
- branching/loops/fan-out/fan-in;
- persisted workflow run state;
- resume/recovery;
- JSON output;
- overlays/extensions/presets;
- direct integrations for major local CLI agents;
- built-in task -> GitHub Issue materialization;
- GitHub remains the human/web-visible collaboration boundary.

The strongest unresolved criterion is **C8 non-software fit**. The official product now explicitly supports business processes and has at least some non-software presets, but Master of Arts is much broader than the available examples. That must be demonstrated by pilot rather than assumed.

## 4. Why GitHub-native remains dangerous to ignore

GitHub control scores **86.3/100** despite having no dedicated AI workflow engine.

Its strengths are unusually aligned with the operator/CEO side:

- directly inspectable project state;
- universal web accessibility;
- durable issue/project history;
- hierarchy, dependencies, custom metadata, boards and roadmap;
- mature permissions/auditing;
- excellent non-software neutrality;
- minimal additional infrastructure.

Its weakness is precisely why Spec Kit may add value: AI agents otherwise need to repeatedly reconstruct process logic, task packets, gates and workflow state from conventions/prompts.

If Spec Kit's pilot overhead is high or its software vocabulary feels unnatural, the control can still win.

## 5. Why Beads is third despite excellent task mechanics

Beads is stronger than both finalists at:

- agent-native dependency graphs;
- ready-work computation;
- atomic claiming;
- persistent graph relationships;
- compact JSON state;
- formulas/molecules;
- context compaction/memory decay.

But the Master of Arts decision is not "best agent issue tracker." Beads loses points because:

- official scope remains coding-agent oriented;
- non-code fit is generic rather than demonstrated;
- Dolt becomes another persistent state substrate;
- a repo-connected web agent cannot inspect the live work graph as naturally as GitHub Issues/Projects;
- a separate spec/method layer may still be needed.

This makes Beads a valuable **gap-filler finalist**, not the default core.

## 6. Sensitivity analysis

The same raw candidate scores were recalculated under four 100-point profiles.

### Profile weights

| Criterion | Balanced | Interop-first | Autonomy/reliability | Simplicity-first |
|---|---:|---:|---:|---:|
| C1 maturity | 12 | 8 | 8 | 10 |
| C2 interoperability | 15 | 22 | 12 | 12 |
| C3 durable orchestration | 12 | 11 | 18 | 10 |
| C4 governance/review | 10 | 10 | 14 | 9 |
| C5 workflow/skills | 10 | 8 | 8 | 8 |
| C6 knowledge/SSOT | 10 | 15 | 8 | 8 |
| C7 deterministic automation | 8 | 8 | 12 | 7 |
| C8 non-software fit | 8 | 6 | 6 | 7 |
| C9 simplicity | 7 | 4 | 6 | 16 |
| C10 context efficiency | 5 | 5 | 5 | 10 |
| C11 security | 3 | 3 | 3 | 3 |

### Results

| Candidate | Balanced | Interop-first | Autonomy/reliability | Simplicity-first | Robustness |
|---|---:|---:|---:|---:|---|
| **Spec Kit + GitHub** | **91.2** | **91.1** | **91.3** | **89.9** | **#1 in all profiles** |
| **GitHub control** | 86.3 | 85.8 | 85.3 | 86.9 | #2 in all profiles |
| **Beads** | 80.4 | 81.0 | 82.7 | 79.4 | #3 in all profiles |

## 7. Sensitivity interpretation

The desk ranking is unusually stable: changing the strategic priority does **not** change the order.

That does **not** authorize implementation, because several load-bearing scores are B/C evidence rather than direct MoA pilot evidence. In particular:

- Spec Kit C8 non-software fit;
- Spec Kit C2 web-agent interoperability in day-to-day use;
- Spec Kit C3 portfolio-level task/project handling after issues materialize;
- GitHub control C4/C5 repeated agent governance burden;
- Beads C8 non-software fit and web visibility.

A pilot can still reverse the ranking if these assumptions fail.

## 8. Finalists

### F1 — GitHub Spec Kit + GitHub Issues/Projects

**Current desk leader.**

Use upstream features only:

- Spec Kit workflows/artifacts/state;
- built-in `taskstoissues` integration where appropriate;
- GitHub Issues/Projects for human-visible portfolio/task state;
- portable Agent Skills only where an established skill/method exists or where a later MoA-specific procedure is legitimately project configuration rather than infrastructure;
- GitHub Actions/hooks/scripts for deterministic checks.

No Beads in F1 unless pilot evidence proves a missing capability.

### F2 — GitHub Issues/Projects + portable Agent Skills

**Complexity control.**

No separate workflow engine. Use:

- Issues/sub-issues/dependencies/custom fields/Projects;
- Agent Skills for repeatable methods;
- Actions/scripts for deterministic checks and scheduled/project mechanics;
- agent clients consume the same GitHub/repo state.

This finalist asks whether Spec Kit materially improves outputs and autonomy enough to justify another installed framework.

### F3 — Beads + minimal repo-visible project layer

**Agent-task-graph challenger.**

Pilot Beads without building a bespoke method framework around it. Keep human-visible summary/decision artifacts in the repo/GitHub. Do not pair it with Spec Kit before proving the task-graph advantage is needed.

## 9. Donor/reference systems retained

The following are not production-core finalists, but may later supply proven reusable modules **after the core is chosen**:

- **Superpowers:** verification, brainstorming, planning, subagent/reviewer patterns;
- **BMAD:** role/process methods, research/planning web bundles;
- **OpenSpec:** lightweight change/spec discipline;
- **Ruflo:** high-autonomy runtime if a later task genuinely needs swarms/memory/MCP scale;
- **Hermes/OpenClaw:** execution clients/runtimes, not portfolio truth;
- **Gas City:** revisit only if the portfolio later needs unattended multi-agent runtime orchestration beyond Spec Kit's workflow engine.

## 10. Decision boundary

**No framework is selected for production yet.**

Desk research has reduced the decision to three finalists. The next phase is to execute the bounded Master of Arts pilot protocol.

Order:

1. Pilot F1 Spec Kit + GitHub first.
2. Run the same tasks using F2 GitHub control.
3. Pilot F3 Beads only on the tasks where agent-native graph/state should create a measurable advantage.
4. Compare product usefulness, handoff/recovery, CEO control, context burden, manual glue, duplicate truth and operational burden.
5. Select the smallest system that materially wins.
