from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_object(schema: dict, value: dict) -> None:
    required = set(schema.get("required", []))
    if not required <= set(value):
        raise ValueError(f"missing fields: {sorted(required - set(value))}")
    properties = schema.get("properties", {})
    if schema.get("additionalProperties") is False and set(value) - set(properties):
        raise ValueError(f"unexpected fields: {sorted(set(value) - set(properties))}")
    for name, rule in properties.items():
        if name not in value:
            continue
        expected = rule.get("type")
        types = {"string": str, "integer": int, "boolean": bool, "object": dict, "array": list}
        if expected in types and not isinstance(value[name], types[expected]):
            raise ValueError(f"{name} must be {expected}")


def approval_digest(principal: str, tool: str, arguments: dict, idempotency_key: str, expires_at: int) -> str:
    return canonical_sha256({"principal": principal, "tool": tool, "arguments": arguments, "idempotency_key": idempotency_key, "expires_at": expires_at})


@dataclass
class ToolExecutor:
    specifications: dict[str, dict]
    side_effects: dict[str, dict] = field(default_factory=dict)
    consumed_approvals: set[str] = field(default_factory=set)
    audit: list[dict] = field(default_factory=list)

    def execute(self, tool: str, arguments: dict, *, principal: str, scopes: set[str], idempotency_key: str, now: int, approval: dict | None = None) -> dict:
        if tool not in self.specifications:
            raise ValueError("unknown tool")
        specification = self.specifications[tool]
        validate_object(specification["input_schema"], arguments)
        if specification["required_scope"] not in scopes:
            raise PermissionError("principal lacks required scope")
        if idempotency_key in self.side_effects:
            self.audit.append({"event": "deduplicated", "tool": tool, "principal": principal, "idempotency_key": idempotency_key})
            return self.side_effects[idempotency_key]
        if specification["risk"] == "irreversible":
            if approval is None or approval.get("expires_at", 0) < now:
                raise PermissionError("valid approval required")
            expected = approval_digest(principal, tool, arguments, idempotency_key, approval["expires_at"])
            if approval.get("digest") != expected or expected in self.consumed_approvals:
                raise PermissionError("approval is unbound or already consumed")
            self.consumed_approvals.add(expected)
        result = {"status": "accepted", "tool": tool, "operation_id": canonical_sha256([tool, idempotency_key])[:16]}
        self.side_effects[idempotency_key] = result
        self.audit.append({"event": "executed", "tool": tool, "principal": principal, "idempotency_key": idempotency_key})
        return result


@dataclass
class DurableWorkflow:
    max_steps: int
    max_cost_microunits: int
    journal: list[dict] = field(default_factory=list)
    used_steps: int = 0
    used_cost_microunits: int = 0
    cancelled: bool = False

    def record_activity(self, activity_id: str, result: dict, *, cost_microunits: int) -> dict:
        existing = next((row for row in self.journal if row["activity_id"] == activity_id), None)
        if existing:
            return existing["result"]
        if self.cancelled or self.used_steps >= self.max_steps:
            raise RuntimeError("workflow step budget exhausted or cancelled")
        if self.used_cost_microunits + cost_microunits > self.max_cost_microunits:
            raise RuntimeError("workflow cost budget exhausted")
        self.used_steps += 1
        self.used_cost_microunits += cost_microunits
        self.journal.append({"sequence": len(self.journal) + 1, "activity_id": activity_id, "result": result, "cost_microunits": cost_microunits})
        return result

    def checkpoint(self) -> dict:
        return {"journal": list(self.journal), "used_steps": self.used_steps, "used_cost_microunits": self.used_cost_microunits, "cancelled": self.cancelled}

    @classmethod
    def resume(cls, checkpoint: dict, *, max_steps: int, max_cost_microunits: int) -> "DurableWorkflow":
        return cls(max_steps=max_steps, max_cost_microunits=max_cost_microunits, journal=list(checkpoint["journal"]), used_steps=checkpoint["used_steps"], used_cost_microunits=checkpoint["used_cost_microunits"], cancelled=checkpoint["cancelled"])

    def cancel(self) -> None:
        self.cancelled = True
