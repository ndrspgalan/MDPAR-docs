# MDPAR-docs

Public documentation and scientific-evidence package for **MDPAR 2.0.0** (Modelo de Dirección de Pensamiento Ampliado y Refinado).

This repository is deliberately **not** the production MDPAR source repository. Its purpose is to make the scientific and operational claims surrounding MDPAR inspectable without publishing the proprietary runtime implementation.

## Contents

- `documents/` — the technical MDPAR document, the Structural Universality Hypothesis document, and the Swagger operational manual.
- `docs/` — operational and evaluation specifications from `mdpar-ai-adapter`.
- `corpus/` — canonical corpora and fixtures used by the retained C0–C12 evaluation protocols.
- `runs/` — retained benchmark evidence, organized by Capability C0–C12, with `runs/index.json` binding retained evidence files by SHA-256.
- `verification/` — public, non-runtime verification utilities for checking the evidence-store index and integrity.
- `requirements.txt` — dependency snapshot of the audited adapter environment. It documents the evaluated environment; it does not make the proprietary runtime independently executable.
- `checksums/SHA256SUMS.txt` — package-level SHA-256 manifest.
- `LICENSE` and `RIGHTS-NOTICE.md` — proprietary publication terms; copyright © 2026 Andrés Pérez Galán, all rights reserved.

## What this package permits a third party to examine

The package is intended to support three separate questions:

1. **Documentary auditability** — inspect the formalism, hypothesis, operational contract, corpora, manifests and raw retained outputs.
2. **Metric/evidence reproducibility** — verify the retained evidence store and recalculate claims that are derivable from the published records.
3. **End-to-end runtime reproducibility** — not provided by this repository because the production MDPAR runtime is proprietary and is not distributed here.

The distinction is intentional. Public evidence should not be described as an independently executable copy of MDPAR.

## Capabilities

C means **Capability**, not level or score.

| Capability | Canonical focus |
|---|---|
| C0 | Contractual reproducibility |
| C1 | Structural identification |
| C2 | Structural metrology |
| C3 | Structural calculus and directional continuity |
| C4 | Structural transformation and equivalence |
| C5 | Contextual cooperation |
| C6 | Longitudinal cognition and epistemic timing |
| C7 | Bounded and heterogeneous CLOSED intelligence |
| C8 | CLOSED/OPEN cooperative composition |
| C9 | Adaptive and concurrent cognition |
| C10 | Temporal authority and embodiment |
| C11 | Degradation, continuity and recovery |
| C12 | Sustained system cooperation |

See `docs/evaluation/MDPAR-BENCHMARKING-STANDARD.md` for the normative evaluation doctrine and `docs/evaluation/BENCHMARK-EVIDENCE-STORE.md` for evidence-store rules.

## Verify the retained evidence

From the repository root:

```powershell
python verification/verify_benchmark_evidence.py
```

The published package should report:

```text
verified_files=582
evidence_integrity=PASS
```

`checksums/SHA256SUMS.txt` provides a second package-level integrity surface independent of the internal run index.

## Scientific scope

C0–C12 are retained experimental evidence for implemented properties and system behavior. They are not, by themselves, a proof of structural universality across all possible domains, modalities, human/artificial systems or future implementations. The broader hypothesis and its falsifiability conditions are specified separately in `documents/MDPAR_Hipotesis_de_Universalidad_Estructural.docx`.

## Software boundary

The production Java runtime and private integration source are not included. Publication of this repository does not imply publication, transfer, or licensing of the proprietary MDPAR implementation.

## GitHub and Zenodo

This directory is structured to be published as a standalone evidence/documentation repository and deposited as a versioned research artifact.
