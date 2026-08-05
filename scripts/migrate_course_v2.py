#!/usr/bin/env python3
"""Migrate the authored PESD-72 manifests and learning contracts to PESD-104.

The migration is deterministic and intentionally keeps the original lesson IDs,
exercise IDs, and frozen-evidence paths recognizable for V1-to-V2 crosswalking.
It does not mark a module ready; calibration, platform, and time-on-task evidence
must be refreshed after the content migration.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

CALENDAR: dict[str, list[int]] = {
    "M01": list(range(1, 6)), "M02": list(range(6, 11)), "M03": list(range(11, 16)),
    "M04": list(range(18, 23)), "M05": list(range(23, 28)), "M06": list(range(28, 33)),
    "M07": list(range(35, 40)), "M08": list(range(40, 45)), "M09": list(range(45, 50)),
    "M10": list(range(52, 58)), "M11": list(range(58, 63)), "M12": list(range(63, 68)),
    "M13": list(range(70, 75)), "M14": list(range(75, 80)), "M15": list(range(80, 85)),
    "M16": list(range(87, 92)), "M17": list(range(92, 98)), "M18": list(range(98, 103)),
}

PRIMARY: dict[str, tuple[str, str]] = {
    "M01": ("A07", "rfc"), "M02": ("A07", "adr"), "M03": ("A06", "adr"),
    "M04": ("A11", "adr"), "M05": ("A05", "adr"), "M06": ("A05", "rfc"),
    "M07": ("A06", "adr"), "M08": ("A06", "adr"), "M09": ("A06", "adr"),
    "M10": ("A06", "adr"), "M11": ("A06", "rfc"), "M12": ("A12", "adr"),
    "M13": ("A07", "rfc"), "M14": ("A07", "adr"), "M15": ("A08", "adr"),
    "M16": ("A07", "rfc"), "M17": ("A12", "adr"), "M18": ("A10", "rfc"),
}

ADDITIONS: dict[str, str] = {
    "M01": "a constraint and assurance ledger covering data classes, tenant boundaries, obligations, AI use, supplier risk, cost allocation, decision rights, evidence owners, uncertainty, and reversal triggers",
    "M02": "per-tenant allocation, forecast variance, useful-outcome economics, shared-cost policy, and modeled energy/carbon sensitivity",
    "M03": "cgroup enforcement, virtualization and steal time, noisy-neighbor isolation, architecture-specific limits, and measured-versus-host-controlled evidence boundaries",
    "M04": "telemetry as a governed data product: schema ownership, PII restrictions, retention, sampling bias, lineage, cardinality, and cost budgets",
    "M05": "workload identity, egress policy, residency-aware routing, encrypted naming implications, and a network certificate and algorithm inventory",
    "M06": "per-tenant work and cost budgets, identity-aware quotas, provider compatibility, residency-safe fallback, and fairness across critical traffic classes",
    "M07": "analytical projections, versioned data contracts, quality SLOs, lineage, stewardship, rebuild and backfill, deletion propagation, and ownership while preserving B+ tree and LSM mechanisms",
    "M08": "retention, deletion, legal holds, key rotation, logs, replicas, exports, backups, restore-time policy replay, and resurrection prevention",
    "M09": "tenant onboarding, suspension, export, offboarding, region movement, cells, control-plane/data-plane separation, tenant keys, quotas, SLOs, and cost attribution",
    "M10": "learner-written elections through membership under deterministic scheduling, crashable persistence, fencing, an independent invariant oracle, executable small-state safety checks, and mutation tests",
    "M11": "semantic event contracts, producer and consumer ownership, data quality, lineage, policy-version-aware replay, lifecycle disposition, and batch/stream reconciliation",
    "M12": "cyber recovery, corrupted-backup recovery, provider concentration, control-plane outages, clean-room assumptions, evidence preservation, and notification ownership",
    "M13": "obligation-to-control-to-evidence mapping, privacy impact reasoning, secure SDLC, source-to-deployment identity, cryptographic inventory, crypto agility, and post-quantum migration planning",
    "M14": "a thin local platform product with a service catalog, self-service interface, golden path, policy guardrails, exception path, ownership metadata, platform SLO, adoption and support metrics, FinOps allocation, and an exit plan",
    "M15": "four transport/schema shells while the learner implements admission, task ownership, cancellation, cleanup, memory and lifetime behavior, synchronization, and validation in TypeScript, Go, Rust, and Java",
    "M16": "offline and degraded client state, browser-storage lifecycle, third-party governance, AI-content transparency and provenance, edge residency, and energy/performance budgets",
    "M17": "an actual streaming tiny-transformer path with incremental KV state, token scheduling, byte-budget admission, tenant/version cache identity, bounded provider failure, profiling, and an AI System Dossier",
    "M18": "a complete AI assurance case covering tool/model inventory, provider supply chain, ongoing evaluation, human-approval efficacy, transparency, deletion, incident response, policy drift, rollback, and retirement",
}

PRIMARY_SOURCE_NOTES: dict[str, str] = {
    "M13": "Use NIST SSDF and NIST crypto-agility as primary anchors; translate obligations into controls and evidence without claiming certification.",
    "M14": "Use CNCF platform guidance and FinOps allocation guidance as primary anchors; measure adoption and support burden as product outcomes.",
    "M17": "Use the NIST AI RMF lifecycle as a primary anchor for inventory, monitoring, incident handling, rollback, and decommissioning.",
    "M18": "Use the NIST AI RMF lifecycle and applicable AI transparency guidance; jurisdictional analysis must be scoped and must not claim universal legal compliance.",
}

FEATURES: dict[tuple[str, str], tuple[str, str, str]] = {
    ("M02", "A06"): ("PI-COST-01", "LIN-COST-CAPACITY", "capacity_cost_model"),
    ("M14", "A02"): ("PI-COST-02", "LIN-COST-PLATFORM", "capacity_cost_model"),
    ("M17", "A13"): ("PI-COST-03", "LIN-COST-INFERENCE", "capacity_cost_model"),
    ("M03", "A05"): ("PI-PERF-01", "LIN-PERF-SYSTEMS", "performance_investigation"),
    ("M04", "A07"): ("PI-PERF-02", "LIN-PERF-OBSERVABILITY", "performance_investigation"),
    ("M05", "A03"): ("PI-PERF-03", "LIN-PERF-NETWORK", "performance_investigation"),
    ("M15", "A06"): ("PI-PERF-04", "LIN-PERF-RUNTIMES", "performance_investigation"),
    ("M16", "A06"): ("PI-PERF-05", "LIN-PERF-WEB-EDGE", "performance_investigation"),
    ("M17", "A06"): ("PI-PERF-06", "LIN-PERF-INFERENCE", "performance_investigation"),
    ("M06", "A11"): ("PI-POST-01", "LIN-POST-REMOTE-CALLS", "controlled_incident_postmortem"),
    ("M09", "A11"): ("PI-POST-02", "LIN-POST-REPLICATION", "controlled_incident_postmortem"),
    ("M12", "A05"): ("PI-POST-03", "LIN-POST-RECOVERY", "controlled_incident_postmortem"),
    ("M18", "A06"): ("PI-POST-04", "LIN-POST-AI", "controlled_incident_postmortem"),
    ("M03", "A04"): ("PI-FAIL-01", "LIN-FAIL-SYSTEMS", "failure_matrix"),
    ("M06", "A04"): ("PI-FAIL-02", "LIN-FAIL-REMOTE-CALLS", "failure_matrix"),
    ("M09", "A04"): ("PI-FAIL-03", "LIN-FAIL-REPLICATION", "failure_matrix"),
    ("M12", "A04"): ("PI-FAIL-04", "LIN-FAIL-RECOVERY", "failure_matrix"),
    ("M15", "A05"): ("PI-FAIL-05", "LIN-FAIL-RUNTIMES", "failure_matrix"),
    ("M18", "A05"): ("PI-FAIL-06", "LIN-FAIL-AI", "failure_matrix"),
    ("M07", "A04"): ("PI-INT-01", "LIN-INT-STORAGE", "source_code_internals_review"),
    ("M10", "A03"): ("PI-INT-02", "LIN-INT-CONSENSUS", "source_code_internals_review"),
    ("M17", "A03"): ("PI-INT-03", "LIN-INT-INFERENCE", "source_code_internals_review"),
    ("M15", "A03"): ("PI-RUNTIME-01", "LIN-RUNTIME-SEMANTICS", "runtime_comparison"),
    ("M15", "A07"): ("PI-RUNTIME-02", "LIN-RUNTIME-OPERABILITY", "runtime_comparison"),
    ("M18", "A07"): ("PI-THREAT-01", "LIN-THREAT-ASSISTANT", "threat_model"),
    ("M08", "A05"): ("PI-DR-01", "LIN-DR-RESTORE", "dr_exercise"),
    ("M12", "A07"): ("PI-DR-02", "LIN-DR-FAILOVER", "dr_exercise"),
    ("M14", "A04"): ("PI-MIG-01", "LIN-MIG-PLATFORM", "migration_plan"),
    ("M18", "A09"): ("PI-MIG-02", "LIN-MIG-CAPSTONE", "migration_plan"),
    ("M11", "A03"): ("PI-GOV-01", "LIN-GOV-DATA", "data_governance_dossier"),
    ("M13", "A06"): ("PI-ASSURE-01", "LIN-ASSURE-SYSTEM", "assurance_case"),
    ("M14", "A03"): ("PI-PLATFORM-01", "LIN-PLATFORM-PRODUCT", "platform_product_experiment"),
    ("M18", "A03"): ("PI-AI-01", "LIN-AI-SYSTEM", "ai_system_dossier"),
}

BASELINE_COMPONENTS: dict[tuple[str, str], tuple[str, str]] = {
    ("M13", "A05"): ("PI-THREAT-01", "LIN-THREAT-ASSISTANT"),
    ("M07", "A10"): ("PI-GOV-01", "LIN-GOV-DATA"),
    ("M17", "A07"): ("PI-AI-01", "LIN-AI-SYSTEM"),
}

REMOVED_GATE_DUPLICATES: dict[str, set[str]] = {
    "M03": {"A08", "A09"},
    "M06": {"A07", "A08", "A10"},
    "M09": {"A08", "A10"},
    "M12": {"A09", "A10"},
    "M15": {"A10", "A11"},
    "M18": {"A12", "A13", "A14"},
}

V2_RESOURCES: dict[str, list[dict[str, str]]] = {
    "M13": [
        {"id": "RES-14", "title": "Secure Software Development Framework", "publisher": "NIST", "url": "https://csrc.nist.gov/projects/ssdf", "boundary": "Read the SSDF practices and use sections; map applicable outcomes to source, build, release, and vulnerability-response evidence."},
        {"id": "RES-15", "title": "Crypto Agility", "publisher": "NIST", "url": "https://csrc.nist.gov/Projects/crypto-agility", "boundary": "Read the overview and current publications boundary; inventory algorithms and plan replacement without claiming a universal migration schedule."},
    ],
    "M14": [
        {"id": "RES-10", "title": "CNCF Platforms White Paper", "publisher": "CNCF TAG App Delivery", "url": "https://tag-app-delivery.cncf.io/whitepapers/platforms/", "boundary": "Read why platforms, successful platform/team attributes, challenges, measurement, and capabilities; extract user-value and support hypotheses."},
        {"id": "RES-11", "title": "Allocation FinOps Framework Capability", "publisher": "FinOps Foundation", "url": "https://www.finops.org/framework/capabilities/allocation/", "boundary": "Read definition, allocation/tagging/shared-cost strategies, and measures; define one transparent allocation and exception policy."},
    ],
    "M16": [
        {"id": "RES-14", "title": "Guidelines on transparency obligations for providers and deployers of AI systems", "publisher": "European Commission", "url": "https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems", "boundary": "Read scope and Article 50 transparency categories; record applicability and uncertainty before translating any obligation into a web control."},
    ],
    "M17": [
        {"id": "RES-10", "title": "NIST AI RMF Core", "publisher": "NIST AIRC", "url": "https://airc.nist.gov/airmf-resources/airmf/5-sec-core/", "boundary": "Read Govern 1.5–1.7 and Manage 3–4; map inventory, monitoring, supplier, incident, recovery, and decommission outcomes into the dossier."},
    ],
    "M18": [
        {"id": "RES-09", "title": "NIST AI RMF Core", "publisher": "NIST AIRC", "url": "https://airc.nist.gov/airmf-resources/airmf/5-sec-core/", "boundary": "Read Govern 1.5–1.7 and Manage 3–4; complete lifecycle inventory, monitoring, incident, recovery, supplier, and retirement evidence."},
        {"id": "RES-10", "title": "Guidelines on transparency obligations for providers and deployers of AI systems", "publisher": "European Commission", "url": "https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems", "boundary": "Read scope and Article 50 categories. Translate only applicable obligations and preserve legal uncertainty; do not claim universal compliance."},
    ],
}


def dump(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def append_once(path: Path, marker: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(text.rstrip() + "\n\n" + body.strip() + "\n", encoding="utf-8")


def artifact_role(category: str, primary: bool) -> str:
    if primary:
        return "decision"
    if category in {"implementation", "platform_product_experiment"}:
        return "implementation"
    if category in {"failure_matrix", "dr_exercise"}:
        return "raw_evidence"
    if category in {
        "performance_investigation", "controlled_incident_postmortem",
        "source_code_internals_review", "runtime_comparison", "threat_model",
        "capacity_cost_model", "data_governance_dossier", "assurance_case",
        "ai_system_dossier",
    }:
        return "analysis"
    if category == "capstone":
        return "revision"
    if category in {"evaluation", "teach_back", "learning_log", "migration_plan"}:
        return "final"
    return "prediction"


def evidence_mode(category: str, role: str) -> str:
    if category in {"performance_investigation", "runtime_comparison"}:
        return "measured_loopback"
    if category == "capacity_cost_model":
        return "modeled_capacity"
    if category in {"failure_matrix", "implementation", "dr_exercise"}:
        return "executed_deterministic"
    if role in {"baseline", "decision", "analysis", "prediction", "final", "revision"}:
        return "derived"
    return "executed_deterministic"


def add_v2_artifacts(module: dict[str, Any]) -> None:
    module_id = module["id"]
    existing = {row["id"] for row in module["artifacts"]}
    if module_id == "M07" and "A10" not in existing:
        module["artifacts"].append({
            "id": "A10", "week": CALENDAR[module_id][1], "required": True,
            "template_path": "templates/pesd-v2-dossier-template.md",
            "submission_path": "reports/module-07-data-governance-dossier.md",
            "portfolio_category": "data_governance_dossier",
        })
    if module_id == "M17" and "A13" not in existing:
        module["artifacts"].append({
            "id": "A13", "week": CALENDAR[module_id][3], "required": True,
            "template_path": "templates/architecture-cost-model-template.md",
            "submission_path": "reports/module-17-useful-output-cost-model.md",
            "portfolio_category": "capacity_cost_model",
        })


def add_v2_resources(module: dict[str, Any], module_root: Path) -> None:
    existing = {row.get("id") for row in module.get("resources", [])}
    lesson8 = sorted((module_root / "lessons").glob("08-*.md"))
    if len(lesson8) != 1:
        raise ValueError(f"{module['id']}: expected one Lesson 8 for resource fallback")
    fallback = lesson8[0].relative_to(module_root).as_posix()
    for source in V2_RESOURCES.get(module["id"], []):
        if source["id"] in existing:
            continue
        module["resources"].append({
            "id": source["id"], "title": source["title"],
            "author_or_publisher": source["publisher"], "type": "official primary guidance",
            "url": source["url"], "required": True, "access": "free",
            "week": CALENDAR[module["id"]][0], "estimated_minutes": 20,
            "purpose": "Ground the PESD 2.0 cross-cutting decision in current primary guidance and produce scoped evidence rather than framework vocabulary.",
            "assignment": source["boundary"], "last_verified": "2026-08-04",
            "text_alternative": fallback, "verified_title": source["title"],
            "verified_publisher": source["publisher"],
            "verification_method": "HTTP GET plus primary-source metadata comparison",
            "final_url": source["url"], "verification_status": "verified",
        })
def migrate_artifacts(module: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    module_id = module["id"]
    primary_id, primary_category = PRIMARY[module_id]
    add_v2_artifacts(module)
    phase_buckets: dict[str, list[dict[str, Any]]] = {key: [] for key in ("model", "build", "integrate", "break", "decide")}
    deep = module_id in {"M10", "M17"}
    featured_counts = [0 for _ in CALENDAR[module_id]]
    for artifact in module["artifacts"]:
        artifact_id = artifact["id"]
        if module_id == "M17" and artifact_id == "A13":
            artifact["template_path"] = "templates/architecture-cost-model-template.md"
        is_primary = artifact_id == primary_id
        if is_primary:
            artifact["portfolio_category"] = primary_category
        elif artifact["portfolio_category"] in {"adr", "rfc"}:
            artifact["portfolio_category"] = "model"
        if (module_id, artifact_id) == ("M01", "A01"):
            artifact["portfolio_item_id"] = "PI-CAPSTONE-01"
            artifact["portfolio_credit"] = False
            artifact["evidence_lineage_id"] = "LIN-CAPSTONE-GLOBAL-COMMERCE"
        elif is_primary:
            artifact["portfolio_item_id"] = f"PI-DECISION-{module_id}"
            artifact["portfolio_credit"] = True
            artifact["evidence_lineage_id"] = f"LIN-DECISION-{module_id}"
        elif (module_id, artifact_id) in FEATURES:
            item_id, lineage, category = FEATURES[(module_id, artifact_id)]
            artifact["portfolio_category"] = category
            artifact["portfolio_item_id"] = item_id
            artifact["portfolio_credit"] = True
            artifact["evidence_lineage_id"] = lineage
        elif (module_id, artifact_id) in BASELINE_COMPONENTS:
            item_id, lineage = BASELINE_COMPONENTS[(module_id, artifact_id)]
            artifact["portfolio_item_id"] = item_id
            artifact["portfolio_credit"] = False
            artifact["evidence_lineage_id"] = lineage
        else:
            artifact["portfolio_item_id"] = None
            artifact["portfolio_credit"] = False
            artifact["evidence_lineage_id"] = f"LIN-{module_id}-{artifact_id}"
        role = artifact_role(artifact["portfolio_category"], is_primary)
        if (module_id, artifact_id) == ("M01", "A01") or (module_id, artifact_id) in BASELINE_COMPONENTS:
            role = "baseline"
        if module_id == "M18" and artifact_id in {"A03", "A07"}:
            role = "final"
        artifact["component_role"] = role
        artifact["estimated_minutes"] = 30
        artifact["evidence_mode"] = evidence_mode(artifact["portfolio_category"], role)

        if role == "baseline":
            bucket = "model"
        elif role == "prediction":
            bucket = "build"
        elif role == "implementation":
            bucket = "integrate" if deep and len(phase_buckets["build"]) else "build"
        elif role in {"raw_evidence", "analysis"}:
            bucket = "break"
        else:
            bucket = "decide"
        phase_buckets[bucket].append(artifact)

    overrides = {
        ("M18", "A03"): "build",
        ("M18", "A07"): "break",
    }
    for (owner, artifact_id), destination in overrides.items():
        if owner != module_id:
            continue
        for source, rows in phase_buckets.items():
            match = next((row for row in rows if row["id"] == artifact_id), None)
            if match is not None and source != destination:
                rows.remove(match)
                phase_buckets[destination].append(match)
                break

    # Spread polished work so no module week closes more than two featured items.
    for bucket in ("break", "decide", "build", "integrate", "model"):
        featured = [row for row in phase_buckets[bucket] if row.get("portfolio_credit")]
        while len(featured) > 2:
            row = featured.pop(0)
            phase_buckets[bucket].remove(row)
            destination = "integrate" if deep and bucket != "integrate" else "build"
            if destination == bucket:
                destination = "model"
            phase_buckets[destination].append(row)

    phase_index = {"model": 0, "build": 1, "integrate": 2, "break": -2, "decide": -1}
    for bucket, rows in phase_buckets.items():
        week = CALENDAR[module_id][phase_index[bucket]]
        for artifact in rows:
            artifact["week"] = week
    return phase_buckets


def split_rows(rows: list[Any]) -> tuple[list[Any], list[Any]]:
    midpoint = (len(rows) + 1) // 2
    return rows[:midpoint], rows[midpoint:]


def split_weighted_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Balance scheduled resources by minutes instead of record count."""
    partitions: list[list[dict[str, Any]]] = [[], []]
    totals = [0, 0]
    for row in sorted(rows, key=lambda item: (-item["estimated_minutes"], item["id"])):
        index = 0 if totals[0] <= totals[1] else 1
        partitions[index].append(row)
        totals[index] += row["estimated_minutes"]
    for partition in partitions:
        partition.sort(key=lambda item: item["id"])
    return partitions[0], partitions[1]


