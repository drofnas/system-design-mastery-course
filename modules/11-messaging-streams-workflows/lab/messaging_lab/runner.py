"""Run deterministic SQLite-backed messaging failure experiments."""

from __future__ import annotations

import hashlib
import json
import sqlite3
import tempfile
from pathlib import Path
from typing import Any


INVARIANT_NAMES = {
    "I01": "authority and outbox commit atomically",
    "I02": "committed publication is published or visibly pending",
    "I03": "one event identity applies once per consumer",
    "I04": "one effect identity causes at most one irreversible effect",
    "I05": "derived aggregate version never regresses",
    "I06": "consumer progress advances only after apply or quarantine",
    "I07": "poison handling bounds attempts and preserves ownership",
    "I08": "backlog and recovery work remain bounded",
    "I09": "workflow follows durable valid transitions",
    "I10": "compensation is idempotent and auditable",
    "I11": "late data follows the declared event-time policy",
    "I12": "reconciliation restores derived state from authority",
}


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def setup_authority(path: Path) -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.executescript(
        "CREATE TABLE observations(id TEXT PRIMARY KEY, version INTEGER NOT NULL);"
        "CREATE TABLE outbox(event_id TEXT PRIMARY KEY, aggregate_id TEXT NOT NULL, "
        "version INTEGER NOT NULL, published INTEGER NOT NULL DEFAULT 0);"
    )
    return db


