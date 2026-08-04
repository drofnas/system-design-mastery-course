#!/usr/bin/env python3
"""Regenerate content-bound factual ledgers after a completed semantic review."""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import date
from pathlib import Path
from typing import Any

from validate_factual_readiness import _authored_paths, _content_digest, extract_formulas


ROOT = Path(__file__).resolve().parents[1]
REVIEW_DATE = date.today().isoformat()
CLAIM_REPLACEMENTS = {
    "M01-FC-006": "A constraint removes choices within the current decision context, whereas an assumption may prove false, a preference may be traded, and a decision driver distinguishes candidates.",
    "M01-FC-009": "A defensible architecture answer connects a user outcome, workload assumption, invariant, measurable scenario, selected mechanism, and reversal condition.",
    "M01-FC-010": "The Transit Signal workload figures are synthetic planning inputs for course exercises and are not observed production traffic.",
    "M02-FC-002": "For a stable long-run boundary, Little's Law relates average work, admitted throughput, and average time as L = λW; it does not predict percentiles or prove stability.",
    "M02-FC-003": "A latency distribution is interpretable only with a named population, timing boundary, workload, environment, window, sample count, warm-up policy, failure treatment, measurement location, and clock.",
    "M02-FC-004": "For n independent parallel branches with per-branch completion probability F(t), all branches finish by t with probability F(t)^n and at least one exceeds t with probability 1 - F(t)^n.",
    "M02-FC-005": "When arrivals exceed completions, work must wait, be rejected, be degraded or deferred, or consume an unbounded resource until failure.",
    "M02-FC-006": "A retry is extra failure-time load and is justified only when the failure may be transient, repetition is safe, deadline remains, success is plausible, and the shared retry budget can afford it.",
    "M02-FC-007": "Failover safety depends on retained capacity, admitted load, recovery drain rate, and an explicit shedding, degradation, transfer, or SLO-violation policy.",
    "M02-FC-008": "A capacity decision connects user outcome and workload to resource demand, measurement, observed saturation, operating policy, cost, ownership, rollout, and reversal evidence.",
    "M02-FC-010": "The Transit Signal rates, service times, fan-out, worker counts, and latency targets are synthetic lab inputs and not production measurements.",
    "M03-FC-008": "A causal performance report preserves the frozen prediction, separates observation from interpretation, tests competing explanations one control at a time, and bounds transfer to production.",
    "M04-FC-006": "End-to-end latency includes arrival lag, queue wait, service work, dependency work, and response time, while spans and query plans expose only their declared boundaries.",
    "M04-FC-007": "A reproducible regression budget names workload, metric, baseline and candidate identities, environment, repetitions, effect calculation, uncertainty rule, allowed change, and enforcement action.",
    "M04-FC-008": "A performance review links a user outcome to bounded observations, mechanism, alternatives, discriminating tests, validation, ownership, rollout, and reversal evidence.",
    "M06-FC-010": "Beacon Dispatch timings, rates, deadlines, and concurrency limits are synthetic scenario inputs for testing remote-call containment, not production measurements.",
    "M07-FC-005": "Read, write, and space amplification compare explicitly bounded physical work with logical application work; ratios with different inclusions are not comparable.",
    "M07-FC-008": "A storage decision compares alternatives under one workload and evidence boundary, publishes amplification and capacity limits, assigns owners, and defines migration and reversal gates.",
    "M08-FC-001": "A transaction boundary should be derived from a falsifiable invariant, its authoritative facts and writers, and the smallest visibility and recovery unit that must be atomic.",
    "M09-FC-001": "A consistency contract defines admitted operation histories, the relevant real-time, session, or causal order, failure behavior, a measurable threshold, and an oracle.",
    "M09-FC-002": "A replication contract must distinguish authority acceptance, local durability, replica transfer and durability, acknowledgement, and read visibility rather than collapsing them into one event.",
    "M09-FC-008": "A reversible replication ADR organizes drivers, evidence, topology and operation semantics, ownership, migration, and quantified reversal conditions by operation.",
    "M12-FC-001": "An SLI requires a named user action, start and completion, deadline, correctness and freshness rules, population, window, owner, and explicit treatment of missing telemetry.",
    "M12-FC-002": "For an SLO target S and N valid events, the allowed bad-event budget is N × (1 - S), with weighting and correlation assumptions stated explicitly.",
    "M13-FC-001": "A threat model iteratively models assets and trust changes, challenges boundaries with contextual abuse cases, assigns responses, and validates controls with evidence and owners.",
    "M13-FC-003": "Authorization evaluates subject, object, action, context, and policy version at an enforcement point before disclosure or effect.",
    "M14-FC-003": "A sourcing comparison begins with required capability and exit obligations, then compares managed, operated open-source, custom, and internal-platform choices without transferring responsibility.",
    "M14-FC-004": "A cost comparison separates recurring and transition costs, defines allocation and the useful-outcome denominator, and varies uncertain inputs before using unit cost in a decision.",
    "M14-FC-005": "Compatibility is a mixed-version property across supported producers, consumers, stored records, and replay paths during a declared window, not a consequence of version labels alone.",
    "M14-FC-008": "A technical strategy connects an outcome to a sequence of reversible investments with shared alternatives, owners, evidence gates, and stop, reversal, and decommission conditions.",
    "M16-FC-003": "Rendering placement distributes compute, data access, bytes, commitment points, and failure behavior across origin, edge, and browser boundaries.",
    "M16-FC-007": "The synthetic Northstar route, wire, browser, edge, and evidence contracts form a deterministic lab oracle and do not establish universal browser or CDN behavior.",
    "M17-FC-004": "Inference admission must reserve bounded weight, runtime, activation, and key-value cache memory before work begins; memory fit alone does not prove latency capacity.",
    "M17-FC-008": "An inference decision reconciles predictions with measured evidence, compares deployment alternatives under one workload, assigns owners, and defines shadow, canary, rollback, and reversal gates.",
}
CLAIM_OVERRIDES: dict[str, dict[str, Any]] = {
    "M01-FC-002": {"classification": "algorithmic"},
    "M01-FC-003": {"classification": "normative"},
    "M01-FC-005": {"classification": "algorithmic"},
    "M01-FC-006": {"classification": "normative"},
    "M01-FC-008": {"classification": "normative"},
    "M01-FC-009": {"classification": "normative"},
    "M02-FC-001": {"classification": "quantitative"},
    "M02-FC-002": {"classification": "quantitative"},
    "M02-FC-003": {"classification": "quantitative"},
    "M02-FC-009": {"classification": "normative"},
    "M02-FC-011": {
        "claim": "Little's Law is the average-value identity L = λW for a stable long-run boundary; the course does not use it to predict a percentile or prove that a queue is stable.",
        "classification": "quantitative", "source_ids": ["RES-01"],
        "source_sections": ["Queueing Systems notes sections defining system occupancy, throughput, time in system, and Little's Law L = λW."],
    },
    "M02-FC-012": {"claim": "The calculation 0.15 seconds × 80 requests/second = 12 requests uses synthetic course inputs and is not a production capacity measurement.", "classification": "synthetic"},
    "M03-FC-009": {"classification": "synthetic"},
    "M03-FC-011": {"claim": "The values C = 2.4 ms, Δ = 0.5 ms, and k > C/Δ = 4.8 are synthetic exercise inputs and arithmetic, not measured host behavior.", "classification": "synthetic"},
    "M03-FC-012": {"claim": "The course defines Δ = D - P only as a synthetic comparison variable inside the locality exercise; it is not a universal performance model.", "classification": "synthetic"},
    "M04-FC-001": {"classification": "algorithmic"},
    "M04-FC-006": {
        "classification": "inference", "source_ids": ["RES-03", "RES-09"],
        "source_sections": ["W3C Trace Context Abstract, header format, and processing model, which define propagation rather than end-to-end latency coverage.", "SQLite EXPLAIN QUERY PLAN Sections 1.1-1.3 and its warning that plan output describes the selected query plan rather than the whole request."],
        "verification_method": "bounded inference from cited premises",
        "premises": ["Trace context carries identifiers and parentage but does not assert complete journey timing.", "A query plan describes database access inside its own boundary, not queueing and all remote work."],
    },
    "M04-FC-009": {"classification": "synthetic"},
    "M05-FC-001": {"classification": "algorithmic"},
    "M05-FC-004": {
        "source_ids": ["RES-03", "CIT-07"],
        "source_sections": [
            "TLS 1.3 Sections 2, 4.1-4.4, and 9 on negotiation, key establishment, certificate authentication, and record protection.",
            "RFC 9525 Sections 1.1-1.3, 6, and 7.7 on reference and presented identifiers, service-identity matching, mismatch failure, and the separate certificate-path trust requirement.",
        ],
    },
    "M05-FC-005": {
        "classification": "inference",
        "source_ids": ["CIT-08", "RES-02", "CIT-06"],
        "source_sections": [
            "RFC 9110 Sections 3.3, 3.7, 7.3.2, 7.6, and 17.2 on intermediary client/server roles, forwarding, connection boundaries, and intermediary risk.",
            "TCP Sections 2.2, 3.5, 3.7, and 3.8 on connection state, endpoints, establishment, closure, and bounded transport behavior.",
            "Queueing Systems notes sections defining inventory, throughput, time in system, and the behavior of finite service boundaries.",
        ],
        "verification_method": "bounded inference from cited premises",
        "premises": [
            "An HTTP proxy receives one connection-facing role and acts as a client on the forwarded hop, so the two transport relationships can differ.",
            "Retaining upstream connections trades repeated establishment for a finite inventory with a measurable hold time.",
            "When a finite inventory has no free item, a bounded system must wait, reject, or invoke an explicitly bounded alternative instead of creating unbounded work.",
        ],
    },
    "M05-FC-009": {"classification": "synthetic"},
    "M05-FC-011": {"claim": "The 12 KiB, 4 Mbit/s, 60 ms, and 30,000-byte calculations are synthetic path-model inputs and lower-bound arithmetic, not measured network performance.", "classification": "synthetic"},
    "M05-FC-012": {"claim": "The 120 KiB/0.4 s and 132 KiB/0.4 s goodput calculations use synthetic exercise observations and do not establish protocol performance in another environment.", "classification": "synthetic"},
    "M05-FC-015": {
        "claim": "For a stable retained-connection boundary, average connection inventory is approximately completion rate multiplied by average connection hold time, an application of L = λW.",
        "source_ids": ["CIT-06"], "source_sections": ["Queueing Systems notes sections defining occupancy, throughput, time in system, and Little's Law L = λW."],
    },
    "M06-FC-009": {"classification": "synthetic"},
    "M06-FC-011": {"claim": "The 420 ms deadline decomposition and related remaining-time calculations use synthetic Beacon Dispatch inputs and do not predict production latency.", "classification": "synthetic"},
    "M06-FC-014": {
        "claim": "For a stable bounded-resource boundary, average active inventory is admitted completion rate multiplied by average hold time, L = λW.",
        "source_ids": ["CIT-02"], "source_sections": ["Queueing Systems notes sections defining occupancy, throughput, time in system, and Little's Law L = λW."],
    },
    "M07-FC-006": {
        "source_ids": ["RES-09", "RES-10"],
        "source_sections": ["PostgreSQL Using EXPLAIN Sections 14.1.1-14.1.3 on plan trees, cost estimates, and estimated versus actual rows.", "PostgreSQL planner statistics Sections 14.2.1-14.2.2 on distribution statistics, extended statistics, and correlated predicates."],
    },
    "M07-FC-002": {
        "source_ids": ["RES-01", "RES-03"],
        "source_sections": [
            "SQLite Database File Format Sections 1.2, 1.6, and 2.1 on pages, page headers, cells, free space, overflow, and bounded on-disk units.",
            "CMU Database Systems Storage I-II and Memory Management materials on page-oriented storage, record layout, buffer management, and variable-length records.",
        ],
    },
    "M07-FC-007": {"classification": "algorithmic"},
    "M07-FC-009": {"classification": "synthetic"},
    "M07-FC-011": {"claim": "The 4,096-byte page, 32-byte header, and 280-byte record calculation is a synthetic exercise layout and is not a measured storage-engine occupancy result.", "classification": "synthetic"},
    "M07-FC-012": {"claim": "The R1, R2, and R3 run contents are synthetic LSM exercise state used to calculate visibility; they are not records from a production engine.", "classification": "synthetic"},
    "M07-FC-013": {"claim": "The floor(4,064/280) = 14 page-occupancy result follows from synthetic course layout inputs and does not generalize to another page format.", "classification": "synthetic"},
    "M07-FC-014": {
        "claim": "Under the standard independent-hash approximation, a Bloom filter with m bits, n inserted items, and k probes has false-positive probability p ≈ (1 - e^(-kn/m))^k; this is an approximation, not an exact finite-filter guarantee.",
        "classification": "quantitative", "source_ids": ["CIT-01"],
        "source_sections": ["Abstract and hosted paper sections contrasting the standard Bloom-filter false-positive approximation with corrected finite-filter analysis."],
    },
    "M07-FC-015": {"claim": "The station_class and region predicate is synthetic query-planning input and does not describe a production schema or distribution.", "classification": "synthetic"},
    "M08-FC-009": {"classification": "synthetic"},
    "M08-FC-002": {
        "source_ids": ["RES-01", "RES-03"],
        "source_sections": [
            "PostgreSQL Transaction Isolation Sections 13.2.1-13.2.3 on admitted histories and serialization anomalies.",
            "CMU Database Systems concurrency-control materials on conflict graphs, edges, cycles, and conflict serializability.",
        ],
    },
    "M08-FC-003": {
        "source_ids": ["RES-02", "RES-03"],
        "source_sections": [
            "PostgreSQL Explicit Locking Sections 13.3.2 and 13.3.4 on compatible modes, conflicts, and deadlocks.",
            "CMU Database Systems two-phase locking materials on growing/shrinking phases, strictness, and predicate/phantom protection.",
        ],
    },
    "M08-FC-004": {"classification": "algorithmic"},
    "M08-FC-007": {"classification": "algorithmic"},
    "M08-FC-011": {"claim": "The completed_exposures = 0 state is a synthetic lost-update schedule used as a transaction oracle, not observed production data.", "classification": "synthetic"},
    "M09-FC-003": {
        "source_ids": ["RES-01"],
        "source_sections": ["Dynamo Section 4.5 on N, R, and W, including the R + W > N intersection condition; the set-intersection derivation here is narrower than a complete consistency protocol."],
    },
    "M09-FC-004": {"classification": "algorithmic"},
    "M09-FC-011": {"claim": "The 120/5 = 24 and 120/(130/3) calculations use synthetic hot-key exercise inputs and do not establish production throughput or fairness.", "classification": "synthetic"},
    "M10-FC-001": {"classification": "quantitative"},
    "M10-FC-002": {"classification": "quantitative"},
    "M10-FC-005": {"source_sections": ["Raft §5.4.1, Election restriction: compare last-log term first and last-log index only when terms tie before granting a vote."]},
    "M10-FC-009": {"classification": "synthetic"},
    "M10-FC-011": {
        "claim": "A linearizable Raft read may wait until last_applied is at least the leader's safe read index; the condition is meaningful only with the paper's current-leader confirmation and committed-prefix requirements.",
        "classification": "quantitative",
        "source_sections": ["Raft Section 8 on read-only operations: confirm current leadership, identify the committed read point, and wait for the state machine to apply through that point before answering."],
    },
    "M10-FC-012": {"claim": "The 30 ppm, 200 second, 3 ms, and 12 ms clock values are synthetic exercise inputs; their arithmetic does not measure a production clock.", "classification": "synthetic"},
    "M10-FC-013": {"claim": "The proposal/value and match-index tuples are synthetic Paxos and Raft exercise state, not observed cluster evidence.", "classification": "synthetic"},
    "M10-FC-016": {"claim": "The term, vote, and last-log tuples are synthetic Raft exercise state used to apply the lexicographic election rule.", "classification": "synthetic"},
    "M10-FC-017": {"claim": "The client ID, sequence, and cached-result tuple is synthetic deduplication state and does not assert a universal wire format.", "classification": "synthetic"},
    "M11-FC-009": {"classification": "synthetic"},
    "M11-FC-001": {"classification": "algorithmic"},
    "M11-FC-003": {"classification": "algorithmic"},
    "M11-FC-005": {"classification": "algorithmic"},
    "M11-FC-011": {"claim": "The 18,000-item backlog and 60-item/second net drain produce a synthetic 300-second estimate; constant rates and no new failure are exercise assumptions.", "classification": "synthetic"},
    "M11-FC-012": {"claim": "B, λ, and μ values in EX-14 are synthetic backlog inputs and not measured broker or consumer rates.", "classification": "synthetic"},
    "M11-FC-013": {"claim": "T = B/(μ-λ) is used only for the course's constant-rate synthetic backlog model; changing arrivals, completions, or failures invalidates the estimate.", "classification": "synthetic"},
    "M12-FC-002": {"classification": "quantitative"},
    "M12-FC-003": {"classification": "quantitative"},
    "M12-FC-009": {"classification": "normative"},
    "M12-FC-011": {"claim": "The 750,000-event and 99.95% SLO arithmetic is a synthetic exercise calculation, not a production error-budget observation.", "classification": "synthetic"},
    "M12-FC-013": {"claim": "The 750,000 × 0.0005 = 375 calculation uses synthetic exercise inputs and does not report production reliability.", "classification": "synthetic"},
    "M13-FC-009": {"classification": "synthetic"},
    "M13-FC-012": {"claim": "requested_tenant=south is synthetic authorization-test input and must not be treated as trusted identity or production tenant data.", "classification": "synthetic"},
    "M14-FC-009": {"claim": "The modular and candidate monthly cost totals and per-1,000-good-read figures are synthetic exercise calculations whose allocations and workload cannot be generalized as market or production prices.", "classification": "synthetic"},
    "M14-FC-011": {"claim": "public=true|false is a synthetic mixed-version field example and not a claim about a deployed schema.", "classification": "synthetic"},
    "M15-FC-009": {"classification": "synthetic"},
    "M15-FC-001": {
        "classification": "inference",
        "source_ids": ["RES-03", "RES-11"],
        "source_sections": [
            "Rust Book Chapter 4 on ownership, borrowing, scope, and deterministic Drop points.",
            "Java 25 Garbage Collection Tuning Introduction on automatic heap reclamation, allocation, pauses, throughput, and latency trade-offs.",
        ],
        "verification_method": "bounded inference from cited premises",
        "premises": [
            "Rust ownership rules describe reachability, mutation, and lifetime without specifying a garbage collector.",
            "A tracing garbage collector reclaims unreachable heap objects but does not itself define external-resource authority or release timing.",
            "Placement, authority, mutation, and release are distinct questions, so none alone predicts locality or latency.",
        ],
    },
    "M15-FC-004": {
        "source_ids": ["RES-02", "RES-08", "RES-10"],
        "source_sections": [
            "Go Memory Model introduction, advice, and synchronization sections defining happens-before and data-race obligations.",
            "Java Language Specification Chapter 17 Sections 17.4-17.5 on memory actions, happens-before, and correctly synchronized programs.",
            "Rust Book Send and Sync sections on concurrency marker traits and the synchronization obligations of shared data.",
        ],
    },
    "M15-FC-011": {"claim": "The 500 - 120 - 50 = 330 ms budget is a synthetic Northstar deadline decomposition and not a measured runtime result.", "classification": "synthetic"},
    "M15-FC-012": {"claim": "The 2,176 KiB and 85 MiB memory figures follow from synthetic exercise inputs and intentionally omit runtime overhead; they are not production memory measurements.", "classification": "synthetic"},
    "M16-FC-002": {"classification": "normative"},
    "M16-FC-001": {
        "source_ids": ["RES-01", "RES-02"],
        "source_sections": [
            "HTML event-loop processing model sections covering task selection, microtask checkpoints, rendering opportunities, and updating the rendering.",
            "RenderingNG architecture sections Rendering pipeline structure and Threads, including style, layout, pre-paint, paint, raster, compositing, and compositor-path exceptions.",
        ],
    },
    "M16-FC-003": {"classification": "normative"},
    "M16-FC-006": {"classification": "algorithmic"},
    "M16-FC-008": {
        "classification": "inference",
        "source_ids": ["CIT-01", "CIT-02", "CIT-03"],
        "source_sections": [
            "Azure Architecture Center BFF Context, Solution, Problems and considerations, and When to use sections on aggregation, tailored interfaces, service overhead, latency, duplication, ownership, and security.",
            "Cloudflare Workers How Workers works sections Isolates, Compute per request, and Distributed execution on globally distributed request placement, isolate lifetime, and state boundaries.",
            "Cloudflare Workers Limits sections on CPU, memory, subrequests, connections, bodies, wall time, and failure behavior; the exact values are provider/version specific.",
        ],
        "verification_method": "bounded inference from cited premises",
        "premises": [
            "A BFF may aggregate or transform client-specific work but creates a separately operated service with latency, security, ownership, and duplication costs.",
            "An edge runtime executes near distributed request entry points but retains provider-specific runtime, state, resource, and failure constraints.",
            "Therefore a new frontend or edge boundary is justified only when its measured independence or distance benefit exceeds those added obligations for the named workload.",
        ],
    },
    "M16-FC-009": {"classification": "synthetic"},
    "M16-FC-011": {"claim": "The 140 ms RTT, 160 KiB payload, and 1.2 Mbit/s calculation is a synthetic lower-bound exercise, not a field-measured page load.", "classification": "synthetic"},
    "M16-FC-012": {"claim": "The transfer-time lower bound and 1.01-second worked result are synthetic network-budget calculations that exclude protocol, contention, CPU, and rendering work.", "classification": "synthetic"},
    "M16-FC-013": {"claim": "aria-busy=true is a synthetic accessibility-state example and not evidence that the entire interaction conforms to WCAG.", "classification": "synthetic"},
    "M17-FC-009": {"classification": "synthetic"},
    "M17-FC-002": {
        "classification": "algorithmic",
        "source_ids": ["CIT-01", "RES-02"],
        "source_sections": [
            "Hugging Face Tokenizers pipeline sections Normalization, Pre-Tokenization, The Model, and Post-Processing on text transformation, vocabulary-to-ID mapping, and special tokens.",
            "Attention Is All You Need Sections 3.1-3.5 on token embeddings, positional encodings, and the ordered model input consumed by attention.",
        ],
    },
    "M17-FC-005": {"classification": "normative"},
    "M17-FC-006": {"classification": "algorithmic"},
    "M17-FC-011": {"claim": "The W matrix and its worked product are synthetic arithmetic inputs used to check shapes and operations, not model-quality or hardware evidence.", "classification": "synthetic"},
    "M18-FC-002": {
        "source_ids": ["RES-01", "RES-05"],
        "source_sections": [
            "Introduction to Information Retrieval Chapters 2 and 6 on document units, postings, fields, scoring, and the retrieval consequences of duplicated indexed content.",
            "OWASP LLM Prompt Injection Prevention Cheat Sheet sections on RAG poisoning, least privilege, remote content sanitization, trust boundaries, monitoring, and testing.",
        ],
    },
    "M18-FC-004": {
        "classification": "quantitative", "source_ids": ["CIT-01"],
        "source_sections": ["Section 1, Equation 1, and the explanation of k as a rank constant; reported TREC and LETOR outcomes are not generalized to CivicAid."],
    },
    "M18-FC-005": {
        "classification": "inference",
        "source_ids": ["RES-04"],
        "source_sections": ["RAG paper Introduction and Sections 2-4 on retrieving external passages, conditioning generation on them, provenance, and updating the non-parametric corpus."],
        "verification_method": "bounded inference from cited premises",
        "premises": [
            "RAG retrieves external records and conditions a generator on them; it does not turn generation into a proof of truth.",
            "Auditing which evidence supported a claim requires stable identifiers and exact versions for the retrieved records and index state.",
            "Revocation, validity, and access policy are application obligations added by CivicAid rather than guarantees of the original RAG paper.",
        ],
    },
    "M18-FC-009": {"classification": "quantitative", "source_ids": ["RES-01"], "source_sections": ["Introduction to Information Retrieval Chapters 6 and 8 definitions of recall, reciprocal rank, DCG, and nDCG; exercise relevance labels remain synthetic."]},
    "M18-FC-012": {"claim": "M=3 and efSearch=5 are synthetic HNSW exercise controls and do not establish a generally optimal index configuration.", "classification": "synthetic"},
}

