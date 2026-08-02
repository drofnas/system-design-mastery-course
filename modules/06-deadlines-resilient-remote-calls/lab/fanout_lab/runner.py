from __future__ import annotations

import asyncio
import hashlib
import json
import platform
from collections import Counter
from typing import Any

from .service import FanoutService


def input_fingerprint(scenario: dict[str, Any]) -> str:
    shared_input = {
        "pair_id": scenario["pair_id"],
        "seed": scenario["seed"],
        "workload": scenario["workload"],
        "dependencies": scenario["dependencies"],
        "fault": scenario["fault"],
    }
    encoded = json.dumps(shared_input, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


async def _start_requests(service: FanoutService) -> list[asyncio.Task[str]]:
    workload = service.workload
    fault = service.fault
    count = (
        fault["duplicate_requests"]
        if fault["kind"] == "duplicate_request"
        else workload["logical_requests"]
    )
    tasks: list[asyncio.Task[str]] = []
    for index in range(count):
        tenant = workload["tenants"][index % len(workload["tenants"])]
        request_id = f"req-{index + 1:03d}"
        fingerprint = (
            "reserve-conflict-v2"
            if fault["conflicting_duplicate"] and index == count - 1
            else "reserve-v1"
        )
        tasks.append(
            asyncio.create_task(
                service.handle_request(
                    request_id,
                    tenant,
                    key="beacon-reservation-001" if workload["operation"] == "reserve" else None,
                    fingerprint=fingerprint,
                ),
                name=request_id,
            )
        )
        if workload["arrival_interval_ms"]:
            await asyncio.sleep(
                workload["arrival_interval_ms"] * workload["time_scale"] / 1000
            )
    return tasks


async def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    service = FanoutService(scenario)
    service.begin()
    tasks = await _start_requests(service)

    health_task: asyncio.Task[bool] | None = None
    if scenario["fault"]["kind"] == "pool_exhaustion":
        await asyncio.sleep(0)
        health_task = asyncio.create_task(service.health_check(), name="health-check")

    cancel_after = scenario["fault"]["cancel_after_ms"]
    if cancel_after is not None:
        await asyncio.sleep(cancel_after * scenario["workload"]["time_scale"] / 1000)
        for task in tasks:
            task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)
    if health_task is not None:
        await health_task
    elif scenario["fault"]["kind"] != "pool_exhaustion":
        await service.health_check()

    attempt_counts = Counter(item["dependency"] for item in service.attempts)
    initial = sum(item["attempt"] == 1 for item in service.attempts)
    retries = len(service.attempts) - initial
    useful = service.outcomes["complete"] + service.outcomes["degraded"]
    pending = [
        task
        for task in asyncio.all_tasks()
        if task is not asyncio.current_task() and not task.done()
    ]
    cleanup = {
        "active_after": service.gate.active_global,
        "queued_after": service.gate.queued,
        "pending_tasks_after": len(pending),
    }
    dependency_bounds = all(
        service.gate.dependency_peak[name] <= limit
        for name, limit in service.policy["per_dependency_limit"].items()
    )
    tenant_bounds = all(
        peak <= service.policy["per_tenant_limit"]
        for tenant, peak in service.gate.tenant_peak.items()
        if tenant != "__health__"
    )
    retry_respected = (
        retries <= service.policy["retry_budget"]
        if service.policy["retry_owner"] == "caller"
        else False
    )
    trial = {
        "schema_version": "1.0",
        "scenario_id": scenario["id"],
        "pair_id": scenario["pair_id"],
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "evidence_kind": "measured-asyncio-scaled",
        "runtime": {
            "implementation": "stdlib-asyncio-fanout-service",
            "python": platform.python_version(),
            "time_scale": scenario["workload"]["time_scale"],
            "network": "offline-synthetic-dependencies",
        },
        "input_fingerprint": input_fingerprint(scenario),
        "logical_request_ids": sorted(service.logical_request_ids),
        "outcomes": {
            "complete": service.outcomes["complete"],
            "degraded": service.outcomes["degraded"],
            "unavailable": service.outcomes["unavailable"],
            "cancelled": service.outcomes["cancelled"],
            "rejected": service.outcomes["rejected"],
        },
        "attempts": {
            "initial": initial,
            "retries": retries,
            "total": len(service.attempts),
            "per_dependency": dict(sorted(attempt_counts.items())),
            "start_logical_ms": [item["start_logical_ms"] for item in service.attempts],
            "backoff_logical_ms": service.backoffs,
            "useful_work_ratio": round(
                min(1.0, useful / max(len(service.attempts), 1)), 4
            ),
        },
        "concurrency": {
            "global_peak": service.gate.global_peak,
            "per_dependency_peak": dict(sorted(service.gate.dependency_peak.items())),
            "per_tenant_peak": dict(sorted(service.gate.tenant_peak.items())),
            "queue_peak": service.gate.queue_peak,
            "rejections": service.gate.rejections,
            "global_limit": service.policy["global_limit"],
            "per_dependency_limit": service.policy["per_dependency_limit"],
            "per_tenant_limit": service.policy["per_tenant_limit"],
            "queue_limit": service.policy["queue_limit"],
        },
        "deadlines": {
            "expired": service.deadline_expired,
            "insufficient_budget": service.insufficient_budget,
            "late_work": service.late_work,
            "remaining_at_dispatch_ms": service.remaining_at_dispatch,
        },
        "cancellation": {
            "signals": service.cancellation_signals,
            "cancelled_children": service.cancelled_children,
            "leaked_children": service.leaked_children,
            "drain_ms": max(service.cancellation_drains, default=0.0),
        },
        "effects": {
            "count": service.effect_count,
            "dedup_replays": service.dedup_replays,
            "conflicts": service.dedup_conflicts,
        },
        "completeness": {
            "false_complete": service.false_complete,
            "degraded": service.degraded,
            "unavailable": service.unavailable,
        },
        "health": {
            "checks": service.health_checks,
            "rejected": service.health_rejected,
            "isolated": service.policy["health_isolated"],
        },
        "cleanup": cleanup,
        "policy_checks": {
            "deadline_propagated": service.policy["propagate_deadline"],
            "retry_budget_respected": retry_respected,
            "global_bound_respected": service.gate.global_peak <= service.policy["global_limit"],
            "dependency_bounds_respected": dependency_bounds,
            "tenant_bounds_respected": tenant_bounds,
            "cancellation_drained": service.leaked_children == 0,
            "single_effect": service.effect_count <= 1,
            "partial_state_truthful": service.false_complete == 0,
            "health_isolated": service.policy["health_isolated"],
            "cleanup_complete": all(value == 0 for value in cleanup.values()),
        },
    }
    return trial
