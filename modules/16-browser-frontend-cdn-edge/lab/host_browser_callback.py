#!/usr/bin/env python3
"""One-shot loopback callback for WSL-to-Windows browser verification."""

from __future__ import annotations

import argparse
import json
import secrets
import subprocess
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def source_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True,
        timeout=5, check=True,
    ).stdout.strip()


def write_attestation(output: Path, record: dict[str, object]) -> None:
    if output.exists():
        raise ValueError(f"refusing to overwrite existing callback attestation: {output}")
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(port: int, timeout: int, output: Path | None = None) -> int:
    token = secrets.token_urlsafe(18)
    observed = threading.Event()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            valid = self.path == f"/callback/{token}"
            if valid:
                observed.set()
            payload = json.dumps({"callback": "verified" if valid else "invalid"}).encode()
            self.send_response(200 if valid else 404)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, format: str, *args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    print(f"Open http://localhost:{server.server_port}/callback/{token} in the normal host browser.")
    try:
        if not observed.wait(timeout):
            print(json.dumps({"result": "blocked", "reason": "host_browser_callback_not_observed"}))
            return 1
        record: dict[str, object] = {
            "schema_version": "1.0",
            "source_commit": source_commit(),
            "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "result": "pass",
            "boundary": "windows-browser-to-wsl-loopback",
            "token_persisted": False,
        }
        if output is not None:
            write_attestation(output.resolve(), record)
        print(json.dumps(record, sort_keys=True))
        return 0
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    return run(args.port, args.timeout, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
