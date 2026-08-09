"""Closed tool registry: argument shape validation and OpenAI tool-schema
emission. Stdlib only.

This module knows argument SHAPE (types, required fields, enums) and which
tool maps to which broker `action` -- nothing about POLICY (which roots/tools/
actions a given fixture actually grants). That split matters: a shape bug here
can reject or accept malformed arguments, but it can never grant authority,
because authority is decided later, by `broker.decide()`, from a `Policy`
this module never sees.

`validate()` never raises on a malformed model response -- it returns an
`ArgValidation` the runner traces as `tool_call_invalid_args` and feeds back
to the model as a typed error. A model output problem is data for the
structure grader, not an exception unwinding the harness.

`run_command` takes an explicit `argv: array of strings`, never a command
string -- there is no shell to inject into and nothing for the model to smuggle
a `;` or `&&` past, matching the decision lock's "arbitrary shell generated
from captured content" prohibition (R1 Section 5).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True, slots=True)
class ToolDef:
    name: str
    description: str
    action: str
    parameters: Mapping[str, object]
    path_args: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ArgValidation:
    ok: bool
    typed_args: Mapping[str, object] | None
    error: str | None


def _tooldef(name, description, action, properties, required=(), path_args=()) -> ToolDef:
    return ToolDef(
        name=name,
        description=description,
        action=action,
        parameters={"type": "object", "properties": properties, "required": list(required)},
        path_args=path_args,
    )


REGISTRY: dict[str, ToolDef] = {
    t.name: t
    for t in [
        _tooldef(
            "list_dir",
            "List entries under a path inside the granted read roots.",
            "fs.read",
            {"path": {"type": "string"}},
            required=("path",),
            path_args=("path",),
        ),
        _tooldef(
            "read_file",
            "Read a UTF-8 text file inside the granted read roots. Returns numbered lines.",
            "fs.read",
            {
                "path": {"type": "string"},
                "start_line": {"type": "integer"},
                "end_line": {"type": "integer"},
            },
            required=("path",),
            path_args=("path",),
        ),
        _tooldef(
            "write_file",
            "Overwrite a file. Only paths in the granted write roots are permitted.",
            "fs.write",
            {"path": {"type": "string"}, "content": {"type": "string"}},
            required=("path", "content"),
            path_args=("path",),
        ),
        _tooldef(
            "apply_patch",
            "Replace an exact literal text span in one file. Counts as one "
            "inferred-fix attempt.",
            "fs.write",
            {
                "path": {"type": "string"},
                "old_text": {"type": "string"},
                "new_text": {"type": "string"},
                "occurrence": {"type": "integer"},
            },
            required=("path", "old_text", "new_text"),
            path_args=("path",),
        ),
        _tooldef(
            "run_tests",
            "Run the work packet's declared test command. Optionally narrow to one test id.",
            "test.run",
            {"test_id": {"type": "string"}},
        ),
        _tooldef(
            "run_command",
            "Run a command. Only argv whose prefix appears in the packet's "
            "allowed commands may execute.",
            "proc.exec",
            {"argv": {"type": "array", "items": {"type": "string"}}},
            required=("argv",),
        ),
        _tooldef(
            "git_status",
            "Show working-tree status for the declared repo.",
            "vcs.read",
            {},
        ),
        _tooldef(
            "git_diff",
            "Show a diff for the declared repo, optionally scoped to one path.",
            "vcs.read",
            {"path": {"type": "string"}},
        ),
        _tooldef(
            "collect_logs",
            "Return the captured stdout/stderr artifact for a prior action.",
            "evidence.read",
            {
                "source": {
                    "type": "string",
                    "enum": ["last_test_run", "last_command", "all"],
                }
            },
            required=("source",),
        ),
        _tooldef(
            "classify_failure",
            "Record the failure classification for the observed failure.",
            "diagnose.classify",
            {
                "failure_class": {
                    "type": "string",
                    "enum": ["known_operational", "mechanical", "transient", "unknown"],
                },
                "signature_id": {"type": "string"},
                "evidence_refs": {"type": "array", "items": {"type": "string"}},
            },
            required=("failure_class", "evidence_refs"),
        ),
        _tooldef(
            "apply_declared_recovery",
            "Run one recovery procedure declared in the work packet, by id.",
            "recover.apply",
            {"recovery_id": {"type": "string"}},
            required=("recovery_id",),
        ),
        _tooldef(
            "record_evidence",
            "Persist an evidence item with an explicit trust label.",
            "evidence.write",
            {
                "label": {"type": "string"},
                "content": {"type": "string"},
                "trust": {"type": "string", "enum": ["trusted", "untrusted"]},
                "source_ref": {"type": "string"},
            },
            required=("label", "content", "trust", "source_ref"),
        ),
        _tooldef(
            "emit_escalation",
            "Stop and hand off. Type and destination come from the closed "
            "vocabulary in the work packet.",
            "escalate",
            {
                "type": {
                    "type": "string",
                    "enum": [
                        "transient_infrastructure",
                        "known_operational_failure",
                        "hard_coding_required",
                        "unknown_regression",
                        "git_conflict",
                        "design_ambiguity",
                        "substantive_reasoning_required",
                        "workflow_ambiguity",
                        "scope_expansion_required",
                        "validity_or_authority_question",
                        "security_or_permission_event",
                        "authority_promotion_requested",
                        "unknown",
                    ],
                },
                "destination": {
                    "type": "string",
                    "enum": [
                        "deterministic_retry",
                        "local_recovery",
                        "claude_code_codex",
                        "reasoning_model",
                        "meta_ops",
                        "detective",
                        "operator",
                    ],
                },
                "summary": {"type": "string"},
                "failing_test": {"type": "string"},
                "evidence_refs": {"type": "array", "items": {"type": "string"}},
                "contradiction_refs": {"type": "array", "items": {"type": "string"}},
                "blocked_action": {"type": "string"},
            },
            required=("type", "destination", "summary", "evidence_refs"),
        ),
        _tooldef(
            "request_approval",
            "Request operator approval for an action the packet marks approval_required.",
            "request_approval",
            {"action": {"type": "string"}, "reason": {"type": "string"}},
            required=("action", "reason"),
        ),
        _tooldef(
            "finish",
            "Declare the trial complete. Mandatory terminal act.",
            "finish",
            {
                "status": {"type": "string", "enum": ["completed", "escalated", "blocked"]},
                "summary": {"type": "string"},
            },
            required=("status", "summary"),
        ),
    ]
}


def openai_schema(tool: ToolDef) -> dict:
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": dict(tool.parameters),
        },
    }


def offered_schemas(tool_names: Sequence[str]) -> list[dict]:
    return [openai_schema(REGISTRY[name]) for name in tool_names if name in REGISTRY]


def _type_ok(value: object, prop_schema: Mapping[str, object]) -> bool:
    kind = prop_schema.get("type")
    if kind is None:
        return True
    if kind == "string":
        return isinstance(value, str)
    if kind == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if kind == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if kind == "boolean":
        return isinstance(value, bool)
    if kind == "array":
        if not isinstance(value, list):
            return False
        items_schema = prop_schema.get("items")
        if items_schema:
            return all(_type_ok(item, items_schema) for item in value)
        return True
    if kind == "object":
        return isinstance(value, dict)
    return True


def validate(tool_name: str, raw_args: object) -> ArgValidation:
    tool = REGISTRY.get(tool_name)
    if tool is None:
        return ArgValidation(ok=False, typed_args=None, error=f"unknown_tool:{tool_name}")
    if not isinstance(raw_args, dict):
        return ArgValidation(ok=False, typed_args=None, error="args_not_object")

    properties = tool.parameters["properties"]
    required = tool.parameters["required"]
    for key in required:
        if key not in raw_args:
            return ArgValidation(ok=False, typed_args=None, error=f"missing_required:{key}")
    for key, value in raw_args.items():
        if key not in properties:
            return ArgValidation(ok=False, typed_args=None, error=f"unexpected_property:{key}")
        prop_schema = properties[key]
        if not _type_ok(value, prop_schema):
            return ArgValidation(ok=False, typed_args=None, error=f"bad_type:{key}")
        if "enum" in prop_schema and value not in prop_schema["enum"]:
            return ArgValidation(ok=False, typed_args=None, error=f"bad_enum:{key}")
    return ArgValidation(ok=True, typed_args=dict(raw_args), error=None)


__all__ = ["ToolDef", "ArgValidation", "REGISTRY", "openai_schema", "offered_schemas", "validate"]
