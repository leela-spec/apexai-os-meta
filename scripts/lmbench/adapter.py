"""Model/runtime adapters. Stdlib only.

Uses `http.client`, not `urllib.request` -- `urllib.request` has one coarse
timeout with no connect/read split and can hang indefinitely on a slow token
stream. `http.client.HTTPConnection(timeout=...)` applies a socket-level
timeout to every blocking recv, which is sufficient here (a single blocking,
non-streaming request per turn) without needing a separate watchdog thread.

Verified live against this machine's actual `llama-server` (b10333) +
Qwen3-8B: `--jinja` is on by default, the GGUF chat template exposes a
`tools` block, and the server returns genuine OpenAI-format `tool_calls`
(`finish_reason: "tool_calls"`, `message.tool_calls[].function.{name,
arguments}`, arguments as a JSON string) -- not a hypothesis, a captured
response. `--reasoning-budget N` caps `<think>` token spend, which is what
fixes the install log's "200 tokens of thinking, empty content" failure mode.
"""

from __future__ import annotations

import http.client
import json
from dataclasses import dataclass, field
from typing import Mapping, Sequence

from .errors import AdapterError


@dataclass(frozen=True, slots=True)
class ToolCall:
    call_id: str
    name: str
    arguments_raw: str


@dataclass(frozen=True, slots=True)
class RawResponse:
    content: str | None
    reasoning_content: str | None
    tool_calls: tuple[ToolCall, ...]
    finish_reason: str | None
    raw: Mapping[str, object] = field(default_factory=dict)


def _parse_openai_response(data: Mapping[str, object]) -> RawResponse:
    choices = data.get("choices") or []
    if not choices:
        raise AdapterError(f"response has no choices: {data!r}")
    message = choices[0].get("message") or {}
    raw_calls = message.get("tool_calls") or []
    tool_calls = tuple(
        ToolCall(
            call_id=call.get("id") or f"call-{i}",
            name=(call.get("function") or {}).get("name", ""),
            arguments_raw=(call.get("function") or {}).get("arguments", "{}"),
        )
        for i, call in enumerate(raw_calls)
    )
    return RawResponse(
        content=message.get("content"),
        reasoning_content=message.get("reasoning_content"),
        tool_calls=tool_calls,
        finish_reason=choices[0].get("finish_reason"),
        raw=data,
    )


class StubAdapter:
    """Replays a scripted list of RawResponse, one per call. VAL tests run
    entirely against this -- offline, deterministic, no model contacted."""

    def __init__(self, script: Sequence[RawResponse]):
        self._script = list(script)
        self._index = 0

    def health(self) -> bool:
        return True

    def chat(self, messages: list[dict], tools: Sequence[dict]) -> RawResponse:
        if self._index >= len(self._script):
            raise AdapterError("StubAdapter script exhausted")
        response = self._script[self._index]
        self._index += 1
        return response

    @property
    def calls_made(self) -> int:
        return self._index


class LlamaCppAdapter:
    """Talks to a running `llama-server` (OpenAI-compatible HTTP) via
    `http.client`. Configuration identity (host/port/generation_config)
    belongs on the trial record, not inferred after the fact."""

    def __init__(
        self,
        *,
        host: str = "127.0.0.1",
        port: int = 8090,
        timeout: float = 180.0,
        generation_config: Mapping[str, object] | None = None,
    ):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.generation_config = dict(generation_config or {})

    def health(self) -> bool:
        conn = http.client.HTTPConnection(self.host, self.port, timeout=10)
        try:
            conn.request("GET", "/health")
            resp = conn.getresponse()
            body = resp.read()
            return resp.status == 200 and b'"ok"' in body
        except OSError:
            return False
        finally:
            conn.close()

    def chat(self, messages: list[dict], tools: Sequence[dict]) -> RawResponse:
        payload: dict = {"messages": messages, **self.generation_config}
        if tools:
            payload["tools"] = list(tools)
            payload["tool_choice"] = "auto"
        body = json.dumps(payload).encode("utf-8")

        conn = http.client.HTTPConnection(self.host, self.port, timeout=self.timeout)
        try:
            conn.request(
                "POST",
                "/v1/chat/completions",
                body=body,
                headers={"Content-Type": "application/json"},
            )
            resp = conn.getresponse()
            raw_body = resp.read()
        except (TimeoutError, OSError) as exc:
            raise AdapterError(f"llama.cpp request failed: {exc}") from exc
        finally:
            conn.close()

        if resp.status != 200:
            raise AdapterError(f"llama.cpp returned HTTP {resp.status}: {raw_body[:500]!r}")
        try:
            data = json.loads(raw_body)
        except json.JSONDecodeError as exc:
            raise AdapterError(f"llama.cpp returned non-JSON body: {exc}") from exc
        return _parse_openai_response(data)


__all__ = ["ToolCall", "RawResponse", "StubAdapter", "LlamaCppAdapter"]
