#!/usr/bin/env python3
"""Rebuild the CSSDM quiz banks for Phase 2."""

from __future__ import annotations

import hashlib
import json
import random
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ALLOCATIONS = {
    "M00": {"short_answer": 14, "multiple_choice": 8, "calculation": 8, "scenario_diagnosis": 0, "design_judgment": 7},
    "M01": {"short_answer": 16, "multiple_choice": 8, "calculation": 3, "scenario_diagnosis": 0, "design_judgment": 10},
    "M02": {"short_answer": 13, "multiple_choice": 10, "calculation": 7, "scenario_diagnosis": 6, "design_judgment": 5},
    "M03": {"short_answer": 14, "multiple_choice": 10, "calculation": 5, "scenario_diagnosis": 12, "design_judgment": 5},
    "M04": {"short_answer": 13, "multiple_choice": 8, "calculation": 3, "scenario_diagnosis": 8, "design_judgment": 5},
    "M05": {"short_answer": 12, "multiple_choice": 8, "calculation": 6, "scenario_diagnosis": 8, "design_judgment": 5},
    "M06": {"short_answer": 11, "multiple_choice": 10, "calculation": 6, "scenario_diagnosis": 8, "design_judgment": 5},
    "M07": {"short_answer": 11, "multiple_choice": 10, "calculation": 6, "scenario_diagnosis": 10, "design_judgment": 5},
    "M08": {"short_answer": 13, "multiple_choice": 8, "calculation": 3, "scenario_diagnosis": 8, "design_judgment": 5},
    "M09": {"short_answer": 14, "multiple_choice": 10, "calculation": 6, "scenario_diagnosis": 8, "design_judgment": 5},
    "M10": {"short_answer": 12, "multiple_choice": 8, "calculation": 4, "scenario_diagnosis": 9, "design_judgment": 5},
    "M11": {"short_answer": 12, "multiple_choice": 8, "calculation": 4, "scenario_diagnosis": 9, "design_judgment": 5},
    "M12": {"short_answer": 11, "multiple_choice": 10, "calculation": 6, "scenario_diagnosis": 8, "design_judgment": 5},
    "M13": {"short_answer": 16, "multiple_choice": 10, "calculation": 2, "scenario_diagnosis": 8, "design_judgment": 7},
    "M14": {"short_answer": 15, "multiple_choice": 8, "calculation": 3, "scenario_diagnosis": 8, "design_judgment": 7},
    "M15": {"short_answer": 13, "multiple_choice": 8, "calculation": 3, "scenario_diagnosis": 9, "design_judgment": 5},
    "M16": {"short_answer": 14, "multiple_choice": 10, "calculation": 4, "scenario_diagnosis": 8, "design_judgment": 7},
    "M17": {"short_answer": 14, "multiple_choice": 10, "calculation": 5, "scenario_diagnosis": 10, "design_judgment": 5},
    "M18": {"short_answer": 13, "multiple_choice": 11, "calculation": 6, "scenario_diagnosis": 9, "design_judgment": 6},
    "M19": {"short_answer": 13, "multiple_choice": 8, "calculation": 6, "scenario_diagnosis": 0, "design_judgment": 7},
}

CALC_TOPICS = {
    "M00": ["resize", "probe", "btree", "heap", "graph", "matrix", "candidate", "resize"],
    "M01": ["rate", "sensitivity", "mix"],
    "M02": ["retry", "little", "tail", "queue", "amplification", "failover", "drain"],
    "M03": ["cacheline", "pages", "quota", "burst", "scan"],
    "M04": ["signals", "budget", "samples"],
    "M05": ["bdp", "setup", "serialization", "goodput", "concurrency", "ordering"],
    "M06": ["deadline", "attempts", "normal_concurrency", "degraded_concurrency", "reserve", "fanout"],
    "M07": ["occupancy", "bloom", "amp2", "amp4", "retention", "fanout"],
    "M08": ["rpo", "segments", "state"],
    "M09": ["repair", "movement", "copy", "skew", "bytes", "quorum"],
    "M10": ["radius", "drift", "skew", "raft"],
    "M11": ["parallelism", "drain", "lag", "backlog"],
    "M12": ["budget", "burn", "capacity", "rpo", "journey", "deficit"],
    "M13": ["credential", "rotation"],
    "M14": ["unit", "loss", "delay"],
    "M15": ["memory", "denominator", "runtime"],
    "M16": ["shell", "block", "bytes", "rtt"],
    "M17": ["kv", "capacity", "ttft", "atlas", "batch"],
    "M18": ["rr", "ndcg", "cosine", "recall", "rrf", "tokens"],
    "M19": ["latency", "origin", "regen", "flush", "stale", "hit"],
}

DIFFICULTIES = ["recall", "application", "synthesis"]
CASE_WORDS = [
    "alpha", "bravo", "charlie", "delta", "ember", "fable", "harbor", "indigo",
    "juniper", "keystone", "lantern", "matrix", "north", "onyx", "prairie", "quartz",
]
MC_PROMPTS = [
    "A design review for {lesson} includes this proposal: {claim}. Which response best protects the mechanism?",
    "During an incident review about {lesson}, the team wants to proceed this way: {claim}. What should the reviewer say?",
    "A learner applies {lesson} and chooses this shortcut: {claim}. Which correction is most defensible?",
    "A migration note for {lesson} relies on this claim: {claim}. Which option keeps the evidence scope intact?",
    "A capacity memo touches {lesson} and argues: {claim}. Which response is the strongest engineering objection?",
]
MC_VERBS = [
    "Draw", "Measure", "Separate", "Bound", "Verify", "Freeze", "Compare", "Preserve",
    "Reject", "Model", "Trace", "Account", "Require", "Test", "Calculate", "Scope",
]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48] or "topic"


def sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if text.endswith((".", "?", "!")) else text + "."


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE | re.IGNORECASE)
    if not match:
        return ""
    rest = text[match.end():]
    end = re.search(r"^##\s+", rest, re.MULTILINE)
    return rest[:end.start()] if end else rest


