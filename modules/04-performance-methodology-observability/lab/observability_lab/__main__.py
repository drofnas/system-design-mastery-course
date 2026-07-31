"""Command-line interface for the Module 4 observability lab."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import platform
import signal
from pathlib import Path

from .benchmark import run_benchmark
from .blind import prepare_blind_collection, reveal_blind_collection
from .config import ScenarioError, load_scenario
from .runner import analyze_bundle, run_trial, write_bundle
from .service import ObservabilityService
from .telemetry import Recorder, validate_telemetry_record


def _endpoint(value: str) -> tuple[str, int]:
    try:
        host, raw_port = value.rsplit(":", 1)
        port = int(raw_port)
    except (ValueError, TypeError) as error:
        raise argparse.ArgumentTypeError("endpoint must be HOST:PORT") from error
    if host not in {"127.0.0.1", "::1", "localhost"} or not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError("endpoint must be a loopback HOST:PORT")
    return host, port


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python3 -m observability_lab")
    commands = parser.add_subparsers(dest="command", required=True)

    run = commands.add_parser("run", help="run an embedded service and write a complete bundle")
    run.add_argument("scenario")
    run.add_argument("--output-dir", required=True)

    load = commands.add_parser("load", help="load a separately running loopback service")
    load.add_argument("scenario")
    load.add_argument("--connect", required=True, type=_endpoint)
    load.add_argument("--output-dir", required=True)

    serve = commands.add_parser("serve", help="serve the instrumented service on loopback")
    serve.add_argument("scenario")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8080)
    serve.add_argument("--output-dir", required=True)

    benchmark = commands.add_parser("benchmark", help="run an interleaved baseline/candidate comparison")
    benchmark.add_argument("baseline")
    benchmark.add_argument("candidate")
    benchmark.add_argument("--output", required=True)

    analyze = commands.add_parser("analyze", help="validate and correlate one telemetry bundle")
    analyze.add_argument("bundle")
    analyze.add_argument("--output")

    blind_prepare = commands.add_parser(
        "blind-prepare",
        help="partner: collect six opaque bundles and hold the reveal mapping separately",
    )
    blind_prepare.add_argument("--output-dir", required=True)
    blind_prepare.add_argument("--reveal-file", required=True)

    blind_reveal = commands.add_parser(
        "blind-reveal",
        help="reveal an opaque mapping after the diagnosis artifact is frozen",
    )
    blind_reveal.add_argument("--bundle-dir", required=True)
    blind_reveal.add_argument("--reveal-file", required=True)
    blind_reveal.add_argument("--frozen-diagnosis", required=True)
    blind_reveal.add_argument("--frozen-commit", required=True)
    blind_reveal.add_argument("--output", required=True)

    trial = commands.add_parser("_trial", help=argparse.SUPPRESS)
    trial.add_argument("scenario")
    trial.add_argument("--output", required=True)
    return parser


async def _run_command(args: argparse.Namespace) -> int:
    if args.command in {"run", "load"}:
        scenario = load_scenario(args.scenario)
        result = await run_trial(
            scenario,
            connect=args.connect if args.command == "load" else None,
        )
        target = write_bundle(args.output_dir, scenario, result)
        print(json.dumps({"bundle": str(target), "summary": result["summary"]}, indent=2, sort_keys=True))
        return 0
    if args.command == "benchmark":
        baseline = load_scenario(args.baseline)
        candidate = load_scenario(args.candidate)
        result = await run_benchmark(baseline, candidate)
        Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    if args.command == "_trial":
        scenario = load_scenario(args.scenario)
        result = await run_trial(scenario)
        payload = {
            "summary": result["summary"],
            "process": {
                "pid": os.getpid(),
                "python_version": platform.python_version(),
                "platform": platform.platform(),
            },
        }
        Path(args.output).write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return 0
    if args.command == "serve":
        scenario = load_scenario(args.scenario)
        recorder = Recorder(
            seed=int(scenario["seed"]),
            cardinality_budget=int(scenario["telemetry"]["cardinality_budget"]),
            max_records=int(scenario["limits"]["max_telemetry_records"]),
            enabled=bool(scenario["telemetry"]["signals_enabled"]),
        )
        service = ObservabilityService(scenario, recorder)
        host, port = await service.start(args.host, args.port)
        print(json.dumps({"host": host, "port": port}, sort_keys=True), flush=True)
        stopped = asyncio.Event()
        loop = asyncio.get_running_loop()
        for name in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(name, stopped.set)
            except NotImplementedError:  # pragma: no cover - non-Unix boundary
                pass
        try:
            await stopped.wait()
        finally:
            await service.close()
            target = Path(args.output_dir)
            target.mkdir(parents=True, exist_ok=True)
            for filename, rows in (
                ("traces.jsonl", recorder.traces),
                ("metrics.jsonl", recorder.metrics),
                ("logs.jsonl", recorder.logs),
            ):
                with (target / filename).open("w", encoding="utf-8") as stream:
                    for row in rows:
                        validate_telemetry_record(row)
                        stream.write(json.dumps(row, sort_keys=True) + "\n")
        return 0
    if args.command == "blind-prepare":
        result = await prepare_blind_collection(args.output_dir, args.reveal_file)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    raise AssertionError(f"unhandled command {args.command}")


def main() -> int:
    args = _parser().parse_args()
    try:
        if args.command == "analyze":
            result = analyze_bundle(args.bundle)
            rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
            if args.output:
                Path(args.output).write_text(rendered, encoding="utf-8")
            print(rendered, end="")
            return 0
        if args.command == "blind-reveal":
            result = reveal_blind_collection(
                args.bundle_dir,
                args.reveal_file,
                args.frozen_diagnosis,
                args.frozen_commit,
                args.output,
            )
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0
        return asyncio.run(_run_command(args))
    except (ScenarioError, OSError, ValueError) as error:
        print(f"observability lab failed: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
