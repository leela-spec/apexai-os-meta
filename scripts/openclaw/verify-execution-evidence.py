from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse


RECEIPT_FIELDS = {
    "schema_version",
    "execution_id",
    "status",
    "provider",
    "browser_profile",
    "hostname",
    "mode",
    "web_model",
    "reasoning_mode",
    "session_policy",
    "conversation_url",
    "prompt_sha256",
    "prompt_body_bytes_submitted",
    "captured_characters",
    "result_path",
    "near_page_cap",
    "reload_performed",
    "instruction_shaped_content_observed",
    "notes",
}


def fail(code: str, message: str) -> None:
    raise ValueError(f"{code}: {message}")


def load_object(path: Path, code: str) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(code, str(exc))
    if not isinstance(value, dict):
        fail(code, "expected a JSON object")
    return value


def same_path(left: object, right: object) -> bool:
    return os.path.normcase(os.path.abspath(str(left))) == os.path.normcase(os.path.abspath(str(right)))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_browser_origin(
    raw_result_path: Path,
    executor_model: str,
    evidence_dir: Path,
    prompt_text: str,
    result_text: str,
    conversation_url: str,
) -> dict[str, object]:
    raw_bytes = raw_result_path.read_bytes()
    raw = load_object(raw_result_path, "OPENCLAW_RESULT_JSON")
    if raw.get("status") != "ok" or raw.get("summary") != "completed":
        fail("OPENCLAW_STATUS", "harness did not report a completed turn")
    try:
        agent_meta = raw["result"]["meta"]["agentMeta"]
        session_path = Path(str(agent_meta["sessionFile"]))
    except (KeyError, TypeError):
        fail("OPENCLAW_META", "harness result lacks agent/session metadata")
    expected_agent = {
        "openai/gpt-4.1-nano": ("openai", "gpt-4.1-nano"),
        "apex-local/qwen3-8b-q4km": ("apex-local", "qwen3-8b-q4km"),
    }.get(executor_model)
    if expected_agent is None or (agent_meta.get("provider"), agent_meta.get("model")) != expected_agent:
        fail("OPENCLAW_MODEL", "harness provider/model does not match the selected executor")
    if same_path(session_path.parent, evidence_dir) or str(session_path).lower().startswith(
        str(evidence_dir).lower() + os.sep
    ):
        fail("SESSION_EVIDENCE_TRUST", "browser transcript must be harness-owned outside the writable evidence directory")
    try:
        session_bytes = session_path.read_bytes()
        entries = [json.loads(line) for line in session_bytes.decode("utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail("SESSION_EVIDENCE", str(exc))

    calls: list[tuple[str, dict[str, object]]] = []
    successful_results: dict[str, str] = {}
    for entry in entries:
        message = entry.get("message") if isinstance(entry, dict) else None
        if not isinstance(message, dict):
            continue
        if message.get("role") == "assistant" and isinstance(message.get("content"), list):
            for content in message["content"]:
                if (
                    isinstance(content, dict)
                    and content.get("type") == "toolCall"
                    and content.get("name") == "browser"
                    and isinstance(content.get("arguments"), dict)
                ):
                    calls.append((str(content.get("id", "")), content["arguments"]))
        elif message.get("role") == "toolResult" and message.get("toolName") == "browser" and message.get("isError") is not True:
            text_parts = [
                str(part["text"])
                for part in message.get("content", [])
                if isinstance(part, dict) and part.get("type") == "text" and isinstance(part.get("text"), str)
            ]
            successful_results[str(message.get("toolCallId", ""))] = "\n".join(text_parts)

    prompt_calls = []
    type_calls = []
    submissions = []
    for index, (call_id, arguments) in enumerate(calls):
        request = arguments.get("request") if arguments.get("action") == "act" else None
        if not isinstance(request, dict):
            continue
        if request.get("kind") == "type":
            type_calls.append((index, call_id, arguments))
            if request.get("text") == prompt_text:
                prompt_calls.append((index, call_id, arguments))
        if request.get("kind") == "press" and request.get("key") == "Enter":
            submissions.append((index, call_id))
    if len(prompt_calls) != 1 or len(type_calls) != 1:
        fail("BROWSER_PROMPT", "browser transcript does not contain exactly one exact frozen-prompt insertion")
    later_submissions = [item for item in submissions if item[0] > prompt_calls[0][0]]
    if len(later_submissions) != 1:
        fail("BROWSER_SUBMISSION_COUNT", "browser transcript does not prove exactly one submission after prompt insertion")
    if prompt_calls[0][1] not in successful_results or later_submissions[0][1] not in successful_results:
        fail("BROWSER_ACTION_RESULT", "prompt insertion or submission lacks a successful browser tool result")

    target_id = prompt_calls[0][2].get("targetId")
    if target_id != calls[later_submissions[0][0]][1].get("targetId"):
        fail("BROWSER_TARGET", "prompt insertion and submission used different browser tabs")
    response_observations = []
    for index, (call_id, arguments) in enumerate(calls):
        if (
            index > later_submissions[0][0]
            and arguments.get("action") == "snapshot"
            and arguments.get("targetId") == target_id
            and call_id in successful_results
        ):
            response_observations.append(successful_results[call_id])
    browser_text = "\n".join(successful_results.values())
    if conversation_url not in browser_text:
        fail("CONVERSATION_NOT_BROWSER_ORIGIN", "receipt URL is absent from successful browser observations")
    normalized_result = " ".join(result_text.split())
    normalized_response_observations = " ".join("\n".join(response_observations).split())
    if normalized_result not in normalized_response_observations:
        fail("RESULT_NOT_BROWSER_ORIGIN", "captured result is absent from successful browser observations")
    browser_evidence = json.dumps(
        [{"tool_call_id": call_id, "text": text} for call_id, text in sorted(successful_results.items())],
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "raw_result_path": str(raw_result_path),
        "raw_result_sha256": sha256(raw_bytes),
        "session_file": str(session_path),
        "session_sha256": sha256(session_bytes),
        "browser_evidence_sha256": sha256(browser_evidence),
        "browser_call_count": len(calls),
        "browser_submission_count": len(later_submissions),
    }


def verify(
    request_path: Path,
    receipt_path: Path,
    raw_result_path: Path,
    executor_model: str,
    dispatch_state_path: Path,
    output_path: Path,
) -> dict[str, object]:
    request = load_object(request_path, "REQUEST_JSON")
    receipt = load_object(receipt_path, "RECEIPT_JSON")
    if set(receipt) != RECEIPT_FIELDS:
        fail("RECEIPT_FIELDS", "receipt fields do not match apex.executor-receipt/v1")
    if receipt["schema_version"] != "apex.executor-receipt/v1":
        fail("RECEIPT_SCHEMA", "unsupported executor receipt schema")
    if receipt["status"] != "completed":
        fail("RECEIPT_STATUS", "executor did not report a completed capture")

    settings = request.get("provider_settings")
    if not isinstance(settings, dict):
        fail("REQUEST_SETTINGS", "provider_settings is missing")
    expected = {
        "execution_id": request.get("execution_id"),
        "provider": request.get("provider"),
        "browser_profile": settings.get("browser_profile"),
        "hostname": settings.get("hostname"),
        "mode": settings.get("mode"),
        "web_model": settings.get("model"),
        "reasoning_mode": settings.get("reasoning_mode"),
        "session_policy": settings.get("session_policy"),
    }
    for field, value in expected.items():
        if receipt[field] != value:
            fail("RECEIPT_SETTINGS", f"{field} does not match the validated request")

    prompt_ref = request.get("prompt_ref")
    if not isinstance(prompt_ref, dict):
        fail("REQUEST_PROMPT", "prompt_ref is missing")
    frozen_prompt = Path(str(request.get("evidence_dir", ""))) / "frozen-prompt.md"
    try:
        prompt_bytes = frozen_prompt.read_bytes()
    except OSError as exc:
        fail("PROMPT_MISSING", str(exc))
    prompt_hash = sha256(prompt_bytes)
    if prompt_hash != prompt_ref.get("sha256") or receipt["prompt_sha256"] != prompt_hash:
        fail("PROMPT_HASH", "frozen prompt, request, and executor receipt do not agree")
    if type(receipt["prompt_body_bytes_submitted"]) is not int or receipt["prompt_body_bytes_submitted"] != len(prompt_bytes):
        fail("PROMPT_BYTES", "submitted prompt byte count does not match the frozen prompt")

    result_path = Path(str(request.get("result_path", "")))
    if not same_path(receipt["result_path"], result_path):
        fail("RESULT_PATH", "receipt result path does not match the request")
    if not result_path.is_file():
        fail("RESULT_MISSING", "declared result artifact does not exist")
    result_bytes = result_path.read_bytes()
    if not result_bytes:
        fail("RESULT_EMPTY", "declared result artifact is empty")
    try:
        result_text = result_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail("RESULT_UTF8", str(exc))
    if type(receipt["captured_characters"]) is not int or receipt["captured_characters"] != len(result_text):
        fail("RESULT_CHARACTERS", "captured character count does not match the result")

    url = urlparse(str(receipt["conversation_url"]))
    if url.scheme != "https" or (url.hostname or "").lower() != str(settings.get("hostname", "")).lower():
        fail("CONVERSATION_HOSTNAME", "conversation URL is not on the declared HTTPS provider host")
    for field in ("near_page_cap", "reload_performed", "instruction_shaped_content_observed"):
        if type(receipt[field]) is not bool:
            fail("RECEIPT_FIELDS", f"{field} must be boolean")
    if not isinstance(receipt["notes"], list) or any(not isinstance(note, str) for note in receipt["notes"]):
        fail("RECEIPT_FIELDS", "notes must be an array of strings")

    browser_origin = verify_browser_origin(
        raw_result_path,
        executor_model,
        Path(str(request["evidence_dir"])),
        prompt_bytes.decode("utf-8"),
        result_text,
        str(receipt["conversation_url"]),
    )

    verified = {
        "schema_version": "apex.verified-executor-receipt/v1",
        "status": "completed",
        "execution_id": request["execution_id"],
        "executor_model": executor_model,
        "provider": request["provider"],
        "browser_profile": settings["browser_profile"],
        "hostname": settings["hostname"],
        "mode": settings["mode"],
        "web_model": settings["model"],
        "reasoning_mode": settings["reasoning_mode"],
        "session_policy": settings["session_policy"],
        "conversation_url": receipt["conversation_url"],
        "prompt_sha256": prompt_hash,
        "prompt_body_bytes_submitted": len(prompt_bytes),
        "result_path": str(result_path),
        "result_bytes": len(result_bytes),
        "captured_characters": len(result_text),
        "result_sha256": sha256(result_bytes),
        "near_page_cap": receipt["near_page_cap"],
        "reload_performed": receipt["reload_performed"],
        "instruction_shaped_content_observed": receipt["instruction_shaped_content_observed"],
        "source_receipt_path": str(receipt_path),
        "source_receipt_sha256": sha256(receipt_path.read_bytes()),
        "dispatch_state_file": str(dispatch_state_path),
        **browser_origin,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = output_path.with_name(f".{output_path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(verified, separators=(",", ":")), encoding="utf-8")
    temporary.replace(output_path)
    return verified


def main() -> int:
    if len(sys.argv) != 7:
        print(
            "USAGE: verify-execution-evidence.py REQUEST RECEIPT RAW_RESULT EXECUTOR_MODEL DISPATCH_STATE OUTPUT",
            file=sys.stderr,
        )
        return 2
    try:
        verified = verify(
            Path(sys.argv[1]),
            Path(sys.argv[2]),
            Path(sys.argv[3]),
            sys.argv[4],
            Path(sys.argv[5]),
            Path(sys.argv[6]),
        )
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps({"valid": True, "result_sha256": verified["result_sha256"]}, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
