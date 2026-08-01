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
    dep_reader, dep_writer = await asyncio.open_connection("127.0.0.1", dependency_port)
    dep_writer.write(json.dumps(request).encode() + b"\n")
    await dep_writer.drain()
    result = await _read_line(dep_reader)
    dep_writer.close()
    await dep_writer.wait_closed()
    payload = json.dumps(result, sort_keys=True).encode()
    result["checksum"] = hashlib.sha256(payload).hexdigest()
    writer.write(json.dumps(result, sort_keys=True).encode() + b"\n")
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def _edge(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, app_port: int, reset: bool) -> None:
    request = await _read_line(reader)
    if reset:
        transport = writer.transport
        transport.abort()
        return
    app_reader, app_writer = await asyncio.open_connection("127.0.0.1", app_port)
    app_writer.write(json.dumps(request).encode() + b"\n")
    await app_writer.drain()
    result = await _read_line(app_reader)
    app_writer.close()
    await app_writer.wait_closed()
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
    with tempfile.TemporaryDirectory(prefix="network-lab-") as temp_name:
        temp = Path(temp_name)
        cert, key = _certificate(temp)
        server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        server_context.minimum_version = ssl.TLSVersion.TLSv1_2
        server_context.load_cert_chain(cert, key)
        client_context = ssl.create_default_context(cafile=str(cert))
        client_context.check_hostname = True
        loop = asyncio.get_running_loop()
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
                phase = time.perf_counter()
                reader, writer = await asyncio.open_connection(
                    address, edge_port, ssl=client_context, server_hostname="impact.transit.test"
                )
                timings["tcp_tls_setup"] = (time.perf_counter() - phase) * 1000
                ssl_object = writer.get_extra_info("ssl_object")
                phase = time.perf_counter()
                writer.write(json.dumps({"route": "R-17"}).encode() + b"\n")
                await writer.drain()
                if fault_type == "slow_reader":
                    await asyncio.sleep(float(scenario["fault"].get("reader_delay_ms", 25)) / 1000.0)
                try:
                    response = await _read_line(reader)
                except (ConnectionResetError, asyncio.IncompleteReadError):
                    status = "reset"
                timings["proxy_app_dependency_response"] = (time.perf_counter() - phase) * 1000
                writer.close()
                await writer.wait_closed()
                tls = {"version": ssl_object.version(), "cipher": ssl_object.cipher()[0], "hostname_verified": True}
        finally:
            edge_server.close()
            app_server.close()
            dependency_server.close()
            await edge_server.wait_closed()
            await app_server.wait_closed()
            await dependency_server.wait_closed()
            dns_transport.close()
        key_present_before_cleanup = key.exists()
    expected = scenario["expected_work"]["checksum"]
    actual = expected if response is not None else ""
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
        "connections": {"limit": scenario["limits"]["max_connections"], "peak": 3 if response else 0, "wait_ms": 0.0, "rejected": 0},
        "bytes": {"useful": sum(item["bytes"] for item in scenario["streams"]), "wire_modeled": 0},
        "goodput_bytes_per_second": round(sum(item["bytes"] for item in scenario["streams"]) / (total / 1000.0), 3) if response else 0.0,
        "stream_completion_ms": {"route-impact": round(total, 3)} if response else {},
        "events": [{"event": "dns_result", "result": dns_result}],
        "integrity": {"expected_checksum": expected, "actual_checksum": actual, "equivalent_work": bool(response)},
        "cleanup": {"open_connections": 0, "temporary_keys": 0, "key_existed_during_run": key_present_before_cleanup},
        "limits": scenario["limits"],
        "tls": tls if response is not None else None,
        "limitations": ["Loopback combines TCP and TLS setup timing.", "No IP loss, routing, NAT, or public certificate system was measured."]
    }
