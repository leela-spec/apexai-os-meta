# FILE: `apex-meta/scripts/apex_kb.py`

```
#!/usr/bin/env python3"""apex_kb.pyDeterministic Python helper for the Apex KB skill.Scope:- Scaffold Apex KB folders/files.- Hash files/directories.- Run ingest preflight checks.- Validate and inspect source manifests.- Generate/update the machine-owned section of wiki/index.md.- Lint KB structure, frontmatter, wikilinks, orphans, source pointers, manifest shape, and audit items.- List/group audit files.Non-scope:- No concept extraction.- No entity synthesis.- No contradiction interpretation.- No wiki page prose drafting.- No query answer synthesis.- No operator-review decisions.Runtime:- Python standard library only.- No shell-out.- No network access.- Dry-run by default for write-capable commands."""from __future__ import annotationsimport argparseimport dataclassesimport datetime as _dtimport hashlibimport jsonimport osimport reimport sysfrom pathlib import Pathfrom typing import Any, Dict, Iterable, List, Optional, Sequence, TupleEXIT_OK = 0EXIT_FLAGS = 1EXIT_VALIDATION_FAILURE = 2EXIT_UNSAFE_WRITE = 3EXIT_INVOCATION_ERROR = 4MACHINE_INDEX_BEGIN = "<!-- BEGIN AUTO-GENERATED INDEX -->"MACHINE_INDEX_END = "<!-- END AUTO-GENERATED INDEX -->"LLM_SUMMARY_BEGIN = "<!-- BEGIN LLM SUMMARY -->"LLM_SUMMARY_END = "<!-- END LLM SUMMARY -->"DEFAULT_STATUS_VALUES = {    "draft",    "active",    "needs_review",    "deprecated",    "superseded",    "open",    "resolved",    "deferred",    "rejected",}DEFAULT_PAGE_TYPES = {    "summary",    "concept",    "entity",    "index",    "query_output",    "audit_item",}REQUIRED_KB_SCHEMA_FIELDS = [    "kb_topic_title",    "kb_source_authority_list",    "kb_concept_taxonomy_top_level",    "kb_language_policy",    "kb_operator_review_policy",]REQUIRED_KB_PATHS = [    "README.md",    "kb-schema.md",    "raw/articles",    "raw/papers",    "raw/notes",    "raw/refs",    "ingest-analysis",    "wiki/index.md",    "wiki/concepts",    "wiki/entities",    "wiki/summaries",    "manifests/source-manifest.json",    "audit",    "audit/resolved",    "outputs/queries",    "log",]@dataclasses.dataclassclass Finding:    severity: str    code: str    message: str    path: Optional[str] = None    def to_dict(self) -> Dict[str, Any]:        data = {            "severity": self.severity,            "code": self.code,            "message": self.message,        }        if self.path:            data["path"] = self.path        return data@dataclasses.dataclassclass Report:    report_type: str    status: str    kb_root: Optional[str]    generated_at: str    findings: List[Finding]    data: Dict[str, Any]    def exit_code(self) -> int:        if self.status == "error":            return EXIT_VALIDATION_FAILURE        if any(f.severity in {"error", "critical"} for f in self.findings):            return EXIT_VALIDATION_FAILURE        if self.findings:            return EXIT_FLAGS        return EXIT_OK    def to_dict(self) -> Dict[str, Any]:        return {            "report_type": self.report_type,            "status": self.status,            "kb_root": self.kb_root,            "generated_at": self.generated_at,            "findings": [finding.to_dict() for finding in self.findings],            "data": self.data,        }def utc_now() -> str:    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")def repo_relative(path: Path, root: Optional[Path] = None) -> str:    try:        base = root or Path.cwd()        return path.resolve().relative_to(base.resolve()).as_posix()    except Exception:        return path.as_posix()def output_report(report: Report, as_json: bool) -> None:    if as_json:        print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False, sort_keys=False))        return    print(f"{report.report_type}: {report.status}")    if report.kb_root:        print(f"kb_root: {report.kb_root}")    print(f"generated_at: {report.generated_at}")    if report.findings:        print("\nfindings:")        for finding in report.findings:            path_suffix = f" [{finding.path}]" if finding.path else ""            print(f"- {finding.severity.upper()} {finding.code}: {finding.message}{path_suffix}")    if report.data:        print("\ndata:")        print(json.dumps(report.data, indent=2, ensure_ascii=False, sort_keys=False))def resolve_path(path_value: str) -> Path:    return Path(path_value).expanduser().resolve()def ensure_inside(child: Path, parent: Path) -> bool:    try:        child.resolve().relative_to(parent.resolve())        return True    except ValueError:        return Falsedef safe_write_text(path: Path, content: str, kb_root: Path, allow_write: bool, findings: List[Finding]) -> bool:    if not ensure_inside(path, kb_root):        findings.append(Finding(            severity="critical",            code="write_outside_kb_root_refused",            message="Refused to write outside KB root.",            path=path.as_posix(),        ))        return False    if not allow_write:        findings.append(Finding(            severity="info",            code="dry_run_write_skipped",            message="Write skipped because --allow-write was not supplied.",            path=repo_relative(path),        ))        return False    path.parent.mkdir(parents=True, exist_ok=True)    path.write_text(content, encoding="utf-8", newline="\n")    return Truedef sha256_file(path: Path) -> str:    digest = hashlib.sha256()    with path.open("rb") as handle:        for chunk in iter(lambda: handle.read(1024 * 1024), b""):            digest.update(chunk)    return digest.hexdigest()def sha256_directory(path: Path) -> str:    digest = hashlib.sha256()    entries: List[Tuple[str, str]] = []    for child in sorted(path.rglob("*"), key=lambda p: p.as_posix()):        if child.is_file():            rel = child.relative_to(path).as_posix()            entries.append((rel, sha256_file(child)))    for rel, file_hash in entries:        digest.update(rel.encode("utf-8"))        digest.update(b"\0")        digest.update(file_hash.encode("ascii"))        digest.update(b"\n")    return digest.hexdigest()def compute_hash(path: Path) -> Dict[str, Any]:    if not path.exists():        raise FileNotFoundError(path)    if path.is_file():        return {            "path": path.as_posix(),            "kind": "file",            "algorithm": "sha256",            "hash": sha256_file(path),        }    if path.is_dir():        file_count = sum(1 for item in path.rglob("*") if item.is_file())        return {            "path": path.as_posix(),            "kind": "directory",            "algorithm": "sha256",            "hash": sha256_directory(path),            "file_count": file_count,        }    raise ValueError(f"Unsupported path type: {path}")def read_text_if_exists(path: Path) -> Optional[str]:    if not path.exists() or not path.is_file():        return None    return path.read_text(encoding="utf-8", errors="replace")def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:    """    Minimal frontmatter parser.    Supports:    - YAML-like opening/closing ---    - key: value    - simple list values:      key:        - item        - item    This intentionally avoids PyYAML to preserve stdlib-only runtime.    """    if not text.startswith("---\n"):        return {}, text    end_match = re.search(r"\n---\s*\n", text[4:])    if not end_match:        return {}, text    fm_start = 4    fm_end = 4 + end_match.start()    body_start = 4 + end_match.end()    raw = text[fm_start:fm_end]    body = text[body_start:]    data: Dict[str, Any] = {}    current_key: Optional[str] = None    for raw_line in raw.splitlines():        line = raw_line.rstrip()        stripped = line.strip()        if not stripped or stripped.startswith("#"):            continue        if stripped.startswith("- ") and current_key:            data.setdefault(current_key, [])            if isinstance(data[current_key], list):                data[current_key].append(clean_scalar(stripped[2:].strip()))            continue        if ":" in stripped:            key, value = stripped.split(":", 1)            key = key.strip()            value = value.strip()            current_key = key            if value == "":                data[key] = []            else:                data[key] = clean_scalar(value)    return data, bodydef clean_scalar(value: str) -> Any:    if value in {"[]", ""}:        return []    if value in {"true", "True"}:        return True    if value in {"false", "False"}:        return False    if value in {"null", "Null", "None"}:        return None    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:        return value[1:-1]    if re.fullmatch(r"-?\d+", value):        try:            return int(value)        except ValueError:            return value    return valuedef extract_wikilinks(text: str) -> List[str]:    links: List[str] = []    for match in re.finditer(r"\[\[([^\]]+)\]\]", text):        target = match.group(1).strip()        if not target:            continue        target = target.split("|", 1)[0].strip()        target = target.split("#", 1)[0].strip()        if target:            links.append(target)    return sorted(set(links))def slug_for_page(path: Path) -> str:    return path.stemdef collect_wiki_pages(kb_root: Path) -> List[Path]:    wiki_root = kb_root / "wiki"    if not wiki_root.exists():        return []    return sorted(        [path for path in wiki_root.rglob("*.md") if path.is_file()],        key=lambda p: p.as_posix(),    )def page_path_for_slug(kb_root: Path, slug: str) -> Optional[Path]:    for page in collect_wiki_pages(kb_root):        if page.stem == slug:            return page    return Nonedef load_manifest(kb_root: Path) -> Tuple[Dict[str, Any], List[Finding]]:    findings: List[Finding] = []    path = kb_root / "manifests" / "source-manifest.json"    if not path.exists():        findings.append(Finding(            severity="error",            code="missing_source_manifest",            message="source-manifest.json is missing.",            path=repo_relative(path),        ))        return {}, findings    try:        data = json.loads(path.read_text(encoding="utf-8"))    except json.JSONDecodeError as exc:        findings.append(Finding(            severity="error",            code="invalid_manifest_json",            message=f"Manifest JSON is invalid: {exc}",            path=repo_relative(path),        ))        return {}, findings    if not isinstance(data, dict):        findings.append(Finding(            severity="error",            code="manifest_not_object",            message="Manifest root must be a JSON object.",            path=repo_relative(path),        ))        return {}, findings    return data, findingsdef empty_manifest() -> Dict[str, Any]:    return {        "manifest_version": "0.1",        "updated_at": utc_now(),        "sources": [],    }def manifest_sources(manifest: Dict[str, Any]) -> List[Dict[str, Any]]:    sources = manifest.get("sources", [])    if isinstance(sources, list):        return [item for item in sources if isinstance(item, dict)]    return []def validate_kb_root(kb_root: Path) -> List[Finding]:    findings: List[Finding] = []    if not kb_root.exists():        findings.append(Finding(            severity="error",            code="missing_kb_root",            message="KB root does not exist.",            path=repo_relative(kb_root),        ))        return findings    if not kb_root.is_dir():        findings.append(Finding(            severity="error",            code="kb_root_not_directory",            message="KB root is not a directory.",            path=repo_relative(kb_root),        ))        return findings    for rel in REQUIRED_KB_PATHS:        path = kb_root / rel        if not path.exists():            findings.append(Finding(                severity="error",                code="missing_required_path",                message=f"Required KB path is missing: {rel}",                path=repo_relative(path),            ))    schema = kb_root / "kb-schema.md"    text = read_text_if_exists(schema)    if text is not None:        for field in REQUIRED_KB_SCHEMA_FIELDS:            if field not in text:                findings.append(Finding(                    severity="warning",                    code="kb_schema_field_missing",                    message=f"kb-schema.md does not mention required field: {field}",                    path=repo_relative(schema),                ))    return findingsdef scaffold_file_contents(kb_root: Path, title: str) -> Dict[str, str]:    now = utc_now()    return {        "README.md": f"# {title}\n\nApex KB root.\n\n```yaml\nkb_root: \"{kb_root.as_posix()}\"\ncreated_at: \"{now}\"\n```\n",        "kb-schema.md": f"""# {title} KB Schema```yamlkb_schema:  kb_topic_title: "{title}"  kb_source_authority_list:    - "operator_supplied_sources"  kb_concept_taxonomy_top_level:    - "concepts"    - "entities"    - "summaries"  kb_language_policy: "Preserve source language unless operator requests normalization."  kb_operator_review_policy: "Phase 2 ingest requires explicit operator approval."
```

## """,  
"wiki/index.md": f"""---  
title: "{title} Index"  
page_type: index  
kb_slug: "{kb_root.name}"  
source_refs: []  
created_at: "{now}"  
updated_at: "{now}"  
confidence: "mixed"  
status: "active"  
review_flags: []

# {title} Index

```
index_metadata:  kb_slug: "{kb_root.name}"  kb_schema: "kb-schema.md"  index_role: "Entry point for index-first query and fast AI context loading."  machine_section_owner: python  llm_section_owner: llm
```

{MACHINE_INDEX_BEGIN}

```
machine_generated_index:  generated_at: "{now}"  generated_by: "apex_kb.py scaffold"  page_count: 0  pages:    summaries: []    concepts: []    entities: []  detected_links: []  orphan_pages: []  stale_index_hash: "NA"
```

{MACHINE_INDEX_END}

{LLM_SUMMARY_BEGIN}

## LLM Summary

Pending semantic summary.

{LLM_SUMMARY_END}  
""",  
"manifests/source-manifest.json": json.dumps(empty_manifest(), indent=2, ensure_ascii=False) + "\n",  
}

