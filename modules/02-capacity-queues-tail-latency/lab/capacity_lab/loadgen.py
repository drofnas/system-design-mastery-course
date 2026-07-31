"""Open- and closed-loop load generation with bounded retries."""

from __future__ import annotations

import asyncio
import json
import math
import random
import time
from dataclasses import dataclass
from typing import Any

from .service import CapacityService


@dataclass
class RetryBudget:
    limit: int
    used: int = 0

    def claim(self) -> bool:
        if self.used >= self.limit:
            return False
        self.used += 1
        return True


async def _send(host: str, port: int, request: dict[str, Any]) -> dict[str, Any]:
    sent_at = time.monotonic()
    try:
        reader, writer = await asyncio.open_connection(host, port)
        writer.write((json.dumps(request, sort_keys=True) + "\n").encode("utf-8"))
        await writer.drain()
        response = json.loads(await asyncio.wait_for(reader.readline(), timeout=65))
        writer.close()
        await writer.wait_closed()
    except (OSError, asyncio.TimeoutError, json.JSONDecodeError) as error:
        response = {
            "request_id": request["request_id"],
            "attempt": request["attempt"],
            "outcome": "transport_failure",
            "accepted": False,
            "admitted_at": None,
            "service_started_at": None,
            "completed_at": time.monotonic(),
            "queue_wait_ms": 0.0,
            "service_ms": 0.0,
            "queue_depth_at_admission": 0,
            "failure_reason": str(error),
            "max_service_concurrency": 0,
            "max_downstream_concurrency": 0,
        }
    response["scheduled_at"] = request["scheduled_at"]
    response["sent_at"] = sent_at
    response["generator_lag_ms"] = round(max(0.0, sent_at - request["scheduled_at"]) * 1000, 6)
    response["end_to_end_ms"] = round(
        max(0.0, response["completed_at"] - request["scheduled_at"]) * 1000,
        6,
    )
    return response


async def _logical_request(
    host: str,
    port: int,
    scenario: dict[str, Any],
    request_id: str,
    scheduled_at: float,
    budget: RetryBudget,
) -> list[dict[str, Any]]:
    retry = scenario["retry"]
    max_attempts = int(retry["max_attempts"])
    events: list[dict[str, Any]] = []
    for attempt in range(1, max_attempts + 1):
        event = await _send(
            host,
            port,
            {
                "request_id": request_id,
                "attempt": attempt,
                "scheduled_at": scheduled_at,
            },
        )
        events.append(event)
        if event["outcome"] == "success":
            break
        if attempt >= max_attempts or not budget.claim():
            break
        base_ms = float(retry["base_backoff_ms"])
        jitter = random.Random(f"{scenario['seed']}:{request_id}:{attempt}").random()
        await asyncio.sleep((base_ms * (2 ** (attempt - 1)) * jitter) / 1000)
    return events


def _open_schedule(scenario: dict[str, Any], started: float) -> list[float]:
    arrival = scenario["arrival"]
    rate = float(arrival["rate_per_second"])
    duration = float(arrival["duration_seconds"])
    interval = 1 / rate
    burst_multiplier = float(arrival.get("burst_multiplier", 1))
    burst_start = float(arrival.get("burst_start_seconds", 0))
    burst_end = burst_start + float(arrival.get("burst_duration_seconds", 0))

    offsets: list[float] = []
    offset = 0.0
    # The epsilon prevents binary floating-point drift from scheduling an extra
    # arrival exactly at the duration boundary (for example 20/s for 0.4 s).
    while offset < duration - 1e-12:
        offsets.append(offset)
        in_burst = burst_start <= offset < burst_end
        effective_interval = interval / burst_multiplier if in_burst else interval
        next_offset = offset + effective_interval
        has_burst = burst_multiplier > 1 and burst_end > burst_start
        if has_burst and offset < burst_start < next_offset:
            next_offset = burst_start
        elif has_burst and in_burst and next_offset > burst_end:
            next_offset = burst_end
        offset = next_offset
    return [started + offset for offset in offsets]


async def _run_open(
    host: str,
    port: int,
    scenario: dict[str, Any],
    budget: RetryBudget,
) -> list[dict[str, Any]]:
    started = time.monotonic() + 0.02
    schedule = _open_schedule(scenario, started)

    async def launch(index: int, scheduled_at: float) -> list[dict[str, Any]]:
        await asyncio.sleep(max(0.0, scheduled_at - time.monotonic()))
        return await _logical_request(
            host,
            port,
            scenario,
            f"request-{index:06d}",
            scheduled_at,
            budget,
        )

    groups = await asyncio.gather(
        *(launch(index, scheduled_at) for index, scheduled_at in enumerate(schedule))
    )
    return [event for group in groups for event in group]


async def _run_closed(
    host: str,
    port: int,
    scenario: dict[str, Any],
    budget: RetryBudget,
) -> list[dict[str, Any]]:
    arrival = scenario["arrival"]
    duration = float(arrival["duration_seconds"])
    concurrency = int(arrival.get("max_in_flight", scenario["service"]["workers"]))
    stop_at = time.monotonic() + duration
    counter = 0
    counter_lock = asyncio.Lock()

    async def participant() -> list[dict[str, Any]]:
        nonlocal counter
        participant_events: list[dict[str, Any]] = []
        while time.monotonic() < stop_at:
            async with counter_lock:
                index = counter
                counter += 1
            scheduled_at = time.monotonic()
            participant_events.extend(
                await _logical_request(
                    host,
                    port,
                    scenario,
                    f"request-{index:06d}",
                    scheduled_at,
                    budget,
                )
            )
        return participant_events

    groups = await asyncio.gather(*(participant() for _ in range(concurrency)))
    return [event for group in groups for event in group]


def retry_budget_limit(scenario: dict[str, Any]) -> int:
    """Return the shared retry allowance fixed before a trial begins."""
    arrival = scenario["arrival"]
    if arrival["mode"] == "open":
        planned_requests = len(_open_schedule(scenario, 0.0))
    else:
        planned_requests = max(
            1,
            math.ceil(
                float(arrival["rate_per_second"])
                * float(arrival["duration_seconds"])
            ),
        )
    return math.floor(
        planned_requests * float(scenario["retry"]["budget_ratio"])
    )


async def run_trial(
    scenario: dict[str, Any],
    *,
    connect: tuple[str, int] | None = None,
) -> tuple[list[dict[str, Any]], RetryBudget]:
    """Run one scenario, starting an embedded loopback service by default."""
    arrival = scenario["arrival"]
    budget = RetryBudget(limit=retry_budget_limit(scenario))
    embedded: CapacityService | None = None
    if connect is None:
        embedded = CapacityService(scenario)
        host, port = await embedded.start()
    else:
        host, port = connect
        if host not in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("capacity lab load generator connects to loopback only")

    try:
        if arrival["mode"] == "open":
            events = await _run_open(host, port, scenario, budget)
        else:
            events = await _run_closed(host, port, scenario, budget)
        return events, budget
    finally:
        if embedded is not None:
            await embedded.close()
