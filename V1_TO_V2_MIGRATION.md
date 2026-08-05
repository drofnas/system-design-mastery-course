# PESD V1.0 (72 Weeks) to V2.0 (104 Weeks)

The immutable V1 release point is `course-v1.0-72-week`. V1 learners may finish
on that release or opt into PESD 2.0. Do not mix week numbers across releases;
module and gate IDs are the stable identity.

## Credit and evidence rules

- A completed V1 module retains credit for its original outcomes.
- Frozen baselines, trials, gate submissions, evaluations, and revisions remain
  byte-identical. Never edit them into V2 form.
- Complete only the bridge pack for newly added outcomes before the next
  applicable V2 gate.
- A passed V1 gate remains a historical pass. The next V2 gate checks accumulated
  bridge evidence; the old gate is not repeated.
- New V2 work uses a separate component in the original evidence lineage and
  records `baseline`, `revision`, or `final` explicitly.
- V1 filenames containing old week numbers may remain as historical evidence.
  V2 manifests and `course-calendar.json` determine current scheduling.

## Module crosswalk

| Stable ID | V1 weeks | V2 weeks | Bridge pack |
|---|---:|---:|---|
| M01 | 1–4 | 1–5 | Constraint and assurance ledger |
| M02 | 5–8 | 6–10 | Tenant allocation, variance, useful-outcome and energy sensitivity |
| M03 | 9–12 | 11–15 | Cgroups, steal time, noisy neighbors, evidence boundary |
| M04 | 13–16 | 18–22 | Governed telemetry data product |
| M05 | 17–20 | 23–27 | Identity, egress, residency, encrypted naming, crypto inventory |
| M06 | 21–24 | 28–32 | Tenant budgets, identity quotas, safe fallback, fairness |
| M07 | 25–28 | 35–39 | Data contracts, quality SLO, lineage, backfill, deletion |
| M08 | 29–32 | 40–44 | Retention/hold/key/export/backup policy replay and resurrection prevention |
| M09 | 33–36 | 45–49 | Tenant lifecycle, cells, control/data plane, quotas and attribution |
| M10 | 37–40 | 52–57 | Learner node under deterministic faults, oracle, fencing, model checks |
| M11 | 41–44 | 58–62 | Semantic event contract, lineage, policy-aware replay, reconciliation |
| M12 | 45–48 | 63–67 | Cyber/corruption recovery, concentration, control-plane and clean-room evidence |
| M13 | 49–52 | 70–74 | Obligation/control/evidence, SSDF, provenance, crypto agility/PQC |
| M14 | 53–56 | 75–79 | Local platform product experiment and FinOps allocation |
| M15 | 57–60 | 80–84 | Common four-runtime semantic and fault contract |
| M16 | 61–64 | 87–91 | Offline state, storage lifecycle, third parties, AI transparency, residency |
| M17 | 65–68 | 92–97 | True streaming/KV/scheduling/cache/failover plus AI dossier |
| M18 | 69–72 | 98–102 | Full AI assurance case and retirement path |

## Gate crosswalk

| Gate ID | V1 week | V2 week | V2 flex delta |
|---|---:|---:|---:|
| G01 | 12 | 16 | 17 |
| G02 | 24 | 33 | 34 |
| G03 | 36 | 50 | 51 |
| G04 | 48 | 68 | 69 |
| G05 | 60 | 85 | 86 |
| G06 | 72 | 103 | 104 |

## Upgrade procedure

1. Tag or otherwise preserve the learner's current V1 commit.
2. Record completed module and gate IDs, not only week numbers.
3. Copy no answer content. Add a V2 bridge-plan file that links immutable V1
   evidence and lists only missing outcomes.
4. Complete bridge work as separate artifacts using the current evidence-mode
   and hashing contract.
5. Submit accumulated bridge evidence at the next V2 gate.
6. Continue with the canonical V2 calendar. If bridge remediation exceeds the
   six-hour flex reserve, pause rather than borrowing from the next module.
