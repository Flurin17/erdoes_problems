# Search Results

All commands below were run from `/Users/flurinlaim/Coding/erdos_problems/647`.

## Reproducibility Tests

Command:

```sh
./SEARCH/run_tests.sh
```

Output:

```text
all tests passed
```

This verifies:

- `record_sieve 1000` returns exactly `1 2 3 4 5 6 8 10 12 24`.
- `verify_candidate.py` accepts `n=24` on the checked range.
- `verify_candidate.py` rejects the published near miss at `k=14`.
- `prime_tuple_search` reproduces the published near miss in a local window.

## Low-Range Sieve

Command:

```sh
./SEARCH/record_sieve 100000 | sed -n '1,3p'
```

Output:

```text
limit 100000
solutions 1 2 3 4 5 6 8 10 12 24
records
```

## Published Near Miss

Command:

```sh
python3 SEARCH/verify_candidate.py 604517614941240 --shift-limit 20
```

Output:

```text
FAIL n=604517614941240 k=14 m=604517614941226 tau=192 bound=16
```

## Complete Branch Scans

These use only the branch conditions that are currently treated as complete
necessary conditions for candidates `n > 84`: the 7-tuple condition and the
Branch A `105N-1` condition from `k=24`.

Command:

```sh
./SEARCH/prime_tuple_search \
  --start 1 \
  --count 1000000000 \
  --segment 10000000 \
  --sieve-limit 200000 \
  --quick-shift 500 \
  --no-full \
  --report-survive 13
```

Output:

```text
DONE start=1 count=1000000000 prime_tuples=622 quick_pass=0
```

Interpretation: among `N < 10^9`, 622 values satisfy the complete branch
prime-form conditions; none passes direct shift checks through `k=500`.

Command:

```sh
./SEARCH/prime_tuple_search \
  --start 1000000001 \
  --count 10000000000 \
  --segment 10000000 \
  --sieve-limit 200000 \
  --quick-shift 500 \
  --no-full \
  --report-survive 13
```

Output:

```text
DONE start=1000000001 count=10000000000 prime_tuples=2883 quick_pass=0
```

Interpretation: among `10^9 < N <= 11*10^9`, 2883 values satisfy the
complete branch prime-form conditions; none passes direct shift checks
through `k=500`.

Command:

```sh
./SEARCH/prime_tuple_search \
  --start 11000000001 \
  --count 10000000000 \
  --segment 10000000 \
  --sieve-limit 200000 \
  --quick-shift 500 \
  --no-full \
  --report-survive 13
```

Output:

```text
DONE start=11000000001 count=10000000000 prime_tuples=2096 quick_pass=0
```

Interpretation: among `11*10^9 < N <= 21*10^9`, 2096 values satisfy the
complete branch prime-form conditions; none passes direct shift checks
through `k=500`.

Command:

```sh
./SEARCH/prime_tuple_search \
  --start 21000000001 \
  --count 10000000000 \
  --segment 10000000 \
  --sieve-limit 500000 \
  --quick-shift 500 \
  --no-full \
  --report-survive 13
```

Output:

```text
DONE start=21000000001 count=10000000000 prime_tuples=1892 quick_pass=0
```

Interpretation: among `21*10^9 < N <= 31*10^9`, 1892 values satisfy the
complete branch prime-form conditions; none passes direct shift checks
through `k=500`.

## Complete 41-Residue Branch Scan

After reconstructing the 41 residue classes modulo `46189`, the search was
restricted to those classes and run through a deeper direct shift window.

Command shape:

```sh
./SEARCH/prime_tuple_search \
  --variable-mod 46189 \
  --variable-rem <one of the 41 residues> \
  --start 0 \
  --count 21650176450 \
  --segment 10000000 \
  --sieve-limit 500000 \
  --quick-shift 5000 \
  --report-survive 13 \
  --stats
```

