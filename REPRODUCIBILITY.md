# Reproducibility and falsifiability boundary

MDPAR-docs separates reproducibility into three layers.

## 1. Evidence integrity

Every retained benchmark evidence file is bound by `runs/index.json`. The public verifier checks that the path, size and SHA-256 of every indexed object still match the published evidence store.

Run:

```powershell
python verification/verify_benchmark_evidence.py
```

Expected release-state result:

```text
verified_files=579
evidence_integrity=PASS
```

## 2. Recalculation from published records

The raw manifests, records, summaries, corpora and evaluation specifications are retained so that claims derivable from those records can be independently inspected and recalculated. A discrepancy between a published claim and the retained data is therefore falsifiable without access to the private runtime.

## 3. End-to-end execution

Independent re-execution of the complete MDPAR pipeline requires the proprietary MDPAR runtime and any provider access used by the applicable protocol. That level of reproduction is outside the scope of this public package.

This limitation must be stated when describing reproducibility. The package supports strong auditability of published evidence and metric-level verification; it must not be represented as an independently executable distribution of MDPAR.

## Frozen-run rule

Retained canonical runs are scientific evidence. Their payloads must not be silently edited after publication. Naming or packaging changes should be handled through a new release and a regenerated integrity manifest, while historical provenance inside the evidence remains unchanged.
