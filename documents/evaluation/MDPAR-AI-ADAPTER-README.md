# MDPAR AI Adapter

Thin Python integration, API and evidence layer for the Java MDPAR runtime.

The adapter has three responsibilities:

1. bridge Python to one longitudinal JVM runtime through JPype;
2. preserve `mdpar_routing` authority for CLOSED ownership and delegate only authorized OPEN semantic identification to external models;
3. execute reproducible C0–C12 evidence protocols without redefining MDPAR semantics.

MDPAR remains authoritative for installed CLOSED coordinates, OPEN structural knowledge, SCC rules, ENGINE execution, TRACK continuity and publication/embodiment boundaries.

## Build

From the MDPAR root:

```powershell
mvn clean package
cd mdpar-ai-adapter
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest tests -v
```

The adapter auto-discovers the newest `target/mdpar-*.jar`; `MDPAR_JAR` may override the path explicitly. Local-model runs must record their provider settings and hardware profile. The reference hardware profile is `andres-reference-laptop-2026` in `docs/evaluation/HARDWARE-PROFILES.json`.

## Public expert-assessment surface

The public FastAPI/OpenAPI contract is deliberately narrow:

- `GET /health`
- `GET /runtime`
- `POST /assessment`
- `GET /reports/{interaction_id}/{filename}`

`POST /assessment` is the single operational service. It accepts one or more evidence files and executes one exhaustive, traceable structural assessment. Domain semantics are inferred from the submitted evidence through the MDPAR + semantic-frontier pipeline; there is no caller-selected domain or semantic profile. `interaction_id` and the client-report language are optional. MDPAR runtime version and JAR SHA-256 are observed from the loaded artifact rather than declared by the caller.

Direct `/closed`, `/open`, `/reason` and OPEN-knowledge surfaces remain available for engineering/evaluation integration but are excluded from Swagger. The service contract is specified in `docs/OPERATIONAL-ASSESSMENT-CONTRACT.md`. The operator-facing specification is `docs/Manual_operativo_Swagger_MDPAR_v2.0.0.md`.

The report pipeline is designed for expert-report quality: source custody, explicit authority boundaries, uncertainty preservation, reproducibility metadata and publication from one canonical analysis are mandatory properties of the contract. External legal admissibility or evidentiary weight are not runtime decisions.

## Evaluation doctrine

The canonical doctrine is `docs/evaluation/MDPAR-BENCHMARKING-STANDARD.md`. C means **Capability**. C0–C12 are distinct capabilities, not levels or scores. Scientific axes are `P` (performance), `A` (attribution) and `G` (generalization). Economics is a separate ledger `E_MDPAR=(C,T,I,M,Q)` for cost/compute, time, infrastructure, maintenance and capability/quality.

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

Canonical capability entry points:

```powershell
python -m scripts.run_c0_contractual_reproducibility
python -m scripts.run_c1_structural_identification --provider openai --model gpt-5.6-sol
python -m scripts.run_c2_structural_metrology --provider openai --model gpt-5.6-sol --repeats 3
python -m scripts.run_c3_structural_calculus
python -m scripts.run_c3_directional_continuity
python -m scripts.run_c4_permutation_realization --provider openai --model gpt-5.6-sol
python -m scripts.run_c4_translation_invariance --provider openai --model gpt-5.6-sol
python -m scripts.run_c5_contextual_direction --provider openai --model gpt-5.6-sol
python -m scripts.run_c6_longitudinal_narrative --source-pdf <path-to-source.pdf>
python -m scripts.run_c7_heterogeneous_closed
python -m scripts.run_c8_closed_open_composition --provider openai --model gpt-5.6-sol
python -m scripts.run_c9_paired_economics
python -m scripts.run_c10_temporal_authority
python -m scripts.run_c11_frontier_recovery
python -m scripts.run_c12_servant_robot
```

C4 exactness is deliberately stronger than textual similarity: exact structural equivalence requires occurrence correspondence and preservation of the required typed relations/endpoints. Missing evidence remains missing; it is never converted into a synthetic score.

Every evidence manifest records software identity, hashes, protocol, capabilities, scientific axes, economic dimensions, evidence stage, regime, environment, timestamps and status. Provider/model settings and corpus hashes are recorded whenever they participate in a claim. Canonical C0–C12 benchmark runs are retained under `runs/capabilities/` as immutable scientific evidence; `runs/index.json` binds every retained evidence file by SHA-256. See `docs/evaluation/BENCHMARK-EVIDENCE-STORE.md`.

## Source layout

- `app/` — bridge, routing/ingress, providers, reporting and evaluation harnesses.
- `corpus/` — canonical fixtures used by current protocols.
- `docs/evaluation/` — normative evaluation, metrology and evidence-store documentation.
- `runs/` — retained C0–C12 benchmark evidence plus a deterministic integrity index.
- `scripts/` — current C0–C12 runners/analyzers, evidence verification and operational utilities.
- `tests/` — tests named by current contracts and components.
