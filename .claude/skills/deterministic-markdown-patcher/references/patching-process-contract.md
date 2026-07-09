# Patching Process Contract

This document describes the deterministic patching architecture used by the
`deterministic‑markdown‑patcher` skill.  It synthesises research on patch
processes and codifies the principles, required modes and hard rules that
govern every modification.

## Principles

1. **Intent over diff** – The operator supplies a patch intent describing
   the desired change.  The executor extracts the existing text from
   the live file and applies a deterministic replacement.  The diff is
   generated automatically as proof; it is never authored by hand.
2. **Live extraction** – All replacements are anchored on content
   extracted from the live file.  The executor must read the current
   file state and capture the old span exactly as it appears.  This
   prevents hallucinations and ensures that edits align with reality.
3. **Single‑match replacement** – Replacement operations must match
   exactly one occurrence of the old span.  If the span appears more
   than once or not at all, the executor must refuse to apply the
   change and prompt for clarification.
4. **No multi‑match or adjacent cleanup** – Operations must not
   replace multiple spans in one run nor perform adjacent cleanup of
   whitespace or punctuation.  The intent should identify the exact
   span or section; the executor must not extrapolate.
5. **Section‑based editing** – Entire sections can be replaced by
   identifying a heading.  The replacement includes everything from
   the heading line down to (but not including) the next heading of
   equal or higher level.  Headings must be specified exactly and
   uniquely.
6. **YAML front‑matter update** – Front‑matter can be set or updated
   using a mapping of keys and values.  Front‑matter must be parsed
   as YAML and rewritten deterministically, preserving existing
   ordering where possible.  Adding new keys is allowed; removing
   existing keys is not unless explicitly requested.
7. **Scope validation and diff** – After applying a patch, the
   executor must run validation to ensure that only the intended span
   changed.  A unified diff must then be produced.  If the diff shows
   unexpected modifications, the patch is rejected.
8. **No network or external execution** – The patch executor uses only
   the Python standard library and local filesystem.  It must refuse
   any patch that attempts to modify files outside the allowed root or
   run external commands.
9. **Generated‑file mode** – Full‑file rewrites are disallowed unless
   explicitly authorised via a generated‑file mode.  In generated‑file
   mode, the executor will replace the entire contents of a file with
   new content provided by the intent and record that the file was
   generated.

## Required Modes

The patch executor exposes several modes.  Each mode is invoked via
command‑line arguments:

| Mode | Purpose |
| --- | --- |
| **inspect** | Read and print the contents of a file.  Used to understand the current state before patching. |
| **extract‑span** | Given a file and an exact text span, locate and print the span along with its line numbers.  Refuses if the span is not found or appears multiple times. |
| **replace‑once** | Replace a single occurrence of an old span with new text.  Fails if the old span is not found or found multiple times.  Preserves newline style. |
| **replace‑heading‑section** | Replace an entire section under a given heading with new content.  The heading must exist exactly once and may include a level indicator (e.g., `### Heading`). |
| **front‑matter‑set** | Update YAML front‑matter keys with new values.  Parses the front‑matter, applies updates and writes back the file.  Errors if the front‑matter cannot be parsed. |
| **validate‑scope** | Check that a proposed replacement affects only the intended span or section.  Compares original and patched files and ensures that the diff is limited to the expected area. |
| **diff** | Produce a unified diff between the original and patched file.  Used to verify and communicate the change. |

## Hard Rules

The following rules must never be violated:

* Replacement must be deterministic and idempotent.  Running the same
  replacement twice should yield no further changes.
* Do not modify any file outside the repository root passed to the
  executor.
* Do not alter binary or unsupported file types.  Only text files
  (Markdown, YAML or similar) may be edited.
* Do not assume encoding; default to UTF‑8 and propagate the original
  newline style (`\n` or `\r\n`).
* Do not modify adjacent content (such as trailing punctuation or
  whitespace) unless explicitly included in the old span.
* Do not reorder YAML front‑matter keys except when inserting a new
  key at the end.
* Do not produce or accept multi‑match replacements.  Always fail
  early with a clear error message.
* Always run validation and diff before considering the patch
  successful.  If either step fails, revert the change and report the
  failure.

## Conclusion

This contract establishes the boundaries and expectations for
deterministic patching.  Adhering to these principles ensures that
edits are reproducible, auditable and confined to the operator’s
intent.  Refer to this document whenever implementing or reviewing
patch execution logic.