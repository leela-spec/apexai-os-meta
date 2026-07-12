# Meta Strategy Doctrine (weekly planning stage)

Purpose: doctrine for the meta_strategy accountability as carried by the apex-precap-week stage agent — how to frame options, direction, and recommendations inside a weekly_plan_packet. Consumer: apex-precap-week (dispatched via weekly-orchestrator, gate G1). Source basis: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_strategy/`. The agent definition (`.claude/agents/apex-precap-week.md`), the PrecapWeek skill contract, and the handoff schema remain schema and boundary authority; this file adds strategic-content doctrine only.

## Best practices

- Rule: the weekly-planning stage owns option framing, scenario comparison, timing analysis, and leverage analysis — every recommended weekly direction is a bounded recommendation handed to downstream stages, never a claim on execution. (Source: `meta_strategy/ESSENCE.md` — Owns / Agent boundary)
- Rule: perform explicit option framing (named alternatives, not a single path) whenever any of these hold: more than one viable path exists, a tradeoff must be framed, timing or leverage is central to the choice, or a high-impact route decision is active for the week. Otherwise a single direct recommendation suffices. (Source: `meta_strategy/ESSENCE.md` — Read when)
- Rule: for every recommended path, surface its dependencies and its reversibility (what must be true first; how costly it is to back out). Record these in the weekly_plan_packet body next to the recommendation, and irreducible unknowns in the envelope `uncertainties`. (Source: `meta_strategy/ESSENCE.md` — Core constraints)
- Rule: when a weekly route decision is high risk, request challenge instead of self-certifying — set a non-trivial `unresolved_risk` line in the envelope so the orchestrator's consequential-packet test can trigger dual-blind review. The stage never validates its own output. (Source: `meta_strategy/ESSENCE.md` — Core constraints, mapped onto the current review wiring)

## Known failure modes

- Avoid: binary "whether or not" framing of a weekly direction. Widen to at least one real alternative (including "defer") before recommending, when the option-framing triggers above apply. (Source: `meta_strategy/Appendices/DecisionMakingProcessReseearch_gem.md` — WRAP, "Widen Your Options")
- Avoid: justifying a recommendation purely by precedent or analogy ("we did it this way before"). Check the assumption the recommendation rests on against current project-status truth; if the axiom cannot be confirmed from the read inputs, say so as an uncertainty rather than asserting it. (Source: `meta_strategy/Appendices/DecisionMakingProcessReseearch_gem.md` — First Principles)

## Templates worth reusing

- Template: option-framing block for a contested weekly route decision — for each named option record: `option`, `assumption_it_rests_on` (reality-tested against read inputs or flagged), `dependencies`, `reversibility` (cheap / costly / one-way), `pre_mortem` (one line: most plausible way this fails by week's end), then a single `recommendation` line with the deciding factor. (Source: `meta_strategy/Appendices/DecisionMakingProcessReseearch_gem.md` — First Principles + WRAP hybrid; `meta_strategy/ESSENCE.md` — recommendation packets)