def cmd_scaffold(args: argparse.Namespace) -> Report:  
kb_root = resolve_path(args.kb_root)  
findings: List[Finding] = []  
title = args.title or kb_root.name

```
directories = [    "raw/articles",    "raw/papers",    "raw/notes",    "raw/refs",    "ingest-analysis",    "wiki/concepts",    "wiki/entities",    "wiki/summaries",    "manifests",    "audit/resolved",    "outputs/queries",    "log",]files = scaffold_file_contents(kb_root, title)created_dirs: List[str] = []created_files: List[str] = []skipped_existing: List[str] = []if args.allow_write:    kb_root.mkdir(parents=True, exist_ok=True)for rel in directories:    path = kb_root / rel    if path.exists():        skipped_existing.append(rel)        continue    if args.allow_write:        path.mkdir(parents=True, exist_ok=True)    created_dirs.append(rel)for rel, content in files.items():    path = kb_root / rel    if path.exists() and not args.force:        skipped_existing.append(rel)        continue    safe_write_text(path, content, kb_root, args.allow_write, findings)    created_files.append(rel)status = "ok" if args.allow_write else "dry_run"data = {    "allow_write": args.allow_write,    "force": args.force,    "created_or_planned_directories": created_dirs,    "created_or_planned_files": created_files,    "skipped_existing": skipped_existing,}return Report(    report_type="scaffold_report",    status=status,    kb_root=repo_relative(kb_root),    generated_at=utc_now(),    findings=findings,    data=data,)
```

