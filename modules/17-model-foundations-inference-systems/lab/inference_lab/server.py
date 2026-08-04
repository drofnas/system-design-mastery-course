from __future__ import annotations

import argparse
import ipaddress
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from .model import TinyTransformer

MODEL = TinyTransformer()
METRICS = {"accepted": 0, "rejected": 0, "completed": 0, "failed": 0, "output_tokens": 0}
REQUIRED_REQUEST_FIELDS = {
    "request_id", "tenant_id", "prompt", "max_output_tokens", "deadline_ms",
    "traffic_class", "model_version",
}


def validate_request(request: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(request) != REQUIRED_REQUEST_FIELDS:
        errors.append(f"request fields differ: {sorted(set(request) ^ REQUIRED_REQUEST_FIELDS)}")
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
    return errors


def generate_events(request: dict[str, Any]) -> list[dict[str, Any]]:
    errors = validate_request(request)
    identity = {
        "request_id": request.get("request_id", "invalid"),
        "model_version": MODEL.version,
        "tokenizer_version": MODEL.tokenizer.version,
        "prompt_policy_version": "atlas-prompt-v1",
        "precision": "python-float",
        "cache_kind": "none",
    }
    if errors:
        METRICS["rejected"] += 1
        return [{"type": "rejected", **identity, "reason": "; ".join(errors)}]

    estimated_ms = 5 + len(MODEL.tokenizer.encode(request["prompt"])) * 2 + request["max_output_tokens"] * 3
    if request["deadline_ms"] < estimated_ms:
        METRICS["rejected"] += 1
        return [{"type": "rejected", **identity, "reason": "insufficient_remaining_deadline"}]

    METRICS["accepted"] += 1
    started = time.monotonic_ns()
    events: list[dict[str, Any]] = [{"type": "accepted", **identity, "traffic_class": request["traffic_class"]}]
    try:
        generated = MODEL.generate(request["prompt"], request["max_output_tokens"])
        first_ns: int | None = None
        prior_ns: int | None = None
        itl_ms: list[float] = []
        for index, token_id in enumerate(generated):
            now = time.monotonic_ns()
            if first_ns is None:
                first_ns = now
            if prior_ns is not None:
                itl_ms.append(round((now - prior_ns) / 1_000_000, 6))
            prior_ns = now
            events.append({
                "type": "token", **identity, "index": index, "token_id": token_id,
                "text": MODEL.tokenizer.decode([token_id]),
            })
        ended = time.monotonic_ns()
        METRICS["completed"] += 1
        METRICS["output_tokens"] += len(generated)
        events.append({
            "type": "completed",
            **identity,
            "input_tokens": len(MODEL.tokenizer.encode(request["prompt"])),
            "output_tokens": len(generated),
            "ttft_ms": round(((first_ns or ended) - started) / 1_000_000, 6),
            "mean_itl_ms": round(sum(itl_ms) / len(itl_ms), 6) if itl_ms else 0.0,
            "total_latency_ms": round((ended - started) / 1_000_000, 6),
            "estimated_cost_units": round((len(generated) + len(MODEL.tokenizer.encode(request["prompt"]))) / 1000.0, 6),
        })
    except (ValueError, ArithmeticError) as error:
        METRICS["failed"] += 1
        events.append({"type": "failed", **identity, "reason": type(error).__name__})
    return events


class Handler(BaseHTTPRequestHandler):
    server_version = "AtlasInferenceLab/1.0"

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
        events = generate_events(request)
        payload = b"".join(json.dumps(event, sort_keys=True).encode("utf-8") + b"\n" for event in events)
        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

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
