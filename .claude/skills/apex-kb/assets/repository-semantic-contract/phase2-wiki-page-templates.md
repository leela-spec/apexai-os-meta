# Phase 2 Wiki Page Contract

Summary, concept, and entity pages require v2 frontmatter (`semantic_contract_version`,
`semantic_run_id`, `target_query_ids`), direct answer-bearing content, `Target Questions
Answered`, Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, and
Uncertainty / Raw Source Reopen Triggers.

**Macro / Meso / Micro is a defined semantic, not a free restatement**: Macro = Why (the
architectural context, the problem, the design decision and value gained); Meso = What it is
(the feature/service/screen/model itself - components, structure, connections); Micro = How
(the concrete execution path - trigger, steps, outcome), with one inline flow chain folded into
Micro rather than given its own heading. Target 3-5 sentences per layer - a complete standalone
thought at that scale, never a single thin sentence.

`related_concepts`/`related_entities` frontmatter must be populated from the matching Phase 1
topic file's Concept/Entity Candidate Shortlist - copy the slugs directly, do not leave them
empty when a shortlist exists. Key Claims carry a `state: present | proposed | open` tag,
inherited unchanged from the Phase 1 claim record. `source_refs` entries carry a `claims:`
sub-key (claim IDs from that source) for claim-level provenance - do not flatten `source_refs`
to bare strings, the object form's `source_hash`/`source_pointer` must be preserved.

An optional `Connection Map` (directional edges to peer pages: direction, peer, what flows,
contract) may follow Routes Here only when the topic has 3 or more edges; below that, fold the
edges into Routes Here and omit the heading. It is not one of the six required value headings.

Adaptive Ranked Source Set contains only sources actually reviewed and materially used, with
rank where available, analysis reference, supported query IDs, claim IDs, rationale, and
coverage. Keep unopened candidates in the semantic ledger. Do not duplicate frontmatter lists
in prose or add numeric page-value scores. Create concept/entity pages only for independent
project-specific retrieval value; otherwise preserve a Phase 1 rejection or embed disposition.