The 41 residue jobs together cover all `N < 10^15` that survive the modular
reduction.

Aggregate output:

```text
prime_tuples=331487 quick_pass=0
BRANCH_COUNTS A=75289 B=256198
FIRST_FAIL_COUNTS 5:288159 7:26766 9:14390 10:1880 11:190 13:61 14:32 15:6 16:3
```

Interpretation: among all branch tuples in the 41 residue classes with
`N < 10^15`, none passed direct shift checks through `k=5000`. The deepest
near misses failed at `k=16`; the best by failing shift and then smaller
failing divisor count was

```text
N = 832414790665601
n = 2097685272477314520
first_fail_k = 16
tau(n-16) = 32
```

The next range was scanned with the same 41 residue classes. This command
shape covers `10^15 <= N < 3*10^15`:

```sh
./SEARCH/prime_tuple_search \
  --variable-mod 46189 \
  --variable-rem <one of the 41 residues> \
  --start 21650176449 \
  --count 43300352899 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15 \
  --stats
```

Aggregate output:

```text
prime_tuples=485824 quick_pass=0
BRANCH_COUNTS A=106851 B=378973
FIRST_FAIL_COUNTS 5:425531 7:37720 9:19745 10:2480 11:231 13:81 14:27 15:9
```

Interpretation: no branch tuple with `10^15 <= N < 3*10^15` passed direct
checks through `k=5000`; no tuple in this range survived past `k=15`.

The final unsigned-64-bit range was scanned with the same 41 residue
classes. This command covers
`3*10^15 <= N < 7320136537186331`, i.e. all remaining `N` for which
`2520N` fits in an unsigned 64-bit integer:

```sh
python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search \
  --n-start 3000000000000000 \
  --n-stop 7320136537186331 \
  --outdir /tmp/erdos647-scan-3e15-u64 \
  --workers 4 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15
```

Aggregate output:

```text
prime_tuples=886846 quick_pass=0
BRANCH_COUNTS A=190308 B=696538
FIRST_FAIL_COUNTS 5:779139 7:68367 9:34486 10:4284 11:360 13:139 14:48 15:16 16:4 18:2 20:1
```

Interpretation: no branch tuple with
`3*10^15 <= N < 7320136537186331` passed direct checks through
`k <= 5000`. The deepest near miss in the range was

```text
N = 3602115923026621
n = 9077332126027084920
first_fail_k = 20
tau(n-20) = 72
```

The first 128-bit scan continued with the original 41 residue classes:

```sh
python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search128_new \
  --n-start 7320136537186331 \
  --n-stop 10000000000000000 \
  --outdir /tmp/erdos647-scan-u64-1e16 \
  --workers 4 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15
```

Aggregate output:

```text
prime_tuples=501242 quick_pass=0
BRANCH_COUNTS A=106940 B=394302
FIRST_FAIL_COUNTS 5:440986 7:38229 9:19525 10:2200 11:198 13:69 14:28 15:7
```

Interpretation: no branch tuple with
`7320136537186331 <= N < 10^16` passed direct checks through
`k <= 5000`; no tuple in this range survived past `k=15`.

For the next range, the 41 classes were safely lifted through the prime
`23`, giving 352 residue classes modulo `1062347`:

```sh
python3 SEARCH/residue_lift.py --k 200 --add-primes 23 --format csv \
  | tail -1 > /tmp/erdos647-residues-mod1062347.csv

python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search128_new \
  --modulus 1062347 \
  --residue-file /tmp/erdos647-residues-mod1062347.csv \
  --n-start 10000000000000000 \
  --n-stop 20000000000000000 \
  --outdir /tmp/erdos647-scan-1e16-2e16-lift23 \
  --workers 6 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15
```

Aggregate output:

```text
prime_tuples=917450 quick_pass=0
BRANCH_COUNTS A=193613 B=723837
FIRST_FAIL_COUNTS 5:801083 7:74718 9:36482 10:4519 11:438 13:142 14:50 15:14 16:3 22:1
```

