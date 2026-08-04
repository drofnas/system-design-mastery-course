#!/usr/bin/env python3
"""Prepare, reveal, and validate the course's sealed local assessment gates."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import random
import subprocess
import sys
import zlib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ASSURANCE_LIMITATION = (
    "This local envelope prevents accidental answer exposure in the documented workflow. "
    "It is not encryption, an anti-cheating control, or evidence of independent human review; "
    "a determined learner who inspects the implementation can recover the generated reveal."
)


class GateError(ValueError):
    pass


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def digest_json(value: Any) -> str:
    return digest_bytes(canonical_bytes(value))


GATE_MODULES = {
    "G01": ["M01", "M02", "M03"],
    "G02": ["M04", "M05", "M06"],
    "G03": ["M07", "M08", "M09"],
    "G04": ["M10", "M11", "M12"],
    "G05": ["M13", "M14", "M15"],
    "G06": ["M16", "M17", "M18"],
}


VARIANTS: dict[str, list[dict[str, Any]]] = {
    "G01": [
        {
            "title": "Burst traffic crosses the process memory boundary",
            "workload": "A synthetic checkout read path receives a tenfold burst while each admitted request allocates a fixed working set.",
            "observations": [("p99_ms", 1650, "ms"), ("rss_mib", 1180, "MiB"), ("page_faults", 8400, "count"), ("admitted_concurrency", 240, "requests")],
            "invariants": ["p99 latency remains below the declared journey budget", "resident memory remains inside the container limit"],
            "root": "Admission is unbounded relative to per-request memory, so the burst drives reclaim and major faults before useful throughput rises.",
            "explanation": "The architectural quality target omitted a finite concurrency bound; Little's Law predicts excess in-flight work, and the operating-system evidence shows memory pressure rather than insufficient CPU capacity.",
            "repair": "Cap admitted concurrency at 48, reject excess work explicitly, and preserve 25 percent memory headroom.",
            "constraints": [("p99_ms", "<=", 500), ("rss_mib", "<=", 768), ("admitted_concurrency", "<=", 48)],
        },
        {
            "title": "Averages conceal a saturated scheduler queue",
            "workload": "A synthetic API has a 220 millisecond mean target, bursty arrivals, a four-worker CPU pool, and a finite end-to-end deadline.",
            "observations": [("mean_ms", 205, "ms"), ("p99_ms", 2400, "ms"), ("run_queue", 37, "tasks"), ("useful_rps", 38, "requests/s")],
            "invariants": ["the declared user percentile stays within its threshold", "accepted work completes before its absolute deadline"],
            "root": "The decision used an average-latency quality target and admitted more CPU work than the four-worker scheduler could drain.",
            "explanation": "The mean remains plausible while the tail and run queue expose saturation. The quality-attribute scenario and capacity model must share the same percentile, workload window, and finite worker assumption.",
            "repair": "Use a p99 target, admit at most eight CPU tasks, and shed requests that cannot finish inside the remaining deadline.",
            "constraints": [("p99_ms", "<=", 600), ("run_queue", "<=", 8), ("useful_rps", ">=", 36)],
        },
        {
            "title": "Buffered acknowledgement violates the durability invariant",
            "workload": "A synthetic order journal acknowledges records after a userspace write while the host is terminated before durable storage acknowledgement.",
            "observations": [("acknowledged", 1000, "records"), ("recovered", 973, "records"), ("fsync_p99_ms", 18, "ms"), ("lost_records", 27, "records")],
            "invariants": ["every durable acknowledgement survives process and host loss", "the latency target names the durability boundary it measures"],
            "root": "The architecture equated a successful buffered write with durable persistence and never stated the storage failure model.",
            "explanation": "Userspace and page-cache completion do not establish the promised recovery boundary. The decision, capacity cost, and systems experiment must distinguish buffered from durable acknowledgement.",
            "repair": "Acknowledge only after the declared durable boundary and batch durable writes within a bounded group-commit window.",
            "constraints": [("lost_records", "==", 0), ("recovered", "==", 1000), ("fsync_p99_ms", "<=", 30)],
        },
    ],
    "G02": [
        {
            "title": "Retries turn a slow dependency into overload",
            "workload": "A synthetic fan-out journey calls three dependencies; one becomes slow while clients and the service both retry.",
            "observations": [("attempts_per_request", 6.4, "attempts"), ("p99_ms", 3100, "ms"), ("open_connections", 480, "connections"), ("deadline_success_pct", 31, "percent")],
            "invariants": ["retry work remains inside the published retry budget", "all dependency work ends by the caller's absolute deadline"],
            "root": "Layered retries amplify work while each attempt restarts a relative timeout and consumes an unbounded connection slot.",
            "explanation": "Trace evidence connects retry amplification, pool growth, and deadline misses. Network delay is the trigger, but missing end-to-end budgets and admission are the controllable causes.",
            "repair": "Use one retry layer, one absolute deadline, a retry-token budget, and a bounded dependency pool.",
            "constraints": [("attempts_per_request", "<=", 1.3), ("open_connections", "<=", 64), ("deadline_success_pct", ">=", 95)],
        },
        {
            "title": "Connection setup consumes the whole journey budget",
            "workload": "A synthetic mobile client performs DNS, TCP, TLS, proxy, application, and downstream work without connection reuse.",
            "observations": [("setup_round_trips", 5, "round-trips"), ("setup_p99_ms", 820, "ms"), ("journey_p99_ms", 1320, "ms"), ("reuse_pct", 4, "percent")],
            "invariants": ["connection establishment fits its allocated portion of the journey", "fallback behavior preserves the same authority and privacy boundary"],
            "root": "The topology decision assumed warm reusable connections for a client population that mostly creates cold paths.",
            "explanation": "The trace separates name resolution, transport, encryption, proxy, and application time. The remote-call budget must be derived from the real network path rather than a datacenter median.",
            "repair": "Pool and reuse connections, budget cold setup explicitly, and fail safely when the remaining deadline cannot cover downstream work.",
            "constraints": [("setup_round_trips", "<=", 3), ("journey_p99_ms", "<=", 700), ("reuse_pct", ">=", 80)],
        },
        {
            "title": "Telemetry cardinality hides a connection leak",
            "workload": "A synthetic service labels metrics by request identifier while a downstream cancellation path leaves response bodies open.",
            "observations": [("metric_series", 240000, "series"), ("open_connections", 760, "connections"), ("cancelled_requests", 400, "requests"), ("closed_after_cancel", 37, "percent")],
            "invariants": ["telemetry remains inside its cardinality budget", "cancellation closes every acquired network resource"],
            "root": "Unbounded labels consume the observability budget while a missing cancellation cleanup path exhausts the connection pool.",
            "explanation": "High-cardinality telemetry is a separate operational failure from the resource leak, but it delays diagnosis and raises cost. The trace/resource identity is correlation data, not a metric label.",
            "repair": "Remove request IDs from metric dimensions, retain them in traces, and close every response in a cancellation-safe scope.",
            "constraints": [("metric_series", "<=", 2000), ("open_connections", "<=", 64), ("closed_after_cancel", "==", 100)],
        },
    ],
    "G03": [
        {
            "title": "A stale replica admits an invariant-breaking write",
            "workload": "A synthetic inventory workflow reads from a lagging replica and conditionally writes to a different leader during a partition.",
            "observations": [("replica_lag_ms", 4800, "ms"), ("negative_inventory", 7, "items"), ("conflicts", 12, "records"), ("repair_seconds", 95, "s")],
            "invariants": ["inventory never becomes negative", "repair converges without discarding an accepted authoritative write"],
            "root": "The transaction predicate is evaluated on stale state outside the authoritative transaction boundary.",
            "explanation": "Replication staleness changes the correctness of the transaction decision. A storage index or quorum label cannot repair an invariant whose predicate and write occur under different authority.",
            "repair": "Evaluate and enforce the predicate at the authoritative write boundary, then use replicas only for explicitly stale-safe operations.",
            "constraints": [("negative_inventory", "==", 0), ("conflicts", "==", 0), ("repair_seconds", "<=", 60)],
        },
        {
            "title": "A hot partition turns compaction into tail latency",
            "workload": "A synthetic tenant key receives skewed writes while an LSM-shaped store compacts and a partition map moves ranges.",
            "observations": [("hottest_partition_pct", 74, "percent"), ("write_p99_ms", 1900, "ms"), ("write_amplification", 18, "ratio"), ("movement_gib", 96, "GiB")],
            "invariants": ["no tenant can consume the declared partition fairness budget", "resharding preserves availability inside the movement budget"],
            "root": "The partition key concentrates one tenant and resharding competes with foreground compaction for the same finite I/O budget.",
            "explanation": "Logical placement, storage-engine background work, and migration traffic share the physical device. Treating them as independent hides the causal path to tail latency.",
            "repair": "Salt or subdivide the tenant key, rate-limit movement and compaction together, and reserve foreground I/O headroom.",
            "constraints": [("hottest_partition_pct", "<=", 30), ("write_p99_ms", "<=", 500), ("write_amplification", "<=", 8)],
        },
        {
            "title": "A backup exists but cannot satisfy the recovery point",
            "workload": "A synthetic transaction log is retained locally while asynchronous replicas and backups share the same regional failure boundary.",
            "observations": [("declared_rpo_seconds", 60, "s"), ("actual_loss_seconds", 1800, "s"), ("restore_minutes", 210, "min"), ("verified_backups", 0, "count")],
            "invariants": ["tested recovery loss stays within the declared RPO", "a backup is independent of the replicated service failure boundary"],
            "root": "Replication was counted as backup and no restore test verified log continuity or independent failure isolation.",
            "explanation": "Transaction durability, replica availability, and recoverable history are different contracts. The recovery claim needs a restored artifact and measured boundary, not the existence of copies.",
            "repair": "Create independently retained backups, verify log continuity, and exercise restore to the declared recovery point.",
            "constraints": [("actual_loss_seconds", "<=", 60), ("restore_minutes", "<=", 90), ("verified_backups", ">=", 1)],
        },
    ],
    "G04": [
        {
            "title": "A stale leader repeats an irreversible workflow effect",
            "workload": "A synthetic workflow leader loses quorum, retains a lease, and submits an external effect after a new leader is elected.",
            "observations": [("active_leaders", 2, "leaders"), ("effect_attempts", 2, "attempts"), ("accepted_fencing_token", 41, "token"), ("current_fencing_token", 42, "token")],
            "invariants": ["only the current authority can perform the external effect", "workflow replay never duplicates an irreversible effect"],
            "root": "The external system accepts an expired authority because the workflow relies on a lease without enforcing a monotonic fencing token.",
            "explanation": "Consensus establishes the current epoch, messaging can redeliver, and reliability controls must reject stale owners at the effect boundary. A local leader flag is insufficient.",
            "repair": "Carry the committed epoch as a fencing token and reject any effect whose token is lower than the last accepted value.",
            "constraints": [("active_leaders", "==", 1), ("effect_attempts", "==", 1), ("accepted_fencing_token", "==", 42)],
        },
        {
            "title": "Backlog recovery burns the user-journey error budget",
            "workload": "A synthetic event consumer restarts after an outage and processes replay traffic and live traffic in one unbounded queue.",
            "observations": [("backlog_events", 900000, "events"), ("live_p99_ms", 7400, "ms"), ("duplicate_effects", 83, "effects"), ("burn_rate", 19, "ratio")],
            "invariants": ["live traffic retains its declared service objective during replay", "redelivery does not repeat irreversible effects"],
            "root": "Replay has no admission or fairness policy and the consumer performs effects without durable idempotency evidence.",
            "explanation": "The log preserves events but does not provide consumer capacity, fairness, or effect uniqueness. Reliability is measured at the user journey, not broker availability.",
            "repair": "Partition replay from live capacity, enforce weighted admission, and persist an idempotency record atomically with effect state.",
            "constraints": [("live_p99_ms", "<=", 800), ("duplicate_effects", "==", 0), ("burn_rate", "<=", 2)],
        },
        {
            "title": "Failback creates two writable authorities",
            "workload": "A synthetic regional recovery promotes a secondary, then reconnects the original region before authority is reconciled.",
            "observations": [("writable_regions", 2, "regions"), ("conflicting_records", 49, "records"), ("rto_minutes", 38, "min"), ("data_loss_seconds", 0, "s")],
            "invariants": ["at most one region owns writes for a protected keyspace", "failback has an explicit reconciliation and rollback boundary"],
            "root": "The recovery runbook treats failback as routing instead of an authority transfer with fencing and reconciliation.",
            "explanation": "A successful failover and zero observed loss do not establish safe failback. Consensus authority, asynchronous records, and incident roles must agree before writes resume.",
            "repair": "Fence the old region, reconcile divergent state, transfer authority once, and reopen traffic only after invariant checks pass.",
            "constraints": [("writable_regions", "==", 1), ("conflicting_records", "==", 0), ("rto_minutes", "<=", 45)],
        },
    ],
    "G05": [
        {
            "title": "Unchecked runtime input crosses a tenant boundary",
            "workload": "A synthetic migration forwards structurally typed JSON to a new runtime that trusts a caller-supplied tenant field.",
            "observations": [("invalid_payloads_accepted", 38, "requests"), ("cross_tenant_reads", 4, "reads"), ("rollback_minutes", 75, "min"), ("audit_coverage_pct", 61, "percent")],
            "invariants": ["untrusted wire data cannot grant tenant authority", "the migration can roll back without losing audit evidence"],
            "root": "Compile-time shape compatibility replaced runtime validation and authority was derived from request data rather than authenticated context.",
            "explanation": "Language types disappear at the process boundary. The evolution plan, security model, and runtime implementation must preserve one validated schema and an external authority source.",
            "repair": "Apply a closed runtime schema, derive tenant identity from authenticated context, shadow-verify results, and retain a bounded rollback path.",
            "constraints": [("invalid_payloads_accepted", "==", 0), ("cross_tenant_reads", "==", 0), ("audit_coverage_pct", "==", 100)],
        },
        {
            "title": "A dual-write migration exhausts the runtime worker pool",
            "workload": "A synthetic service performs synchronous old/new writes during migration while each request creates unbounded blocking tasks.",
            "observations": [("active_workers", 420, "workers"), ("queue_depth", 2200, "tasks"), ("divergence_records", 17, "records"), ("cost_per_1k", 8.7, "currency/1000")],
            "invariants": ["migration work remains bounded under dependency slowdown", "old and new stores have a verifiable source of truth"],
            "root": "The migration combines unsafe application dual writes with an execution model that admits blocking work without a pool bound.",
            "explanation": "The architecture boundary creates both correctness ambiguity and resource amplification. Extra workers mask neither partial-write divergence nor the lack of a recovery owner.",
            "repair": "Publish changes from one authoritative write, bound migration consumers, reconcile divergence, and define a rollback cutoff.",
            "constraints": [("active_workers", "<=", 64), ("queue_depth", "<=", 256), ("divergence_records", "==", 0)],
        },
        {
            "title": "A leaked secret turns event-loop delay into economic abuse",
            "workload": "A synthetic public endpoint accepts expensive work with a leaked service credential and executes CPU work on an event loop.",
            "observations": [("unauthorized_jobs", 920, "jobs"), ("event_loop_delay_ms", 1250, "ms"), ("daily_cost", 6400, "currency/day"), ("revocation_minutes", 180, "min")],
            "invariants": ["credentials have least privilege and bounded lifetime", "public work cannot monopolize the runtime scheduler or cost budget"],
            "root": "A broad long-lived credential and unbounded CPU admission let unauthorized callers consume both scheduler and financial capacity.",
            "explanation": "Secret lifecycle, economic abuse controls, and runtime scheduling form one causal chain. Moving languages alone does not repair missing authority or bounds.",
            "repair": "Rotate to scoped short-lived credentials, enforce quota before admission, and move bounded CPU work off the event loop.",
            "constraints": [("unauthorized_jobs", "==", 0), ("event_loop_delay_ms", "<=", 50), ("revocation_minutes", "<=", 15)],
        },
    ],
    "G06": [
        {
            "title": "A personalized answer is stored in a shared edge cache",
            "workload": "A synthetic assistant streams a personalized retrieval answer through an edge cache whose key omits identity and corpus version.",
            "observations": [("cross_user_responses", 3, "responses"), ("stale_citations", 18, "citations"), ("cache_hit_pct", 91, "percent"), ("ttft_ms", 240, "ms")],
            "invariants": ["private responses never cross an identity boundary", "every cited passage matches the authorized current corpus version"],
            "root": "The cache key and policy omit authorization and corpus identity, so a performance optimization violates privacy and freshness.",
            "explanation": "Browser/edge caching, inference latency, and retrieval provenance share one response contract. A high hit rate and low TTFT are not success when authority is wrong.",
            "repair": "Mark private responses non-shared, key safe caches by complete public identity, and revalidate source version and authorization before generation.",
            "constraints": [("cross_user_responses", "==", 0), ("stale_citations", "==", 0), ("ttft_ms", "<=", 500)],
        },
        {
            "title": "Long prompts starve interactive inference and stale retrieval wins",
            "workload": "A synthetic serving queue mixes long batch prompts with interactive retrieval requests while the index update stream is delayed.",
            "observations": [("interactive_ttft_ms", 6200, "ms"), ("index_lag_seconds", 900, "s"), ("unsupported_claims", 11, "claims"), ("batch_share_pct", 88, "percent")],
            "invariants": ["interactive traffic retains its latency allocation", "answers abstain when current authorized evidence is unavailable"],
            "root": "Unfair token-based work admission lets long batches monopolize service while generation proceeds despite stale evidence.",
            "explanation": "Request count is not equivalent work for inference, and retrieval availability is not grounding. The system needs token-aware fairness and a deterministic abstention boundary.",
            "repair": "Reserve interactive token capacity, bound batch quanta, gate on source freshness, and abstain when evidence cannot satisfy the contract.",
            "constraints": [("interactive_ttft_ms", "<=", 900), ("index_lag_seconds", "<=", 60), ("unsupported_claims", "==", 0)],
        },
        {
            "title": "A replayed agent step repeats an authorized purchase",
            "workload": "A synthetic browser retries after losing a response while a durable agent workflow repeats a previously approved side effect.",
            "observations": [("tool_attempts", 2, "attempts"), ("completed_purchases", 2, "purchases"), ("approval_records", 1, "approvals"), ("audit_events", 1, "events")],
            "invariants": ["one approval authorizes at most one bounded side effect", "workflow replay returns the original result without repeating the effect"],
            "root": "The workflow checkpoints intent but not an idempotent effect result, and the tool does not bind approval to a unique operation key.",
            "explanation": "Browser retries, agent durability, and tool authorization meet at the side-effect boundary. Model output and a prior approval cannot substitute for atomic deduplication.",
            "repair": "Bind approval and scoped credentials to one operation key, persist the effect result atomically, and return it on replay.",
            "constraints": [("tool_attempts", "==", 1), ("completed_purchases", "==", 1), ("audit_events", ">=", 2)],
        },
    ],
}


def _git(*args: str, text: bool = False) -> bytes | str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if result.returncode:
        raise GateError("Git could not verify the requested commit or artifact")
    return result.stdout.decode("utf-8").strip() if text else result.stdout


def _repo_file(path: Path) -> tuple[Path, str, bytes]:
    try:
        resolved = path.resolve(strict=True)
        relative = resolved.relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        raise GateError("artifact must be an existing file inside this Git repository") from None
    data = resolved.read_bytes()
    if not data:
        raise GateError("artifact must be non-empty")
    return resolved, relative, data


def _write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise GateError(f"output already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def prepare(gate: str, output: Path, seed: int | None = None) -> dict[str, Any]:
    gate = gate.upper()
    if gate not in VARIANTS:
        raise GateError(f"unknown gate: {gate}")
    if seed is not None and seed < 0:
        raise GateError("seed must be non-negative")
    actual_seed = seed if seed is not None else random.SystemRandom().randrange(0, 2**63)
    variant_index = random.Random(f"{gate}:{actual_seed}").randrange(3)
    definition = VARIANTS[gate][variant_index]
    variant_id = f"{gate}-V{variant_index + 1:02d}"
    workload = {"description": definition["workload"], "sha256": digest_bytes(definition["workload"].encode("utf-8"))}
    challenge_id = f"{gate}-{digest_bytes(f'{gate}:{actual_seed}:{variant_id}'.encode())[:16]}"
    core = {
        "schema_version": "1.0",
        "gate": gate,
        "challenge_id": challenge_id,
        "variant_id": variant_id,
        "seed": actual_seed,
        "title": definition["title"],
        "module_ids": GATE_MODULES[gate],
        "synthetic": True,
        "assurance_limitation": ASSURANCE_LIMITATION,
        "workload": workload,
        "observations": [dict(zip(("metric", "value", "unit"), row)) for row in definition["observations"]],
        "target_invariants": definition["invariants"],
        "diagnosis_instructions": [
            "Explain the causal chain from the observations to the first failed invariant.",
            "Commit this challenge and your diagnosis before running reveal.",
            "Do not use live AI assistance before the diagnosis and answers are frozen.",
            "After reveal, preserve new repaired evidence under the identical workload hash.",
        ],
    }
    reveal_payload = {
        "root_cause": definition["root"],
        "causal_explanation": definition["explanation"],
        "repair": definition["repair"],
        "acceptance_constraints": [dict(zip(("metric", "operator", "value"), row)) for row in definition["constraints"]],
        "workload_sha256": workload["sha256"],
    }
    raw_payload = canonical_bytes(reveal_payload)
    envelope = {
        "schema_version": "1.0",
        "gate": gate,
        "challenge_id": challenge_id,
        "challenge_core_sha256": digest_json(core),
        "encoding": "base64+zlib",
        "payload": base64.b64encode(zlib.compress(raw_payload, level=9)).decode("ascii"),
        "payload_sha256": digest_bytes(raw_payload),
        "assurance_limitation": ASSURANCE_LIMITATION,
    }
    envelope_bytes = json.dumps(envelope, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    challenge = {**core, "envelope_sha256": digest_bytes(envelope_bytes)}
    challenge_bytes = json.dumps(challenge, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    envelope_path = ROOT / ".course-private" / "gates" / gate / f"{challenge_id}.sgate"
    _write_new(output, challenge_bytes)
    try:
        _write_new(envelope_path, envelope_bytes)
    except Exception:
        output.unlink(missing_ok=True)
        raise
    return challenge


def reveal(challenge_path: Path, diagnosis_path: Path, commit: str, output: Path) -> dict[str, Any]:
    _, challenge_relative, challenge_bytes = _repo_file(challenge_path)
    _, diagnosis_relative, diagnosis_bytes = _repo_file(diagnosis_path)
    challenge = json.loads(challenge_bytes)
    if challenge.get("gate") not in VARIANTS or not challenge.get("challenge_id"):
        raise GateError("challenge contract is invalid")
    resolved_commit = str(_git("rev-parse", "--verify", f"{commit}^{{commit}}", text=True))
    if _git("show", f"{resolved_commit}:{challenge_relative}") != challenge_bytes:
        raise GateError("challenge bytes do not match the supplied commit")
    if _git("show", f"{resolved_commit}:{diagnosis_relative}") != diagnosis_bytes:
        raise GateError("diagnosis bytes do not match the supplied commit")
    envelope_path = ROOT / ".course-private" / "gates" / challenge["gate"] / f"{challenge['challenge_id']}.sgate"
    if not envelope_path.is_file():
        raise GateError("matching local reveal envelope is missing")
    envelope_bytes = envelope_path.read_bytes()
    if digest_bytes(envelope_bytes) != challenge.get("envelope_sha256"):
        raise GateError("local reveal envelope hash does not match the challenge")
    envelope = json.loads(envelope_bytes)
    core = {key: value for key, value in challenge.items() if key != "envelope_sha256"}
    if envelope.get("challenge_core_sha256") != digest_json(core):
        raise GateError("challenge content was altered after preparation")
    try:
        raw_payload = zlib.decompress(base64.b64decode(envelope["payload"], validate=True))
    except (KeyError, ValueError, zlib.error) as error:
        raise GateError("local reveal envelope cannot be decoded") from error
    if digest_bytes(raw_payload) != envelope.get("payload_sha256"):
        raise GateError("local reveal payload hash mismatch")
    payload = json.loads(raw_payload)
    result = {
        "schema_version": "1.0",
        "gate": challenge["gate"],
        "challenge_id": challenge["challenge_id"],
        "challenge_sha256": digest_bytes(challenge_bytes),
        "workload_sha256": payload["workload_sha256"],
        "frozen_diagnosis": {
            "repository_relative_path": diagnosis_relative,
            "sha256": digest_bytes(diagnosis_bytes),
            "commit": resolved_commit,
        },
        "root_cause": payload["root_cause"],
        "causal_explanation": payload["causal_explanation"],
        "repair": payload["repair"],
        "acceptance_constraints": payload["acceptance_constraints"],
        "disclosure": ASSURANCE_LIMITATION,
    }
    _write_new(output, json.dumps(result, indent=2, sort_keys=True).encode("utf-8") + b"\n")
    return result


def _compare(actual: float, operator: str, expected: float) -> bool:
    return {"<=": actual <= expected, ">=": actual >= expected, "==": actual == expected}[operator]


def check(challenge_path: Path, reveal_path: Path, repair_path: Path, output: Path) -> dict[str, Any]:
    _, _, challenge_bytes = _repo_file(challenge_path)
    _, _, reveal_bytes = _repo_file(reveal_path)
    _, _, repair_bytes = _repo_file(repair_path)
    challenge = json.loads(challenge_bytes)
    revealed = json.loads(reveal_bytes)
    repair = json.loads(repair_bytes)
    expected_challenge_hash = digest_bytes(challenge_bytes)
    envelope_path = ROOT / ".course-private" / "gates" / str(challenge.get("gate")) / f"{challenge.get('challenge_id')}.sgate"
    if not envelope_path.is_file():
        raise GateError("matching local reveal envelope is missing")
    envelope_bytes = envelope_path.read_bytes()
    if digest_bytes(envelope_bytes) != challenge.get("envelope_sha256"):
        raise GateError("local reveal envelope hash does not match the challenge")
    envelope = json.loads(envelope_bytes)
    core = {key: value for key, value in challenge.items() if key != "envelope_sha256"}
    if envelope.get("challenge_core_sha256") != digest_json(core):
        raise GateError("challenge content was altered after preparation")
    try:
        sealed_bytes = zlib.decompress(base64.b64decode(envelope["payload"], validate=True))
    except (KeyError, ValueError, zlib.error) as error:
        raise GateError("local reveal envelope cannot be decoded") from error
    if digest_bytes(sealed_bytes) != envelope.get("payload_sha256"):
        raise GateError("local reveal payload hash mismatch")
    sealed = json.loads(sealed_bytes)
    for key in ("root_cause", "causal_explanation", "repair", "acceptance_constraints", "workload_sha256"):
        if revealed.get(key) != sealed.get(key):
            raise GateError(f"reveal {key} does not match the sealed challenge")
    for name, value in (("reveal", revealed), ("repair", repair)):
        if value.get("gate") != challenge.get("gate") or value.get("challenge_id") != challenge.get("challenge_id"):
            raise GateError(f"{name} belongs to a different gate challenge")
        if value.get("challenge_sha256") != expected_challenge_hash:
            raise GateError(f"{name} challenge hash mismatch")
        if value.get("workload_sha256") != challenge.get("workload", {}).get("sha256"):
            raise GateError(f"{name} workload hash mismatch")
    measurements = repair.get("measurements")
    evidence_paths = repair.get("evidence_paths")
    if not isinstance(measurements, dict) or not isinstance(evidence_paths, list) or not evidence_paths:
        raise GateError("repair evidence is incomplete")
    evidence_hashes: dict[str, str] = {}
    for raw_path in evidence_paths:
        _, relative, data = _repo_file(ROOT / str(raw_path))
        evidence_hashes[relative] = digest_bytes(data)
    findings = []
    for constraint in revealed.get("acceptance_constraints", []):
        metric = constraint["metric"]
        actual = measurements.get(metric)
        passed = isinstance(actual, (int, float)) and _compare(float(actual), constraint["operator"], float(constraint["value"]))
        findings.append({**constraint, "actual": actual, "passed": passed})
    if not findings:
        raise GateError("reveal contains no acceptance constraints")
    result = {
        "schema_version": "1.0",
        "gate": challenge["gate"],
        "challenge_id": challenge["challenge_id"],
        "challenge_sha256": expected_challenge_hash,
        "workload_sha256": challenge["workload"]["sha256"],
        "passed": all(row["passed"] for row in findings),
        "findings": findings,
        "evidence_sha256": evidence_hashes,
    }
    _write_new(output, json.dumps(result, indent=2, sort_keys=True).encode("utf-8") + b"\n")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare_parser = subparsers.add_parser("prepare")
    prepare_parser.add_argument("--gate", required=True)
    prepare_parser.add_argument("--output", required=True, type=Path)
    prepare_parser.add_argument("--seed", type=int)
    reveal_parser = subparsers.add_parser("reveal")
    reveal_parser.add_argument("--challenge", required=True, type=Path)
    reveal_parser.add_argument("--diagnosis", required=True, type=Path)
    reveal_parser.add_argument("--commit", required=True)
    reveal_parser.add_argument("--output", required=True, type=Path)
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("--challenge", required=True, type=Path)
    check_parser.add_argument("--reveal", required=True, type=Path)
    check_parser.add_argument("--repair", required=True, type=Path)
    check_parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "prepare":
            result = prepare(args.gate, args.output, args.seed)
            print(f"prepared {result['challenge_id']} at {args.output}")
        elif args.command == "reveal":
            result = reveal(args.challenge, args.diagnosis, args.commit, args.output)
            print(f"revealed {result['challenge_id']} at {args.output}")
        else:
            result = check(args.challenge, args.reveal, args.repair, args.output)
            print(f"checked {result['challenge_id']}: {'Pass' if result['passed'] else 'Revise'}")
    except (GateError, OSError, json.JSONDecodeError) as error:
        print(f"solo gate failed: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
