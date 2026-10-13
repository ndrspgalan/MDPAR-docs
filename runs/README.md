# MDPAR v2.3.0 — C0–C13 evidence snapshot

`runs/capabilities/` contains the scientific evidence carried by the MDPAR-docs 2.3.0 distribution. 
The package preserves **historical** C0–C12 releases (including 2.0.0, 2.1.0 and 2.2.0) alongside later experiments 
and the **C13** mathematical/algorithmic evidence ledger. The distribution version is not a blanket claim that every
recorded run was executed under 2.3.0.

## Index contract

`runs/index.json` uses `MDPAR_BENCHMARK_EVIDENCE_INDEX_V3` and covers **C0–C13**, including version-qualified and 
unversioned instrument paths. It records each evidence file's path, capability, originating MDPAR version, instrument, 
byte count and SHA-256. For non-C13 files the version/instrument labels are inherited from the retained provenance 
index; the index builder refuses to invent labels for newly added non-C13 files. C13 is assigned the 2.3.0 release 
identity in the authoritative C13 index policy.

`python verification/verify_benchmark_evidence.py` verifies actual bytes against the index.
`python verification/index_benchmark_evidence.py --check-existing` rebuilds and compares the index without rewriting 
the published artifact. Run from the `MDPAR-docs` root.

## C13

`runs/capabilities/C13/` contains `manifest.json`, `provenance.json`, `milestones.json`, `protocol.json`, 
`evidence_index.json` and the algorithm, scientific and regression batches. To regenerate C13 experimental data, use 
the private MDPAR AI adapter and its documented runner; do **not** regenerate the evidence store merely to repair hashes.

## Release discipline

The `checksums/SHA256SUMS.txt` manifest covers the published repository snapshot, excluding `.git`, `.idea` and itself.
Regenerate the index only after an intentional, reviewed evidence change; regenerate the package manifest only after
the complete release tree is final. Source execution tests must be performed separately in the MDPAR code repository.
