#!/usr/bin/env python3
"""Deterministic corpus intelligence for downloaded ProjectRepos.

Standard-library only. Scans candidate text/code files and emits inventories,
maps, and pre-selection reports for Claude/Agent skill design source selection.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any


INCLUDE_EXTENSIONS = {".md", ".mdx", ".txt", ".yaml", ".yml", ".json", ".py", ".ts", ".js", ".toml"}
SKIP_DIRS = {".git", "node_modules", "dist", "build", "coverage", "__pycache__", ".venv", "venv", "assets", "images", "logos", "fonts"}
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ttf", ".otf", ".woff", ".woff2", ".lock"}
KEYWORDS = [
    "skill",
    "agent",
    "claude",
    "prompt",
    "frontmatter",
    "description",
    "progressive_disclosure",
    "reference",
    "template",
    "tool",
    "script",
    "evaluation",
    "safety",
    "routing",
    "manifest",
]
CONTENT_PHRASES = {
    "Use this skill when": 60,
    "progressive disclosure": 50,
    "frontmatter": 25,
    "SKILL.md": 40,
    "Agent Skills": 40,
    "Claude": 20,
    "prompt engineering": 30,
    "evaluation": 20,
    "tools": 15,
    "scripts": 15,
}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")


def norm_rel(path: Path) -> str:
    return path.as_posix()


def read_text(path: Path) -> str:
    data = path.read_bytes()
    return data.decode("utf-8", errors="replace")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_frontmatter(text: str) -> dict[str, Any]:
    result = {"present": False, "raw_keys": [], "name": None, "description": None, "allowed_tools": None, "system_prompt": None}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return result
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return result
    result["present"] = True
    current_key = None
    values: dict[str, Any] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            current_key = key
            values[key] = value.strip("\"'") if value else ""
            if key not in result["raw_keys"]:
                result["raw_keys"].append(key)
        elif current_key and line.startswith((" ", "\t")):
            values[current_key] = (str(values.get(current_key, "")) + "\n" + line.strip()).strip()
    for key in ("name", "description", "allowed_tools", "system_prompt"):
        result[key] = values.get(key)
    return result


def extract_headings(lines: list[str]) -> list[dict[str, Any]]:
    out = []
    for i, line in enumerate(lines, start=1):
        m = HEADING_RE.match(line)
        if m:
            out.append({"level": len(m.group(1)), "text": m.group(2).strip(), "line": i})
    return out


def extract_links(lines: list[str]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    markdown_links = []
    wikilinks = []
    for i, line in enumerate(lines, start=1):
        for m in MD_LINK_RE.finditer(line):
            markdown_links.append({"text": m.group(1), "target": m.group(2), "line": i})
        for m in WIKILINK_RE.finditer(line):
            raw = m.group(1).strip()
            target, _, alias = raw.partition("|")
            wikilinks.append({"raw": raw, "target": target.strip(), "alias": alias.strip() or None, "line": i})
    return markdown_links, wikilinks


def keyword_counts(text: str) -> dict[str, int]:
    lower = text.lower()
    aliases = {
        "progressive_disclosure": "progressive disclosure",
    }
    return {k: lower.count(aliases.get(k, k).lower()) for k in KEYWORDS}


def bool_flags(repo_rel: str, name: str, ext: str, frontmatter: dict[str, Any]) -> dict[str, bool]:
    lower_path = repo_rel.lower()
    lower_name = name.lower()
    return {
        "is_skill_entrypoint": lower_name == "skill.md" or (frontmatter["present"] and bool(frontmatter.get("name")) and "skill" in lower_path),
        "is_package_manifest": "manifest" in lower_name or lower_name in {"package.json", "pyproject.toml"} or lower_name == "package-manifest.md",
        "is_reference": "reference" in lower_path or "/refs/" in lower_path or "/references/" in lower_path,
        "is_template": "template" in lower_path,
        "is_example": "example" in lower_path or "sample" in lower_path,
        "is_script": ext in {".py", ".ts", ".js"} or "/scripts/" in lower_path or lower_path.startswith("scripts/"),
    }


def score_file(record: dict[str, Any], text: str) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    name = record["file_name"]
    lower_name = name.lower()
    rel = record["repo_relative_path"].lower()
    segments = rel.split("/")
    exact_names = {"skill.md": 100, "readme.md": 30, "package-manifest.md": 50}
    for exact, value in exact_names.items():
        if lower_name == exact:
            score += value
            reasons.append(f"filename {exact} +{value}")
    for token, value in {"manifest": 30, "best-practice": 50, "quickstart": 35, "evaluation": 40, "description": 35, "reference": 25, "template": 25, "example": 20, "prompt": 35}.items():
        if token in lower_name:
            score += value
            reasons.append(f"filename contains {token} +{value}")
    if ".claude/skills" in rel:
        score += 60
        reasons.append("path contains .claude/skills +60")
    for token, value in {"skills": 35, "skill": 35, "references": 30, "templates": 25, "examples": 20, "docs": 15, "prompts": 35, "prompt-engineering": 50}.items():
        if token in segments or token in rel:
            score += value
            reasons.append(f"path contains {token} +{value}")
    fm = record["frontmatter"]
    if fm["present"]:
        score += 25
        reasons.append("frontmatter present +25")
    for key, value in {"name": 25, "description": 35, "allowed_tools": 20, "system_prompt": 20}.items():
        if fm.get(key):
            score += value
            reasons.append(f"frontmatter has {key} +{value}")
    lower = text.lower()
    for phrase, value in CONTENT_PHRASES.items():
        if phrase.lower() in lower:
            score += value
            reasons.append(f"content phrase {phrase!r} +{value}")
    if record["size_bytes"] > 5 * 1024 * 1024:
        score -= 100
        reasons.append("size over 5mb -100")
    elif record["size_bytes"] > 1024 * 1024:
        score -= 30
        reasons.append("size over 1mb -30")
    return score, reasons


def should_skip(path: Path, source_root: Path) -> bool:
    rel_parts = path.relative_to(source_root).parts
    if any(part in SKIP_DIRS for part in rel_parts[:-1]):
        return True
    if path.suffix.lower() in SKIP_SUFFIXES:
        return True
    return path.suffix.lower() not in INCLUDE_EXTENSIONS


def scan(source_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, str]]]:
    files: list[dict[str, Any]] = []
    repos: list[dict[str, Any]] = []
    skipped_noise: list[dict[str, str]] = []
    for repo_dir in sorted([p for p in source_root.iterdir() if p.is_dir()], key=lambda p: p.name.lower()):
        repo_slug = repo_dir.name
        total_seen = included = skipped = total_bytes = 0
        repo_files: list[dict[str, Any]] = []
        for root, dirs, names in os.walk(repo_dir):
            dirs[:] = sorted([d for d in dirs if d not in SKIP_DIRS], key=str.lower)
            for name in sorted(names, key=str.lower):
                path = Path(root) / name
                total_seen += 1
                rel_from_source = norm_rel(path.relative_to(source_root))
                if should_skip(path, source_root):
                    skipped += 1
                    if path.suffix.lower() in SKIP_SUFFIXES or any(part in SKIP_DIRS for part in path.relative_to(source_root).parts):
                        skipped_noise.append({"repo": repo_slug, "path": rel_from_source, "reason": "skipped generated/binary/noisy path or extension"})
                    continue
                text = read_text(path)
                lines = text.splitlines()
                repo_rel = norm_rel(path.relative_to(repo_dir))
                fm = parse_frontmatter(text)
                flags = bool_flags(repo_rel, name, path.suffix.lower(), fm)
                md_links, wikilinks = extract_links(lines)
                rec = {
                    "repo_slug": repo_slug,
                    "relative_path_from_projectrepos": rel_from_source,
                    "repo_relative_path": repo_rel,
                    "file_name": name,
                    "extension": path.suffix.lower(),
                    "size_bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                    "line_count": len(lines),
                    **flags,
                    "frontmatter": fm,
                    "headings": extract_headings(lines),
                    "markdown_links": md_links,
                    "wikilinks": wikilinks,
                    "keywords": keyword_counts(text),
                }
                rec["score"], rec["score_reasons"] = score_file(rec, text)
                total_bytes += rec["size_bytes"]
                included += 1
                repo_files.append(rec)
                files.append(rec)
        high = sorted(repo_files, key=lambda r: (-r["score"], r["repo_relative_path"]))[:20]
        score = sum(1 for r in repo_files if r["score"] >= 120) * 20 + sum(r["is_skill_entrypoint"] for r in repo_files) * 50 + sum(r["is_reference"] for r in repo_files) * 5
        if included > 500:
            score -= 30
        if score >= 100:
            label = "high"
        elif score >= 40:
            label = "medium"
        elif included:
            label = "low"
        else:
            label = "noise"
        repos.append({
            "repo_slug": repo_slug,
            "root_path": str(repo_dir),
            "total_files_seen": total_seen,
            "included_files": included,
            "skipped_files": skipped,
            "total_included_bytes": total_bytes,
            "skill_entrypoint_count": sum(r["is_skill_entrypoint"] for r in repo_files),
            "package_manifest_count": sum(r["is_package_manifest"] for r in repo_files),
            "reference_count": sum(r["is_reference"] for r in repo_files),
            "template_count": sum(r["is_template"] for r in repo_files),
            "example_count": sum(r["is_example"] for r in repo_files),
            "script_count": sum(r["is_script"] for r in repo_files),
            "top_level_readme_present": any(r["repo_relative_path"].lower() == "readme.md" for r in repo_files),
            "likely_relevance": {"score": score, "label": label, "reasons": repo_reasons(repo_files, included, skipped)},
            "high_signal_files": [{"path": r["repo_relative_path"], "score": r["score"], "reasons": r["score_reasons"][:6]} for r in high if r["score"] > 0],
        })
    return repos, files, skipped_noise


def repo_reasons(repo_files: list[dict[str, Any]], included: int, skipped: int) -> list[str]:
    reasons = []
    if any(r["is_skill_entrypoint"] for r in repo_files):
        reasons.append("contains SKILL.md or skill entrypoint-like files")
    if any("prompt" in r["repo_relative_path"].lower() for r in repo_files):
        reasons.append("contains prompt-related paths/files")
    if any(r["is_reference"] for r in repo_files):
        reasons.append("contains references")
    if included > 500 or skipped > 500:
        reasons.append("large/noisy repo; avoid bulk import")
    if not reasons:
        reasons.append("limited direct skill-design signal")
    return reasons


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(row[k], ensure_ascii=False) if isinstance(row.get(k), (dict, list)) else row.get(k) for k in fields})


def write_reports(output: Path, repos: list[dict[str, Any]], files: list[dict[str, Any]], skipped_noise: list[dict[str, str]]) -> dict[str, Any]:
    skill_files = [f for f in files if f["is_skill_entrypoint"]]
    frontmatter = [f for f in files if f["frontmatter"]["present"]]
    headings = [{"repo": f["repo_slug"], "path": f["repo_relative_path"], **h} for f in files for h in f["headings"]]
    links = [{"repo": f["repo_slug"], "path": f["repo_relative_path"], "kind": "markdown", **l} for f in files for l in f["markdown_links"]]
    links += [{"repo": f["repo_slug"], "path": f["repo_relative_path"], "kind": "wikilink", **w} for f in files for w in f["wikilinks"]]
    high = sorted([f for f in files if f["score"] >= 80], key=lambda f: (-f["score"], f["repo_slug"], f["repo_relative_path"]))
    prompt = [f for f in files if any(t in f["repo_relative_path"].lower() for t in ("prompt", "instruction", "system", "role", "design")) or any(f["keywords"].get(k, 0) for k in ("prompt", "claude"))]

    write_json(output / "repo-summary.json", repos)
    write_csv(output / "repo-summary.csv", repos, ["repo_slug", "root_path", "total_files_seen", "included_files", "skipped_files", "total_included_bytes", "skill_entrypoint_count", "package_manifest_count", "reference_count", "template_count", "example_count", "script_count", "top_level_readme_present", "likely_relevance"])
    write_json(output / "file-inventory.json", files)
    write_csv(output / "file-inventory.csv", files, ["repo_slug", "relative_path_from_projectrepos", "repo_relative_path", "file_name", "extension", "size_bytes", "sha256", "line_count", "score", "is_skill_entrypoint", "is_package_manifest", "is_reference", "is_template", "is_example", "is_script"])
    write_json(output / "skill-entrypoints.json", skill_files)
    write_csv(output / "skill-entrypoints.csv", skill_files, ["repo_slug", "repo_relative_path", "file_name", "size_bytes", "sha256", "line_count", "score", "frontmatter"])
    write_json(output / "frontmatter-map.json", [{"repo": f["repo_slug"], "path": f["repo_relative_path"], "frontmatter": f["frontmatter"]} for f in frontmatter])
    write_json(output / "heading-map.json", headings)
    write_json(output / "link-map.json", links)
    with (output / "keyword-hits.ndjson").open("w", encoding="utf-8") as fh:
        for f in files:
            hits = {k: v for k, v in f["keywords"].items() if v}
            if hits:
                fh.write(json.dumps({"repo": f["repo_slug"], "path": f["repo_relative_path"], "keywords": hits}, ensure_ascii=False) + "\n")
    write_json(output / "high-signal-candidates.json", high)
    write_markdown_reports(output, repos, files, high, skill_files, prompt, skipped_noise)
    return {"high": high, "skill": skill_files, "prompt": prompt}


def write_markdown_reports(output: Path, repos: list[dict[str, Any]], files: list[dict[str, Any]], high: list[dict[str, Any]], skill_files: list[dict[str, Any]], prompt: list[dict[str, Any]], skipped_noise: list[dict[str, str]]) -> None:
    total_seen = sum(r["total_files_seen"] for r in repos)
    included = sum(r["included_files"] for r in repos)
    skipped = sum(r["skipped_files"] for r in repos)
    useful = [r for r in repos if r["likely_relevance"]["label"] in {"high", "medium"}]
    noisy = [r for r in repos if r["likely_relevance"]["label"] in {"low", "noise"} or r["included_files"] > 500]
    profile = ["# ProjectRepos Corpus Profile", "", "## 1. Executive Summary", "", f"- total repos scanned: {len(repos)}", f"- total files seen: {total_seen}", f"- included files: {included}", f"- skipped files: {skipped}", f"- skill entrypoints found: {len(skill_files)}", f"- high-signal candidate files: {len(high)}", f"- likely useful repos: {len(useful)}", f"- noisy repos: {len(noisy)}", "", "## 2. Repo Map", "", "| repo | included files | skill entrypoints | manifests | references | templates | examples | relevance | notes |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |"]
    for r in repos:
        profile.append(f"| {r['repo_slug']} | {r['included_files']} | {r['skill_entrypoint_count']} | {r['package_manifest_count']} | {r['reference_count']} | {r['template_count']} | {r['example_count']} | {r['likely_relevance']['label']} | {'; '.join(r['likely_relevance']['reasons'])} |")
    profile += ["", "## 3. Top High-Signal Files", "", "| score | repo | path | reason |", "| ---: | --- | --- | --- |"]
    for f in high[:100]:
        profile.append(f"| {f['score']} | {f['repo_slug']} | {f['repo_relative_path']} | {'; '.join(f['score_reasons'][:4])} |")
    profile += ["", "## 4. Skill Entrypoints", "", "| repo | path | frontmatter name | description present | line count |", "| --- | --- | --- | --- | ---: |"]
    for f in skill_files:
        profile.append(f"| {f['repo_slug']} | {f['repo_relative_path']} | {f['frontmatter'].get('name') or ''} | {bool(f['frontmatter'].get('description'))} | {f['line_count']} |")
    profile += ["", "## 5. Prompt / Prompt-Engineering Sources", ""]
    profile += [f"- {f['repo_slug']}/{f['repo_relative_path']} (score: {f['score']})" for f in prompt[:200]] or ["- None found."]
    profile += ["", "## 6. Pollution Risks", ""]
    profile += [f"- {r['repo_slug']}: {r['included_files']} included, {r['skipped_files']} skipped; {'; '.join(r['likely_relevance']['reasons'])}" for r in noisy] or ["- No substantial pollution risks detected."]
    profile += ["", "## 7. Recommended Import Allowlist", "", "First-pass files to consider copying into `apex-meta/kb/claude-skill-design/sources/curated/high-impact-repos/` later:", ""]
    profile += [f"- {f['repo_slug']}/{f['repo_relative_path']} (score: {f['score']})" for f in high[:75]] or ["- None."]
    profile += ["", "## 8. Recommended Next Step", "", "Claude Skill Design KB appears to have enough source coverage for Phase 1 if the allowlist is reviewed and copied selectively; do not bulk import noisy repos."]
    (output / "projectrepos-corpus-profile.md").write_text("\n".join(profile) + "\n", encoding="utf-8")

    groups: dict[str, list[dict[str, Any]]] = {}
    for f in files:
        groups.setdefault(f["repo_slug"], []).append(f)
    lines = ["# High-Signal Candidates", ""]
    for repo in sorted(groups):
        ranked = sorted(groups[repo], key=lambda f: (-f["score"], f["repo_relative_path"]))
        lines += [f"## {repo}", "", "### Include first", ""]
        lines += [f"- {f['repo_relative_path']}\n  - score: {f['score']}\n  - reason: {'; '.join(f['score_reasons'][:5])}" for f in ranked if f["score"] >= 140][:30] or ["- None."]
        lines += ["", "### Maybe include later", ""]
        lines += [f"- {f['repo_relative_path']}\n  - score: {f['score']}\n  - reason: {'; '.join(f['score_reasons'][:5])}" for f in ranked if 80 <= f["score"] < 140][:30] or ["- None."]
        lines += ["", "### Exclude / noise", ""]
        lines += [f"- {n['path']}\n  - reason: {n['reason']}" for n in skipped_noise if n["repo"] == repo][:20] or ["- No major skipped binary/generated files recorded."]
        lines.append("")
    (output / "high-signal-candidates.md").write_text("\n".join(lines), encoding="utf-8")

    empty = [r for r in repos if r["total_files_seen"] == 0 or r["included_files"] == 0]
    (output / "missing-or-empty-repos.md").write_text("# Missing Or Empty Repos\n\n" + ("\n".join(f"- {r['repo_slug']}: seen={r['total_files_seen']}, included={r['included_files']}" for r in empty) or "- None.") + "\n", encoding="utf-8")
    risk = ["# Pollution Risk Report", "", "## Which repos are likely unrelated to Claude skill design?", ""]
    risk += [f"- {r['repo_slug']}: {r['likely_relevance']['label']}; {'; '.join(r['likely_relevance']['reasons'])}" for r in repos if r["likely_relevance"]["label"] in {"low", "noise"}] or ["- None obvious."]
    risk += ["", "## Which repos are huge and should not be bulk imported?", ""]
    risk += [f"- {r['repo_slug']}: {r['total_files_seen']} seen, {r['included_files']} included, {r['skipped_files']} skipped" for r in repos if r["total_files_seen"] > 500 or r["included_files"] > 300] or ["- None exceed the configured size heuristic."]
    risk += ["", "## Which repos duplicate existing official sources?", "", "- Repos with `claude-skills`, `antigravity-awesome-skills`, or other official/example naming may duplicate source material; compare against existing curated official sources before import."]
    risk += ["", "## Which files are binary/assets/noise?", ""]
    risk += [f"- {n['repo']}/{n['path']}" for n in skipped_noise[:300]] or ["- None recorded."]
    risk += ["", "## Which repos are actually project-management/task orchestration rather than skill-package design?", ""]
    risk += [f"- {r['repo_slug']}" for r in repos if any(t in r["repo_slug"].lower() for t in ("task", "backlog", "ccpm", "planning"))] or ["- None obvious."]
    risk += ["", "## Which repos are prompt-design relevant?", ""]
    risk += [f"- {r['repo_slug']}" for r in repos if any(f["repo_slug"] == r["repo_slug"] for f in prompt)] or ["- None found."]
    (output / "pollution-risk-report.md").write_text("\n".join(risk) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", default="source-knowledge/ProjectRepos")
    parser.add_argument("--output-root", default="apex-meta/kb/claude-skill-design/manifests/projectrepos-corpus-intelligence")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--top", type=int, default=0)
    args = parser.parse_args()
    source = Path(args.source_root)
    if not source.exists():
        print("SOURCE_ROOT_MISSING")
        return 2
    output = Path(args.output_root)
    output.mkdir(parents=True, exist_ok=True)
    repos, files, skipped_noise = scan(source)
    result = write_reports(output, repos, files, skipped_noise)
    summary = {"repos_scanned": len(repos), "files_seen": sum(r["total_files_seen"] for r in repos), "files_included": len(files), "skill_entrypoints_found": len(result["skill"]), "high_signal_candidates": len(result["high"]), "prompt_design_candidates": len(result["prompt"])}
    if args.json:
        print(json.dumps(summary, indent=2))
    if args.top:
        for f in result["high"][: args.top]:
            print(f"{f['score']:>4}  {f['repo_slug']}/{f['repo_relative_path']}  {'; '.join(f['score_reasons'][:3])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
