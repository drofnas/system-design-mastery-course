"""Deterministic event model; output is never labeled as measured packets."""

from __future__ import annotations

import math
import random
from typing import Any

from .config import scenario_hash, sha256_bytes


PACKET_BYTES = 1200


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    index = min(len(ordered) - 1, math.ceil(len(ordered) * fraction) - 1)
    return ordered[index]


def simulate(scenario: dict[str, Any]) -> dict[str, Any]:
    rng = random.Random(scenario["seed"])
    path = scenario["path"]
    fault = scenario["fault"]
    rtt = float(path["rtt_ms"])
    bandwidth_bytes_ms = float(path["bandwidth_kbps"]) / 8.0
    if fault["type"] == "bandwidth":
        bandwidth_bytes_ms = float(fault.get("bandwidth_kbps", path["bandwidth_kbps"])) / 8.0
    base_one_way = rtt / 2.0 + float(fault.get("delay_ms", 0.0))
    jitter_ms = float(fault.get("jitter_ms", 0.0)) if fault["type"] == "jitter" else 0.0
    recovery_ms = float(fault.get("recovery_ms", rtt))
    target_stream = str(fault.get("stream_id", scenario["streams"][0]["id"]))
    target_packet = int(fault.get("packet_index", 0))
    shared_ordering = scenario["protocol"] == "h2_tcp"
    # Hold setup constant: this experiment isolates recovery ordering, not handshake cost.
    setup_ms = 2 * rtt
    events: list[dict[str, Any]] = []
    completion: dict[str, float] = {}
    shared_recovery_until = setup_ms
    stream_recovery_until = {stream["id"]: setup_ms for stream in scenario["streams"]}
    cursor = setup_ms
    total_wire = 0
    packet_counts = {
        stream["id"]: math.ceil(stream["bytes"] / PACKET_BYTES)
        for stream in scenario["streams"]
    }

    # Round-robin serialization gives both protocol variants the same packet schedule.
    send_order = 0
    for packet_index in range(max(packet_counts.values())):
        for stream in scenario["streams"]:
            stream_id = stream["id"]
            if packet_index >= packet_counts[stream_id]:
                continue
            size = min(PACKET_BYTES, stream["bytes"] - packet_index * PACKET_BYTES)
            cursor += size / bandwidth_bytes_ms
            arrival = cursor + base_one_way
            if jitter_ms:
                arrival += rng.uniform(-jitter_ms, jitter_ms)
            kind = "delivered"
            if fault["type"] == "loss" and stream_id == target_stream and packet_index == target_packet:
                arrival += recovery_ms
                kind = "lost_then_recovered"
            if fault["type"] == "reordering" and stream_id == target_stream and packet_index == target_packet:
                arrival += float(fault.get("reorder_ms", rtt / 2.0))
                kind = "reordered"
            if kind != "delivered":
                if shared_ordering:
                    shared_recovery_until = max(shared_recovery_until, arrival)
                else:
                    stream_recovery_until[stream_id] = max(stream_recovery_until[stream_id], arrival)
            delivery = max(
                arrival,
                shared_recovery_until if shared_ordering else stream_recovery_until[stream_id],
            )
            completion[stream_id] = max(completion.get(stream_id, setup_ms), delivery)
            total_wire += size
            events.append({
                "stream_id": stream_id,
                "packet_index": packet_index,
                "send_order": send_order,
                "bytes": size,
                "event": kind,
                "arrival_ms": round(arrival, 3),
                "delivery_ms": round(delivery, 3),
            })
            send_order += 1
    completion = {stream_id: round(value, 3) for stream_id, value in completion.items()}
    pool = {"limit": scenario["limits"]["max_connections"], "peak": min(len(scenario["streams"]), scenario["limits"]["max_connections"]), "wait_ms": 0.0, "rejected": 0}
    if fault["type"] == "pool_exhaustion":
        demand = int(fault.get("connections", len(scenario["streams"]) + 1))
        pool["peak"] = scenario["limits"]["max_connections"]
        pool["rejected"] = max(0, demand - pool["limit"])
        pool["wait_ms"] = round(rtt, 3)
    elapsed = max(completion.values(), default=setup_ms)
    useful = sum(stream["bytes"] for stream in scenario["streams"])
    actual_checksum = sha256_bytes(b"T" * useful)
    equivalent_work = actual_checksum == scenario["expected_work"]["checksum"]
    return {
        "schema_version": "1.0",
        "scenario_id": scenario["id"],
        "scenario_hash": scenario_hash(scenario),
        "evidence_kind": "deterministic_model",
        "seed": scenario["seed"],
        "protocol": scenario["protocol"],
        "status": "ok",
        "phase_timings_ms": {"setup": round(setup_ms, 3), "transfer": round(max(0.0, elapsed - setup_ms), 3), "total": round(elapsed, 3)},
        "connections": dict(pool, created=pool["peak"], reused_requests=0),
        "attempts": [{"number": 1, "connection": 1, "reused": False, "duration_ms": round(elapsed, 3), "bytes": useful, "checksum": actual_checksum}],
        "bytes": {"useful": useful, "wire_modeled": total_wire},
        "goodput_bytes_per_second": round(useful / (elapsed / 1000.0), 3) if elapsed else 0.0,
        "stream_completion_ms": completion,
        "events": events,
        "integrity": {"expected_checksum": scenario["expected_work"]["checksum"], "actual_checksum": actual_checksum, "equivalent_work": equivalent_work},
        "cleanup": {"open_connections": 0, "temporary_keys": 0, "unresolved_tasks": 0},
        "limits": scenario["limits"],
        "limitations": ["No IP packets or production protocol stack were measured.", "Congestion and recovery are simplified deterministic teaching rules."]
    }
