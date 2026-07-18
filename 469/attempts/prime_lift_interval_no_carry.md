# Prime lifts of a weird integer: exact gaps and a summable no-carry branch

This note proves a partial result for Problem 469.  It does **not** settle the
remaining case described at the end.

## 1. Exact two-layer criterion

For an integer `m`, write

\[
 D(m)=\{d:d\mid m\},\qquad P(m)=D(m)\setminus\{m\},
\]

and let `Sigma(F)` denote all subset sums of a finite set `F`, including the
empty sum.  Suppose that `m` is weird: `sigma(m)>2m` and
`m notin Sigma(P(m))`.  Put

\[
 E(m)=\sigma(m)-2m,
 \qquad
 \Delta(m)=\min\{m-t>0:t\in\Sigma(P(m))\}.
\]

Complementation inside `P(m)`, whose sum is `m+E(m)`, gives the equivalent
formula

\[
 \Delta(m)=\min\{r>0:E(m)+r\in\Sigma(P(m))\}.                 \tag{1}
\]

Let `p` be prime and coprime to `m`.  Every proper divisor of `mp` is in one
of the disjoint layers `D(m)` and `pP(m)`.  Therefore

\[
 mp\text{ is semiperfect}
 \quad\Longleftrightarrow\quad
 \exists k\ge1:\quad
 E(m)+k\in\Sigma(P(m)),\quad pk\in\Sigma(D(m)).              \tag{2}
\]

Indeed, a witness has the form

\[
 \sum A+p\sum B=pm,qquad A\subseteq D(m),\quad B\subseteq P(m).
\]

The number `k=m-sum B` is positive: equality to zero would make `m`
semiperfect, and a negative value is incompatible with `sum A>=0`.  Thus
`sum A=pk`.  If `C=P(m)\setminus B`, then

\[
 \sum C=(m+E(m))-(m-k)=E(m)+k.
\]

The converse reverses these steps.  In particular,

\[
 p\le {\sigma(m)\over\Delta(m)}.                              \tag{3}
\]

More precisely, if

\[
 {\sigma(m)\over j+1}<p\le {\sigma(m)\over j},
\]

then a witness in (2) has `k<=j`.

## 2. The top half is exact and automatically minimal

If `p>sigma(m)/2`, (2) forces `k=1`.  Hence

\[
 mp\text{ is semiperfect}
 \quad\Longleftrightarrow\quad
 E(m)+1\in\Sigma(P(m))\text{ and }p\in\Sigma(D(m)).           \tag{4}
\]

Every semiperfect lift in (4) is in the set `A` of Problem 469.  First, every
divisor of a weird integer is nonsemiperfect, since semiperfectness lifts
under multiplication.  If `d<m` divides `m` and `t=m/d`, then

\[
 t\sigma(d)=\sum_{e\mid d}te\le\sigma(m),
\]

so `sigma(d)<=sigma(m)/2<p`.  If `d` is nonsemiperfect and `p>sigma(d)`,
then `dp` is nonsemiperfect: splitting a hypothetical witness as
`A+pB=pd`, either `sum B=d` witnesses `d`, or
`sum A=p(d-sum B)>=p>sigma(d)`.  Thus all proper divisors `d` and `pd` of
`mp` are nonsemiperfect.

The same proof gives a useful hierarchy.  If `p>sigma(m)/(j+1)`, then only
proper divisors `d=m/t` with `2<=t<=j` can possibly make `pd`
semiperfect; all indices `t>=j+1` are automatically excluded.

For a fixed weird base, the reciprocal mass of its top-half lifts is

\[
 \sum_{\substack{\sigma(m)/2<p\le\sigma(m)\\mp\in A}}{1\over mp}
 \ll {1\over m\log(2m)},                                      \tag{5}
\]

by the elementary Chebyshev prime-counting bound.  The summation of the
right side over all eligible weird bases is not proved here.

### Example showing that congruences need not thin the primes

For `m=70`, `sigma(m)=144`, `E(m)=4`, and `Delta(m)=1`.  Direct interval
addition gives

