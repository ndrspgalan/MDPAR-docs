# MDPAR benchmark evidence store

This directory contains the canonical C0–C12 benchmark evidence retained for MDPAR 2.0.0. The directory taxonomy is packaging metadata; the contents of historical run artifacts are preserved byte-for-byte. The only newly generated benchmark is C0, rerun after the final 2.0.0 runtime freeze to bind the current JAR SHA-256.

Each capability is stored under `runs/capabilities/C0` through `C12`. Instrument names describe the current canonical capability vocabulary; historical run identifiers embedded inside JSON files are provenance and are intentionally not rewritten.

`index.json` is a machine-readable inventory. It records every evidence file, its SHA-256, size, capability and instrument path so third parties can verify the published package without executing MDPAR.

The evidence store is immutable evidence, not an output scratch directory. New benchmark executions should use a fresh timestamped run directory and must never overwrite an existing run.
