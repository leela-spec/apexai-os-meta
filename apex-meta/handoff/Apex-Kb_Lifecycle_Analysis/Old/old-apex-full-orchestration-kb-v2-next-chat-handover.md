# Handover: Old-Apex-Full-Orchestration KB Lifecycle

## Mission

Run the Apex KB lifecycle for exactly:

`C:\GitDev\apexai-os-meta\apex-meta\kb\old-apex-full-orchestration-agent-kb-v2`

Produce a query-ready, source-grounded knowledge base whose analysis and wiki pages are highly valuable to another AI: detailed enough to explain decisions and workflows, but structured and compressed enough for fast retrieval and processing.

This handover is the starting contract for the next chat. Do not broaden the corpus, mutate Apex plan/sync/session state, or begin Claude-skill integration. The target is the Old-Apex-Full-Orchestration KB only.

## Critical source and interpretation rules

- **System 2 fallback:** System 2 has no compiled wiki yet. When a task asks for System 2 knowledge, read `ingest-analysis/` first, especially the relevant `phase1-*.md` files. Do not claim a wiki page exists when it does not.
- **Source custody:** Treat `raw/` and the source manifests as authoritative evidence. Never infer content from filenames, memory, or prior summaries.
- **Claude target:** The implementation target is Claude orchestration. Hermes material is historical/reference evidence only. State everywhere that the Hermes architecture is a possible blueprint with Hermes logic, not the target runtime logic.
- **Operational role:** The PMKB/PD workflow is important evidence, but it describes the operational meta-agent layer of the MetaOps agent; do not present it as the entire Claude architecture.
- **Alternatives:** Rank alternatives by use case, evidence, trade-offs, and implementation fit. Do not collapse competing designs into one undifferentiated answer.
- **Decisions first:** Claude-relevant implementation decisions, constraints, and workflows have higher retrieval priority than historical narrative.

## Required value contract for every semantic page

Do not create heading-only or one-sentence pages. Each summary, concept, and entity page must contain substantive, source-pointer-backed prose and answer how an AI should use the information.

Each page should include, as applicable:

1. **Purpose and scope** — what the page answers and what it does not answer.
2. **Decision/use guidance** — the recommended Claude implementation interpretation.
3. **Key claims** — multiple atomic claims, each with exact source pointers.
4. **Macro / meso / micro synthesis** — system-level pattern, component/workflow relationship, and concrete operational detail.
5. **Overlap and evidence** — repeated processes, designs, agents, or workflows across files; count or enumerate independent occurrences and explain why repetition raises confidence in a core pattern.
6. **Alternatives ranked by use case** — preferred option, viable alternatives, when each wins, and disqualifiers.
7. **Connections** — explicit links to related pages, source files, concepts, decisions, workflows, and unresolved questions.
8. **Uncertainty and contradictions** — distinguish verified evidence, strong inference, weak inference, historical design, and unresolved conflict.
9. **Retrieval triggers** — query terms and the next page/source an agent should open.

Use compact tables, stable IDs, and short paragraphs. Token efficiency means high information density, not low content volume.

## Lifecycle execution order

1. Read the live package contract before execution:
   - `.claude/skills/apex-kb/SKILL.md`
   - `package-manifest.md`
   - `references/kb-contract.md`
   - `references/script-command-contract.md`
   - `references/ingest-query-lint-audit-rules.md`
   - `references/retrieval-contract.md`
   - `examples/lifecycle-runbook.md`
2. Lock the single KB root above and run the topic interview. Record operator topics/open questions in `manifests/topic-registry.json`.
3. Run or confirm: `scaffold`, `hash`, `source-intake`, `preflight`, and `phase0`.
4. Inspect Phase 0 outputs and propose additional corpus-evidenced topics in the registry. Do not hand-edit deterministic rankings.
5. Run `ingest-phase1`. Read all Phase 1 analysis before drafting wiki pages. Use Phase 1 as the fallback knowledge surface for System 2.
6. Compile Phase 2 in small batches (2–3 pages). For each batch: draft, run strict quality, repair reason-coded failures, then advance. Never generate the entire wiki as shallow boilerplate.
7. Build the compiled wiki around the most decision-relevant entities, concepts, summaries, and workflows. Include cross-file overlap/evidence maps and connection routes.
8. Run deterministic postflight: capability-checked index rebuild, retrieval index rebuild, stale check, strict lint/quality, audit, and status.
9. Generate query packets and local retrieval outputs. `query_ready` requires deterministic postflight, fresh retrieval, and semantic acceptance.

## Preferred artifact shape

- `ingest-analysis/`: rich Phase 1 evidence synthesis, source-by-source and cross-source.
- `wiki/entities/`: defining agents, architectures, workflows, and operational roles.
- `wiki/concepts/`: reusable principles, boundaries, decision rules, and repeated patterns.
- `wiki/summaries/`: Claude implementation briefs and ranked alternatives by use case.
- `wiki/index.md`: navigation by decision, workflow, entity, concept, and query route.
- `audit/`: contradictions, unsupported claims, thin pages, unresolved source gaps, and repair candidates.
- `outputs/queries/`: compact query-ready packets that point to the smallest sufficient source/page set.

## Quality assurance gate

Before calling the run complete, verify:

- Every substantive claim has a specific source pointer.
- Every important page has multiple claims and meaningful macro/meso/micro depth.
- Repeated patterns are explicitly counted/compared, not merely mentioned.
- Connections point both ways where useful; no orphan high-value page remains.
- System 2 references use Phase 1 fallback wording when compiled wiki coverage is absent.
- Hermes is labeled historical/blueprint evidence and Claude is the implementation target.
- Alternatives are ranked by use case and evidence.
- Retrieval indexes are fresh and rebuildable.
- Strict lint/quality, audit, and semantic acceptance pass; otherwise report `compiled_unvalidated` or `partial`, never `query_ready`.

## Fast continuation instruction for the next chat

Begin by reading this handover and the live `SKILL.md`, then execute against the locked KB root. Do not ask for a new general explanation. If a required command fails, report the exact command and error, repair only the blocking issue, and continue the lifecycle. Stop only at a truthful lifecycle state with artifacts and evidence recorded.
