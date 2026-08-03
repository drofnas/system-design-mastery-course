---
lesson_id: L04
title: Tenant isolation and scoped access
---

# Tenant isolation and scoped access

## Outcomes

- Bind tenant identity to authenticated context rather than attacker-controlled input.
- Trace isolation through data, cache, file, message, search, compute, and administrative surfaces.
- Design break-glass access with scope, expiry, attribution, monitoring, and review.

## Prerequisites

L02 session authority, L03 authorization tuples, and Module 9 partition and tenant-skew reasoning.

## Mechanism and repeatable method

Tenant isolation is an end-to-end invariant: no subject or workload for tenant A
may disclose or mutate tenant B's protected state without explicit, tested
cross-tenant authority. A tenant ID supplied in a URL or header is a requested
resource locator, not trusted identity.

Apply the **seven-surface audit**:

1. API and background command inputs;
2. authoritative database queries and constraints;
3. cache keys and invalidation;
4. file/blob namespaces and signed access;
5. messages, partition keys, consumers, and dead letters;
6. search, analytics, retrieval, exports, and logs;
7. operators, support tools, migrations, backups, and break glass.

For each surface record tenant source, propagation, enforcement, denied result,
telemetry, repair, and a cross-tenant test. Defense in depth can combine
application predicates, database policies, namespace separation, tenant-scoped
credentials, and isolated resources. More physical separation can reduce some
blast radius while increasing cost and operational drift; it is not automatically safer.

Break glass is a separate state machine: reason and incident, named approver,
specific tenant/object/action, short expiry, strong authentication, visible
session banner, immutable attribution, alerts, automatic closure, and review.

## Worked example

Northstar derives the research consortium from the verified subject membership.
An observation lookup includes object ID and tenant at the data layer; the cache
key is `(tenant, object, representation, policy version)`. Publication messages
carry tenant and object identity but consumers verify both against authoritative
state. Search filters before ranking rather than discarding unauthorized results afterward.

F01 supplies `requested_tenant=south` from a north-tenant session. The broken
variant trusts the request and returns a record. The repaired path ignores that
tenant for authority, loads the object's tenant, denies the mismatch, returns no
existence-revealing detail, and records an attributable isolation event.

## Common expert mistakes

- **Adding tenant filters only in controllers:** workers, exports, caches, and
  search can still cross the boundary.
- **Random identifiers as authorization:** unguessable IDs reduce discovery but
  do not grant access.
- **Shared cache keys:** a correct database check cannot repair data already
  returned from the wrong cached entry.
- **“Internal” bypasses:** support and migration paths often have the largest blast radius.
- **One isolation tier for every tenant:** risk, cost, residency, and operational
  requirements may justify different tiers with explicit contracts.

## Guided practice

Audit the seven Northstar surfaces. For each, write the tenant authority,
enforcement, denial, audit event, negative test, and repair method. Then compare
shared-row, schema/namespace, and dedicated-resource isolation using blast
radius, migration, noisy-neighbor behavior, recovery, cost, and operator error.

## Self-check

1. Why is a tenant header not authoritative?
2. Which surfaces remain after a database row filter?
3. When can dedicated resources be worse?
4. What turns emergency access into break glass rather than a backdoor?

## Explained answers

1. The requester controls it unless it is verified and bound to authenticated membership.
2. Cache, files, messages, search, exports, logs, administration, and backups.
3. When configuration drift, weak operations, or recovery gaps exceed the isolation benefit.
4. Explicit scope, strong authentication, approval, short expiry, attribution,
   alerts, automatic closure, and mandatory review.

## Sources and next work

- [OWASP Multi-Tenant Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)

Complete EX-07 and EX-08, then implement and test every surface you claim to protect.
