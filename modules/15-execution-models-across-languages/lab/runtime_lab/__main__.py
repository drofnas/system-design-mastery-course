from __future__ import annotations

import json
from pathlib import Path

from .config import load_scenario
from .runner import run_scenario

root = Path(__file__).resolve().parents[1]
scenario = root / "scenarios" / "f01-event-loop-block-broken.json"
print(json.dumps(run_scenario(load_scenario(scenario)), indent=2, sort_keys=True))
