---
title: "Target Drift and Source Authority Gates"
page_type: concept
kb_slug: "llm-wiki-project-repos"
concept_slug: "target-drift-and-source-authority-gates"
created_at: "2026-07-06"
status: "active"
confidence: "high"
claim_label: "source_backed_summary"
---

# Target Drift and Source Authority Gates

## Definition

Target drift occurs when an assistant lets the container of files define the task, rather than using the operator mission as the primary relevance filter. Source authority is narrower than source access: reading a file proves access only, not that it belongs in the read-first set or final synthesis.

## Operating Rules

```yaml
rules:
  - "Restate the mission as a hard filter before ranking sources."
  - "A file enters read-first only if it directly improves the declared lifecycle target."
  - "Domain-only context goes to appendix/domain routes, not lifecycle core."
  - "Machine-readable outputs must be stricter and smaller than prose."
  - "If prose and machine ranking contradict each other, repair before writing."
```

## Failure Pattern

```yaml
failure:
  name: handoff_folder_index_target_drift
  root_cause: scope_priority_inversion
  symptoms:
    - "folder membership treated as relevance"
    - "domain files ranked as read-first for lifecycle work"
    - "same bad classification duplicated across Markdown, OKF, JSON"
    - "machine artifacts preserved weak analysis instead of enforcing strict routing"
```

## Patch Ideas

```yaml
patches:
  - id: TD-001
    title: "Binary lifecycle relevance gate"
    target: "handover/index prompts and Apex KB runbooks"
    acceptance: "Every read-first file has one explicit lifecycle relevance reason."
  - id: TD-002
    title: "Contradiction gate before write"
    target: "semantic compile instructions"
    acceptance: "No output says a file is non-authoritative while ranking it read-first."
  - id: TD-003
    title: "Minimal machine routing map"
    target: "generated OKF/JSON routing artifacts"
    acceptance: "Machine files contain routing decisions only, not repeated prose."
```

## Routes Here

Use this concept before any folder-level Apex KB index, handoff index, or semantic compile where source inventory could be confused with authority.
