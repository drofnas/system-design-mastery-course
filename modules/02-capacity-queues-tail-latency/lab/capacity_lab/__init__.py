"""Dependency-free capacity, queueing, and tail-latency lab."""

from .analysis import analyze_events, percentile
from .config import load_scenario, validate_scenario
from .model import capacity_plan, fanout_tail_probability, little_law

__all__ = [
    "analyze_events",
    "capacity_plan",
    "fanout_tail_probability",
    "little_law",
    "load_scenario",
    "percentile",
    "validate_scenario",
]