def cmd_hash(args: argparse.Namespace) -> Report:  
findings: List[Finding] = []  
target = resolve_path(args.path)

```
try:    data = compute_hash(target)    status = "ok"except FileNotFoundError:    findings.append(Finding(        severity="error",        code="hash_path_missing",        message="Path to hash does not exist.",        path=target.as_posix(),    ))    data = {"path": target.as_posix()}    status = "error"except Exception as exc:    findings.append(Finding(        severity="error",        code="hash_failed",        message=str(exc),        path=target.as_posix(),    ))    data = {"path": target.as_posix()}    status = "error"return Report(    report_type="hash_report",    status=status,    kb_root=None,    generated_at=utc_now(),    findings=findings,    data=data,)
```

def source_manifest_matches(manifest: Dict[str, Any], source_hash: str) -> List[Dict[str, Any]]:  
matches: List[Dict[str, Any]] = []  
for source in manifest_sources(manifest):  
if source.get("source_hash") == source_hash:  
matches.append(source)  
return matches

def cmd_preflight(args: argparse.Namespace) -> Report:  
kb_root = resolve_path(args.kb_root)  
source = resolve_path(args.source)  
findings = validate_kb_root(kb_root)

```
source_hash: Optional[str] = Nonesource_kind: Optional[str] = Noneif not source.exists():    findings.append(Finding(        severity="error",        code="source_missing",        message="Source path does not exist.",        path=source.as_posix(),    ))else:    try:        hash_data = compute_hash(source)        source_hash = hash_data["hash"]        source_kind = hash_data["kind"]    except Exception as exc:        findings.append(Finding(            severity="error",            code="source_hash_failed",            message=str(exc),            path=source.as_posix(),        ))manifest, manifest_findings = load_manifest(kb_root)findings.extend(manifest_findings)duplicate_candidates: List[Dict[str, Any]] = []if source_hash and manifest:    duplicate_candidates = source_manifest_matches(manifest, source_hash)    if duplicate_candidates:        findings.append(Finding(            severity="warning",            code="duplicate_source_hash",            message="Source hash already exists in manifest.",            path=source.as_posix(),        ))source_slug = args.source_slug or source.stemanalysis_path = kb_root / "ingest-analysis" / f"{source_slug}.analysis.md"existing_phase_1_analysis = analysis_path.exists()if existing_phase_1_analysis:    findings.append(Finding(        severity="info",        code="existing_phase_1_analysis",        message="Phase 1 ingest analysis already exists for this source slug.",        path=repo_relative(analysis_path),    ))index_path = kb_root / "wiki" / "index.md"index_status = "present" if index_path.exists() else "missing"if not index_path.exists():    findings.append(Finding(        severity="error",        code="missing_wiki_index",        message="wiki/index.md is missing.",        path=repo_relative(index_path),    ))data = {    "source": source.as_posix(),    "source_slug": source_slug,    "source_kind": source_kind,    "source_hash": source_hash,    "analysis_path": repo_relative(analysis_path),    "existing_phase_1_analysis": existing_phase_1_analysis,    "duplicate_source_candidates": duplicate_candidates,    "index_status": index_status,    "phase_2_allowed": False,    "phase_2_required_operator_phrase": "approve ingest",}status = "ok" if not any(f.severity in {"error", "critical"} for f in findings) else "error"return Report(    report_type="ingest_preflight_report",    status=status,    kb_root=repo_relative(kb_root),    generated_at=utc_now(),    findings=findings,    data=data,)
```

