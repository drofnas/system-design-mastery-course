from __future__ import annotations

import asyncio
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any, Awaitable, Callable


class AdmissionRejected(Exception):
    pass


class TransientFailure(Exception):
    pass


class MissingResult(Exception):
    pass


class DeadlineFailure(Exception):
    pass


class IdempotencyConflict(Exception):
    pass


@dataclass
class Permit:
    controller: "AdmissionController"
    dependency: str
    tenant: str
    tracked: bool = True
    released: bool = False

    async def release(self) -> None:
        if self.released or not self.tracked:
            return
        self.released = True
        await self.controller.release(self.dependency, self.tenant)


class AdmissionController:
    def __init__(self, policy: dict[str, Any], scale: float) -> None:
        self.policy = policy
        self.scale = scale
        self.condition = asyncio.Condition()
        self.active_global = 0
        self.active_dependency: Counter[str] = Counter()
        self.active_tenant: Counter[str] = Counter()
        self.queued = 0
        self.global_peak = 0
        self.dependency_peak: Counter[str] = Counter()
        self.tenant_peak: Counter[str] = Counter()
        self.queue_peak = 0
        self.rejections = 0

    def _capacity(self, dependency: str, tenant: str) -> bool:
        dependency_limit = self.policy["per_dependency_limit"].get(
            dependency, self.policy["global_limit"]
        )
        return (
            self.active_global < self.policy["global_limit"]
            and self.active_dependency[dependency] < dependency_limit
            and self.active_tenant[tenant] < self.policy["per_tenant_limit"]
        )

    async def acquire(
        self,
        dependency: str,
        tenant: str,
        dispatch_deadline: float,
        *,
        isolated: bool = False,
    ) -> Permit:
        if isolated:
            return Permit(self, dependency, tenant, tracked=False)
        loop = asyncio.get_running_loop()
        wait_deadline = min(
            dispatch_deadline,
            loop.time() + self.policy["queue_wait_ms"] * self.scale / 1000,
        )
        queued = False
        async with self.condition:
            while not self._capacity(dependency, tenant):
                if not queued:
                    if self.queued >= self.policy["queue_limit"]:
                        self.rejections += 1
                        raise AdmissionRejected("queue full")
                    self.queued += 1
                    queued = True
                    self.queue_peak = max(self.queue_peak, self.queued)
                remaining = wait_deadline - loop.time()
                if remaining <= 0:
                    self.queued -= 1
                    self.rejections += 1
                    raise AdmissionRejected("queue wait expired")
                try:
                    await asyncio.wait_for(self.condition.wait(), timeout=remaining)
                except TimeoutError as error:
                    self.queued -= 1
                    self.rejections += 1
                    raise AdmissionRejected("queue wait expired") from error
            if queued:
                self.queued -= 1
            self.active_global += 1
            self.active_dependency[dependency] += 1
            self.active_tenant[tenant] += 1
            self.global_peak = max(self.global_peak, self.active_global)
            self.dependency_peak[dependency] = max(
                self.dependency_peak[dependency], self.active_dependency[dependency]
            )
            self.tenant_peak[tenant] = max(
                self.tenant_peak[tenant], self.active_tenant[tenant]
            )
            return Permit(self, dependency, tenant)

    async def release(self, dependency: str, tenant: str) -> None:
        async with self.condition:
            self.active_global -= 1
            self.active_dependency[dependency] -= 1
            self.active_tenant[tenant] -= 1
            self.condition.notify_all()


class RetryBudget:
    def __init__(self, tokens: int) -> None:
        self.remaining = tokens
        self.spent = 0
        self.lock = asyncio.Lock()

    async def consume(self) -> bool:
        async with self.lock:
            if self.remaining <= 0:
                return False
            self.remaining -= 1
            self.spent += 1
            return True


class IdempotencyStore:
    def __init__(self) -> None:
        self.records: dict[str, tuple[str, Any]] = {}
        self.lock = asyncio.Lock()

    async def execute(
        self,
        key: str,
        fingerprint: str,
        operation: Callable[[], Awaitable[Any]],
    ) -> tuple[Any, str]:
        async with self.lock:
            existing = self.records.get(key)
            if existing is not None:
                if existing[0] != fingerprint:
                    raise IdempotencyConflict(key)
                return existing[1], "replay"
            result = await operation()
            self.records[key] = (fingerprint, result)
            return result, "created"


