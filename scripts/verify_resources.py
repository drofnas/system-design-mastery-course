#!/usr/bin/env python3
"""Retrieve course resources and record redirects, access, and title evidence."""
from __future__ import annotations

import argparse
import concurrent.futures
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

ROOT = Path(__file__).resolve().parents[1]
MAX_READ = 786_432
STOP_WORDS = {"a", "an", "and", "for", "in", "of", "on", "the", "to", "with", "documentation", "guide"}
AUTHORITY_ALIASES = {
    "aws.amazon.com": "amazon web services builders library",
    "builder.aws.com": "amazon web services builders library",
    "opentelemetry.io": "opentelemetry maintainers cncf",
    "15445.courses.cs.cmu.edu": "carnegie mellon university",
    "github.com/hdrhistogram/hdrhistogram": "gil tene michael barker hdrhistogram maintainers",
    "github.com/facebook/rocksdb": "rocksdb maintainers meta",
    "debezium.io": "debezium project maintainers",
    "slsa.dev": "openssf slsa project",
    "docs.oracle.com": "oracle java community process",
}


def normalize_words(value: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9]+", html.unescape(value).lower()) if len(word) > 1 and word not in STOP_WORDS}


def authority_words(url: str) -> set[str]:
    parsed = urllib.parse.urlsplit(url)
    identity = f"{parsed.netloc.lower()}{parsed.path.lower()}"
    words = normalize_words(identity)
    for prefix, aliases in AUTHORITY_ALIASES.items():
        if identity.startswith(prefix):
            words |= normalize_words(aliases)
    return words


def inspect_body(
    record: dict[str, Any], resource: dict[str, Any], *, status: int,
    final_url: str, content_type: str, body: bytes, charset: str = "utf-8",
    transport: str = "python-stdlib",
) -> dict[str, Any]:
    record.update({
        "status": status,
        "final_url": final_url,
        "content_type": content_type,
        "bytes_inspected": len(body),
        "access": "retrieved" if 200 <= status < 400 else "failed",
        "transport": transport,
    })
    if content_type in {"text/html", "application/xhtml+xml", "text/plain"}:
        text = body.decode(charset, errors="replace")
        title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
        remote_title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", title_match.group(1))).strip() if title_match else ""
        declared_words = normalize_words(resource["title"])
        remote_words = normalize_words(remote_title)
        publisher_words = normalize_words(resource["author_or_publisher"])
        body_words = normalize_words(re.sub(r"<[^>]+>", " ", text))
        url_words = authority_words(final_url)
        title_evidence_words = remote_words | body_words | url_words
        publisher_evidence_words = body_words | url_words
        remote_overlap = len(declared_words & remote_words) / max(1, len(declared_words))
        evidence_overlap = len(declared_words & title_evidence_words) / max(1, len(declared_words))
        publisher_overlap = len(publisher_words & publisher_evidence_words) / max(1, len(publisher_words))
        record.update({
            "remote_title": remote_title,
            "remote_title_overlap": round(remote_overlap, 3),
            "title_evidence_overlap": round(evidence_overlap, 3),
            "title_match": evidence_overlap >= 0.5,
            "publisher_overlap": round(publisher_overlap, 3),
            "publisher_match": publisher_overlap >= 0.5,
        })
    else:
        record.update({"remote_title": None, "title_match": None, "publisher_match": None, "metadata_note": "binary source metadata requires the declared manual primary-source comparison"})
    return record


def curl_retrieve(record: dict[str, Any], resource: dict[str, Any], url: str) -> dict[str, Any]:
    """Retry with the operating-system trust store without disabling TLS validation."""
    with tempfile.TemporaryDirectory(prefix="course-resource-") as directory:
        body_path = Path(directory) / "body"
        result = subprocess.run(
            [
                "curl", "--location", "--fail", "--silent", "--show-error",
                "--max-time", "25", "--range", f"0-{MAX_READ - 1}",
                "--header", "Accept: text/html,application/pdf,text/plain,*/*;q=0.5",
                "--user-agent", "system-design-mastery-course-resource-verifier/1.0",
                "--output", str(body_path),
                "--write-out", "%{http_code}\n%{url_effective}\n%{content_type}",
                url,
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            raise OSError(result.stderr.strip() or f"curl exited {result.returncode}")
        metadata = result.stdout.splitlines()
        if len(metadata) < 3:
            raise OSError("curl did not return verification metadata")
        status = int(metadata[0])
        final_url = metadata[1]
        content_type = metadata[2].split(";", 1)[0].strip().lower()
        body = body_path.read_bytes()[:MAX_READ]
        return inspect_body(
            record, resource, status=status, final_url=final_url,
            content_type=content_type, body=body, transport="curl-system-trust",
        )


def retrieve(item: tuple[str, str, dict[str, Any]]) -> dict[str, Any]:
    module_id, module_relative, resource = item
    url = str(resource["url"])
    request = urllib.request.Request(url, headers={
        "User-Agent": "system-design-mastery-course-resource-verifier/1.0",
        "Accept": "text/html,application/pdf,text/plain,*/*;q=0.5",
        "Accept-Encoding": "identity",
        "Range": f"bytes=0-{MAX_READ - 1}",
    })
    record: dict[str, Any] = {
        "module": module_id,
        "resource_id": resource["id"],
        "required": resource["required"],
        "declared_title": resource["title"],
        "declared_publisher": resource["author_or_publisher"],
        "requested_url": url,
        "reading_boundary": resource["assignment"],
        "local_fallback": f"{module_relative}/{resource['text_alternative']}",
    }
    try:
        context = ssl.create_default_context()
        with urllib.request.urlopen(request, timeout=25, context=context) as response:
            body = response.read(MAX_READ)
            content_type = response.headers.get_content_type()
            charset = response.headers.get_content_charset() or "utf-8"
            return inspect_body(
                record, resource, status=response.status, final_url=response.geturl(),
                content_type=content_type, body=body, charset=charset,
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError(f"refusing to overwrite verification report: {args.output}")
    items: list[tuple[str, str, dict[str, Any]]] = []
    for manifest_path in sorted((ROOT / "modules").glob("*/module.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if args.module and manifest["id"] != args.module.upper():
            continue
        module_relative = manifest_path.parent.relative_to(ROOT).as_posix()
        items.extend((manifest["id"], module_relative, resource) for resource in manifest["resources"])
    if not items:
        raise ValueError("no resources selected")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        records = list(executor.map(retrieve, items))
    records.sort(key=lambda row: (row["module"], row["resource_id"]))
    failures = []
    for record in records:
        fallback = ROOT / record["local_fallback"]
        if record["required"] and (record["access"] != "retrieved" or not fallback.is_file()):
            failures.append(f"{record['module']} {record['resource_id']}: required access/fallback failure")
        if record["required"] and record.get("title_match") is False:
            failures.append(f"{record['module']} {record['resource_id']}: remote title does not match the declared title")
        if record["required"] and record.get("publisher_match") is False:
            failures.append(f"{record['module']} {record['resource_id']}: remote authority does not match the declared publisher")
    report = {
        "schema_version": "1.0",
        "verified_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "method": "bounded HTTP GET with redirects, access check, declared-title comparison against HTML title/body and final URL, publisher-token observation, and local-fallback existence check",
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Resource verification {report['status']}: {len(records)} records, {len(failures)} blocking failures")
    for failure in failures:
        print(f"- {failure}")
    return 0 if not failures else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"Resource verification failed: {error}", file=sys.stderr)
        raise SystemExit(1)
