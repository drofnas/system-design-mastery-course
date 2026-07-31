"""Command-line interface for the capacity lab."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .analysis import analyze_events
from .config import ScenarioError, load_scenario
from .loadgen import RetryBudget, retry_budget_limit, run_trial
from .model import capacity_plan
from .service import CapacityService


def _json_dump(data: Any, output: str | None = None) -> None:
    rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if output:
        Path(output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


def _write_jsonl(events: list[dict[str, Any]], output: str) -> None:
    Path(output).write_text(
        "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
        encoding="utf-8",
    )


def _read_jsonl(path: str) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        Path(path).read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {error}") from error
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: event must be an object")
        events.append(value)
    return events


async def _serve(args: argparse.Namespace) -> None:
    scenario = load_scenario(args.scenario)
    service = CapacityService(scenario)
    host, port = await service.start(args.host, args.port)
    print(json.dumps({"host": host, "port": port, "scenario_id": scenario["id"]}))
    try:
        await asyncio.Event().wait()
    finally:
        await service.close()


async def _load(args: argparse.Namespace) -> None:
    scenario = load_scenario(args.scenario)
    connect = None
    if args.connect:
        host, raw_port = args.connect.rsplit(":", 1)
        connect = (host, int(raw_port))
    started_at = datetime.now(timezone.utc).isoformat()
    events, budget = await run_trial(scenario, connect=connect)
    _write_jsonl(events, args.output)
    _json_dump(analyze_events(scenario, events, budget), args.summary)
    if args.metadata:
        canonical_scenario = json.dumps(
            scenario,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        _json_dump(
            {
                "scenario_id": scenario["id"],
                "scenario_sha256": hashlib.sha256(canonical_scenario).hexdigest(),
                "seed": scenario["seed"],
                "arrival_mode": scenario["arrival"]["mode"],
                "started_at": started_at,
                "completed_at": datetime.now(timezone.utc).isoformat(),
                "python_version": platform.python_version(),
                "platform": platform.platform(),
                "endpoint": args.connect or "embedded-loopback",
                "event_count": len(events),
                "command": "capacity_lab load",
            },
            args.metadata,
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python3 -m capacity_lab")
    commands = parser.add_subparsers(dest="command", required=True)

    plan = commands.add_parser("plan", help="calculate the pre-experiment model")
    plan.add_argument("scenario")
    plan.add_argument("--output")

    serve = commands.add_parser("serve", help="run the bounded loopback service")
    serve.add_argument("scenario")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8080)

    load = commands.add_parser("load", help="run one open- or closed-loop trial")
    load.add_argument("scenario")
    load.add_argument("--output", required=True, help="request-attempt JSONL")
    load.add_argument("--summary", help="optional trial-summary JSON")
    load.add_argument("--metadata", help="optional reproducibility metadata JSON")
    load.add_argument("--connect", help="existing loopback service as HOST:PORT")

    analyze = commands.add_parser("analyze", help="aggregate existing request events")
    analyze.add_argument("scenario")
    analyze.add_argument("events")
    analyze.add_argument("--output")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "plan":
            _json_dump(capacity_plan(load_scenario(args.scenario)), args.output)
        elif args.command == "serve":
            asyncio.run(_serve(args))
        elif args.command == "load":
            asyncio.run(_load(args))
        elif args.command == "analyze":
            scenario = load_scenario(args.scenario)
            events = _read_jsonl(args.events)
            retries = sum(1 for event in events if int(event.get("attempt", 1)) > 1)
            _json_dump(
                analyze_events(
                    scenario,
                    events,
                    RetryBudget(
                        limit=retry_budget_limit(scenario),
                        used=retries,
                    ),
                ),
                args.output,
            )
    except (OSError, ValueError, ScenarioError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
