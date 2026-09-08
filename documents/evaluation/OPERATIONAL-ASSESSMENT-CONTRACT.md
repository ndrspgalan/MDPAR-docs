# MDPAR Expert Assessment Contract

## Purpose

The public API has one operational purpose: execute an exhaustive, traceable structural assessment of submitted evidence with the quality controls required for expert-report use. The service is intentionally narrow. It is not a catalogue of user-selectable C0–C12 capabilities, objectives or domains, and it does not allow callers to select CLOSED or OPEN execution.

Canonical purpose:

`EXHAUSTIVE_STRUCTURAL_EVIDENCE_ASSESSMENT`

MDPAR applies the structural capabilities required by the evidence and runtime state. C0–C12 remain internal capability/evidence contracts, not Swagger options.

## Domain agnosticism

The caller does not provide any domain selector or semantic profile. Domain semantics are inferred from the evidence through the MDPAR + semantic-frontier pipeline and, where applicable, through installed CLOSED coordinates. MDPAR retains routing and structural authority.

The public product contract is therefore:

`one structural assessment + evidence -> domain-sensitive expert report realization`

The domain changes the semantic variables that become observable and the form in which the result is explained; it does not replace the common structural formalism or create a user-selected ontology.

## Public Swagger surface

Only four routes are public in the OpenAPI schema:

- `GET /health`
- `GET /runtime`
- `POST /assessment`
- `GET /reports/{interaction_id}/{filename}`

Engineering endpoints for direct CLOSED, OPEN and canonical-ingress execution remain available to tests/integration but are excluded from Swagger.

## Assessment request

`POST /assessment` accepts one or more evidence files. One file is sufficient. Additional evidence is optional and supports annexes, opposing evidence, versions, longitudinal material or other documents belonging to the same case.

Required fields:

- `file`: primary supported document;
- `source_language`: default source language;
- `operator_report_language`: operator report language.

Optional fields:

- `additional_file_1` … `additional_file_7`: optional additional evidence documents from the same case;
- `client_report_language`: if absent, only the operator report is generated;
- `interaction_id`: if absent, the service creates a new case identifier; if supplied, it can continue a longitudinal case;
- `evidence_metadata`: optional UTF-8 JSON file uploaded through the normal file picker. Its array is aligned with the evidence files in field order and each item may provide `document_id`, `role`, `source_language`, and `observed_at`.

The MDPAR version is never declared by the caller. It is observed from the loaded runtime JAR and bound to its SHA-256 in audit provenance.

## Evidence custody

Each uploaded item receives its own original-file hash and extracted-text hash. The exact text surface analyzed by MDPAR receives a composite hash. For multiple files, provenance records the UTF-16 code-unit span occupied by each extracted document in that composite surface; no synthetic document labels are inserted into the analyzed text.

## Expert-quality boundary

The service contract requires source integrity, explicit authority boundaries, uncertainty preservation, provenance, reproducibility metadata, declared neural boundaries and derivation of every human report from one canonical analysis. These are implemented quality properties, not a marketing objective.

They do not imply that a court, regulator, scientific body, employer or other external authority must admit a report, appoint its operator as an expert or assign it a predetermined evidentiary weight. Those are institutional decisions external to the runtime.


## Human-report completeness

The canonical JSON is the machine-readable source of truth, but the generated DOCX is required to be self-sufficient for a human expert reader. It must expose the substantive canonical findings and the MDPAR structural/audit context needed to interpret them; the JSON is retained as the original technical record, not as a substitute for a usable report.

## Direct-LLM comparison boundary

OPEN does not create a claim that a frontier model used directly could not produce semantically similar prose. Without a paired baseline on the same evidence, the service does not claim semantic superiority or exclusivity. The auditable MDPAR delta is architectural: MDPAR-owned routing, canonical structure, continuity, structural operations, provenance, runtime identity, deterministic/neural separation and authority boundaries. Semantic similarity is therefore compatible with MDPAR operation and does not establish system equivalence.


## Forensic extraction coverage

`EXHAUSTIVE_STRUCTURAL_EVIDENCE_ASSESSMENT` is exhaustive only over the textual surface actually extracted and recorded in the evidence descriptor. Every item publishes `extraction_coverage`, including examined and unexamined surfaces and a claim limit. The service must not infer the absence of signatures, images, annotations, metadata or other features from a surface that the extractor did not inspect. DOCX extraction covers body paragraphs/tables in document order plus section headers/footers; visual/OLE/comment/tracked-change/package-authenticity surfaces remain outside this adapter. PDF ingestion is text-layer only and does not constitute visual/OCR/attachment examination.

## Exact adapter identity

Every assessment records both `adapter_version` and `adapter_source_sha256`. The source digest covers runtime Python under `app/` and `scripts/` plus `requirements.txt`, excluding mutable runs, reports, caches, tests and virtual environments. Version labels are descriptive; the source hash is the exact executable-code identity required for contradiction and replay.

## OPEN structural stability probe

A wholly OPEN single-dispatch assessment performs two additional structural-identification observations over the exact same composite text without committing longitudinal state. The canonical run is never averaged or replaced. The provenance records exact structural signatures and reports `STABLE_EXACT`, `VARIATION_OBSERVED`, or a failure/not-applicable state. Exact matching requires identical grounded state spans/evidence, relation edges/types/evidence, and trajectory boundaries. This probe measures the neural identification boundary; it does not make OPEN deterministic.


## Execution telemetry

Each assessment records `execution_timing` from the same runtime phase events emitted to the operational log. The record preserves phase order and, where available, completion/failure status, wall-clock duration and operational detail. Repeated phases remain separate observations.

Execution timing has `OBSERVABILITY_ONLY` authority. It is not a StructuralMark input, does not change canonical findings or routing authority, and exact timing equality is not required for replay because hardware, network conditions and provider latency are mutable.
