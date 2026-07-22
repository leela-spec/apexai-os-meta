# Apex KB target decisions and value matrix

## Purpose

This file prevents architectural rediscovery and priority drift. It records what has already been decided, what the live branch currently implements, and which missing capabilities create the most product value for the least additional complexity.

## Locked decisions

| Decision | Selected target | Why it matters | Do not reopen unless |
|---|---|---|---|
| Product form | Windows-first modular Python CLI | Deterministic, testable, restartable, local | a proven product requirement cannot be met by the CLI |
| Skill role | Thin optional launcher/instruction surface | Skills must not own sequencing or state | CLI operation is already working and a small convenience layer is needed |
| Phase model | Phase 0 Setup; Phase 1 Deterministic; Phase 2 Semantic; Phase 3 Finish | Final operator-facing model repeatedly selected | migration cost is justified by a measured usability failure |
| Setup interface | One fixed selected Start template plus one configuration | Prevents model-improvised intake | real operator test proves a concrete missing field |
| Deterministic scope | Complete corpus inventory and exhaustive candidate mapping | Preserves whole-corpus intelligence | measured runtime cost requires a bounded optimization that preserves completeness |
| Semantic worker | Subscription ChatGPT browser chat using connected GitHub repository | Matches the chosen operating environment | operator explicitly changes execution environment |
| Semantic transport | Generated repository-aware prompt; agent edits repo, commits, pushes | Repository is durable cross-chat state | a real platform limitation is demonstrated |
| Local continuation | Safe pull/fast-forward, validate expected files/commit, generate next prompt | Keeps deterministic CLI authority | no repository mutation is needed in a specific output tier |
| Retrieval | Derived local SQLite FTS5 after accepted compilation | Useful and already implemented | semantic spine proves a simpler replacement is better |
| Real proof | Leela Skill Tree repository round trip | Synthetic tests do not prove product value | a different real corpus is explicitly selected |

## Value scoring

Scores are decision aids, not measured benchmarks.

- **Product value:** contribution to a working knowledge-base process.
- **Target alignment:** direct fit with already selected architecture.
- **Implementation cost:** 5 means low cost; 1 means high cost.
- **Drift risk:** 5 means low risk; 1 means high risk.
- **Priority score:** product value + target alignment + implementation cost + drift risk.

## Missing-capability matrix

| Capability | Current live state | Product value | Target alignment | Impl. cost | Low drift risk | Score /20 | Disposition |
|---|---|---:|---:|---:|---:|---:|---|
| Repository-aware Phase 2A prompt | Missing; local packet points to filesystem/incoming JSON | 5 | 5 | 4 | 5 | **19** | **Build next** |
| Browser agent write/commit/push contract | Missing; current worker is forbidden from writing wiki/manifests | 5 | 5 | 4 | 5 | **19** | **Build next** |
| Local Git pull and semantic reconciliation | Missing | 5 | 5 | 3 | 4 | **17** | **Build after prompt contract** |
| Repository-aware Phase 2B compilation prompt | Missing | 5 | 5 | 4 | 5 | **19** | **Build with Phase 2A pattern** |
| Real Leela Skill Tree round-trip canary | Missing | 5 | 5 | 3 | 5 | **18** | **Mandatory proof** |
| Phase 0 selected template/parser integration | Implemented at commit `93c6b534...` | 5 | 5 | 5 | 5 | **20** | Preserve; no redesign |
| Deterministic whole-corpus engine | Substantially implemented | 5 | 5 | 2 | 4 | **16** | Validate on real corpus; patch only proven defects |
| Compact human Start readback | Raw JSON remains less friendly | 3 | 4 | 4 | 5 | **16** | Defer until semantic spine is working unless operator usability blocks canary |
| Additional acceptance checks | Existing packet/import present | 2 | 3 | 2 | 3 | **10** | Defer |
| More retrieval integrity layers | Already extensive | 1 | 2 | 2 | 2 | **7** | Do not expand |
| Provider-neutral AI adapters | Not selected | 1 | 1 | 1 | 1 | **4** | Reject now |
| Linux support | Not required | 0 | 0 | 2 | 2 | **4** | Reject now |
| GUI/TUI | Not required | 1 | 1 | 1 | 2 | **5** | Defer |
| Concurrency/lock framework | Single operator; not demonstrated need | 1 | 1 | 2 | 2 | **6** | Defer |
| New orchestration/state database | Existing files already own state | 0 | 0 | 1 | 1 | **2** | Reject |

## Phase-by-phase target matrix

| Phase | Selected operator experience | Deterministic owner | Browser semantic owner | Current status | Next value action |
|---|---|---|---|---|---|
| Phase 0 Setup | Print template → fill config → preflight → confirm | CLI | None, optional explanations only | Integrated and tested | Preserve |
| Phase 1 Deterministic | One local action generates exhaustive corpus intelligence | CLI | None | Substantially implemented | Validate against real Leela output |
| Phase 2A Analysis | CLI outputs one complete prompt; browser agent reads repo, writes analyses, commits and pushes | CLI generates prompt and validates returned repo state | ChatGPT browser chat | Missing/replaced by local JSON workflow | Restore repository-aware handoff |
| Phase 2B Compilation | CLI outputs one complete prompt; browser agent writes dossier/atlas, commits and pushes | CLI generates prompt and validates returned repo state | Fresh ChatGPT browser chat | Missing/replaced by local JSON workflow | Restore after Phase 2A |
| Phase 3 Finish | Pull → validate → optional fresh acceptance → postflight → retrieval | CLI | Fresh evaluator only where output tier requires it | Mechanically present, not real-flow proven | Do not expand before Phase 2 works |

## Anti-overengineering gate

Before approving any new component, answer all five questions:

1. Does it directly enable the selected end-to-end workflow?
2. Is the missing behavior proven in the live branch or real canary?
3. Can an existing module be adapted instead of adding another authority?
4. Does it reduce operator work or semantic reading cost?
5. Can it be implemented and proven in one bounded iteration?

Reject or defer the component when fewer than four answers are yes.
