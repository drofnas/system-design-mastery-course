#!/usr/bin/env python3
"""One-shot loopback callback for WSL-to-Windows browser verification."""

from __future__ import annotations

import argparse
import json
import secrets
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def run(port: int, timeout: int) -> int:
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
        print(json.dumps({"result": "pass", "boundary": "host-browser-to-guest-loopback", "token_disclosed": False}))
        return 0
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    return run(args.port, args.timeout)


if __name__ == "__main__":
    raise SystemExit(main())
