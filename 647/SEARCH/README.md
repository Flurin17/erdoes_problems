# Search And Verification Code

This directory contains search programs and independent verifiers for Erdos
Problem 647.

## Programs

- `record_sieve.cpp`: independent low-range divisor sieve for records of
  `m + tau(m)`.
- `prime_tuple_search.cpp`: segmented prime-form sieve plus Miller-Rabin /
  Pollard-Rho shift verification.
- `verify_candidate.py`: independent factorization-based verifier for a
  proposed `n`.
- `residue_classes.cpp`: experimental small-modulus residue filter.

## Build

```sh
c++ -O3 -std=c++17 -march=native SEARCH/prime_tuple_search.cpp -o SEARCH/prime_tuple_search
c++ -O3 -std=c++17 -march=native SEARCH/record_sieve.cpp -o SEARCH/record_sieve
c++ -O3 -std=c++17 SEARCH/residue_classes.cpp -o SEARCH/residue_classes
```

## Reproducibility Checks

```sh
./SEARCH/record_sieve 1000
python3 SEARCH/verify_candidate.py 24 --shift-limit 30
python3 SEARCH/verify_candidate.py 604517614941240 --shift-limit 20
```

Known expected facts:

- `record_sieve 1000` lists solutions
  `1 2 3 4 5 6 8 10 12 24`.
- `n=24` passes.
- `604517614941240` fails at `k=14`.

## Complete Prime-Tuple Search

For every candidate `n > 84`, write `n = 2520N`. The current strongest
complete prime-form filter is the 7-tuple branch condition, plus the
branch-specific `105N-1` prime condition for Branch A.

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

Remove `--no-full` when a `QUICK_PASS` appears; the program will then compute
the exact divisor-count bound `B` and verify the full finite certificate
range.

## Restrictive Subsearch

The option below additionally requires `504N-1`, `280N-1`, and `252N-1` to
be prime. This is useful for finding very prime-rich near misses, but it is
not complete: shifts `k=5,9,10` allow some composite cases such as `5p`,
`3p`, or `9p` in the corresponding cofactors.

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
