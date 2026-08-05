from __future__ import annotations

import argparse
import copy
import ipaddress
import json
import threading
import time
from collections import OrderedDict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Iterator

from .model import KVState, TinyTransformer


MODEL = TinyTransformer()
METRICS = {
    "accepted": 0, "rejected": 0, "completed": 0, "failed": 0,
    "output_tokens": 0, "cache_hits": 0, "provider_failovers": 0,
    "reserved_bytes": 0, "queued_tokens": 0,
}
REQUIRED_REQUEST_FIELDS = {
    "request_id", "tenant_id", "prompt", "max_output_tokens", "deadline_ms",
    "traffic_class", "model_version",
}
OPTIONAL_REQUEST_FIELDS = {"provider_mode", "fallback_model_version"}


class ByteBudgetAllocator:
    """Admission reservation that refuses work before host memory is threatened."""

    def __init__(self, capacity_bytes: int) -> None:
        self.capacity_bytes = capacity_bytes
        self.reserved_bytes = 0
        self.lock = threading.Lock()

    def reserve(self, amount: int) -> bool:
        if amount <= 0:
            return False
        with self.lock:
            if self.reserved_bytes + amount > self.capacity_bytes:
                return False
            self.reserved_bytes += amount
            METRICS["reserved_bytes"] = self.reserved_bytes
            return True

    def release(self, amount: int) -> None:
        with self.lock:
            self.reserved_bytes = max(0, self.reserved_bytes - amount)
            METRICS["reserved_bytes"] = self.reserved_bytes


class TokenBudgetScheduler:
    """Bounded interactive/batch admission with explicit token ownership."""

    def __init__(self, capacity_tokens: int) -> None:
        self.capacity_tokens = capacity_tokens
        self.inflight = {"interactive": 0, "batch": 0}
        self.lock = threading.Lock()

    def acquire(self, traffic_class: str, tokens: int) -> bool:
        with self.lock:
            total = sum(self.inflight.values())
            interactive_reserve = self.capacity_tokens // 4
            if total + tokens > self.capacity_tokens:
                return False
            if traffic_class == "batch" and self.inflight["batch"] + tokens > self.capacity_tokens - interactive_reserve:
                return False
            self.inflight[traffic_class] += tokens
            METRICS["queued_tokens"] = sum(self.inflight.values())
            return True

    def release(self, traffic_class: str, tokens: int) -> None:
        with self.lock:
            self.inflight[traffic_class] = max(0, self.inflight[traffic_class] - tokens)
            METRICS["queued_tokens"] = sum(self.inflight.values())


class PromptKVCache:
    """Bounded cache keyed by tenant and every semantic/version boundary."""

    def __init__(self, maximum_entries: int = 8) -> None:
        self.maximum_entries = maximum_entries
        self.entries: OrderedDict[tuple[str, ...], KVState] = OrderedDict()
        self.lock = threading.Lock()

    @staticmethod
    def identity(request: dict[str, Any]) -> tuple[str, ...]:
        normalized = " ".join(str(request["prompt"]).lower().strip().split())
        return (
            str(request["tenant_id"]), str(request["model_version"]), MODEL.tokenizer.version,
            "atlas-prompt-v1", "python-float", "prompt-kv", normalized,
        )

    def get(self, request: dict[str, Any]) -> KVState | None:
        key = self.identity(request)
        with self.lock:
            state = self.entries.get(key)
            if state is None:
                return None
            self.entries.move_to_end(key)
            METRICS["cache_hits"] += 1
            return copy.deepcopy(state)

    def put(self, request: dict[str, Any], state: KVState) -> None:
        key = self.identity(request)
        with self.lock:
            self.entries[key] = copy.deepcopy(state)
            self.entries.move_to_end(key)
            while len(self.entries) > self.maximum_entries:
                self.entries.popitem(last=False)


