# Module 13 Remediation Map

| Finding area | Revisit | Repeat evidence |
|---|---|---|
| R01 threat model | L01, EX-01-EX-02 | New dated boundary/abuse review; preserve baseline |
| R02 identity/session | L02, EX-03-EX-04 | Replay/recovery negative tests |
| R03 authorization | L03, EX-05-EX-06 | Expanded allow/deny matrix and policy-failure test |
| R04 tenant isolation | L04, EX-07-EX-08 | Seven-surface cross-tenant tests |
| R05 secrets/keys | L05, EX-09-EX-10 | Rotation and old-version rejection evidence |
| R06 audit/response | L06, EX-11 | Tamper/logging-failure trial and response record |
| R07 data lifecycle | L06, EX-12-EX-13 | Copy ledger and delete/restore verification |
| R08 dependency/abuse | L07, EX-14-EX-15 | Wrong-provenance and bounded-cost reruns |
| R09 prompt/tools | L08, EX-16-EX-17 | Deterministic denial and duplicate-effect tests |
| R10 decision/defense | L08, EX-18 | Revised RFC addendum and new recorded defense |

Repeat only the weak component unless a hard-gate or shared invariant failure
invalidates dependent evidence. Never edit frozen predictions, raw trials, the
submitted major threat model, or earlier capstone artifacts.
