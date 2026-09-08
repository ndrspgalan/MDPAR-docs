# MDPAR v2.0.0 — Cooperative Benchmarking Standard

## 1. Purpose and authority

This document is the canonical benchmarking doctrine for MDPAR v2.0.0. It defines what MDPAR must demonstrate when it operates as cooperative software and how experimental evidence is allowed to support those claims.

The machine-readable capability identifiers are mirrored by `app/evaluation/benchmarking_standard.py`. 
The governing distinction is:

- **capability**: what property of cooperative MDPAR is being demonstrated;
- **cross-cutting axis**: a measurement dimension that may be attached to one or more capabilities but is not itself a capability level;
- **evidence stage**: the scientific maturity of a run under a frozen protocol.

No benchmark may redefine CORE, PARSER, ENGINE, TRACK, routing or plugin semantics in order to improve a score.

## 2. Experimental regimes

Two orthogonal execution regimes remain canonical:

### `OFFLINE_CAPABILITY`

Asks whether the selected cognitive tier can perform the requested operation when capability is prioritized over an embodiment deadline. Network access may exist; “offline” does not mean network-disconnected. Frontier-only capability experiments must not silently fall back to a local model.

### `ONLINE_EMBODIMENT`

Asks whether the architecture can operate under an explicit external deadline and availability profile while preserving authority, continuity and safe degradation. Provider availability, local compute budgets and action deadlines belong to the embodiment profile, not to universal MDPAR semantics.

Passing one regime does not imply passing the other.

## 3. Cooperative capability taxonomy

The canonical capabilities are `C0-C12`, where `C` means **Cooperative Capability**. They are not levels, a scalar intelligence score, or an ordinal ladder and must not be averaged. Later identifiers do not erase the obligation to preserve invariants established by earlier capabilities.

### C0 — Contractual reproducibility

MDPAR demonstrates that the evaluated system is exactly the system claimed by the run.

Required evidence includes, where applicable:

- MDPAR version and JAR hash;
- adapter version and source hash;
- Java/Python boundary parity;
- protocol and corpus identifiers plus content hashes;
- provider/model/settings and retry semantics;
- source modality and provenance coordinates;
- Java UTF-16 span semantics for textual OPEN input;
- explicit representation of `NOT_ESTIMABLE` / absence rather than synthetic neutral, best or worst values;
- deterministic Java verification state;
- presence of normative OPEN knowledge resources in the runtime artifact.

C0 establishes epistemic traceability, not reasoning competence.

### C1 — Structural identification

MDPAR demonstrates that observations can be projected onto the SCC structural vocabulary without conflating domain semantics with structural position.

Evidence may cover:

- `StateType` identification;
- occurrence identity and order;
- relation endpoints and explicitness;
- trajectory boundaries;
- source spans;
- `UNKNOWN` as unresolved canonical SCC assignment rather than ontological absence;
- preservation of source provenance.

The LLM or external observer may propose observations. The parser assembly and CORE remain the structural authorities.

### C2 — Structural metrology

MDPAR demonstrates that C1 observations can be measured for repeatability, discriminability and stability without inventing evidence.

The standard explicitly requires:

`absence of comparable evidence != 0`

`absence of comparable evidence != 1`

`absence of comparable evidence = NOT_ESTIMABLE`

Repeated measurements are permitted only when repetition itself is part of the metrological question. Repetition must never serve as semantic retry until a desirable claim appears.

### C3 — Structural calculus and directional continuity

MDPAR demonstrates the current mathematical SCC calculus rather than only a directional label.

The evaluation surface includes:

- positive occurrence trajectories;
- the forward occurrence DAG;
- recurrence after state/radial projection without occurrence-cycle fabrication;
- radial depth and radial pseudometric properties;
- orbital localization of `WHEN`, `WHERE` and `HOW_MUCH`;
- `UNKNOWN` gap topology;
- local/global closure, including nested, overlapping and disjoint cases;
- `ThoughtDirection`;
- `GENERATIVE_LINK`, `INTERPRETIVE_PROJECTION` and `CHAIN_CONNECTOR`;
- continuity and restart persistence where relevant.

C3 must contain deterministic tests that make no neural call where the property is wholly owned by MDPAR.

### C4 — Structural transformation and equivalence

MDPAR demonstrates what is preserved, transformed or lost when one structural realization is converted into another.

The canonical authority is the current exact structural report, not prior ordinal equivalence classes. Evidence may independently test:

- occurrence bijection;
- state-label preservation;
- relation bijection;
- endpoint preservation;
- typed `TransitionType` transformation;
- undirected topology preservation;
- exact structural equivalence;
- admissible permutation realization and re-identification.

