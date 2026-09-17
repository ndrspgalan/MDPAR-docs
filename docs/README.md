# MDPAR-docs --- Verification and integrity

This repository is the public evidence and reproducibility surface
associated with MDPAR 2.2.0.

The commands below serve two different purposes:

1.  **Package integrity** --- regenerate and verify
    `checksums/SHA256SUMS.txt`.
2.  **Benchmark evidence verification** --- verify the canonical MDPAR
    evidence store and confirm that its evidence index can be rebuilt
    without divergence.

Run the commands from the **root directory of `MDPAR-docs`**.

------------------------------------------------------------------------

## 1. Package integrity --- Linux / Git Bash

### Regenerate `SHA256SUMS.txt`

``` bash
find . -type f \
  ! -path './.git/*' \
  ! -path './.idea/*' \
  ! -path './checksums/SHA256SUMS.txt' \
  -print0 | sort -z | xargs -0 sha256sum | sed 's#  \./#  #' > checksums/SHA256SUMS.txt
```

The checksum manifest intentionally excludes:

-   `.git/`
-   `.idea/`
-   `checksums/SHA256SUMS.txt` itself

The checksum file must exclude itself because a file cannot contain a
stable cryptographic hash of its own final contents.

### Verify `SHA256SUMS.txt`

``` bash
sha256sum -c checksums/SHA256SUMS.txt
```

Every listed file should report:

``` text
OK
```

Any `FAILED` or missing file indicates that the checked distribution no
longer matches the manifest.

------------------------------------------------------------------------

## 2. Package integrity --- Windows PowerShell

### Regenerate `SHA256SUMS.txt`

``` powershell
$files = Get-ChildItem -Recurse -File |
    Where-Object {
        $_.FullName -notmatch '\\\.git\\' -and
        $_.FullName -notmatch '\\\.idea\\' -and
        $_.FullName -ne (Join-Path $PWD 'checksums\SHA256SUMS.txt')
    } |
    Sort-Object { $_.FullName.Substring($PWD.Path.Length + 1).Replace('\','/') }

$lines = foreach ($file in $files) {
    $relative = $file.FullName.Substring($PWD.Path.Length + 1).Replace('\','/')
    $hash = (Get-FileHash -Algorithm SHA256 $file.FullName).Hash.ToLower()
    "$hash  $relative"
}

$lines | Set-Content -Encoding utf8 checksums\SHA256SUMS.txt
```

This produces the same canonical path convention used by the Linux/Git
Bash manifest: repository-relative paths with `/` separators.

### Verify `SHA256SUMS.txt`

``` powershell
$ok = $true

Get-Content checksums\SHA256SUMS.txt | ForEach-Object {
    if ($_ -match '^([0-9a-fA-F]{64})  (.+)$') {
        $expected = $matches[1].ToLower()
        $path = $matches[2].Replace('/', '\')

        if (-not (Test-Path $path)) {
            Write-Host "MISSING  $path"
            $ok = $false
        }
        else {
            $actual = (Get-FileHash -Algorithm SHA256 $path).Hash.ToLower()

            if ($actual -eq $expected) {
                Write-Host "OK       $path"
            }
            else {
                Write-Host "FAILED   $path"
                $ok = $false
            }
        }
    }
}

if ($ok) {
    Write-Host "`nSHA256SUMS: PASS"
} else {
    Write-Host "`nSHA256SUMS: FAIL"
    exit 1
}
```

Expected final result:

``` text
SHA256SUMS: PASS
```

------------------------------------------------------------------------

## 3. MDPAR benchmark evidence verification

The following commands are independent of the operating-system-specific
checksum commands above. They use the Python verification utilities
distributed with `MDPAR-docs`.

Run them from the repository root.

### 3.1 Verify canonical benchmark evidence

Linux / Git Bash:

``` bash
python verification/verify_benchmark_evidence.py
```

Windows PowerShell:

``` powershell
python verification\verify_benchmark_evidence.py
```

Expected result for the canonical MDPAR 2.2.0 evidence package:

``` text
verified_files=677
evidence_integrity=PASS
```

This verifies the integrity of the files represented by the canonical
benchmark evidence index.

### 3.2 Verify reproducibility of the evidence index

Linux / Git Bash:

``` bash
python verification/index_benchmark_evidence.py --check-existing
```

Windows PowerShell:

``` powershell
python verification\index_benchmark_evidence.py --check-existing
```

Expected result:

``` text
evidence_index_rebuild=PASS
```

This checks that rebuilding the canonical evidence index from the
versioned evidence surface reproduces the committed index rather than
silently changing its contents.

------------------------------------------------------------------------

## 4. Recommended verification sequence

For a downloaded, cloned, archived, cited or independently inspected
copy of `MDPAR-docs`, the recommended order is:

``` text
1. Verify SHA256SUMS.txt
2. Verify canonical benchmark evidence
3. Verify reproducibility of the evidence index
```

On Linux / Git Bash:

``` bash
sha256sum -c checksums/SHA256SUMS.txt
python verification/verify_benchmark_evidence.py
python verification/index_benchmark_evidence.py --check-existing
```

On Windows PowerShell, first run the PowerShell checksum-verification
block in Section 2 and then:

``` powershell
python verification\verify_benchmark_evidence.py
python verification\index_benchmark_evidence.py --check-existing
```

A fully consistent canonical package should end with:

``` text
SHA256SUMS: PASS
verified_files=677
evidence_integrity=PASS
evidence_index_rebuild=PASS
```

------------------------------------------------------------------------

## 5. Regenerating versus verifying

**Verification** and **regeneration** are deliberately separate
operations.

If the purpose is to test whether a downloaded or archived release is
intact, **do not regenerate `SHA256SUMS.txt` first**. Verify the
existing manifest. Regenerating it before verification would replace the
expected hashes with hashes of the current files and would therefore
defeat the integrity check.

Regenerate `checksums/SHA256SUMS.txt` only when intentionally preparing
a new canonical distribution after authorized changes to its contents.
After regeneration, verify the resulting manifest once before publishing
or archiving the package.

The benchmark evidence index follows the same principle.
`--check-existing` is the verification operation: it tests whether the
committed canonical index can be reproduced without replacing it.
