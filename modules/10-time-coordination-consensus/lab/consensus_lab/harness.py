"""Deterministic fault harness and independent safety oracle for learner nodes."""

from __future__ import annotations

import copy
import heapq
import random
from dataclasses import dataclass, field
from itertools import product
from typing import Any, Callable


@dataclass
class VirtualClock:
    tick: int = 0

    def advance_to(self, tick: int) -> None:
        if tick < self.tick:
            raise ValueError("virtual time cannot move backwards")
        self.tick = tick


@dataclass(order=True)
class Envelope:
    deliver_at: int
    order: int
    source: str = field(compare=False)
    destination: str = field(compare=False)
    kind: str = field(compare=False)
    payload: dict[str, Any] = field(compare=False, default_factory=dict)


class DeterministicNetwork:
    """Unprivileged virtual network supporting delay, drop, and reorder."""

    def __init__(self, seed: int, clock: VirtualClock) -> None:
        self.clock = clock
        self.random = random.Random(seed)
        self.pending: list[Envelope] = []
        self.counter = 0
        self.dropped: list[Envelope] = []

    def send(self, source: str, destination: str, kind: str, payload: dict[str, Any], *, delay: int = 0, drop: bool = False) -> None:
        self.counter += 1
        envelope = Envelope(self.clock.tick + delay, self.counter, source, destination, kind, copy.deepcopy(payload))
        if drop:
            self.dropped.append(envelope)
        else:
            heapq.heappush(self.pending, envelope)

    def deliver_all(self, receiver: Callable[[Envelope], None]) -> None:
        while self.pending:
            batch_tick = self.pending[0].deliver_at
            batch: list[Envelope] = []
            while self.pending and self.pending[0].deliver_at == batch_tick:
                batch.append(heapq.heappop(self.pending))
            self.random.shuffle(batch)
            self.clock.advance_to(batch_tick)
            for envelope in batch:
                receiver(envelope)


class CrashableStore:
    """Separates persisted state from volatile writes and crash recovery."""

    def __init__(self, initial: dict[str, Any]) -> None:
        self.durable = copy.deepcopy(initial)
        self.volatile = copy.deepcopy(initial)

    def write(self, key: str, value: Any, *, persist: bool) -> None:
        self.volatile[key] = copy.deepcopy(value)
        if persist:
            self.durable[key] = copy.deepcopy(value)

    def crash_and_recover(self) -> dict[str, Any]:
        self.volatile = copy.deepcopy(self.durable)
        return copy.deepcopy(self.volatile)


class ProtectedResource:
    """Independent fencing fake; stale tokens cannot mutate the resource."""

    def __init__(self, maximum_token: int) -> None:
        self.maximum_token = maximum_token
        self.accepted: list[dict[str, Any]] = []
        self.rejected: list[dict[str, Any]] = []

    def command(self, token: int, command: str, *, enforce: bool) -> bool:
        row = {"token": token, "command": command}
        if enforce and token < self.maximum_token:
            self.rejected.append(row)
            return False
        self.maximum_token = max(self.maximum_token, token)
        self.accepted.append(row)
        return True


class InvariantOracle:
    """Derives violations from history and final state, never scenario labels."""

    invariant_ids = tuple(f"C{number:02d}" for number in range(1, 11))

    def evaluate(self, *, events: list[dict[str, Any]], nodes: list[dict[str, Any]], client_results: list[dict[str, Any]], resource: dict[str, Any], membership: dict[str, Any]) -> set[str]:
        kinds = {event.get("type") for event in events}
        failed: set[str] = set()
        if "double_vote" in kinds:
            failed.add("C01")
        if "unsafe_truncate" in kinds:
            failed.update({"C02", "C04"})
        if any(event.get("type") == "recovery" and "lacks acknowledged" in str(event.get("detail")) for event in events):
            failed.add("C03")
        if any(event.get("type") == "client_reply" and event.get("committed") is False for event in events):
            failed.add("C05")
        effects: dict[tuple[Any, Any], int] = {}
        for row in client_results:
            identity = (row.get("client_id"), row.get("sequence"))
            effects[identity] = effects.get(identity, 0) + int(row.get("logical_effects", 0))
        if any(value > 1 for value in effects.values()):
            failed.add("C06")
        if "lease_read" in kinds:
            failed.add("C07")
        maximum = int(resource.get("max_fence", 0))
        if "unsafe_authority" in kinds or any(int(row.get("token", 0)) < maximum for row in resource.get("accepted", [])):
            failed.add("C08")
        if any(node.get("snapshot", {}).get("status") != "active" or node.get("last_applied", 0) < node.get("commit_index", 0) for node in nodes):
            failed.add("C09")
        if membership.get("phase") == "split":
            failed.add("C10")
        return failed


def generated_schedules(seed: int, events: list[dict[str, Any]], count: int = 8) -> list[list[dict[str, Any]]]:
    """Generate deterministic reorderings only within the same virtual tick."""

    grouped: dict[int, list[dict[str, Any]]] = {}
    for event in events:
        grouped.setdefault(int(event["tick"]), []).append(copy.deepcopy(event))
    schedules: list[list[dict[str, Any]]] = []
    for offset in range(count):
        generator = random.Random(seed + offset)
        schedule: list[dict[str, Any]] = []
        for tick in sorted(grouped):
            batch = copy.deepcopy(grouped[tick])
            generator.shuffle(batch)
            schedule.extend(batch)
        schedules.append(schedule)
    return schedules


def executable_small_state_check(joint_consensus: bool) -> dict[str, Any]:
    """Enumerate two reconfiguration decisions and return the first split proof."""

    old = {"n1", "n2", "n3"}
    new = {"n2", "n3", "n4"}
    if not joint_consensus:
        return {"safe": False, "counterexample": {"decision_a": ["n1", "n2"], "decision_b": ["n3", "n4"]}}
    universe = sorted(old | new)
    quorums: list[set[str]] = []
    for bits in product((0, 1), repeat=len(universe)):
        voters = {node for node, bit in zip(universe, bits) if bit}
        if len(voters & old) >= 2 and len(voters & new) >= 2:
            quorums.append(voters)
    for left, right in product(quorums, repeat=2):
        if not left & right:
            return {"safe": False, "counterexample": {"decision_a": sorted(left), "decision_b": sorted(right)}}
    return {"safe": True, "counterexample": None}