class ServingRuntime:
    def __init__(self, *, byte_capacity: int = 8 * 1024 * 1024, token_capacity: int = 256) -> None:
        self.allocator = ByteBudgetAllocator(byte_capacity)
        self.scheduler = TokenBudgetScheduler(token_capacity)
        self.cache = PromptKVCache()

    @staticmethod
    def reservation_bytes(request: dict[str, Any]) -> int:
        input_tokens = len(MODEL.tokenizer.encode(str(request["prompt"])))
        total_tokens = input_tokens + int(request["max_output_tokens"])
        numeric_kv = 2 * total_tokens * MODEL.hidden_size * 8
        return max(4096, numeric_kv * 4)  # bounded allowance for Python-object overhead

    def iter_events(self, request: dict[str, Any]) -> Iterator[dict[str, Any]]:
        errors = validate_request(request)
        identity = event_identity(request)
        if errors:
            METRICS["rejected"] += 1
            yield {"type": "rejected", **identity, "reason": "; ".join(errors)}
            return
        input_tokens = len(MODEL.tokenizer.encode(request["prompt"]))
        token_budget = input_tokens + request["max_output_tokens"]
        reservation = self.reservation_bytes(request)
        estimated_ms = 5 + input_tokens * 2 + request["max_output_tokens"] * 3
        if request["deadline_ms"] < estimated_ms:
            METRICS["rejected"] += 1
            yield {"type": "rejected", **identity, "reason": "insufficient_remaining_deadline"}
            return
        if not self.allocator.reserve(reservation):
            METRICS["rejected"] += 1
            yield {"type": "rejected", **identity, "reason": "byte_budget_exhausted"}
            return
        if not self.scheduler.acquire(request["traffic_class"], token_budget):
            self.allocator.release(reservation)
            METRICS["rejected"] += 1
            yield {"type": "rejected", **identity, "reason": "token_budget_exhausted"}
            return

        METRICS["accepted"] += 1
        provider_attempts = 1
        yield {"type": "accepted", **identity, "traffic_class": request["traffic_class"], "reservation_bytes": reservation}
        started = time.monotonic_ns()
        first_ns: int | None = None
        prior_ns: int | None = None
        itl_ms: list[float] = []
        try:
            provider_mode = request.get("provider_mode", "local")
            if provider_mode == "fail_once":
                provider_attempts += 1
                fallback = request.get("fallback_model_version", MODEL.version)
                if fallback != MODEL.version or request["deadline_ms"] <= estimated_ms * 2:
                    raise RuntimeError("bounded_provider_failover_refused")
                METRICS["provider_failovers"] += 1
            cached = self.cache.get(request)
            if cached is None:
                state = MODEL.prefill(request["prompt"])
                cached_prompt = copy.deepcopy(state)
                self.cache.put(request, cached_prompt)
                reused_tokens = 0
            else:
                state = cached
                reused_tokens = state.token_count
            for index, token_id in enumerate(MODEL.generate_iter(state, request["max_output_tokens"])):
                now = time.monotonic_ns()
                if first_ns is None:
                    first_ns = now
                if prior_ns is not None:
                    itl_ms.append(round((now - prior_ns) / 1_000_000, 6))
                prior_ns = now
                yield {
                    "type": "token", **identity, "index": index, "token_id": token_id,
                    "text": MODEL.tokenizer.decode([token_id]), "kv_tokens": state.token_count,
                }
            ended = time.monotonic_ns()
            output_tokens = state.token_count - input_tokens
            METRICS["completed"] += 1
            METRICS["output_tokens"] += output_tokens
            yield {
                "type": "completed", **identity,
                "input_tokens": input_tokens, "output_tokens": output_tokens,
                "ttft_ms": round(((first_ns or ended) - started) / 1_000_000, 6),
                "mean_itl_ms": round(sum(itl_ms) / len(itl_ms), 6) if itl_ms else 0.0,
                "total_latency_ms": round((ended - started) / 1_000_000, 6),
                "estimated_cost_units": round((output_tokens + input_tokens) / 1000.0, 6),
                "kv_reused_tokens": reused_tokens, "kv_payload_bytes": state.byte_size(),
                "provider_attempts": provider_attempts,
            }
        except (ValueError, ArithmeticError, RuntimeError) as error:
            METRICS["failed"] += 1
            yield {"type": "failed", **identity, "reason": str(error), "provider_attempts": provider_attempts}
        finally:
            self.scheduler.release(request["traffic_class"], token_budget)
            self.allocator.release(reservation)