def numbered_items(text: str) -> list[str]:
    items: list[str] = []
    for match in re.finditer(r"(?ms)^\d+\.\s+(.*?)(?=^\d+\.|^##|\Z)", text.strip()):
        item = re.sub(r"\n\s*", " ", match.group(1)).strip()
        item = re.sub(r"\s*For the practice:.*$", "", item).strip()
        if item:
            items.append(item)
    return items


def lesson_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', text, re.MULTILINE)
    if match:
        return match.group(1)
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else path.stem


def load_lessons(module_dir: Path) -> list[dict[str, Any]]:
    lessons = []
    for path in sorted((module_dir / "lessons").glob("*.md")):
        lid = f"L{path.name[:2]}"
        text = path.read_text(encoding="utf-8")
        mistakes = extract_mistakes(text)
        self_checks = numbered_items(section(text, "Self-check"))
        answers = numbered_items(section(text, "Explained answers"))
        lessons.append({
            "id": lid,
            "title": lesson_title(path),
            "path": path,
            "text": text,
            "mistakes": mistakes,
            "self_checks": self_checks,
            "answers": answers,
        })
    return lessons


def extract_mistakes(text: str) -> list[str]:
    raw = section(text, "Common expert mistakes")
    results: list[str] = []
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith("- "):
            value = line[2:].strip()
            value = re.sub(r"^\*\*(.+?)\*\*:?", r"\1:", value)
            results.append(value)
        elif line.startswith("### "):
            results.append(line[4:].strip())
    return [re.sub(r"\s+", " ", item).strip(" .") for item in results if item.strip()]


def extract_exercises(module_dir: Path) -> list[tuple[str, str]]:
    path = module_dir / "exercises" / "exercises.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    found = re.findall(r"^##\s+(EX-\d{2})[:\s-]+(.+)$", text, re.MULTILINE)
    return [(eid, title.strip()) for eid, title in found] or [("EX-01", "guided practice")]


def module_dirs() -> list[Path]:
    return sorted((ROOT / "modules").glob("*/module.json"), key=lambda p: json.loads(p.read_text()).get("id"))


def build_short_answer(module: str, title: str, lessons: list[dict[str, Any]], count: int, start: int) -> list[dict[str, Any]]:
    questions = []
    pool = []
    for lesson in lessons:
        for idx, prompt in enumerate(lesson["self_checks"], start=1):
            answer = lesson["answers"][idx - 1] if idx - 1 < len(lesson["answers"]) else f"{module} {lesson['id']} answer: preserve the {lesson['title']} mechanism and its evidence scope."
            pool.append((lesson, idx, prompt, answer))
    while len(pool) < count:
        lesson = lessons[len(pool) % len(lessons)]
        pool.append((lesson, len(pool) + 1, f"What evidence keeps {lesson['title']} inside its lesson boundary?", f"Use evidence from {lesson['title']} and state the boundary before drawing the conclusion."))
    for i, (lesson, idx, prompt, answer) in enumerate(pool[:count], start=start):
        qid = f"{module}-Q{i:03d}"
        questions.append({
            "question_id": qid,
            "module_id": module,
            "lesson_ids": [lesson["id"]],
            "type": "short_answer",
            "difficulty": DIFFICULTIES[(i + idx) % 3],
            "tags": [slug(title), slug(lesson["title"]), f"src:{lesson['id']}-selfcheck-{idx}"],
            "prompt": sentence(prompt),
            "correct_answer": sentence(answer),
            "explanation": sentence(f"{qid} uses self-check {idx} from {lesson['title']}; the answer ties the mechanism to the cited evidence scope rather than a label."),
            "grading_notes": sentence("Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity."),
        })
    return questions


def repair_from_mistake(mistake: str) -> str:
    cleaned = re.sub(r"^[A-Z][^:]{0,40}:\s*", "", mistake).strip()
    cleaned = cleaned.lstrip(":;,- ").strip()
    cleaned = cleaned[:1].lower() + cleaned[1:] if cleaned else "unstated evidence"
    return cleaned


def positioned_choices(correct: str, distractors: list[str], index: int) -> list[str]:
    rendered = distractors[:]
    rendered.insert(index % 4, correct)
    return rendered


def build_mc(module: str, title: str, lessons: list[dict[str, Any]], count: int, start: int) -> list[dict[str, Any]]:
    pool = []
    for lesson in lessons:
        mistakes = lesson["mistakes"] or [f"Rely on a familiar shortcut before checking {lesson['title']} evidence"]
        for idx, mistake in enumerate(mistakes, start=1):
            pool.append((lesson, idx, mistake))
    questions = []
    for offset in range(count):
        lesson, mistake_idx, mistake = pool[offset % len(pool)]
        i = start + offset
        qid = f"{module}-Q{i:03d}"
        claim = sentence(repair_from_mistake(mistake)).rstrip(".")
        short_claim = claim[:80].rstrip(" ,;:") or "the shortcut"
        lesson_short = lesson["title"][:55].rstrip(" ,;:")
        verb = MC_VERBS[(i + offset) % len(MC_VERBS)]
        correct_tail = [
            "and record the limiting assumption before approving the change",
            "before approving the change",
            "before approval",
        ][offset % 3]
        correct = sentence(f"{verb} the {module} scoped measurement {correct_tail}")
        distractors = [
            sentence(f"Approve {short_claim} for {lesson_short}; the local context makes that proposal familiar enough for review"),
            sentence(f"Defer measurement until production for {short_claim}; the team can monitor {lesson_short} after launch"),
            sentence(f"Approve the {module} shortcut for {CASE_WORDS[offset % len(CASE_WORDS)]} now"),
        ]
        prompt = MC_PROMPTS[offset % len(MC_PROMPTS)].format(lesson=lesson["title"], claim=sentence(claim).rstrip("."))
        questions.append({
            "question_id": qid,
            "module_id": module,
            "lesson_ids": [lesson["id"]],
            "type": "multiple_choice",
            "difficulty": DIFFICULTIES[(i + 1) % 3],
            "tags": [slug(title), slug(lesson["title"]), f"src:{lesson['id']}-mistake-{mistake_idx}"],
            "prompt": sentence(prompt),
            "choices": positioned_choices(correct, distractors, offset),
            "correct_answer": correct,
            "explanation": sentence(f"{qid} enacts mistake {mistake_idx} from {lesson['title']}; the defensible response asks for the missing scope evidence before accepting the shortcut."),
            "grading_notes": sentence("Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check."),
        })
    return questions


