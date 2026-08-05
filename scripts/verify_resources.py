#!/usr/bin/env python3
"""Verify every assigned resource and authored external citation."""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
import json
import re
import ssl
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from schema_contract import SchemaContractError, validate_instance


ROOT = Path(__file__).resolve().parents[1]
MAX_TEXT_READ = 786_432
MAX_BINARY_READ = 52_428_800
STOP_WORDS = {"a", "al", "an", "and", "com", "et", "for", "in", "of", "on", "the", "to", "with", "documentation", "guide"}
AUTHORITY_ALIASES = {
    "sre.google": "google site reliability engineering google sre",
    "aws.amazon.com": "amazon web services builders library",
    "builder.aws.com": "amazon web services builders library",
    "c4model.com": "simon brown c4 model project",
    "opentelemetry.io": "opentelemetry maintainers cncf",
    "15445.courses.cs.cmu.edu": "carnegie mellon university",
    "github.com/hdrhistogram/hdrhistogram": "gil tene michael barker hdrhistogram maintainers",
    "github.com/facebook/rocksdb": "rocksdb maintainers meta",
    "debezium.io": "debezium project maintainers",
    "slsa.dev": "openssf slsa project",
    "docs.oracle.com": "oracle java community process",
    "rfc-editor.org": "internet engineering task force ietf rfc editor",
    "datatracker.ietf.org": "internet engineering task force ietf",
    "docs.python.org": "python software foundation",
    "docs.docker.com": "docker",
    "kernel.org": "linux kernel contributors tejun heo",
    "man7.org": "linux man pages project",
    "grpc.io": "grpc authors",
    "postgresql.org": "postgresql global development group",
    "docs.cloud.google.com": "google cloud",
    "learn.microsoft.com": "microsoft",
    "playwright.dev": "microsoft playwright",
    "sei.cmu.edu": "software engineering institute carnegie mellon university",
    "w3.org": "world wide web consortium w3c",
    "w3.org/tr/trace-context": "w3c distributed tracing working group",
    "amazon.science": "amazon science amazon",
    "nvmexpress.org": "nvm express",
    "nist.gov": "national institute standards technology nist",
    "github.com/ongardie": "diego ongaro",
    "cs.princeton.edu": "princeton university",
    "nodejs.org": "node.js node project",
    "typescriptlang.org": "typescript project microsoft",
    "web.dev": "google chrome web.dev",
    "deeplearningbook.org": "ian goodfellow yoshua bengio aaron courville mit press",
    "nlp.stanford.edu": "stanford university christopher manning prabhakar raghavan hinrich schutze",
    "arxiv.org": "arxiv",
    "melconway.com": "melvin conway",
    "martinfowler.com": "martinfowler.com martin fowler",
    "ocw.mit.edu": "mit open courseware massachusetts institute technology",
    "youtube.com": "youtube",
    "cheatsheetseries.owasp.org": "owasp cheat sheet series",
    "developer.chrome.com": "chromium project google chrome developers",
    "web.dev/case-studies/better-youtube": "youtube chrome teams web.dev",
    "devblogs.microsoft.com/typescript": "typescript team microsoft",
    # Some authoritative sites publish no usable publisher metadata and use a
    # compound brand in the host label. Keep those identities explicit rather
    # than accepting publisher text found anywhere in the page body.
    "huggingface.co": "hugging face",
    "sqlite.org": "sqlite project sqlite authors",
    "kafka.apache.org": "apache kafka apache software foundation",
    "martin.kleppmann.com": "martin kleppmann domain driven design europe",
    "owasp.org": "owasp foundation",
    "finops.org": "finops foundation",
    "tag-app-delivery.cncf.io": "cloud native computing foundation cncf tag app delivery",
    "digital-strategy.ec.europa.eu": "european commission shaping europe digital future",
    "stripe.com": "stripe engineering jacqueline xu atlas",
    "go.dev": "go project",
    "rust-lang.org": "rust project rust foundation",
    "discord.com": "discord engineering",
    "oracle.com": "oracle",
    "whatwg.org": "whatwg",
    "react.dev": "react project",
    "docs.vllm.ai": "vllm project",
    "docs.pytorch.org": "pytorch project",
    "go.temporal.io": "temporal technologies",
    "json-schema.org": "json schema project austin wright henry andrews ben hutton greg dennis",
    "web.dev/case-studies/better-youtube-web-part1": "youtube chrome teams web.dev",
    "dropbox.tech": "dropbox engineering",
}
URL = re.compile(r"https?://[^\s)>]+")
FENCED_CODE = re.compile(r"^```.*?^```\s*$", re.MULTILINE | re.DOTALL)


