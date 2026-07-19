# Reproducible computations for Erdős #415

## Exhaustive scan through $10^6$

Command, from the problem directory:

```bash
python3 computational/pattern_scan.py \
  --limit 1000000 --max-k 6 \
  --output computational/pattern_scan_1m.json
```

Algorithm: an Euler totient sieve followed by an exhaustive scan of every
overlapping window.  A tied window is counted but realizes no permutation.
The program asserts
\[
\#\{\text{strict windows}\}+\#\{\text{tied windows}\}
=\#\{\text{all windows}\}
\]
for every $k$.  It independently checks every sieve value through $500$ using
the gcd-count definition of $\phi$.

Recorded run: limit $10^6$, $k\le6$, 11.943987 seconds in this workspace.
The exact JSON output is `pattern_scan_1m.json`.

| $k$ | patterns seen | $k!$ | exact $M_k$ if complete | decreasing endpoint |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 6 | 6 |
| 3 | 6 | 6 | 315 | 315 |
| 4 | 18 | 24 | not complete by $10^6$ | 826 |
| 5 | 45 | 120 | not complete by $10^6$ | not found |
| 6 | 116 | 720 | not complete by $10^6$ | not found |

Finite absence beyond the searched range is not used as an asymptotic proof.

## Independent $k=4$ counterexample certificate

Command:

```bash
python3 computational/verify_k4_counterexample.py
```

This implementation does not use the sieve.  It computes each totient by trial
division and cross-checks all values through $827$ by direct gcd counting.  It
exhaustively certifies
\[
M((4,3,2,1))=826,
\quad \phi(823),\ldots,\phi(826)=(822,408,400,348),
\]
but
\[
M((3,2,1,4))=827,
\quad \phi(824),\ldots,\phi(827)=(408,400,348,826).
\]
Therefore the decreasing $4$-pattern is not last to appear.  This finite
certificate, not the million-term absence data, disproves the source's
“always decreasing” assertion.
