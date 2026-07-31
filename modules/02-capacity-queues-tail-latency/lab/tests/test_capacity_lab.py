from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from capacity_lab.analysis import (
    TrialResultError,
    analyze_events,
    percentile,
    validate_trial_summary,
)
from capacity_lab.config import ScenarioError, load_scenario, validate_scenario
from capacity_lab.loadgen import (
    RetryBudget,
    _open_schedule,
    retry_budget_limit,
    run_trial,
)
from capacity_lab.model import capacity_plan, fanout_tail_probability, little_law


SCENARIOS = LAB_ROOT / "scenarios"
FIXTURES = SCENARIOS / "fixtures"


class ModelTests(unittest.TestCase):
    def test_little_law(self) -> None:
        self.assertEqual(little_law(200, 0.05), 10)

    def test_fanout_tail_probability(self) -> None:
        self.assertAlmostEqual(fanout_tail_probability(0.01, 3), 0.029701)

    def test_capacity_plan_accounts_for_failover_and_cost(self) -> None:
        plan = capacity_plan(load_scenario(SCENARIOS / "transit-baseline.json"))
        self.assertLess(
            plan["failover_capacity_per_second"],
            plan["theoretical_capacity_per_second"],
        )
        self.assertAlmostEqual(
            plan["failover_headroom_per_second"],
            plan["failover_capacity_per_second"] - 30,
            places=6,
        )
        self.assertGreater(plan["estimated_cost_per_useful_request"], 0)
        self.assertAlmostEqual(
            plan["estimated_cost_per_useful_request"],
            0.76 / (30 * 3600),
            places=12,
        )
        self.assertIn(plan["predicted_bottleneck"], {"workers", "downstream"})

    def test_percentile_interpolates(self) -> None:
        self.assertEqual(percentile([0, 10, 20], 0.5), 10)
        self.assertEqual(percentile([0, 10], 0.95), 9.5)

    def test_validation_rejects_unbounded_experiment_size(self) -> None:
        scenario = json.loads((SCENARIOS / "test-stable.json").read_text())
        scenario["arrival"]["rate_per_second"] = 10000
        scenario["arrival"]["duration_seconds"] = 300
        with self.assertRaisesRegex(ScenarioError, "100,000"):
            validate_scenario(scenario)

    def test_validation_rejects_non_finite_numbers(self) -> None:
        scenario = json.loads((SCENARIOS / "test-stable.json").read_text())
        scenario["arrival"]["rate_per_second"] = float("nan")
        with self.assertRaisesRegex(ScenarioError, "finite"):
            validate_scenario(scenario)

    def test_retry_budget_denies_work_after_shared_limit(self) -> None:
        budget = RetryBudget(limit=2)
        self.assertTrue(budget.claim())
        self.assertTrue(budget.claim())
        self.assertFalse(budget.claim())
        self.assertEqual(budget.used, 2)

    def test_useful_throughput_counts_request_identity_once(self) -> None:
        scenario = load_scenario(SCENARIOS / "test-stable.json")

        def event(request_id: str, attempt: int, outcome: str, sent_at: float) -> dict:
            return {
                "request_id": request_id,
                "attempt": attempt,
                "outcome": outcome,
                "accepted": True,
                "queue_depth_at_admission": 0,
                "sent_at": sent_at,
                "end_to_end_ms": 2.0,
                "queue_wait_ms": 0.0,
                "generator_lag_ms": 0.0,
                "max_service_concurrency": 1,
                "max_downstream_concurrency": 1,
            }

        summary = analyze_events(
            scenario,
            [
                event("request-a", 1, "downstream_failure", 0.0),
                event("request-a", 2, "success", 0.1),
                event("request-b", 1, "success", 0.2),
            ],
            RetryBudget(limit=1, used=1),
        )
        self.assertEqual(summary["attempts"], 3)
        self.assertEqual(summary["unique_successes"], 2)
        self.assertEqual(summary["useful_throughput_per_second"], 5)
        self.assertAlmostEqual(
            summary["estimated_cost_per_useful_request"],
            0.25 / (5 * 3600),
            places=12,
        )

    def test_open_schedule_is_independent_of_completion(self) -> None:
        scenario = load_scenario(SCENARIOS / "test-stable.json")
        schedule = _open_schedule(scenario, started=100.0)
        self.assertEqual(len(schedule), 8)
        for first, second in zip(schedule, schedule[1:]):
            self.assertAlmostEqual(second - first, 0.05, places=9)

    def test_open_schedule_honors_burst_boundaries(self) -> None:
        scenario = json.loads((SCENARIOS / "test-stable.json").read_text())
        scenario["arrival"].update(
            {
                "rate_per_second": 10,
                "duration_seconds": 1,
                "burst_multiplier": 2,
                "burst_start_seconds": 0.3,
                "burst_duration_seconds": 0.4,
            }
        )
        validate_scenario(scenario)
        offsets = _open_schedule(scenario, started=0)
        self.assertEqual(len(offsets), 14)
        self.assertIn(0.3, [round(offset, 10) for offset in offsets])
        self.assertIn(0.7, [round(offset, 10) for offset in offsets])
        scenario["retry"]["budget_ratio"] = 0.5
        self.assertEqual(retry_budget_limit(scenario), 7)

    def test_trial_contract_rejects_contradictory_retry_state(self) -> None:
        scenario = load_scenario(SCENARIOS / "test-stable.json")
        summary = analyze_events(scenario, [], RetryBudget(limit=1, used=0))
        summary["retry_budget"]["used"] = 2
        with self.assertRaises(TrialResultError):
            validate_trial_summary(summary)


