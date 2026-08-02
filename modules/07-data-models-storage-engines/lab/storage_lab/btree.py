from __future__ import annotations

import bisect
import json
import os
import struct
from collections import OrderedDict
from pathlib import Path
from typing import Any, Iterator


class FixedPageStore:
    """Fixed-size page file with a tiny LRU buffer pool and explicit counters."""

    FORMAT = "m07-bplus-v1"

    def __init__(self, path: Path, page_size: int, cache_pages: int) -> None:
        if page_size < 512:
            raise ValueError("page_size must be at least 512")
        if cache_pages < 1:
            raise ValueError("cache_pages must be positive")
        self.path = path
        self.page_size = page_size
        self.cache_pages = cache_pages
        self.cache: OrderedDict[int, dict[str, Any]] = OrderedDict()
        self.dirty: set[int] = set()
        self.metrics: dict[str, int] = {
            "page_reads": 0,
            "page_writes": 0,
            "bytes_read": 0,
            "bytes_written": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "evictions": 0,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists() and self.path.stat().st_size:
            header = self._read_raw(0)
            if header.get("format") != self.FORMAT:
                raise ValueError("unsupported B+ tree page format")
            if int(header["page_size"]) != page_size:
                raise ValueError("page_size does not match existing tree")
            self.root_id = int(header["root_id"])
            self.next_id = int(header["next_id"])
        else:
            self.path.touch()
            self.root_id = 1
            self.next_id = 2
            self.put({"id": 1, "leaf": True, "keys": [], "values": [], "next": None})

    def reset_metrics(self) -> None:
        for key in self.metrics:
            self.metrics[key] = 0

    def _encode(self, page: dict[str, Any]) -> bytes:
        payload = json.dumps(page, sort_keys=True, separators=(",", ":")).encode()
        if len(payload) + 4 > self.page_size:
            raise ValueError(f"page {page.get('id')} exceeds fixed page size")
        return struct.pack(">I", len(payload)) + payload + bytes(self.page_size - len(payload) - 4)

    def fits(self, page: dict[str, Any]) -> bool:
        try:
            self._encode(page)
            return True
        except ValueError:
            return False

    def _read_raw(self, page_id: int) -> dict[str, Any]:
        with self.path.open("rb") as handle:
            handle.seek(page_id * self.page_size)
            raw = handle.read(self.page_size)
        if len(raw) != self.page_size:
            raise ValueError(f"missing or truncated page {page_id}")
        length = struct.unpack(">I", raw[:4])[0]
        if length <= 0 or length + 4 > self.page_size:
            raise ValueError(f"invalid page frame {page_id}")
        return json.loads(raw[4 : 4 + length])

    def _write_raw(self, page_id: int, page: dict[str, Any]) -> None:
        encoded = self._encode(page)
        mode = "r+b" if self.path.exists() else "w+b"
        with self.path.open(mode) as handle:
            handle.seek(page_id * self.page_size)
            handle.write(encoded)
        self.metrics["page_writes"] += 1
        self.metrics["bytes_written"] += self.page_size

    def _evict_if_needed(self) -> None:
        while len(self.cache) > self.cache_pages:
            page_id, page = self.cache.popitem(last=False)
            if page_id in self.dirty:
                self._write_raw(page_id, page)
                self.dirty.remove(page_id)
            self.metrics["evictions"] += 1

    def get(self, page_id: int) -> dict[str, Any]:
        if page_id in self.cache:
            self.metrics["cache_hits"] += 1
            page = self.cache.pop(page_id)
            self.cache[page_id] = page
            return page
        self.metrics["cache_misses"] += 1
        page = self._read_raw(page_id)
        self.metrics["page_reads"] += 1
        self.metrics["bytes_read"] += self.page_size
        self.cache[page_id] = page
        self._evict_if_needed()
        return page

    def put(self, page: dict[str, Any]) -> None:
        page_id = int(page["id"])
        self.cache.pop(page_id, None)
        self.cache[page_id] = page
        self.dirty.add(page_id)
        self._evict_if_needed()

    def new_page(self, leaf: bool) -> dict[str, Any]:
        page_id = self.next_id
        self.next_id += 1
        page: dict[str, Any] = {"id": page_id, "leaf": leaf, "keys": []}
        if leaf:
            page.update({"values": [], "next": None})
        else:
            page["children"] = []
        return page

    def close(self) -> None:
        for page_id, page in list(self.cache.items()):
            if page_id in self.dirty:
                self._write_raw(page_id, page)
        self.dirty.clear()
        header = {
            "format": self.FORMAT,
            "page_size": self.page_size,
            "root_id": self.root_id,
            "next_id": self.next_id,
        }
        self._write_raw(0, header)
        self.cache.clear()

    def disk_bytes(self) -> int:
        return self.path.stat().st_size if self.path.exists() else 0


class BPlusTree:
    """Educational persistent B+ tree; single-process and clean-close only."""

    def __init__(self, path: Path, page_size: int = 4096, cache_pages: int = 16) -> None:
        self.path = path
        self.page_size = page_size
        self.cache_pages = cache_pages
        self.store = FixedPageStore(path, page_size, cache_pages)
        self.underfull_pages = 0

    @classmethod
    def reopen(cls, path: Path, page_size: int = 4096, cache_pages: int = 16) -> "BPlusTree":
        return cls(path, page_size, cache_pages)

    def reset_metrics(self) -> None:
        self.store.reset_metrics()

    def _find_leaf(self, key: str) -> dict[str, Any]:
        page = self.store.get(self.store.root_id)
        while not page["leaf"]:
            index = bisect.bisect_right(page["keys"], key)
            page = self.store.get(int(page["children"][index]))
        return page

    def get(self, key: str) -> str | None:
        leaf = self._find_leaf(key)
        index = bisect.bisect_left(leaf["keys"], key)
        return leaf["values"][index] if index < len(leaf["keys"]) and leaf["keys"][index] == key else None

    def put(self, key: str, value: str) -> None:
        promoted = self._insert(self.store.root_id, key, value)
        if promoted is not None:
            separator, right_id = promoted
            old_root = self.store.root_id
            root = self.store.new_page(False)
            root["keys"] = [separator]
            root["children"] = [old_root, right_id]
            self.store.put(root)
            self.store.root_id = int(root["id"])

    def _insert(self, page_id: int, key: str, value: str) -> tuple[str, int] | None:
        page = self.store.get(page_id)
        if page["leaf"]:
            index = bisect.bisect_left(page["keys"], key)
            if index < len(page["keys"]) and page["keys"][index] == key:
                page["values"][index] = value
            else:
                page["keys"].insert(index, key)
                page["values"].insert(index, value)
            if self.store.fits(page):
                self.store.put(page)
                return None
            midpoint = len(page["keys"]) // 2
            right = self.store.new_page(True)
            right["keys"] = page["keys"][midpoint:]
            right["values"] = page["values"][midpoint:]
            right["next"] = page["next"]
            page["keys"] = page["keys"][:midpoint]
            page["values"] = page["values"][:midpoint]
            page["next"] = int(right["id"])
            self.store.put(page)
            self.store.put(right)
            return str(right["keys"][0]), int(right["id"])

        child_index = bisect.bisect_right(page["keys"], key)
        promoted = self._insert(int(page["children"][child_index]), key, value)
        if promoted is None:
            return None
        separator, right_id = promoted
        page["keys"].insert(child_index, separator)
        page["children"].insert(child_index + 1, right_id)
        if self.store.fits(page):
            self.store.put(page)
            return None
        midpoint = len(page["keys"]) // 2
        up = str(page["keys"][midpoint])
        right = self.store.new_page(False)
        right["keys"] = page["keys"][midpoint + 1 :]
        right["children"] = page["children"][midpoint + 1 :]
        page["keys"] = page["keys"][:midpoint]
        page["children"] = page["children"][: midpoint + 1]
        self.store.put(page)
        self.store.put(right)
        return up, int(right["id"])

    def delete(self, key: str) -> bool:
        leaf = self._find_leaf(key)
        index = bisect.bisect_left(leaf["keys"], key)
        if index >= len(leaf["keys"]) or leaf["keys"][index] != key:
            return False
        leaf["keys"].pop(index)
        leaf["values"].pop(index)
        if not leaf["keys"] and int(leaf["id"]) != self.store.root_id:
            self.underfull_pages += 1
        self.store.put(leaf)
        return True

    def scan(self, start: str = "", end: str | None = None) -> list[tuple[str, str]]:
        leaf = self._find_leaf(start)
        result: list[tuple[str, str]] = []
        while True:
            for key, value in zip(leaf["keys"], leaf["values"]):
                if key < start:
                    continue
                if end is not None and key >= end:
                    return result
                result.append((key, value))
            if leaf["next"] is None:
                return result
            leaf = self.store.get(int(leaf["next"]))

    def validate(self) -> list[str]:
        errors: list[str] = []
        leaf_depths: set[int] = set()
        seen: set[int] = set()

        def walk(page_id: int, depth: int, low: str | None, high: str | None) -> None:
            if page_id in seen:
                errors.append(f"page cycle at {page_id}")
                return
            seen.add(page_id)
            page = self.store.get(page_id)
            keys = list(page["keys"])
            if keys != sorted(set(keys)):
                errors.append(f"page {page_id} keys are not strictly sorted")
            if low is not None and keys and keys[0] < low:
                errors.append(f"page {page_id} violates lower bound")
            if high is not None and keys and keys[-1] >= high and page["leaf"]:
                errors.append(f"page {page_id} violates upper bound")
            if page["leaf"]:
                leaf_depths.add(depth)
                if len(keys) != len(page["values"]):
                    errors.append(f"page {page_id} key/value mismatch")
                return
            children = list(page["children"])
            if len(children) != len(keys) + 1:
                errors.append(f"page {page_id} child count mismatch")
                return
            bounds = [low, *keys, high]
            for index, child in enumerate(children):
                walk(int(child), depth + 1, bounds[index], bounds[index + 1])

        walk(self.store.root_id, 0, None, None)
        if len(leaf_depths) > 1:
            errors.append("leaves have unequal depths")
        scanned = self.scan()
        if [key for key, _ in scanned] != sorted(key for key, _ in scanned):
            errors.append("linked leaves are not globally ordered")
        return errors

    def close(self) -> None:
        self.store.close()

    def metrics(self) -> dict[str, int]:
        return {**self.store.metrics, "underfull_pages": self.underfull_pages}

    def disk_bytes(self) -> int:
        return self.store.disk_bytes()

    def live_bytes(self) -> int:
        return sum(len(key.encode()) + len(value.encode()) for key, value in self.scan())