\[
 \Sigma(P(70))=[0,74]\setminus\{4,70\},
 \qquad
 \Sigma(D(70))=[0,144]\setminus\{4,140\}.                    \tag{6}
\]

For completeness, the subset sums of
`{1,2,5,7,10,14}` are `[0,39]` except `4,35`; adjoining `35` proves the
first identity, and adjoining `70` proves the second.  It follows from (4)
that

\[
 70p\in A\qquad(73\le p\le139,\ p\text{ prime}).              \tag{7}
\]

Thus an entire prime interval can survive the exact subset-sum condition.
For `p=139`, take `C={5}`, `B=P(70)\setminus C`, and
`A=D(70)\setminus C`; their sums are `5,69,139`, respectively.

## 3. Exact no-carry recursion

The gap definition extends verbatim to every nonsemiperfect integer.  Let
`u` be nonsemiperfect, let `q` be a prime not dividing `u`, and suppose

\[
 q>\sigma(u)=s.
\]

For `a>=1`, put `m=uq^a`.  Divisor subset sums have genuine base-`q`
digits: the lower `a` coefficients lie in `Sigma(D(u))`, and the top
coefficient lies in `Sigma(P(u))`; every coefficient is smaller than `q`.
Consequently

\[
 \begin{split}
 E(uq^a)&=q^aE(u)+s{q^a-1\over q-1},\\
 \Delta(uq^a)&=q^a\Delta(u)-s{q^a-1\over q-1}.                \tag{8}
 \end{split}
\]

For the second identity, a subset sum above `E(uq^a)` must have top
coefficient at least `E(u)+Delta(u)`; choosing that coefficient and zero
lower digits attains the displayed difference.  The same no-carry argument
shows that if `u` is weird, every `uq^a` is weird.

Now suppose that `m=uq^a` is weird and that a prime `p>q` makes `mp`
semiperfect.  From (3) and (8),

\[
 p\le X_a:={s(q^{a+1}-1)\over
 q^a((q-1)\Delta(u)-s)+s}.
\]

Since `p>q`, the inequality `X_a>q` gives exactly

\[
 q^{a+1}\bigl(2s-(q-1)\Delta(u)\bigr)>s(q+1).                \tag{9}
\]

Thus `(q-1)Delta(u)<2s`.  Since `q>s` and `Delta(u)>=1`, this forces

\[
 \Delta(u)=1,\qquad s<q<2s+1.                                \tag{10}
\]

In the actual weird setup, `u` is itself weird.  It cannot be semiperfect,
since such a witness would lift.  If it were deficient, `Delta(u)=1` would
mean `sigma(u)=2u-1`; for `u>1`, a prime `q>2u-1` has `q>2u`, and then

\[
 {\sigma(uq^a)\over uq^a}
 <\left(2-{1\over u}\right){q\over q-1}<2,
\]

contrary to `m` being weird.  The case `u=1` is also deficient after
lifting.

## 4. Convergence of the whole no-carry branch

We now sum all integers of the form

\[
 n=uq^ap,qquad q>s=\sigma(u),\quad p>q,quad uq^a\text{ weird},
 \quad uq^ap\text{ semiperfect}.                              \tag{11}
\]

This overcounts the members of `A`, which is harmless for convergence.
By (10), only `Delta(u)=1` and `s<q<2s+1` occur.  Write

\[
 h=q-1-s.
\]

If `h>=1`, (8) gives

\[
 X_a={s(q^{a+1}-1)\over hq^a+s}<{sq\over h}.                 \tag{12}
\]

Summing `q^{-a}` over `a>=1`, the contribution for a fixed `u` is at most
a constant times

\[
 {1\over u}K(s),\qquad
 K(s)=\sum_{\substack{s+2\le q<2s+1\\q\ {m prime}}}{1\over q}
       \sum_{\substack{q<p\le sq/(q-1-s)\\p\ {m prime}}}{1\over p}.
                                                                    \tag{13}
\]

We claim

\[
 K(s)\ll {1\over\log^2(2s)}.                                  \tag{14}
\]

Chebyshev's estimate and partial summation give, uniformly for
`1<=h<s`,