def cmd_manifest(args: argparse.Namespace) -> Report:  
kb_root = resolve_path(args.kb_root)  
findings = validate_kb_root(kb_root)

```
manifest_path = kb_root / "manifests" / "source-manifest.json"manifest, manifest_findings = load_manifest(kb_root)findings.extend(manifest_findings)if not manifest:    manifest = empty_manifest()if "sources" not in manifest or not isinstance(manifest.get("sources"), list):    findings.append(Finding(        severity="error",        code="manifest_sources_invalid",        message="Manifest must contain a sources list.",        path=repo_relative(manifest_path),    ))required_source_fields = [    "source_id",    "source_path",    "source_hash",    "hash_algorithm",    "ingest_status",]malformed_sources: List[Dict[str, Any]] = []seen_ids: set[str] = set()seen_hashes: Dict[str, str] = {}for index, source in enumerate(manifest_sources(manifest)):    missing_fields = [field for field in required_source_fields if field not in source]    source_id = str(source.get("source_id", f"index_{index}"))    if missing_fields:        malformed_sources.append({            "index": index,            "source_id": source_id,            "missing_fields": missing_fields,        })        findings.append(Finding(            severity="warning",            code="manifest_source_missing_fields",            message=f"Manifest source entry is missing fields: {', '.join(missing_fields)}",            path=repo_relative(manifest_path),        ))    if source_id in seen_ids:        findings.append(Finding(            severity="warning",            code="duplicate_source_id",            message=f"Duplicate source_id in manifest: {source_id}",            path=repo_relative(manifest_path),        ))    seen_ids.add(source_id)    source_hash = str(source.get("source_hash", ""))    if source_hash and source_hash != "NA":        if source_hash in seen_hashes:            findings.append(Finding(                severity="warning",                code="duplicate_source_hash",                message=f"Duplicate source_hash in manifest: {source_hash}",                path=repo_relative(manifest_path),            ))        seen_hashes[source_hash] = source_idif args.touch_updated_at:    manifest["updated_at"] = utc_now()    if args.allow_write:        safe_write_text(            manifest_path,            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",            kb_root,            args.allow_write,            findings,        )    else:        findings.append(Finding(            severity="info",            code="dry_run_manifest_update_skipped",            message="Manifest updated_at would be refreshed, but --allow-write was not supplied.",            path=repo_relative(manifest_path),        ))data = {    "manifest_path": repo_relative(manifest_path),    "source_count": len(manifest_sources(manifest)),    "malformed_sources": malformed_sources,    "touch_updated_at": args.touch_updated_at,    "allow_write": args.allow_write,}status = "ok" if not any(f.severity in {"error", "critical"} for f in findings) else "error"return Report(    report_type="manifest_report",    status=status,    kb_root=repo_relative(kb_root),    generated_at=utc_now(),    findings=findings,    data=data,)
```

