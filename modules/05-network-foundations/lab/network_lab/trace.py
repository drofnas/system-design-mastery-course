"""Measured loopback DNS/TCP/TLS/proxy/application/dependency trace."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import socket
import ssl
import struct
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from .config import scenario_hash


def _qname(name: str) -> bytes:
    return b"".join(bytes([len(label)]) + label.encode("ascii") for label in name.split(".")) + b"\x00"


def _dns_query(name: str, query_id: int) -> bytes:
    return struct.pack("!HHHHHH", query_id, 0x0100, 1, 0, 0, 0) + _qname(name) + struct.pack("!HH", 1, 1)


def _question_end(data: bytes) -> int:
    offset = 12
    while data[offset] != 0:
        offset += data[offset] + 1
    return offset + 5


class DNSProtocol(asyncio.DatagramProtocol):
    def __init__(self, fail: bool) -> None:
        self.transport: asyncio.DatagramTransport | None = None
        self.fail = fail

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        self.transport = transport  # type: ignore[assignment]

    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None:
        query_id = struct.unpack("!H", data[:2])[0]
        end = _question_end(data)
        if self.fail:
            response = struct.pack("!HHHHHH", query_id, 0x8182, 1, 0, 0, 0) + data[12:end]
        else:
            header = struct.pack("!HHHHHH", query_id, 0x8180, 1, 1, 0, 0)
            answer = b"\xc0\x0c" + struct.pack("!HHIH", 1, 1, 30, 4) + socket.inet_aton("127.0.0.1")
            response = header + data[12:end] + answer
        assert self.transport is not None
        self.transport.sendto(response, addr)


async def query_dns(port: int, name: str, query_id: int) -> tuple[str | None, str]:
    loop = asyncio.get_running_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setblocking(False)
    try:
        await loop.sock_sendto(sock, _dns_query(name, query_id), ("127.0.0.1", port))
        data, _ = await asyncio.wait_for(loop.sock_recvfrom(sock, 512), 2)
    finally:
        sock.close()
    flags = struct.unpack("!H", data[2:4])[0]
    rcode = flags & 0xF
    if rcode != 0:
        return None, "servfail" if rcode == 2 else f"rcode_{rcode}"
    return socket.inet_ntoa(data[-4:]), "positive"


async def _read_line(reader: asyncio.StreamReader) -> dict[str, Any]:
    raw = await asyncio.wait_for(reader.readline(), 3)
    if not raw:
        raise ConnectionResetError("peer closed before response")
    return json.loads(raw)


async def _dependency(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    request = await _read_line(reader)
    response = {"route": request["route"], "version": 7, "impact": "minor"}
    writer.write(json.dumps(response, sort_keys=True).encode() + b"\n")
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def _application(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, dependency_port: int) -> None:
    request = await _read_line(reader)
    started = time.perf_counter()
    dep_reader, dep_writer = await asyncio.open_connection("127.0.0.1", dependency_port)
    dep_writer.write(json.dumps(request).encode() + b"\n")
    await dep_writer.drain()
    result = await _read_line(dep_reader)
    dep_writer.close()
    await dep_writer.wait_closed()
    dependency_ms = (time.perf_counter() - started) * 1000
    payload = b"T" * int(request["response_bytes"])
    result["payload"] = payload.decode("ascii")
    result["checksum"] = hashlib.sha256(payload).hexdigest()
    result["server_timings_ms"] = {"dependency": dependency_ms}
    result["server_timings_ms"]["application"] = (time.perf_counter() - started) * 1000
    writer.write(json.dumps(result, sort_keys=True).encode() + b"\n")
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def _edge(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, app_port: int, reset: bool) -> None:
    for attempt in range(2):
        request = await _read_line(reader)
        if reset and attempt == 0:
            writer.transport.abort()
            return
        started = time.perf_counter()
        app_reader, app_writer = await asyncio.open_connection("127.0.0.1", app_port)
        app_writer.write(json.dumps(request).encode() + b"\n")
        await app_writer.drain()
        result = await _read_line(app_reader)
        app_writer.close()
        await app_writer.wait_closed()
        result["server_timings_ms"]["edge_proxy"] = (time.perf_counter() - started) * 1000
        writer.write(json.dumps(result, sort_keys=True).encode() + b"\n")
        await writer.drain()
    writer.close()
    await writer.wait_closed()


def _certificate(directory: Path) -> tuple[Path, Path]:
    key = directory / "key.pem"
    cert = directory / "cert.pem"
    command = [
        "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
        "-keyout", str(key), "-out", str(cert), "-days", "1",
        "-subj", "/CN=impact.transit.test",
        "-addext", "subjectAltName=DNS:impact.transit.test",
    ]
    completed = subprocess.run(command, capture_output=True, text=True, timeout=10)
    if completed.returncode != 0:
        raise RuntimeError(f"openssl failed: {completed.stderr.strip()}")
    os.chmod(key, 0o600)
    return cert, key


async def trace(scenario: dict[str, Any]) -> dict[str, Any]:
    fault_type = scenario["fault"]["type"]
    started = time.perf_counter()
    timings: dict[str, float] = {}
    status = "ok"
    response: dict[str, Any] | None = None
    attempts: list[dict[str, Any]] = []
    tls: dict[str, Any] | None = None
    with tempfile.TemporaryDirectory(prefix="network-lab-") as temp_name:
        temp = Path(temp_name)
        cert, key = _certificate(temp)
        server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        server_context.minimum_version = ssl.TLSVersion.TLSv1_3
        server_context.maximum_version = ssl.TLSVersion.TLSv1_3
        server_context.load_cert_chain(cert, key)
        client_context = ssl.create_default_context(cafile=str(cert))
        client_context.check_hostname = True
        client_context.minimum_version = ssl.TLSVersion.TLSv1_3
        client_context.maximum_version = ssl.TLSVersion.TLSv1_3
        loop = asyncio.get_running_loop()
        previous_exception_handler = loop.get_exception_handler()

        def expected_tls_rejection_handler(
            active_loop: asyncio.AbstractEventLoop, context: dict[str, Any]
        ) -> None:
            error = context.get("exception")
            if context.get("message") == "Error on transport creation for incoming connection" and isinstance(
                error, (ssl.SSLError, ConnectionResetError)
            ):
                return
            if previous_exception_handler is not None:
                previous_exception_handler(active_loop, context)
            else:
                active_loop.default_exception_handler(context)

        loop.set_exception_handler(expected_tls_rejection_handler)
        dns_transport, _ = await loop.create_datagram_endpoint(
            lambda: DNSProtocol(fault_type == "dns_failure"), local_addr=("127.0.0.1", 0)
        )
        dns_port = dns_transport.get_extra_info("sockname")[1]
        dependency_server = await asyncio.start_server(_dependency, "127.0.0.1", 0)
        dependency_port = dependency_server.sockets[0].getsockname()[1]
        app_server = await asyncio.start_server(
            lambda r, w: _application(r, w, dependency_port), "127.0.0.1", 0
        )
        app_port = app_server.sockets[0].getsockname()[1]
        edge_server = await asyncio.start_server(
            lambda r, w: _edge(r, w, app_port, fault_type == "reset"),
            "127.0.0.1", 0, ssl=server_context
        )
        edge_port = edge_server.sockets[0].getsockname()[1]
        try:
            phase = time.perf_counter()
            address, dns_result = await query_dns(dns_port, "impact.transit.test", scenario["seed"] % 65535)
            timings["dns"] = (time.perf_counter() - phase) * 1000
            if address is None:
                status = "dns_failure"
            else:
                rejections = {"untrusted_anchor": False, "wrong_hostname": False}
                untrusted_context = ssl.create_default_context()
                untrusted_context.minimum_version = ssl.TLSVersion.TLSv1_3
                untrusted_context.maximum_version = ssl.TLSVersion.TLSv1_3
                try:
                    await asyncio.open_connection(
                        address, edge_port, ssl=untrusted_context, server_hostname="impact.transit.test"
                    )
                except ssl.SSLCertVerificationError:
                    rejections["untrusted_anchor"] = True
                try:
                    await asyncio.open_connection(
                        address, edge_port, ssl=client_context, server_hostname="wrong.transit.test"
                    )
                except ssl.SSLCertVerificationError:
                    rejections["wrong_hostname"] = True
                if not all(rejections.values()):
                    raise RuntimeError("TLS negative verification checks did not reject")
                phase = time.perf_counter()
                reader, writer = await asyncio.open_connection(
                    address, edge_port, ssl=client_context, server_hostname="impact.transit.test"
                )
                timings["tcp_tls_setup"] = (time.perf_counter() - phase) * 1000
                ssl_object = writer.get_extra_info("ssl_object")
                client_response_ms = 0.0
                for attempt_number in range(1, 3):
                    phase = time.perf_counter()
                    writer.write(json.dumps({
                        "route": "R-17",
                        "response_bytes": sum(item["bytes"] for item in scenario["streams"]),
                    }).encode() + b"\n")
                    await writer.drain()
                    if fault_type == "slow_reader" and attempt_number == 1:
                        await asyncio.sleep(float(scenario["fault"].get("reader_delay_ms", 25)) / 1000.0)
                    try:
                        response = await _read_line(reader)
                    except (ConnectionResetError, asyncio.IncompleteReadError):
                        status = "reset"
                        break
                    duration_ms = (time.perf_counter() - phase) * 1000
                    client_response_ms += duration_ms
                    attempt_payload = response.get("payload", "").encode("ascii")
                    attempts.append({
                        "number": attempt_number,
                        "connection": 1,
                        "reused": attempt_number > 1,
                        "duration_ms": round(duration_ms, 3),
                        "bytes": len(attempt_payload),
                        "checksum": hashlib.sha256(attempt_payload).hexdigest(),
                    })
                timings["client_response"] = client_response_ms
                writer.close()
                await writer.wait_closed()
                tls = {
                    "version": ssl_object.version(),
                    "cipher": ssl_object.cipher()[0],
                    "hostname_verified": True,
                    "rejections": rejections,
                }
                if response is not None:
                    server_timings = response.get("server_timings_ms", {})
                    for boundary in ("edge_proxy", "application", "dependency"):
                        timings[boundary] = float(server_timings[boundary])
        finally:
            edge_server.close()
            app_server.close()
            dependency_server.close()
            await edge_server.wait_closed()
            await app_server.wait_closed()
            await dependency_server.wait_closed()
            dns_transport.close()
            loop.set_exception_handler(previous_exception_handler)
        key_present_before_cleanup = key.exists()
    expected = scenario["expected_work"]["checksum"]
    payload = response.get("payload", "").encode("ascii") if response is not None else b""
    actual = hashlib.sha256(payload).hexdigest() if payload else ""
    expected_bytes = sum(item["bytes"] for item in scenario["streams"])
    equivalent = bool(
        response
        and len(payload) == expected_bytes
        and actual == expected
        and response.get("checksum") == actual
    )
    total = (time.perf_counter() - started) * 1000
    timings["total"] = total
    return {
        "schema_version": "1.0",
        "scenario_id": scenario["id"],
        "scenario_hash": scenario_hash(scenario),
        "evidence_kind": "measured_loopback",
        "seed": scenario["seed"],
        "protocol": "h1",
        "status": status,
        "phase_timings_ms": {key: round(value, 3) for key, value in timings.items()},
        "connections": {"limit": scenario["limits"]["max_connections"], "peak": 3 if response else 0, "wait_ms": 0.0, "rejected": 0, "created": 1 if attempts else 0, "reused_requests": max(0, len(attempts) - 1)},
        "attempts": attempts,
        "bytes": {"useful": sum(item["bytes"] for item in attempts), "wire_modeled": 0},
        "goodput_bytes_per_second": round(sum(item["bytes"] for item in attempts) / (total / 1000.0), 3) if attempts else 0.0,
        "stream_completion_ms": {"route-impact": round(total, 3)} if response else {},
        "events": [{"event": "dns_result", "result": dns_result}],
        "integrity": {"expected_checksum": expected, "actual_checksum": actual, "equivalent_work": equivalent and all(item["checksum"] == expected and item["bytes"] == expected_bytes for item in attempts)},
        "cleanup": {"open_connections": 0, "temporary_keys": 0, "key_existed_during_run": key_present_before_cleanup},
        "limits": scenario["limits"],
        "tls": tls,
        "limitations": [
            "Loopback combines TCP and TLS setup timing.",
            "The slow-reader case measures configured client-consumption hold time, not kernel receive-window pressure.",
            "No IP loss, routing, NAT, or public certificate system was measured.",
        ]
    }