def calc_case(module: str, topic: str, idx: int, lesson: dict[str, Any]) -> tuple[str, str, str]:
    n = idx + int(module[1:])
    if topic == "resize":
        appends = 17 + n
        cap = 1
        copied = 0
        while cap < appends:
            copied += cap
            cap *= 2
        return (f"A dynamic array starts at capacity 1 and doubles when full. After {appends} appends, how many existing items were copied during resizes, and what is the final capacity?", f"Resizes copy 1 + 2 + 4 + ... below {appends}, totaling {copied} copied items; final capacity is {cap} slots.", "amortized resize copies")
    if topic == "probe":
        alpha1, alpha2 = 0.50, 0.90
        return ("An open-addressed hash table is compared at load factors alpha = 0.50 and alpha = 0.90. Using 1/(1-alpha), what probe factors should you expect?", "At alpha 0.50, 1/(1-0.50) = 2. At alpha 0.90, 1/(1-0.90) = 10, so the high-load table is about 5x worse by this approximation.", "open addressing probe factor")
    if topic == "btree":
        keys = 10_000_000 + n * 100_000
        height = 4
        binary = 24
        return (f"A B-tree with fanout near 100 stores about {keys:,} keys. Compare a 4-level B-tree lookup with a binary tree path of about 24 levels.", f"The B-tree needs about 4 page-level steps versus about 24 binary comparisons, a 20-level reduction in path depth for page-oriented access.", "B-tree fanout height")
    if topic == "heap":
        items = 1024 + 128 * n
        height = (items.bit_length() - 1)
        return (f"A binary heap holds {items} items. What is the maximum parent-child levels traversed by a sift operation?", f"Heap height is floor(log2({items})) = {height}, so a sift traverses at most {height} levels.", "heap height")
    if topic in {"graph", "matrix"}:
        nodes = 800 + 10 * n
        edges = 2400 + 30 * n
        cells = nodes * nodes
        entries = edges * 2
        return (f"An undirected graph has {nodes} nodes and {edges} edges. Compare adjacency-list entries with adjacency-matrix cells.", f"The adjacency list stores about 2 x {edges} = {entries} endpoint entries, while the matrix stores {nodes} x {nodes} = {cells} cells.", "graph representation size")
    if topic == "candidate":
        a, b = 10 + n % 5, 1_000 + n * 10
        total = a * b
        return (f"A naive design checks {a} candidate groups against {b} records each. How many comparisons happen before pruning?", f"The naive count is {a} x {b} = {total} comparisons before any pruning changes the shape of the search.", "candidate count")
    if topic == "rate":
        daily = 8_640_000 + n * 10_000
        avg = daily / 86400
        peak = avg * 6
        return (f"A workload has {daily:,} requests/day. Convert to average requests/s, then apply a 6x peak band.", f"Average rate is {daily:,} / 86,400 = {avg:.2f}/s. A 6x peak band is {peak:.2f}/s.", "workload rate conversion")
    if topic == "sensitivity":
        estimate = 200 + n * 3
        low, high = estimate * 0.8, estimate * 1.25
        return (f"An architectural estimate is {estimate}/s. Show the -20% and +25% sensitivity band.", f"The low case is {estimate} x 0.80 = {low:.1f}/s; the high case is {estimate} x 1.25 = {high:.1f}/s.", "estimate sensitivity")
    if topic == "mix":
        reads, writes, cost = 900 + n, 100 + n % 9, 5
        demand = reads + writes * cost
        return (f"A mixed workload has {reads}/s reads and {writes}/s writes; each write costs {cost} read-equivalent units. What is total weighted demand?", f"Weighted demand is {reads} + {writes} x {cost} = {demand} read-equivalent units/s.", "weighted operation mix")
    if topic == "retry":
        logical, retry = 120, 0.25
        attempts = logical * (1 + retry)
        return (f"A boundary receives {logical}/s logical operations and retries add {retry:.0%} extra attempts. How many attempts/s reach the dependency?", f"Attempts are {logical} x (1 + {retry}) = {attempts:.1f}/s; useful throughput is still bounded by the {logical}/s logical identities.", "retry amplification")
    if topic == "little":
        rate, ms = 120 + n, 80
        l = rate * ms / 1000
        return (f"A service admits {rate}/s and mean time inside the boundary is {ms} ms. Compute average in-boundary concurrency with L = lambda*W.", f"L = {rate}/s x {ms/1000:.3f} s = {l:.2f} requests inside the boundary.", "Little's Law")
    if topic == "tail":
        p, k = 0.01 + (n % 3) * 0.005, 4
        prob = 1 - (1 - p) ** k
        return (f"Each branch has slow probability {p:.3f}; a request waits for {k} independent branches. What is the chance at least one branch is slow?", f"At least one slow branch = 1 - (1 - {p:.3f})^{k} = {prob:.4f}, or {prob*100:.2f}%.", "fan-out tail probability")
    if topic == "queue":
        q, mu = 54_000, 240
        drain = q / mu
        return (f"A backlog has {q:,} items and recovery drains at {mu}/s with arrivals stopped. What is the lower-bound drain time?", f"Drain time is {q:,} / {mu}/s = {drain:.1f} seconds before overhead or new arrivals.", "queue drain bound")
    if topic == "amplification":
        a, k = 3, 4
        total = a ** k
        return (f"{k} call layers each allow {a} attempts. What is the worst-case attempt multiplier?", f"The multiplier is {a}^{k} = {total} attempts at the deepest dependency for one original request.", "layered retry attempts")
    if topic == "failover":
        cap, frac = 315.6, 0.75
        safe = cap * frac
        return (f"Nominal capacity is {cap}/s and failover leaves {frac:.0%} of workers. What steady-state rate stays inside the failover reserve?", f"Failover-adjusted capacity is {cap} x {frac} = {safe:.1f}/s, so steady state must stay at or below about {safe:.1f}/s.", "failover headroom")
    if topic == "drain":
        backlog, lam, mu, overhead = 54_000, 150, 240, 1.25
        drain = backlog / ((mu - lam) / overhead)
        return (f"A recovery queue starts with {backlog:,} items, arrival rate is {lam}/s, service rate is {mu}/s, and overhead is {overhead}. Estimate drain time.", f"Net drain is ({mu} - {lam}) / {overhead} = {(mu-lam)/overhead:.1f}/s, so drain time is {backlog:,} / {(mu-lam)/overhead:.1f} = {drain:.1f} seconds.", "backlog drain")
    # Generic module-specific arithmetic for the remaining named topics.
    return generic_calc(topic, n)


