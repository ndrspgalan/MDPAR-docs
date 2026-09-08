# MDPAR v2.0.0 — Transverse measurement standard

This document is subordinate to `MDPAR-BENCHMARKING-STANDARD.md`. It governs the scientific axes `P/A/G`, the economic ledger `E_MDPAR=(C,T,I,M,Q)`, evidence provenance and hardware binding. None creates a new Cooperative Capability.

## 1. Three-plane model

Canonical evidence is located as:

`Capability x Scientific Axis x Economic Ledger`

A run may therefore be `C9 + P+A + C/T/Q`, `C10 + P+A + T/Q`, or purely `P` without inventing another capability.

## 2. Scientific axes

### P — Performance

Measure only named boundaries: native Java, Python↔JVM bridge, provider/neural wall, queue, persistence, foreground completion, exposed tail, throughput or latency hidden. Never collapse them into a generic speed score.

Concurrency may establish latency hiding. It does not establish compute avoidance.

### A — Attribution

A requires a specified contrast/ablation. Separate MDPAR authority, SCC externalization, reasoning effort, provider stochasticity, scheduling and backend effects. Association is not causal attribution.

### G — Generalization

Report the tested support matrix: domains/profiles, languages, modalities, providers/models, transformations and hardware. Do not infer universality from coverage.

## 3. Economic ledger E_MDPAR=(C,T,I,M,Q)

### C — Cost/compute

Requests; input, cached-input, output, reasoning and total tokens; accelerator-time where measurable; and money only after applying a dated pricing snapshot.

### T — Time

Wall time, foreground latency, p50/p95/p99 when sampling supports them, deadline misses, latency hidden, queue waiting and exposed tail.

### I — Infrastructure

RAM/VRAM, accelerator capacity, bandwidth, queue depth, service availability and explicit capacity-equivalent denominators. Do not infer joules or MW directly from tokens without a measured conversion.

### M — Maintenance

Control-plane LOC, model-coupled churn, adapter surface, regression work, engineer-hours and incidents. These remain `FUTURE` or `SCENARIO` until directly measured.

### Q — Capability/quality

Sufficiency, exactness, coverage, availability, invariants and safety. Q prevents a cheaper but weaker treatment from being sold as an equivalent economic improvement.

The economic decision rule is:

`min(C,T,I,M) subject to Q >= Q_required`

## 4. Provenance of economic quantities

Every economic datum is one of:

- `MEASURED` — directly observed;
- `DERIVED` — mechanical transformation of measured/published inputs;
- `SCENARIO` — planning assumption;
- `FUTURE` — known variable still awaiting measurement.

This is orthogonal to evidence maturity (`DEVELOPMENT`, `CONFIRMATORY`, `FROZEN`).

## 5. No-double-counting rule

A physical/economic unit is saved once. Keep separate:

- `COMPUTE_AVOIDED`;
- `LATENCY_HIDDEN`;
- `CAPACITY_RELEASED`;
- `MAINTENANCE_DISPLACED`.

Example: a HIGH call eliminated by adaptive allocation cannot also be counted as latency hidden by concurrent execution. A frontier call eliminated by CLOSED cannot also be counted as an OPEN-routing saving.

## 6. Pricing snapshots

Raw provider usage is canonical run evidence. Prices are mutable external inputs attached at analysis time with date/source/model/tier. Repricing must not require rerunning or mutating the original campaign.

## 7. Hardware binding

Local inference results bind an explicit `HARDWARE-PROFILES.json` profile plus effective model/runtime settings. The reference hardware profile is the ASUS TUF Gaming A15 FA507RR with Ryzen 7 6800H, 16 GB nominal DDR5 and RTX 3070 Laptop GPU with 8 GB physical GDDR6 VRAM. `num_ctx=8192` is a measured local configuration, not an MDPAR constant.

Prior Qwen3 4B evidence establishes only what was actually tested. Failure to meet a foreground deadline on this laptop is a `(model, hardware, configuration, deadline)` result, not an abstract incapacity of MDPAR.

## 8. Naturalistic composite campaign

Prior order is fixed:

`AI Engineering exam -> Longitudinal book -> Fair`


| Scenario | Capability | Scientific axes | Economic dimensions |
|---|---|---|---|
| AI Engineering exam | C10 | P, A | T, Q |
| Longitudinal book | C6, C9 | P | C, T, Q |
| Fair | C10 | P, A | C, T, Q |

The book was introduced after the exam activated no HIGH and deliberately increased longitudinal difficulty/data volume. Prior telemetry: 4,930,997 total tokens; 22,792 HIGH tokens; HIGH exposure 0.4622%; non-HIGH exposure 99.5378% (~99.54%). This is not an ALWAYS_HIGH counterfactual.

C12 servant robot is a later capstone, not a fourth member of this triad.

## 9. Paired adaptive economics

`C9_PAIRED_ADAPTIVE_ECONOMICS_V1` carries `C9 + P/A + C/T/Q`. It compares paired `ALWAYS_HIGH` and `ADAPTIVE` arms on the same workload cases and preserves the guardrail that a raw reduction is not called an equivalent-capability saving if ADAPTIVE regresses a case solved by ALWAYS_HIGH.

The canonical C9 workload families are `CONTEXTUAL_DIRECTION` and `CONTEXTUAL_ADAPTATION`.

## 10. Reporting

Do not emit a universal transverse/economic score. Report vectors, invariants, denominators, provenance, evidence maturity and limitations. Scientific performance and economic time can share raw measurements while remaining semantically distinct layers.