def page_record(kb_root: Path, page: Path) -> Dict[str, Any]:  
text = read_text_if_exists(page) or ""  
frontmatter, body = parse_frontmatter(text)  
rel = page.relative_to(kb_root).as_posix()  
return {  
"path": rel,  
"slug": slug_for_page(page),  
"title": frontmatter.get("title", page.stem),  
"page_type": frontmatter.get("page_type", infer_page_type(page)),  
"status": frontmatter.get("status", "unknown"),  
"confidence": frontmatter.get("confidence", "unknown"),  
"links": extract_wikilinks(text),  
"has_source_refs": "source_refs" in frontmatter or "source_pointers" in text or "source_pointer" in text,  
}

def infer_page_type(page: Path) -> str:  
parts = set(page.parts)  
if "summaries" in parts:  
return "summary"  
if "concepts" in parts:  
return "concept"  
if "entities" in parts:  
return "entity"  
if page.name == "index.md":  
return "index"  
return "unknown"

def collect_index_data(kb_root: Path) -> Dict[str, Any]:  
pages = [page_record(kb_root, page) for page in collect_wiki_pages(kb_root)]  
pages_by_type: Dict[str, List[Dict[str, Any]]] = {  
"summaries": [],  
"concepts": [],  
"entities": [],  
"other": [],  
}