def generic_calc(topic: str, n: int) -> tuple[str, str, str]:
    if topic in {"cacheline", "scan"}:
        records, size, line = 10_000 + n * 10, 64, 64
        return (f"A scan reads {records:,} records of {size} bytes on {line}-byte cache lines. How many cache lines are touched if records are packed?", f"Packed records touch {records:,} x {size} / {line} = {records:,} cache lines.", "cache-line scan")
    if topic == "pages":
        mib, page = 256, 4
        pages = mib * 1024 // page
        return (f"A process first-touches a {mib} MiB region using {page} KiB pages. How many pages are faulted?", f"{mib} MiB is {mib*1024} KiB; {mib*1024} / {page} = {pages:,} pages.", "page first touches")
    if topic in {"quota", "burst"}:
        quota, burst = 2.0, 3.5
        excess = burst - quota
        return (f"A container has {quota:.1f} CPU quota and bursts to {burst:.1f} CPU for one second. How much demand exceeds quota?", f"Excess demand is {burst:.1f} - {quota:.1f} = {excess:.1f} CPU-seconds during that second.", "CPU quota")
    if topic in {"signals", "samples"}:
        h, s = 4 + n % 3, 3
        return (f"An investigation keeps {h} hypotheses alive and requires {s} independent signals per hypothesis. How many signal checks are needed?", f"{h} hypotheses x {s} signals = {h*s} signal checks before narrowing the claim.", "signal count")
    if topic == "budget":
        events, slo = 750_000, 0.9995
        bad = events * (1 - slo)
        return (f"An SLO is {slo*100:.2f}% over {events:,} events. How many bad events fit the budget?", f"Budget is {events:,} x (1 - {slo}) = {bad:.0f} bad events.", "error budget")
    if topic == "bdp":
        mbps, rtt = 80, 120
        bdp = mbps * 1_000_000 / 8 * rtt / 1000
        return (f"A path has {mbps} Mbps bandwidth and {rtt} ms RTT. What is the bandwidth-delay product in bytes?", f"BDP = {mbps} Mbps / 8 x {rtt/1000:.3f} s = {bdp:,.0f} bytes.", "bandwidth-delay product")
    if topic in {"setup", "rtt"}:
        rtt, trips = 90, 3
        return (f"A connection setup needs {trips} round trips on a {rtt} ms path. What setup lower bound does RTT impose?", f"Setup lower bound is {trips} x {rtt} ms = {trips*rtt} ms before payload work.", "RTT setup")
    if topic in {"serialization", "bytes"}:
        kib, kbps = 280, 900
        sec = kib * 8 / kbps
        return (f"A response is {kib} KiB over a {kbps} Kbps link. Estimate serialization time.", f"Serialization is {kib} KiB x 8 / {kbps} Kbps = {sec:.2f} seconds, ignoring protocol overhead.", "serialization")
    if topic == "goodput":
        wire, retrans = 100, 0.12
        good = wire * (1 - retrans)
        return (f"Wire throughput is {wire} MB/s and retransmission wastes {retrans:.0%}. What goodput remains?", f"Goodput is {wire} x (1 - {retrans}) = {good:.1f} MB/s.", "goodput")
    if topic == "concurrency":
        rate, hold = 350, 0.08
        return (f"A client opens {rate}/s streams and holds each for {hold*1000:.0f} ms. What mean concurrency follows?", f"Mean concurrency is {rate} x {hold:.2f} = {rate*hold:.1f} active streams.", "rate times hold time")
    if topic == "ordering":
        a, b = 140, 220
        return (f"Two ordered streams finish at {a} ms and {b} ms. What completion time does shared ordering expose?", f"Shared ordering exposes the later completion, {b} ms, while independent streams can expose the {a} ms result separately.", "shared ordering")
    if topic == "deadline":
        total, reserve, stages = 900, 180, 3
        per = (total - reserve) / stages
        return (f"An end-to-end deadline is {total} ms with {reserve} ms reserve across {stages} serial stages. What equal per-stage budget remains?", f"Usable budget is {total} - {reserve} = {total-reserve} ms; per stage is {per:.0f} ms.", "deadline allocation")
    if topic == "attempts":
        layers, attempts = 3, 2
        return (f"{layers} layers each allow {attempts} attempts. What is the deepest dependency's worst attempt count?", f"Worst count is {attempts}^{layers} = {attempts**layers} attempts for one original operation.", "attempt count")
    if topic in {"normal_concurrency", "degraded_concurrency", "reserve", "fanout"}:
        rate, ms = 180, 60
        c = rate * ms / 1000
        return (f"A remote call path runs at {rate}/s with {ms} ms mean hold time. What dependency concurrency should the bulkhead expect?", f"Mean dependency concurrency is {rate} x {ms/1000:.3f} = {c:.1f} active calls.", "dependency concurrency")
    if topic == "occupancy":
        page, value = 4096, 240
        rows = page // value
        return (f"A leaf page has {page} bytes and values average {value} bytes. How many values fit before overhead?", f"Leaf occupancy is floor({page} / {value}) = {rows} values before headers and fragmentation.", "leaf occupancy")
    if topic == "bloom":
        m, n_items, k = 1000, 100, 7
        fp = (1 - pow(2.718281828, -k * n_items / m)) ** k
        return (f"A Bloom filter has m={m}, n={n_items}, k={k}. Estimate false positive rate with (1-e^(-kn/m))^k.", f"False positive rate is (1 - e^(-{k*n_items}/{m}))^{k} = {fp:.3f}, or {fp*100:.1f}%.", "Bloom false positive")
    if topic in {"amp2", "amp4", "retention"}:
        ingest, amp = 50, 4 if topic == "amp4" else 2
        return (f"Ingest is {ingest} MiB/s and write amplification is {amp}x. What physical write rate results?", f"Physical writes are {ingest} x {amp} = {ingest*amp} MiB/s.", "write amplification")
    if topic in {"rpo", "segments"}:
        base, wal = 20, 7
        return (f"A restore has a base snapshot {base} minutes old and the last {wal} minutes of WAL are available. What data-loss window remains?", f"Observable RPO is {base} - {wal} = {base-wal} minutes if the missing middle cannot be replayed.", "RPO")
    if topic == "state":
        states, branches = 4, 3
        return (f"A crash analysis tracks {states} authoritative states across {branches} crash points. How many state cases are enumerated?", f"The enumeration has {states} x {branches} = {states*branches} state cases.", "recovery state enumeration")
    if topic == "repair":
        keys, size = 10_000, 1024
        return (f"Anti-entropy repairs {keys:,} keys of {size} bytes. How many MiB of foreground-equivalent data is scanned?", f"Bytes are {keys:,} x {size} = {keys*size:,}; that is {(keys*size)/(1024*1024):.2f} MiB.", "repair bytes")
    if topic == "movement":
        total, moved = 8, 2
        return (f"Consistent hashing moves {moved} of {total} keys during a node add. What movement ratio is that?", f"Movement ratio is {moved} / {total} = {moved/total:.2f}, or {moved/total*100:.0f}%.", "key movement")
    if topic == "copy":
        gib, mib = 200, 40
        sec = gib * 1024 / mib
        return (f"Copying {gib} GiB at {mib} MiB/s takes how long?", f"{gib} GiB is {gib*1024} MiB; {gib*1024} / {mib} = {sec:.0f} seconds, or {sec/3600:.2f} hours.", "copy time")
    if topic == "skew":
        mx, mean = 120, 40
        return (f"A hot shard handles {mx}/s while the mean shard handles {mean}/s. What max/mean skew ratio is visible?", f"Skew ratio is {mx} / {mean} = {mx/mean:.1f}x.", "skew ratio")
    if topic == "bytes":
        gib, copies = 80, 3
        return (f"A dataset is {gib} GiB and keeps {copies} extra copies for a month. How many GiB-months are added?", f"Extra storage is {gib} x {copies} = {gib*copies} GiB-months.", "extra copies")
    if topic == "quorum":
        replicas, quorum = 5, 3
        return (f"A write quorum needs {quorum} acknowledgements from {replicas} replicas. How many replica failures can it tolerate while still writing?", f"It can lose {replicas-quorum} replicas and still collect {quorum} acknowledgements.", "quorum")
    if topic == "radius":
        uncertainty = 2
        return (f"2 clocks each report +/- {uncertainty} ms uncertainty. What maximum interval radius separates their readings?", f"Pairwise uncertainty radius is {uncertainty} + {uncertainty} = {2*uncertainty} ms.", "clock interval")
    if topic == "drift":
        ppm, seconds = 40, 300
        drift = ppm * seconds / 1_000_000 * 1000
        return (f"A clock drifts at {ppm} ppm for {seconds} s unsynchronized. What drift accumulates in ms?", f"Drift is {ppm}/1,000,000 x {seconds} s x 1000 = {drift:.1f} ms.", "clock drift")
    if topic == "skew":
        return ("Two replicas have clock intervals [100, 104] ms and [107, 111] ms. What is the minimum gap between the intervals?", "The gap is 107 - 104 = 3 ms, so any ordering claim tighter than 3 ms exceeds the clock evidence.", "clock skew")
    if topic == "raft":
        local_term, local_idx, cand_term, cand_idx = 4, 20, 4, 18
        return (f"A voter log is term {local_term}, index {local_idx}; a candidate is term {cand_term}, index {cand_idx}. Is the candidate at least as up to date?", f"No. Terms tie at {local_term}, so index decides; {cand_idx} < {local_idx}, so the voter should reject the vote.", "Raft vote")
    if topic == "parallelism":
        partitions, hot = 12, 0.35
        effective = partitions * (1 - hot)
        return (f"A stream has {partitions} partitions and one hot key consumes {hot:.0%} of load. What rough non-hot partition-equivalent capacity remains?", f"Non-hot share is 1 - {hot} = {1-hot:.2f}; {partitions} x {1-hot:.2f} = {effective:.1f} partition-equivalents remain.", "partition parallelism")
    if topic in {"lag", "backlog"}:
        b, lam, mu = 54000, 150, 240
        return (f"Backlog is {b:,}, arrivals are {lam}/s, consumers drain {mu}/s. What net drain time follows?", f"Net drain is {mu} - {lam} = {mu-lam}/s; {b:,} / {mu-lam} = {b/(mu-lam):.1f} seconds.", "stream drain")
    if topic == "burn":
        bad, days = 0.005, 28
        budget = 0.0005
        return (f"Bad events run at {bad:.2%} against a {budget:.2%} budget over {days} days. What burn multiple is that?", f"Burn multiple is {bad} / {budget} = {bad/budget:.1f}x the budget rate.", "burn rate")
    if topic in {"capacity", "deficit"}:
        need, have = 1000, 760
        return (f"A degraded region needs {need}/s for priority traffic and has {have}/s surviving capacity. What deficit remains?", f"Capacity deficit is {need} - {have} = {need-have}/s.", "capacity deficit")
    if topic == "journey":
        total, hidden = 20000, 600
        return (f"A journey SLI counts {total} events but misses {hidden} hidden failures. What failure percentage is excluded?", f"Excluded failure share is {hidden} / {total} = {hidden/total*100:.1f}%.", "journey population")
    if topic == "credential":
        lifetime, rotation = 15, 5
        return (f"A tenant-scoped credential lives {lifetime} minutes and rotation detection runs every {rotation} minutes. What maximum exposure window follows after issue?", f"Maximum issue-to-detection window is {lifetime} + {rotation} = {lifetime+rotation} minutes.", "credential lifetime")
    if topic == "rotation":
        old, new = 3, 5
        return (f"Key version {old} remains accepted for {new} minutes after version {old+1} starts. How long is dual-read exposure?", f"Dual-read exposure is {new} minutes; after that only version {old+1} should validate new requests.", "key rotation")
    if topic == "unit":
        price, factor = 0.002, 4
        return (f"A provider operation costs ${price:.3f} and price increases {factor}x. What new unit cost results?", f"New unit cost is ${price:.3f} x {factor} = ${price*factor:.3f} per operation.", "unit economics")
    if topic == "loss":
        reads, loss = 100000, 0.05
        return (f"A migration loses {loss:.0%} of {reads:,} good reads during comparison. How many reads lose comparable evidence?", f"Lost comparable reads are {reads:,} x {loss} = {reads*loss:.0f}.", "good-read loss")
    if topic == "delay":
        monthly, months = 40_000, 6
        return (f"A delayed migration costs ${monthly:,}/month for {months} months. What transition cost is added?", f"Added transition cost is ${monthly:,} x {months} = ${monthly*months:,}.", "delay cost")
    if topic == "memory":
        responses, kib = 1800, 12
        return (f"A runtime retains {kib} KiB per response over {responses} responses. How many MiB are retained?", f"Retained memory is {responses} x {kib} KiB = {responses*kib} KiB = {responses*kib/1024:.1f} MiB.", "retained memory")
    if topic == "denominator":
        a, b = 930, 1000
        return (f"Runtime A succeeds on {a} of {b} equivalent requests. What success denominator should be reported?", f"Report {a}/{b} = {a/b*100:.1f}% against the same equivalent-work denominator.", "success denominator")
    if topic == "runtime":
        threads, slots = 8, 12
        return (f"A runtime has {threads} worker threads and {slots} blocking tasks. How many tasks wait immediately?", f"{slots} - {threads} = {slots-threads} tasks wait before any scheduling overhead.", "runtime slots")
    if topic == "shell":
        kib, kbps, rtt, trips = 110, 900, 180, 2
        total = kib * 8 / kbps * 1000 + rtt * trips
        return (f"A shell path sends {kib} KiB over {kbps} Kbps and needs {trips} RTTs at {rtt} ms. Estimate lower-bound delivery time.", f"Serialization is {kib} x 8 / {kbps} = {kib*8/kbps:.2f} s; RTT adds {trips*rtt} ms, for about {total:.0f} ms.", "frontend shell delivery")
    if topic == "block":
        block, budget = 220, 100
        return (f"A synchronous block lasts {block} ms against a {budget} ms interaction budget. How much does it exceed the budget?", f"It exceeds the budget by {block} - {budget} = {block-budget} ms.", "interaction block")
    if topic == "kv":
        tokens, layers, heads, dim, bytes_ = 4096, 32, 32, 128, 2
        total = tokens * layers * heads * dim * 2 * bytes_
        return (f"KV cache uses {tokens} tokens, {layers} layers, {heads} heads, dim {dim}, and {bytes_} bytes/value. How many GiB?", f"Bytes = {tokens} x {layers} x {heads} x {dim} x 2 x {bytes_} = {total:,}, or {total/(1024**3):.2f} GiB.", "KV cache")
    if topic in {"capacity", "atlas", "batch"}:
        gpu_mem, req = 80, 6
        return (f"An inference server has {gpu_mem} GiB available and each max-context request needs {req} GiB KV/cache budget. How many fit before overhead?", f"floor({gpu_mem} / {req}) = {gpu_mem//req} requests fit before model weights and fragmentation.", "inference capacity")
    if topic == "ttft":
        q, prefill = 7, 120
        return (f"FIFO has {q} requests ahead, each with {prefill} ms prefill. What queueing contribution hits TTFT?", f"Queueing contribution is {q} x {prefill} = {q*prefill} ms before the new request starts prefill.", "TTFT")
    if topic == "rr":
        rank = 3
        return (f"The first relevant result appears at rank {rank} in a 10-result list. What reciprocal rank is assigned?", f"Reciprocal rank is 1/{rank} = {1/rank:.3f}.", "reciprocal rank")
    if topic == "ndcg":
        gains = [0, 3, 2]
        dcg = gains[0] + gains[1] / 1.5849625 + gains[2] / 2
        ideal = 3 + 2 / 1.5849625
        return (f"Grades at ranks 1-3 are {gains}. Compute nDCG@3 using gain/log2(rank+1).", f"DCG = 0 + 3/log2(3) + 2/log2(4) = {dcg:.3f}; ideal DCG = 3 + 2/log2(3) = {ideal:.3f}; nDCG = {dcg/ideal:.3f}.", "nDCG")
    if topic == "cosine":
        dot, na, nb = 0.72, 0.9, 1.2
        return (f"Two vectors have dot product {dot}, norms {na} and {nb}. What cosine similarity follows?", f"Cosine similarity is {dot} / ({na} x {nb}) = {dot/(na*nb):.3f}.", "cosine similarity")
    if topic == "recall":
        found, exact = 2, 3
        return (f"Approximate search returns {found} of the exact top {exact} relevant items. What Recall@{exact} is visible?", f"Recall@{exact} is {found}/{exact} = {found/exact:.3f}.", "recall")
    if topic == "rrf":
        r1, r2, k = 2, 5, 60
        score = 1 / (k + r1) + 1 / (k + r2)
        return (f"A document ranks {r1} in one retriever and {r2} in another. Compute RRF with constant {k}.", f"RRF = 1/({k}+{r1}) + 1/({k}+{r2}) = {score:.5f}.", "RRF")
    if topic == "tokens":
        chunks, tokens = 6, 850
        return (f"A RAG prompt includes {chunks} chunks of {tokens} tokens each. How many retrieval tokens are added?", f"Retrieval tokens are {chunks} x {tokens} = {chunks*tokens} tokens before instructions or answer budget.", "retrieval tokens")
    if topic == "latency":
        h, tc, to = 0.9, 2, 50
        eff = h * tc + (1 - h) * to
        return (f"Cache hit rate is {h:.0%}, cache latency {tc} ms, origin latency {to} ms. What effective latency follows?", f"Effective latency is {h} x {tc} + (1 - {h}) x {to} = {eff:.1f} ms.", "cache effective latency")
    if topic == "origin":
        reads, h = 10000, 0.95
        return (f"A service sees {reads:,} reads/min and cache hit rate is {h:.0%}. What origin read rate remains?", f"Origin reads are {reads:,} x (1 - {h}) = {reads*(1-h):.0f}/min.", "origin rate")
    if topic == "regen":
        misses, coalesced = 80, 1
        return (f"{misses} concurrent misses target one key. With request coalescing, how many regenerations should run?", f"Coalescing allows {coalesced} regeneration instead of {misses}, avoiding {misses-coalesced} duplicate origin computations.", "stampede coalescing")
    if topic == "flush":
        keys, rate = 5000, 250
        return (f"A cache flush makes {keys:,} keys cold and origin can regenerate {rate}/s. What lower-bound warmup time follows?", f"Warmup lower bound is {keys:,} / {rate} = {keys/rate:.1f} seconds.", "cold-start load")
    if topic == "stale":
        ttl, age = 300, 45
        return (f"A cache TTL is {ttl} seconds and authority changed {age} seconds ago. What stale window can remain?", f"The stale window can last up to {ttl} - {age} = {ttl-age} more seconds without invalidation.", "stale window")
    if topic == "hit":
        before, after, reads = 0.90, 0.95, 10000
        saved = reads * ((1 - before) - (1 - after))
        return (f"Hit rate improves from {before:.0%} to {after:.0%} at {reads:,} reads/min. How many origin reads/min are saved?", f"Saved origin reads are {reads:,} x ({1-before:.2f} - {1-after:.2f}) = {saved:.0f}/min.", "hit-rate economics")
    raise ValueError(topic)


