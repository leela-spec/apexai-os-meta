from __future__ import annotations

import fnmatch
import json
import os
import re
import shutil
import stat
import subprocess
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

from ..errors import ApexKBError
from ..extractors import EXTRACTION_VERSION, extract_for_policy
from ..io import (
    atomic_json,
    atomic_ndjson,
    atomic_text,
    canonical_hash,
    iter_ndjson,
    load_json,
    safe_relative,
    sha256_bytes,
    sha256_file,
    utc_now,
    validate_schema,
)

PHASE0_SCHEMA = "apex.kb.phase0.v2"
TOKEN_RE = re.compile(r"[^\W_]+(?:[-'][^\W_]+)*", re.UNICODE)
MARKDOWN_EXTENSIONS = {".md", ".markdown", ".mdx"}
FIELD_WEIGHTS = {"path": 16, "filename": 18, "frontmatter_title": 16, "title": 14, "h1": 15, "heading": 12, "link": 8, "reference": 8, "identifier_co_occurrence": 6, "body": 3}
TERM_WEIGHTS = {"primary": 5, "alias": 4, "supporting": 1, "ambiguous": 0, "negative": -3}
CLASS_ORDER = {"core": 0, "contextual": 1, "incidental": 2, "blocked": 3}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    # Treat punctuation and path separators as word boundaries so phrases such as
    # "skill tree" match "skill-tree.md" without becoming substring matches.
    value = re.sub(r"[^\w\s]+", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def tokens(value: str) -> list[str]:
    return [match.group(0).casefold() for match in TOKEN_RE.finditer(unicodedata.normalize("NFKC", value)) if len(match.group(0)) > 1]


def source_id(repository: str, repository_path: str) -> str:
    return "src-" + sha256_bytes(f"{repository}\0{repository_path}".encode("utf-8"))[:16]


def _matches_exclusion(repository_path: str, rules: list[dict[str, str]]) -> tuple[bool, str | None, str | None]:
    normalized_path = repository_path.replace("\\", "/")
    for index, rule in enumerate(rules, 1):
        pattern = str(rule["path"]).replace("\\", "/").rstrip("/")
        if normalized_path == pattern or normalized_path.startswith(pattern + "/") or fnmatch.fnmatch(normalized_path, pattern):
            return True, str(rule["reason"]), str(rule.get("rule_id") or f"exclusion-{index:03d}")
    return False, None, None


def _iter_files(
    source_root: Path,
    folders: list[dict[str, str]],
    errors: list[dict[str, str]] | None = None,
) -> Iterable[tuple[str, Path]]:
    seen: set[Path] = set()
    for folder in folders:
        configured = folder["configured"]
        root = Path(folder["resolved"])

        def record_walk_error(error: OSError) -> None:
            if errors is not None:
                errors.append({"path": str(error.filename or root), "error": str(error)})

        for dirpath, dirnames, filenames in os.walk(root, followlinks=False, onerror=record_walk_error):
            dirnames[:] = sorted(name for name in dirnames if not (Path(dirpath) / name).is_symlink())
            for filename in sorted(filenames):
                path = Path(dirpath) / filename
                resolved = path.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                repository_path = safe_relative(resolved, source_root)
                yield configured, path


def _git_file_dates(source_root: Path, folders: list[dict[str, str]], enabled: bool) -> tuple[dict[str, dict[str, str]], str | None]:
    if not enabled:
        return {}, None
    command = [
        "git", "-C", str(source_root), "log", "--format=@@@%H\t%cI", "--name-only", "--no-renames", "--",
        *[item["configured"] for item in folders],
    ]
    try:
        output = subprocess.run(command, check=True, text=True, capture_output=True, timeout=180).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        return {}, str(exc)
    current_commit = None
    current_date = None
    mapping: dict[str, dict[str, str]] = {}
    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("@@@"):
            payload = line[3:].split("\t", 1)
            current_commit = payload[0]
            current_date = payload[1] if len(payload) > 1 else ""
            continue
        path = line.replace("\\", "/")
        if current_commit and path not in mapping:
            mapping[path] = {"commit": current_commit, "date": current_date or ""}
    return mapping, None


def _version_signals(repository_path: str) -> list[str]:
    stem = Path(repository_path).stem
    patterns = [
        (r"(?i)\bv(?:ersion)?[ _-]*(\d+(?:\.\d+)*)\b", "version"),
        (r"(?i)\b(draft|final|prototype|deprecated|legacy|archive|old|new|current)\b", "lifecycle_word"),
        (r"\b(20\d{2}[-_](?:0[1-9]|1[0-2])[-_](?:0[1-9]|[12]\d|3[01]))\b", "date"),
    ]
    values: list[str] = []
    for pattern, kind in patterns:
        for match in re.finditer(pattern, stem):
            values.append(f"{kind}:{match.group(0)}")
    return values


def _custody_path(run_root: Path, manifest: dict[str, Any], record: dict[str, Any], path: Path) -> str | None:
    mode = manifest["run_options"]["source_handling"]
    if mode == "pointer_only":
        return None
    if mode == "copy_into_kb":
        target = run_root / "raw" / "sources" / record["repository_path"]
    elif mode == "snapshot_copy":
        target = run_root / "raw" / "snapshots" / manifest["run_id"] / record["repository_path"]
    else:
        raise ApexKBError("source_handling_unknown", f"Unknown source handling mode: {mode}")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if not target.is_file():
            raise ApexKBError("custody_target_not_file", f"Custody target is not a regular file: {target}")
        existing_hash = sha256_file(target)
        if existing_hash != record["sha256"]:
            raise ApexKBError(
                "custody_collision",
                f"Refusing to overwrite a different file in source custody: {target}",
                {"target": str(target), "expected_sha256": record["sha256"], "actual_sha256": existing_hash},
            )
        return target.relative_to(run_root).as_posix()
    shutil.copy2(path, target)
    if sha256_file(target) != record["sha256"]:
        target.unlink(missing_ok=True)
        raise ApexKBError("custody_hash_mismatch", f"Copied source hash mismatch: {path}")
    return target.relative_to(run_root).as_posix()

def _frontmatter(lines: list[str]) -> tuple[dict[str, Any], int, list[str]]:
    if not lines or lines[0].strip() != "---":
        return {}, 0, []
    end = None
    for index in range(1, min(len(lines), 400)):
        if lines[index].strip() in {"---", "..."}:
            end = index
            break
    if end is None:
        return {}, 0, ["unterminated_frontmatter"]
    raw = "\n".join(lines[1:end])
    try:
        value = yaml.safe_load(raw) or {}
        if not isinstance(value, dict):
            return {}, end + 1, ["frontmatter_not_mapping"]
        return value, end + 1, []
    except yaml.YAMLError as exc:
        return {}, end + 1, [f"frontmatter_parse_error:{exc}"]


def _markdown_structure(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    frontmatter, body_start, warnings = _frontmatter(lines)
    headings: list[dict[str, Any]] = []
    links: list[dict[str, Any]] = []
    references: list[dict[str, Any]] = []
    fence = False
    fence_marker = ""
    heading_re = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    wiki_re = re.compile(r"\[\[([^\]]+)\]\]")
    backtick_re = re.compile(r"`([^`\n]+)`")
    for line_no, line in enumerate(lines, 1):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not fence:
                fence, fence_marker = True, marker
            elif marker == fence_marker:
                fence, fence_marker = False, ""
            continue
        if fence or line_no <= body_start:
            continue
        match = heading_re.match(line)
        if match:
            headings.append({"level": len(match.group(1)), "text": match.group(2).strip(), "line": line_no})
        for match in link_re.finditer(line):
            links.append({"kind": "markdown", "label": match.group(1), "target": match.group(2), "line": line_no})
        for match in wiki_re.finditer(line):
            links.append({"kind": "wikilink", "label": match.group(1), "target": match.group(1), "line": line_no})
        for match in backtick_re.finditer(line):
            raw = match.group(1).strip()
            if ("/" in raw or "\\" in raw) and not re.match(r"^[a-z]+://", raw, flags=re.I):
                references.append({"kind": "repository_reference", "label": raw, "target": raw, "line": line_no})
    for index, heading in enumerate(headings):
        heading["end_line"] = headings[index + 1]["line"] - 1 if index + 1 < len(headings) else len(lines)
    frontmatter_title = None
    for key in ("title", "name", "subject"):
        if key in frontmatter and isinstance(frontmatter[key], (str, int, float)):
            frontmatter_title = str(frontmatter[key])
            break
    h1 = next((item["text"] for item in headings if item["level"] == 1), None)
    return {
        "frontmatter": frontmatter,
        "frontmatter_title": frontmatter_title,
        "title": frontmatter_title,
        "h1": h1,
        "headings": headings,
        "links": links,
        "references": references,
        "body_start_line": body_start + 1,
        "parser_warnings": warnings,
    }

def _generic_structure(path: Path, extraction: dict[str, Any]) -> dict[str, Any]:
    title = path.stem
    headings = []
    for segment in extraction["segments"][:200]:
        text = segment["text"].strip()
        if len(text) <= 120 and (text.endswith(":") or text.isupper()):
            headings.append({"level": 2, "text": text.rstrip(":"), "pointer": segment["pointer"]})
    return {
        "frontmatter": {},
        "frontmatter_title": None,
        "title": title,
        "h1": None,
        "headings": headings,
        "links": [],
        "references": [],
        "body_start_line": 1,
        "parser_warnings": [],
    }

def _field_segments(record: dict[str, Any], structure: dict[str, Any], extraction: dict[str, Any]) -> dict[str, list[tuple[str, str]]]:
    fields: dict[str, list[tuple[str, str]]] = {
        "path": [("path", record["repository_path"])],
        "filename": [("filename", Path(record["repository_path"]).name)],
        "frontmatter_title": [("frontmatter:title", structure.get("frontmatter_title") or "")],
        "title": [("title", structure.get("title") or "")],
        "h1": [("h1", structure.get("h1") or "")],
        "heading": [],
        "link": [],
        "reference": [],
        "identifier_co_occurrence": [],
        "body": [],
    }
    for item in structure.get("headings", []):
        pointer = f"line:{item['line']}" if "line" in item else item.get("pointer", "heading")
        fields["heading"].append((pointer, item["text"]))
    for item in structure.get("links", []):
        fields["link"].append((f"line:{item.get('line', '?')}", f"{item.get('label', '')} {item.get('target', '')}"))
    for item in structure.get("references", []):
        fields["reference"].append((f"line:{item.get('line', '?')}", f"{item.get('label', '')} {item.get('target', '')}"))
    excluded_line_numbers = {
        int(item["line"])
        for item in [*structure.get("headings", []), *structure.get("links", []), *structure.get("references", [])]
        if isinstance(item.get("line"), int)
    }
    body_start = int(structure.get("body_start_line") or 1)
    body_segments: list[tuple[str, str]] = []
    for item in extraction.get("segments", []):
        pointer = item["pointer"]
        match = re.fullmatch(r"line:(\d+)", pointer)
        if match:
            line_no = int(match.group(1))
            if line_no < body_start or line_no in excluded_line_numbers:
                continue
        body_segments.append((pointer, item["text"]))
    fields["body"] = body_segments
    return fields

def _bounded_count(needle: str, haystack: str) -> int:
    if not needle or not haystack:
        return 0
    pattern = re.compile(r"(?<!\w)" + re.escape(needle) + r"(?!\w)", flags=re.UNICODE)
    return sum(1 for _ in pattern.finditer(haystack))


def _occurrences(term: str, values: list[tuple[str, str]]) -> tuple[int, list[str]]:
    needle = normalize(term)
    if not needle:
        return 0, []
    count = 0
    pointers: list[str] = []
    for pointer, value in values:
        found = _bounded_count(needle, normalize(value))
        if found:
            count += found
            if len(pointers) < 25:
                pointers.append(pointer)
    return count, pointers


def _rule_matches(repository_path: str, pattern: str) -> bool:
    normalized_path = repository_path.replace("\\", "/")
    normalized_pattern = str(pattern).replace("\\", "/").rstrip("/")
    return (
        normalized_path == normalized_pattern
        or normalized_path.startswith(normalized_pattern + "/")
        or fnmatch.fnmatch(normalized_path, normalized_pattern)
    )


def _configured_hints(repository_path: str, rules: list[dict[str, Any]], prefix: str) -> list[dict[str, Any]]:
    evidence: list[dict[str, Any]] = []
    for index, rule in enumerate(rules, 1):
        if _rule_matches(repository_path, str(rule["path"])):
            item = {
                "rule_id": str(rule.get("rule_id") or f"{prefix}-{index:03d}"),
                "path": str(rule["path"]),
                "hint": str(rule["hint"]),
            }
            if "score" in rule:
                item["score"] = int(rule["score"])
            evidence.append(item)
    return evidence


def _lifecycle_hints(repository_path: str, rules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return _configured_hints(repository_path, rules, "lifecycle-hint")

def _family_key(path: str) -> str:
    stem = Path(path).stem.casefold()
    stem = re.sub(r"\b(v(?:ersion)?\s*\d+(?:\.\d+)*|draft|final|copy|old|new|\d{4}[-_]?\d{2}[-_]?\d{2})\b", " ", stem)
    stem = re.sub(r"[^a-z0-9]+", " ", stem)
    return re.sub(r"\s+", " ", stem).strip()


def _duplicate_map(records: list[dict[str, Any]], normalized_hashes: dict[str, str]) -> dict[str, Any]:
    exact: dict[str, list[str]] = defaultdict(list)
    normalized: dict[str, list[str]] = defaultdict(list)
    families: dict[str, list[str]] = defaultdict(list)
    by_id = {record["source_id"]: record for record in records}
    for record in records:
        if record["inclusion_state"] == "excluded":
            continue
        exact[record["sha256"]].append(record["source_id"])
        if record["source_id"] in normalized_hashes:
            normalized[normalized_hashes[record["source_id"]]].append(record["source_id"])
        key = _family_key(record["repository_path"])
        if key:
            families[key].append(record["source_id"])

    def group(kind_key: str, digest: str, source_ids: list[str]) -> dict[str, Any]:
        ordered = sorted(source_ids, key=lambda source: by_id[source]["repository_path"].casefold())
        representative = ordered[0]
        return {
            kind_key: digest,
            "representative_source_id": representative,
            "representative_repository_path": by_id[representative]["repository_path"],
            "source_ids": ordered,
            "repository_paths": [by_id[source]["repository_path"] for source in ordered],
        }

    return {
        "schema": "apex.kb.duplicate-map.v2",
        "exact_hash_groups": [group("sha256", key, value) for key, value in sorted(exact.items()) if len(value) > 1],
        "normalized_text_groups": [group("normalized_sha256", key, value) for key, value in sorted(normalized.items()) if len(value) > 1],
        "possible_filename_families": [group("family_key", key, value) for key, value in sorted(families.items()) if len(value) > 1],
        "automatic_supersession": False,
        "representative_rule": "lexicographically_smallest_repository_path",
    }

def _duplicate_lookup(duplicate_map: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    lookup: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for kind in ("exact_hash_groups", "normalized_text_groups", "possible_filename_families"):
        for group in duplicate_map[kind]:
            for source in group["source_ids"]:
                lookup[source].append({"relationship": kind, **group})
    return lookup


def _topic_identifiers(topic: dict[str, Any]) -> list[str]:
    ordered: list[str] = []
    seen: set[str] = set()
    for key in ("primary_phrases", "aliases", "supporting_terms"):
        for raw in topic[key]:
            normalized = normalize(raw)
            if normalized and normalized not in seen:
                ordered.append(normalized)
                seen.add(normalized)
    return ordered


def _co_occurrence_segments(topic: dict[str, Any], fields: dict[str, list[tuple[str, str]]]) -> list[tuple[str, str, list[str]]]:
    identifiers = _topic_identifiers(topic)
    rows: list[tuple[str, str, list[str]]] = []
    for field in ("frontmatter_title", "title", "h1", "heading", "body", "link", "reference"):
        for pointer, value in fields.get(field, []):
            normalized_value = normalize(value)
            matched = [identifier for identifier in identifiers if _bounded_count(identifier, normalized_value)]
            if len(set(matched)) >= 2:
                rows.append((f"{field}:{pointer}", value, sorted(set(matched))))
    return rows


def _build_postings(structures: dict[str, dict[str, Any]], topics: list[dict[str, Any]]) -> list[dict[str, Any]]:
    configured_terms = {
        normalize(term)
        for topic in topics
        for key in ("primary_phrases", "aliases", "supporting_terms", "negative_terms", "ambiguous_terms")
        for term in topic[key]
        if normalize(term)
    }
    rows: list[dict[str, Any]] = []
    for source, item in sorted(structures.items(), key=lambda pair: pair[1]["repository_path"].casefold()):
        for field, segments in item["fields"].items():
            if field == "identifier_co_occurrence":
                continue
            counts: Counter[str] = Counter()
            pointer_map: dict[str, list[str]] = defaultdict(list)
            for pointer, value in segments:
                for token in tokens(value):
                    counts[token] += 1
                    if pointer not in pointer_map[token] and len(pointer_map[token]) < 10:
                        pointer_map[token].append(pointer)
                normalized_value = normalize(value)
                for term in configured_terms:
                    if " " not in term:
                        continue
                    found = _bounded_count(term, normalized_value)
                    if found:
                        counts[term] += found
                        if pointer not in pointer_map[term] and len(pointer_map[term]) < 10:
                            pointer_map[term].append(pointer)
            for term, count in sorted(counts.items()):
                rows.append({"term": term, "source_id": source, "field": field, "count": count, "pointers": pointer_map[term]})
        for topic in topics:
            co_occurrences = _co_occurrence_segments(topic, item["fields"])
            term_counts: Counter[str] = Counter()
            term_pointers: dict[str, list[str]] = defaultdict(list)
            for pointer, _value, matched in co_occurrences:
                for term in matched:
                    term_counts[term] += 1
                    if pointer not in term_pointers[term] and len(term_pointers[term]) < 10:
                        term_pointers[term].append(pointer)
            for term, count in sorted(term_counts.items()):
                rows.append({
                    "term": term,
                    "topic_id": topic["topic_id"],
                    "source_id": source,
                    "field": "identifier_co_occurrence",
                    "count": count,
                    "pointers": term_pointers[term],
                })
    return sorted(rows, key=lambda row: (row["term"], row["source_id"], row["field"], row.get("topic_id", "")))

def _candidate_map(topic: dict[str, Any], records_by_id: dict[str, dict[str, Any]], structures: dict[str, dict[str, Any]], duplicates: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    term_sets = {
        "primary": topic["primary_phrases"],
        "alias": topic["aliases"],
        "supporting": topic["supporting_terms"],
        "ambiguous": topic["ambiguous_terms"],
        "negative": topic["negative_terms"],
    }
    candidates: list[dict[str, Any]] = []
    suppressed: list[dict[str, Any]] = []
    for source, record in records_by_id.items():
        if record["inclusion_state"] == "excluded":
            continue
        fields = structures.get(source, {}).get("fields") or {
            "path": [("path", record["repository_path"])],
            "filename": [("filename", Path(record["repository_path"]).name)],
            "frontmatter_title": [], "title": [], "h1": [], "heading": [], "link": [], "reference": [], "identifier_co_occurrence": [], "body": [],
        }
        reasons: list[dict[str, Any]] = []
        positive_score = 0
        negative_score = 0
        strong_match = False
        supporting_match_count = 0
        for term_type, term_values in term_sets.items():
            for term in term_values:
                for field, values in fields.items():
                    if field == "identifier_co_occurrence":
                        continue
                    count, pointers = _occurrences(term, values)
                    if not count:
                        continue
                    reason_score = FIELD_WEIGHTS[field] * TERM_WEIGHTS[term_type] * min(count, 10)
                    if term_type == "ambiguous":
                        reason_score = 0
                    if term_type == "negative":
                        negative_score += abs(reason_score)
                    else:
                        positive_score += reason_score
                    if term_type in {"primary", "alias"}:
                        strong_match = True
                    if term_type == "supporting":
                        supporting_match_count += 1
                    reasons.append({"term": term, "term_type": term_type, "field": field, "count": count, "score": reason_score, "pointers": pointers})
        co_occurrences = _co_occurrence_segments(topic, fields)
        if co_occurrences:
            pointers = [pointer for pointer, _value, _matched in co_occurrences[:25]]
            co_score = FIELD_WEIGHTS["identifier_co_occurrence"] * min(len(co_occurrences), 10)
            positive_score += co_score
            reasons.append({
                "term": "<configured-identifiers>",
                "term_type": "cooccurrence",
                "field": "identifier_co_occurrence",
                "count": len(co_occurrences),
                "score": co_score,
                "pointers": pointers,
            })
        ambiguous_only = bool(reasons) and not strong_match and not supporting_match_count and not co_occurrences and all(item["term_type"] in {"ambiguous", "negative"} for item in reasons)
        authority_hint_score = int(record.get("authority_hint_score", 0))
        lexical_score = max(0, positive_score - negative_score)
        score = max(0, lexical_score + authority_hint_score)
        if ambiguous_only:
            suppressed.append({
                "source_id": source,
                "repository_path": record["repository_path"],
                "reason": "ambiguous_or_negative_terms_without_strong_or_supporting_evidence",
                "match_reasons": sorted(reasons, key=lambda item: (-item["score"], item["field"], normalize(item["term"]))),
            })
            continue
        if lexical_score <= 0:
            continue
        core_signal = any(item["term_type"] in {"primary", "alias"} and item["field"] in {"path", "filename", "frontmatter_title", "title", "h1", "heading"} for item in reasons)
        contextual_signal = strong_match or supporting_match_count >= 2 or bool(co_occurrences)
        if record["extraction_status"] in {"unsupported", "error", "metadata_only"}:
            candidate_class = "blocked"
        elif core_signal:
            candidate_class = "core"
        elif contextual_signal:
            candidate_class = "contextual"
        else:
            candidate_class = "incidental"
        duplicate_relationships = duplicates.get(source, [])
        representative = next((item for item in duplicate_relationships if item["relationship"] in {"exact_hash_groups", "normalized_text_groups"}), None)
        candidates.append(
            {
                "source_id": source,
                "repository_path": record["repository_path"],
                "absolute_path": record["absolute_path"],
                "source_format": record["extraction_format"] or record["extension"].lstrip(".") or "unknown",
                "size_bytes": record["bytes"],
                "content_hash": record["sha256"],
                "candidate_class": candidate_class,
                "score": score,
                "score_vector": {
                    "class_order": CLASS_ORDER[candidate_class],
                    "lexical_positive_score": positive_score,
                    "negative_penalty": negative_score,
                    "configured_authority_hint_score": authority_hint_score,
                    "git_last_changed": record["git_last_changed"],
                    "version_signals": record["version_signals"],
                    "reason_count": len(reasons),
                },
                "match_reasons": sorted(reasons, key=lambda item: (-item["score"], item["field"], normalize(item["term"]))),
                "lifecycle_hints": record.get("lifecycle_hints", []),
                "lifecycle_hint_evidence": record.get("lifecycle_hint_evidence", []),
                "authority_hints": record.get("authority_hints", []),
                "version_signals": record["version_signals"],
                "git_last_changed": record["git_last_changed"],
                "derived_text_path": record["derived_text_path"],
                "custody_path": record["custody_path"],
                "extraction_status": record["extraction_status"],
                "extraction_error": record["extraction_error"],
                "duplicate_representative_source_id": representative.get("representative_source_id") if representative else source,
                "duplicate_representative_repository_path": representative.get("representative_repository_path") if representative else record["repository_path"],
                "duplicate_relationships": duplicate_relationships,
                "semantic_disposition": "pending",
                "phase0_semantic_claim": None,
            }
        )
    candidates.sort(key=lambda item: (CLASS_ORDER[item["candidate_class"]], -item["score"], item["repository_path"].casefold()))
    for rank, candidate in enumerate(candidates, 1):
        candidate["rank"] = rank
    return {
        "schema": "apex.kb.topic-map.v2",
        "topic": topic,
        "candidate_count": len(candidates),
        "candidate_set_truncated": False,
        "suppressed_ambiguous_match_count": len(suppressed),
        "suppressed_ambiguous_matches": sorted(suppressed, key=lambda item: item["repository_path"].casefold()),
        "phase0_semantic_authority": False,
        "candidates": candidates,
    }

def _topic_markdown(topic_map: dict[str, Any]) -> str:
    topic = topic_map["topic"]
    lines = [
        f"# Topic map — {topic['name']}",
        "",
        f"- Topic ID: `{topic['topic_id']}`",
        f"- Exhaustive candidates: **{topic_map['candidate_count']}**",
        "- Canonical set truncated: **no**",
        "",
        "## Read-first projection",
        "",
        "This projection is bounded for navigation. The JSON file is the exhaustive authoritative candidate set.",
        "",
    ]
    for candidate in topic_map["candidates"][:30]:
        reasons = "; ".join(f"{item['term_type']} `{item['term']}` in {item['field']} x{item['count']}" for item in candidate["match_reasons"][:4])
        lines.append(f"{candidate['rank']}. `{candidate['repository_path']}` — {candidate['candidate_class']}, score {candidate['score']} — {reasons}")
    lines.extend(["", "## Complete candidate ledger", ""])
    for candidate in topic_map["candidates"]:
        pointers = []
        for reason in candidate["match_reasons"]:
            pointers.extend(f"{reason['field']}:{pointer}" for pointer in reason["pointers"][:3])
        lines.append(f"- `{candidate['source_id']}` `{candidate['repository_path']}` — class `{candidate['candidate_class']}`, score `{candidate['score']}`; pointers: {', '.join(pointers[:10]) or 'none'}")
    return "\n".join(lines) + "\n"


def _link_graph(records: list[dict[str, Any]], structures: dict[str, dict[str, Any]], graph_depth: str) -> dict[str, Any]:
    by_path = {item["repository_path"].casefold(): item["source_id"] for item in records}
    nodes = [
        {"source_id": item["source_id"], "repository_path": item["repository_path"], "inclusion_state": item["inclusion_state"]}
        for item in records
    ]
    edges: list[dict[str, Any]] = []
    if graph_depth == "none":
        return {"schema": "apex.kb.link-graph.v2", "graph_depth": graph_depth, "nodes": nodes, "edges": edges}
    for source_id_value, structure in structures.items():
        source_path = Path(structure["repository_path"])
        for link in structure.get("links", []):
            raw_target = str(link.get("target", "")).split("#", 1)[0].strip()
            target_id = None
            resolved = None
            if raw_target and not re.match(r"^[a-z]+://", raw_target, flags=re.I):
                candidate = (source_path.parent / raw_target).as_posix()
                candidate = str(Path(candidate)).replace("\\", "/")
                target_id = by_path.get(candidate.casefold())
                resolved = candidate
            edges.append({
                "edge_type": link.get("kind", "link"),
                "from_source_id": source_id_value,
                "to_source_id": target_id,
                "raw_target": raw_target,
                "resolved_repository_path": resolved,
                "pointer": f"line:{link.get('line', '?')}",
            })
        if graph_depth == "process":
            frontmatter = structure.get("frontmatter") or {}
            for field in ("depends_on", "inputs", "outputs", "consumes", "produces", "next", "related", "owner"):
                raw = frontmatter.get(field)
                if raw is None:
                    continue
                values = raw if isinstance(raw, list) else [raw]
                for value in values:
                    edges.append({
                        "edge_type": f"frontmatter_{field}",
                        "from_source_id": source_id_value,
                        "to_source_id": None,
                        "raw_target": str(value),
                        "resolved_repository_path": None,
                        "pointer": f"frontmatter:{field}",
                    })
    return {"schema": "apex.kb.link-graph.v2", "graph_depth": graph_depth, "nodes": nodes, "edges": edges}


def _profile(records: list[dict[str, Any]], duplicate_map: dict[str, Any]) -> str:
    by_ext = Counter(record["extension"] or "[none]" for record in records)
    by_status = Counter(record["extraction_status"] for record in records)
    lines = [
        "# Corpus profile",
        "",
        f"- Files inventoried: **{len(records)}**",
        f"- Included: **{sum(record['inclusion_state'] == 'included' for record in records)}**",
        f"- Excluded: **{sum(record['inclusion_state'] == 'excluded' for record in records)}**",
        f"- Bytes: **{sum(record['bytes'] for record in records)}**",
        f"- Exact duplicate groups: **{len(duplicate_map['exact_hash_groups'])}**",
        f"- Normalized-text duplicate groups: **{len(duplicate_map['normalized_text_groups'])}**",
        "",
        "## Extraction status",
        "",
    ]
    lines.extend(f"- `{key}`: {value}" for key, value in sorted(by_status.items()))
    lines.extend(["", "## Extensions", ""])
    lines.extend(f"- `{key}`: {value}" for key, value in sorted(by_ext.items()))
    largest = sorted(records, key=lambda item: item["bytes"], reverse=True)[:20]
    lines.extend(["", "## Largest files", ""])
    lines.extend(f"- `{item['repository_path']}` — {item['bytes']} bytes" for item in largest)
    errors = [item for item in records if item["extraction_status"] in {"unsupported", "error", "metadata_only"} and item["inclusion_state"] == "included"]
    lines.extend(["", "## Extraction warnings and blocked files", ""])
    lines.extend(f"- `{item['repository_path']}` — {item['extraction_status']}: {item['extraction_error'] or ', '.join(item['extraction_warnings']) or 'metadata only'}" for item in errors)
    if not errors:
        lines.append("- None")
    return "\n".join(lines) + "\n"


def _navigation_report(manifest: dict[str, Any], records: list[dict[str, Any]], topic_maps: dict[str, dict[str, Any]], duplicate_map: dict[str, Any]) -> str:
    blocked = [item for item in records if item["inclusion_state"] == "included" and item["extraction_status"] in {"unsupported", "error", "metadata_only"}]
    topic_membership: dict[str, list[str]] = defaultdict(list)
    for topic_id, topic_map in topic_maps.items():
        for candidate in topic_map["candidates"]:
            topic_membership[candidate["source_id"]].append(topic_id)
    reusable = [source for source, topics in topic_membership.items() if len(topics) > 1]
    by_id = {item["source_id"]: item for item in records}
    lines = [
        "# Phase 0 navigation report",
        "",
        f"Run: `{manifest['run_id']}`",
        "",
        "## Corpus accountability",
        "",
        f"- Every discovered file is represented in `source-inventory.ndjson`: **{len(records)}** files.",
        f"- Explicitly excluded: **{sum(item['inclusion_state'] == 'excluded' for item in records)}**.",
        f"- Included but extraction-blocked/metadata-only: **{len(blocked)}**.",
        f"- Exact duplicate groups: **{len(duplicate_map['exact_hash_groups'])}**.",
        f"- Normalized-text duplicate groups: **{len(duplicate_map['normalized_text_groups'])}**.",
        f"- Possible filename/version families: **{len(duplicate_map['possible_filename_families'])}**.",
        "- Topic candidate JSON sets are exhaustive and never top-N truncated.",
        "- Configured path hints are inspectable routing evidence only; they do not establish semantic authority.",
        "",
        "## Extraction blockers",
        "",
    ]
    if blocked:
        for item in blocked[:100]:
            lines.append(f"- `{item['repository_path']}` — `{item['extraction_status']}` — {item['extraction_error'] or ', '.join(item['extraction_warnings']) or 'metadata only'}")
    else:
        lines.append("- None")
    lines.extend(["", "## Duplicate and version families", ""])
    for label, key in (("Exact", "exact_hash_groups"), ("Normalized", "normalized_text_groups"), ("Filename/version", "possible_filename_families")):
        lines.append(f"### {label}")
        lines.append("")
        groups = duplicate_map[key]
        if not groups:
            lines.append("- None")
        for group in groups[:50]:
            lines.append(f"- Representative `{group['representative_repository_path']}`; members: {', '.join(f'`{path}`' for path in group['repository_paths'])}")
        lines.append("")
    lines.extend(["## Cross-topic reusable sources", ""])
    if reusable:
        for source in sorted(reusable, key=lambda value: by_id[value]["repository_path"].casefold()):
            lines.append(f"- `{by_id[source]['repository_path']}` — topics: {', '.join(sorted(topic_membership[source]))}")
    else:
        lines.append("- None")
    lines.extend(["", "## Topic routes", ""])
    for topic_id, topic_map in topic_maps.items():
        classes = Counter(item["candidate_class"] for item in topic_map["candidates"])
        lines.append(f"### {topic_map['topic']['name']} (`{topic_id}`)")
        lines.append("")
        lines.append(f"- Candidates: **{topic_map['candidate_count']}** — core {classes['core']}, contextual {classes['contextual']}, incidental {classes['incidental']}, blocked {classes['blocked']}.")
        lines.append(f"- Suppressed ambiguous-only matches: **{topic_map['suppressed_ambiguous_match_count']}**.")
        lines.append(f"- Authoritative map: `manifests/phase0/topic-maps/{topic_id}.json`")
        lines.append(f"- Compact route: `manifests/phase0/topic-maps/{topic_id}.md`")
        lines.append("- Read-first families:")
        families: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for candidate in topic_map["candidates"]:
            family = candidate["duplicate_representative_repository_path"]
            families[family].append(candidate)
        for family, members in list(sorted(families.items(), key=lambda pair: (CLASS_ORDER[pair[1][0]["candidate_class"]], -pair[1][0]["score"], pair[0].casefold())))[:10]:
            first = members[0]
            lines.append(f"  - `{family}` — {first['candidate_class']}, score {first['score']}, family members {len(members)}")
        lines.append("- Recommended semantic batches:")
        lines.append(f"  - Core full reads: {classes['core']}")
        lines.append(f"  - Contextual targeted reads: {classes['contextual']}")
        lines.append(f"  - Incidental disposition checks: {classes['incidental']}")
        lines.append(f"  - Blocked/unreadable review: {classes['blocked']}")
        lines.append("")
    lines.extend([
        "## Unresolved deterministic ambiguities",
        "",
        "Ambiguous-only matches are preserved in each JSON topic map under `suppressed_ambiguous_matches`; they are not silently promoted to semantic workload.",
        "",
        "## Semantic handoff rule",
        "",
        "Phase 0 rank is navigation evidence, not semantic authority. Every candidate must receive a durable semantic disposition in Phase 1. Unopened sources may not be represented as evidence.",
    ])
    return "\n".join(lines) + "\n"

def _write_current_and_run(run_root: Path, manifest: dict[str, Any], relative: str, writer: Any, value: Any) -> tuple[str, str]:
    current = run_root / relative
    run_copy = run_root / manifest["artifact_layout"]["run_dir"] / relative
    writer(current, value)
    writer(run_copy, value)
    return str(current.relative_to(run_root)), str(run_copy.relative_to(run_root))


def _change_report(previous_rows: list[dict[str, Any]], current_rows: list[dict[str, Any]], old_topic_maps: dict[str, dict[str, Any]], new_topic_maps: dict[str, dict[str, Any]]) -> dict[str, Any]:
    previous = {item["repository_path"]: item for item in previous_rows}
    current = {item["repository_path"]: item for item in current_rows}
    added = sorted(set(current) - set(previous))
    deleted = sorted(set(previous) - set(current))
    changed = sorted(
        path for path in set(current) & set(previous)
        if current[path]["sha256"] != previous[path]["sha256"]
        or current[path]["inclusion_state"] != previous[path]["inclusion_state"]
        or current[path].get("extraction_status") != previous[path].get("extraction_status")
    )
    newly_unreadable = sorted(
        path for path in set(current) & set(previous)
        if previous[path].get("extraction_status") not in {"unsupported", "error", "metadata_only"}
        and current[path].get("extraction_status") in {"unsupported", "error", "metadata_only"}
    )
    deleted_by_hash: dict[str, list[str]] = defaultdict(list)
    added_by_hash: dict[str, list[str]] = defaultdict(list)
    for path in deleted:
        deleted_by_hash[previous[path]["sha256"]].append(path)
    for path in added:
        added_by_hash[current[path]["sha256"]].append(path)
    moved: list[dict[str, str]] = []
    for digest in sorted(set(deleted_by_hash) & set(added_by_hash)):
        old_paths = sorted(deleted_by_hash[digest])
        new_paths = sorted(added_by_hash[digest])
        for old_path, new_path in zip(old_paths, new_paths):
            moved.append({"from": old_path, "to": new_path, "sha256": digest})
    unchanged = sorted(path for path in set(current) & set(previous) if path not in changed)
    affected: dict[str, dict[str, Any]] = {}
    changed_set = set(added + deleted + changed)
    for topic_id, new_map in new_topic_maps.items():
        old_candidates = {item["repository_path"] for item in old_topic_maps.get(topic_id, {}).get("candidates", [])}
        new_candidates = {item["repository_path"] for item in new_map["candidates"]}
        relevant = sorted(changed_set & (old_candidates | new_candidates))
        topic_contract_changed = old_topic_maps.get(topic_id, {}).get("topic") != new_map.get("topic")
        affected[topic_id] = {
            "affected": bool(relevant) or old_candidates != new_candidates or topic_contract_changed,
            "changed_candidate_paths": relevant,
            "candidate_set_changed": old_candidates != new_candidates,
            "topic_contract_changed": topic_contract_changed,
        }
    return {
        "schema": "apex.kb.impact-report.v2",
        "added": added,
        "deleted": deleted,
        "moved": moved,
        "changed": changed,
        "newly_unreadable": newly_unreadable,
        "unchanged_count": len(unchanged),
        "affected_topics": affected,
        "unchanged_capsules_reusable": True,
        "content_identity_preserved_across_moves": True,
    }

def build_corpus_intelligence(run_root: Path, manifest: dict[str, Any], previous_run: dict[str, Any] | None = None) -> dict[str, Any]:
    started = manifest["created_at"]
    source_root = Path(manifest["source"]["resolved_root"])
    exclusions = manifest.get("exclusions", [])
    records: list[dict[str, Any]] = []
    structures: dict[str, dict[str, Any]] = {}
    normalized_hashes: dict[str, str] = {}
    extraction_root = run_root / manifest["artifact_layout"]["run_dir"] / "extracted"
    extraction_root.mkdir(parents=True, exist_ok=True)
    git_dates, git_metadata_error = _git_file_dates(
        source_root, manifest["source"]["resolved_folders"], manifest["run_options"].get("git_metadata", False)
    )
    for configured_folder, path in _iter_files(source_root, manifest["source"]["resolved_folders"]):
        repository_path = safe_relative(path, source_root)
        excluded, exclusion_reason, exclusion_rule = _matches_exclusion(repository_path, exclusions)
        stat = path.stat()
        digest = sha256_file(path)
        sid = source_id(manifest["source"]["repository"], repository_path)
        lifecycle_evidence = _lifecycle_hints(repository_path, manifest.get("lifecycle_hint_rules", []))
        authority_evidence = _configured_hints(repository_path, manifest.get("authority_hint_rules", []), "authority-hint")
        record: dict[str, Any] = {
            "schema": "apex.kb.source-inventory-record.v2",
            "source_id": sid,
            "source_repository": manifest["source"]["repository"],
            "source_folder": configured_folder,
            "repository_path": repository_path,
            "absolute_path": str(path.resolve()),
            "extension": path.suffix.lower(),
            "bytes": stat.st_size,
            "mtime_ns": stat.st_mtime_ns,
            "sha256": digest,
            "inclusion_state": "excluded" if excluded else "included",
            "exclusion_reason": exclusion_reason,
            "exclusion_rule_id": exclusion_rule,
            "is_symlink": path.is_symlink(),
            "extraction_version": EXTRACTION_VERSION,
            "extraction_policy": manifest["run_options"]["non_text"],
            "extraction_status": "not_attempted_excluded" if excluded else "pending",
            "extraction_format": None,
            "extraction_error": None,
            "extraction_warnings": [],
            "extracted_text_chars": 0,
            "segment_count": 0,
            "derived_text_path": None,
            "custody_path": None,
            "lifecycle_hints": [item["hint"] for item in lifecycle_evidence],
            "lifecycle_hint_evidence": lifecycle_evidence,
            "authority_hints": authority_evidence,
            "authority_hint_score": sum(int(item.get("score", 0)) for item in authority_evidence),
            "version_signals": _version_signals(repository_path),
            "git_last_changed": git_dates.get(repository_path),
        }
        if not excluded:
            extraction = extract_for_policy(path, manifest["run_options"]["non_text"])
            record.update(
                {
                    "extraction_status": extraction["status"],
                    "extraction_format": extraction["format"],
                    "extraction_error": extraction["error"],
                    "extraction_warnings": extraction["warnings"],
                    "extracted_text_chars": len(extraction["text"]),
                    "segment_count": len(extraction["segments"]),
                }
            )
            if extraction["text"]:
                text_path = extraction_root / f"{sid}.txt"
                atomic_text(text_path, extraction["text"])
                record["derived_text_path"] = str(text_path.relative_to(run_root))
                normalized_hashes[sid] = sha256_bytes(normalize(extraction["text"]).encode("utf-8"))
            if path.suffix.lower() in MARKDOWN_EXTENSIONS and extraction["status"] == "success":
                structure = _markdown_structure(extraction["text"])
            else:
                structure = _generic_structure(path, extraction)
            structure_record = {
                "schema": "apex.kb.structure-record.v2",
                "source_id": sid,
                "repository_path": repository_path,
                **structure,
                "extraction_status": extraction["status"],
                "fields": _field_segments(record, structure, extraction),
            }
            structures[sid] = structure_record
            record["custody_path"] = _custody_path(run_root, manifest, record, path)
        records.append(record)
    records.sort(key=lambda item: item["repository_path"].casefold())
    records_by_id = {item["source_id"]: item for item in records}
    duplicate_map = _duplicate_map(records, normalized_hashes)
    duplicate_lookup = _duplicate_lookup(duplicate_map)
    postings = _build_postings(structures, manifest["topics"])
    topic_maps = {topic["topic_id"]: _candidate_map(topic, records_by_id, structures, duplicate_lookup) for topic in manifest["topics"]}
    link_graph = _link_graph(records, structures, manifest["run_options"].get("graph_depth", "links"))
    artifacts: list[str] = []
    for relative, writer, value in (
        ("manifests/source-inventory.ndjson", atomic_ndjson, records),
        ("manifests/source-manifest.json", atomic_json, {"schema": "apex.kb.source-manifest.v2", "run_id": manifest["run_id"], "config_hash": manifest["config_hash"], "source_count": len(records), "records": [{key: item[key] for key in ("source_id", "repository_path", "sha256", "inclusion_state", "custody_path", "derived_text_path")} for item in records]}),
        ("manifests/source-payload-manifest.json", atomic_json, {"schema": "apex.kb.source-payload-manifest.v2", "run_id": manifest["run_id"], "source_handling": manifest["run_options"]["source_handling"], "payloads": [{"source_id": item["source_id"], "original_path": item["absolute_path"], "custody_path": item["custody_path"], "sha256": item["sha256"]} for item in records if item["inclusion_state"] == "included"]}),
        ("manifests/phase0/structure-map.ndjson", atomic_ndjson, [{key: value for key, value in item.items() if key != "fields"} for item in structures.values()]),
        ("manifests/phase0/term-postings.ndjson", atomic_ndjson, postings),
        ("manifests/phase0/duplicate-map.json", atomic_json, duplicate_map),
        ("manifests/phase0/link-graph.json", atomic_json, link_graph),
        ("manifests/phase0/heading-map.json", atomic_json, {"schema": "apex.kb.heading-map.v2", "records": [{"source_id": item["source_id"], "repository_path": item["repository_path"], "frontmatter_title": item.get("frontmatter_title"), "title": item.get("title"), "h1": item.get("h1"), "headings": item.get("headings", []), "parser_warnings": item.get("parser_warnings", [])} for item in structures.values()]}),
        ("manifests/phase0/markdown-link-map.json", atomic_json, {"schema": "apex.kb.markdown-link-map.v2", "records": [{"source_id": item["source_id"], "repository_path": item["repository_path"], "links": item.get("links", [])} for item in structures.values()]}),
        ("manifests/phase0/frontmatter-map.json", atomic_json, {"schema": "apex.kb.frontmatter-map.v2", "records": [{"source_id": item["source_id"], "repository_path": item["repository_path"], "frontmatter": item.get("frontmatter", {})} for item in structures.values()]}),
        ("manifests/phase0/corpus-profile.md", atomic_text, _profile(records, duplicate_map)),
    ):
        current, run_copy = _write_current_and_run(run_root, manifest, relative, writer, value)
        artifacts.extend([current, run_copy])
    for topic_id, topic_map in topic_maps.items():
        for extension, writer, value in (
            ("json", atomic_json, topic_map),
            ("md", atomic_text, _topic_markdown(topic_map)),
        ):
            current, run_copy = _write_current_and_run(run_root, manifest, f"manifests/phase0/topic-maps/{topic_id}.{extension}", writer, value)
            artifacts.extend([current, run_copy])
    report = _navigation_report(manifest, records, topic_maps, duplicate_map)
    current, run_copy = _write_current_and_run(run_root, manifest, "manifests/phase0/phase0-navigation-report.md", atomic_text, report)
    artifacts.extend([current, run_copy])
    impact = None
    if previous_run:
        previous_rows = list(iter_ndjson(Path(previous_run["inventory_path"])))
        old_topic_maps = {topic_id: load_json(Path(path)) for topic_id, path in previous_run.get("topic_map_paths", {}).items() if Path(path).is_file()}
        impact = _change_report(previous_rows, records, old_topic_maps, topic_maps)
        atomic_json(run_root / "maintenance" / "impact-report.json", impact)
        atomic_json(run_root / manifest["artifact_layout"]["run_dir"] / "maintenance" / "impact-report.json", impact)
        artifacts.extend(["maintenance/impact-report.json", f"{manifest['artifact_layout']['run_dir']}/maintenance/impact-report.json"])
    summary = {
        "schema": "apex.kb.phase0-summary.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "created_at": manifest["created_at"],
        "file_count": len(records),
        "included_count": sum(item["inclusion_state"] == "included" for item in records),
        "excluded_count": sum(item["inclusion_state"] == "excluded" for item in records),
        "blocked_or_metadata_only_count": sum(item["inclusion_state"] == "included" and item["extraction_status"] in {"unsupported", "error", "metadata_only"} for item in records),
        "total_bytes": sum(item["bytes"] for item in records),
        "topic_candidate_counts": {topic_id: item["candidate_count"] for topic_id, item in topic_maps.items()},
        "candidate_sets_truncated": False,
        "git_metadata_error": git_metadata_error,
        "git_dated_file_count": sum(bool(item["git_last_changed"]) for item in records),
        "link_graph_edge_count": len(link_graph["edges"]),
        "artifacts": artifacts,
        "impact_report": impact,
    }
    current, run_copy = _write_current_and_run(run_root, manifest, "manifests/phase0/phase0-stats.json", atomic_json, summary)
    artifacts.extend([current, run_copy])
    if manifest["run_options"]["non_text"] == "block_on_unsupported" and summary["blocked_or_metadata_only_count"]:
        raise ApexKBError("unsupported_files_blocked", f"{summary['blocked_or_metadata_only_count']} included files could not be fully extracted", {"summary": summary})
    result = {
        "schema": "apex.kb.stage-result.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "stage": "corpus_intelligence",
        "status": "completed",
        "started_at": started,
        "completed_at": manifest["created_at"],
        "artifacts": artifacts,
        "reason_code": None,
        "message": f"Inventoried {len(records)} files and built exhaustive topic maps for {len(topic_maps)} topics.",
        "metrics": summary,
    }
    validate_schema(result, "stage-result.schema.json")
    atomic_json(run_root / manifest["artifact_layout"]["stage_results"] / "corpus-intelligence.json", result)
    return {"summary": summary, "topic_maps": topic_maps, "records": records, "result": result}


def load_topic_map(run_root: Path, topic_id: str) -> dict[str, Any]:
    path = run_root / "manifests" / "phase0" / "topic-maps" / f"{topic_id}.json"
    value = load_json(path)
    if value.get("schema") != "apex.kb.topic-map.v2" or value.get("topic", {}).get("topic_id") != topic_id:
        raise ApexKBError("topic_map_identity_mismatch", f"Invalid topic map for {topic_id}: {path}")
    return value


def check_source_drift(run_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    inventory_path = run_root / "manifests" / "source-inventory.ndjson"
    inventory = {record["repository_path"]: record for record in iter_ndjson(inventory_path)}
    source_root = Path(manifest["source"]["resolved_root"])
    enumeration_errors: list[dict[str, str]] = []
    current_paths = {
        safe_relative(path.resolve(), source_root): path
        for _configured, path in _iter_files(
            source_root,
            manifest["source"]["resolved_folders"],
            enumeration_errors,
        )
    }
    added = sorted(set(current_paths) - set(inventory))
    changed: list[dict[str, Any]] = []
    missing: list[str] = []
    newly_unreadable: list[str] = []
    checked_count = 0
    for record in inventory.values():
        path = Path(record["absolute_path"])
        try:
            file_stat = path.stat()
        except FileNotFoundError:
            missing.append(record["repository_path"])
            continue
        except OSError:
            newly_unreadable.append(record["repository_path"])
            continue
        if not stat.S_ISREG(file_stat.st_mode):
            missing.append(record["repository_path"])
            continue
        try:
            current = sha256_file(path)
        except FileNotFoundError:
            missing.append(record["repository_path"])
            continue
        except OSError:
            newly_unreadable.append(record["repository_path"])
            continue
        checked_count += 1
        if current != record["sha256"]:
            changed.append({"repository_path": record["repository_path"], "expected": record["sha256"], "actual": current})
    missing.sort()
    newly_unreadable.sort()
    fresh = not (added or changed or missing or newly_unreadable or enumeration_errors)
    return {
        "fresh": fresh,
        "inventory_count": len(inventory),
        "current_count": len(current_paths),
        "checked_count": checked_count,
        "added": added,
        "deleted": missing,
        "missing": missing,
        "changed": changed,
        "newly_unreadable": newly_unreadable,
        "enumeration_errors": enumeration_errors,
    }
