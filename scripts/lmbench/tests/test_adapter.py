"""Adapter parsing, tested against a RECORDED real llama-server response --
never a live call in unittest. This exact JSON body was captured this session
from `llama-server` b10333 serving Qwen3-8B-Q4_K_M with `--reasoning-budget
200`, confirming the server does emit genuine OpenAI-format tool_calls."""

from __future__ import annotations

import json
import unittest

from scripts.lmbench import adapter
from scripts.lmbench.errors import AdapterError

RECORDED_TOOL_CALL_RESPONSE = json.loads(
    r"""
{
    "choices": [
        {
            "finish_reason": "tool_calls",
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "",
                "reasoning_content": "Okay, the user wants me to list the files in the current directory using the list_dir tool with the path set to \".\".",
                "tool_calls": [
                    {
                        "type": "function",
                        "function": {
                            "name": "list_dir",
                            "arguments": "{\"path\": \".\"}"
                        },
                        "id": "JEGxZrs8vBs9KgkVdozVscDy81ImHQvZ"
                    }
                ]
            }
        }
    ],
    "created": 1786301515,
    "model": "C:\\LocalModels\\qwen3-8b\\gguf-q4km\\Qwen3-8B-Q4_K_M.gguf",
    "system_fingerprint": "b10333-08659901c",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 187,
        "prompt_tokens": 162,
        "total_tokens": 349
    },
    "id": "chatcmpl-WMPPNUcwTeABXlmTsHdmjPumfkhqptvr"
}
"""
)

RECORDED_TEXT_ONLY_RESPONSE = json.loads(
    r"""
{
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Hello, I'm Qwen!",
                "reasoning_content": "Thinking about the greeting."
            }
        }
    ],
    "created": 1786289078,
    "model": "C:\\LocalModels\\qwen3-8b\\gguf-q4km\\Qwen3-8B-Q4_K_M.gguf",
    "id": "chatcmpl-x"
}
"""
)


class TestParseRecordedResponses(unittest.TestCase):
    def test_tool_call_response_parses(self):
        parsed = adapter._parse_openai_response(RECORDED_TOOL_CALL_RESPONSE)
        self.assertEqual(parsed.finish_reason, "tool_calls")
        self.assertEqual(len(parsed.tool_calls), 1)
        call = parsed.tool_calls[0]
        self.assertEqual(call.name, "list_dir")
        self.assertEqual(call.call_id, "JEGxZrs8vBs9KgkVdozVscDy81ImHQvZ")
        self.assertEqual(json.loads(call.arguments_raw), {"path": "."})
        self.assertEqual(parsed.content, "")
        self.assertIn("list_dir", parsed.reasoning_content)

    def test_text_only_response_parses_with_no_tool_calls(self):
        parsed = adapter._parse_openai_response(RECORDED_TEXT_ONLY_RESPONSE)
        self.assertEqual(parsed.tool_calls, ())
        self.assertEqual(parsed.content, "Hello, I'm Qwen!")
        self.assertEqual(parsed.finish_reason, "stop")

    def test_response_with_no_choices_raises_adapter_error(self):
        with self.assertRaises(AdapterError):
            adapter._parse_openai_response({"choices": []})

    def test_raw_field_preserves_the_full_original_body(self):
        parsed = adapter._parse_openai_response(RECORDED_TOOL_CALL_RESPONSE)
        self.assertEqual(parsed.raw, RECORDED_TOOL_CALL_RESPONSE)


class TestStubAdapter(unittest.TestCase):
    def test_replays_script_in_order(self):
        r1 = adapter.RawResponse(content="a", reasoning_content=None, tool_calls=(), finish_reason="stop")
        r2 = adapter.RawResponse(content="b", reasoning_content=None, tool_calls=(), finish_reason="stop")
        stub = adapter.StubAdapter([r1, r2])
        self.assertEqual(stub.chat([], []).content, "a")
        self.assertEqual(stub.chat([], []).content, "b")
        self.assertEqual(stub.calls_made, 2)

    def test_raises_when_script_exhausted(self):
        stub = adapter.StubAdapter([])
        with self.assertRaises(AdapterError):
            stub.chat([], [])

    def test_health_always_true(self):
        self.assertTrue(adapter.StubAdapter([]).health())


if __name__ == "__main__":
    unittest.main()