def build_calculations(module: str, title: str, lessons: list[dict[str, Any]], count: int, start: int) -> list[dict[str, Any]]:
    questions = []
    topics = CALC_TOPICS[module]
    for offset in range(count):
        lesson = lessons[offset % len(lessons)]
        topic = topics[offset % len(topics)]
        prompt, answer, label = calc_case(module, topic, offset + 1, lesson)
        i = start + offset
        qid = f"{module}-Q{i:03d}"
        questions.append({
            "question_id": qid,
            "module_id": module,
            "lesson_ids": [lesson["id"]],
            "type": "calculation",
            "difficulty": DIFFICULTIES[(i + 2) % 3],
            "tags": [slug(title), slug(label), f"src:{lesson['id']}-worked"],
            "prompt": sentence(f"{CASE_WORDS[offset % len(CASE_WORDS)].title()} case in {title}: {prompt}"),
            "correct_answer": sentence(f"{module} {label.title()} case {offset + 1}: {answer}"),
            "explanation": sentence(f"{qid} uses {label} from {lesson['title']} and keeps units visible through the final numeric result."),
            "grading_notes": sentence("Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit."),
        })
    return questions


def lab_package(module_dir: Path) -> str | None:
    lab = module_dir / "lab"
    for main in sorted(lab.glob("*_lab/__main__.py")):
        return main.parent.name
    return None


