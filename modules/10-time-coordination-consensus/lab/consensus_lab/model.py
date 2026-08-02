"""Small deterministic Raft-shaped state machine used by paired scenarios."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    id: str
    role: str = "follower"
    current_term: int = 0
    voted_for: str | None = None
    log: list[dict[str, Any]] = field(default_factory=list)
    commit_index: int = 0
    last_applied: int = 0
    snapshot: dict[str, Any] = field(default_factory=lambda: {
        "status": "active", "last_included_index": 0,
        "last_included_term": 0, "checksum": "genesis",
    })
    membership: dict[str, Any] = field(default_factory=dict)

    def append(self, term: int, command: str) -> dict[str, Any]:
        entry = {"index": len(self.log) + 1, "term": term, "command": command}
        self.log.append(entry)
        return entry

    def record(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "role": self.role,
            "current_term": self.current_term,
            "voted_for": self.voted_for,
            "log": self.log,
            "commit_index": self.commit_index,
            "last_applied": self.last_applied,
            "snapshot": self.snapshot,
            "membership": self.membership,
        }


class Cluster:
    def __init__(self, node_ids: list[str], voters: list[str], initial: dict[str, Any]) -> None:
        self.nodes = {node_id: Node(node_id) for node_id in node_ids}
        for node_id, node in self.nodes.items():
            hard_state = initial["hard_state"][node_id]
            node.current_term = hard_state["current_term"]
            node.voted_for = hard_state["voted_for"]
            node.log = [dict(entry) for entry in initial["logs"][node_id]]
            node.commit_index = hard_state["commit_index"]
            node.last_applied = hard_state["last_applied"]
            snapshot = initial["snapshots"][node_id]
            node.snapshot = {
                "status": "active",
                "last_included_index": snapshot["last_included_index"],
                "last_included_term": snapshot["last_included_term"],
                "checksum": snapshot["checksum"],
            }
            node.membership = {"phase": "old", "voters": list(voters)}
        self.voters = list(voters)
        self.kv = dict(initial["key_values"])
        self.clients = dict(initial["client_sessions"])
        self.events: list[dict[str, Any]] = []
        self.client_results: list[dict[str, Any]] = []
        self.resource = {"max_fence": initial["max_fence"], "accepted": [], "rejected": []}
        self.membership = {
            "old": list(voters), "joint": [], "new": list(voters),
            "phase": "old", "quorum_proofs": [],
        }
        self.metrics = {"messages": 0, "elections": 0, "commits": 0, "applies": 0, "unavailable_operations": 0}

    def emit(self, tick: int, kind: str, detail: str, **values: Any) -> None:
        row = {"tick": tick, "type": kind, "detail": detail}
        row.update(values)
        self.events.append(row)

    def elect(self, candidate: str, term: int, voters: list[str], persist: bool = True) -> None:
        self.metrics["elections"] += 1
        node = self.nodes[candidate]
        node.role = "candidate"
        node.current_term = term
        node.voted_for = candidate
        self.emit(1, "persist" if persist else "volatile", f"{candidate} records term {term} and self-vote")
        for voter_id in voters:
            voter = self.nodes[voter_id]
            voter.current_term = term
            voter.voted_for = candidate
            self.metrics["messages"] += 2
            self.emit(2, "vote", f"{voter_id} grants {candidate} in term {term}", persisted=persist)
        if 1 + len(voters) >= len(self.voters) // 2 + 1:
            node.role = "leader"
            self.emit(3, "leader", f"{candidate} becomes leader in term {term}")

    def append_and_maybe_commit(
        self, leader_id: str, command: str, followers: list[str], commit: bool
    ) -> dict[str, Any]:
        leader = self.nodes[leader_id]
        entry = leader.append(leader.current_term, command)
        self.emit(4, "append", f"{leader_id} appends {command}", index=entry["index"], term=entry["term"])
        for follower_id in followers:
            follower = self.nodes[follower_id]
            follower.log = [dict(row) for row in leader.log]
            self.metrics["messages"] += 2
            self.emit(5, "append_entries", f"{follower_id} stores index {entry['index']}")
        if commit and 1 + len(followers) >= len(self.voters) // 2 + 1:
            for node_id in [leader_id, *followers]:
                node = self.nodes[node_id]
                node.commit_index = entry["index"]
                node.last_applied = entry["index"]
            self.metrics["commits"] += 1
            self.metrics["applies"] += 1 + len(followers)
            self.apply(command)
            self.emit(6, "commit_apply", f"commit and apply index {entry['index']}")
        return entry

    def apply(self, command: str) -> Any:
        parts = command.split(":")
        if parts[0] == "set":
            self.kv[parts[1]] = parts[2]
        elif parts[0] == "inc":
            self.kv[parts[1]] = int(self.kv.get(parts[1], 0)) + 1
        return self.kv.get(parts[1]) if len(parts) > 1 else None

    def client_command(self, client: str, sequence: int, command: str, deduplicate: bool) -> Any:
        identity = f"{client}:{sequence}"
        if deduplicate and identity in self.clients:
            result = self.clients[identity]
            self.client_results.append({
                "client_id": client, "sequence": sequence, "status": "duplicate",
                "result": result, "logical_effects": 0,
            })
            self.emit(10, "client_duplicate", f"return cached result for {identity}")
            return result
        result = self.apply(command)
        if deduplicate:
            self.clients[identity] = result
        self.client_results.append({
            "client_id": client, "sequence": sequence, "status": "applied",
            "result": result, "logical_effects": 1,
        })
        self.emit(10, "client_apply", f"apply {identity}", result=result)
        return result

    def command_resource(self, token: int, command: str, enforce: bool) -> bool:
        if enforce and token < self.resource["max_fence"]:
            self.resource["rejected"].append({"token": token, "command": command})
            self.emit(20, "fence_reject", f"reject stale token {token}")
            return False
        self.resource["max_fence"] = max(token, self.resource["max_fence"])
        self.resource["accepted"].append({"token": token, "command": command})
        self.emit(20, "resource_accept", f"accept token {token}")
        return True
