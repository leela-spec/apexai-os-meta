#!/usr/bin/env python3
"""
download_orchestration_agents_in_cc_sources.py

Download source files listed in the OrchestrationAgentsInCC research notes for the
Apex Claude orchestration-agents KB.

Default input notes:
  apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_Research_CC.md
  apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_Research_gem.md

Default output:
  apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/

This script is intentionally different from the earlier SubskillsVsAgents downloader:
  - It targets orchestration/subagent/team/workflow/plugin/hook sources.
  - It extracts table URLs and "Exact Raw Download URL" blocks.
  - It unwraps accidental google.com/search?q=<real-url> wrappers.
  - It converts GitHub blob URLs to raw.githubusercontent.com URLs.
  - It saves official docs, raw repo files, config files, and repo HTML pages.
  - It writes sidecar metadata and machine/human run reports.

Examples from repo root:
  python scripts/download_orchestration_agents_in_cc_sources.py --dry-run
  python scripts/download_orchestration_agents_in_cc_sources.py
  python scripts/download_orchestration_agents_in_cc_sources.py --force
  python scripts/download_orchestration_agents_in_cc_sources.py --only-tier primary

No external Python dependencies are required.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

KB_REL = Path("apex-meta/kb/claude-orchestration-agents")
DEFAULT_NOTES_REL = [
    KB_REL / "raw/notes/OrchestrationAgentsInCC_Research_CC.md",
    KB_REL / "raw/notes/OrchestrationAgentsInCC_Research_gem.md",
]
DEFAULT_OUT_REL = KB_REL / "raw/refs/orchestration-agents-in-cc"
DEFAULT_REPORT_REL = KB_REL / "manifests/downloads"

USER_AGENT = (
    "Mozilla/5.0 (compatible; ApexOrchestrationAgentsInCCDownloader/1.0; "
    "+https://github.com/leela-spec/apexai-os-meta)"
)

DIRECT_EXTENSIONS = {
    ".md", ".mdx", ".txt", ".json", ".jsonl", ".ndjson", ".yaml", ".yml",
    ".toml", ".xml", ".csv", ".tsv", ".pdf", ".doc", ".docx", ".zip",
    ".sh", ".ps1", ".py", ".js", ".ts", ".tsx", ".jsx", ".nu",
}

# These official Claude docs are the high-value orchestration source set from
# OrchestrationAgentsInCC_Research_CC.md. The script can extract them from the
# note, but keeping this list here prevents accidental loss if Markdown table
# parsing breaks.
PRIMARY_ORCHESTRATION_URLS = [
    "https://code.claude.com/docs/llms.txt",
    "https://code.claude.com/docs/en/agents.md",
    "https://code.claude.com/docs/en/sub-agents.md",
    "https://code.claude.com/docs/en/agent-teams.md",
    "https://code.claude.com/docs/en/workflows.md",
    "https://code.claude.com/docs/en/plugins.md",
    "https://code.claude.com/docs/en/plugins-reference.md",
    "https://code.claude.com/docs/en/hooks.md",
    "https://code.claude.com/docs/en/features-overview.md",
    "https://code.claude.com/docs/en/claude-directory.md",
    "https://code.claude.com/docs/en/agent-view.md",
    "https://code.claude.com/docs/en/costs.md",
    "https://code.claude.com/docs/en/mcp.md",
    "https://code.claude.com/docs/en/agent-sdk/overview.md",
    "https://code.claude.com/docs/en/agent-sdk/subagents.md",
    "https://code.claude.com/docs/en/agent-sdk/skills.md",
    "https://code.claude.com/docs/en/agent-sdk/agent-loop.md",
    "https://code.claude.com/docs/en/agent-sdk/hosting.md",
]

# Non-Claude or repo-example sources present in the Gem research file. These are
# useful for real file/config patterns, not just official documentation prose.
REPO_AND_EXTERNAL_URLS = [
    "https://raw.githubusercontent.com/agentskills/agentskills/main/README.md",
    "https://raw.githubusercontent.com/vinnie357/claude-skills/main/plugin.json",
    "https://raw.githubusercontent.com/vinnie357/claude-skills/main/marketplace.json",
    "https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/plugin.json",
    "https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/marketplace.json",
    "https://raw.githubusercontent.com/trailofbits/claude-code-config/main/settings.json",
    "https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/main/guide/workflows/agent-teams.md",
    "https://agentskills.io",
    "https://learn.microsoft.com/en-us/agent-framework/agents/skills",
    "https://www.skillsdirectory.com/docs/skill-file-structure",
    "https://www.mindstudio.ai/blog/what-are-claude-code-skills",
]

MARKDOWN_LINK_RE = re.compile(r"!??\[([^\]]{0,500})\]\(([^)\s]+)(?:\s+['\"][^)]+['"])?\)")
AUTOLINK_RE = re.compile(r"<((?:https?|ftp)://[^>\s]+)>")
BARE_URL_RE = re.compile(r"(?<![\](])\b(?:https?|ftp)://[^\s<>'\"`|]+")
TRAILING_PUNCT = ".,;:!?)]}"


@dataclass(frozen=True)
class SourceCandidate:
    url: str
    normalized_url: str
    source_note: str
    line: int
    title: str = ""
    target_component_type: str = ""
    structural_integrity_key: str = ""
    verification_method: str = ""
    evidence: Optional[int] = None
    impact: Optional[int] = None
    risk: Optional[int] = None
    notes: str = ""
    origin: str = "extracted"
    tier: str = "secondary"


@dataclass
class DownloadResult:
    index: int
    status: str
    url: str
    normalized_url: str
    source_note: str
    line: int
    title: str = ""
    tier: str = ""
    target_path: Optional[str] = None
    meta_path: Optional[str] = None
    capture_url: Optional[str] = None
    capture_method: Optional[str] = None
    content_type: Optional[str] = None
    final_url: Optional[str] = None
    bytes_written: int = 0
    sha256: Optional[str] = None
    error: Optional[str] = None
    skipped_reason: Optional[str] = None
    structural_integrity_key: str = ""
    verification_method: str = ""
    evidence: Optional[int] = None
    impact: Optional[int] = None
    risk: Optional[int] = None
    notes: str = ""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists() or (candidate / "apex-meta").exists():
            return candidate
    return current


def strip_markdown_noise(url: str) -> str:
    url = html.unescape(url.strip())
    # Accidental Markdown table suffixes sometimes get captured into bare URLs.
    url = url.split("|")[0].strip()
    while url and url[-1] in TRAILING_PUNCT:
        url = url[:-1]
    return url


def unwrap_google_search(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower().removeprefix("www.")
    if host == "google.com" and parsed.path.startswith("/search"):
        params = urllib.parse.parse_qs(parsed.query)
        q = params.get("q", [""])[0]
        if q.startswith(("http://", "https://")):
            return q
    return url


def github_blob_to_raw(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower()
    if host != "github.com":
        return url
    parts = [p for p in parsed.path.split("/") if p]
    # /owner/repo/blob/branch/path/to/file
    if len(parts) >= 5 and parts[2] == "blob":
        owner, repo, _blob, branch = parts[:4]
        file_path = "/".join(parts[4:])
        return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    return url


def normalize_url(url: str) -> Optional[str]:
    url = strip_markdown_noise(url)
    url = unwrap_google_search(url)
    url = github_blob_to_raw(url)
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme.lower() not in {"http", "https", "ftp"}:
        return None
    query_pairs = []
    for key, value in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True):
        kl = key.lower()
        if kl.startswith("utm_") or kl in {"fbclid", "gclid", "mc_cid", "mc_eid"}:
            continue
        query_pairs.append((key, value))
    clean_query = urllib.parse.urlencode(query_pairs, doseq=True)
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path or "/", clean_query, ""))


def domain_of(url: str) -> str:
    return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")


def url_extension(url: str) -> str:
    return Path(urllib.parse.urlsplit(url).path).suffix.lower()


def build_jina_url(url: str) -> str:
    return "https://r.jina.ai/" + url


def safe_slug(text: str, max_len: int = 100) -> str:
    text = urllib.parse.unquote(text)
    text = re.sub(r"https?://", "", text, flags=re.I)
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-._")
    return (text[:max_len].strip("-._") or "source")


def infer_tier(url: str, evidence: Optional[int] = None, impact: Optional[int] = None) -> str:
    d = domain_of(url)
    if d == "code.claude.com" and evidence == 5 and impact and impact >= 4:
        return "primary"
    if d in {"raw.githubusercontent.com", "github.com"}:
        return "repo-example"
    if d in {"learn.microsoft.com", "agentskills.io", "skillsdirectory.com", "mindstudio.ai"}:
        return "external"
    return "secondary"


def parse_markdown_table_row(line: str, source_note: str, line_no: int) -> List[SourceCandidate]:
    if not line.startswith("|") or "http" not in line:
        return []
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 2:
        return []
    candidates: List[SourceCandidate] = []
    title_cell = cells[0]
    source_type = cells[1] if len(cells) > 1 else ""
    evidence = int(cells[2]) if len(cells) > 2 and cells[2].isdigit() else None
    impact = int(cells[3]) if len(cells) > 3 and cells[3].isdigit() else None
    risk = int(cells[4]) if len(cells) > 4 and cells[4].isdigit() else None
    notes = cells[6] if len(cells) > 6 else ""
    for match in MARKDOWN_LINK_RE.finditer(title_cell):
        raw = match.group(2)
        normalized = normalize_url(raw)
        if normalized:
            candidates.append(
                SourceCandidate(
                    url=raw,
                    normalized_url=normalized,
                    source_note=source_note,
                    line=line_no,
                    title=match.group(1).strip(),
                    target_component_type=source_type,
                    evidence=evidence,
                    impact=impact,
                    risk=risk,
                    notes=notes,
                    origin="rating_table",
                    tier=infer_tier(normalized, evidence, impact),
                )
            )
    return candidates


def parse_exact_raw_blocks(text: str, source_note: str) -> List[SourceCandidate]:
    lines = text.splitlines()
    current_title = ""
    current_component = ""
    current_integrity = ""
    current_verification = ""
    out: List[SourceCandidate] = []
    for idx, line in enumerate(lines, start=1):
        heading = re.match(r"^###\s+(.+?)\s*$", line)
        if heading:
            current_title = heading.group(1).strip()
            current_component = ""
            current_integrity = ""
            current_verification = ""
            continue
        if "Target Component Type" in line:
            current_component = re.sub(r".*Target Component Type\*\*:\s*", "", line).strip()
        elif "Structural Integrity Key" in line:
            current_integrity = re.sub(r".*Structural Integrity Key\*\*:\s*", "", line).strip()
        elif "Verification Method" in line:
            current_verification = re.sub(r".*Verification Method\*\*:\s*", "", line).strip()
        if "Exact Raw Download URL" not in line:
            continue
        for match in MARKDOWN_LINK_RE.finditer(line):
            # Prefer visible link text because some research files wrap the real URL
            # in google.com/search?q=<real-url> links.
            visible = match.group(1).strip()
            raw = visible if visible.startswith(("http://", "https://")) else match.group(2)
            normalized = normalize_url(raw)
            if not normalized:
                continue
            out.append(
                SourceCandidate(
                    url=raw,
                    normalized_url=normalized,
                    source_note=source_note,
                    line=idx,
                    title=current_title,
                    target_component_type=current_component,
                    structural_integrity_key=current_integrity,
                    verification_method=current_verification,
                    origin="exact_raw_block",
                    tier=infer_tier(normalized),
                )
            )
    return out


def extract_generic_urls(text: str, source_note: str) -> List[SourceCandidate]:
    out: List[SourceCandidate] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for regex in (MARKDOWN_LINK_RE, AUTOLINK_RE, BARE_URL_RE):
            for match in regex.finditer(line):
                if regex is MARKDOWN_LINK_RE:
                    raw = match.group(2)
                    label = match.group(1).strip()
                else:
                    raw = match.group(1) if regex is AUTOLINK_RE else match.group(0)
                    label = ""
                normalized = normalize_url(raw)
                if normalized:
                    out.append(
                        SourceCandidate(
                            url=raw,
                            normalized_url=normalized,
                            source_note=source_note,
                            line=line_no,
                            title=label,
                            notes=line.strip()[:500],
                            origin="generic_url",
                            tier=infer_tier(normalized),
                        )
                    )
    return out


def curated_candidates(source_note: str = "curated_from_orchestration_research") -> List[SourceCandidate]:
    out: List[SourceCandidate] = []
    for raw in PRIMARY_ORCHESTRATION_URLS:
        normalized = normalize_url(raw)
        if normalized:
            out.append(SourceCandidate(raw, normalized, source_note, 0, title=Path(raw).name, origin="curated_primary", tier="primary"))
    for raw in REPO_AND_EXTERNAL_URLS:
        normalized = normalize_url(raw)
        if normalized:
            out.append(SourceCandidate(raw, normalized, source_note, 0, title=Path(urllib.parse.urlsplit(raw).path).name or domain_of(raw), origin="curated_external", tier=infer_tier(normalized)))
    return out


def dedupe(candidates: Iterable[SourceCandidate]) -> List[SourceCandidate]:
    ranked: Dict[str, SourceCandidate] = {}
    origin_rank = {"rating_table": 0, "exact_raw_block": 1, "curated_primary": 2, "curated_external": 2, "generic_url": 3}
    for c in candidates:
        old = ranked.get(c.normalized_url)
        if old is None:
            ranked[c.normalized_url] = c
            continue
        old_rank = origin_rank.get(old.origin, 9)
        new_rank = origin_rank.get(c.origin, 9)
        # Keep richer table/block data over generic URL captures.
        if new_rank < old_rank or (not old.title and c.title):
            ranked[c.normalized_url] = c
    return list(ranked.values())


def choose_capture(candidate: SourceCandidate, no_jina: bool) -> Tuple[str, str, str]:
    url = candidate.normalized_url
    ext = url_extension(url)
    domain = domain_of(url)
    if domain == "raw.githubusercontent.com" or ext in DIRECT_EXTENSIONS:
        return url, ext or ".txt", "direct"
    if domain == "github.com":
        return url, ".html", "github_html"
    if no_jina:
        return url, ".html", "raw_html"
    return build_jina_url(url), ".md", "jina_markdown"


def filename_for(candidate: SourceCandidate, ext: str, used: set[str]) -> str:
    parsed = urllib.parse.urlsplit(candidate.normalized_url)
    domain = domain_of(candidate.normalized_url).replace(".", "-")
    path = parsed.path.strip("/") or "index"
    if path.endswith(".md") or path.endswith(".mdx") or path.endswith(".json"):
        stem_source = path
    else:
        stem_source = candidate.title or path
    stem = safe_slug(f"{candidate.tier}-{domain}-{stem_source}", 120)
    name = f"{stem}{ext or '.md'}"
    i = 2
    while name.lower() in used:
        name = f"{stem}-{i}{ext or '.md'}"
        i += 1
    used.add(name.lower())
    return name


def request_bytes(url: str, timeout: int, max_bytes: int) -> Tuple[bytes, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        final_url = response.geturl()
        chunks: List[bytes] = []
        total = 0
        while True:
            chunk = response.read(64 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if max_bytes and total > max_bytes:
                raise ValueError(f"download_exceeded_max_bytes:{total}>{max_bytes}")
        return b"".join(chunks), content_type, final_url


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def render_markdown_report(results: Sequence[DownloadResult], notes: Sequence[Path], args: argparse.Namespace) -> str:
    counts: Dict[str, int] = {}
    tiers: Dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
        tiers[r.tier or "unknown"] = tiers.get(r.tier or "unknown", 0) + 1
    lines = [
        "# OrchestrationAgentsInCC Source Download Report",
        "",
        f"Generated: `{utc_now()}`",
        "",
        "## Input Notes",
        "",
    ]
    for n in notes:
        lines.append(f"- `{n.as_posix()}`")
    lines.extend([
        "",
        "## Run Configuration",
        "",
        "```yaml",
        f"dry_run: {bool(args.dry_run)}",
        f"force: {bool(args.force)}",
        f"no_jina: {bool(args.no_jina)}",
        f"only_tier: {args.only_tier}",
        f"limit: {args.limit}",
        f"timeout_seconds: {args.timeout}",
        f"max_bytes: {args.max_bytes}",
        "```",
        "",
        "## Status Counts",
        "",
        "| Status | Count |",
        "|---|---:|",
    ])
    for status, count in sorted(counts.items()):
        lines.append(f"| {status} | {count} |")
    lines.extend(["", "## Tier Counts", "", "| Tier | Count |", "|---|---:|"])
    for tier, count in sorted(tiers.items()):
        lines.append(f"| {tier} | {count} |")
    lines.extend(["", "## Results", "", "| # | Status | Tier | Source | Target | Origin line | Notes/Error |", "|---:|---|---|---|---|---:|---|"])
    for r in results:
        note = r.error or r.skipped_reason or r.notes or ""
        lines.append(f"| {r.index} | {r.status} | {r.tier} | `{r.normalized_url}` | `{r.target_path or ''}` | {r.line} | {note[:160]} |")
    lines.append("")
    return "\n".join(lines)


def load_candidates(repo_root: Path, note_paths: Sequence[Path], include_curated: bool) -> Tuple[List[SourceCandidate], List[str]]:
    candidates: List[SourceCandidate] = []
    missing: List[str] = []
    for note in note_paths:
        path = repo_root / note
        if not path.exists():
            missing.append(note.as_posix())
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        source_note = note.as_posix()
        candidates.extend(parse_exact_raw_blocks(text, source_note))
        for line_no, line in enumerate(text.splitlines(), start=1):
            candidates.extend(parse_markdown_table_row(line, source_note, line_no))
        candidates.extend(extract_generic_urls(text, source_note))
    if include_curated:
        candidates.extend(curated_candidates())
    return dedupe(candidates), missing


def run(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve() if args.repo_root else find_repo_root(Path.cwd())
    note_paths = [Path(p) for p in (args.notes or DEFAULT_NOTES_REL)]
    out_dir = repo_root / args.out_dir
    report_dir = repo_root / args.report_dir

    candidates, missing = load_candidates(repo_root, note_paths, not args.no_curated)
    if args.only_tier != "all":
        candidates = [c for c in candidates if c.tier == args.only_tier]
    if args.limit:
        candidates = candidates[: args.limit]

    used_names: set[str] = set()
    results: List[DownloadResult] = []
    started = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M%S")

    for idx, c in enumerate(candidates, start=1):
        capture_url, ext, method = choose_capture(c, args.no_jina)
        filename = filename_for(c, ext, used_names)
        target = out_dir / filename
        meta = target.with_suffix(target.suffix + ".source-meta.json")
        rel_target = target.relative_to(repo_root) if target.is_relative_to(repo_root) else target
        rel_meta = meta.relative_to(repo_root) if meta.is_relative_to(repo_root) else meta
        result = DownloadResult(
            index=idx,
            status="pending",
            url=c.url,
            normalized_url=c.normalized_url,
            source_note=c.source_note,
            line=c.line,
            title=c.title,
            tier=c.tier,
            target_path=rel_target.as_posix(),
            meta_path=rel_meta.as_posix(),
            capture_url=capture_url,
            capture_method=method,
            structural_integrity_key=c.structural_integrity_key,
            verification_method=c.verification_method,
            evidence=c.evidence,
            impact=c.impact,
            risk=c.risk,
            notes=c.notes,
        )
        if target.exists() and target.stat().st_size > 0 and not args.force:
            result.status = "skipped"
            result.skipped_reason = "target_exists_use_force_to_overwrite"
            results.append(result)
            continue
        if args.dry_run:
            result.status = "dry_run"
            result.skipped_reason = method
            results.append(result)
            continue
        try:
            data, content_type, final_url = request_bytes(capture_url, args.timeout, args.max_bytes)
            if len(data) < args.min_bytes:
                raise ValueError(f"download_too_small:{len(data)}<{args.min_bytes}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            digest = sha256_bytes(data)
            result.status = "downloaded"
            result.content_type = content_type
            result.final_url = final_url
            result.bytes_written = len(data)
            result.sha256 = digest
            metadata = {
                "source_url": c.normalized_url,
                "original_url_text": c.url,
                "capture_url": capture_url,
                "final_url": final_url,
                "capture_method": method,
                "tier": c.tier,
                "title": c.title,
                "target_component_type": c.target_component_type,
                "structural_integrity_key": c.structural_integrity_key,
                "verification_method": c.verification_method,
                "evidence": c.evidence,
                "impact": c.impact,
                "risk": c.risk,
                "origin": c.origin,
                "source_note": c.source_note,
                "source_line": c.line,
                "downloaded_at": utc_now(),
                "content_type": content_type,
                "bytes_written": len(data),
                "sha256": digest,
            }
            write_text(meta, json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, OSError) as exc:
            result.status = "failed"
            result.error = f"{type(exc).__name__}: {exc}"
        results.append(result)
        if args.sleep and not args.dry_run:
            time.sleep(args.sleep)

    if missing:
        start = len(results) + 1
        for offset, note in enumerate(missing):
            results.append(DownloadResult(start + offset, "failed", "", "", note, 0, error="input_note_missing"))

    report_dir.mkdir(parents=True, exist_ok=True)
    json_report = report_dir / f"orchestration-agents-in-cc-downloads_{started}.json"
    md_report = report_dir / f"orchestration-agents-in-cc-downloads_{started}.md"
    payload = {
        "generated_at": utc_now(),
        "repo_root": repo_root.as_posix(),
        "input_notes": [p.as_posix() for p in note_paths],
        "output_dir": out_dir.as_posix(),
        "candidate_count": len(candidates),
        "missing_notes": missing,
        "results": [asdict(r) for r in results],
    }
    write_text(json_report, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    write_text(md_report, render_markdown_report(results, note_paths, args))

    downloaded = sum(1 for r in results if r.status == "downloaded")
    failed = sum(1 for r in results if r.status == "failed")
    skipped = sum(1 for r in results if r.status == "skipped")
    dry = sum(1 for r in results if r.status == "dry_run")
    print(f"repo_root: {repo_root}")
    print(f"candidates: {len(candidates)}")
    print(f"downloaded: {downloaded} skipped: {skipped} dry_run: {dry} failed: {failed}")
    print(f"report_json: {json_report}")
    print(f"report_md: {md_report}")
    return 1 if failed and args.fail_on_error else 0


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download OrchestrationAgentsInCC research sources into the claude-orchestration-agents KB.")
    parser.add_argument("--repo-root", default=None, help="Repository root. Defaults to auto-detection.")
    parser.add_argument("--notes", nargs="*", default=None, help="Input research notes relative to repo root.")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_REL, help="Output directory relative to repo root.")
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_REL, help="Report directory relative to repo root.")
    parser.add_argument("--dry-run", action="store_true", help="Plan downloads and write reports without fetching content.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing downloaded files.")
    parser.add_argument("--no-jina", action="store_true", help="Disable Jina Reader for HTML pages and save raw HTML instead.")
    parser.add_argument("--no-curated", action="store_true", help="Use only URLs extracted from notes; do not add the curated safety seed list.")
    parser.add_argument("--only-tier", choices=["all", "primary", "repo-example", "external", "secondary"], default="all", help="Restrict downloads to one source tier.")
    parser.add_argument("--limit", type=int, default=0, help="Process at most N candidates. 0 means no limit.")
    parser.add_argument("--timeout", type=int, default=35, help="Request timeout in seconds.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Seconds to sleep between download attempts.")
    parser.add_argument("--max-bytes", type=int, default=50 * 1024 * 1024, help="Maximum bytes per source. 0 disables cap.")
    parser.add_argument("--min-bytes", type=int, default=40, help="Minimum acceptable response size in bytes.")
    parser.add_argument("--fail-on-error", action="store_true", help="Return non-zero if any source fails.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    return run(parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