Interpretation: no branch tuple with `10^16 <= N < 2*10^16` passed direct
checks through `k <= 5000`. The deepest near miss in the range was

```text
N = 10182590254890053
n = 25660127442322933560
first_fail_k = 22
tau(n-22) = 32
```

For the next interval, the residue filter was first lifted through primes
`23,29` with `k <= 1000`, giving 4,374 residue classes modulo `30808063`:

```sh
python3 SEARCH/residue_lift.py --k 1000 --add-primes 23,29 --format csv \
  | tail -1 > /tmp/erdos647-residues-mod30808063-k1000.csv

python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search128_new \
  --modulus 30808063 \
  --residue-file /tmp/erdos647-residues-mod30808063-k1000.csv \
  --n-start 20000000000000000 \
  --n-stop 40000000000000000 \
  --outdir /tmp/erdos647-scan-2e16-4e16-lift23-29-k1000 \
  --workers 6 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15
```

This scan was stopped early after 1,010 of 4,374 residue jobs because the
stricter `23,29,31` lift below became available. A prior attempt over this
interval using only the 352 classes modulo `1062347` had also been stopped
early because the `23,29` lift cut the tested progression density from about
`3.3134e-4` to `1.4198e-4`.

The next lift through `23,29,31` with `k <= 1000` gives 59,128 residue
classes modulo `955049953`, density about `6.1911e-5`. Because this creates
too many small one-residue jobs, `prime_tuple_search128` now accepts
`--jobs-file` with `residue start count` triples, and `run_residue_scan.py`
supports `--batch-size`. The range `2*10^16 <= N < 4*10^16` was then scanned
completely with this stricter lift:

```sh
python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search128_batch \
  --modulus 955049953 \
  --residue-file /tmp/erdos647-residues-mod955049953-k1000.csv \
  --n-start 20000000000000000 \
  --n-stop 40000000000000000 \
  --outdir /tmp/erdos647-scan-2e16-4e16-lift23-29-31-k1000 \
  --workers 6 \
  --batch-size 128 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15
```

Aggregate output:

```text
prime_tuples=532062 quick_pass=0
BRANCH_COUNTS A=119201 B=412861
FIRST_FAIL_COUNTS 5:459759 7:46776 9:22007 10:3035 11:325 13:114 14:38 15:5 16:3
```

Interpretation: no branch tuple with `2*10^16 <= N < 4*10^16` passed direct
checks through `k <= 5000`. The deepest near misses in this range all failed
at `k=16`; the best by failing shift and then smaller failing divisor count
was

```text
N = 27483420334150209
n = 69258219242058526680
first_fail_k = 16
tau(n-16) = 32
n-16 = 2^3 * 29 * 1061 * 281363625898057
```

Both independent Python verifiers reject this near miss at `k=16`.

The dry run for the next range, `4*10^16 <= N < 8*10^16`, with
`--batch-size 128` produces 462 process jobs and total `X` count
`2476435910553`.

## Restrictive Prime-Form Subsearch

This uses the 7-tuple branch conditions plus the forced prime forms
`504N-1`, `280N-1`, and `252N-1`. This is not a complete exclusion because
the corresponding shifts allow some composite cofactors such as `5p`, `3p`,
or `9p`.

Command:

```sh
./SEARCH/prime_tuple_search \
  --start 1 \
  --count 1000000000 \
  --segment 10000000 \
  --sieve-limit 200000 \
  --quick-shift 500 \
  --no-full \
  --report-survive 13 \
  --extra-prime-coeffs 504,280,252
```

Output:

```text
DONE start=1 count=1000000000 prime_tuples=2 quick_pass=0
```

Interpretation: among `N < 10^9`, two `N` satisfy this restrictive
prime-only subsearch, and neither passes the direct shift checks through
`k=500`.
