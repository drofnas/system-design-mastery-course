from __future__ import annotations

import hashlib
import json
import os
import shutil
import time
from pathlib import Path
from typing import Any


def _digest(record: dict[str, Any]) -> str:
    body = {key: value for key, value in record.items() if key != "checksum"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read_wal(path: str | Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    wal_path = Path(path)
    if not wal_path.exists():
        return records
    for number, line in enumerate(wal_path.read_text(encoding="utf-8").splitlines(), 1):
        record = json.loads(line)
        if record.get("checksum") != _digest(record):
            raise ValueError(f"WAL checksum mismatch at line {number}")
        records.append(record)
    return records


class ToyStore:
    """A tiny steal/no-force store for teaching ordering, not a production DBMS."""

    def __init__(self, root: str | Path, initial_state: dict[str, Any]):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.data_path = self.root / "data.json"
        self.wal_path = self.root / "wal.jsonl"
        self.state = dict(initial_state)
        self.active: dict[str, list[tuple[str, Any, Any]]] = {}
        self.next_lsn = 1
        self.durable_lsn = 0
        self.fsync_count = 0
        self.acknowledged: list[dict[str, Any]] = []
        self._write_data()

    def _write_data(self) -> None:
        payload = {"state": self.state}
        payload["checksum"] = hashlib.sha256(json.dumps(self.state, sort_keys=True).encode()).hexdigest()
        self.data_path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")

    def append(self, kind: str, txn: str | None = None, **fields: Any) -> dict[str, Any]:
        record = {"lsn": self.next_lsn, "kind": kind, "txn": txn, **fields}
        record["checksum"] = _digest(record)
        with self.wal_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
        self.next_lsn += 1
        return record

    def flush(self, through_lsn: int | None = None) -> None:
        with self.wal_path.open("a", encoding="utf-8") as handle:
            handle.flush()
            os.fsync(handle.fileno())
        self.durable_lsn = through_lsn or self.next_lsn - 1
        self.fsync_count += 1

    def begin(self, txn: str) -> None:
        self.active[txn] = []
        self.append("BEGIN", txn)

    def update(self, txn: str, key: str, value: Any, steal: bool = True) -> None:
        before = self.state.get(key)
        self.append("UPDATE", txn, key=key, before=before, after=value)
        self.active[txn].append((key, before, value))
        if steal:
            self.state[key] = value
            self._write_data()

    def commit(self, txn: str, flush_before_ack: bool = True, acknowledge: bool = True) -> int:
        record = self.append("COMMIT", txn)
        if flush_before_ack:
            self.flush(record["lsn"])
        if acknowledge:
            self.acknowledged.append({"txn": txn, "commit_lsn": record["lsn"]})
        self.active.pop(txn, None)
        return record["lsn"]

    def group_commit(self, txns: list[str]) -> list[int]:
        """Append several commits, share one flush, then acknowledge each."""
        records = [self.append("COMMIT", txn) for txn in txns]
        self.flush(records[-1]["lsn"])
        for txn, record in zip(txns, records):
            self.acknowledged.append({"txn": txn, "commit_lsn": record["lsn"]})
            self.active.pop(txn, None)
        return [record["lsn"] for record in records]

    def abort(self, txn: str) -> None:
        for key, before, _after in reversed(self.active.get(txn, [])):
            self.state[key] = before
        self.append("ABORT", txn)
        self.active.pop(txn, None)
        self._write_data()

    def checkpoint(self) -> int:
        record = self.append("CHECKPOINT", None, state=self.state)
        self.flush(record["lsn"])
        self._write_data()
        return record["lsn"]

    def backup(self, destination: str | Path) -> Path:
        self.checkpoint()
        target = Path(destination)
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(self.data_path, target / "data.json")
        metadata = {"checkpoint_lsn": self.durable_lsn, "state": self.state}
        metadata["checksum"] = hashlib.sha256(json.dumps(metadata["state"], sort_keys=True).encode()).hexdigest()
        (target / "backup.json").write_text(json.dumps(metadata, sort_keys=True), encoding="utf-8")
        return target


def recover(data_path: str | Path, wal_path: str | Path, target_lsn: int | None = None) -> dict[str, Any]:
    started = time.perf_counter_ns()
    payload = json.loads(Path(data_path).read_text(encoding="utf-8"))
    state = dict(payload["state"])
    if payload.get("checksum") != hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest():
        raise ValueError("data checksum mismatch")
    records = [record for record in read_wal(wal_path) if target_lsn is None or record["lsn"] <= target_lsn]
    committed = {record["txn"] for record in records if record["kind"] == "COMMIT"}
    updates = [record for record in records if record["kind"] == "UPDATE"]
    for record in updates:
        if record["txn"] in committed:
            state[record["key"]] = record["after"]
    for record in reversed(updates):
        if record["txn"] not in committed:
            state[record["key"]] = record["before"]
    elapsed_ms = round((time.perf_counter_ns() - started) / 1_000_000, 3)
    return {"state": state, "committed": sorted(committed), "rto_ms": elapsed_ms, "target_lsn": target_lsn or (records[-1]["lsn"] if records else 0)}
