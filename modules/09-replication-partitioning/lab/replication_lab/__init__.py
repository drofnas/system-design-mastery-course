"""Deterministic teaching model for replication and partitioning."""

from .config import load_scenario, validate_trial
from .runner import run_scenario

__all__ = ["load_scenario", "run_scenario", "validate_trial"]
__version__ = "1.0.0"
