# Search And Verification Code

This directory contains search programs and independent verifiers for Erdos
Problem 647.

## Programs

- `record_sieve.cpp`: independent low-range divisor sieve for records of
  `m + tau(m)`.
- `prime_tuple_search.cpp`: segmented prime-form sieve plus Miller-Rabin /
  Pollard-Rho shift verification for unsigned 64-bit ranges.
- `prime_tuple_search128.cpp`: the same search with 128-bit `N`/`n`
  support and optional batched residue jobs.
- `verify_candidate.py`: independent factorization-based verifier for a
  proposed `n`.
- `residue_classes.cpp`: experimental small-modulus residue filter.
- `residue_lift.py`: lifts the 41-class filter through extra small primes
  using the forced-smooth obstruction.
- `run_residue_scan.py`: launches and aggregates `prime_tuple_search` jobs
  over exact half-open ranges of `N`, either one residue per process or
  batched with `--batch-size` for the 128-bit binary.

## Build

```sh
c++ -O3 -std=c++17 -march=native SEARCH/prime_tuple_search.cpp -o SEARCH/prime_tuple_search
c++ -O3 -std=c++17 -march=native SEARCH/prime_tuple_search128.cpp -o SEARCH/prime_tuple_search128
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
- `residue_classes 50` returns 41 residue classes for `N mod 46189`.
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

The `--variable-mod` and `--variable-rem` options restrict the search to
values

```text
N = variable_mod * X + variable_rem.
```

This is used with the 41-class reduction modulo `46189`. The
`--extra-prime-forms` option accepts comma-separated `A:B` affine forms in
the `X` variable and requires each `A*X+B` to be prime. The
`--extra-prime-n-forms` option is the same condition in the `N` variable,
so `315:-2` requires `315N-2` to be prime after conversion to the active
residue progression. These options support restrictive subsearches and exact
split-residue filters such as `(504N-1)/5`, `(280N-1)/3`, `(280N-1)/9`, and
`(252N-1)/5` when the chosen variable modulus makes the division integral for
all `X`.

The range driver records reproducible logs for complete residue scans. For
example, this covers `3*10^15 <= N < 7320136537186331`, the largest range
where `2520N` still fits in an unsigned 64-bit word:

```sh
python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search \
  --n-start 3000000000000000 \
  --n-stop 7320136537186331 \
  --outdir /tmp/erdos647-scan-3e15-u64 \
  --workers 8 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15
```

For larger searches, a safe one-prime lift through 23 gives 352 residues
modulo `1062347`:

```sh
python3 SEARCH/residue_lift.py --k 200 --add-primes 23 --format csv \
  | tail -1 > /tmp/erdos647-residues-mod1062347.csv

python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search128 \
  --modulus 1062347 \
  --residue-file /tmp/erdos647-residues-mod1062347.csv \
  --n-start 10000000000000000 \
  --n-stop 20000000000000000 \
  --outdir /tmp/erdos647-scan-1e16-2e16-lift23
```

Deeper lifts have many more residue classes. Use the 128-bit binary's
batched job mode through the range driver to keep process overhead low:

```sh
python3 SEARCH/residue_lift.py --k 1000 --add-primes 23,29,31 --format csv \
  | tail -1 > /tmp/erdos647-residues-mod955049953-k1000.csv

python3 SEARCH/run_residue_scan.py \
  --binary /tmp/erdos647-bin/prime_tuple_search128 \
  --modulus 955049953 \
  --residue-file /tmp/erdos647-residues-mod955049953-k1000.csv \
  --n-start 40000000000000000 \
  --n-stop 80000000000000000 \
  --outdir /tmp/erdos647-scan-4e16-8e16-lift23-29-31-k1000 \
  --workers 6 \
  --batch-size 128 \
  --segment 10000000 \
  --sieve-limit 10000 \
  --quick-shift 5000 \
  --report-survive 15
```

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

For shifts whose useful cofactor is not of the form `cN-1`, use
`--extra-prime-n-forms`; for example, `315:-2` asks for the `k=16` cofactor
`315N-2` to be prime.
