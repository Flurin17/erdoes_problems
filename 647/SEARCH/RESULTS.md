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
