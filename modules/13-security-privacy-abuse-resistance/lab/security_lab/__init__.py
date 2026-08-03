"""Deterministic security, privacy, and abuse-resistance teaching model."""

from .config import load_scenario, validate_trial
from .runner import run_scenario

__all__ = ["load_scenario", "run_scenario", "validate_trial"]