class FanoutService:
    """An actual asyncio fan-out service using scaled, synthetic dependency time."""

    def __init__(self, scenario: dict[str, Any]) -> None:
        self.scenario = scenario
        self.workload = scenario["workload"]
        self.policy = scenario["policy"]
        self.fault = scenario["fault"]
        self.scale = float(self.workload["time_scale"])
        self.random = random.Random(scenario["seed"])
        self.gate = AdmissionController(self.policy, self.scale)
        self.retry_budget = RetryBudget(self.policy["retry_budget"])
        self.idempotency = IdempotencyStore()
        self.started_at = 0.0
        self.outcomes: Counter[str] = Counter()
        self.attempts: list[dict[str, Any]] = []
        self.backoffs: list[float] = []
        self.remaining_at_dispatch: list[float] = []
        self.deadline_expired = 0
        self.insufficient_budget = 0
        self.late_work = 0
        self.cancellation_signals = 0
        self.cancelled_children = 0
        self.leaked_children = 0
        self.cancellation_drains: list[float] = []
        self.effect_count = 0
        self.dedup_replays = 0
        self.dedup_conflicts = 0
        self.false_complete = 0
        self.degraded = 0
        self.unavailable = 0
        self.health_checks = 0
        self.health_rejected = 0
        self.logical_request_ids: list[str] = []

    def begin(self) -> None:
        self.started_at = asyncio.get_running_loop().time()

    def _logical_now_ms(self) -> float:
        return (
            (asyncio.get_running_loop().time() - self.started_at)
            * 1000
            / self.scale
        )

    def _seconds(self, logical_ms: float) -> float:
        return logical_ms * self.scale / 1000

    def child_budget_ms(self, parent_deadline: float) -> float:
        remaining = (parent_deadline - asyncio.get_running_loop().time()) * 1000 / self.scale
        return max(0.0, remaining - self.workload["cleanup_reserve_ms"])

    def _dependency_latency_ms(self, dependency: dict[str, Any]) -> float:
        if self.fault["slow_dependency"] == dependency["name"]:
            return float(self.fault["slow_latency_ms"])
        return float(dependency["latency_ms"])

    async def _attempt(
        self,
        request_id: str,
        tenant: str,
        dependency: dict[str, Any],
        attempt: int,
        parent_deadline: float,
    ) -> str:
        loop = asyncio.get_running_loop()
        admission_deadline = (
            parent_deadline
            if self.policy["propagate_deadline"]
            else loop.time() + self._seconds(self.workload["deadline_ms"])
        )
        dispatch_deadline = admission_deadline - self._seconds(
            self.workload["cleanup_reserve_ms"]
        )
        remaining_ms = (dispatch_deadline - loop.time()) * 1000 / self.scale
        if remaining_ms <= 0:
            self.insufficient_budget += 1
            raise DeadlineFailure("insufficient dispatch budget")
        permit = await self.gate.acquire(
            dependency["name"], tenant, dispatch_deadline
        )
        execution_deadline = (
            dispatch_deadline
            if self.policy["propagate_deadline"]
            else loop.time()
            + self._seconds(
                self.workload["deadline_ms"] - self.workload["cleanup_reserve_ms"]
            )
        )
        remaining_ms = (execution_deadline - loop.time()) * 1000 / self.scale
        self.remaining_at_dispatch.append(round(remaining_ms, 3))
        self.attempts.append(
            {
                "request_id": request_id,
                "dependency": dependency["name"],
                "attempt": attempt,
                "start_logical_ms": round(self._logical_now_ms(), 3),
            }
        )
        try:
            execution_remaining = execution_deadline - loop.time()
            if execution_remaining <= 0:
                self.insufficient_budget += 1
                raise DeadlineFailure("no execution budget")
            try:
                await asyncio.wait_for(
                    asyncio.sleep(self._seconds(self._dependency_latency_ms(dependency))),
                    timeout=execution_remaining,
                )
            except TimeoutError as error:
                self.deadline_expired += 1
                if loop.time() > parent_deadline:
                    self.late_work += 1
                raise DeadlineFailure("dependency deadline") from error
            if loop.time() > parent_deadline:
                self.late_work += 1
            if dependency["name"] in self.fault["missing_dependencies"]:
                raise MissingResult(dependency["name"])
            if (
                dependency["name"] == self.fault["retry_dependency"]
                and attempt <= self.fault["retryable_failures_per_request"]
            ):
                raise TransientFailure(dependency["name"])
            return dependency["name"]
        except asyncio.CancelledError:
            self.cancelled_children += 1
            raise
        finally:
            await permit.release()

    async def _call_dependency(
        self,
        request_id: str,
        tenant: str,
        dependency: dict[str, Any],
        parent_deadline: float,
    ) -> str:
        for attempt in range(1, self.policy["max_attempts"] + 1):
            try:
                return await self._attempt(
                    request_id, tenant, dependency, attempt, parent_deadline
                )
            except TransientFailure:
                if attempt >= self.policy["max_attempts"]:
                    raise
                if self.policy["retry_owner"] == "caller":
                    if not await self.retry_budget.consume():
                        raise AdmissionRejected("retry budget exhausted")
                else:
                    # A second retrying layer repeats the failed attempt before
                    # the caller advances its own loop. This is real measured
                    # work, not a post-run multiplier.
                    try:
                        await self._attempt(
                            request_id, tenant, dependency, attempt, parent_deadline
                        )
                    except TransientFailure:
                        pass
                cap = min(
                    self.policy["backoff_cap_ms"],
                    self.policy["backoff_base_ms"] * (2 ** (attempt - 1)),
                )
                wait_ms = self.random.uniform(0, cap) if self.policy["full_jitter"] else cap
                required_ms = wait_ms + self._dependency_latency_ms(dependency)
                if self.child_budget_ms(parent_deadline) <= required_ms:
                    self.insufficient_budget += 1
                    raise DeadlineFailure("retry does not fit")
                self.backoffs.append(round(wait_ms, 3))
                await asyncio.sleep(self._seconds(wait_ms))
        raise AssertionError("unreachable retry loop")

    async def _fanout(
        self, request_id: str, tenant: str, parent_deadline: float
    ) -> str:
        dependencies = self.scenario["dependencies"]
        tasks = [
            asyncio.create_task(
                self._call_dependency(request_id, tenant, dependency, parent_deadline),
                name=f"{request_id}:{dependency['name']}",
            )
            for dependency in dependencies
        ]
        gather = asyncio.gather(*tasks, return_exceptions=True)
        try:
            remaining = max(0.0, parent_deadline - asyncio.get_running_loop().time())
            if self.policy["cancellation"]:
                results = await asyncio.wait_for(gather, timeout=remaining)
            else:
                try:
                    results = await asyncio.wait_for(asyncio.shield(gather), timeout=remaining)
                except TimeoutError:
                    leaked = sum(not task.done() for task in tasks)
                    self.leaked_children += leaked
                    results = await gather
        except asyncio.CancelledError:
            self.cancellation_signals += 1
            signalled = asyncio.get_running_loop().time()
            if self.policy["cancellation"]:
                for task in tasks:
                    task.cancel()
            else:
                self.leaked_children += sum(not task.done() for task in tasks)
            await asyncio.gather(*tasks, return_exceptions=True)
            drain_ms = (
                (asyncio.get_running_loop().time() - signalled) * 1000 / self.scale
            )
            self.cancellation_drains.append(round(drain_ms, 3))
            self.outcomes["cancelled"] += 1
            return "cancelled"
        except TimeoutError:
            self.deadline_expired += 1
            results = await asyncio.gather(*tasks, return_exceptions=True)

        required_failure = False
        optional_failure = False
        for dependency, result in zip(dependencies, results):
            if isinstance(result, BaseException):
                if dependency["required"]:
                    required_failure = True
                else:
                    optional_failure = True
        if required_failure:
            if self.policy["explicit_partial"]:
                self.unavailable += 1
                self.outcomes["unavailable"] += 1
                return "unavailable"
            self.false_complete += 1
        elif optional_failure and self.policy["explicit_partial"]:
            self.degraded += 1
            self.outcomes["degraded"] += 1
            return "degraded"
        self.outcomes["complete"] += 1
        return "complete"

    async def _reserve(
        self,
        request_id: str,
        tenant: str,
        parent_deadline: float,
        key: str,
        fingerprint: str,
    ) -> str:
        dependency = next(item for item in self.scenario["dependencies"] if item["effectful"])

        async def effect() -> str:
            await self._call_dependency(request_id, tenant, dependency, parent_deadline)
            self.effect_count += 1
            return "reserved"

        try:
            if self.policy["deduplicate"]:
                _, disposition = await self.idempotency.execute(key, fingerprint, effect)
                if disposition == "replay":
                    self.dedup_replays += 1
            else:
                await effect()
            self.outcomes["complete"] += 1
            return "complete"
        except IdempotencyConflict:
            self.dedup_conflicts += 1
            self.outcomes["rejected"] += 1
            return "rejected"
        except (AdmissionRejected, DeadlineFailure, TransientFailure, MissingResult):
            self.outcomes["unavailable"] += 1
            self.unavailable += 1
            return "unavailable"

    async def handle_request(
        self,
        request_id: str,
        tenant: str,
        *,
        key: str | None = None,
        fingerprint: str = "status-v1",
    ) -> str:
        self.logical_request_ids.append(request_id)
        parent_deadline = asyncio.get_running_loop().time() + self._seconds(
            self.workload["deadline_ms"]
        )
        if self.workload["operation"] == "reserve":
            return await self._reserve(
                request_id,
                tenant,
                parent_deadline,
                key or request_id,
                fingerprint,
            )
        try:
            return await self._fanout(request_id, tenant, parent_deadline)
        except AdmissionRejected:
            self.outcomes["rejected"] += 1
            return "rejected"

    async def health_check(self) -> bool:
        self.health_checks += 1
        loop = asyncio.get_running_loop()
        try:
            permit = await self.gate.acquire(
                "health",
                "__health__",
                loop.time() + self._seconds(self.policy["queue_wait_ms"]),
                isolated=self.policy["health_isolated"],
            )
        except AdmissionRejected:
            self.health_rejected += 1
            return False
        await permit.release()
        return True
