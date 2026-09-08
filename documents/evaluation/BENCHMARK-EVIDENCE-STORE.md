# MDPAR v2.0.0 — Benchmark evidence store

## Purpose

`runs/` is the retained empirical evidence for the C0–C12 campaign. It is part of the scientific evidence package, not disposable execution output.

The canonical hierarchy is:

```text
runs/
  capabilities/
    C0/
    ...
    C12/
```

Each capability may contain one or more named instruments. Instrument names use the current v2.0.0 vocabulary. Historical identifiers inside original JSON/JSONL artifacts remain unchanged because they are provenance, not current architecture.

## Immutability rule

A completed run is immutable. Packaging directories may be renamed to the canonical C0–C12 taxonomy, but the evidence files inside historical runs must not be rewritten merely to modernize terminology. A new benchmark execution must create a new timestamped directory.

C0 is the exception only in the sense that it must be rerun after the final source/runtime freeze: its purpose is to bind the evaluated adapter source and MDPAR JAR by hash. An older C0 remains historical evidence, but it cannot certify a later refactor.

## Integrity index

`runs/index.json` inventories every retained evidence file with SHA-256 and byte size. Rebuild it with:

```powershell
python -m scripts.index_benchmark_evidence
```

Verify the package with:

```powershell
python -m scripts.verify_benchmark_evidence
```

This verification checks the published evidence package only. It does not execute MDPAR or reproduce neural calls.

## Canonical instrument map

- C0: `contractual-reproducibility`
- C1: `structural-identification`
- C2: `structural-metrology`
- C3: `structural-calculus`, `directional-continuity`
- C4: `permutation-realization`, `translation-invariance`
- C5: `contextual-direction`, `contextual-adaptation`
- C6: `longitudinal-narrative`
- C7: `lexical-closed`, `heterogeneous-closed`
- C8: `closed-open-composition`
- C9: `paired-adaptive-economics`, `concurrent-adaptive`
- C10: `temporal-authority`, `natural-online`
- C11: `handoff-contract`, `frontier-recovery`
- C12: `servant-robot`

The map describes experimental instrumentation. It does not subdivide MDPAR into products or user-selectable reasoning modes.
