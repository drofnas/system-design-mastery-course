# Module 8 Semantic Readiness Review

> **PESD 2.0 status: Review.** This pre-migration readiness record is historical, not a current Ready decision. Fresh evaluator repetitions, platform/offline/cleanup matrices, and timed learner pilots remain pending.

Reviewed on 2026-08-02 against the syllabus, `MODULE_STANDARD.md`, Module 7's
explicit durability handoff, learner-artifact preservation rules, and the
published Module 8 assessment contract.

## Local teaching and worked-example isolation

Lessons 1–8 teach every graded mechanism before application: invariant mapping,
histories, serialization dependencies, locks/deadlocks/retries, MVCC/OCC/write
skew, constraints/authority, WAL/checkpoint/redo/undo/group commit,
backup/PITR/RTO/RPO, and decision/migration/ownership. Each lesson contains the
required outcomes, prerequisites, technique, Northstar example, expert errors,
practice, self-check, explanations, and authoritative citations.

Northstar contains controllers, telescopes, exposures, audit rows, and derived
summaries. Search found no commerce mechanism or proposed capstone transaction.
Mentions of commerce exist only to enforce freeze and non-copy boundaries. The
case and answer key state that alternatives can pass.

## Outcome and evidence crosswalk

All M08-O1–O8 resolve to local lessons, EX-01–EX-16, A01–A09, and R01–R10.
Weeks 29–32 each include learn, practice, independent application, reflection,
and 10–12 hours; total effort is 43.5 hours. The package preserves the syllabus
build, seven named failure experiments, transaction/recovery decision, one ADR,
failure matrix, internals report, restore exercise, and teach-back.

No graded requirement relies only on an external source. Required resources
are free, bounded, verified, and have local alternatives. CMU videos have linked
notes/slides plus a complete local written lesson.

## Executable evidence boundary

The Python standard-library lab implements inspectable shared/exclusive locks,
MVCC validation, WAL records/checksums/LSNs, steal/no-force redo/undo, target-LSN
restore, shared-flush group commit, and real subprocess termination. Fourteen
strict scenarios form seven same-input broken/repaired pairs. Trial labels and
README explicitly exclude production database, hardware, kernel, distributed,
cloud, security, and scale claims.

The scenario runner uses deterministic Northstar outcome oracles in addition to
the general mechanisms. It is appropriate as a controlled teaching instrument;
learners must reproduce relevant semantics in their chosen stack before making
vendor or production claims.

## Assessment and safety

Structural gates precede scoring and hard-fail overwritten evidence,
contradiction, missing required work, or correctness failure. R07 protects
evidence integrity; R08 protects invariant, durability, and restore correctness.
The prompt requires heading citations, allowed finding classes, recalculated
averages, confidence, uncertainty, and lesson/EX remediation without replacing
graded answers.

Pass, Revise, and Repeat fixtures use only Northstar. Six serial fixture-scoped
evaluator records preserve runtime/settings, unique isolation IDs, times, raw
JSON, and hashes. Both runs agree on bands; maximum category drift is one. The
generic checker now reads safety-critical criteria from each module manifest,
preserving older modules while correctly applying M08's R07/R08 contract.

## Operational, security, cost, and change coverage

Lessons, worksheet, rubric, and case cover backup confidentiality, restore
credentials and isolation, retention, authorization replay, abort/log/archive/
restore cost, degraded capacity, application/database/security/on-call owners,
mixed-version isolation, canary, rollback/roll-forward, decommissioning,
exceptions, dissent, and measurable reversal evidence.

## Learner artifact safety

The repository contains no Module 7 or Module 8 learner submissions that this
package overwrites. Existing Week 1, Week 12, and Week 24 capstone artifacts are
unchanged. A01, A04, and A05 are immutable after submission; all remediation is
directed to dated addenda. Secret-pattern and answer-leakage searches found no
credential material or canonical commerce choices.

## Reviewer conclusion

The module teaches rather than merely tests, stays inside the syllabus, and is
semantically ready. Remaining limitations are explicitly taught evidence
boundaries, not hidden readiness gaps.
