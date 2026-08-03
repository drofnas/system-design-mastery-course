# Northstar Revise Calibration Submission

## Submission chronology and integrity

The baseline predates eighteen raw trials and pair hashes match. All repaired
invariants pass. Assistance is disclosed. Two experiment interpretations cite
summary tables rather than raw headings, but raw evidence remains unchanged.

## Threat model and protected outcomes

Assets, main API boundaries, N-T01-N-T09, owners, and mitigations exist. Support
and restore appear in the diagram, but their abuse cases have no expiry or
reversal evidence. The model says risk is “medium” without recording confidence.

## Identity and sessions

Expiry, revocation, sensitive reauthentication, and F03 replay denial are tested.
The recovery design names notification and old-material invalidation but does not
test recovery-channel replacement or revocation propagation through one cache.

## Authorization and tenant isolation

Object/action decisions and F01/F02 deny correctly. Database, cache, message,
search, and file surfaces are tested. The administrative export and restore
paths are described but lack negative tests. Break glass has approval and expiry
but no automatic closure evidence.

## Secrets, keys, and encryption

F04 proves old-version rejection. The ledger omits backup-key recovery and does
not quantify consumer observation time. Encryption limits are correctly scoped.

## Audit and privacy lifecycle

The event schema excludes secrets and F05 detects tampering. Logging-storage
failure is predicted but not run. F06 deletes active copies and records the
backup exception; the restore-time deletion test is described but cites no raw result.

## Dependency, abuse, and security response

F07 rejects the mismatched artifact and F08 bounds subject and tenant work.
Transitive dependency expectations and coordinated multi-account abuse remain
untested. Recovery owners exist, but cost units are estimated rather than measured.

## Prompt injection and tools

F09 denies the retrieved instruction with external authorization and approval.
Direct and retrieved attacks are covered, but stale approval and ambiguous
duplicate-effect tests are missing. The assistant credential scope is cited.

## Security architecture and defense

Three options use shared drivers and the selected design has owners and rollback.
The RFC lacks a quantified operating-cost comparison, one privacy reviewer did
not attend, and dissent is summarized without the evidence needed to resolve it.

## Evidence boundaries and remediation

Production and compliance claims are scoped. The learner proposes L02/EX-04,
L04/EX-07-EX-08, L06/EX-13, L07/EX-14-EX-15, and L08/EX-17 remediation in new addenda.
