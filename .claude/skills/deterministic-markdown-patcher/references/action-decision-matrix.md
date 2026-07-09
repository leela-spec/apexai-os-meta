# Action Decision Matrix

This matrix helps the operator select the appropriate patch action mode
based on the characteristics of the desired change.  Choosing the
correct mode ensures that the patch executor behaves deterministically
and complies with the patching process contract.

| Intent Characteristics | Recommended Mode | Rationale |
| --- | --- | --- |
| You need to replace a specific word, phrase or small block of text that appears exactly once in the file. | **replace‑once** | This mode performs a single exact match replacement.  It verifies that the old text exists exactly once and then substitutes the new text. |
| You need to replace an entire section of a Markdown document under a specific heading.  The heading text is known and unambiguous. | **replace‑heading‑section** | This mode identifies the section delineated by the specified heading and the next heading of equal or higher level.  It replaces the entire section content with the new content provided. |
| You need to update or set values in the YAML front‑matter (e.g., title, tags, date) at the top of a Markdown file. | **front‑matter‑set** | This mode parses the front‑matter block, updates the specified keys with new values or adds new keys.  It preserves existing keys and ordering. |
| You are unsure whether the old text exists or how many times it appears and want to examine the file first. | **inspect** or **extract‑span** | Use `inspect` to view the entire file or `extract‑span` with the suspected old text to confirm its presence and occurrence count. |
| You have applied a replacement and need to ensure that only the intended span was changed. | **validate‑scope** | This mode compares the original and patched files to verify that changes are confined to the expected area.  It aborts on unexpected modifications. |
| You need to communicate or audit the exact changes made after a replacement. | **diff** | Generates a unified diff between the original and patched file, providing a concise representation of the modifications. |

## Guidelines for Using the Matrix

1. Always start by analysing the patch intent.  Determine whether the
   change targets a specific span, a section under a heading or YAML
   front‑matter.
2. If the old span is not known or may appear multiple times,
   run the executor in `inspect` or `extract‑span` mode to confirm
   uniqueness before attempting a replacement.
3. Use `replace‑once` only when the span appears exactly once.  If the
   span appears more than once, refine the context or consider a
   section‑based replacement if appropriate.
4. Use `replace‑heading‑section` when replacing a logical section of
   a Markdown document.  Ensure that the heading is unambiguous and
   at the correct level; otherwise you may accidentally replace the
   wrong portion.
5. Use `front‑matter‑set` strictly for YAML front‑matter updates.
   Do not use it to modify arbitrary YAML elsewhere in the file.
6. After any replacement, run `validate‑scope` followed by `diff` to
   check that only the intended change occurred and to produce proof
   of change.
7. When in doubt, consult the patching process contract and the
   failure modes reference before selecting an action.