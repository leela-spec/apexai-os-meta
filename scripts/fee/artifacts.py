"""Strict-subset reader for APEX artifact files (FEE module M1, input side).

APEX artifacts are markdown documents carrying fenced ```yaml blocks and, in the
prompt packs, markdown pipe tables. They are not YAML files, and this repo already
reads them without a YAML dependency (see scripts/orchestration_check.py).

D-I2 keeps M1 stdlib-only, so this module implements the *subset* of block YAML the
live artifacts actually use, verified by construct scan over every input file:
nested block maps, block sequences, empty flow collections, bare and quoted scalars,
null, booleans, comments and blank lines. No block scalars, anchors, aliases, or
non-empty flow collections appear anywhere in the artifact family.

The load-bearing safety property: anything outside that subset raises
UnsupportedConstruct rather than being guessed at. A loud failure on an unexpected
construct is honest; a silent misparse is not. That is the whole reason a subset
reader is acceptable here instead of a dependency.

Parsing is two-pass -- tokenize lines, then build recursively from the token list.
A single-pass container stack cannot tell whether a bare `key:` opens a mapping or
a sequence without lookahead, and guessing there is exactly the silent-misparse
failure this module exists to avoid.
"""

from __future__ import annotations

import re
from pathlib import Path

YAML_FENCE_OPEN = re.compile(r"^```ya?ml\s*$", re.IGNORECASE)
FENCE_CLOSE = re.compile(r"^```\s*$")

# Constructs deliberately outside the supported subset.
_BLOCK_SCALAR = re.compile(r":\s*[|>][0-9+-]*\s*$")
_ANCHOR_OR_ALIAS = re.compile(r"(?:^|\s)[&*][A-Za-z_][\w-]*(?:\s|$)")

_KEY_LINE = re.compile(r"^(?P<key>[A-Za-z_][\w./&-]*)\s*:(?P<rest>.*)$")
_SEQ_LINE = re.compile(r"^-(?:\s+(?P<value>.*))?\s*$")

# Token kinds
_MAP = "map"
_SEQ = "seq"


class UnsupportedConstruct(Exception):
    """Raised when an artifact uses YAML this reader will not guess at."""


class ArtifactParseError(Exception):
    """Raised when an artifact is structurally malformed."""


def _strip_comment(raw: str) -> str:
    """Drop a trailing ` #...` comment, respecting quotes.

    Only space-hash starts a comment, so values like `.../FlowRecap-handoff.md#F1`
    survive intact -- that form is live in the flow packets.
    """
    out: list[str] = []
    quote: str | None = None
    i = 0
    while i < len(raw):
        ch = raw[i]
        if quote:
            out.append(ch)
            if ch == "\\" and i + 1 < len(raw):
                out.append(raw[i + 1])
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#" and i > 0 and raw[i - 1] in " \t":
            break
        else:
            out.append(ch)
        i += 1
    return "".join(out).rstrip()


def _split_flow(inner: str, where: str) -> list[str]:
    """Split a flow-sequence body on top-level commas, respecting quotes."""
    parts: list[str] = []
    buf: list[str] = []
    quote: str | None = None
    for ch in inner:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch == ",":
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if quote:
        raise ArtifactParseError(f"{where}: unterminated quote in flow sequence")
    parts.append("".join(buf))
    return [p for p in (part.strip() for part in parts) if p != ""]


