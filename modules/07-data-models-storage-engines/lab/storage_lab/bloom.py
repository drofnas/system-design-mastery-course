from __future__ import annotations

import hashlib
import math


class BloomFilter:
    """Small deterministic Bloom filter; positives always require a real lookup."""

    def __init__(self, bit_count: int, hash_count: int = 0, bits: int = 0) -> None:
        if bit_count < 0:
            raise ValueError("bit_count must be non-negative")
        self.bit_count = bit_count
        self.hash_count = hash_count if bit_count else 0
        self.bits = bits

    @classmethod
    def for_keys(cls, keys: list[str], bits_per_key: int) -> "BloomFilter":
        if bits_per_key <= 0 or not keys:
            return cls(0)
        bit_count = max(64, len(keys) * bits_per_key)
        hash_count = max(1, min(12, round(bits_per_key * math.log(2))))
        bloom = cls(bit_count, hash_count)
        for key in keys:
            bloom.add(key)
        return bloom

    def _positions(self, key: str):
        digest = hashlib.sha256(key.encode("utf-8")).digest()
        h1 = int.from_bytes(digest[:16], "big")
        h2 = int.from_bytes(digest[16:], "big") | 1
        for index in range(self.hash_count):
            yield (h1 + index * h2) % self.bit_count

    def add(self, key: str) -> None:
        for position in self._positions(key):
            self.bits |= 1 << position

    def might_contain(self, key: str) -> bool:
        if self.bit_count == 0:
            return True
        return all(self.bits & (1 << position) for position in self._positions(key))

    def to_json(self) -> dict[str, object]:
        return {
            "bit_count": self.bit_count,
            "hash_count": self.hash_count,
            "bits_hex": hex(self.bits),
        }

    @classmethod
    def from_json(cls, data: dict[str, object]) -> "BloomFilter":
        return cls(
            int(data["bit_count"]),
            int(data["hash_count"]),
            int(str(data["bits_hex"]), 16),
        )
