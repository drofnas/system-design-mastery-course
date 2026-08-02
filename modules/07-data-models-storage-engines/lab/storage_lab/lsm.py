from __future__ import annotations

import json
import os
import struct
from pathlib import Path
from typing import Any

from .bloom import BloomFilter


class LSMTree:
    """Educational persisted LSM with clean-close, not WAL/crash durability."""

    FORMAT = "m07-lsm-v1"

    def __init__(
        self,
        directory: Path,
        memtable_entries: int = 16,
        bloom_bits_per_key: int = 8,
        compaction_threshold: int = 4,
        compaction_enabled: bool = True,
        max_runs: int = 8,
        sparse_stride: int = 4,
    ) -> None:
        if memtable_entries < 1 or compaction_threshold < 2 or max_runs < 1 or sparse_stride < 1:
            raise ValueError("invalid LSM configuration")
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=True)
        self.manifest_path = directory / "MANIFEST.json"
        self.memtable_entries = memtable_entries
        self.bloom_bits_per_key = bloom_bits_per_key
        self.compaction_threshold = compaction_threshold
        self.compaction_enabled = compaction_enabled
        self.max_runs = max_runs
        self.sparse_stride = sparse_stride
        self.memtable: dict[str, str | None] = {}
        self.tables: list[dict[str, Any]] = []
        self.next_generation = 1
        self._metrics: dict[str, int] = {
            "table_probes": 0,
            "bloom_checks": 0,
            "bloom_negatives": 0,
            "bloom_false_positives": 0,
            "bytes_read": 0,
            "bytes_written": 0,
            "flushes": 0,
            "compactions": 0,
            "compaction_bytes": 0,
            "stalls": 0,
        }
        if self.manifest_path.exists():
            data = json.loads(self.manifest_path.read_text(encoding="utf-8"))
            if data.get("format") != self.FORMAT:
                raise ValueError("unsupported LSM manifest format")
            self.tables = list(data["tables"])
            self.next_generation = int(data["next_generation"])

    @classmethod
    def reopen(cls, directory: Path, **config: Any) -> "LSMTree":
        return cls(directory, **config)

    def reset_metrics(self) -> None:
        for key in self._metrics:
            self._metrics[key] = 0

    def _manifest(self) -> dict[str, Any]:
        return {
            "format": self.FORMAT,
            "next_generation": self.next_generation,
            "tables": self.tables,
        }

    def _write_manifest(self) -> None:
        payload = json.dumps(self._manifest(), sort_keys=True, separators=(",", ":")).encode()
        temporary = self.manifest_path.with_suffix(".tmp")
        temporary.write_bytes(payload)
        os.replace(temporary, self.manifest_path)
        self._metrics["bytes_written"] += len(payload)

    def put(self, key: str, value: str) -> None:
        self.memtable[key] = value
        self._after_write()

    def delete(self, key: str) -> bool:
        existed = self.get(key) is not None
        self.memtable[key] = None
        self._after_write()
        return existed

    def _after_write(self) -> None:
        if len(self.tables) >= self.max_runs:
            self._metrics["stalls"] += 1
        if len(self.memtable) >= self.memtable_entries:
            self.flush()

    def _table_path(self, table: dict[str, Any]) -> Path:
        return self.directory / str(table["file"])

    def _write_table(self, entries: list[tuple[str, str | None]], generation: int) -> dict[str, Any]:
        filename = f"sst-{generation:06d}.dat"
        path = self.directory / filename
        offsets: list[list[object]] = []
        bytes_written = 0
        with path.open("wb") as handle:
            for index, (key, value) in enumerate(entries):
                if index % self.sparse_stride == 0:
                    offsets.append([key, handle.tell()])
                payload = json.dumps([key, value], separators=(",", ":")).encode()
                frame = struct.pack(">I", len(payload)) + payload
                handle.write(frame)
                bytes_written += len(frame)
        bloom = BloomFilter.for_keys([key for key, _ in entries], self.bloom_bits_per_key)
        meta = {
            "generation": generation,
            "file": filename,
            "count": len(entries),
            "min_key": entries[0][0] if entries else "",
            "max_key": entries[-1][0] if entries else "",
            "sparse_index": offsets,
            "bloom": bloom.to_json(),
            "bytes": bytes_written,
            "tombstones": sum(value is None for _, value in entries),
        }
        self._metrics["bytes_written"] += bytes_written
        return meta

    def _read_entries(
        self,
        table: dict[str, Any],
        start_offset: int = 0,
        stop_after_key: str | None = None,
    ) -> list[tuple[str, str | None]]:
        path = self._table_path(table)
        entries: list[tuple[str, str | None]] = []
        with path.open("rb") as handle:
            handle.seek(start_offset)
            while True:
                header = handle.read(4)
                if not header:
                    break
                if len(header) != 4:
                    raise ValueError(f"truncated frame in {path.name}")
                length = struct.unpack(">I", header)[0]
                payload = handle.read(length)
                if len(payload) != length:
                    raise ValueError(f"truncated payload in {path.name}")
                key, value = json.loads(payload)
                entries.append((str(key), None if value is None else str(value)))
                self._metrics["bytes_read"] += 4 + length
                if stop_after_key is not None and str(key) >= stop_after_key:
                    break
        self._metrics["table_probes"] += 1
        return entries

    def flush(self) -> None:
        if not self.memtable:
            return
        generation = self.next_generation
        self.next_generation += 1
        table = self._write_table(sorted(self.memtable.items()), generation)
        self.tables.append(table)
        self.memtable.clear()
        self._metrics["flushes"] += 1
        self._write_manifest()
        if self.compaction_enabled and len(self.tables) >= self.compaction_threshold:
            self.compact_all()

    def _table_lookup(self, table: dict[str, Any], key: str) -> tuple[bool, str | None]:
        if key < str(table["min_key"]) or key > str(table["max_key"]):
            return False, None
        bloom = BloomFilter.from_json(dict(table["bloom"]))
        self._metrics["bloom_checks"] += 1
        if not bloom.might_contain(key):
            self._metrics["bloom_negatives"] += 1
            return False, None
        offset = 0
        for fence_key, fence_offset in table["sparse_index"]:
            if str(fence_key) > key:
                break
            offset = int(fence_offset)
        entries = self._read_entries(table, offset, key)
        for candidate, value in entries:
            if candidate == key:
                return True, value
        self._metrics["bloom_false_positives"] += 1
        return False, None

    def get(self, key: str) -> str | None:
        if key in self.memtable:
            return self.memtable[key]
        for table in reversed(self.tables):
            found, value = self._table_lookup(table, key)
            if found:
                return value
        return None

    def scan(self, start: str = "", end: str | None = None) -> list[tuple[str, str]]:
        visible: dict[str, tuple[int, str | None]] = {
            key: (self.next_generation, value) for key, value in self.memtable.items()
        }
        for table in self.tables:
            generation = int(table["generation"])
            for key, value in self._read_entries(table):
                if key < start or (end is not None and key >= end):
                    continue
                previous = visible.get(key)
                if previous is None or generation > previous[0]:
                    visible[key] = (generation, value)
        return sorted((key, value) for key, (_, value) in visible.items() if value is not None and key >= start and (end is None or key < end))

    def compact_all(self) -> None:
        if len(self.tables) < 2:
            return
        merged: dict[str, tuple[int, str | None]] = {}
        input_bytes = 0
        old_tables = list(self.tables)
        for table in old_tables:
            generation = int(table["generation"])
            input_bytes += int(table["bytes"])
            for key, value in self._read_entries(table):
                previous = merged.get(key)
                if previous is None or generation > previous[0]:
                    merged[key] = (generation, value)
        output_entries = sorted((key, value) for key, (_, value) in merged.items() if value is not None)
        generation = self.next_generation
        self.next_generation += 1
        output = self._write_table(output_entries, generation)
        self.tables = [output]
        self._write_manifest()
        for table in old_tables:
            self._table_path(table).unlink()
        self._metrics["compactions"] += 1
        self._metrics["compaction_bytes"] += input_bytes + int(output["bytes"])

    def close(self) -> None:
        self.flush()
        if not self.manifest_path.exists():
            self._write_manifest()

    def metrics(self) -> dict[str, int]:
        return {
            **self._metrics,
            "runs": len(self.tables),
            "tombstones": sum(int(table["tombstones"]) for table in self.tables) + sum(value is None for value in self.memtable.values()),
            "pending_compaction_bytes": sum(int(table["bytes"]) for table in self.tables) if len(self.tables) >= self.compaction_threshold else 0,
        }

    def disk_bytes(self) -> int:
        return sum(path.stat().st_size for path in self.directory.iterdir() if path.is_file())

    def live_bytes(self) -> int:
        return sum(len(key.encode()) + len(value.encode()) for key, value in self.scan())

    def validate(self) -> list[str]:
        errors: list[str] = []
        for table in self.tables:
            entries = self._read_entries(table)
            keys = [key for key, _ in entries]
            if keys != sorted(set(keys)):
                errors.append(f"{table['file']} keys are not strictly sorted")
            bloom = BloomFilter.from_json(dict(table["bloom"]))
            for key in keys:
                if not bloom.might_contain(key):
                    errors.append(f"Bloom false negative for {key}")
        return errors
