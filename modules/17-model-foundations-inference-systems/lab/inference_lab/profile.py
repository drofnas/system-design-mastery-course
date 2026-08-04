from __future__ import annotations

import argparse
import json
import platform
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", choices=("auto", "cpu", "cuda", "mps"), default="auto")
    args = parser.parse_args()
    try:
        import torch
    except ImportError:
        print(json.dumps({
            "status": "skipped",
            "reason": "PyTorch is not installed; optional profiling is not a readiness gate.",
            "python": platform.python_version(),
        }, sort_keys=True))
        return 0

    if args.device == "auto":
        if torch.cuda.is_available():
            device = "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
    else:
        device = args.device
    if device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but unavailable")
    if device == "mps" and not (hasattr(torch.backends, "mps") and torch.backends.mps.is_available()):
        raise SystemExit("MPS requested but unavailable")

    model = torch.nn.Sequential(torch.nn.Linear(64, 128), torch.nn.GELU(), torch.nn.Linear(128, 64)).to(device)
    inputs = torch.randn(16, 64, device=device)
    for _ in range(5):
        model(inputs)
    if device == "cuda":
        torch.cuda.synchronize()
    started = time.perf_counter_ns()
    for _ in range(20):
        model(inputs)
    if device == "cuda":
        torch.cuda.synchronize()
    elapsed_ms = (time.perf_counter_ns() - started) / 1_000_000
    print(json.dumps({
        "status": "measured",
        "evidence_kind": "measured",
        "device": device,
        "python": platform.python_version(),
        "torch": torch.__version__,
        "warmup_iterations": 5,
        "measured_iterations": 20,
        "elapsed_ms": round(elapsed_ms, 6),
        "limitations": ["This operator microprofile is not a production transformer-serving benchmark."],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