Agreement of coarse invariants is never sufficient evidence of exact isomorphism.

### C5 — Contextual cooperation

MDPAR demonstrates cooperation between external semantic interpretation and MDPAR structural authority during an unfolding task.

Typical pipeline:

`observation -> structural identification -> contextual direction -> candidate contribution -> structural verification -> optional transformation -> final verification`

The benchmark must keep distinct:

- semantic appropriateness;
- SCC structural validity;
- contextual direction;
- realization quality;
- abstention or `UNKNOWN` caused by genuine underdetermination.

### C6 — Longitudinal cognition and epistemic timing

MDPAR demonstrates continuity of structural reasoning across temporally separated evidence.

Evidence may include:

- remembered observations and hypotheses;
- later evidence that confirms, narrows or revises earlier structure;
- persistent `UNKNOWN` where evidence remains insufficient;
- longitudinal remembrance;
- reinterpretation without rewriting prior occurrence identity;
- persistence/restart behavior;
- separation of current structural state from raw prior narrative.

TRACK is the longitudinal authority. A model narrative summary is not a substitute for TRACK state.

### C7 — Bounded and heterogeneous CLOSED intelligence

MDPAR demonstrates that formally bounded local intelligences can participate without CORE acquiring their domain semantics.

Evidence must cover more than a single single demonstration and should include heterogeneous domain/profile coordinates, where appropriate:

- lexical and typed ingress;
- profile eligibility;
- structural reading separated from domain evidence;
- domain-specific marks and admissibility policies;
- operational publication;
- deterministic bounded execution.

CLOSED domain metrics are local to their profile unless a separate proof establishes cross-profile comparability.

### C8 — CLOSED/OPEN cooperative composition

MDPAR demonstrates that heterogeneous observations can be routed and composed across CLOSED and OPEN without delegating structural ownership to an LLM.

Evidence should include:

- representation filtering before ownership competition;
- lexical and typed routes;
- OPEN fallback only when routing semantics permit it;
- multiple CLOSED profiles in one runtime;
- mixed CLOSED/OPEN streams;
- conflict resolution and `CONFLICT_RESOLVED` provenance;
- continued longitudinal identity across routing decisions;
- explicit separation between a routing competition unit and semantic segmentation.

### C9 — Adaptive and concurrent cognition

MDPAR demonstrates that multiple cognitive workloads can be scheduled without turning temporal policy into domain semantics.

Evidence may include:

- foreground/background cognition;
- reasoning tiers;
- pending and completed work;
- concurrency;
- queue pressure;
- external cognitive scheduling boundaries;
- future-state-only cognition;
- resource adaptation under an explicit policy.

The benchmark must distinguish scheduling outcome from reasoning correctness.

### C10 — Temporal authority and embodiment

MDPAR demonstrates that cognition is authorized by when it becomes available relative to an external action commitment.

The canonical invariant is:

`late cognition != permission to rewrite a committed action`

Evidence may include:

- explicit deadlines;
- authority capture;
- frontier-before-deadline completion;
- local completion before/after deadline;
- safe abstention;
- committed action identity;
- late completions retained as evidence without retroactive authority.

### C11 — Degradation, continuity and recovery

MDPAR demonstrates coherent behavior through availability loss and restoration while the embodied episode continues.

The canonical frontier transition is:

`FRONTIER_AVAILABLE -> FRONTIER_UNAVAILABLE -> FRONTIER_AVAILABLE`

This transition is not called `OFFLINE -> ONLINE`; `OFFLINE_CAPABILITY` and `ONLINE_EMBODIMENT` are evaluation regimes and must remain semantically distinct.

C11 evidence must test, where applicable:

- CLOSED continuity while frontier OPEN is unavailable;
- certified local OPEN delegation only for gates actually supported by evidence;
- deterministic safe state/abstention otherwise;
- preservation of pending-work identity;
- transport of reconstructable task state rather than fictitious migration of hidden model state;
- stale-result identification;
- restoration of frontier authority;
- migration/reissue of transportable pending work after restoration;
- prohibition on retroactive rewriting of committed actions;
- preservation of the same longitudinal episode through degradation and recovery.

### C12 — Sustained system cooperation

C12 is the capstone integration capability. It is not valid until C0-C11 protocols needed by the scenario are frozen independently.

The canonical C12 scenario is a sustained servant-robot episode of approximately five minutes under `ONLINE_EMBODIMENT` in which:

