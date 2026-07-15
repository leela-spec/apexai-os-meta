# Phase 1 Analysis Contract

One analysis file exists per registry topic (`ingest-analysis/<topic-slug>.analysis.md`), not
one per source - it carries every source accepted for that topic. This file has exactly one
reader class: the Phase 2 synthesis LLM and the operator during review; no deterministic tool
parses it, so structure for LLM synthesis and provenance fidelity, not for a parser.

Each file records: a ranked Source Inventory (rejected/held sources get one row and nothing
more); a per-source record for every accepted source (identity, target-query coverage, summary,
extraction candidates, key claims with a `present | proposed | open` state tag, concept/entity
candidates, uncertainty triggers); a Cross-Source Synthesis Notes block for the Phase 2 LLM
(conflicts, authority-wins, what was discarded); and deduplicated Concept/Entity Candidate
Shortlist tables the Phase 2 LLM copies directly into `related_concepts`/`related_entities`.

Give every concept/entity candidate one disposition: `promote`, `embed_in_summary`,
`defer_blocked`, or `reject_no_independent_value`, with rationale, query IDs, and destination
page when applicable. Keep `concept_slug:`/`entity_slug:`/`disposition:` on their own lines
exactly as the template shows - deterministic lint greps these keys verbatim.

Use the authoritative complete template copied from the Apex package
(`templates/ingest-analysis-template.md`) when present. Do not remove any established section.