SERVING = ServingRuntime()


def validate_request(request: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    fields = set(request)
    if not REQUIRED_REQUEST_FIELDS <= fields or fields - REQUIRED_REQUEST_FIELDS - OPTIONAL_REQUEST_FIELDS:
        errors.append(f"request fields differ: {sorted((REQUIRED_REQUEST_FIELDS - fields) | (fields - REQUIRED_REQUEST_FIELDS - OPTIONAL_REQUEST_FIELDS))}")
        return errors
    if not isinstance(request["request_id"], str) or not request["request_id"]:
        errors.append("request_id must be a non-empty string")
    if not isinstance(request["tenant_id"], str) or not request["tenant_id"]:
        errors.append("tenant_id must be a non-empty authenticated-context placeholder")
    if not isinstance(request["prompt"], str) or len(request["prompt"]) > 4096:
        errors.append("prompt must be a string of at most 4096 characters")
    if not isinstance(request["max_output_tokens"], int) or not 1 <= request["max_output_tokens"] <= 16:
        errors.append("max_output_tokens must be an integer from 1 to 16")
    if not isinstance(request["deadline_ms"], int) or request["deadline_ms"] <= 0:
        errors.append("deadline_ms must be a positive integer")
    if request["traffic_class"] not in {"interactive", "batch"}:
        errors.append("traffic_class must be interactive or batch")
    if request["model_version"] != MODEL.version:
        errors.append("unsupported model_version")
    if request.get("provider_mode", "local") not in {"local", "fail_once"}:
        errors.append("provider_mode must be local or fail_once")
    return errors


def event_identity(request: dict[str, Any]) -> dict[str, Any]:
    return {
        "request_id": request.get("request_id", "invalid"), "model_version": MODEL.version,
        "tokenizer_version": MODEL.tokenizer.version, "prompt_policy_version": "atlas-prompt-v1",
        "precision": "python-float", "cache_kind": "prompt-kv",
    }


def generate_events(request: dict[str, Any]) -> list[dict[str, Any]]:
    """Compatibility helper; HTTP serving uses the iterator and flushes each event."""

    return list(SERVING.iter_events(request))


class Handler(BaseHTTPRequestHandler):
    server_version = "AtlasInferenceLab/2.0"

    def _json(self, status: int, body: dict[str, Any]) -> None:
        payload = json.dumps(body, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/healthz":
            self._json(200, {"status": "ok", "model_version": MODEL.version})
        elif self.path == "/metrics":
            self._json(200, dict(METRICS))
        else:
            self._json(404, {"error": "not_found"})

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/v1/generate":
            self._json(404, {"error": "not_found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 8192:
                raise ValueError("invalid content length")
            request = json.loads(self.rfile.read(length))
            if not isinstance(request, dict):
                raise ValueError("request body must be an object")
        except (ValueError, json.JSONDecodeError):
            self._json(400, {"error": "invalid_request"})
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        self.close_connection = True
        for event in SERVING.iter_events(request):
            self.wfile.write(json.dumps(event, sort_keys=True).encode("utf-8") + b"\n")
            self.wfile.flush()

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8017, type=int)
    args = parser.parse_args()
    try:
        if not ipaddress.ip_address(args.host).is_loopback:
            raise SystemExit("the teaching server must bind to a loopback address")
    except ValueError as error:
        raise SystemExit("--host must be a loopback IP address") from error
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Atlas inference lab listening on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