def setup_consumer(path: Path) -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.executescript(
        "CREATE TABLE inbox(consumer TEXT NOT NULL, event_id TEXT NOT NULL, "
        "PRIMARY KEY(consumer,event_id));"
        "CREATE TABLE projection(aggregate_id TEXT PRIMARY KEY, version INTEGER NOT NULL);"
    )
    return db


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    workload = scenario["workload"]
    controls = scenario["controls"]
    pair = scenario["pair_id"]
    aggregate = workload["aggregate_id"]
    event_id = workload["event_id"]
    version = int(workload["aggregate_version"])
    results = {key: True for key in INVARIANT_NAMES}

    with tempfile.TemporaryDirectory(prefix="m11-messaging-") as temp:
        root = Path(temp)
        authority_db = setup_authority(root / "authority.sqlite")
        consumer_db = setup_consumer(root / "consumer.sqlite")

        if pair == "F01" and not controls["atomic_outbox"]:
            authority_db.execute("INSERT INTO observations VALUES (?,?)", (aggregate, version))
            authority_db.commit()
            results["I01"] = False
        else:
            with authority_db:
                authority_db.execute("INSERT INTO observations VALUES (?,?)", (aggregate, version))
                authority_db.execute("INSERT INTO outbox VALUES (?,?,?,0)", (event_id, aggregate, version))

        facts = [dict(id=row[0], version=row[1]) for row in authority_db.execute("SELECT id,version FROM observations")]
        outbox_rows = [dict(event_id=row[0], aggregate_id=row[1], version=row[2], published=bool(row[3])) for row in authority_db.execute("SELECT event_id,aggregate_id,version,published FROM outbox")]
        broker_records = [dict(position=index, event_id=row["event_id"], aggregate_id=aggregate, version=version) for index, row in enumerate(outbox_rows)]

        if pair == "F02":
            broker_records = [
                {"position": 0, "event_id": event_id, "aggregate_id": aggregate, "version": version},
                {"position": 1, "event_id": event_id, "aggregate_id": aggregate, "version": version},
            ]
        if outbox_rows:
            authority_db.execute("UPDATE outbox SET published=1")
            authority_db.commit()
        pending = sum(1 for row in outbox_rows if not row["published"])
        published = len(outbox_rows)
        results["I02"] = bool(outbox_rows) or not facts

        applications = 0
        inbox_ids: list[str] = []
        projection_version = int(scenario["initial_state"]["projection_version"])
        for record in broker_records:
            should_apply = True
            if controls["inbox_deduplication"]:
                try:
                    consumer_db.execute("INSERT INTO inbox VALUES (?,?)", ("catalog", record["event_id"]))
                    consumer_db.commit()
                except sqlite3.IntegrityError:
                    should_apply = False
            if should_apply:
                applications += 1
                if controls["enforce_versions"]:
                    projection_version = max(projection_version, int(record["version"]))
                else:
                    projection_version = int(record["version"])
        inbox_ids = [row[0] for row in consumer_db.execute("SELECT event_id FROM inbox ORDER BY event_id")]
        if pair == "F02" and not controls["inbox_deduplication"]:
            results["I03"] = False

        effect_count = 1
        if pair == "F03" and not controls["effect_idempotency"]:
            effect_count = 2
            results["I04"] = False

        if pair == "F04":
            ordered_versions = [version, version - 1]
            projection_version = int(scenario["initial_state"]["projection_version"])
            for candidate in ordered_versions:
                projection_version = max(projection_version, candidate) if controls["enforce_versions"] else candidate
            if not controls["enforce_versions"]:
                results["I05"] = False

        attempts = 1
        dead_letters: list[dict[str, Any]] = []
        offset = len(broker_records)
        if pair == "F05":
            if controls["quarantine_poison"]:
                attempts = 3
                dead_letters.append({"event_id": event_id, "attempts": 3, "owner": "publication-team", "reason": "unsupported-schema"})
            else:
                attempts = 8
                offset = 0
                results["I07"] = False

        backlog_start = int(workload["backlog"])
        backlog_end = max(0, backlog_start - max(0, int(workload["service_rate"]) - int(workload["arrival_rate"])) * 5)
        oldest_age = 300
        if pair == "F06" and not controls["bounded_recovery"]:
            backlog_end = backlog_start + int(workload["arrival_rate"]) * 5
            oldest_age = 600
            results["I08"] = False

        workflow_state = "published"
        workflow_history = ["validated", "cataloged", "bulletin_pending", "published"]
        compensation_effects = 1
        if pair == "F07" and not controls["durable_workflow"]:
            workflow_state = "unknown"
            workflow_history = ["validated", "cataloged", "crash", "cataloged"]
            compensation_effects = 2
            results["I09"] = False
            results["I10"] = False

        late_action = "on-time"
        corrections = 0
        if pair == "F08":
            if controls["late_data_policy"] == "correct":
                late_action = "versioned-correction"
                corrections = 1
            else:
                late_action = "silent-drop"
                results["I11"] = False

        before = {"authority_version": version, "projection_version": projection_version}
        repairs: list[dict[str, Any]] = []
        if pair == "F09":
            projection_version = version - 1
            before["projection_version"] = projection_version
            if controls["reconcile_derived"]:
                repairs.append({"aggregate_id": aggregate, "from": projection_version, "to": version})
                projection_version = version
            else:
                results["I12"] = False
        after = {"authority_version": version, "projection_version": projection_version}

        if pair == "F01" and not outbox_rows:
            results["I02"] = False
        event_ids = [row["event_id"] for row in broker_records]
        results["I03"] = results["I03"] and applications <= 1
        results["I04"] = results["I04"] and effect_count <= 1
        results["I05"] = results["I05"] and projection_version >= min(version, int(scenario["initial_state"]["projection_version"]))
        results["I06"] = offset >= len(broker_records) or bool(dead_letters) or pair == "F05"
        results["I10"] = results["I10"] and compensation_effects <= 1
        results["I12"] = results["I12"] and after["projection_version"] == after["authority_version"]

        invariant_rows = [
            {"id": key, "name": INVARIANT_NAMES[key], "passed": results[key], "evidence": f"{key}={str(results[key]).lower()} for {pair}"}
            for key in sorted(INVARIANT_NAMES)
        ]
        trial = {
            "schema_version": "1.0",
            "scenario_id": scenario["scenario_id"],
            "pair_id": pair,
            "variant": scenario["variant"],
            "seed": scenario["seed"],
            "scenario_sha256": digest(scenario),
            "shared_input_sha256": digest({key: scenario[key] for key in ("seed", "workload", "initial_state", "events")}),
            "config_sha256": digest(controls),
            "authority": {"database": "temporary-sqlite", "facts": facts, "version": version},
            "outbox": {"rows": outbox_rows, "pending": pending, "published": published},
            "broker": {"records": broker_records, "duplicates": max(0, len(event_ids) - len(set(event_ids)))},
            "consumer": {"name": "catalog", "offset": offset, "applications": applications, "attempts": attempts},
            "inbox": {"event_ids": inbox_ids},
            "derived_view": {"aggregate_id": aggregate, "version": projection_version},
            "workflow": {"state": workflow_state, "history": workflow_history, "compensation_effects": compensation_effects},
            "dead_letters": dead_letters,
            "watermarks": {"event_time": workload["event_time"], "processing_time": workload["processing_time"], "watermark": workload["processing_time"] - 10, "late_action": late_action},
            "reconciliation": {"before": before, "repairs": repairs, "after": after},
            "metrics": {"published_records": len(broker_records), "consumed_records": len(broker_records), "logical_applications": applications, "effect_count": effect_count, "attempts": attempts, "backlog_start": backlog_start, "backlog_end": backlog_end, "oldest_age_ticks": oldest_age, "corrections": corrections, "repairs": len(repairs)},
            "invariants": invariant_rows,
            "evidence_boundary": ["Deterministic teaching model; not production durability, availability, performance, regional survival, universal exactly-once, or security proof."],
        }
        authority_db.close()
        consumer_db.close()
        return trial
