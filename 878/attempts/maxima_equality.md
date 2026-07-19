# Route: equality of the running maxima

All substantive assertions use `a_i>1`; if the unit is allowed, each optimum
increases by one.

## Counterexample to “for all `x`”

At `n=210`, the admissible pairwise-coprime family
`128=2^7`, `125=5^3`, `189=3^3*7` has sum `442`, so `F(210)>=442`.
On the other hand,

`max_{m<=210}f(m)=f(210)=128+81+125+49=383`.                   (1)

Indeed five distinct prime divisors are impossible, while four force
`m=210`.  For three primes `p<q<r`: if `p=2,q=3`, the crude bound
`128+81+169=378` suffices.  If `p=2,q=5`, then
`r in {7,11,13,17,19}`; the only crude danger is `r=13`, but support
`{2,5,13}` forces `m=130`, giving `f(m)=266`; all other cases are at most
`128+125+121=374`.  If `p=2,q=7`, the bound is `346`; larger `q` are
impossible.  If `p=3`, necessarily `q=5,r<=13`, giving at most
`81+125+169=375`; `p>=5` is impossible.  For two primes, if the larger is at
most `13`, the two largest possible powers give `169+128=297`.  If it is at
least `17`, its contribution is the prime itself; splitting on the smaller
prime `2,3,5,7,11` gives respective upper bounds `231,148,166,78,140`.
One-prime support contributes at most `210`.  This proves (1).

Therefore

`max_{m<=210}F(m)>=442>383=max_{m<=210}f(m)`,                  (2)

so equality is false for all `x`.  The exact optimizer independently checks
(2), but the finite argument above is the proof.

In fact `210` is a strict `F`-record.  For `m<=147`,
`F(m)<=omega(m)m<=3m<=441`.  For `148<=m<210` and `omega(m)<=2`,
`F(m)<=2m<420`.  The remaining three-prime integers and their values, obtained
directly from the displayed three-prime formula in `equality_count.md`, are

`m:    150 154 156 165 168 170 174 180 182 186 190 195 198 204`

`F(m): 334 298 245 327 275 270 238 334 346 240 277 375 330 281`.

All are below `442`, whereas the family above gives `F(210)>=442`.

## Exact record reformulation

Put

`R_f(x)=max_{n<=x}f(n)`,  `R_F(x)=max_{n<=x}F(n)`.

Then `R_f(x)=R_F(x)` for every sufficiently large `x` if and only if all but
finitely many strict `F`-record holders `r` satisfy `F(r)=f(r)`.             (3)

Indeed, suppose the running maxima agree from some point onward.  At a later
strict `F`-record `r`, `R_F(r)>R_F(r-1)`, so the equal `f`-envelope also jumps
at `r`; hence `f(r)=R_f(r)=R_F(r)=F(r)`.  Conversely, let `r<=x` be the last
strict `F`-record.  Once all such records are equality points,
`R_F(x)=F(r)=f(r)<=R_f(x)<=R_F(x)`.  Since `F` is unbounded, the last record
eventually lies beyond the finite exceptional set.

## Eventual equality

One finite separation does not disprove equality for every sufficiently large
cutoff: later `f`-records can overtake `442`.  It does disprove any universal
transfer of every `F(n)` partition value to `f(m)` with `m<=n`.  A negative
eventual result needs unbounded separating cutoffs; a positive result must be
a theorem about record holders, not arbitrary partitions.

There is an exact one-block obstruction to extracting such a theorem from the
proved first-order asymptotic.  If `F(n)>f(n)`, no maximizing partition can
have `omega(n)` blocks (that would be the singleton partition), and therefore

`F(n)<=(omega(n)-1)n`.                                         (4)

The established estimates `R_f(x)~R_F(x)~x log x/log_2 x` do not resolve an
additive loss of one term of size at most `n`.  By (3), the missing statement
is an additive record-envelope comparison at every prospective bad record,
not another fixed-order relative asymptotic.  Neither recurrence of bad
records nor their eventual absence has been proved locally.
