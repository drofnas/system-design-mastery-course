# Northstar Repeat Calibration Submission

## Submission chronology and integrity

The learner ran the lab before writing predictions, then replaced broken F01,
F06, and F09 outputs with repaired files under the same names. A04 is missing
and scenario/config hashes are not cited. Generated evidence was not disclosed.

## Threat model and protected outcomes

The submission lists “use MFA, RBAC, encryption, rate limiting, and guardrails.”
It has no data-flow diagram, support/restore boundary, concrete abuse paths,
testable treatment, residual-risk owner, or expiry.

## Identity and sessions

The API accepts any signed token until its one-day expiry. Logout is client-only.
Recovery sends a reusable code to a newly supplied address. A replayed revoked
session succeeds in the rewritten F03 narrative.

## Authorization and tenant isolation

Routes check the `admin` role but ordinary object reads trust `X-Tenant-ID`.
Cache keys omit tenant and search filters after ranking. F01 returns a south
tenant observation to a north tenant. The worker trusts the UI's publication approval.

## Secrets, keys, and encryption

One static credential is shared by all workers and stored in a committed example.
Rotation adds a new value but the old value remains accepted as rollback. The
submission claims encryption prevents unauthorized tenant reads.

## Audit and privacy lifecycle

Logs include access tokens and full observation bodies. Administrators can edit
records without independent detection. Deletion removes the primary profile but
leaves cache, index, export, and backup copies; restore resurrects the profile
and the report still calls deletion complete.

## Dependency, abuse, and security response

Any signed dependency is accepted without source, builder, or digest expectation.
One global request counter allows a tenant to exhaust export workers. There is
no quarantine, incident owner, or last-good rollback evidence.

## Prompt injection and tools

The system prompt tells the model not to follow malicious documents. The
assistant holds an array-admin credential and may call `array.reconfigure`
without external authorization, exact approval, or idempotency. F09 produces the
effect and is later overwritten.

## Security architecture and defense

The RFC names one preferred product, no alternatives, no migration or rollback,
and claims the system is compliant because it uses encryption. The defense was
answered with AI and contains no reviewer dissent or remediation plan.

## Evidence boundaries and remediation

The submission claims the toy lab proves production security. It edits the
baseline and recommends copying Northstar controls into the commerce system.
