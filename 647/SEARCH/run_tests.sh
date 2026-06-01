#!/usr/bin/env bash
set -euo pipefail

c++ -O3 -std=c++17 -march=native SEARCH/prime_tuple_search.cpp -o SEARCH/prime_tuple_search
c++ -O3 -std=c++17 -march=native SEARCH/prime_tuple_search128.cpp -o SEARCH/prime_tuple_search128
c++ -O3 -std=c++17 -march=native SEARCH/record_sieve.cpp -o SEARCH/record_sieve
c++ -O3 -std=c++17 SEARCH/residue_classes.cpp -o SEARCH/residue_classes

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

./SEARCH/record_sieve 1000 > "$tmp"
grep -q '^solutions 1 2 3 4 5 6 8 10 12 24$' "$tmp"

python3 SEARCH/verify_candidate.py 24 --shift-limit 30 > "$tmp"
grep -q '^PASS n=24' "$tmp"

if python3 SEARCH/verify_candidate.py 604517614941240 --shift-limit 20 > "$tmp"; then
  echo "near miss unexpectedly passed" >&2
  exit 1
fi
grep -q '^FAIL n=604517614941240 k=14' "$tmp"

./SEARCH/prime_tuple_search \
  --start 239887000000 \
  --count 2000000 \
  --segment 1000000 \
  --sieve-limit 200000 \
  --quick-shift 100 \
  --no-full \
  --report-survive 10 \
  --print-fails > "$tmp"
grep -q 'SURVIVE branch=B N=239887942437 n=604517614941240 first_fail_k=14' "$tmp"

./SEARCH/prime_tuple_search128 \
  --start 59845588255683945 \
  --count 1 \
  --segment 1 \
  --sieve-limit 10000 \
  --quick-shift 25 \
  --report-survive 15 \
  --stats \
  --extra-prime-shift-forms 5,9,10 > "$tmp"
grep -q 'SURVIVE branch=B N=59845588255683945 n=150810882404323541400 first_fail_k=21' "$tmp"

./SEARCH/prime_tuple_search128 \
  --start 113432449033802613 \
  --count 1 \
  --segment 1 \
  --sieve-limit 10000 \
  --quick-shift 25 \
  --stats \
  --extra-prime-shift-forms 5,9,10 > "$tmp"
grep -q '^DONE start=113432449033802613 count=1 prime_tuples=0 quick_pass=0$' "$tmp"

echo "all tests passed"