def normalize_words(value: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9]+", html.unescape(value).lower()) if len(word) > 1 and word not in STOP_WORDS}


def normalize_url(value: str) -> str:
    cleaned = value.rstrip(".,;:>`]")
    parsed = urllib.parse.urlsplit(cleaned)
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path, parsed.query, ""))


def authority_words(url: str) -> set[str]:
    parsed = urllib.parse.urlsplit(url)
    host = (parsed.hostname or "").lower()
    path = parsed.path.lower().rstrip("/")
    words: set[str] = set()
    for authority, aliases in AUTHORITY_ALIASES.items():
        authority_host, separator, authority_path = authority.partition("/")
        host_matches = host == authority_host or host.endswith(f".{authority_host}")
        expected_path = f"/{authority_path.rstrip('/')}" if separator else ""
        path_matches = not expected_path or path == expected_path or path.startswith(f"{expected_path}/")
        if host_matches and path_matches:
            words |= normalize_words(aliases)
    return words


def _structured_metadata(text: str, content_type: str, final_url: str) -> tuple[list[str], list[str]]:
    titles: list[str] = []
    publishers: list[str] = []
    if content_type in {"text/markdown", "text/plain"}:
        heading = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        if heading:
            titles.append(heading.group(1).strip())
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
    if title_match:
        titles.append(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", title_match.group(1))).strip())
    h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.IGNORECASE | re.DOTALL)
    if h1_match:
        titles.append(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h1_match.group(1))).strip())
    h2_match = re.search(r"<h2[^>]*>(.*?)</h2>", text, re.IGNORECASE | re.DOTALL)
    if h2_match:
        titles.append(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h2_match.group(1))).strip())
    rfc_heading = re.search(r'<span\s+class=["\']h1["\']>(.*?)</span>', text, re.IGNORECASE | re.DOTALL)
    if rfc_heading:
        titles.append(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", rfc_heading.group(1))).strip())
    for tag in re.findall(r"<meta\s+[^>]*>", text, re.IGNORECASE):
        attributes = {
            key.lower(): html.unescape(value)
            for key, _, value in re.findall(r"([\w:-]+)\s*=\s*(['\"])(.*?)\2", tag, re.DOTALL)
        }
        name = (attributes.get("name") or attributes.get("property") or "").lower()
        content = attributes.get("content", "").strip()
        if not content:
            continue
        if name in {"og:title", "twitter:title", "citation_title", "dc.title"}:
            titles.append(content)
        if name in {"author", "article:author", "citation_author", "publisher", "og:site_name", "dc.creator"}:
            publishers.append(content)
    parsed = urllib.parse.urlsplit(final_url)
    if parsed.netloc.lower().endswith("builder.aws.com"):
        slug = parsed.path.rstrip("/").rsplit("/", 1)[-1]
        if slug:
            titles.append(slug.replace("-", " "))
    if parsed.fragment:
        section = parsed.fragment.replace("-", " ")
        titles.extend(f"{candidate} {section}" for candidate in list(titles))
    channel = re.search(r'"ownerChannelName"\s*:\s*"([^"\\]+)"', text)
    if channel:
        publishers.append(channel.group(1))
    return titles, publishers


def inspect_body(
    record: dict[str, Any], resource: dict[str, Any], *, status: int,
    final_url: str, content_type: str, body: bytes, charset: str = "utf-8",
    transport: str = "python-stdlib", complete_body: bool = True,
) -> dict[str, Any]:
    record.update({
        "status": status,
        "final_url": final_url,
        "redirected": normalize_url(final_url) != normalize_url(record["requested_url"]),
        "content_type": content_type,
        "bytes_inspected": len(body),
        "content_complete": complete_body,
        "content_sha256": hashlib.sha256(body).hexdigest(),
        "access": "retrieved" if 200 <= status < 400 else "failed",
        "transport": transport,
    })
    if content_type in {"text/html", "application/xhtml+xml", "text/plain", "text/markdown"}:
        text = body.decode(charset, errors="replace")
        titles, publishers = _structured_metadata(text, content_type, final_url)
        declared_words = normalize_words(resource["title"])
        publisher_words = normalize_words(resource["author_or_publisher"])
        title_overlaps = [len(declared_words & normalize_words(candidate)) / max(1, len(declared_words)) for candidate in titles]
        publisher_candidates = [authority_words(final_url), *(normalize_words(candidate) for candidate in publishers)]
        publisher_overlap = max(
            (len(publisher_words & candidate) / max(1, min(len(publisher_words), len(candidate))) for candidate in publisher_candidates),
            default=0.0,
        )
        title_overlap = max(title_overlaps, default=0.0)
        record.update({
            "remote_titles": titles,
            "remote_title_overlap": round(title_overlap, 3),
            "title_match": title_overlap >= 0.5,
            "publisher_metadata": publishers,
            "publisher_overlap": round(publisher_overlap, 3),
            "publisher_match": publisher_overlap >= 0.5,
        })
    else:
        record.update({
            "remote_titles": [], "title_match": None, "publisher_match": None,
            "metadata_note": "Binary source metadata is accepted only through a content-hash-bound manual attestation.",
        })
    return record


def curl_retrieve(record: dict[str, Any], resource: dict[str, Any], url: str) -> dict[str, Any]:
    """Retry with the operating-system trust store without disabling TLS."""
    with tempfile.TemporaryDirectory(prefix="course-resource-") as directory:
        body_path = Path(directory) / "body"
        result = subprocess.run(
            [
                "curl", "--location", "--fail", "--silent", "--show-error",
                "--max-time", "40", "--max-filesize", str(MAX_BINARY_READ),
                "--header", "Accept: text/html,application/pdf,text/plain,*/*;q=0.5",
                "--user-agent", "system-design-mastery-course-resource-verifier/2.0",
                "--output", str(body_path),
                "--write-out", "%{http_code}\n%{url_effective}\n%{content_type}",
                url,
            ],
            check=False, capture_output=True, text=True, timeout=45,
        )
        if result.returncode != 0:
            raise OSError(result.stderr.strip() or f"curl exited {result.returncode}")
        metadata = result.stdout.splitlines()
        if len(metadata) < 3:
            raise OSError("curl did not return verification metadata")
        body = body_path.read_bytes()
        content_type = metadata[2].split(";", 1)[0].strip().lower()
        complete = True
        if content_type in {"text/html", "application/xhtml+xml", "text/plain"} and len(body) > MAX_TEXT_READ:
            body = body[:MAX_TEXT_READ]
            complete = False
        return inspect_body(
            record, resource, status=int(metadata[0]), final_url=metadata[1],
            content_type=content_type, body=body, transport="curl-system-trust",
            complete_body=complete,
        )


def retrieve(item: tuple[str, str, str, dict[str, Any], bool]) -> dict[str, Any]:
    module_id, module_relative, kind, resource, blocking = item
    url = str(resource["url"])
    fallback = resource["text_alternative"] if module_id == "GLOBAL" else f"{module_relative}/{resource['text_alternative']}"
    boundary = resource.get("assignment", resource.get("reading_boundary", ""))
    record: dict[str, Any] = {
        "module": module_id,
        "resource_id": resource["id"],
        "resource_key": f"{module_id}/{resource['id']}",
        "kind": kind,
        "required": bool(resource["required"]),
        "blocking": blocking,
        "declared_title": resource["title"],
        "declared_publisher": resource["author_or_publisher"],
        "requested_url": url,
        "declared_final_url": resource["final_url"],
        "reading_boundary": boundary,
        "local_fallback": fallback,
    }
    request = urllib.request.Request(url, headers={
        "User-Agent": "system-design-mastery-course-resource-verifier/2.0",
        "Accept": "text/html,application/pdf,text/plain,*/*;q=0.5",
        "Accept-Encoding": "identity",
    })
    try:
        with urllib.request.urlopen(request, timeout=30, context=ssl.create_default_context()) as response:
            content_type = response.headers.get_content_type()
            text_content = content_type in {"text/html", "application/xhtml+xml", "text/plain", "text/markdown"}
            limit = MAX_TEXT_READ if text_content else MAX_BINARY_READ
            body = response.read(limit + 1)
            if len(body) > limit and not text_content:
                record.update({"status": response.status, "final_url": response.geturl(), "access": "failed", "error": f"source exceeds {limit} byte verification limit"})
                return record
            if len(body) > limit:
                body = body[:limit]
            return inspect_body(
                record, resource, status=response.status, final_url=response.geturl(),
                content_type=content_type, body=body,
                charset=response.headers.get_content_charset() or "utf-8",
                complete_body=not text_content,
            )
    except urllib.error.HTTPError as error:
        record.update({"status": error.code, "final_url": error.geturl(), "access": "failed", "error": str(error)})
    except urllib.error.URLError as error:
        if isinstance(error.reason, ssl.SSLCertVerificationError):
            try:
                return curl_retrieve(record, resource, url)
            except (OSError, subprocess.SubprocessError, ValueError) as curl_error:
                record.update({"status": None, "final_url": None, "access": "failed", "error": f"{error}; system-trust retry failed: {curl_error}"})
                return record
        record.update({"status": None, "final_url": None, "access": "failed", "error": str(error)})
    except (TimeoutError, OSError, ValueError) as error:
        record.update({"status": None, "final_url": None, "access": "failed", "error": str(error)})
    return record


def scan_markdown_urls(root: Path = ROOT) -> dict[str, list[str]]:
    result = subprocess.run(["git", "ls-files", "--", "*.md"], cwd=root, capture_output=True, text=True, check=True)
    observed: dict[str, list[str]] = {}
    for relative in result.stdout.splitlines():
        path = root / relative
        if not path.is_file():
            # A tracked file can be intentionally moved in the current worktree;
            # only authored bytes that actually exist can contribute URLs.
            continue
        text = FENCED_CODE.sub("", path.read_text(encoding="utf-8", errors="replace"))
        for match in URL.finditer(text):
            normalized = normalize_url(match.group(0))
            host = urllib.parse.urlsplit(normalized).netloc
            if host in {"localhost", "127.0.0.1"} or host.startswith(("localhost:", "127.0.0.1:")) or "YOUR-" in normalized:
                continue
            observed.setdefault(normalized, []).append(relative)
    return observed


def _claim_sources(module_root: Path) -> set[str]:
    ledger = json.loads((module_root / "assessment" / "factual-claims.json").read_text(encoding="utf-8"))
    return {source for claim in ledger.get("claims", []) for source in claim.get("source_ids", [])}


def inventory(module: str | None = None) -> tuple[list[tuple[str, str, str, dict[str, Any], bool]], set[str]]:
    items: list[tuple[str, str, str, dict[str, Any], bool]] = []
    registered: set[str] = set()
    for manifest_path in sorted((ROOT / "modules").glob("*/module.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if module and manifest["id"] != module.upper():
            continue
        module_relative = manifest_path.parent.relative_to(ROOT).as_posix()
        claim_sources = _claim_sources(manifest_path.parent)
        for kind, rows in (("assigned_resource", manifest["resources"]), ("direct_citation", manifest.get("citation_catalog", []))):
            for resource in rows:
                blocking = bool(resource["required"] or resource["id"] in claim_sources)
                items.append((manifest["id"], module_relative, kind, resource, blocking))
                registered.add(normalize_url(resource["url"]))
    if module is None:
        global_resources = json.loads((ROOT / "course-resources.json").read_text(encoding="utf-8"))["resources"]
        for resource in global_resources:
            items.append(("GLOBAL", "", "setup_resource", resource, bool(resource["required"])))
            registered.add(normalize_url(resource["url"]))
    return items, registered


def evaluate_records(records: list[dict[str, Any]], attestations: dict[str, dict[str, Any]]) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []
    for record in records:
        key = record["resource_key"]
        fallback = ROOT / record["local_fallback"]
        if record["blocking"] and record.get("access") != "retrieved" and not fallback.is_file():
            failures.append(f"{key}: blocking source could not be retrieved and has no verified local fallback")
        elif record["blocking"] and record.get("access") != "retrieved":
            warnings.append(f"{key}: source could not be retrieved; reviewed local fallback remains available")
        if record["blocking"] and not fallback.is_file():
            failures.append(f"{key}: blocking source has no local fallback")
        if record.get("access") != "retrieved":
            continue
        if normalize_url(str(record.get("final_url", ""))) != normalize_url(record["declared_final_url"]):
            failures.append(f"{key}: verified final URL changed")
        binary = record.get("title_match") is None
        if binary:
            attestation = attestations.get(key)
            valid = bool(
                attestation
                and record.get("content_complete") is True
                and normalize_url(str(attestation.get("requested_url", ""))) == normalize_url(record["requested_url"])
                and attestation.get("content_sha256") == record.get("content_sha256")
                and attestation.get("verified_title") == record["declared_title"]
                and attestation.get("verified_publisher") == record["declared_publisher"]
            )
            record["manual_attestation_match"] = valid
            if record["blocking"] and not valid:
                failures.append(f"{key}: binary source lacks matching title/publisher/content-hash attestation")
            elif not valid:
                warnings.append(f"{key}: optional binary source lacks a current manual attestation")
        else:
            if record["blocking"] and record.get("title_match") is not True:
                failures.append(f"{key}: structured remote title does not match declared title")
            if record["blocking"] and record.get("publisher_match") is not True:
                failures.append(f"{key}: structured remote authority does not match declared publisher")
    return failures, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError(f"refusing to overwrite verification report: {args.output}")
    items, registered = inventory(args.module)
    if not items:
        raise ValueError("no resources selected")
    unregistered: dict[str, list[str]] = {}
    if args.module is None:
        unregistered = {url: paths for url, paths in scan_markdown_urls().items() if url not in registered}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        records = list(executor.map(retrieve, items))
    records.sort(key=lambda row: (row["module"], row["resource_id"]))
    attestation_path = ROOT / "resource-verification-attestations.json"
    attestation_data = json.loads(attestation_path.read_text(encoding="utf-8")) if attestation_path.is_file() else {"schema_version": "2.0", "records": []}
    attestation_schema = json.loads((ROOT / "schemas" / "resource-verification-attestations.schema.json").read_text(encoding="utf-8"))
    validate_instance(attestation_data, attestation_schema, label="resource-verification-attestations.json")
    attestation_rows = attestation_data["records"]
    keys = [row["resource_key"] for row in attestation_rows]
    if len(keys) != len(set(keys)):
        raise ValueError("resource verification attestations contain duplicate resource keys")
    attestations = {row["resource_key"]: row for row in attestation_rows}
    failures, warnings = evaluate_records(records, attestations)
    for url, paths in sorted(unregistered.items()):
        failures.append(f"unregistered authored URL {url}: {sorted(set(paths))}")
    report = {
        "schema_version": "2.0",
        "verified_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "method": "bounded HTTP GET with redirects; structured title/publisher metadata; exact authored-URL inventory; local fallback check; full binary SHA-256 attestation",
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "warnings": warnings,
        "unregistered_urls": unregistered,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Resource verification {report['status']}: {len(records)} records, {len(failures)} blocking failures, {len(warnings)} warnings")
    for failure in failures:
        print(f"- {failure}")
    return 0 if not failures else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, SchemaContractError, json.JSONDecodeError, subprocess.SubprocessError) as error:
        print(f"Resource verification failed: {error}", file=sys.stderr)
        raise SystemExit(1)