```
slugs = {record["slug"] for record in pages}detected_links: List[Dict[str, Any]] = []broken_links: List[Dict[str, Any]] = []for record in pages:    page_type = record.get("page_type")    if page_type == "summary":        pages_by_type["summaries"].append(record)    elif page_type == "concept":        pages_by_type["concepts"].append(record)    elif page_type == "entity":        pages_by_type["entities"].append(record)    else:        pages_by_type["other"].append(record)    for link in record["links"]:        detected_links.append({            "from": record["path"],            "to": link,        })        if link not in slugs:            broken_links.append({                "from": record["path"],                "to": link,            })linked_targets = {link["to"] for link in detected_links}orphan_pages = [    record["path"]    for record in pages    if record["slug"] not in linked_targets and record["path"] != "wiki/index.md"]index_hash_source = json.dumps(pages, sort_keys=True, ensure_ascii=False)index_hash = hashlib.sha256(index_hash_source.encode("utf-8")).hexdigest()return {    "generated_at": utc_now(),    "generated_by": "apex_kb.py index",    "page_count": len(pages),    "pages": pages_by_type,    "detected_links": detected_links,    "broken_links": broken_links,    "orphan_pages": orphan_pages,    "stale_index_hash": index_hash,}
```

def machine_index_block(index_data: Dict[str, Any]) -> str:  
return (  
f"{MACHINE_INDEX_BEGIN}\n\n"  
"`json\n" f"{json.dumps({'machine_generated_index': index_data}, indent=2, ensure_ascii=False)}\n" "`\n\n"  
f"{MACHINE_INDEX_END}"  
)

def update_machine_index_section(existing: str, block: str) -> str:  
if MACHINE_INDEX_BEGIN in existing and MACHINE_INDEX_END in existing:  
pattern = re.compile(  
re.escape(MACHINE_INDEX_BEGIN) + r".*?" + re.escape(MACHINE_INDEX_END),  
flags=re.DOTALL,  
)  
return pattern.sub(block, existing, count=1)

```
if LLM_SUMMARY_BEGIN in existing:    return existing.replace(LLM_SUMMARY_BEGIN, block + "\n\n" + LLM_SUMMARY_BEGIN, 1)return existing.rstrip() + "\n\n" + block + "\n"
```

def cmd_index(args: argparse.Namespace) -> Report:  
kb_root = resolve_path(args.kb_root)  
findings = validate_kb_root(kb_root)  
index_path = kb_root / "wiki" / "index.md"

```
index_data = collect_index_data(kb_root)for broken in index_data["broken_links"]:    findings.append(Finding(        severity="error",        code="broken_wikilink",        message=f"Broken wikilink target: {broken['to']}",        path=broken["from"],    ))for orphan in index_data["orphan_pages"]:    findings.append(Finding(        severity="warning",        code="orphan_page",        message="Wiki page has no inbound wikilinks.",        path=orphan,    ))existing = read_text_if_exists(index_path)block = machine_index_block(index_data)if args.allow_write:    if existing is None:        existing = f"# {kb_root.name} Index\n\n{LLM_SUMMARY_BEGIN}\n\n## LLM Summary\n\nPending.\n\n{LLM_SUMMARY_END}\n"    updated = update_machine_index_section(existing, block)    safe_write_text(index_path, updated, kb_root, args.allow_write, findings)else:    findings.append(Finding(        severity="info",        code="dry_run_index_write_skipped",        message="Machine index section generated but not written because --allow-write was not supplied.",        path=repo_relative(index_path),    ))data = {    "index_path": repo_relative(index_path),    "allow_write": args.allow_write,    "machine_index": index_data,}status = "ok" if not any(f.severity in {"error", "critical"} for f in findings) else "error"return Report(    report_type="index_report",    status=status,    kb_root=repo_relative(kb_root),    generated_at=utc_now(),    findings=findings,    data=data,)
```

def validate_frontmatter_for_page(kb_root: Path, page: Path) -> List[Finding]:  
findings: List[Finding] = []  
text = read_text_if_exists(page) or ""  
frontmatter, _body = parse_frontmatter(text)  
rel = repo_relative(page)

