# Exact computation for Erdős #878

`exact_optimization.py` is a deterministic, standard-library-only reference
implementation.  It uses integer arithmetic throughout; in particular it does
not evaluate `floor(log_p n)` with floating point logarithms.

## Implemented quantities

- `f_exact(n)` factors `n` and repeatedly multiplies by each support prime to
  obtain `p^floor(log_p n)` exactly.  The empty-support value is `f(1)=0`.
- `exact_support_max(n,B)` exhausts positive exponent vectors and returns
  `M_n(B)=max{product(p^e_p): e_p>=1, product<=n}`.
- `f_partition_dp(n)` evaluates every nonempty support block and the canonical
  subset recurrence in which every considered block contains the least unused
  bit.  It returns both `F_nonunit` and an optimal partition witness.
- `F_unit=F_nonunit+1`, including `F_nonunit(1)=0`, `F_unit(1)=1`.
- `brute_force_family(n)` is the independent small-range oracle.  It scans
  every integer `2<=a<=n`, rejects `a` if it has a prime outside `P(n)`, and
  runs a disjoint-support family DP over the remaining integers.  It does not
  call the partition recurrence or exponent-vector enumeration.
- `h_direct(x)` and `h_prime_block_identity(x)` compute the two sides of the
  exact finite identity for integer `x`, as `fractions.Fraction` objects.

The partition mechanism being tested is: pairwise coprimality makes the exact
prime supports of chosen nonunits disjoint; positivity forces an optimum to
use every support prime; on a fixed block its best possible member is `M_n(B)`.
Thus an optimum is obtained by maximizing the sum of block maxima over support
partitions.  This also motivates the following lemma chain checked finitely:

1. every enumerated block maximum is in range and has its requested exact
   support;
2. singleton maxima equal the exact integer powers in `f`, while the full
   support maximum is `n`;
3. the support-partition DP equals the independently scanned admissible-family
   DP;
4. `F_nonunit=f` exactly when all subset inequalities
   `M_n(B)<=sum_{p in B}p^floor(log_p n)` hold;
5. the one-prime formula is `F=f=n`, the two-prime formula is
   `F=max(n,f)`, and adjoining the unit always adds exactly one;
6. direct summation of `f(n)/n` agrees with the finite prime/block identity.

These finite checks test the implementation and can falsify proposed formulas;
they are not proofs for unbounded `n`.

## Reproduction

Run from the repository root:

```text
python3 878/computational/exact_optimization.py verify --limit 500 --h-x 501
python3 878/computational/exact_optimization.py tables --limit 100
python3 878/computational/exact_optimization.py single 120
python3 878/computational/exact_optimization.py h 501
```

The `verify` command asserts, for every `1<=n<=limit`, agreement of every
block `M_n(B)` with the integer-scan oracle; agreement of the two optimizers
for `F_nonunit`; range, distinctness, admissibility, and pairwise coprimality
of the oracle witness; the singleton, full-block, one-prime, and two-prime
formulas; the all-subsets equality criterion; and the unit shift.  It also
checks the two exact formulas for `H(h_x)`.  A failed invariant stops at the
first counterexample.  `tables` prints every running-record event and the
complete equality lists for both unit conventions in its requested range.

## Recorded finite run

The checked range, wall-clock runtime, exact `H` value, and case counts are
recorded below after executing the commands in this environment.  Runtime is
informational and will vary by machine.

<!-- RUN-RESULTS -->

On 2026-07-17 the first command above completed successfully in 0.110782
seconds and reported:

```text
verified n=1..500; H at integer x=501
one-prime cases=114; two-prime cases=266; F_nonunit=f cases=318
H(501)=3208472611630658107360217446577961761604012799439042832047227159180175729880822755278893952363169968675223/5729880480457278243128575486488197752467901211751115891773754968581389252694254184020057965371224464000
(approximately 559.954544004)
```

Thus the verified finite claim is: for every `1<=n<=500`, every computed
`M_n(B)` and `F_nonunit(n)` agrees with its independent integer-scan oracle,
all listed invariants hold, and the direct and prime/block rational values of
`H(501)` agree exactly.  The second command completed in 0.002763 seconds.  It
found 80 nonunit-convention equality cases and no unit-convention equality
case in `1<=n<=100`; at the terminal cutoff all three running maxima were
`max f=194`, `max F_nonunit=194`, and `max F_unit=195`.  These counts and
records describe only the stated finite intervals.

Two targeted checks also reproduce the obstructions used in `NOTES.md`:
`n=120` has `(f,F_nonunit)=(170,181)`, with optimal blocks `{2,5}` and `{3}`
of values 100 and 81, while `n=3689` has `(f,F_nonunit)=(3651,3689)` even
though each two-prime block satisfies its singleton-sum inequality.

## Interpretation and remaining gap

A successful run is a verified finite claim only: within the stated range,
the independently implemented optimizers and both finite `H` identities agree
exactly.  The weakest theoretical gap is uniform asymptotic control: neither
the bounded partition search nor exact harmonic sums supplies estimates as
`n,x -> infinity`.  In particular, tables cannot prove a density, maximal
order, almost-all assertion, or the proposed bound for `H`.

A concrete falsification test for any proposed structural equality rule is to
translate it into a Boolean predicate and compare it, for each `n`, with both
`F_nonunit(n)==f(n)` and every subset inequality.  A concrete next action is
to extend the script with route-specific statistics (for example the size and
prime scale of the first violating block), then use those data only to propose
a uniform counting lemma which must be proved analytically.
