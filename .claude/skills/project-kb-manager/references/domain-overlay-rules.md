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
  - Append the overlay block matching the record's domain_type value.
  - Treat domain overlays as optional extensions; base_record remains complete without them.
  - If domain_type is missing, flag missing_domain_type and do not infer an overlay.
  - Treat absent overlay fields as absent, not null.
  - Allow operator-added overlay fields incrementally across sessions.
  - Put unmatched information into the matching overlay notes field.
  - Do not create or rename overlay blocks outside references/project-schema.md.
  - Do not move base_record fields into overlays.

domain_context:
  dev: "Software, repo, app, infrastructure, automation, or technical build projects; use notes for unstable technical details."
  content: "Writing, publishing, editorial, curriculum, creative, or media projects; use notes for brief/style/audience context."
  business: "Offers, clients, products, sales, strategy, operations, or commercial decisions; use notes for market assumptions."
  comms: "Conversations, follow-ups, relationship threads, response queues, or platform communication; use notes for tone/history."
  investment: "Investment ideas, positions, thesis tracking, risk review, or entry/exit reasoning; use notes for unresolved thesis context."

non_goals:
  - Do not define field types or allowed values.
  - Do not select overlays without domain_type.
  - Do not write project records.
```