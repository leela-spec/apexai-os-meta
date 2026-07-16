"""Anti-drift guard: every concrete (non-placeholder) schema example embedded in the apex-kb
skill's own documentation must actually validate against the JSON schema it claims to represent.

A doc author marks a concrete instance with an HTML comment `<!-- schema: <name>.schema.json -->`
immediately before a fenced ```json block. This test finds every such marker in the skill package
and validates the following block against that schema using apex_kb_control's own validator - the
same deterministic validator a real run relies on, not a re-implementation.

This exists because a prior run's semantic-acceptance output used field names (`semantic_run_id`,
`review_mode`, `verdict: "answerable"`, `material_claim_verifications`) that looked plausible but
did not match `semantic-acceptance.schema.json` (`run_id`, `evaluator_context`, `result`,
`claim_reviews`) - the executor had faithfully copied a doc example that had drifted from the
schema it was supposed to represent. See acceptance-tests.md's marked worked example.
"""

import importlib.util
import json
import re
import sys
import unittest
from pathlib import Path


CONTROL_MODULE_PATH = Path(__file__).resolve().parents[1] / "apex_kb_control.py"
SPEC = importlib.util.spec_from_file_location("apex_kb_control_under_test_docs", CONTROL_MODULE_PATH)
assert SPEC and SPEC.loader
apex_kb_control = importlib.util.module_from_spec(SPEC)
sys.modules["apex_kb_control_under_test_docs"] = apex_kb_control
SPEC.loader.exec_module(apex_kb_control)


MARKER_RE = re.compile(
    r"<!--\s*schema:\s*(?P<schema>[\w.-]+\.json)\s*-->\s*\n"
    r"```json\n(?P<body>.*?)\n```",
    re.DOTALL,
)


def find_marked_examples():
    """Yield (doc_path, schema_name, line_number, parsed_json) for every marked example
    under the apex-kb skill package."""
    skill_root = apex_kb_control.skill_root()
    for doc_path in sorted(skill_root.rglob("*.md")):
        text = doc_path.read_text(encoding="utf-8-sig")
        for match in MARKER_RE.finditer(text):
            line_number = text.count("\n", 0, match.start()) + 1
            yield doc_path, match.group("schema"), line_number, match.group("body")


class DocSchemaExampleDriftTests(unittest.TestCase):
    def test_at_least_one_marked_example_exists(self):
        # If this ever finds zero, either no doc currently carries a concrete example (fine on
        # its own) or the marker convention/regex has silently broken - fail loud either way so
        # the anti-drift guard is never quietly doing nothing.
        found = list(find_marked_examples())
        self.assertGreater(len(found), 0, "No <!-- schema: ... --> marked examples found under the apex-kb skill package")

    def test_every_marked_example_parses_as_json(self):
        for doc_path, schema_name, line_number, body in find_marked_examples():
            with self.subTest(doc=str(doc_path), schema=schema_name, line=line_number):
                try:
                    json.loads(body)
                except json.JSONDecodeError as exc:
                    self.fail(f"{doc_path}:{line_number} marked as {schema_name} is not valid JSON: {exc}")

    def test_every_marked_example_validates_against_its_named_schema(self):
        for doc_path, schema_name, line_number, body in find_marked_examples():
            with self.subTest(doc=str(doc_path), schema=schema_name, line=line_number):
                value = json.loads(body)
                schema = apex_kb_control.load_schema(schema_name)
                errors = apex_kb_control.validate_schema(value, schema)
                self.assertEqual(
                    errors,
                    [],
                    f"{doc_path}:{line_number} example marked as {schema_name} does not validate: {errors}",
                )


if __name__ == "__main__":
    unittest.main()
