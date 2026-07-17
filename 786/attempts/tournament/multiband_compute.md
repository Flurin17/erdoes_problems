# Multi-band exact computation

## Outcome

No searched rational multi-band grading improves the one-threshold grading.
The cleanest comparison is at (N=100000).  The exact best prime threshold is
(y=59), with

\[
 \#\{n\leq 100000:\Omega_{p>59}(n)=1\}=80421.
\]

An exhaustive three-band grid, an exact-cut four-band grid, all 4096 binary
patterns in a broad 12-bin exponent window, and all 6561 ternary patterns in
an eight-bin window all have maximum nonzero fiber size (80421).  In each
case a description of the threshold grading is the maximizer.  This is a
finite negative experiment, not a proof that the threshold construction is
optimal among all rational gradings or asymptotically.

The best genuinely multi-segment system found has size (79612).  Its prime
weights are

\[
 w_p=\begin{cases}
 0,&p\leq41,\\
 1,&43\leq p\leq59,\\
 0,&61\leq p\leq83,\\
 1,&p\geq89,
 \end{cases}
 \qquad A=\{n\leq100000:f(n)=1\}.
\]

Thus it is 809 elements below the exact threshold benchmark.

## Mechanism and proved certificate lemma

For a denominator (D), atomic prime bin (j) is

\[
 N^{j/D}<p\leq N^{(j+1)/D}\qquad(0\leq j<D).
\]

All boundary tests are the exact integer comparison (p^D\leq N^k); the
program never uses floating point to assign a prime.  A rational vector of
band weights can be scaled to a primitive integer vector, so enumerating
primitive integer representatives loses no projective rational grading
within the stated coefficient bound.

**Lemma (complete).** If the completely additive function
(f(n)=\sum_p w_pv_p(n)) has the same nonzero value (c) on (A), then
(A) is repetition-allowed PLR and

\[
 \operatorname{rank}_{\mathbb Q}V_A
 =\operatorname{rank}_{\mathbb Q}[V_A\mid\mathbf1].
\]

Indeed, applying (f) to a product equality gives (rc=sc), hence (r=s).
For the matrix assertion, the prime-coordinate vector
(q_p=w_p/c) satisfies (V_Aq=\mathbf1), so the augmented column already
lies in the column span of (V_A).

This gives an exact full-set rank-equality certificate for every reported
fiber; it is not a modular or numerical surrogate.

## Exact search at (N=100000)

| family | exact parameter space | distinct projective fibers | best count | best genuine multi-segment count |
|---|---:|---:|---:|---:|
| Three bands, cuts (k/31), primitive (|w|_\infty\leq5) | (435\cdot577=250995) | 189337 | 80421 | 77682 |
| Four bands, cuts (k/31), required cut (11/31), primitive (|w|_\infty\leq3) | (406\cdot1120=454720) | 300445 | 80421 | 79612 |
| Binary atomic weights, bins (5,\ldots,16) free, lower bins (0), upper bins (1) | (2^{12}=4096) | 4096 | 80421 | 79612 |
| Ternary atomic weights, bins (7,\ldots,14) free, lower bins (0), upper bins (1) | (3^8=6561) | 6561 | 80421 | 79612 |

For the binary window, the freely selected bands cover exactly the primes
from (7) through (547); below them the weight is fixed at (0), and above
them at (1).  For the ternary window, the free weights
({-1,0,1}) cover the primes from (17) through (257).  Hence these are
not merely perturbations confined to primes near (N).

The integer boundary cutoffs relevant to the best multi-segment candidate
are exact:

| exponent cut | largest prime below the cut |
|---:|---:|
| (10/31) | 41 |
| (11/31) | 59 |
| (12/31) | 83 |

The exact threshold sweep gives the following slow finite-size approach to
the known threshold limit (c_*=0.828499\ldots):

| (N) | best integer cutoff (y) | exact threshold count | density |
|---:|---:|---:|---:|
| 1000 | 7 | 746 | 0.746000 |
| 10000 | 23 | 7860 | 0.786000 |
| 100000 | 59 | 80421 | 0.804210 |
| 1000000 | 149 | 814206 | 0.814206 |