1. the robot begins with frontier OPEN available;
2. natural inputs continue throughout the episode;
3. three heterogeneous CLOSED plugins remain installed and active;
4. CLOSED, OPEN and mixed inputs occur during normal operation;
5. routing conflicts/interactions occur without an LLM owning routing authority;
6. TRACK preserves longitudinal continuity;
7. frontier OPEN becomes unavailable at a prospectively fixed time/event;
8. the embodied world and CLOSED processing continue;
9. OPEN degrades only according to certified local capabilities and deterministic safe-state policy;
10. pending cognitive work remains traceable;
11. cognitive debt may accumulate without being hidden;
12. locally completed work may become late or stale;
13. frontier OPEN is restored at a prospectively fixed time/event;
14. reconstructable pending work is reissued/migrated to frontier authority where policy requires it;
15. stale or superseded completions are identified rather than silently merged;
16. no late result rewrites an already committed action;
17. new inputs continue during recovery;
18. all three CLOSED plugins remain available throughout unless the scenario explicitly injects a separate CLOSED fault;
19. the runtime completes the same episode without resetting structural or longitudinal identity.

C12 is reported as an invariant vector plus transverse measurements. There is no single C12 score. Violation of a required safety/authority invariant is a failed capstone result even if latency or model quality is otherwise high.

The exact five-minute duration, fault injection times, workload schedule, deadlines, plugin profiles, models and corpus must be frozen prospectively before the confirmatory run. They are protocol parameters, not universal MDPAR constants.

## 4. Orthogonal evidence planes

Every canonical result is described on three independent planes:

`Capability x Scientific Axes x Economic Ledger`

The planes answer different questions and must not be collapsed into a single score.

- `C0-C12` states **what cooperative capability is being demonstrated**.
- `P/A/G` states **which scientific property of the experiment is being measured**.
- `E_MDPAR=(C,T,I,M,Q)` states **which economic/operational consequences are being accounted for**.

A run may legitimately have no scientific axis or no economic dimension. A purely transverse benchmark may also have no `C0-C12` capability, provided at least one scientific axis or economic dimension is declared.

### 4.1 Scientific axes

#### P — Performance

Performance measures computational/temporal behavior at a named boundary: native Java latency, Python-JVM bridge wall time, provider latency, throughput, persistence overhead, queue delay, deadline distributions, latency hiding and memory/compute utilization.

Performance is not the economic ledger. A P measurement may later feed the economic time dimension `T`, but the scientific observation and its economic interpretation remain distinct records.

#### A — Attribution

Attribution asks what caused an observed difference. It requires a prospectively specified contrast or ablation and explicit separation of MDPAR authority, SCC externalization, reasoning effort, provider stochasticity, scheduling and backend effects.

Association is not attribution. No weighted attribution score is permitted.

#### G — Generalization

Generalization is the support matrix actually exercised: domains, profiles, languages, modalities, providers/models, transformations and hardware environments. It is never a universality score.

Profile-local quantities remain profile-local unless a proof/protocol establishes comparability.

### 4.2 Economic ledger

The canonical economic ledger is:

`E_MDPAR=(C,T,I,M,Q)`

where:

- `C — Cost/compute`: input/cached-input/output/reasoning/total tokens, requests, monetary cost from a dated pricing snapshot, accelerator-time when measurable.
- `T — Time`: wall-time, foreground latency, p50/p95/p99 where justified, deadline misses, exposed tail and latency hidden.
- `I — Infrastructure`: accelerator capacity, RAM/VRAM, bandwidth, queue depth, availability, MW/GW or capacity-equivalent shares when the denominator is explicit.
- `M — Maintenance`: model-coupled control-plane surface, adapters, retesting, churn, engineer-hours and incidents when actually measured or scenarized.
- `Q — Capability/quality`: sufficiency, exactness, coverage, availability, invariants and safety conditions that prevent declaring an economic gain by degrading the service.

The governing optimization is not "minimize cost". It is resource minimization subject to an explicit capability floor:

`min(C,T,I,M) subject to Q >= Q_required`

`Q` is therefore a guardrail as well as an economic dimension.

### 4.3 Economic provenance

Every economic quantity must identify one of four provenance classes:

- `MEASURED`: observed directly in a run/benchmark;
- `DERIVED`: mechanically computed from measured or published quantities;
- `SCENARIO`: explicit planning assumption, not an experimental result;
- `FUTURE`: known variable whose value requires a pending evaluation.

These classes are independent of `EvidenceStage`. A `FROZEN` campaign may contain `MEASURED`, `DERIVED`, `SCENARIO` and `FUTURE` entries.

### 4.4 No double counting

