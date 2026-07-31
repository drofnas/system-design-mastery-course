"""Loopback-only bounded JSON-lines service for controlled experiments."""

from __future__ import annotations

import asyncio
import json
import random
import time
from dataclasses import dataclass
from typing import Any


@dataclass
class WorkItem:
    request: dict[str, Any]
    admitted_at: float
    queue_depth_at_admission: int
    result: asyncio.Future[dict[str, Any]]


class CapacityService:
    """A fixed worker pool with an explicit bounded waiting queue."""

    def __init__(self, scenario: dict[str, Any]) -> None:
        self.scenario = scenario
        service = scenario["service"]
        queue_capacity = int(service["queue_capacity"])
        self.queue: asyncio.Queue[WorkItem] = asyncio.Queue(maxsize=queue_capacity)
        self.worker_count = int(service["workers"])
        self._workers: list[asyncio.Task[None]] = []
        self._server: asyncio.Server | None = None
        self._service_in_use = 0
        self._service_peak = 0
        self._downstream_in_use = 0
        self._downstream_peak = 0
        self._downstream_lock = asyncio.Lock()

    @property
    def service_peak(self) -> int:
        return self._service_peak

    @property
    def downstream_peak(self) -> int:
        return self._downstream_peak

    async def start(self, host: str = "127.0.0.1", port: int = 0) -> tuple[str, int]:
        if host not in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("capacity lab serves loopback addresses only")
        self._workers = [
            asyncio.create_task(self._worker(index), name=f"capacity-worker-{index}")
            for index in range(self.worker_count)
        ]
        self._server = await asyncio.start_server(self._handle_connection, host, port)
        socket = self._server.sockets[0]
        bound_host, bound_port = socket.getsockname()[:2]
        return str(bound_host), int(bound_port)

    async def close(self) -> None:
        if self._server is not None:
            self._server.close()
            await self._server.wait_closed()
        await self.queue.join()
        for worker in self._workers:
            worker.cancel()
        await asyncio.gather(*self._workers, return_exceptions=True)
        self._workers.clear()

    async def _handle_connection(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        try:
            raw = await asyncio.wait_for(reader.readline(), timeout=5)
            request = json.loads(raw)
            response = await self.submit(request)
        except (asyncio.TimeoutError, json.JSONDecodeError, TypeError, ValueError) as error:
            response = {
                "outcome": "invalid_request",
                "failure_reason": str(error),
                "completed_at": time.monotonic(),
            }
        writer.write((json.dumps(response, sort_keys=True) + "\n").encode("utf-8"))
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    async def submit(self, request: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(request.get("request_id"), str):
            raise ValueError("request_id must be a string")
        if not isinstance(request.get("attempt"), int) or request["attempt"] < 1:
            raise ValueError("attempt must be a positive integer")

        admitted_at = time.monotonic()
        loop = asyncio.get_running_loop()
        result: asyncio.Future[dict[str, Any]] = loop.create_future()
        item = WorkItem(
            request=request,
            admitted_at=admitted_at,
            queue_depth_at_admission=self.queue.qsize(),
            result=result,
        )
        try:
            self.queue.put_nowait(item)
        except asyncio.QueueFull:
            return {
                "request_id": request["request_id"],
                "attempt": request["attempt"],
                "outcome": "rejected_queue_full",
                "accepted": False,
                "admitted_at": None,
                "service_started_at": None,
                "completed_at": time.monotonic(),
                "queue_wait_ms": 0.0,
                "service_ms": 0.0,
                "queue_depth_at_admission": self.queue.qsize(),
                "failure_reason": "bounded queue rejected the attempt",
                "max_service_concurrency": self._service_peak,
                "max_downstream_concurrency": self._downstream_peak,
            }
        return await result

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
            except Exception as error:  # pragma: no cover - defensive lab boundary
                if not item.result.cancelled():
                    item.result.set_result(
                        {
                            "request_id": item.request["request_id"],
                            "attempt": item.request["attempt"],
                            "outcome": "internal_error",
                            "accepted": True,
                            "admitted_at": item.admitted_at,
                            "service_started_at": started,
                            "completed_at": time.monotonic(),
                            "queue_wait_ms": (started - item.admitted_at) * 1000,
                            "service_ms": 0.0,
                            "queue_depth_at_admission": item.queue_depth_at_admission,
                            "failure_reason": str(error),
                            "max_service_concurrency": self._service_peak,
                            "max_downstream_concurrency": self._downstream_peak,
                        }
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

    async def _release_downstream(self, amount: int) -> None:
        async with self._downstream_lock:
            self._downstream_in_use -= amount

    async def _process(self, item: WorkItem, started: float) -> dict[str, Any]:
        service = self.scenario["service"]
        fanout = int(service["fanout"])
        if not await self._reserve_downstream(fanout):
            completed = time.monotonic()
            return self._response(
                item,
                started,
                completed,
                outcome="rejected_downstream_limit",
                failure_reason="fan-out would exceed downstream concurrency",
            )

        try:
            branches = [
                asyncio.create_task(self._branch(item.request, branch))
                for branch in range(fanout)
            ]
            results = await asyncio.gather(*branches)
        finally:
            await self._release_downstream(fanout)

        completed = time.monotonic()
        if any(result == "failed" for result in results):
            return self._response(
                item,
                started,
                completed,
                outcome="downstream_failure",
                failure_reason="at least one fan-out branch failed",
            )
        return self._response(
            item,
            started,
            completed,
            outcome="success",
            failure_reason=None,
        )

    async def _branch(self, request: dict[str, Any], branch: int) -> str:
        service = self.scenario["service"]
        material = (
            f"{self.scenario['seed']}:{request['request_id']}:"
            f"{request['attempt']}:{branch}"
        )
        randomizer = random.Random(material)
        slow = randomizer.random() < float(service["slow_probability"])
        latency_ms = (
            float(service["slow_service_ms"])
            if slow
            else float(service["base_service_ms"])
        )
        await asyncio.sleep(latency_ms / 1000)
        failed = randomizer.random() < float(service["downstream_failure_probability"])
        return "failed" if failed else "success"

    def _response(
        self,
        item: WorkItem,
        started: float,
        completed: float,
        *,
        outcome: str,
        failure_reason: str | None,
    ) -> dict[str, Any]:
        return {
            "request_id": item.request["request_id"],
            "attempt": item.request["attempt"],
            "outcome": outcome,
            "accepted": True,
            "admitted_at": item.admitted_at,
            "service_started_at": started,
            "completed_at": completed,
            "queue_wait_ms": round((started - item.admitted_at) * 1000, 6),
            "service_ms": round((completed - started) * 1000, 6),
            "queue_depth_at_admission": item.queue_depth_at_admission,
            "failure_reason": failure_reason,
            "max_service_concurrency": self._service_peak,
            "max_downstream_concurrency": self._downstream_peak,
        }