def build_weeks(module: dict[str, Any], buckets: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    module_id = module["id"]
    weeks = CALENDAR[module_id]
    deep = len(weeks) == 6
    phases = [
        ("Model and derive", 510, "model"),
        ("Guided build and prediction freeze", 540, "build"),
        ("Independent build and integration", 600, "integrate"),
    ]
    if deep:
        phases.append(("Independent build and integration II", 600, "integrate"))
    phases.extend([
        ("Break, repair, measure, and diagnose", 600, "break"),
        ("Decide, teach, assess, and freeze", 570, "decide"),
    ])

    required_resources = [row for row in module.get("resources", []) if row.get("required")]
    res_a, res_b = split_weighted_rows(required_resources)
    resource_by_phase = {0: res_a, 1: res_b}
    lesson_a, lesson_b = split_rows(module["lesson_catalog"])
    lesson_by_phase = {0: lesson_a, 1: lesson_b}
    module_root = next(path.parent for path in (ROOT / "modules").glob("*/module.json") if json.loads(path.read_text())["id"] == module_id)
    exercises = re.findall(r"^## (EX-\d{2}):", (module_root / "exercises" / "exercises.md").read_text(encoding="utf-8"), re.MULTILINE)
    exercise_a, exercise_b = split_rows(exercises)
    exercise_by_phase = {0: exercise_a, 1: exercise_b}

    result: list[dict[str, Any]] = []
    used_integrate = False
    for index, (focus, target_minutes, bucket) in enumerate(phases):
        week_number = weeks[index]
        blocks: list[dict[str, Any]] = []
        block_index = 1

        def add_block(
            label: str,
            minutes: int,
            activity: str,
            *,
            required: bool = True,
            **extra: Any,
        ) -> None:
            nonlocal block_index
            if minutes <= 0:
                return
            block = {
                "id": f"W{week_number:03d}-T{block_index:02d}",
                "label": label,
                "minutes": minutes,
                "activity": activity,
                "required": required,
                **extra,
            }
            blocks.append(block)
            block_index += 1

        resources = resource_by_phase.get(index, [])
        if resources:
            for row in resources:
                row["week"] = week_number
            add_block(
                "Bounded authoritative resources",
                sum(int(row["estimated_minutes"]) for row in resources),
                "required_resource",
                resource_ids=[row["id"] for row in resources],
            )
        lessons = lesson_by_phase.get(index, [])
        if lessons:
            add_block(
                "Local mechanism instruction",
                sum(int(row["estimated_minutes"]) for row in lessons),
                "local_instruction",
                lesson_ids=[row["id"] for row in lessons],
            )
        exercises_for_week = exercise_by_phase.get(index, [])
        if exercises_for_week:
            add_block("Guided practice", 60, "guided_practice", exercise_ids=exercises_for_week)

        artifact_bucket = bucket
        if bucket == "integrate" and deep:
            artifact_rows = buckets[bucket] if not used_integrate else []
            used_integrate = True
        else:
            artifact_rows = buckets[bucket]
        if artifact_rows:
            allocations = [{"artifact_id": row["id"], "minutes": row["estimated_minutes"]} for row in artifact_rows]
            activity = {
                "model": "independent_work", "build": "independent_work", "integrate": "independent_work",
                "break": "failure_experiment", "decide": "decision_artifact",
            }[bucket]
            add_block(
                "Required evidence components",
                sum(row["minutes"] for row in allocations),
                activity,
                artifact_allocations=allocations,
            )

        consumed = sum(int(block["minutes"]) for block in blocks)
        remaining = target_minutes - consumed
        if remaining < 15:
            raise ValueError(f"{module_id} Week {week_number}: fixed work exceeds the phase budget")
        fill_activity = {
            "model": "independent_work", "build": "independent_work", "integrate": "independent_work",
            "break": "failure_experiment", "decide": "assessment",
        }[bucket]
        add_block(focus + " core work", remaining, fill_activity)
        if len(blocks) == 1:
            blocks[-1]["minutes"] -= 60
            add_block(focus + " verification checkpoint", 60, fill_activity)
        if bucket == "decide":
            # Preserve explicit teach-back and reflection without changing the total.
            blocks[-1]["minutes"] -= 60
            add_block("Module teach-back", 30, "teach_back")
            add_block("Learning log and freeze check", 30, "reflection")
        add_block(
            "Optional contingency capacity",
            12 * 60 - target_minutes,
            "contingency",
            required=False,
        )
        result.append({
            "number": week_number,
            "phase": focus,
            "focus": focus,
            "hours": target_minutes / 60,
            "core_hours": target_minutes / 60,
            "capacity_hours": 12,
            "evidence": [f"{focus} evidence frozen at source commit"],
            "time_blocks": blocks,
        })
    return result


def schedule_markdown(module: dict[str, Any]) -> str:
    lines = ["## Schedule", "", "The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately", "budgeted below that ceiling; unused time is recovery buffer, not hidden work.", ""]
    for week in module["weeks"]:
        lines.extend([
            f"### Week {week['number']}: {week['focus']} — {week['hours']:g} hours",
            "",
            "| Work | Time |",
            "|---|---:|",
        ])
        for block in week["time_blocks"]:
            if not block["required"]:
                continue
            lines.append(f"| {block['label']} | {block['minutes']} min |")
        contingency = sum(block["minutes"] for block in week["time_blocks"] if not block["required"])
        lines.append("")
        lines.append(
            f"Optional contingency capacity: {contingency} minutes. It is not core work, "
            "carries no required evidence, and may remain unused."
        )
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_schedule(readme: Path, module: dict[str, Any]) -> None:
    text = readme.read_text(encoding="utf-8")
    text = re.sub(
        r"^> \*\*Authoring status:\*\*.*?(?=\n\n)",
        "> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.",
        text,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )
    replacement = schedule_markdown(module)
    updated, count = re.subn(r"## Schedule\n.*?(?=\n## )", replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise ValueError(f"{readme}: schedule section not found")
    readme.write_text(updated, encoding="utf-8")


def rewrite_resources_guide(module_root: Path, module: dict[str, Any]) -> None:
    """Keep the learner-facing resource guide identical to the migrated manifest."""

    path = module_root / "resources.md"
    text = path.read_text(encoding="utf-8")
    required_by_week: dict[int, list[dict[str, Any]]] = {}
    for resource in module.get("resources", []):
        if resource.get("required"):
            required_by_week.setdefault(int(resource["week"]), []).append(resource)
    table_rows = []
    for week in sorted(required_by_week):
        rows = sorted(required_by_week[week], key=lambda row: row["id"])
        table_rows.append(
            f"| {week} | {', '.join(row['id'] for row in rows)} | "
            f"{sum(int(row['estimated_minutes']) for row in rows)} |"
        )
    table = (
        "| Week | Required resources | Assigned minutes |\n"
        "|---:|---|---:|\n" + "\n".join(table_rows)
    )
    required_ids = sorted(
        str(resource["id"]) for resource in module.get("resources", []) if resource.get("required")
    )
    text, count = re.subn(
        r"The required records are .*?\.\nEvery required record",
        f"The required records are {', '.join(required_ids)}.\nEvery required record",
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise ValueError(f"{path}: required-resource spine sentence not found")
    text, count = re.subn(
        r"\| Week \| Required resources \| Assigned minutes \|\n"
        r"\|---:\|---\|---:\|\n.*?(?=\n\nFor each assigned source)",
        table,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise ValueError(f"{path}: required-resource table not found")

    existing_ids = set(re.findall(r"^### (RES-\d{2}):", text, re.MULTILINE))
    v2_rows = [row for row in module.get("resources", []) if row["id"] not in existing_ids]
    if v2_rows:
        generated = ["## PESD 2.0 primary anchors", ""]
        for resource in sorted(v2_rows, key=lambda row: row["id"]):
            status = "Required" if resource["required"] else "Optional enrichment"
            allocation = "assigned" if resource["required"] else "optional"
            generated.extend([
                f"### {resource['id']}: {resource['title']}", "",
                f"- **Author/publisher:** {resource['author_or_publisher']}",
                f"- **URL:** {resource['url']}",
                f"- **Type/status:** {resource['type']}; {status}",
                f"- **Access:** {resource['access']}",
                f"- **Week/time:** Week {resource['week']}; {resource['estimated_minutes']} minutes {allocation}",
                f"- **Purpose:** {resource['purpose']}",
                f"- **Boundary and evidence:** {resource['assignment']}",
                f"- **Local alternative:** [{resource['text_alternative']}]({resource['text_alternative']})",
                f"- **Verification:** {resource.get('verification_status', 'verified')}; "
                f"{resource.get('verification_method', 'primary-source metadata comparison')}; "
                f"last checked {resource['last_verified']}",
                "- **Reflection:** Which obligation applies, which evidence proves its control, "
                "and what uncertainty or failure would reverse the decision?", "",
            ])
        replacement = "\n".join(generated).rstrip() + "\n"
        if "## PESD 2.0 primary anchors" in text:
            text = text.split("## PESD 2.0 primary anchors", 1)[0].rstrip() + "\n\n" + replacement
        else:
            text = text.rstrip() + "\n\n" + replacement

    for resource in module.get("resources", []):
        pattern = rf"(^### {re.escape(resource['id'])}:.*?^- \*\*Week/time:\*\* Week )\d+(; )\d+( minutes (?:assigned|optional))"
        replacement = rf"\g<1>{resource['week']}\g<2>{resource['estimated_minutes']}\g<3>"
        text, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE | re.DOTALL)
        if count != 1:
            raise ValueError(f"{path}: structured record for {resource['id']} not found")
    path.write_text(text, encoding="utf-8")


def rewrite_subsumed_evaluation_docs(module_root: Path, module_id: str) -> None:
    gate_number = (int(module_id[1:]) + 2) // 3
    gate_id = f"G{gate_number:02d}"
    boundary = (
        f"> **PESD 2.0 evaluation ownership:** {gate_id} invokes this module-specific "
        "rubric and evaluator exactly once as its domain score. Do not run or "
        "submit a separate module semantic evaluation report."
    )
    for relative in ("assessment/README.md", "assessment/evaluator-prompt.md"):
        path = module_root / relative
        text = path.read_text(encoding="utf-8")
        if boundary not in text:
            first, remainder = text.split("\n", 1)
            path.write_text(first + "\n\n" + boundary + "\n\n" + remainder.lstrip(), encoding="utf-8")
    report = module_root / "assessment" / "report-template.md"
    text = report.read_text(encoding="utf-8")
    text = re.sub(
        r"^# .+$",
        f"# {module_id} {gate_id} Domain Evaluation Record",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if boundary not in text:
        first, remainder = text.split("\n", 1)
        text = first + "\n\n" + boundary + "\n\n" + remainder.lstrip()
    report.write_text(text, encoding="utf-8")


def v2_extension(module_id: str) -> str:
    source_note = PRIMARY_SOURCE_NOTES.get(module_id, "Use the module's bounded primary sources and preserve the local evidence boundary.")
    return f"""
## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **{ADDITIONS[module_id]}**.

### Repeatable decision procedure

1. Inventory the affected data, tenants, identities, providers, jurisdictions,
   control planes, evidence owners, and cost owners before selecting a mechanism.
2. State the invariant and the authority that may change it. Separate a claimed
   policy from the enforcement point and from the evidence that proves execution.
3. Freeze a prediction, implement or model the named mechanism, and record the
   accepted evidence mode and runtime boundary.
4. Inject one policy, isolation, recovery, or supplier failure in addition to the
   module's mechanism failure. Preserve raw evidence before interpretation.
5. Compare at least two options across product outcome, technical mechanism,
   security and governance, operations and recovery, economics, ownership,
   migration, and reversal triggers.

### Non-capstone extension

Apply the procedure to the module's continuing case. Add one tenant or governed
data class, one supplier or control-plane dependency, and one deletion, recovery,
or exit obligation. The completed case may demonstrate the method, but its
topology, thresholds, policy choices, and answer are not defaults for Global
Commerce.

### Evidence boundary

Use `derived`, `executed_deterministic`, `measured_loopback`,
`measured_container`, `modeled_capacity`, `fixture_replay`, or
`measured_accelerator` exactly as defined by the course. Fixture replay supports
practice and remediation only. Modeled remote scale is not local measurement.
Every trial records commit and input/configuration hashes, runtime and resource
limits, clock, warm-up/repetition policy, raw outcomes, and limitations.

### Source boundary

{source_note}
"""


def migrate_module(module_path: Path) -> None:
    module = json.loads(module_path.read_text(encoding="utf-8"))
    module_id = module["id"]
    if module_id == "M09":
        module = json.loads(
            json.dumps(module).replace("Week 36 Gate 3", "Week 50 Gate 3")
        )
    module_root = module_path.parent
    add_v2_resources(module, module_root)
    removed = REMOVED_GATE_DUPLICATES.get(module_id, set())
    removed = set(removed) | {
        str(row.get("id")) for row in module.get("artifacts", [])
        if "remediation" in str(row.get("submission_path", "")).lower()
    }
    if removed:
        module["artifacts"] = [row for row in module["artifacts"] if row.get("id") not in removed]
        primary_id = PRIMARY[module_id][0]
        for outcome in module.get("outcomes", []):
            mapped = [primary_id if artifact in removed else artifact for artifact in outcome.get("artifacts", [])]
            outcome["artifacts"] = list(dict.fromkeys(mapped))
    module["course_id"] = "PESD-104"
    module["course_version"] = "2.0"
    module["status"] = "review"
    buckets = migrate_artifacts(module)
    module["weeks"] = build_weeks(module, buckets)
    for artifact in module.get("artifacts", []):
        if artifact.get("portfolio_category") == "learning_log":
            artifact["submission_path"] = (
                f"learning-log/week-{CALENDAR[module_id][0]:03d}.md through "
                f"learning-log/week-{CALENDAR[module_id][-1]:03d}.md"
            )
    for resource in module.get("resources", []):
        if resource["week"] not in CALENDAR[module_id]:
            # Optional enrichment remains discoverable without consuming core time.
            resource["week"] = CALENDAR[module_id][-1]
    module["target_hours"] = 57 if module_id in {"M10", "M17"} else 47
    module["primary_decision"] = {"artifact_id": PRIMARY[module_id][0], "type": PRIMARY[module_id][1].upper()}
    module["pesd_v2_additions"] = ADDITIONS[module_id]
    module["semantic_evaluation"] = "subsumed_by_gate" if module_id in {"M03", "M06", "M09", "M12", "M15", "M18"} else "module_specific"
    dump(module_path, module)
    rewrite_resources_guide(module_root, module)

    replace_schedule(module_root / "README.md", module)
    readme_note = f"""
## PESD 2.0 scope addition

This {len(module['weeks'])}-week module schedules {module['target_hours']} core hours. Its primary
decision is {PRIMARY[module_id][1].upper()} {PRIMARY[module_id][0]}. The added graded scope is
{ADDITIONS[module_id]}. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
"""
    append_once(module_root / "README.md", "## PESD 2.0 scope addition", readme_note)
    if module["semantic_evaluation"] == "subsumed_by_gate":
        rewrite_subsumed_evaluation_docs(module_root, module_id)
        gate_number = (int(module_id[1:]) + 2) // 3
        append_once(module_root / "README.md", "## PESD 2.0 evaluation ownership", f"""
## PESD 2.0 evaluation ownership

Gate G{gate_number:02d} invokes this module's rubric and provider-neutral
evaluator once for its domain score. Do not create a second module semantic
evaluation report. The gate result is authoritative; remediation remains a
separate dated artifact only for Revise or Repeat.
""")

    lesson8 = sorted((module_root / "lessons").glob("08-*.md"))
    if len(lesson8) != 1:
        raise ValueError(f"{module_id}: expected one Lesson 8")
    append_once(lesson8[0], "## PESD 2.0 extension: modern constraints and ownership", v2_extension(module_id))

    append_once(module_root / "exercises" / "exercises.md", "## PESD 2.0 extension to the final exercise", f"""
## PESD 2.0 extension to the final exercise

Extend the final guided exercise with {ADDITIONS[module_id]}. Produce an
obligation/control/evidence row, a named owner, a bounded cost or capacity
effect, a failure or policy-drift test, a migration step, and a reversal trigger.
Label every observation with an accepted evidence mode and do not use fixture
replay as independent Build, Break, Implement, or Measure evidence.
""")
    append_once(module_root / "exercises" / "answer-key.md", "## PESD 2.0 extension answer", f"""
## PESD 2.0 extension answer

A defensible answer covers {ADDITIONS[module_id]}. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
""")

    worksheets = sorted((module_root / "worksheets").glob("*.md"))
    if worksheets:
        append_once(worksheets[-1], "## PESD 2.0 decision and assurance check", f"""
## PESD 2.0 decision and assurance check

- Added scope: {ADDITIONS[module_id]}
- Requirement or obligation and applicability:
- Enforcement point and failure mode:
- Evidence owner, source commit, hashes, and evidence mode:
- Tenant/data/provider boundary:
- Cost allocation and operating owner:
- Migration, rollback, and decommissioning step:
- Uncertainty and reversal trigger:
""")

    append_once(module_root / "assessment" / "rubric.md", "## PESD 2.0 cross-cutting anchors", f"""
## PESD 2.0 cross-cutting anchors

Apply these anchors inside the published module-specific criteria; they do not
create a generic substitute rubric.

- **0–1:** ignores or merely names {ADDITIONS[module_id]} without an enforceable
  causal model, evidence boundary, or owner.
- **2:** covers the happy path but leaves a material tenant, governance,
  recovery, supplier, cost, migration, or evidence gap.
- **3:** connects the requirement to a mechanism, failure evidence, ownership,
  cost, migration, and a scoped residual risk.
- **4:** additionally tests policy drift or isolation failure, quantifies useful
  outcome and uncertainty, preserves lineage, and gives teachable reversal and
  decommissioning triggers.
""")
    append_once(module_root / "assessment" / "evaluator-prompt.md", "## PESD 2.0 evaluator instruction", f"""
## PESD 2.0 evaluator instruction

Score the published criteria against evidence for {ADDITIONS[module_id]}.
Classify missing evidence, incorrect reasoning, unsupported claims, and
reasonable uncertainty separately. Reject fixture replay presented as
independent build or break evidence. Do not invent legal applicability or treat
a named framework as proof of compliance.
""")
    append_once(module_root / "assessment" / "remediation-map.md", "## PESD 2.0 remediation", """
## PESD 2.0 remediation

When a cross-cutting floor is missed, return to Lesson 8's PESD 2.0 extension
and the final exercise. Create a separate dated revision containing the missing
requirement/control/evidence mapping, owner, evidence boundary, failure check,
cost consequence, migration, and reversal trigger. Never edit the frozen
baseline or raw trial. A Pass creates no required remediation artifact.
    """)
    if module_id in V2_RESOURCES:
        rows = "\n".join(
            f"- [{source['title']}]({source['url']}) — {source['publisher']}; required, free, 20 minutes; {source['boundary']} Local alternative: Lesson 8 PESD 2.0 extension. Last verified 2026-08-04."
            for source in V2_RESOURCES[module_id]
        )
        append_once(module_root / "resources.md", "## PESD 2.0 primary anchors", f"""
## PESD 2.0 primary anchors

{rows}

For each source, submit the named control/evidence mapping and applicability or
scope uncertainty. A framework name is not evidence of implementation or legal
compliance.
""")


def build_calendar() -> None:
    terms = [(1, 1, 17), (2, 18, 34), (3, 35, 51), (4, 52, 69), (5, 70, 86), (6, 87, 104)]
    gate_weeks = {16: "G01", 33: "G02", 50: "G03", 68: "G04", 85: "G05", 103: "G06"}
    flex_weeks = {17: "F01", 34: "F02", 51: "F03", 69: "F04", 86: "F05", 104: "F06"}
    module_by_week = {week: module for module, weeks in CALENDAR.items() for week in weeks}
    module_phase: dict[int, tuple[str, float]] = {}
    for module_path in sorted((ROOT / "modules").glob("*/module.json")):
        module = json.loads(module_path.read_text(encoding="utf-8"))
        for row in module["weeks"]:
            module_phase[row["number"]] = (row["phase"], row["core_hours"])
    rows = []
    for week in range(1, 105):
        term = next(number for number, start, end in terms if start <= week <= end)
        base = {"week": week, "term": term, "capacity_hours": 12}
        if week in module_by_week:
            owner = module_by_week[week]
            phase, core = module_phase[week]
            rows.append({**base, "type": "module", "core_hours": core, "phase": phase, "owner": owner, "module": owner})
        elif week in gate_weeks:
            owner = gate_weeks[week]
            rows.append({**base, "type": "gate", "core_hours": 9.5 if owner == "G06" else 6.5, "phase": "Standalone assessment gate", "owner": owner, "gate": owner})
        else:
            owner = flex_weeks[week]
            rows.append({**base, "type": "flex", "core_hours": 2, "phase": "Frozen capstone delta and next-term plan", "owner": owner, "flex": owner})
    dump(ROOT / "course-calendar.json", {
        "$schema": "schemas/course-calendar.schema.json",
        "course_id": "PESD-104", "version": "2.0",
        "capacity_hours_per_week": {"minimum": 10, "maximum": 12},
        "weeks": rows,
    })


def gate_assessment_brief(gate_id: str, week: int, modules: list[str], final: bool) -> str:
    current = ROOT / "gates" / gate_id / "assessment-brief.md"
    embedded = sorted((ROOT / "modules").glob(f"*/assessment/gate-{gate_id[1:]}.md"))
    if current.is_file() and not embedded:
        return current.read_text(encoding="utf-8")
    sources = {
        "G01": ROOT / "modules/03-computer-systems-operating-systems/assessment/gate-01.md",
        "G02": ROOT / "modules/06-deadlines-resilient-remote-calls/assessment/gate-02.md",
        "G03": ROOT / "modules/09-replication-partitioning/assessment/gate-03.md",
        "G04": ROOT / "modules/12-reliability-incidents-disaster-recovery/assessment/gate-04.md",
        "G05": ROOT / "modules/15-execution-models-across-languages/assessment/gate-05.md",
        "G06": ROOT / "modules/18-retrieval-rag-agents-capstone-defense/assessment/gate-06.md",
    }
    text = sources[gate_id].read_text(encoding="utf-8")
    text = re.sub(
        r"\n> \*\*PESD V1 historical contract:\*\*.*?\n\n",
        "\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(r"^# .+$", f"# {gate_id} Assessment Brief", text, count=1, flags=re.MULTILINE)
    text = text.replace("../../../SOLO_GATE_GUIDE.md", "../../SOLO_GATE_GUIDE.md")
    replacements = {
        "G01": {
            "[Week 12 Gate 1 revision](../../../capstone/revisions/week-12-gate-01.md)": "[Week 16 Gate 1 freeze](../../capstone/submissions/week-016-gate-01-freeze.md)",
            "Week 12 revision": "Week 17 delta", "Week 12": "Week 16",
            "ten minutes to present and twenty-five minutes to answer": "fifteen minutes to present and forty-five minutes to answer",
        },
        "G02": {"Complete `capstone/revisions/week-24-gate-02.md`": "After gate scoring, complete `capstone/revisions/week-034-delta.md`", "Week 24": "Week 34"},
        "G03": {"Gate 3 closes Week 36": "Gate 3 runs in Week 50", "capstone revision remains Week 48": "separate capstone delta is Week 51"},
        "G04": {"Gate 4 closes Week 48": "Gate 4 runs in Week 68", "the separately\nfrozen Week 48 capstone revision": "the Week 68 gate freeze; accepted findings belong in the later\nWeek 69 capstone delta"},
        "G05": {"Gate 5 closes Week 60": "Gate 5 runs in Week 85", "Gate 5 does not\ncreate a Week 60 capstone revision.": "Gate 5 freezes the Week 85 submission; the separate capstone delta is Week 86."},
        "G06": {
            "Week 1, 12, 24, 48, and 72 artifacts": "Week 1 baseline; Weeks 16, 33, 50, 68, 85, and 103 freezes; and separate flex-week deltas",
            "I01–I12 passing": "commerce C01–C10 and retrieval/agent AI01–AI12 passing",
        },
    }
    for old, new in replacements[gate_id].items():
        text = text.replace(old, new)
    for token, minutes in (
        ("Written examination", 90 if final else 75),
        ("practical", 180 if final else 150),
        ("Architecture defense", 120 if final else 60),
        ("Portfolio", 90 if final else 45),
    ):
        text = re.sub(
            rf"(## Part [^\n]*{re.escape(token)}[^\n]*?) — \d+ minutes",
            rf"\1 — {minutes} minutes",
            text,
            flags=re.IGNORECASE,
        )
    text = text.replace("Total learner time: 3.5 hours", "Scored-part time: 5.5 hours")
    result_heading = re.search(r"^## (?:Gate result algorithm|Result algorithm|Scoring|Result)\s*$", text, re.MULTILINE)
    if result_heading:
        text = text[:result_heading.start()].rstrip()
    result = """
## Result

Pass only when all structural gates, scored parts, three module-domain
subscores, safety-critical rows, and the overall average meet their published
floors. Revise applies only when evidence and chronology are complete and a
non-safety floor is missed. Repeat applies when an invariant fails, chronology
is invalid, evidence is fabricated or mismatched, or the causal model is
materially incorrect. A Pass creates no required remediation artifact.
"""
    if final:
        result += """
Gate 6 additionally requires a 3.5 overall and longitudinal-capstone score,
3.0 in every review dimension, and passing evidence for both C01–C10 and
AI01–AI12.
"""
    preamble = f"""
This is the learner-facing prompt set for the standalone Week {week} gate over
{', '.join(modules)}. The exact time boxes and hard floors in [gate.json](gate.json)
control. The 30-minute freeze and final scoring/closure block are managed from
the [gate overview](README.md); this brief contains the four scored parts.
"""
    return text.split("\n", 1)[0] + "\n\n" + preamble.strip() + "\n\n" + text.split("\n", 1)[1].lstrip() + "\n\n" + result.strip() + "\n"


def gate_assessor_guide(gate_id: str, modules: list[str]) -> str:
    current = ROOT / "gates" / gate_id / "assessor-guide.md"
    if current.is_file():
        return current.read_text(encoding="utf-8")
    source_paths = {
        "G02": ROOT / "modules/06-deadlines-resilient-remote-calls/assessment/gate-02-answer-key.md",
        "G03": ROOT / "modules/09-replication-partitioning/assessment/gate-03-answer-key.md",
        "G04": ROOT / "modules/12-reliability-incidents-disaster-recovery/assessment/gate-04-answer-key.md",
        "G05": ROOT / "modules/15-execution-models-across-languages/assessment/gate-05-answer-key.md",
        "G06": ROOT / "modules/18-retrieval-rag-agents-capstone-defense/assessment/gate-06-answer-key.md",
    }
    if gate_id == "G01":
        body = """## Review boundaries

- Credit competing causal models only when each predicts discriminating evidence.
- Keep buffered completion, durable acknowledgement, and recovery guarantees separate.
- Require container and host-controlled evidence boundaries for every systems claim.
- Accept different architecture decisions when the submitted workload, invariant,
  causal model, operations, cost, ownership, migration, and reversal evidence support them.
"""
    else:
        body = source_paths[gate_id].read_text(encoding="utf-8")
        body = re.sub(
            r"\n> \*\*PESD V1 historical contract:\*\*.*?\n\n", "\n", body,
            flags=re.DOTALL,
        )
        body = re.sub(r"^# .+$", "## Review boundaries", body, count=1, flags=re.MULTILINE)
        replacements = {
            "G02": {"Week 24 revision": "Week 34 delta"},
            "G03": {},
            "G04": {"Week 48 revision": "Week 68 freeze and later Week 69 delta"},
            "G05": {},
            "G06": {"Week 1, 12, 24, 48, and 72 artifacts": "Week 1 baseline, all six gate freezes, and all six flex-week deltas"},
        }
        for old, new in replacements[gate_id].items():
            body = body.replace(old, new)
    return f"""# {gate_id} Assessor Guide

Use this guide only after the learner freezes every submitted part. Score only
the published module rubrics and evidence for {', '.join(modules)}. Cite a file
and heading for every finding, preserve reasonable alternatives, and recommend
remediation without drafting replacement graded answers. A Pass creates no
required remediation artifact.

{body.lstrip()}"""


def build_gates() -> None:
    gate_root = ROOT / "gates"
    gate_root.mkdir(exist_ok=True)
    groups = {
        "G01": (16, ["M01", "M02", "M03"]), "G02": (33, ["M04", "M05", "M06"]),
        "G03": (50, ["M07", "M08", "M09"]), "G04": (68, ["M10", "M11", "M12"]),
        "G05": (85, ["M13", "M14", "M15"]), "G06": (103, ["M16", "M17", "M18"]),
    }
    normal_parts = [("freeze", "Evidence freeze", 30, 0), ("written", "Written examination", 75, 3),
                    ("practical", "Hidden practical", 150, 3), ("defense", "Architecture defense", 60, 3),
                    ("portfolio", "Portfolio review", 45, 3), ("closure", "Scoring and feedback review", 30, 0)]
    final_parts = [("freeze", "Final evidence freeze", 30, 0), ("written", "Written examination", 90, 3),
                   ("practical", "Hidden practical", 180, 3), ("defense", "Architecture defense", 120, 3),
                   ("portfolio", "Longitudinal portfolio review", 90, 3), ("closure", "Scoring and closure", 60, 0)]
    rubric = [
        ("GR01", "Product and user outcome", False), ("GR02", "Technical causal model", False),
        ("GR03", "Security and governance", True), ("GR04", "Operations and recovery", True),
        ("GR05", "Economics and capacity", False), ("GR06", "Ownership, migration, and teaching", False),
    ]
    for gate_id, (week, modules) in groups.items():
        final = gate_id == "G06"
        parts = final_parts if final else normal_parts
        manifest = {
            "$schema": "../../schemas/gate.schema.json", "id": gate_id, "week": week, "modules": modules,
            "core_minutes": sum(row[2] for row in parts),
            "parts": [{"id": pid, "title": title, "minutes": minutes, "minimum_score": floor,
                       "new_teaching": False, "new_build_work": False} for pid, title, minutes, floor in parts],
            "domain_matrix": [{"module": module, "criteria": ["module_specific_rubric"], "minimum_score": 3} for module in modules],
            "rubric_rows": [{"id": rid, "title": title, "safety_critical": safety} for rid, title, safety in rubric],
            "hard_floors": {"part": 3, "domain": 3, "safety": 3, "overall": 3.5 if final else 3},
            "invariant_sets": [],
            "result_rules": {
                "Pass": "All structural, scored-part, domain, safety, invariant, and average floors pass.",
                "Revise": "Evidence is complete, chronology is valid, and only one or more non-safety scoring floors are missed.",
                "Repeat": "An invariant fails, chronology is invalid, evidence is fabricated or mismatched, or the causal model is materially incorrect.",
            },
            "remediation_reserve_hours": 6,
            "pass_remediation_required": False,
        }
        if final:
            manifest["hard_floors"]["longitudinal_capstone"] = 3.5
            manifest["hard_floors"]["review_dimensions"] = {
                "product": 3, "technical": 3, "security_governance": 3,
                "operations_recovery": 3, "economics": 3, "ownership_migration": 3,
            }
            manifest["invariant_sets"] = [
                {"id": "commerce", "invariants": [f"C{i:02d}" for i in range(1, 11)], "required_to_pass": True},
                {"id": "retrieval_agent", "invariants": [f"AI{i:02d}" for i in range(1, 13)], "required_to_pass": True},
            ]
        destination = gate_root / gate_id
        destination.mkdir(exist_ok=True)
        dump(destination / "gate.json", manifest)
        (destination / "assessment-brief.md").write_text(
            gate_assessment_brief(gate_id, week, modules, final), encoding="utf-8"
        )
        (destination / "assessor-guide.md").write_text(
            gate_assessor_guide(gate_id, modules), encoding="utf-8"
        )
        schedule = "\n".join(f"| {title} | {minutes} min |" for _, title, minutes, _ in parts)
        (destination / "README.md").write_text(f"""# {gate_id}: Standalone Course Gate

Week {week} assesses Modules {', '.join(modules)}. It contains no new required
teaching or build work. Freeze the submitted commit before opening the hidden
practical or defense prompts.

Use the [assessment brief](assessment-brief.md) for the written, practical,
defense, and portfolio prompts. After freezing, use the
[assessor guide](assessor-guide.md) for explained reasoning boundaries. The hidden practical is selected through the
[sealed-local gate workflow](../../SOLO_GATE_GUIDE.md).

| Part | Time |
|---|---:|
{schedule}

Each scored part, each module-domain subscore, and each safety-critical row must
score at least 3.0. The overall floor is {'3.5' if final else '3.0'}.
Pass, Revise, and Repeat follow `gate.json`; a Pass creates no required
remediation artifact. A Revise may use at most six hours in the following flex
week. More work pauses the calendar.
""", encoding="utf-8")


def build_portfolio() -> None:
    title_by_category = {
        "adr": "Architecture decision", "rfc": "Request for comments",
        "capacity_cost_model": "Capacity and cost model", "performance_investigation": "Performance investigation",
        "controlled_incident_postmortem": "Controlled incident postmortem", "failure_matrix": "Featured failure matrix",
        "source_code_internals_review": "Internals review", "runtime_comparison": "Runtime comparison",
        "threat_model": "Threat model lineage", "dr_exercise": "Disaster recovery exercise",
        "migration_plan": "Migration plan", "data_governance_dossier": "Data Governance Dossier",
        "assurance_case": "Assurance Case", "platform_product_experiment": "Platform Product Experiment",
        "ai_system_dossier": "AI System Dossier",
    }
    items: list[dict[str, Any]] = []
    for module, (artifact, category) in PRIMARY.items():
        item_id = f"PI-DECISION-{module}"
        items.append({"id": item_id, "title": f"{module} {title_by_category[category]}", "category": category,
                      "evidence_lineage_id": f"LIN-DECISION-{module}",
                      "components": [{"owner": module, "artifact": artifact, "role": "decision"}],
                      "credit_component": f"{module}:{artifact}"})
    grouped: dict[str, dict[str, Any]] = {}
    for (module, artifact), (item_id, lineage, category) in FEATURES.items():
        grouped[item_id] = {"id": item_id, "title": title_by_category[category], "category": category,
                            "evidence_lineage_id": lineage, "components": [], "credit_component": f"{module}:{artifact}"}
        grouped[item_id]["components"].append({"owner": module, "artifact": artifact, "role": "final" if (module, artifact) in {("M18", "A03"), ("M18", "A07")} else "analysis"})
    for (module, artifact), (item_id, _) in BASELINE_COMPONENTS.items():
        grouped[item_id]["components"].insert(0, {"owner": module, "artifact": artifact, "role": "baseline"})
    items.extend(grouped[key] for key in sorted(grouped))
    for number in range(1, 7):
        gate = f"G{number:02d}"
        items.append({"id": f"PI-TEACH-{number:02d}", "title": f"{gate} recorded teach-back", "category": "teach_back",
                      "evidence_lineage_id": f"LIN-TEACH-{number:02d}",
                      "components": [{"owner": gate, "artifact": "recorded-defense", "role": "final"}],
                      "credit_component": f"{gate}:recorded-defense"})
    capstone_components = [{"owner": "M01", "artifact": "A01", "role": "baseline"}]
    for number, flex in enumerate((17, 34, 51, 69, 86, 104), start=1):
        capstone_components.append({"owner": f"F{number:02d}", "artifact": f"week-{flex:03d}-delta", "role": "final" if flex == 104 else "revision"})
    items.append({"id": "PI-CAPSTONE-01", "title": "Global Commerce capstone lineage", "category": "capstone",
                  "evidence_lineage_id": "LIN-CAPSTONE-GLOBAL-COMMERCE", "components": capstone_components,
                  "credit_component": "F06:week-104-delta"})
    dump(ROOT / "portfolio-items.json", {"$schema": "schemas/portfolio-items.schema.json", "course_id": "PESD-104", "version": "2.0", "items": items})


def build_capstone_chronology() -> None:
    submissions = ROOT / "capstone" / "submissions"
    revisions = ROOT / "capstone" / "revisions"
    submissions.mkdir(exist_ok=True)
    revisions.mkdir(exist_ok=True)
    gate_weeks = (16, 33, 50, 68, 85, 103)
    flex_weeks = (17, 34, 51, 69, 86, 104)
    for gate, (gate_week, flex_week) in enumerate(zip(gate_weeks, flex_weeks), start=1):
        freeze = submissions / f"week-{gate_week:03d}-gate-{gate:02d}-freeze.md"
        freeze.write_text(f"""# Week {gate_week} Gate {gate} Capstone Freeze

This file records the commit, hashes, and evidence index submitted to Gate {gate}.
After the gate begins, **never edit this file or any referenced frozen artifact**.
Corrections belong in separate artifacts, beginning with the Week {flex_week} delta.

## Frozen identity

- Source commit:
- Submitted artifact hashes:
- Gate challenge identity:
- Runtime and evaluator versions:
- AI-assistance disclosure:

## Commerce invariants C01–C10

For each invariant, cite the submitted file and heading, enforcement mechanism,
failure evidence, owner, and unresolved uncertainty.

## Domain evidence index

| Module domain | Submitted file and heading | Component role | Evidence mode | Hash |
|---|---|---|---|---|

## Known limitations

Record uncertainty and missing evidence without repairing the frozen submission.
""", encoding="utf-8")
        delta = revisions / f"week-{flex_week:03d}-delta.md"
        delta.write_text(f"""# Week {flex_week} Frozen Capstone Delta

Do not edit the Week {gate_week} Gate {gate} freeze or any earlier baseline,
experiment, gate submission, or revision. This file is a separate delta.

The normal required budget is at most two hours: record accepted findings,
changed decisions, and the next-term plan. A **Revise** may use up to six hours.
If more work is required, pause the course calendar; do not spill remediation
into the next module. Optional studio work does not affect completion.

## Findings accepted, disputed, or deferred

| Finding | Classification | Evidence citation | Decision | Owner |
|---|---|---|---|---|

## Delta only

List changed assumptions, controls, interfaces, ownership, cost, migration,
recovery, or AI assurance. Link to new artifacts; do not copy or rewrite history.

## Next-term plan

- Evidence gaps to close:
- Assumptions to re-test:
- Ownership or stakeholder work:
- Scheduled bridge pack, if migrating from V1:
""", encoding="utf-8")


def rewrite_current_pacing_references() -> None:
    replacements: dict[str, list[tuple[str, str]]] = {
        "modules/01-architectural-judgment/README.md": [
            ("This four-week module", "This five-week module"),
            ("Week 4 revision log", "dated post-assessment revision log"),
        ],
        "modules/02-capacity-queues-tail-latency/assessment/README.md": [
            ("Weeks 5–8 learning logs", "Weeks 6–10 learning logs"),
        ],
        "modules/03-computer-systems-operating-systems/README.md": [
            ("[Gate 1](assessment/gate-01.md)", "[Gate 1](../../gates/G01/assessment-brief.md)"),
            ("[Week 12 revision](../../capstone/revisions/week-12-gate-01.md)", "[Week 17 delta](../../capstone/revisions/week-017-delta.md)"),
        ],
        "modules/03-computer-systems-operating-systems/assessment/README.md": [
            ("[Gate 1](gate-01.md)", "[Gate 1](../../../gates/G01/assessment-brief.md)"),
            ("Frozen Week 9 benchmark prediction", "Frozen Week 12 benchmark prediction"),
            ("Weeks 9–12 learning logs", "Weeks 11–15 learning logs"),
        ],
        "modules/06-deadlines-resilient-remote-calls/README.md": [
            ("teach-back, and the Week 24 Gate 2 revision to the portfolio.", "teach-back, the Week 33 Gate 2 freeze, and the separate Week 34 capstone delta to the portfolio lineage."),
            ("Complete the four-part [Gate 2 assessment](assessment/gate-02.md), then use\n  the [assessor notes](assessment/gate-02-answer-key.md) after freezing it.", "Complete the standalone [Gate 2 assessment](../../gates/G02/assessment-brief.md) in Week 33 after freezing Module 6 evidence."),
        ],
        "modules/09-replication-partitioning/README.md": [
            ("Defend a Week 36 Gate 3 invariant", "Defend a Week 50 Gate 3 invariant"),
            ("[Gate 3](assessment/gate-03.md)", "[Gate 3](../../gates/G03/assessment-brief.md)"),
            ("The next planned\n  capstone revision remains Week 48.", "Accepted Gate 3 findings belong in the separate Week 51 capstone delta."),
        ],
        "modules/10-time-coordination-consensus/README.md": [
            ("A preserved Week 36 commerce replication/partitioning decision", "The preserved Week 50 Gate 3 freeze and Week 51 commerce delta"),
            ("Week 48 after Modules 10–12", "Week 68 after Modules 10–12"),
        ],
        "modules/11-messaging-streams-workflows/README.md": [
            ("Week 48 after Module 12", "Week 68 after Module 12"),
        ],
        "modules/12-reliability-incidents-disaster-recovery/README.md": [
            ("one Week 48 capstone revision", "one Week 68 gate freeze and separate Week 69 capstone delta"),
            ("[Gate 4](assessment/gate-04.md)", "[Gate 4](../../gates/G04/assessment-brief.md)"),
            ("the Week 48 capstone revision separately", "the Week 68 gate freeze and Week 69 capstone delta separately"),
        ],
        "modules/12-reliability-incidents-disaster-recovery/assessment/README.md": [
            ("Gate 4 parts and the separate Week 48 revision", "Gate 4 Week 68 parts and the separate Week 69 delta"),
        ],
        "modules/12-reliability-incidents-disaster-recovery/worksheets/week-48-reliability-decision-gate-04.md": [
            ("Run the module evaluator after freezing A01–A08. Revise only in dated addenda;\nRepeat uses new seeds.", "Gate 4 invokes the Module 12 evaluator once for its domain score after A01–A08 are frozen. Do not create a duplicate module evaluation report. Revise only in dated addenda; Repeat uses new seeds."),
        ],
        "modules/12-reliability-incidents-disaster-recovery/lessons/08-game-days-reliability-decisions.md": [
            ("freeze Gate 4, and write the separate Week 48 capstone revision", "freeze Gate 4 in Week 68, and write the separate Week 69 capstone delta"),
        ],
        "modules/10-time-coordination-consensus/assessment/semantic-readiness-review.md": [
            ("Gate 4 remains at Week 48", "Gate 4 runs in Week 68"),
        ],
        "modules/11-messaging-streams-workflows/assessment/semantic-readiness-review.md": [
            ("No Gate 4 or Week 48 capstone answer is exposed.", "No Gate 4 or Week 69 capstone-delta answer is exposed."),
        ],
        "modules/13-security-privacy-abuse-resistance/README.md": [
            ("Preserved Week 1 baseline and Week 48 revision", "Preserved Week 1 baseline, Week 68 Gate 4 freeze, and Week 69 delta"),
            ("Gate 5 remains at Week 60", "Gate 5 runs in Week 85"),
        ],
        "modules/13-security-privacy-abuse-resistance/assessment/README.md": [
            ("Week 49 predictions", "Week 71 predictions"),
        ],
        "modules/14-architecture-evolution-economics-organization/README.md": [
            ("Preserved Week 1 baseline and Week 48 revision", "Preserved Week 1 baseline, Week 68 Gate 4 freeze, and Week 69 delta"),
            ("Gate 5 remains at Week 60. Week 56 does not create or edit a capstone gate\n  revision; Module 14 evidence feeds the later assessment.", "Gate 5 runs in Week 85. Module 14 evidence feeds that later assessment; accepted findings belong in the separate Week 86 delta."),
        ],
        "modules/14-architecture-evolution-economics-organization/assessment/README.md": [
            ("Week 53 baseline", "Week 76 baseline"),
        ],
        "modules/15-execution-models-across-languages/README.md": [
            ("[Gate 5](assessment/gate-05.md)", "[Gate 5](../../gates/G05/assessment-brief.md)"),
            ("It does not create a Week 60 capstone revision.", "The Week 85 gate freeze remains immutable; accepted findings belong in the separate Week 86 delta."),
        ],
        "modules/15-execution-models-across-languages/assessment/README.md": [
            ("The Week 57 baseline", "The Week 81 baseline"),
        ],
        "modules/15-execution-models-across-languages/worksheets/week-60-runtime-decision-gate-05.md": [
            ("Freeze the module submission, run the evaluator, preserve its output, and create\na separate remediation revision. Then complete", "Freeze the module submission. Gate 5 invokes the Module 15 evaluator once for its domain score; do not create a duplicate module evaluation report. Preserve the gate output and create a separate remediation revision only when required. Then complete"),
        ],
        "modules/15-execution-models-across-languages/lessons/08-runtime-decision-teach-back.md": [
            ("[Gate 5](../assessment/gate-05.md)", "[Gate 5](../../../gates/G05/assessment-brief.md)"),
        ],
        "modules/16-browser-frontend-cdn-edge/README.md": [
            ("Gate 6 occurs in Week 72 after Modules 17–18; Module 16 creates no gate submission.", "Gate 6 runs in Week 103 after Modules 17–18; Module 16 evidence is frozen there but creates no duplicate module gate submission."),
        ],
        "modules/17-model-foundations-inference-systems/README.md": [
            ("Gate 6 occurs in Week 72 after Module 18; Module 17 creates inputs but no final\n  capstone defense submission.", "Gate 6 runs in Week 103 after Module 18; Module 17 creates inputs but no duplicate final capstone defense submission."),
        ],
        "modules/18-retrieval-rag-agents-capstone-defense/README.md": [
            ("Frozen Week 1 baseline, Week 12/24/48 revisions, Gate 5 evidence, and\n  independent Module 16–17 capstone evidence", "Frozen Week 1 baseline; Gate freezes from Weeks 16, 33, 50, 68, and 85; their separate flex-week deltas; and independent Module 16–17 evidence"),
            ("[Gate 6 contract](assessment/gate-06.md)", "[Gate 6 contract](../../gates/G06/assessment-brief.md)"),
            ("every A01–A17 artifact", "every required artifact in `module.json`"),
            ("no failed capstone invariant, and no safety-critical zero", "passing C01–C10 and AI01–AI12 evidence, and at least 3.0 in every safety-critical dimension"),
        ],
        "modules/18-retrieval-rag-agents-capstone-defense/assessment/README.md": [
            ("A01–A17 and Weeks 69–72 logs", "Every required manifest artifact and Weeks 98–102 logs"),
            ("The Week 72 artifact cites but does not alter Week 1, 12, 24, or 48 evidence.", "The Week 103 freeze cites but does not alter the Week 1 baseline or any earlier freeze and delta."),
            ("Gate 6 submission, Week 72 revision, evaluation, separate remediation", "Week 103 Gate 6 freeze, separate Week 104 final delta, evaluation, remediation when required"),
            ("A01–A17, average", "every required manifest artifact, average"),
            ("no zero in R04–R07", "at least 3.0 in R04–R07"),
        ],
        "modules/18-retrieval-rag-agents-capstone-defense/lessons/08-civicaid-capstone-defense.md": [
            ("Build the Week 72 revision as a new artifact that cites the Week 1, 12, 24, and 48 baselines", "Build the Week 104 final delta as a new artifact that cites the Week 1 baseline and every Week 16–103 freeze and flex-week delta"),
            ("the Week 72 worksheet, and the Gate 6 submission. Use [week-72-final.md](../../../capstone/revisions/week-72-final.md) only as a new revision contract.", "the final worksheet, and the Week 103 Gate 6 submission. Use [week-104-delta.md](../../../capstone/revisions/week-104-delta.md) only after the Gate 6 freeze as a new final-delta contract."),
        ],
        "modules/18-retrieval-rag-agents-capstone-defense/worksheets/week-72-capstone-defense.md": [
            ("Link Gate 6, module evaluation, separate remediation artifact, and reassessment result.", "Link the single Gate 6 Module 18 domain evaluation, any required separate remediation artifact, and the reassessment result. Do not create a duplicate module evaluation report."),
        ],
    }
    for relative, pairs in replacements.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        for old, new in pairs:
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def migrate_m18_invariant_names() -> None:
    root = ROOT / "modules/18-retrieval-rag-agents-capstone-defense"
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".json", ".py"} or "legacy" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        migrated = re.sub(r"(?<![A-Z])I(0[1-9]|1[0-2])\b", r"AI\1", text)
        if migrated != text:
            path.write_text(migrated, encoding="utf-8")


def mark_v1_evidence() -> None:
    paths = [
        *(ROOT / "modules").glob("*/assessment/gate-*.md"),
        ROOT / "capstone/revisions/week-12-gate-01.md",
        ROOT / "capstone/revisions/week-24-gate-02.md",
        ROOT / "capstone/revisions/week-48-gate-04.md",
        ROOT / "capstone/revisions/week-72-final.md",
    ]
    marker = "PESD V1 historical contract:"
    for path in paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if marker in text:
            if "capstone" in path.parts:
                text = re.sub(
                    r"PESD 2\.0 uses \[gates/G0[1-6]/README\.md\]\(\.\./\.\./\.\./gates/G0[1-6]/README\.md\)\.",
                    "PESD 2.0 uses [V1_TO_V2_MIGRATION.md](../../V1_TO_V2_MIGRATION.md).",
                    text,
                )
                path.write_text(text, encoding="utf-8")
            continue
        first, remainder = text.split("\n", 1)
        gate_match = re.search(r"gate-(0[1-6])", path.name)
        if gate_match and "modules" in path.parts:
            current = f"gates/G{gate_match.group(1)}/README.md"
            link = f"../../../{current}"
        else:
            current = "V1_TO_V2_MIGRATION.md"
            link = f"../../{current}"
        banner = (
            f"> **{marker}** Preserve this file for V1 learners and immutable evidence. "
            f"PESD 2.0 uses [{current}]({link}).\n"
        )
        path.write_text(first + "\n\n" + banner + "\n" + remainder.lstrip(), encoding="utf-8")


def retire_embedded_v1_gates() -> None:
    """The V1 tag preserves these files; PESD 2.0 owns only top-level gates."""

    for path in sorted((ROOT / "modules").glob("*/assessment/gate-*.md")):
        path.unlink()


def supersede_pre_v2_readiness_reviews() -> None:
    banner = (
        "> **PESD 2.0 status: Review.** This pre-migration readiness record is "
        "historical, not a current Ready decision. Fresh evaluator repetitions, "
        "platform/offline/cleanup matrices, and timed learner pilots remain pending."
    )
    for path in sorted((ROOT / "modules").glob("*/assessment/*readiness-review.md")):
        text = path.read_text(encoding="utf-8")
        if banner not in text:
            first, remainder = text.split("\n", 1)
            text = first + "\n\n" + banner + "\n\n" + remainder.lstrip()
        text = text.replace("Current decision: **Ready**", "Historical decision (superseded): **Ready**")
        text = text.replace("## Current status: ready", "## Historical status (superseded): ready")
        text = text.replace("- Final result: ready.", "- Historical final result (superseded): ready.")
        text = re.sub(
            r"## Result\n\n(\*\*Ready on [^\n]+\*\*)",
            r"## Historical result (superseded)\n\n\1",
            text,
        )
        text = text.replace("the module is ready for learners", "the historical review found the module ready for learners")
        text = text.replace("The module is ready within", "The historical review found the module ready within")
        path.write_text(text, encoding="utf-8")


def main() -> int:
    module_paths = sorted((ROOT / "modules").glob("*/module.json"))
    if len(module_paths) != 18:
        raise ValueError(f"expected 18 modules, found {len(module_paths)}")
    for module_path in module_paths:
        migrate_module(module_path)
        print(f"migrated {module_path.parent.name}")
    rewrite_current_pacing_references()
    build_calendar()
    build_gates()
    build_portfolio()
    build_capstone_chronology()
    migrate_m18_invariant_names()
    mark_v1_evidence()
    retire_embedded_v1_gates()
    supersede_pre_v2_readiness_reviews()
    print("generated calendar, gates, and portfolio registry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