def _scalar(text: str, where: str):
    """Convert a scalar token to a Python value, or raise on unsupported forms."""
    token = text.strip()
    if token == "" or token in ("null", "~", "Null", "NULL"):
        return None
    if token in ("true", "True", "TRUE"):
        return True
    if token in ("false", "False", "FALSE"):
        return False
    if token[0] in "\"'":
        if len(token) < 2 or token[-1] != token[0]:
            raise ArtifactParseError(f"{where}: unterminated quoted scalar: {token!r}")
        return token[1:-1].replace("\\" + token[0], token[0])
    # Flow collections whose members are all scalars are unambiguous, and live
    # artifacts use both forms: `source_refs: [path]` and the inline authority block
    # `authority: {state: candidate, basis_digest: null, ...}`. Nesting stays out.
    if token[0] in "[{":
        closer = "]" if token[0] == "[" else "}"
        if not token.endswith(closer):
            raise ArtifactParseError(f"{where}: unterminated flow collection: {token!r}")
        inner = token[1:-1].strip()
        if not inner:
            return [] if closer == "]" else {}
        if "[" in inner or "{" in inner:
            raise UnsupportedConstruct(
                f"{where}: nested flow collection is outside the supported subset: {token!r}"
            )
        parts = _split_flow(inner, where)
        if closer == "]":
            return [_scalar(part, where) for part in parts]
        flow_map: dict = {}
        for part in parts:
            key, sep, value = part.partition(":")
            if not sep:
                raise ArtifactParseError(
                    f"{where}: flow mapping entry without ':' -- {part!r}"
                )
            flow_map[key.strip()] = _scalar(value, where)
        return flow_map
    if re.fullmatch(r"-?\d+", token):
        return int(token)
    if re.fullmatch(r"-?\d+\.\d+", token):
        return float(token)
    return token


def _tokenize(text: str, source: str) -> list[tuple]:
    """Turn lines into (indent, kind, key, value_text, where) tokens.

    value_text is None when a mapping key opens a nested block.
    """
    tokens: list[tuple] = []
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        where = f"{source}:{lineno}"
        if "\t" in raw_line:
            raise UnsupportedConstruct(f"{where}: tab indentation is not supported")
        if _BLOCK_SCALAR.search(raw_line):
            raise UnsupportedConstruct(
                f"{where}: block scalar (| or >) is outside the supported subset"
            )
        if _ANCHOR_OR_ALIAS.search(raw_line):
            raise UnsupportedConstruct(
                f"{where}: anchors and aliases are outside the supported subset"
            )

        line = _strip_comment(raw_line)
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        body = line.strip()

        seq = _SEQ_LINE.match(body)
        if seq:
            value = seq.group("value")
            if value is None or not value.strip():
                raise UnsupportedConstruct(
                    f"{where}: bare '-' opening a nested block is outside the supported subset"
                )
            tokens.append((indent, _SEQ, None, value.strip(), where))
            continue

        key_match = _KEY_LINE.match(body)
        if not key_match:
            raise ArtifactParseError(f"{where}: not a key or sequence item: {body!r}")
        rest = key_match.group("rest")
        tokens.append(
            (indent, _MAP, key_match.group("key"), None if rest.strip() == "" else rest, where)
        )
    return tokens


def _build(tokens: list[tuple], i: int, indent: int):
    """Build the container starting at tokens[i], which sits at `indent`."""
    if tokens[i][1] == _SEQ:
        return _build_seq(tokens, i, indent)
    return _build_map(tokens, i, indent)


def _build_map(tokens: list[tuple], i: int, indent: int):
    mapping: dict = {}
    while i < len(tokens) and tokens[i][0] == indent:
        cur_indent, kind, key, value_text, where = tokens[i]
        if kind != _MAP:
            raise ArtifactParseError(
                f"{where}: sequence item where a mapping key was expected"
            )
        if key in mapping:
            raise ArtifactParseError(f"{where}: duplicate key {key!r} in the same mapping")
        i += 1
        if value_text is None:
            if i < len(tokens) and tokens[i][0] > cur_indent:
                mapping[key], i = _build(tokens, i, tokens[i][0])
            else:
                # `key:` with no children -- an explicitly empty value.
                mapping[key] = None
        else:
            mapping[key] = _scalar(value_text, where)
    return mapping, i


