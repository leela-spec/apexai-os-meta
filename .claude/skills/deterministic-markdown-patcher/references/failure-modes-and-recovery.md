# Failure Modes and Recovery

This document catalogues common failure modes encountered during
deterministic patching and offers recommended recovery steps.  Use it
when the patch executor reports an error or validation failure.

## No Match

* **Symptom**: The `replace‑once` or `replace‑heading‑section` mode
  cannot find the specified old text or heading in the target file.
* **Possible Causes**: The old span is misspelled; the file has changed
  since the intent was created; the heading level is different.
* **Recovery**:
  1. Inspect the file (`inspect` mode) or extract the span to verify
     its presence.
  2. Adjust the old text or heading in the intent to match the live
     file exactly.
  3. If the file has changed, update the intent to reflect the
     current state.

## Multiple Matches

* **Symptom**: The old span appears more than once in the file.
* **Possible Causes**: The span is too generic; multiple identical
  headings exist.
* **Recovery**:
  1. Narrow the context by including additional surrounding text.
  2. If replacing a section, provide the full heading hierarchy
     (e.g., `## Parent › Subheading`).
  3. Alternatively, perform the replacement in multiple passes,
     each targeting one occurrence explicitly (not recommended for
     large numbers of matches).

## Ambiguous Heading

* **Symptom**: The specified heading matches multiple sections or
  appears at different levels.
* **Possible Causes**: Duplicate headings, inconsistent heading levels.
* **Recovery**:
  1. Include the full heading text and level (e.g., `### API Usage`).
  2. Prepend parent headings separated by `›` to disambiguate (e.g.,
     `## Usage › ### API Usage`).
  3. If headings are genuinely duplicated, rename one in the source
     file before patching.

## YAML Parse Error

* **Symptom**: `front‑matter‑set` fails to parse the YAML front‑matter.
* **Possible Causes**: The front‑matter is missing, malformed or
  contains invalid YAML syntax.
* **Recovery**:
  1. Confirm that the file begins with `---` and ends the front‑matter
     with another `---` delimiter.
  2. Use a YAML linter to identify syntax errors.
  3. Manually fix the front‑matter before attempting the patch.

## Validation Failure

* **Symptom**: After applying a patch, `validate‑scope` reports
  unexpected changes or the diff includes unintended modifications.
* **Possible Causes**: The old span boundaries were incorrect; the
  replacement text contains newline differences; the file encoding
  changed.
* **Recovery**:
  1. Re‑extract the span or section to verify its exact bounds.
  2. Ensure that the replacement text uses the same newline style
     (`\n` or `\r\n`) as the original file.
  3. Revert the patch, refine the intent and reapply.

## Invalid Path

* **Symptom**: The executor refuses to modify the file because the
  path is outside the allowed root.
* **Possible Causes**: Absolute or traversing paths (`../`) were used.
* **Recovery**:
  1. Provide a relative path within the repository root.
  2. Avoid using directory traversal (`..`) in the target path.

## General Error Handling

* Capture and log the error message.  Use the `on_error` hook to
  notify operators.
* Do not attempt to apply the patch if any precondition fails.
* Always revert the file to its original state on failure.
* Consult this document and the contract for further guidance.