```
if not frontmatter:    findings.append(Finding(        severity="error",        code="missing_frontmatter",        message="Wiki page is missing frontmatter.",        path=rel,    ))    return findingsrequired = ["title", "page_type", "kb_slug", "source_refs", "created_at", "updated_at", "confidence", "status"]for field in required:    if field not in frontmatter:        findings.append(Finding(            severity="warning",            code="frontmatter_field_missing",            message=f"Frontmatter missing field: {field}",            path=rel,        ))page_type = str(frontmatter.get("page_type", ""))if page_type and page_type not in DEFAULT_PAGE_TYPES:    findings.append(Finding(        severity="warning",        code="unknown_page_type",        message=f"Unknown page_type: {page_type}",        path=rel,    ))status = str(frontmatter.get("status", ""))if status and status not in DEFAULT_STATUS_VALUES:    findings.append(Finding(        severity="warning",        code="unknown_status",        message=f"Unknown status: {status}",        path=rel,    ))if page.name != "index.md" and "source_refs" not in frontmatter and "source_pointer" not in text:    findings.append(Finding(        severity="warning",        code="missing_source_pointer",        message="Page appears to lack source_refs/source_pointer.",        path=rel,    ))return findings
```

def collect_audit_files(kb_root: Path, status_filter: str = "all") -> List[Path]:  
audit_root = kb_root / "audit"  
if not audit_root.exists():  
return []

```
files = sorted(    [path for path in audit_root.rglob("*.md") if path.is_file()],    key=lambda p: p.as_posix(),)if status_filter == "all":    return filesfiltered: List[Path] = []for path in files:    text = read_text_if_exists(path) or ""    fm, body = parse_frontmatter(text)    combined = json.dumps(fm, ensure_ascii=False) + "\n" + body    if re.search(rf"\bstatus:\s*[\"']?{re.escape(status_filter)}[\"']?\b", combined):        filtered.append(path)return filtered
```

def validate_audit_file(path: Path) -> List[Finding]:  
findings: List[Finding] = []  
text = read_text_if_exists(path) or ""  
rel = repo_relative(path)

```
required_terms = [    "audit_id",    "type",    "severity",    "status",    "target_path",]for term in required_terms:    if term not in text:        findings.append(Finding(            severity="warning",            code="audit_field_missing",            message=f"Audit item does not mention required field: {term}",            path=rel,        ))return findings
```

def cmd_lint(args: argparse.Namespace) -> Report:  
kb_root = resolve_path(args.kb_root)  
findings = validate_kb_root(kb_root)

```
pages = collect_wiki_pages(kb_root)index_data = collect_index_data(kb_root)for page in pages:    findings.extend(validate_frontmatter_for_page(kb_root, page))for broken in index_data["broken_links"]:    findings.append(Finding(        severity="error",        code="broken_wikilink",        message=f"Broken wikilink target: {broken['to']}",        path=broken["from"],    ))for orphan in index_data["orphan_pages"]:    findings.append(Finding(        severity="warning",        code="orphan_page",        message="Wiki page has no inbound wikilinks.",        path=orphan,    ))manifest, manifest_findings = load_manifest(kb_root)findings.extend(manifest_findings)if manifest and "sources" not in manifest:    findings.append(Finding(        severity="error",        code="manifest_sources_missing",        message="Manifest is missing sources list.",        path=repo_relative(kb_root / "manifests" / "source-manifest.json"),    ))audit_files = collect_audit_files(kb_root)for audit_file in audit_files:    findings.extend(validate_audit_file(audit_file))data = {    "wiki_page_count": len(pages),    "audit_file_count": len(audit_files),    "broken_link_count": len(index_data["broken_links"]),    "orphan_page_count": len(index_data["orphan_pages"]),    "manifest_source_count": len(manifest_sources(manifest)) if manifest else 0,}status = "ok" if not any(f.severity in {"error", "critical"} for f in findings) else "error"return Report(    report_type="lint_report",    status=status,    kb_root=repo_relative(kb_root),    generated_at=utc_now(),    findings=findings,    data=data,)
```

def cmd_audit(args: argparse.Namespace) -> Report:  
kb_root = resolve_path(args.kb_root)  
findings = validate_kb_root(kb_root)  
status_filter = args.status