\[
 \sum_{q<p\le sq/h}{1\over p}
 \ll {1+\log(s/h)\over\log(2s)}.                              \tag{15}
\]

It remains to prove

\[
 \sum_{\substack{s+2\le q<2s+1\\q\ {m prime}}}
       (1+\log(s/(q-1-s)))\ll {s\over\log(2s)}.               \tag{16}
\]

For `h<=sqrt(s)`, the trivial count gives `O(sqrt(s) log(2s))`, which is
acceptable.  For the dyadic ranges

\[
 s/2^{j+1}<h\le s/2^j,\qquad h>\sqrt{s},
\]

Brun--Titchmarsh bounds the number of possible primes `q` by
`O(s/(2^j log(2s)))`, while the weight is `O(j+1)`.  Summing
`(j+1)/2^j` proves (16), hence (14).  Therefore this part of (11) is at
most

\[
 \sum_{u\ge2}{1\over u\log^2(2\sigma(u))}<\infty.             \tag{17}
\]

Finally, if `h=0`, then the only possible prime is `q=s+1`.  Formula (8)
gives `Delta(uq^a)=1` and `X_a=q^{a+1}-1`.  A prime-reciprocal estimate
gives

\[
 \sum_{q<p\le X_a}{1\over p}\ll\log(a+2),
\]

and hence

\[
 \sum_{a\ge1}{\log(a+2)\over q^a}\ll {1\over q}.
\]

The exceptional contribution is bounded by

\[
 \sum_u {1\over u(\sigma(u)+1)}\ll\sum_u{1\over u^2}<\infty. \tag{18}
\]

Equations (17)--(18) prove that the complete no-carry predecessor branch
is reciprocally summable.

## 5. Composite largest exact blocks are harmless

There is a second unconditional convergent branch.  Consider all

\[
 n=uq^ap,\qquad P^+(u)<q<p,\qquad a\ge2,
\]

and impose only the necessary inequality `p<=sigma(uq^a)`.  This is already
a superset of the relevant prime lifts.  The elementary prime-reciprocal
bound and `sigma(v)<=v^2` give

\[
 \sum_{q<p\le\sigma(uq^a)}{1\over p}
 \ll \log\bigl(e+\log u+a\log q\bigr).                       \tag{19}
\]

For fixed `q`, put

\[
 Z_q=\sum_{P^+(u)<q}{1\over u}
     =\prod_{r<q}(1-r^{-1})^{-1}\ll\log(2q).
\]

Under the probability measure `Z_q^{-1}/u`, the prime exponents of `u`
are independent geometric variables, and

\[
 \mathbb E(\log u)=\sum_{r<q}{\log r\over r-1}\ll\log(2q).
\]

The last estimate follows from Chebyshev's bound by partial summation.
Since `x -> log(e+x+a log q)` is concave, Jensen's inequality yields

\[
 \sum_{P^+(u)<q}{\log(e+\log u+a\log q)\over u}
 \ll \log(2q)\bigl(\log(a+1)+\log\log(3q)\bigr).             \tag{20}
\]

Consequently the total reciprocal mass in this branch is at most

\[
 \sum_q\sum_{a\ge2}{\log(2q)
       (\log(a+1)+\log\log(3q))\over q^a}<\infty.             \tag{21}
\]

No weirdness or minimality was used in this estimate.

## 6. Remaining bottleneck

Write a prospective member as `n=mp=uq^ap`, where `p=P(n)` and
`q=P(m)`.  The argument above settles `q>sigma(u)`.  A crude exact-block
Euler-product argument also settles `a>=2`, even after paying the final
prime harmonic factor.  The unresolved core is therefore

\[
 m=uq\text{ weird},\qquad P(u)<q\le\sigma(u),\qquad p>q,
\qquad mp\text{ semiperfect}.                                \tag{22}
\]

When `u` is deficient this is a first-abundance-crossing problem.  When
`u` is itself weird, (22) is a genuinely recursive smooth prime extension;
the exact condition (2), rather than abundance alone, still has to supply
the missing summability.