At (N=10000), the separate three-band (D=23,|w|_\infty\leq3) and
four-band (D=14,|w|_\infty\leq2) grids also attain, but do not exceed,
the exact threshold count 7860.  At (N=1000000), the coarser tested grids
do not contain the exact finite optimum and therefore are not used for an
optimality comparison.

## Counting and rank validation

The smallest-prime-factor dynamic program records the complete vector of
atomic prime-factor counts (with multiplicity) for every (n\leq N).  It
aggregates equal signatures, forms every exact score histogram with integer
arithmetic, and ignores score zero.  The winning counts are then recomputed
integer-by-integer from the factorization table, separately from signature
aggregation.  Assertions require the two counts to agree.

The one-threshold benchmark is independently swept over every integer cutoff
(y).  If (P_1(n)\geq P_2(n)) are the two largest prime factors of (n),
with multiplicity and missing factors set to (1), then
(Omega_{p>y}(n)=1) exactly for (P_2(n)\leq y<P_1(n)).  An interval
difference array counts all cutoffs, followed by a direct factorization
recount of the winner.

For all 80421 threshold rows and all 79612 best multi-segment rows, the exact
identity (V_A(w/c)=\mathbf1) certifies full rank equality.  As an independent
small exact check, fraction-valued sparse Gaussian elimination on the same
(N=100000) construction restricted to integers at most 450 gives

| fiber | rows in the restriction | (operatorname{rank}_{\mathbb Q}V) | (operatorname{rank}_{\mathbb Q}[V\mid\mathbf1]) |
|---|---:|---:|---:|
| threshold | 143 | 74 | 74 |
| best multi-segment | 142 | 72 | 72 |

These numeric ranks concern the stated initial-segment restrictions.  The
full (N=100000) equality is certified algebraically, without claiming that
its numeric rank was explicitly row-reduced.

## Reproduction

The script uses only the Python standard library and has no random seed.

```bash
python3 786/computational/multiband_search.py --N 100000 \
  --config 3:31:5 --top 15 --rank-n 450

python3 786/computational/multiband_search.py --N 100000 \
  --config 4:31:3:11 --top 15 --rank-n 450

python3 786/computational/multiband_search.py --N 100000 \
  --binary-window 31:5:17 --top 15 --rank-n 450

python3 786/computational/multiband_search.py --N 100000 \
  --ternary-window 31:7:15 --top 15 --rank-n 450
```

Observed search times in this workspace were approximately 29, 58, 9, and
12 seconds respectively (rank recounts add a few seconds).  Exact counts,
not timing, are the reproducible outputs.

## Dependency chain, limitation, and next test

1. Rational band weights reduce projectively to primitive integer weights.
2. Exact factor signatures give exact histograms for every enumerated
   grading.
3. Every nonzero histogram fiber has the PLR/rank certificate proved above.
4. The exact one-threshold sweep supplies the same-(N) benchmark.
5. Exhaustion of the displayed finite grids proves only that no member of
   those grids improves the benchmark.

The weakest unsupported step would be any inference from item 5 to all
rational band systems or to an asymptotic upper bound; no such inference is
made.  A concrete falsification is any run reporting a positive
`delta_vs_threshold`.  The next useful expansion is a five-or-more-band
search with finer rational cuts around (10/31,11/31,12/31), followed by a
larger-(N) check of any positive candidate.  The alternating
(0,1,0,1) runner-up identifies that neighborhood as the only observed
competitive non-threshold mechanism.

## Coordinator rerun

The coordinator reran the \(4096\)-pattern binary window at \(N=100000\).
It reproduced threshold count \(80421\), best multisegment count \(79612\),
both full algebraic certificates, and restricted exact ranks \(74=74\) and
\(72=72\). Observed resource summary:
\[
\text{wall}=12.39\text{s},\quad
\text{user}=12.33\text{s},\quad
\text{maxrss}=28836\text{ KB}.
\]