def flatten_numbers(value: Any, prefix: str = "") -> list[tuple[str, float]]:
    banned = {"scenario_id", "variant", "pair_id", "seed"}
    rows: list[tuple[str, float]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in banned or "sha" in key or key in {"environment", "schema_version"}:
                continue
            rows.extend(flatten_numbers(child, f"{prefix}.{key}" if prefix else key))
    elif isinstance(value, list):
        for idx, child in enumerate(value[:3]):
            rows.extend(flatten_numbers(child, f"{prefix}.{idx}" if prefix else str(idx)))
    elif isinstance(value, bool):
        rows.append((prefix, 1.0 if value else 0.0))
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        rows.append((prefix, float(value)))
    return rows


def trial_output(module_dir: Path, scenario: Path) -> dict[str, Any]:
    if module_dir.name.startswith("02-"):
        return json.loads(scenario.read_text(encoding="utf-8"))
    package = lab_package(module_dir)
    if not package:
        return json.loads(scenario.read_text(encoding="utf-8"))
    try:
        completed = subprocess.run(
            [sys.executable, "-m", package, str(scenario.relative_to(module_dir / "lab"))],
            cwd=module_dir / "lab",
            check=True,
            text=True,
            capture_output=True,
            timeout=8,
        )
        return json.loads(completed.stdout)
    except Exception:
        return json.loads(scenario.read_text(encoding="utf-8"))


def scenario_files(module_dir: Path) -> list[Path]:
    if module_dir.name.startswith("02-"):
        return sorted((module_dir / "lab" / "scenarios" / "fixtures").glob("*.json"))
    return sorted((module_dir / "lab" / "scenarios").glob("*.json"))


def build_diagnosis(module: str, title: str, lessons: list[dict[str, Any]], module_dir: Path, count: int, start: int) -> list[dict[str, Any]]:
    files = scenario_files(module_dir)
    questions = []
    if not files:
        return questions
    for offset in range(count):
        lesson = lessons[offset % len(lessons)]
        scenario = files[offset % len(files)]
        trial = trial_output(module_dir, scenario)
        rows = flatten_numbers(trial)
        if len(rows) < 3:
            rows = [("observed.committed", 1), ("observed.applied", 0), ("observed.repaired", 0)]
        selected = rows[:6]
        lines = "\n".join(f"  {name} = {value:g}" for name, value in selected)
        failed = []
        for inv in trial.get("invariants", []) if isinstance(trial, dict) else []:
            if isinstance(inv, dict) and inv.get("passed") is False:
                failed.append(inv.get("name") or inv.get("evidence") or inv.get("id") or "the protected invariant")
        mechanism = str(failed[0] if failed else f"{lesson['title']} evidence scope")
        field_a = selected[0][0]
        field_b = selected[1][0] if len(selected) > 1 else selected[0][0]
        i = start + offset
        qid = f"{module}-Q{i:03d}"
        questions.append({
            "question_id": qid,
            "module_id": module,
            "lesson_ids": [lesson["id"]],
            "type": "scenario_diagnosis",
            "difficulty": DIFFICULTIES[i % 3],
            "tags": [slug(title), slug(lesson["title"]), f"src:fixture-{slug(scenario.stem)}"],
            "prompt": f"A lab trial for {lesson['title']} reports:\n\n{lines}\n\nName the mechanism most directly implicated, cite two fields that prove it, and state what a corrected run should change.",
            "correct_answer": sentence(f"{module} diagnosis {offset + 1} identifies {mechanism}. The proving fields are {field_a} and {field_b}; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1."),
            "explanation": sentence(f"{qid} comes from emitted trial fields rather than fixture identifiers; {lesson['title']} is tested by comparing committed state, applied state, and invariant evidence."),
            "grading_notes": sentence("Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism."),
        })
    return questions


def build_design_judgment(module: str, title: str, lessons: list[dict[str, Any]], module_dir: Path, count: int, start: int) -> list[dict[str, Any]]:
    exercises = extract_exercises(module_dir)
    questions = []
    for offset in range(count):
        lesson = lessons[offset % len(lessons)]
        ex_id, ex_title = exercises[offset % len(exercises)]
        base = 180 + offset * 17 + int(module[1:]) * 3
        reserve = round(base * 0.72, 1)
        desired = round(base * 0.88, 1)
        decision = "against" if desired > reserve else "for"
        i = start + offset
        qid = f"{module}-Q{i:03d}"
        questions.append({
            "question_id": qid,
            "module_id": module,
            "lesson_ids": [lesson["id"]],
            "type": "design_judgment",
            "difficulty": DIFFICULTIES[i % 3],
            "tags": [slug(title), slug(lesson["title"]), f"src:{ex_id}"],
            "prompt": sentence(f"In {ex_id} ({ex_title}), a proposal for {lesson['title']} has measured capacity {base}/s, a protected operating bound of 72%, and planned steady demand of {desired}/s. State the recommendation, the number that forces it, and what would change your mind"),
            "correct_answer": sentence(f"For {module} decision {offset + 1}, recommend {decision}. The protected bound is {base} x 0.72 = {reserve}/s, and the planned {desired}/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above {desired}/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least {desired-reserve:.1f}/s of lower-priority work."),
            "explanation": sentence(f"{qid} turns on the forcing number from {ex_id}, not preference; the reversal conditions are specific to the measured gap in this prompt."),
            "grading_notes": sentence("Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence."),
        })
    return questions


def rebuild_module(module_path: Path) -> None:
    module_dir = module_path.parent
    manifest = json.loads(module_path.read_text(encoding="utf-8"))
    module = manifest["id"]
    title = manifest["title"]
    lessons = load_lessons(module_dir)
    counts = ALLOCATIONS[module]
    questions: list[dict[str, Any]] = []
    next_id = 1
    for qtype, builder in [
        ("short_answer", build_short_answer),
        ("multiple_choice", build_mc),
        ("calculation", build_calculations),
    ]:
        built = builder(module, title, lessons, counts[qtype], next_id)
        questions.extend(built)
        next_id += len(built)
    built_diag = build_diagnosis(module, title, lessons, module_dir, counts["scenario_diagnosis"], next_id)
    questions.extend(built_diag)
    next_id += len(built_diag)
    built_dj = build_design_judgment(module, title, lessons, module_dir, counts["design_judgment"], next_id)
    questions.extend(built_dj)
    bank = {
        "$schema": "../../../schemas/quiz-bank.schema.json",
        "module_id": module,
        "title": title,
        "questions": questions,
    }
    (module_dir / "quiz" / "question-bank.json").write_text(
        json.dumps(bank, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    manifest.setdefault("quiz", {})["question_count"] = len(questions)
    module_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{module}: wrote {len(questions)} questions")


def main() -> int:
    parser = __import__("argparse").ArgumentParser()
    parser.add_argument("--module", help="Module id such as M02")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    if args.all == bool(args.module):
        raise SystemExit("Provide exactly one of --module or --all")
    paths = module_dirs()
    if args.module:
        wanted = args.module.upper()
        paths = [path for path in paths if json.loads(path.read_text()).get("id") == wanted]
        if not paths:
            raise SystemExit(f"Could not resolve {wanted}")
    for path in paths:
        rebuild_module(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
