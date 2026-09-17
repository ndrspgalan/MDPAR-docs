# MDPAR benchmark evidence store

This directory contains the canonical C0–C12 benchmark evidence for MDPAR. Evidence is organized first by capability (`C0` through `C12`), then by MDPAR release (`MDPAR-v2.0.0`, `MDPAR-v2.1.0`), then by instrument and, where relevant, by neural regime.

The packaging taxonomy is descriptive metadata only. Historical JSON/JSONL/state artifacts are preserved without rewriting their internal provenance, timestamps, run IDs, protocol names or hashes. Timestamp-heavy directory names have been replaced by semantic names such as `Sol-none`, `Sol-high`, `Qwen3-4B-non-thinking`, or `deterministic`.

## Layout

```text
runs/
  capabilities/
    C0/
      MDPAR-v2.0.0/
      MDPAR-v2.1.0/
    ...
    C12/
      MDPAR-v2.0.0/
  README.md
  index.json
```

C0–C5 contain both the historical MDPAR 2.0.0 evidence and the new MDPAR 2.1.0 campaign where available.
C6–C12 currently contain the retained MDPAR 2.0.0 campaign only.

For neural instruments, folder names identify the execution regime directly.
For compound late-capability campaigns (adaptive, sequential, concurrent, frontier recovery,
temporal authority, servant robot), the original internal semantic layout is retained because the run itself contains 
multiple policies or authorities and cannot be reduced to one LLM-effort label.

`index.json` is regenerated from this organized tree and records every evidence file with path,
capability, MDPAR release, instrument, size and SHA-256.

### Preservation note

The three loose C0 v2.0.0 files in the input package were byte-identical duplicates of the timestamped canonical C0
v2.0.0 directory. Only one copy is retained in the organized package; 
no unique evidence was removed.
