# Domain Overlay Rules

```yaml id="ff8rx9"
purpose:
  file_role: domain_overlay_application_rules
  schema_authority: references/project-schema.md
  rule_boundary: rules_only_no_field_type_definitions

overlay_selection:
  dev: dev_fields
  content: content_fields
  business: business_fields
  comms: comms_fields
  investment: investment_fields

application_rules:
  - Append the overlay block that matches the record's domain_type value.
  - Treat domain overlays as optional extensions; base_record remains complete without overlay fields.
  - If domain_type is missing, flag missing_domain_type and do not infer an overlay.
  - Treat overlay fields absent from a record as absent, not null.
  - Allow the operator to add overlay fields incrementally across sessions.
  - Put information that does not yet fit the overlay into that overlay's notes field.
  - Do not create new overlay blocks or rename overlay blocks outside references/project-schema.md.
  - Do not move base_record fields into overlays.

domain_context:
  dev:
    context: >
      Use for software, repo, app, infrastructure, automation, or technical
      build projects. It represents implementation state, code artifacts,
      deployment readiness, testing, and acceptance boundaries.
    notes_rule: >
      Use notes for technical details that are useful now but not stable enough
      to become structured fields.

  content:
    context: >
      Use for writing, publishing, editorial, curriculum, creative, or media
      projects. It represents content type, draft/review state, channel, and
      publishing readiness.
    notes_rule: >
      Use notes for loose brief details, style constraints, audience fragments,
      or editorial context not yet structured.

  business:
    context: >
      Use for offers, clients, products, sales, strategy, operations, or
      commercial decisions. It represents business-stage clarity, stakeholders,
      decisions, risks, and success signals.
    notes_rule: >
      Use notes for market context, informal assumptions, or operator comments
      that should not become schema yet.

  comms:
    context: >
      Use for conversations, follow-ups, relationship threads, response queues,
      and platform-specific communication work. It represents who is waiting,
      what action is required, and when follow-up matters.
    notes_rule: >
      Use notes for tone, relationship nuance, message history summaries, or
      context that does not fit the lean overlay.

  investment:
    context: >
      Use for investment ideas, positions, thesis tracking, risk review, or
      exit/entry reasoning. It represents asset-level thesis state, sizing,
      timing, and risk constraints.
    notes_rule: >
      Use notes for market observations, unresolved thesis questions, or
      operator caveats not yet promoted into structured fields.
```