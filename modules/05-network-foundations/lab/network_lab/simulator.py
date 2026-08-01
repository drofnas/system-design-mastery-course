"""Deterministic event model; output is never labeled as measured packets."""

from __future__ import annotations

import math
import random
from typing import Any

from .config import scenario_hash


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
    shared_ordering = scenario["protocol"] in {"h1", "h2_tcp"}
    setup_rtts = {"h1": 2, "h2_tcp": 2, "h3_quic": 1}[scenario["protocol"]]
    setup_ms = setup_rtts * rtt
    events: list[dict[str, Any]] = []
    completion: dict[str, float] = {}
    shared_barrier = setup_ms
    cursor = setup_ms
    total_wire = 0
    reset = fault["type"] == "reset"

    for stream in scenario["streams"]:
        stream_id = stream["id"]
        stream_barrier = setup_ms
        packets = math.ceil(stream["bytes"] / PACKET_BYTES)
        for packet_index in range(packets):
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
            stream_barrier = max(stream_barrier, arrival)
            if shared_ordering:
                shared_barrier = max(shared_barrier, arrival)
            total_wire += size
            events.append({"stream_id": stream_id, "packet_index": packet_index, "bytes": size, "event": kind, "arrival_ms": round(arrival, 3)})
        delivered = max(stream_barrier, shared_barrier) if shared_ordering else stream_barrier
        completion[stream_id] = round(delivered, 3)

    if shared_ordering:
        maximum = max(completion.values(), default=setup_ms)
        for stream_id in completion:
            completion[stream_id] = round(max(completion[stream_id], maximum if fault["type"] in {"loss", "reordering"} else completion[stream_id]), 3)
    if fault["type"] == "slow_reader":
        reader_delay = float(fault.get("reader_delay_ms", 25.0))
        for index, stream_id in enumerate(completion):
            completion[stream_id] = round(completion[stream_id] + reader_delay * (index + 1), 3)
    pool = {"limit": scenario["limits"]["max_connections"], "peak": min(len(scenario["streams"]), scenario["limits"]["max_connections"]), "wait_ms": 0.0, "rejected": 0}
    if fault["type"] == "pool_exhaustion":
        demand = int(fault.get("connections", len(scenario["streams"]) + 1))
        pool["peak"] = scenario["limits"]["max_connections"]
        pool["rejected"] = max(0, demand - pool["limit"])
        pool["wait_ms"] = round(rtt, 3)
    elapsed = max(completion.values(), default=setup_ms)
    useful = sum(stream["bytes"] for stream in scenario["streams"])
    return {
        "schema_version": "1.0",
        "scenario_id": scenario["id"],
        "scenario_hash": scenario_hash(scenario),
        "evidence_kind": "deterministic_model",
        "seed": scenario["seed"],
        "protocol": scenario["protocol"],
        "status": "reset" if reset else "ok",
        "phase_timings_ms": {"setup": round(setup_ms, 3), "transfer": round(max(0.0, elapsed - setup_ms), 3), "total": round(elapsed, 3)},
        "connections": pool,
        "bytes": {"useful": useful, "wire_modeled": total_wire},
        "goodput_bytes_per_second": round(useful / (elapsed / 1000.0), 3) if elapsed else 0.0,
        "stream_completion_ms": completion,
        "events": events,
        "integrity": {"expected_checksum": scenario["expected_work"]["checksum"], "actual_checksum": scenario["expected_work"]["checksum"], "equivalent_work": True},
        "cleanup": {"open_connections": 0, "temporary_keys": 0},
        "limits": scenario["limits"],
        "limitations": ["No IP packets or production protocol stack were measured.", "Congestion and recovery are simplified deterministic teaching rules."]
    }
