from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from importlib import resources
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator

from .errors import ApexKBError


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-") or "topic"


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def atomic_bytes(path: Path, value: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def atomic_json(path: Path, value: Any) -> None:
    atomic_text(path, json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def atomic_yaml(path: Path, value: Any) -> None:
    atomic_text(path, yaml.safe_dump(value, sort_keys=False, allow_unicode=True))


def load_json(path: Path) -> Any:
    if not path.is_file():
        raise ApexKBError("artifact_missing", f"Required file does not exist: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - reason-coded boundary
        raise ApexKBError("artifact_invalid_json", f"Invalid JSON in {path}: {exc}") from exc


def load_yaml(path: Path) -> Any:
    if not path.is_file():
        raise ApexKBError("config_missing", f"Configuration file does not exist: {path}")
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:  # noqa: BLE001 - reason-coded boundary
        raise ApexKBError("config_invalid_yaml", f"Invalid YAML in {path}: {exc}") from exc


def iter_ndjson(path: Path) -> Iterable[dict[str, Any]]:
    if not path.is_file():
        raise ApexKBError("artifact_missing", f"Required NDJSON file does not exist: {path}")
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ApexKBError("artifact_invalid_ndjson", f"Invalid NDJSON at {path}:{line_no}: {exc}") from exc
            if not isinstance(item, dict):
                raise ApexKBError("artifact_invalid_ndjson", f"NDJSON record at {path}:{line_no} is not an object")
            yield item


def atomic_ndjson(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    atomic_text(path, "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows))


def schema(name: str) -> dict[str, Any]:
    try:
        text = resources.files("apex_kb.schemas").joinpath(name).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ApexKBError("schema_missing", f"Packaged schema is missing: {name}") from exc
    return json.loads(text)


def template(name: str) -> str:
    try:
        return resources.files("apex_kb.templates").joinpath(name).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ApexKBError("template_missing", f"Packaged template is missing: {name}") from exc


def validate_schema(value: Any, name: str) -> None:
    validator = Draft202012Validator(schema(name))
    errors = sorted(validator.iter_errors(value), key=lambda item: list(item.absolute_path))
    if not errors:
        return
    rendered = []
    for error in errors[:50]:
        pointer = ".".join(map(str, error.absolute_path)) or "$"
        rendered.append(f"{pointer}: {error.message}")
    raise ApexKBError("schema_validation_failed", "; ".join(rendered), rendered)


def ensure_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ApexKBError("object_required", f"{label} must be a mapping/object")
    return value


def safe_relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise ApexKBError("path_outside_root", f"Path is outside root: {path} not within {root}") from exc
