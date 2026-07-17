# Notes for Erdős #878

This file records normalized definitions, equivalent formulations,
calculations, and locally proved lemmas.  See `STATUS.md` for the task contract
and research ledger.

## Normalized notation

For `n>1`, let `P(n)={p:p|n}` and `L_p(n)=floor(log_p n)`.  Put
`q_p(n)=p^{L_p(n)}`.  Then `f(n)=sum_{p in P(n)}q_p(n)`.  For `n=1`, all three
objects are empty/zero in the evident sense.

For a nonempty subset `B` of a finite prime set `P`, define

`M_n(B)=max{ product_{p in B}p^{e_p} : e_p>=1 integers, product<=n }`.

The feasibility set is nonempty exactly when `product_{p in B}p<=n`.

## Exact elementary identities

For real `y>=1`,

`p^{floor(log_p y)} = y*p^{-fractional_part(log_p y)}`.

It is constant on every half-open interval `[p^j,p^{j+1})` and has an upward
jump by the factor `p` at `p^j`.

## Convention split for the unit

Let `F_{>1}` denote the optimization restricted to `a_i>1`, and let `F_unit`
use the literal vacuous-prime-factor reading.  Then
`F_unit(n)=F_{>1}(n)+1` for `n>=2`; also `F_unit(1)=1` and `F_{>1}(1)=0`.

Proof: `1` is coprime to every positive integer, distinct from every member of
a non-unit family, and adds one to the sum.  Conversely an admissible family
contains at most one `1`; remove it.

## Lemma 1: exact fixed-support optimization

Let `n>1`, `P=P(n)`, and exclude the unit.  Then

`F_{>1}(n)=max_{Pi partition of P} sum_{B in Pi} M_n(B)`.

Proof.  The exact prime supports of pairwise coprime nonunits are disjoint
nonempty sets.  An optimum uses every prime of `P`, since an unused prime `p`
can be appended as a new term.  Its supports therefore partition `P`.
Replacing the term on a block `B` by `M_n(B)` preserves all coprimality
relations and cannot decrease the sum.  Conversely, choosing a maximizer for
each block of any partition produces an admissible family.  (The chosen terms
are automatically distinct: equal integers greater than one are not coprime.)

The maximum exists because `prod_{p in B}p <= rad(n) <= n`.  Furthermore

- `M_n({p})=p^{L_p(n)}`;
- `M_n(P)=n`, because `n` itself has exact support `P`;
- `n/p < M_n(B) <= n` for every `p in B`: multiply a maximizer by `p`; if the
  result were still at most `n`, maximality would fail;
- consequently `F_{>1}(n)>=max(f(n),n)` and
  `F_{>1}(n)<=n*omega(n)`.

An exact subset dynamic program is

`V(empty)=0`,

`V(S)=max_{B subset S, min(S) in B}(M_n(B)+V(S\\B))`.

Thus `F_{>1}(n)=V(P)`.

## Lemma 2: exact equality criterion

Under the nonunit convention,

`F_{>1}(n)=f(n)`

if and only if, for every nonempty `B subset P(n)`,

`M_n(B) <= sum_{p in B}p^{L_p(n)}`.                         (E)

It is enough to check `|B|>=2`.  If (E) holds, sum it over the blocks of any
partition and apply Lemma 1.  If it fails for `B`, use the partition consisting
of `B` and singleton blocks outside `B` to beat `f(n)`.

Checking only the full block is not sufficient.  For `n=120`, the singleton
weights are `64,81,25`, so `f(120)=170>120`, but
`M_120({2,5})=100>64+25`; hence `F(120)>=100+81=181`.
Even checking all pairs is insufficient: for `n=3689=7*17*31`, the singleton
weights are `2401,289,961`, whose sum is `3651`.  Direct enumeration of the
two exponents gives block maxima `2023,1519,527`, respectively, below the
corresponding singleton sums, but the full block has value `3689>3651`.

## Corollaries for small supports

- `n=1`: `f(1)=F_{>1}(1)=0` when the empty family is allowed.
- `n=p^a`: `f(n)=F_{>1}(n)=n`.
- If `P(n)={p,q}`, then `F_{>1}(n)=max(f(n),n)`.
- If `n=pq` is squarefree with `p<q` and `r=floor(log_p q)`, then
  `f(n)=p^{r+1}+q` and
  `F_{>1}(n)=max(pq,p^{r+1}+q)`.  Equality holds exactly when
  `p^{r+1}>=q(p-1)`.  In particular every `n=2q` has equality, whereas
  `n=15` does not.

## Merge identities and obstructions

For disjoint nonempty blocks `A,B`, exact-support factorization gives

`M_n(A union B)=max_{a in S(A), a<=n/rad(B)} a*M_{n/a}(B)`,

where `S(A)` is the multiplicative semigroup of integers with exact support
`A`.  Merging `A,B` improves a partition exactly when the left side exceeds
`M_n(A)+M_n(B)`.  If `M_n(A)M_n(B)<=n`, then the merged maximum equals their
product and the merge is strictly beneficial.  If their sum is at least `n`,
a merge cannot help.  The middle regime depends on logarithmic lattice gaps:
at `n=35`, merging `{5},{7}` wins, while at `n=42`, merging `{2},{7}` loses.

## Exact finite identity for the summatory function

Let `U_p(x)=ceil(x/p)-1`, the largest integer `m<x/p`, and let
`h_0=0`, `h_r=sum_{1<=m<=r}1/m`.  Finite reindexing `n=pm` gives

`H(x)=sum_{p<x} sum_{0<=j: p^j<=U_p(x)}
 p^j*(h_{min(p^{j+1}-1,U_p(x))}-h_{p^j-1})`.              (H)

Indeed the `p`-summand of `f(pm)/(pm)` is
`p^{floor(log_p m)}/m`, and `floor(log_p m)=j` precisely on
`p^j<=m<p^{j+1}`.  Identity (H) involves only finite sums, so no convergence
interchange is present.

## Dependency graph separated by subquestion

1. Almost-all `f`: a dyadic first-moment bound for (H), followed by Markov.
2. Almost-all `F`: a deterministic theorem packing a typical prime support
   into `Omega(log log n)` blocks whose exact-support semigroups hit `[cn,n]`,
   plus a density-one prime-divisor distribution theorem.
3. Extremal `f`: maximal order of `omega(n)` gives the upper bound; the lower
   bound separately requires simultaneous control of the fractional logarithms
   `{log_p n}` for many support primes.
4. Running-max equality: substantially stronger than equal asymptotics; it
   needs a domination/transfer theorem for every partition value.
5. Pointwise equality count: Lemma 2 plus a uniform count of all subset
   inequalities.  It is logically independent of running-max equality.
6. `H(x)`: start from (H); completed prime-power blocks are elementary, while
   terminal blocks encode the phase `log x-k log p` and require uniform prime
   estimates in short root intervals.
