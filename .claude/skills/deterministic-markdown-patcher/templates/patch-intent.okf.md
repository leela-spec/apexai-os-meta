**Patch Intent Template**

Use this template to draft a patch intent for the deterministic
markdown patcher.  Replace the placeholder values with your own
content.  The intent can be expressed in YAML, JSON or free‑form
Markdown; however, structured formats are preferred for complex
changes.

```yaml
# Specify the target file relative to the repository root
target_file: path/to/file.md

# Select the mode of operation: one of
#   - replace_once
#   - replace_heading_section
#   - front_matter_set
mode: replace_once

# For replace_once: the exact text to replace and its replacement
old_text: >
  Replace this exact text.
new_text: >
  With this new text.

# For replace_heading_section: the heading to match and the new
# section content.  The heading may include the level (e.g., "## Heading").
# heading: "## My Heading"
# new_section: |
#   New content under the heading.

# For front_matter_set: a mapping of keys to new values.
# front_matter: {title: "New Title", tags: ["docs", "patch"]}

# Optional description of the intent for human readers
description: >
  Explain why this change is needed and any context that helps
  reviewers understand the patch.
```

Fill in only the fields relevant to your chosen mode.  Omit unused
sections to avoid confusion.  The patch executor will ignore keys
that do not apply to the selected mode.