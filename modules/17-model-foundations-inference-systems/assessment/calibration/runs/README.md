# Module 17 Raw Calibration Runs

Store exactly six schema-valid evaluator responses here: Pass, Revise, and Repeat
twice. Each run must use a unique isolated read-only session and the deterministic
settings recorded in `run-metadata.json`. Do not create aggregate readiness
results until `scripts/check_calibration.py` accepts all six files.