class IntegrationTests(unittest.IsolatedAsyncioTestCase):
    async def test_stable_open_loop_is_seeded_and_successful(self) -> None:
        scenario = load_scenario(SCENARIOS / "test-stable.json")
        first_events, first_budget = await run_trial(scenario)
        second_events, second_budget = await run_trial(scenario)
        first = analyze_events(scenario, first_events, first_budget)
        second = analyze_events(scenario, second_events, second_budget)
        self.assertEqual(first["logical_requests"], second["logical_requests"])
        self.assertEqual(first["unique_successes"], first["logical_requests"])
        self.assertEqual(second["unique_successes"], second["logical_requests"])
        self.assertEqual(first["retry_budget"]["used"], 0)
        scheduled = sorted(
            event["scheduled_at"]
            for event in first_events
            if event["attempt"] == 1
        )
        for first_time, second_time in zip(scheduled, scheduled[1:]):
            self.assertAlmostEqual(second_time - first_time, 0.05, places=9)

    async def test_overload_rejects_and_bounds_retries(self) -> None:
        scenario = load_scenario(SCENARIOS / "test-overload.json")
        events, budget = await run_trial(scenario)
        summary = analyze_events(scenario, events, budget)
        self.assertGreater(summary["rejected_attempts"], 0)
        self.assertLessEqual(summary["retry_budget"]["used"], summary["retry_budget"]["limit"])
        self.assertLessEqual(summary["max_service_concurrency"], 1)
        self.assertLessEqual(summary["max_downstream_concurrency"], 1)

    async def test_downstream_reservation_rejects_without_hidden_wait(self) -> None:
        scenario = json.loads((SCENARIOS / "test-overload.json").read_text())
        scenario["id"] = "test-downstream-reservation"
        scenario["arrival"]["rate_per_second"] = 100
        scenario["arrival"]["duration_seconds"] = 0.2
        scenario["service"]["workers"] = 2
        scenario["service"]["queue_capacity"] = 10
        scenario["retry"]["max_attempts"] = 1
        scenario["retry"]["budget_ratio"] = 0
        validate_scenario(scenario)
        events, budget = await run_trial(scenario)
        summary = analyze_events(scenario, events, budget)
        self.assertIn(
            "rejected_downstream_limit",
            {event["outcome"] for event in events},
        )
        self.assertLessEqual(summary["max_downstream_concurrency"], 1)

    async def test_closed_loop_waits_for_completion(self) -> None:
        closed = load_scenario(SCENARIOS / "test-closed-loop.json")
        events, budget = await run_trial(closed)
        summary = analyze_events(closed, events, budget)
        self.assertEqual(summary["arrival_mode"], "closed")
        self.assertLess(
            summary["offered_rate_per_second"],
            closed["arrival"]["rate_per_second"],
        )

    async def test_trial_summary_has_schema_contract_fields(self) -> None:
        scenario = load_scenario(SCENARIOS / "test-stable.json")
        events, budget = await run_trial(scenario)
        summary = analyze_events(scenario, events, budget)
        required = {
            "scenario_id",
            "arrival_mode",
            "duration_seconds",
            "offered_rate_per_second",
            "logical_requests",
            "attempts",
            "accepted_attempts",
            "rejected_attempts",
            "unique_successes",
            "useful_throughput_per_second",
            "latency_ms",
            "queue_wait_ms",
            "generator_lag_ms",
            "queue_depth",
            "max_service_concurrency",
            "max_downstream_concurrency",
            "retry_budget",
            "estimated_cost_per_useful_request",
            "prediction_comparison",
            "failure_reason",
        }
        self.assertEqual(set(summary), required)

    async def test_fixture_tail_amplification(self) -> None:
        single = load_scenario(FIXTURES / "tail-single.json")
        fanout = load_scenario(FIXTURES / "tail-fanout.json")
        single_events, single_budget = await run_trial(single)
        fanout_events, fanout_budget = await run_trial(fanout)
        single_summary = analyze_events(single, single_events, single_budget)
        fanout_summary = analyze_events(fanout, fanout_events, fanout_budget)
        self.assertGreater(
            fanout_summary["latency_ms"]["p50"],
            single_summary["latency_ms"]["p50"],
        )

    async def test_fixture_stable_and_saturation_modes(self) -> None:
        stable = load_scenario(FIXTURES / "stable.json")
        saturation = load_scenario(FIXTURES / "saturation.json")
        stable_events, stable_budget = await run_trial(stable)
        saturation_events, saturation_budget = await run_trial(saturation)
        stable_summary = analyze_events(stable, stable_events, stable_budget)
        saturation_summary = analyze_events(
            saturation,
            saturation_events,
            saturation_budget,
        )
        self.assertEqual(
            stable_summary["unique_successes"],
            stable_summary["logical_requests"],
        )
        self.assertGreater(saturation_summary["rejected_attempts"], 0)

    async def test_fixture_retry_amplification_is_bounded(self) -> None:
        scenario = load_scenario(FIXTURES / "retry-amplification.json")
        events, budget = await run_trial(scenario)
        summary = analyze_events(scenario, events, budget)
        self.assertGreater(summary["attempts"], summary["logical_requests"])
        self.assertLessEqual(
            summary["attempts"],
            summary["logical_requests"] + summary["retry_budget"]["limit"],
        )
        self.assertLessEqual(summary["retry_budget"]["used"], budget.limit)

    async def test_seeded_failure_decisions_repeat(self) -> None:
        scenario = load_scenario(FIXTURES / "retry-amplification.json")
        first_events, _ = await run_trial(scenario)
        second_events, _ = await run_trial(scenario)
        first_outcomes = {
            (event["request_id"], event["attempt"]): event["outcome"]
            for event in first_events
        }
        second_outcomes = {
            (event["request_id"], event["attempt"]): event["outcome"]
            for event in second_events
        }
        self.assertEqual(first_outcomes, second_outcomes)

    async def test_fixture_failover_capacity_loss(self) -> None:
        normal = load_scenario(FIXTURES / "failover-normal.json")
        loss = load_scenario(FIXTURES / "failover-loss.json")
        normal_events, normal_budget = await run_trial(normal)
        loss_events, loss_budget = await run_trial(loss)
        normal_summary = analyze_events(normal, normal_events, normal_budget)
        loss_summary = analyze_events(loss, loss_events, loss_budget)
        self.assertGreater(
            normal_summary["unique_successes"],
            loss_summary["unique_successes"],
        )
        self.assertGreater(
            loss_summary["rejected_attempts"],
            normal_summary["rejected_attempts"],
        )

    async def test_fixture_closed_loop_under_reports_stalls(self) -> None:
        opened = load_scenario(FIXTURES / "open-loop-stall.json")
        closed = load_scenario(FIXTURES / "closed-loop-stall.json")
        open_events, open_budget = await run_trial(opened)
        closed_events, closed_budget = await run_trial(closed)
        open_summary = analyze_events(opened, open_events, open_budget)
        closed_summary = analyze_events(closed, closed_events, closed_budget)
        self.assertGreater(
            open_summary["logical_requests"],
            closed_summary["logical_requests"],
        )


if __name__ == "__main__":
    unittest.main()