def _build_seq(tokens: list[tuple], i: int, indent: int):
    items: list = []
    while i < len(tokens) and tokens[i][0] == indent:
        cur_indent, kind, _key, value_text, where = tokens[i]
        if kind != _SEQ:
            raise ArtifactParseError(
                f"{where}: mapping key where a sequence item was expected"
            )
        i += 1
        inline = _KEY_LINE.match(value_text)
        if inline:
            # "- key: value" starts a mapping whose columns begin after the dash.
            rest = inline.group("rest")
            item: dict = {
                inline.group("key"): None if rest.strip() == "" else _scalar(rest, where)
            }
            child_indent = cur_indent + 2
            if i < len(tokens) and tokens[i][0] >= child_indent and tokens[i][1] == _MAP:
                nested, i = _build_map(tokens, i, tokens[i][0])
                for nested_key, nested_value in nested.items():
                    if nested_key in item:
                        raise ArtifactParseError(
                            f"{where}: duplicate key {nested_key!r} in sequence item"
                        )
                    item[nested_key] = nested_value
            items.append(item)
        else:
            if i < len(tokens) and tokens[i][0] > cur_indent:
                raise UnsupportedConstruct(
                    f"{where}: nested block under a scalar sequence item is outside the subset"
                )
            items.append(_scalar(value_text, where))
    return items, i


def parse_block_yaml(text: str, *, source: str = "<yaml>") -> dict:
    """Parse the supported block-YAML subset into nested dicts and lists."""
    tokens = _tokenize(text, source)
    if not tokens:
        return {}
    base = tokens[0][0]
    if tokens[0][1] != _MAP:
        raise ArtifactParseError(f"{tokens[0][4]}: document root must be a mapping")
    result, consumed = _build_map(tokens, 0, base)
    if consumed != len(tokens):
        raise ArtifactParseError(
            f"{tokens[consumed][4]}: inconsistent indentation "
            f"(expected {base}, got {tokens[consumed][0]})"
        )
    return result


def extract_yaml_blocks(text: str) -> list[str]:
    """Return the bodies of every fenced ```yaml block, in document order."""
    blocks: list[str] = []
    current: list[str] | None = None
    for line in text.splitlines():
        if current is None:
            if YAML_FENCE_OPEN.match(line):
                current = []
            continue
        if FENCE_CLOSE.match(line):
            blocks.append("\n".join(current))
            current = None
            continue
        current.append(line)
    if current is not None:
        raise ArtifactParseError("unterminated ```yaml fence")
    return blocks


def parse_pipe_tables(text: str) -> list[list[dict]]:
    """Return every markdown pipe table as a list of header-keyed row dicts."""
    tables: list[list[dict]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not (line.startswith("|") and line.endswith("|") and i + 1 < len(lines)):
            i += 1
            continue
        if not re.fullmatch(r"\|(?:\s*:?-{2,}:?\s*\|)+", lines[i + 1].strip()):
            i += 1
            continue
        headers = [c.strip() for c in line.strip("|").split("|")]
        rows: list[dict] = []
        j = i + 2
        while j < len(lines):
            row_line = lines[j].strip()
            if not (row_line.startswith("|") and row_line.endswith("|")):
                break
            cells = [c.strip() for c in row_line.strip("|").split("|")]
            rows.append(dict(zip(headers, cells)))
            j += 1
        tables.append(rows)
        i = j
    return tables


def load_artifact(path: Path) -> tuple[dict, list[list[dict]]]:
    """Read an APEX artifact into (merged yaml blocks, pipe tables).

    Top-level keys from every fenced block are merged into one mapping. The live
    artifacts use distinct top-level keys per block (handoff_envelope, flow_packet,
    raw_flow_dump_template, ...), so a collision means the artifact changed shape
    and is surfaced rather than silently overwritten.
    """
    if not path.exists():
        raise ArtifactParseError(f"artifact not found: {path}")
    text = path.read_text(encoding="utf-8")
    merged: dict = {}
    for index, block in enumerate(extract_yaml_blocks(text)):
        parsed = parse_block_yaml(block, source=f"{path.name}#yaml{index + 1}")
        for key, value in parsed.items():
            if key in merged:
                raise ArtifactParseError(
                    f"{path.name}: duplicate top-level key {key!r} across yaml blocks"
                )
            merged[key] = value
    return merged, parse_pipe_tables(text)


def dig(mapping, *keys, default=None):
    """Walk nested mappings by key path, returning `default` on any miss."""
    node = mapping
    for key in keys:
        if not isinstance(node, dict) or key not in node:
            return default
        node = node[key]
    return node
