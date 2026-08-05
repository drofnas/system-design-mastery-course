"""Reusable three-process boundary with deterministic unprivileged faults."""

from __future__ import annotations

import hashlib
import json
import multiprocessing as mp
import queue
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


def _worker(node_id: str, storage: str, inbox: mp.Queue, outbox: mp.Queue) -> None:
    path = Path(storage) / "events.jsonl"
    while True:
        message = inbox.get()
        if message == {"type": "stop"}:
            break
        encoded = json.dumps(message, sort_keys=True) + "\n"
        with path.open("a", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
        outbox.put({"node": node_id, "message": message})


@dataclass(order=True)
class Envelope:
    deliver_at: int
    order: int
    destination: str = field(compare=False)
    payload: dict[str, Any] = field(compare=False)


class FaultProxy:
    def __init__(self, inboxes: dict[str, mp.Queue]) -> None:
        self.inboxes = inboxes
        self.pending: list[Envelope] = []
        self.dropped: list[Envelope] = []
        self.order = 0

    def send(self, destination: str, payload: dict[str, Any], *, tick: int, delay: int = 0, drop: bool = False) -> None:
        self.order += 1
        envelope = Envelope(tick + delay, self.order, destination, json.loads(json.dumps(payload)))
        (self.dropped if drop else self.pending).append(envelope)

    def deliver_through(self, tick: int, *, reverse_same_tick: bool = False) -> int:
        ready = [row for row in self.pending if row.deliver_at <= tick]
        self.pending = [row for row in self.pending if row.deliver_at > tick]
        ready.sort(key=lambda row: (row.deliver_at, -row.order if reverse_same_tick else row.order))
        for envelope in ready:
            self.inboxes[envelope.destination].put(envelope.payload)
        return len(ready)


class ThreeNodeCluster:
    def __init__(self) -> None:
        # Supported lab hosts are macOS/Linux/WSL2, all of which provide fork.
        context = mp.get_context("fork")
        self.temporary = tempfile.TemporaryDirectory(prefix="pesd-three-node-")
        self.root = Path(self.temporary.name)
        self.inboxes = {node: context.Queue() for node in ("n1", "n2", "n3")}
        self.outbox: mp.Queue = context.Queue()
        self.processes: dict[str, mp.Process] = {}
        for node, inbox in self.inboxes.items():
            storage = self.root / node
            storage.mkdir()
            process = context.Process(target=_worker, args=(node, str(storage), inbox, self.outbox), daemon=True)
            process.start()
            self.processes[node] = process
        self.proxy = FaultProxy(self.inboxes)

    def receive(self, count: int, timeout: float = 2.0) -> list[dict[str, Any]]:
        rows = []
        for _ in range(count):
            try:
                rows.append(self.outbox.get(timeout=timeout))
            except queue.Empty as error:
                raise TimeoutError("cluster response timed out") from error
        return rows

    def storage_hashes(self) -> dict[str, str]:
        result = {}
        for node in self.processes:
            path = self.root / node / "events.jsonl"
            result[node] = hashlib.sha256(path.read_bytes() if path.exists() else b"").hexdigest()
        return result

    def close(self) -> None:
        for inbox in self.inboxes.values():
            inbox.put({"type": "stop"})
        for process in self.processes.values():
            process.join(timeout=2)
            if process.is_alive():
                raise RuntimeError("worker did not stop cleanly")
        self.temporary.cleanup()

    def __enter__(self) -> "ThreeNodeCluster":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
