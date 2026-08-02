# Module 8 Evaluator Calibration

Pass, Revise, and Repeat fixtures use Northstar only. Each fixture has an
immutable manifest. Run the evaluator twice per fixture with deterministic
settings and isolated context. Preserve six raw JSON responses, runtime/model/
client, invocation time, isolation ID, settings, and SHA-256.

Aggregate runs in `results.json`, then run:

```bash
python3 scripts/check_calibration.py modules/08-transactions-concurrency-recovery
python3 scripts/validate_course.py --module M08
```

Bands must agree and each category may drift by at most one point. The checker
also verifies averages, citations, finding classes, remediation references,
manifest identity, result rules, and shared-schema fields.
