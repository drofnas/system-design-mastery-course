from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .analysis import wait_for_cycle


class LockManager:
    """Small shared/exclusive lock table with an inspectable wait-for graph."""

    def __init__(self) -> None:
        self.holders: dict[str, list[tuple[str, str]]] = {}
        self.waits: list[list[str]] = []

    def acquire(self, txn: str, key: str, mode: str) -> bool:
        if mode not in {"S", "X"}:
            raise ValueError("mode must be S or X")
        conflicting = [
            holder
            for holder, held_mode in self.holders.get(key, [])
            if holder != txn and (mode == "X" or held_mode == "X")
        ]
        if conflicting:
            for holder in conflicting:
                edge = [txn, holder]
                if edge not in self.waits:
                    self.waits.append(edge)
            return False
        entries = self.holders.setdefault(key, [])
        if (txn, mode) not in entries:
            entries.append((txn, mode))
        return True

    def release_all(self, txn: str) -> None:
        for key in list(self.holders):
            self.holders[key] = [entry for entry in self.holders[key] if entry[0] != txn]
            if not self.holders[key]:
                del self.holders[key]
        self.waits = [edge for edge in self.waits if txn not in edge]

    def deadlocked(self) -> bool:
        return wait_for_cycle(self.waits)


@dataclass
class MVCCTxn:
    txn_id: str
    snapshot: int
    read_set: set[str] = field(default_factory=set)
    workspace: dict[str, Any] = field(default_factory=dict)


class MVCCStore:
    """Version visibility and commit validation for controlled schedules."""

    def __init__(self, initial: dict[str, Any]):
        self.clock = 0
        self.versions = {key: [(0, value)] for key, value in initial.items()}

    def begin(self, txn_id: str) -> MVCCTxn:
        return MVCCTxn(txn_id=txn_id, snapshot=self.clock)

    def read(self, txn: MVCCTxn, key: str) -> Any:
        txn.read_set.add(key)
        if key in txn.workspace:
            return txn.workspace[key]
        visible = [value for timestamp, value in self.versions.get(key, []) if timestamp <= txn.snapshot]
        return visible[-1] if visible else None

    def write(self, txn: MVCCTxn, key: str, value: Any) -> None:
        txn.workspace[key] = value

    def commit(self, txn: MVCCTxn, serializable: bool = False) -> bool:
        latest = {key: values[-1][0] for key, values in self.versions.items() if values}
        if any(latest.get(key, 0) > txn.snapshot for key in txn.workspace):
            return False
        if serializable and any(latest.get(key, 0) > txn.snapshot for key in txn.read_set):
            return False
        self.clock += 1
        for key, value in txn.workspace.items():
            self.versions.setdefault(key, []).append((self.clock, value))
        return True
