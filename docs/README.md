# MDPAR-docs — Verification and integrity

MDPAR-docs is the versioned public evidence and reproducibility repository associated with **MDPAR v2.3.0**.
It contains scientific documentation, corpora, benchmark records and deterministic verification utilities. 
Its evidence inventory covers **C0–C13**. Historical experiments retain their original execution versions and provenance.

The repository distinguishes two independent verification levels:

- **Package integrity:** validate every file listed in `checksums/SHA256SUMS.txt` against its SHA-256 digest.
- **Benchmark evidence integrity and reproducibility:** validate the indexed evidence files and independently
reconstruct `runs/index.json` without altering it.

All commands below are executed from the **root of MDPAR-docs**.

## 1. Package integrity — Linux / Git Bash

### Verify the published manifest

```bash
sha256sum -c checksums/SHA256SUMS.txt
```

Every listed file should report `OK`. A missing file or a digest mismatch indicates that the local package differs 
from the recorded distribution.

### Generate a manifest for a new distribution

```bash
find . -type f \
  ! -path './.git/*' \
  ! -path './.idea/*' \
  ! -path './checksums/SHA256SUMS.txt' \
  -print0 | LC_ALL=C sort -z | xargs -0 sha256sum | sed 's#  \./#  #' > checksums/SHA256SUMS.txt
```

The manifest excludes `.git/`, `.idea/` and `checksums/SHA256SUMS.txt`. The manifest cannot contain a stable hash of
its own final contents.

## 2. Package integrity — Windows PowerShell

The following commands work in **Windows PowerShell 5.1** and PowerShell 7 without requiring `sha256sum`.

### Verify the published manifest

```powershell
$errors = 0
$verified = 0

foreach ($line in [System.IO.File]::ReadAllLines((Join-Path $PWD.Path 'checksums\SHA256SUMS.txt'))) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    if ($line -notmatch '^([0-9a-fA-F]{64}) [ *](.+)$') {
        Write-Host "INVALID  $line"
        $errors++
        continue
    }
    $expected = $matches[1].ToLowerInvariant()
    $relative = $matches[2]
    $path = Join-Path $PWD.Path ($relative.Replace('/', '\'))
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Write-Host "MISSING  $relative"
        $errors++
        continue
    }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $expected) {
        Write-Host "FAILED   $relative"
        $errors++
    } else {
        $verified++
    }
}

Write-Host "verified_files=$verified"
if ($errors -eq 0) {
    Write-Host 'SHA256SUMS: PASS'
} else {
    Write-Host "SHA256SUMS: FAIL ($errors errors)"
    throw 'Package integrity verification failed.'
}
```

### Generate a manifest for a new distribution

```powershell
$root = (Get-Location).Path
$manifest = Join-Path $root 'checksums\SHA256SUMS.txt'
$files = Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object {
    $_.FullName -notmatch '[\/](\.git|\.idea)[\/]' -and
    $_.FullName -ne $manifest
} | Sort-Object { $_.FullName.Substring($root.Length + 1).Replace('\','/') } -CaseSensitive

$lines = foreach ($file in $files) {
    $relative = $file.FullName.Substring($root.Length + 1).Replace('\','/')
    $hash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    "$hash  $relative"
}
[System.IO.File]::WriteAllText($manifest, (($lines -join "`n") + "`n"), (New-Object System.Text.UTF8Encoding($false)))
```

The manifest uses repository-relative paths separated by `/`, SHA-256 in lowercase hexadecimal and UTF-8 **without BOM**.

## 3. Benchmark evidence verification

The two verification utilities are part of this repository. Python 3 is required; on Windows, the Python launcher `py` 
can be used instead of `python`.

### 3.1 Verify the evidence store

Linux / Git Bash:

```bash
python verification/verify_benchmark_evidence.py
```

Windows PowerShell:

```powershell
py verification/verify_benchmark_evidence.py
```

Expected result for the MDPAR-docs v2.3.0 evidence inventory:

```text
verified_files=1784
evidence_integrity=PASS
```

The verifier checks the existence, byte length and SHA-256 of every file listed in `runs/index.json`.

### 3.2 Verify reproducibility of the evidence index

Linux / Git Bash:

```bash
python verification/index_benchmark_evidence.py --check-existing
```

Windows PowerShell:

```powershell
py verification/index_benchmark_evidence.py --check-existing
```

Expected result:

```text
evidence_index_rebuild=PASS
```

The index builder reconstructs the inventory from `runs/capabilities/`, using stable repository-relative path ordering
and the version/instrument provenance retained in the canonical index. Verification compares the reconstructed JSON 
data with the committed index without rewriting it. Line-ending and JSON presentation differences do not affect this
semantic comparison.

## 4. Recommended verification sequence

For a cloned, downloaded, archived or independently inspected distribution:

1. Verify `checksums/SHA256SUMS.txt` using Section 1 or Section 2.
2. Verify the benchmark evidence using Section 3.1.
3. Verify deterministic reconstruction using Section 3.2.

A consistent MDPAR-docs v2.3.0 distribution reports:

```text
SHA256SUMS: PASS
verified_files=1784
evidence_integrity=PASS
evidence_index_rebuild=PASS
```

## 5. Regeneration and verification are distinct operations

A verification operation must compare the existing files against the **published** manifest or index. Regenerating an 
integrity manifest before checking a downloaded distribution replaces the expected values and invalidates the purpose
of the check.

Manifest generation is appropriate when assembling a new versioned distribution. The evidence index is regenerated
only when the evidence tree or its provenance has changed intentionally. A new package manifest is generated after
all distribution files are finalized and is then verified before archival or publication.

## 6. Scope of verification

Package and evidence checks establish byte-level integrity and index reproducibility. They do not independently 
reproduce external model calls or establish mathematical theorems from finite experiments. The underlying MDPAR Java 
and Python application build and tests belong to the separate MDPAR source repository.

For scientific scope and citation conventions, see `runs/README.md`, `docs/Citation-template.md`, `RIGHTS-NOTICE.md` 
and `LICENSE`.
