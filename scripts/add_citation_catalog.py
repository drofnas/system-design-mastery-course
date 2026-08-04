#!/usr/bin/env python3
"""Install the reviewed direct-citation catalogs into module manifests."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIED = "2026-08-04"


def citation(identifier: str, title: str, publisher: str, url: str, fallback: str, boundary: str) -> dict:
    return {
        "id": identifier,
        "title": title,
        "author_or_publisher": publisher,
        "type": "primary-source citation",
        "url": url,
        "required": True,
        "access": "free",
        "purpose": "Provide primary-source support for the bounded mechanism discussed in the cited local lesson.",
        "reading_boundary": boundary,
        "last_verified": VERIFIED,
        "text_alternative": fallback,
        "verified_title": title,
        "verified_publisher": publisher,
        "verification_method": "HTTP GET plus primary-source metadata comparison",
        "final_url": url,
        "verification_status": "verified",
    }


CATALOGS = {
    "M01": [
        citation("CIT-01", "Early Analysis of Software Architecture", "Software Engineering Institute", "https://www.sei.cmu.edu/library/early-analysis-of-software-architecture/", "lessons/07-failure-models-and-adversarial-review.md", "Read the abstract and collection description on quality-attribute mechanisms, sufficiency of architecture evidence, and risk analysis."),
        citation("CIT-02", "Architecture Tradeoff Analysis Method® Collection", "Software Engineering Institute", "https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/", "lessons/08-decisions-rfcs-and-defense.md", "Read the Description, nine ATAM steps, outputs, and benefits; the multi-day facilitated process is context, not a solo-course requirement."),
    ],
    "M03": [
        citation("CIT-01", "write(2) — Linux manual page", "Linux man-pages project", "https://www.man7.org/linux/man-pages/man2/write.2.html", "lessons/05-files-page-cache-and-durability.md", "Read Description, Return Value, Notes, and Bugs; distinguish write completion from durable storage."),
        citation("CIT-02", "Resource constraints", "Docker", "https://docs.docker.com/engine/containers/resource_constraints/", "lessons/07-containers-quotas-and-limits.md", "Read memory, CPU, and block-I/O constraint sections and note host and cgroup prerequisites."),
    ],
    "M04": [
        citation("CIT-01", "timeit — Measure execution time of small code snippets", "Python Software Foundation", "https://docs.python.org/3/library/timeit.html", "lessons/02-controlled-experiments.md", "Read the command-line interface, default repetition behavior, and timing caveats; do not generalize microbenchmarks to production."),
        citation("CIT-02", "Tracing API", "OpenTelemetry", "https://opentelemetry.io/docs/specs/otel/trace/api/", "lessons/03-trace-context.md", "Read TracerProvider, Tracer, Span creation, context propagation, links, events, status, and shutdown boundaries."),
        citation("CIT-03", "OpenTelemetry Metrics", "OpenTelemetry", "https://opentelemetry.io/docs/specs/otel/metrics/", "lessons/04-signals-cardinality-cost.md", "Read the data model overview, instrument guidance, attribute requirements, aggregation, and cardinality limits."),
        citation("CIT-04", "OpenTelemetry Logging", "OpenTelemetry", "https://opentelemetry.io/docs/specs/otel/logs/", "lessons/04-signals-cardinality-cost.md", "Read the log data model, severity, trace correlation, resource, and attribute guidance."),
        citation("CIT-05", "OpenTelemetry Profiles", "OpenTelemetry", "https://opentelemetry.io/docs/specs/otel/profiles/", "lessons/05-profiling.md", "Read the profile data model overview, mappings, timestamps, stack traces, and stability statements."),
        citation("CIT-06", "sqlite3 — DB-API 2.0 interface for SQLite databases", "Python Software Foundation", "https://docs.python.org/3/library/sqlite3.html", "lessons/06-dependencies-query-plans.md", "Read transaction control and EXPLAIN-related API boundaries used by the local SQLite experiment."),
        citation("CIT-07", "statistics — Mathematical statistics functions", "Python Software Foundation", "https://docs.python.org/3/library/statistics.html", "lessons/07-benchmarks-regression-budgets.md", "Read median and quantiles contracts, including method and small-sample caveats used by the deterministic checker."),
    ],
    "M05": [
        citation("CIT-01", "Default Address Selection for Internet Protocol Version 6 (IPv6)", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc6724.html", "lessons/02-dns-routing-and-discovery.md", "Read Sections 2, 5, 6, and 8 for policy tables, source/destination selection, and implementation boundaries."),
        citation("CIT-02", "Happy Eyeballs Version 2: Better Connectivity Using Concurrency", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc8305.html", "lessons/02-dns-routing-and-discovery.md", "Read Sections 2 through 5 for lookup, sorting, connection racing, delay, and state-management requirements."),
        citation("CIT-03", "Requirements for IP Version 4 Routers", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc1812.html", "lessons/02-dns-routing-and-discovery.md", "Read Section 5.2.4.3 on route selection and longest-prefix matching; treat obsolete adjacent requirements historically."),
        citation("CIT-04", "Negative Caching of DNS Resolution Failures", "Internet Engineering Task Force", "https://datatracker.ietf.org/doc/rfc9520/", "lessons/02-dns-routing-and-discovery.md", "Read Sections 2 through 6 for failure caching, TTL handling, delegation behavior, and security considerations."),
        citation("CIT-05", "HTTP/3", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc9114.html", "lessons/07-quic-http3-streams.md", "Read Sections 2 through 4, 6, and 8 for stream mapping, connection setup, request cancellation, and error handling."),
    ],
    "M06": [
        citation("CIT-01", "Status Codes", "gRPC Authors", "https://grpc.io/docs/guides/status-codes/", "lessons/04-idempotency-and-deduplication.md", "Read the complete status-code table and the notes about library-generated codes; retryability remains operation-specific."),
    ],
    "M08": [
        citation("CIT-01", "13.1. Introduction", "PostgreSQL Global Development Group", "https://www.postgresql.org/docs/current/mvcc-intro.html", "lessons/04-occ-mvcc-write-skew.md", "Read the MVCC introduction and follow its linked transaction-isolation section for version-specific PostgreSQL behavior."),
        citation("CIT-02", "Perform testing for recovery from data loss", "Google Cloud", "https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-data-loss", "lessons/08-decisions-migration-ownership.md", "Read the recovery-testing recommendations, validation steps, ownership guidance, and stated cloud applicability boundary."),
    ],
}


def main() -> int:
    for path in sorted((ROOT / "modules").glob("*/module.json")):
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["citation_catalog"] = CATALOGS.get(manifest["id"], [])
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{manifest['id']}: {len(manifest['citation_catalog'])} direct citations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
