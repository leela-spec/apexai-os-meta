# Example: Running a Patch Pack

Patch packs allow multiple deterministic patches to be applied in
sequence via a fixture.  Consider two files:

- `CHANGELOG.md` contains "version 1.0.0".
- `docs/usage.md` contains a section headed `## Deprecated` that we
  want to replace entirely.

Define a fixture `examples/upgrade-fixture.json`:

```json
{
  "description": "Upgrade version and remove deprecated section",
  "steps": [
    {
      "mode": "replace_once",
      "target_file": "CHANGELOG.md",
      "old_text": "version 1.0.0",
      "new_text": "version 2.0.0",
      "expected_diff": "-version 1.0.0\n+version 2.0.0"
    },
    {
      "mode": "replace_heading_section",
      "target_file": "docs/usage.md",
      "heading": "## Deprecated",
      "new_section": "This section has been removed in version 2.0.0.",
      "expected_output": "Section replaced"
    }
  ]
}
```

Run the fixture with:

```sh
python scripts/fixture_runner.py examples/upgrade-fixture.json
```

The runner will execute each step in order, assert the expected
outputs/diffs and exit with a non‑zero status on failure.