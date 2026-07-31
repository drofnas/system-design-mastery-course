"""Instrumented version of the Module 2 bounded saturation service."""

from __future__ import annotations

import asyncio
import hashlib
import json
import random
import sqlite3
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .telemetry import Recorder, SpanToken, make_traceparent, parse_traceparent


@dataclass
class WorkItem:
    request: dict[str, Any]
    admitted_at: float
    queue_depth: int
    server_span: SpanToken
    result: asyncio.Future[dict[str, Any]]


class ObservabilityService:
    """Fixed workers, bounded queue, fan-out, and bounded fault injection."""

    def __init__(self, scenario: dict[str, Any], recorder: Recorder) -> None:
        self.scenario = scenario
        self.recorder = recorder
        service = scenario["service"]
        self.queue: asyncio.Queue[WorkItem] = asyncio.Queue(
            maxsize=int(service["queue_capacity"])
        )
        self.worker_count = int(service["workers"])
        self._workers: list[asyncio.Task[None]] = []
        self._server: asyncio.Server | None = None
        self._service_in_use = 0
        self._service_peak = 0
        self._downstream_in_use = 0
        self._downstream_peak = 0
        self._downstream_lock = asyncio.Lock()
        self._fault_lock = asyncio.Lock()
        self._retained_connections: list[asyncio.StreamWriter] = []
        self._retained_allocations: list[bytearray] = []
        self._connection_peak = 0
        self._connection_active = 0
        self._tempdir = tempfile.TemporaryDirectory(prefix="module04-observability-")
        self._io_path = Path(self._tempdir.name) / "dependency.bin"
        self._database = sqlite3.connect(":memory:")
        self._query_plan: list[str] = []
        self._setup_database()

    @property
    def query_plan(self) -> list[str]:
        return list(self._query_plan)

    @property
    def connection_peak(self) -> int:
        return self._connection_peak

    @property
    def retained_connection_count(self) -> int:
        return len(self._retained_connections)

    async def start(self, host: str = "127.0.0.1", port: int = 0) -> tuple[str, int]:
        if host not in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("observability lab serves loopback addresses only")
        self._workers = [
            asyncio.create_task(self._worker(index), name=f"observability-worker-{index}")
            for index in range(self.worker_count)
        ]
        self._server = await asyncio.start_server(self._handle_connection, host, port)
        socket = self._server.sockets[0]
        bound_host, bound_port = socket.getsockname()[:2]
        return str(bound_host), int(bound_port)

    async def close(self) -> None:
        if self._server is not None:
            self._server.close()
        for writer in self._retained_connections:
            writer.close()
        await asyncio.gather(
            *(writer.wait_closed() for writer in self._retained_connections),
            return_exceptions=True,
        )
        if self._server is not None:
            await self._server.wait_closed()
        await self.queue.join()
        self._retained_connections.clear()
        self._connection_active = 0
        self.recorder.metric(
            "service.active_connections",
            0,
            unit="{connection}",
            attributes={"state": "after_cleanup"},
        )
        for worker in self._workers:
            worker.cancel()
        await asyncio.gather(*self._workers, return_exceptions=True)
        self._workers.clear()
        self._database.close()
        self._retained_allocations.clear()
        self._tempdir.cleanup()

    def _setup_database(self) -> None:
        database = self.scenario["database"]
        self._database.execute(
            "create table impacts(route_id integer, approved_at integer, detail text)"
        )
        rows = int(database["rows"])
        self._database.executemany(
            "insert into impacts values (?, ?, ?)",
            ((index % 64, index, f"impact-{index}") for index in range(rows)),
        )
        indexed = bool(database["indexed"]) and self.scenario["fault"]["kind"] != "query_scan"
        if indexed:
            self._database.execute(
                "create index impact_route_approved on impacts(route_id, approved_at)"
            )
        plan_rows = self._database.execute(
            "explain query plan select detail from impacts where route_id = ? order by approved_at desc limit 1",
            (1,),
        ).fetchall()
        self._query_plan = [str(row[3]) for row in plan_rows]

    async def _handle_connection(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        self._connection_active += 1
        self._connection_peak = max(self._connection_peak, self._connection_active)
        retain = False
        try:
            raw = await asyncio.wait_for(reader.readline(), timeout=5)
            request = json.loads(raw)
            response = await self.submit(request)
        except (asyncio.TimeoutError, json.JSONDecodeError, TypeError, ValueError) as error:
            response = {
                "request_id": "invalid",
                "attempt": 0,
                "outcome": "invalid_request",
                "failure_reason": str(error),
                "completed_at": time.monotonic(),
            }
        writer.write((json.dumps(response, sort_keys=True) + "\n").encode("utf-8"))
        await writer.drain()
        maximum = int(self.scenario["telemetry"]["max_retained_connections"])
        if (
            self.scenario["fault"]["kind"] == "connection_leak"
            and len(self._retained_connections) < maximum
        ):
            self._retained_connections.append(writer)
            retain = True
        if not retain:
            writer.close()
            await writer.wait_closed()
            self._connection_active -= 1
        self.recorder.metric(
            "service.active_connections",
            self._connection_active,
            unit="{connection}",
            attributes={"state": "observed"},
        )

    async def submit(self, request: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(request.get("request_id"), str):
            raise ValueError("request_id must be a string")
        if not isinstance(request.get("attempt"), int) or request["attempt"] < 1:
            raise ValueError("attempt must be a positive integer")
        incoming = parse_traceparent(request.get("traceparent"))
        if incoming is None:
            trace_id = self.recorder.new_trace()
            parent_span_id = None
            context_state = "new"
        else:
            trace_id, parent_span_id, _flags = incoming
            context_state = "continued"
        server_span = self.recorder.start_span(
            "route-impact.server",
            trace_id=trace_id,
            parent_span_id=parent_span_id,
            attributes={"context.state": context_state},
        )
        admitted_at = time.monotonic()
        loop = asyncio.get_running_loop()
        future: asyncio.Future[dict[str, Any]] = loop.create_future()
        item = WorkItem(
            request=request,
            admitted_at=admitted_at,
            queue_depth=self.queue.qsize(),
            server_span=server_span,
            result=future,
        )
        try:
            self.queue.put_nowait(item)
        except asyncio.QueueFull:
            self.recorder.end_span(server_span, status="error", attributes={"outcome": "rejected_queue_full"})
            return self._response(item, admitted_at, time.monotonic(), "rejected_queue_full", "bounded queue full")
        self.recorder.metric(
            "service.queue_depth",
            self.queue.qsize(),
            unit="{request}",
            attributes={"queue": "route-impact"},
            trace_id=server_span.trace_id,
            span_id=server_span.span_id,
        )
        return await future

    async def _worker(self, _index: int) -> None:
        while True:
            item = await self.queue.get()
            started = time.monotonic()
            self._service_in_use += 1
            self._service_peak = max(self._service_peak, self._service_in_use)
            try:
                response = await self._process(item, started)
                if not item.result.cancelled():
                    item.result.set_result(response)
            except Exception as error:  # pragma: no cover - defensive boundary
                self.recorder.end_span(item.server_span, status="error", attributes={"outcome": "internal_error"})
                if not item.result.cancelled():
                    item.result.set_result(
                        self._response(item, started, time.monotonic(), "internal_error", str(error))
                    )
            finally:
                self._service_in_use -= 1
                self.queue.task_done()

    async def _reserve_downstream(self, amount: int) -> bool:
        limit = int(self.scenario["service"]["downstream_concurrency"])
        async with self._downstream_lock:
            if self._downstream_in_use + amount > limit:
                return False
            self._downstream_in_use += amount
            self._downstream_peak = max(self._downstream_peak, self._downstream_in_use)
            return True

    async def _process(self, item: WorkItem, started: float) -> dict[str, Any]:
        fanout = int(self.scenario["service"]["fanout"])
        if not await self._reserve_downstream(fanout):
            completed = time.monotonic()
            self.recorder.end_span(item.server_span, status="error", attributes={"outcome": "rejected_downstream"})
            return self._response(item, started, completed, "rejected_downstream", "downstream bound")
        try:
            await self._apply_fault(item)
            results = await asyncio.gather(
                *(self._branch(item, branch) for branch in range(fanout))
            )
            await self._query_dependency(item)
        finally:
            async with self._downstream_lock:
                self._downstream_in_use -= fanout
        completed = time.monotonic()
        outcome = "downstream_failure" if any(value == "failed" for value in results) else "success"
        self.recorder.log(
            "request.completed",
            severity="ERROR" if outcome != "success" else "INFO",
            trace_id=item.server_span.trace_id,
            span_id=item.server_span.span_id,
            attributes={"request_id": item.request["request_id"], "outcome": outcome},
        )
        metric_attributes = {"operation": "route-impact", "outcome": outcome}
        metric_name = "journey.duration"
        if self.scenario["fault"]["kind"] == "high_cardinality":
            metric_attributes["request_id"] = item.request["request_id"]
            metric_name = "lab.high_cardinality"
        self.recorder.metric(
            metric_name,
            (completed - item.admitted_at) * 1000,
            unit="ms",
            attributes=metric_attributes,
            trace_id=item.server_span.trace_id,
            span_id=item.server_span.span_id,
        )
        self.recorder.end_span(item.server_span, status="ok" if outcome == "success" else "error", attributes={"outcome": outcome})
        return self._response(item, started, completed, outcome, None if outcome == "success" else "branch failed")

    async def _apply_fault(self, item: WorkItem) -> None:
        fault = self.scenario["fault"]
        kind = fault["kind"]
        intensity = int(fault["intensity"])
        delay = float(fault["delay_ms"]) / 1000
        if kind == "cpu":
            token = self.recorder.start_span(
                "fault.cpu-work",
                trace_id=item.server_span.trace_id,
                parent_span_id=item.server_span.span_id,
            )
            self._cpu_work(intensity)
            self.recorder.end_span(token)
        elif kind == "allocation":
            amount = min(intensity, 1_000_000)
            self._retained_allocations.append(bytearray(amount))
            self.recorder.metric(
                "process.retained_allocation_bytes",
                sum(len(value) for value in self._retained_allocations),
                unit="By",
                attributes={"scope": "trial"},
            )
        elif kind == "lock":
            waiting = time.monotonic()
            async with self._fault_lock:
                waited_ms = (time.monotonic() - waiting) * 1000
                self.recorder.metric(
                    "service.lock_wait",
                    waited_ms,
                    unit="ms",
                    attributes={"lock": "impact-normalization"},
                )
                await asyncio.sleep(delay)
        elif kind == "slow_io":
            token = self.recorder.start_span(
                "dependency.file",
                trace_id=item.server_span.trace_id,
                parent_span_id=item.server_span.span_id,
            )
            await asyncio.to_thread(self._bounded_io, max(1, intensity), delay)
            self.recorder.end_span(token)

    @staticmethod
    def _cpu_work(iterations: int) -> str:
        digest = b"transit"
        for _ in range(iterations):
            digest = hashlib.sha256(digest).digest()
        return digest.hex()

    def _bounded_io(self, amount: int, delay: float) -> None:
        payload = b"x" * min(amount, 1_000_000)
        self._io_path.write_bytes(payload)
        _ = self._io_path.read_bytes()
        if delay:
            time.sleep(delay)

    async def _branch(self, item: WorkItem, branch: int) -> str:
        token = self.recorder.start_span(
            "route-impact.branch",
            trace_id=item.server_span.trace_id,
            parent_span_id=item.server_span.span_id,
            attributes={"branch": branch},
        )
        service = self.scenario["service"]
        material = f"{self.scenario['seed']}:{item.request['request_id']}:{item.request['attempt']}:{branch}"
        randomizer = random.Random(material)
        slow = randomizer.random() < float(service["slow_probability"])
        latency_ms = float(service["slow_service_ms"] if slow else service["base_service_ms"])
        await asyncio.sleep(latency_ms / 1000)
        failed = randomizer.random() < float(service["downstream_failure_probability"])
        self.recorder.end_span(token, status="error" if failed else "ok", attributes={"slow": slow})
        return "failed" if failed else "success"

    async def _query_dependency(self, item: WorkItem) -> None:
        token = self.recorder.start_span(
            "dependency.sqlite",
            trace_id=item.server_span.trace_id,
            parent_span_id=item.server_span.span_id,
            attributes={"db.system": "sqlite", "db.operation": "select"},
        )
        rows = self._database.execute(
            "select detail from impacts where route_id = ? order by approved_at desc limit 1",
            (1,),
        ).fetchall()
        self.recorder.end_span(token, attributes={"result.count": len(rows)})

    def _response(
        self,
        item: WorkItem,
        started: float,
        completed: float,
        outcome: str,
        failure_reason: str | None,
    ) -> dict[str, Any]:
        return {
            "request_id": item.request["request_id"],
            "attempt": item.request["attempt"],
            "outcome": outcome,
            "accepted": outcome != "rejected_queue_full",
            "scheduled_at": item.request["scheduled_at"],
            "admitted_at": item.admitted_at,
            "service_started_at": started,
            "completed_at": completed,
            "queue_wait_ms": round(max(0.0, started - item.admitted_at) * 1000, 6),
            "service_ms": round(max(0.0, completed - started) * 1000, 6),
            "end_to_end_ms": round(max(0.0, completed - item.request["scheduled_at"]) * 1000, 6),
            "queue_depth_at_admission": item.queue_depth,
            "failure_reason": failure_reason,
            "max_service_concurrency": self._service_peak,
            "max_downstream_concurrency": self._downstream_peak,
            "trace_id": item.server_span.trace_id,
            "server_span_id": item.server_span.span_id,
            "traceparent": make_traceparent(item.server_span.trace_id, item.server_span.span_id),
        }