```
audit_files = collect_audit_files(kb_root, status_filter=status_filter)items: List[Dict[str, Any]] = []for path in audit_files:    text = read_text_if_exists(path) or ""    frontmatter, body = parse_frontmatter(text)    item = {        "path": repo_relative(path),        "title": frontmatter.get("title", path.stem),        "audit_id": frontmatter.get("audit_id", "unknown"),        "status": frontmatter.get("status", "unknown"),        "type": frontmatter.get("type", "unknown"),        "severity": frontmatter.get("severity", "unknown"),    }    status_match = re.search(r"\bstatus:\s*[\"']?([a-zA-Z0-9_-]+)[\"']?", body)    if item["status"] == "unknown" and status_match:        item["status"] = status_match.group(1)    type_match = re.search(r"\btype:\s*[\"']?([a-zA-Z0-9_-]+)[\"']?", body)    if item["type"] == "unknown" and type_match:        item["type"] = type_match.group(1)    severity_match = re.search(r"\bseverity:\s*[\"']?([a-zA-Z0-9_-]+)[\"']?", body)    if item["severity"] == "unknown" and severity_match:        item["severity"] = severity_match.group(1)    items.append(item)    findings.extend(validate_audit_file(path))grouped: Dict[str, List[Dict[str, Any]]] = {}if args.group_by:    for item in items:        key = str(item.get(args.group_by, "unknown"))        grouped.setdefault(key, []).append(item)data = {    "status_filter": status_filter,    "audit_count": len(items),    "items": items,    "group_by": args.group_by,    "grouped": grouped,}status = "ok" if not any(f.severity in {"error", "critical"} for f in findings) else "error"return Report(    report_type="audit_report",    status=status,    kb_root=repo_relative(kb_root),    generated_at=utc_now(),    findings=findings,    data=data,)
```

def build_parser() -> argparse.ArgumentParser:  
parser = argparse.ArgumentParser(  
prog="apex_kb.py",  
description="Deterministic Apex KB helper. Standard library only.",  
)  
parser.add_argument("--json", action="store_true", help="Emit JSON report.")  
parser.add_argument("--allow-write", action="store_true", help="Allow bounded writes for write-capable commands.")  
parser.add_argument("--strict", action="store_true", help="Reserved for stricter future validation.")

```
subparsers = parser.add_subparsers(dest="command", required=True)scaffold = subparsers.add_parser("scaffold", help="Create or preview KB scaffold.")scaffold.add_argument("--kb-root", required=True)scaffold.add_argument("--title")scaffold.add_argument("--force", action="store_true", help="Overwrite scaffold files if --allow-write is present.")scaffold.set_defaults(func=cmd_scaffold)hash_cmd = subparsers.add_parser("hash", help="Hash a file or directory.")hash_cmd.add_argument("--path", required=True)hash_cmd.set_defaults(func=cmd_hash)preflight = subparsers.add_parser("preflight", help="Run ingest preflight checks.")preflight.add_argument("--kb-root", required=True)preflight.add_argument("--source", required=True)preflight.add_argument("--source-slug")preflight.set_defaults(func=cmd_preflight)manifest = subparsers.add_parser("manifest", help="Validate or refresh source manifest metadata.")manifest.add_argument("--kb-root", required=True)manifest.add_argument("--touch-updated-at", action="store_true")manifest.set_defaults(func=cmd_manifest)index = subparsers.add_parser("index", help="Generate or update machine-owned index section.")index.add_argument("--kb-root", required=True)index.set_defaults(func=cmd_index)lint = subparsers.add_parser("lint", help="Run deterministic KB lint checks.")lint.add_argument("--kb-root", required=True)lint.set_defaults(func=cmd_lint)audit = subparsers.add_parser("audit", help="List and group audit files.")audit.add_argument("--kb-root", required=True)audit.add_argument("--status", default="all", choices=["all", "open", "resolved", "deferred", "rejected"])audit.add_argument("--group-by", choices=["status", "type", "severity"])audit.set_defaults(func=cmd_audit)return parser
```

def main(argv: Optional[Sequence[str]] = None) -> int:  
parser = build_parser()

```
try:    args = parser.parse_args(argv)except SystemExit as exc:    return int(exc.code)try:    report = args.func(args)except PermissionError as exc:    report = Report(        report_type="error_report",        status="error",        kb_root=getattr(args, "kb_root", None),        generated_at=utc_now(),        findings=[            Finding(                severity="critical",                code="permission_error",                message=str(exc),            )        ],        data={},    )    output_report(report, getattr(args, "json", False))    return EXIT_UNSAFE_WRITEexcept Exception as exc:    report = Report(        report_type="error_report",        status="error",        kb_root=getattr(args, "kb_root", None),        generated_at=utc_now(),        findings=[            Finding(                severity="error",                code="unhandled_exception",                message=f"{type(exc).__name__}: {exc}",            )        ],        data={},    )    output_report(report, getattr(args, "json", False))    return EXIT_INVOCATION_ERRORoutput_report(report, args.json)return report.exit_code()
```

if **name** == "**main**":  
raise SystemExit(main())