A physical/economic unit can be claimed once. The canonical mechanisms are distinguished as:

- `COMPUTE_AVOIDED`;
- `LATENCY_HIDDEN`;
- `CAPACITY_RELEASED`;
- `MAINTENANCE_DISPLACED`.

A HIGH call avoided by adaptive allocation cannot also be counted as a HIGH call hidden by concurrency. A frontier call removed by CLOSED cannot simultaneously be counted as an OPEN-routing saving. Derived monetary reporting must preserve the identity of the underlying resource unit or aggregate population so that this rule is auditable.

### 4.5 Pricing and hardware

Provider prices are analysis-time snapshots, never immutable run evidence. Raw token/request quantities must be retained so a later pricing snapshot can be applied without rewriting the run.

Local inference is hardware-bound. Any local-model result must bind a profile from `HARDWARE-PROFILES.json` and record effective model/runtime settings. The 2026 reference laptop is a measured environment, not an MDPAR requirement.

## 5. Evidence maturity

- `DEVELOPMENT`: protocol/instrument may still change after diagnostic findings.
- `CONFIRMATORY`: protocol, corpus, analysis plan and relevant environment are frozen before execution.
- `FROZEN`: evidence package is closed and citable. `FROZEN` does not mean positive.



## 6. Evidence classes and failure semantics

Each record/run must distinguish:

- valid positive structural observation;
- valid negative/disconfirming result;
- `UNKNOWN` / structural underdetermination;
- `NOT_ESTIMABLE` because a comparison is undefined;
- neural `UNEVALUABLE` because a model claim could not be completed/parsed;
- provider/transport failure;
- adapter failure;
- JVM/MDPAR failure;
- protocol violation;
- invariant violation.

A neural invalidity must never be silently replaced by repeated neural attempts unless repetition is the measured phenomenon. Transport retry after no neural claim was produced must be counted separately.

## 7. Metric doctrine

1. No universal confidence, intelligence, quality, capability or economic score is permitted.
2. No weighted aggregate may conceal failure of a required component.
3. Profile-local metrics remain profile-local unless comparability is established.
4. `StructuralMark` is a non-ordinal property seal.
5. Exact equivalence is established by the current structural equivalence contract, not by coarse invariants.
6. Missing experiments remain absent/not estimable.
7. P/A/G and C/T/I/M/Q qualify capability evidence; none can replace structural/authority validity.
8. A C12 safety/authority invariant cannot be compensated by lower cost, lower latency or higher semantic quality.
9. A saving at equivalent capability may be claimed only when the treatment does not regress any required baseline capability case under the comparison protocol.

## 8. Corpus doctrine



## 9. Manifest doctrine

Every new canonical run manifest declares, as applicable:

- `mdpar_version` and `mdpar_jar_sha256`;
- `adapter_version` and adapter source hash;
- `protocol`;
- `capabilities`: zero or more of `C0-C12`;
- `scientific_axes`: zero or more of `P`, `A`, `G`;
- `economic_dimensions`: zero or more of `C`, `T`, `I`, `M`, `Q`;
- `evidence_stage`;
- `evaluation_regime`;
- corpus identity/hash;
- model/provider/settings where neural calls occur;
- retry/repetition policy;
- hardware profile when relevant;
- start/end timestamps;
- explicit status/failure semantics.




## 10. Paired adaptive economics authority



Its scientific question is causal allocation: paired `ALWAYS_HIGH` versus MDPAR-gated `ADAPTIVE`, same case corpus, deterministic AB/BA arm ordering, sequential execution to isolate acquisition from concurrency, and gold labels excluded from the sufficiency gate.

Its canonical identity is:

- capability: `C9`;
- scientific axes: `P+A`;
- economic dimensions: `C+T+Q`.



A compute/time saving is called equivalent-capability saving only when no case solved by `ALWAYS_HIGH` regresses under `ADAPTIVE`. A treatment may rationally spend more resources when it increases `Q`; such a result demonstrates adaptive allocation, not universal cheapness.

Pricing is applied only in analysis from a dated snapshot. Canonical run evidence preserves raw usage.


## 11. Reporting doctrine

Every headline result states:

- capability context;
- scientific axes;
- economic dimensions if any;
- economic provenance (`MEASURED`, `DERIVED`, `SCENARIO`, `FUTURE`) for each economic quantity;
- regime;
- protocol/corpus/hash;
- evidence stage;
- model/provider/hardware when relevant;
- invariant/metric vector;
- comparison arm when applicable;
- negative, mixed and unevaluable evidence;
- generalization/attribution limitations.