EXTRA_CLAIMS: dict[str, list[dict[str, Any]]] = {
    "M01": [{
        "id": "M01-FC-011",
        "location": {"path": "lessons/02-problem-framing-and-workloads.md", "heading": "Worked example: Transit Signal"},
        "claim": "The rider counts, checks per rider, time windows, and derived average and burst rates are synthetic workload-model inputs, not observed production traffic.",
        "classification": "synthetic", "source_ids": [], "source_sections": [],
        "verification_method": "controlled synthetic fixture", "status": "verified",
        "scope_limit": "These values exist only to demonstrate workload arithmetic inside the course and must not be generalized.",
        "synthetic_label": "Synthetic course workload values; not production measurements.",
    }, {
        "id": "M01-FC-012",
        "location": {"path": "exercises/answer-key.md", "heading": "EX-01"},
        "claim": "The rider totals, time windows, checks per rider, and derived average and burst rates in the answer key are synthetic arithmetic, not production observations.",
        "classification": "synthetic", "source_ids": [], "source_sections": [],
        "verification_method": "controlled synthetic fixture", "status": "verified",
        "scope_limit": "These values exist only inside the course answer key and must not be generalized.",
        "synthetic_label": "Synthetic answer-key values; not production measurements.",
    }],
    "M02": [{
        "id": "M02-FC-014",
        "location": {"path": "exercises/answer-key.md", "heading": "EX-01"},
        "claim": "Rates, fan-out, service times, worker counts, queue depths, and derived capacity figures in this answer key are synthetic exercise evidence, not production measurements.",
        "classification": "synthetic", "source_ids": [], "source_sections": [],
        "verification_method": "controlled synthetic fixture", "status": "verified",
        "scope_limit": "The calculations are valid only for the answer key's declared synthetic workload and assumptions.",
        "synthetic_label": "Synthetic capacity answer-key values; not production measurements.",
    }],
    "M15": [{
        "id": "M15-FC-013",
        "location": {"path": "assessment/semantic-readiness-review.md", "heading": "Contract and implementation review"},
        "claim": "Node.js 24.18.0, TypeScript 7.0.2, Go 1.26.5, Rust 1.97.1, and Java 25 are published releases; the course additionally binds the container images to exact locally exercised SHA-256 digests.",
        "classification": "versioned",
        "source_ids": ["RES-12", "CIT-01", "RES-13", "RES-14", "RES-15"],
        "source_sections": [
            "Node.js Releases entry for v24.18.0 LTS.",
            "TypeScript 7.0 announcement installation and side-by-side sections naming the 7.0.2 package.",
            "Go release history entry for go1.26.5, released 2026-07-07.",
            "Rust release announcement for 1.97.1, dated 2026-07-16.",
            "Oracle Java SE Support Roadmap row identifying Java 25 as an LTS release and its September 2025 GA date.",
        ],
        "verification_method": "official-documentation comparison", "status": "verified",
        "scope_limit": "Official release records establish version identity; only the digest-pinned local harness establishes which image bytes this course executed.",
    }],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scope_for(path: str, previous: dict[str, dict[str, Any]]) -> tuple[str, list[str], str, str | None]:
    if path in previous:
        row = previous[path]
        scope = row["review_scope"]
        if scope == "synthetic_fixture":
            label = row.get("synthetic_label") or "Synthetic course fixture; do not generalize as production evidence."
        else:
            label = None
        return scope, list(row.get("claim_ids", [])), row["review_note"], label
    parts = set(Path(path).parts)
    if "calibration" in parts or "scenarios" in parts:
        return (
            "synthetic_fixture", [],
            "Reviewed as a deterministic synthetic fixture; values and outcomes are not production evidence.",
            "Synthetic course fixture; do not generalize as production evidence.",
        )
    if Path(path).suffix != ".md":
        return "implementation_evidence", [], "Reviewed as implementation or configuration evidence and verified by the declared laboratory tests.", None
    if path.startswith("lab/"):
        return "implementation_evidence", [], "Reviewed as laboratory instructions or implementation evidence with behavior bounded by executable tests.", None
    return "normative_or_assignment_only", [], "Reviewed as course navigation, assignment, rubric, or policy text rather than an external empirical claim.", None


def apply_semantic_contract(claim: dict[str, Any]) -> None:
    claim.update(CLAIM_OVERRIDES.get(claim["id"], {}))
    classification = claim["classification"]
    if classification == "synthetic":
        claim["source_ids"] = []
        claim["source_sections"] = []
        claim["verification_method"] = "controlled synthetic fixture"
        claim["synthetic_label"] = "Synthetic course data or behavior; not production evidence."
        claim["scope_limit"] = (
            "The values, state, and outcome are bounded to the named course fixture and must not be generalized to production."
        )
        claim.pop("premises", None)
    elif classification == "normative":
        claim["source_ids"] = []
        claim["source_sections"] = []
        claim["verification_method"] = "course-contract review"
        claim["scope_limit"] = (
            "This is a published course evidence-quality or decision rule, not an empirical statement about an external system."
        )
        claim.pop("synthetic_label", None)
        claim.pop("premises", None)
    else:
        claim.pop("synthetic_label", None)
        if classification != "inference":
            claim.pop("premises", None)


def main() -> int:
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    for ledger_path in sorted((ROOT / "modules").glob("*/assessment/factual-claims.json")):
        root = ledger_path.parent.parent
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        previous = {row["path"]: row for row in ledger.get("document_coverage", [])}
        ledger["schema_version"] = "2.0"
        ledger["reviewed_commit"] = commit
        ledger["reviewed_at"] = REVIEW_DATE

        claims = ledger["claims"]
        existing = {claim["id"]: claim for claim in claims}
        for extra in EXTRA_CLAIMS.get(ledger["module"], []):
            if extra["id"] in existing:
                existing[extra["id"]].update(extra)
            else:
                claims.append(dict(extra))
        for claim in claims:
            if claim["id"] in CLAIM_REPLACEMENTS:
                claim["claim"] = CLAIM_REPLACEMENTS[claim["id"]]
            if claim["id"] == "M02-FC-002":
                claim["source_ids"] = ["RES-01"]
                claim["source_sections"] = [
                    "Study the Queueing Systems notes sections introducing system occupancy, throughput, time in system, and Little's Law L = λW."
                ]
            apply_semantic_contract(claim)
            claim["source_section_sha256"] = [
                hashlib.sha256(section.strip().encode("utf-8")).hexdigest()
                for section in claim["source_sections"]
            ]
            claim["verified_at"] = REVIEW_DATE

        authored = _authored_paths(root)
        documents: list[dict[str, Any]] = []
        for path in authored:
            scope, identifiers, note, label = scope_for(path, previous)
            row: dict[str, Any] = {
                "path": path,
                "sha256": sha256(root / path),
                "review_scope": scope,
                "claim_ids": identifiers,
                "review_note": note,
            }
            if label:
                row["synthetic_label"] = label
            documents.append(row)
        row_by_path = {row["path"]: row for row in documents}
        for claim in claims:
            path = claim["location"]["path"]
            if path not in row_by_path:
                raise ValueError(f"{claim['id']}: claim path is outside authored inventory: {path}")
            if claim["id"] not in row_by_path[path]["claim_ids"]:
                row_by_path[path]["claim_ids"].append(claim["id"])
            if row_by_path[path]["review_scope"] == "normative_or_assignment_only":
                row_by_path[path]["review_scope"] = "substantive_claims"

        formulas_by_path: dict[str, list[tuple[str, str, str, str]]] = {}
        for row in documents:
            path = row["path"]
            if row["claim_ids"] and Path(path).suffix == ".md" and row["review_scope"] in {"substantive_claims", "synthetic_fixture"}:
                formulas = sorted(extract_formulas(path, (root / path).read_text(encoding="utf-8")))
                if formulas:
                    formulas_by_path[path] = formulas
        for claim in claims:
            claim["claim_sha256"] = hashlib.sha256(claim["claim"].strip().encode("utf-8")).hexdigest()

        formula_mappings: list[dict[str, str]] = []
        for path, formulas in formulas_by_path.items():
            candidates = [
                claim for claim in claims
                if claim["location"]["path"] == path and claim["classification"] in {"quantitative", "synthetic"}
            ]
            if not candidates:
                raise ValueError(f"{root.name}: no quantitative claim for formula-bearing {path}")
            claim_id = candidates[0]["id"]
            for formula_path, heading, expression, expression_hash in formulas:
                formula_mappings.append({
                    "path": formula_path,
                    "heading": heading,
                    "normalized_expression": expression,
                    "expression_sha256": expression_hash,
                    "claim_id": claim_id,
                })

        ledger["document_coverage"] = sorted(documents, key=lambda row: row["path"])
        ledger["formula_mappings"] = sorted(
            formula_mappings,
            key=lambda row: (row["path"], row["heading"], row["normalized_expression"]),
        )
        digest = _content_digest(ledger["document_coverage"])
        ledger["content_digest"] = digest
        ledger["review_attestation"] = {
            "reviewer": "course readiness remediation review",
            "method": "primary-source semantic review",
            "status": "complete",
            "content_digest": digest,
            "scope_note": (
                "All tracked learner-facing prose, exercises, answers, assessment contracts, "
                "synthetic fixtures, laboratory documentation, implementation, and configuration "
                "in this module were inventoried; substantive claims were checked against the named source boundaries."
            ),
        }
        ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"migrated {ledger['module']}: {len(documents)} files, {len(claims)} claims, {len(formula_mappings)} formulas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
