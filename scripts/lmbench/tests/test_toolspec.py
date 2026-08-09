"""Tool registry: argument shape validation and OpenAI schema emission."""

from __future__ import annotations

import unittest

from scripts.lmbench import toolspec


class TestValidate(unittest.TestCase):
    def test_missing_required_field_rejected(self):
        result = toolspec.validate("read_file", {})
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "missing_required:path")

    def test_unexpected_property_rejected(self):
        result = toolspec.validate("read_file", {"path": "a.txt", "sneaky": "x"})
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "unexpected_property:sneaky")

    def test_bad_type_rejected(self):
        result = toolspec.validate("read_file", {"path": 123})
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "bad_type:path")

    def test_bad_enum_rejected(self):
        result = toolspec.validate(
            "classify_failure",
            {"failure_class": "not_a_real_class", "evidence_refs": []},
        )
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "bad_enum:failure_class")

    def test_valid_args_accepted(self):
        result = toolspec.validate("read_file", {"path": "a.txt"})
        self.assertTrue(result.ok)
        self.assertEqual(result.typed_args, {"path": "a.txt"})

    def test_unknown_tool_rejected(self):
        result = toolspec.validate("no_such_tool", {})
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "unknown_tool:no_such_tool")

    def test_args_not_object_rejected(self):
        result = toolspec.validate("read_file", "not-a-dict")
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "args_not_object")

    def test_array_of_strings_validated_element_wise(self):
        ok = toolspec.validate(
            "classify_failure",
            {"failure_class": "unknown", "evidence_refs": ["a", "b"]},
        )
        self.assertTrue(ok.ok)
        bad = toolspec.validate(
            "classify_failure",
            {"failure_class": "unknown", "evidence_refs": ["a", 5]},
        )
        self.assertFalse(bad.ok)
        self.assertEqual(bad.error, "bad_type:evidence_refs")

    def test_run_command_takes_argv_array_never_a_command_string(self):
        tool = toolspec.REGISTRY["run_command"]
        self.assertIn("argv", tool.parameters["properties"])
        self.assertEqual(tool.parameters["properties"]["argv"]["type"], "array")
        self.assertNotIn("command", tool.parameters["properties"])


class TestOpenAISchemaEmission(unittest.TestCase):
    def test_offered_schemas_only_includes_requested_tools(self):
        schemas = toolspec.offered_schemas(["read_file", "finish"])
        names = {s["function"]["name"] for s in schemas}
        self.assertEqual(names, {"read_file", "finish"})

    def test_unknown_tool_name_silently_dropped_from_offered_schemas(self):
        schemas = toolspec.offered_schemas(["read_file", "not_a_tool"])
        names = {s["function"]["name"] for s in schemas}
        self.assertEqual(names, {"read_file"})

    def test_every_registered_tool_has_a_finish_and_an_escalate_path(self):
        self.assertIn("finish", toolspec.REGISTRY)
        self.assertIn("emit_escalation", toolspec.REGISTRY)
        escalation_tool = toolspec.REGISTRY["emit_escalation"]
        destinations = escalation_tool.parameters["properties"]["destination"]["enum"]
        self.assertEqual(len(destinations), 7)


if __name__ == "__main__":
    unittest.main()
