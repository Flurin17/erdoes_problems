# Almost-all lower bound for `F(n)`: two-band semigroup matching

This route proves, under the nonunit convention, that there is an absolute
constant `c>0` such that

`F(n) >= c n log log n`

for a set of positive integers of natural density one.  The literal
unit-admissible version is larger by one and hence satisfies the same result.
The only analytic inputs are the prime Mertens theorem and a standard uniform
upper-bound sieve estimate for primes in an arbitrary interval.  They are
stated precisely below.  In particular, no unproved equidistribution of primes
with respect to fractional logarithms is being used.

## 1. Standard inputs

The proof invokes the following standard results.

1. **Prime Mertens theorem.**  As `y -> infinity`,

   `sum_{p<=y} 1/p = log log y + B_1 + o(1)`.

   We only apply this with endpoints tending to infinity.  An error `O(1)`
   would actually suffice for all band-mass estimates below.

2. **Uniform short-interval Brun--Titchmarsh/Selberg upper-bound sieve.**  There
   is an absolute `C` such that, for every real `z>=0` and `h>=2`,

   `#{p prime : z < p <= z+h} <= C h/log h`.

   This uniform interval form (with an unspecified absolute constant, rather
   than the sharp constant 2) is the exact form needed in Lemma 2.  It is a
   standard consequence of the Selberg upper-bound sieve.  If one only admits
   a version in a more restricted range of `h`, then Lemma 2 is the precise
   point which would have to be rechecked.  No asymptotic prime number theorem
   in short intervals is assumed.

3. **Konig's theorem.**  In a finite bipartite graph, maximum matching size
   equals minimum vertex-cover size.

The prime number theorem `pi(y)~y/log y` is not separately used.  It may be
used to replace some trivial estimates for the number of primes in a band,
but the trivial bound `pi(y)<=y` already makes every floor error below `o(1)`.

## 2. A metric shrinking-target lemma

All fractional parts in this section are on `R/Z`, with Lebesgue measure
normalized to one.

**Lemma 1 (uniform shrinking target for a rotation parameter).**  Let
`N>=2`, `0<lambda<=1/2`, and `t in R`.  Put

`S(theta)=sum_{1<=b<=N} 1_[0,lambda]({t-b theta})`.

Then

`meas{theta in [0,1):S(theta)=0}
   <= C log(2N)/(N lambda)`                                      (2.1)

for an absolute constant `C`, uniformly in `t`.

**Proof.**  Put `g=1_[0,lambda]-lambda`.  Its nonzero Fourier coefficients
satisfy

`|g_hat(k)| <= min(lambda,1/(pi |k|))`.                         (2.2)

For distinct positive integers `b,c`, write `b=d r`, `c=d s`, where
`d=(b,c)` and `(r,s)=1`.  Orthogonality in `theta` and (2.2) give, assuming
`r<=s`,

```
|int_0^1 g(t-b theta)g(t-c theta)dtheta|
 <= 2 sum_{m>=1} min(lambda,1/(s m))min(lambda,1/(r m))
 <= C (lambda/s)(1+log(s/r)).                                  (2.3)
```

The last inequality follows by splitting the sum at
`1/(s lambda)` and `1/(r lambda)` (empty ranges are simply omitted).
The diagonal contribution is at most `N lambda`.  Moreover,

```
sum_{1<=b<c<=N} ((b,c)/c)(1+log(c/b))
 <= sum_{s<=N} sum_{r<s} sum_{d<=N/s}
       (1/s)(1+log(s/r))
 <= C N log(2N),                                                (2.4)
```

where dropping `(r,s)=1` only enlarges the sum, and
`sum_{r<s}(1+log(s/r))=O(s)`.  Equations (2.3)--(2.4) imply

`int_0^1 |S(theta)-N lambda|^2 dtheta
   <= C N lambda log(2N)`.

On the set `S=0`, the squared deviation is `(N lambda)^2`.
Chebyshev's inequality proves (2.1).  Endpoints of the interval have measure
zero and do not matter.  QED.

This Fourier lemma is the substitute for an unjustified assertion that
`log q/log p` is equidistributed.  It averages over the real rotation
parameter first; Lemma 2 rigorously transfers the resulting small exceptional
set to reciprocal prime mass.

## 3. Transferring logarithmic measure to reciprocal prime mass

**Lemma 2 (upper-bound-sieve transference).**  Let `U>=4`, `V>=U`, and let
`E` be a union of at most `K` intervals in `[U,V]`.  Suppose
`log(K+V)=o(U)`.  Then, uniformly in such `E`,

`sum_{q prime, log q in E} 1/q
   <= C int_E du/u + o(1)`,                                    (3.1)

where the `o(1)` is uniform whenever `U -> infinity` and
`log(K+V)=o(U)`.

**Proof.**  Set `eta=exp(-U/2)`.  Enlarge every component of `E` by at most
`eta` at either endpoint.  The added logarithmic measure is at most
`2K eta/U=o(1)`.  Split the enlarged components into intervals `[a,a+h]` of
length at most one and at least `eta` (enlarging a last short piece again if
necessary).  This introduces at most `O(K+V)` pieces.  Enlarging the final
piece of each component adds at most `O((K+V)eta/U)=o(1)` in logarithmic
measure by the complexity hypothesis.

The corresponding ordinary interval is
`[exp(a),exp(a+h)]`, of length

`Y=exp(a)(exp(h)-1) >= (1/2)exp(a)h >= (1/2)exp(a-U/2)`.

Thus `log Y >= a/3` for all large `U`.  The uniform interval upper-bound sieve
and partial summation (or simply bounding `1/q` by `exp(-a)`) give

`sum_{exp(a)<q<=exp(a+h)}1/q <= C h/a`.

Summing the pieces proves (3.1).  QED.

The complexity hypothesis in this lemma is important.  It is verified below;
one cannot transfer an arbitrary small-measure set to primes using only the
ordinary prime number theorem.

## 4. Most cross-band prime pairs are good

Fix a large dyadic parameter `X` and write

`L=log X`, `ell=log L=log log X`.

Use the two disjoint logarithmic prime bands

```
A=A_X={p prime: L^(1/8) <= log p <= L^(1/4)},
B=B_X={q prime: L^(1/3) <= log q <= L^(1/2)}.
```

Prime Mertens gives

```
M_A:=sum_{p in A}1/p = (1/8)ell+o(ell),
M_B:=sum_{q in B}1/q = (1/6)ell+o(ell).                         (4.1)
```

Call `(p,q) in A x B` **good** if there are integers `a,b>=1` with

`X/e <= p^a q^b <= X`;                                         (4.2)

otherwise call it bad.

**Lemma 3 (bad harmonic pair mass is negligible).**

`W_bad(X):=sum_{(p,q) bad}1/(pq)=o(ell^2)`.                     (4.3)

**Proof.**  Fix `p in A`, put `alpha=log p`, and let

`B_0=L^(1/3)`, `B_1=L^(1/2)`,
`N=floor(L/(3B_1))`, `lambda=1/alpha`, `t=L/alpha`.

For `q in B`, set `beta=log q` and `theta=beta/alpha`.  If for some
`1<=b<=N` one has

`{t-b theta} in [0,lambda]`,                                   (4.4)

then, with `a=floor((L-b beta)/alpha)`,

`0 <= L-a alpha-b beta <= 1`.

Also `b beta<=L/3` and therefore `a>=1` for large `X`.  Hence (4.4)
produces (4.2).  Consequently every bad `q` has `theta` in the period-one set

`E_p={theta:S(theta)=0}`

from Lemma 1.  Uniformly for `p in A`,

```
delta_X:=meas(E_p intersect [0,1))
 <= C alpha log(2N)/N
 <= C L^(-1/4) log L=o(1).                                    (4.5)
```

The relevant theta interval begins at
`B_0/alpha >= L^(1/12)`.  Since `E_p` is period one, summing over its full
unit intervals with weight `1/theta`, and treating the two end intervals
trivially, gives

```
int_{B_0/alpha}^{B_1/alpha} 1_{E_p}(theta)dtheta/theta
 <= delta_X log(B_1/B_0)+O(alpha/B_0)
 =o(ell),                                                       (4.6)
```

uniformly in `p`.  The change of variables `beta=alpha theta` preserves the
measure `d beta/beta=d theta/theta`.

It remains to transfer (4.6) to primes, for which the complexity must be
checked.  In a theta interval of length `R`, the boundary of the condition
`{t-b theta} in [0,lambda]` has `O(bR+1)` points.  Thus `E_p` restricted to
the relevant interval, and hence its beta-image, has at most

`K=O(N^2(B_1-B_0)/alpha+N)`

components.  Here `K` is a fixed power of `L`, while `B_0=L^(1/3)`; hence
`log(K+B_1)=O(log L)=o(B_0)`.  Lemma 2 and (4.6) now yield, uniformly in
`p in A`,

`sum_{q in B:(p,q) bad}1/q=o(ell)`.                             (4.7)

Multiplying by `1/p`, summing over `p in A`, and using (4.1), proves
(4.3).  QED.

Notice the deliberately separated exponents `1/4<1/3` and
`1/4+1/2<1`.  The first makes the theta interval start far beyond zero; the
second gives `N lambda -> infinity` uniformly and is the source of the
shrinking-target gain.

## 5. Almost every integer sees a large good matching

For `X<=n<2X`, define

```
R_A(n)=#{p in A:p|n},
R_B(n)=#{q in B:q|n},
Z(n)=#{(p,q) bad:pq|n}.
```

Average throughout this section with respect to the `X+O(1)` integers in the
dyadic interval.  For every integer `d<=X`,

`#{X<=n<2X:d|n}=X/d+O(1)`.                                     (5.1)

All primes in `A union B` and all products of two such primes are
`exp(O(L^(1/2)))=X^(o(1))`.  Expanding first and second moments using (5.1),
and bounding the total floor errors by
`O((#(A union B))^2/X)=o(1)`, gives

```
E R_A=M_A+o(1),       Var(R_A)<=M_A+o(M_A),
E R_B=M_B+o(1),       Var(R_B)<=M_B+o(M_B).                     (5.2)
```

Thus Chebyshev and (4.1) show that, outside `o(X)` integers in the interval,

`R_A(n)>=ell/10` and `R_B(n)>=ell/10`.                          (5.3)

Similarly, Lemma 3 and (5.1) give

`E Z(n)=W_bad(X)+o(1)=o(ell^2)`.                               (5.4)

By Markov,

`Z(n)=o(ell^2)`                                                   (5.5)

in probability on `[X,2X)`; in particular, outside `o(X)` integers it is
less than `ell^2/200`.

For such an `n`, form the bipartite graph whose left vertices are the primes
of `A` dividing `n`, whose right vertices are the primes of `B` dividing `n`,
and whose edges are the good pairs.  If its maximum matching had fewer than
`ell/40` edges, Konig's theorem would give a vertex cover of fewer than
`ell/40` vertices.  After deleting that cover, both sides would retain at
least `3ell/40` vertices, and every one of the at least
`9ell^2/1600>ell^2/200` cross pairs would be bad.  This contradicts (5.5).
Therefore, for all but `o(X)` integers `n in [X,2X)`, there is a matching of
at least `ell/40` good pairs.

Choose one number `p^a q^b` satisfying (4.2) for every edge of this matching.
The selected numbers have disjoint prime supports, hence are pairwise
coprime; all their prime factors divide `n`; and they lie below `X<=n`.
Since `n<2X`, each is at least `X/e>n/(2e)`.  Therefore

`F_{>1}(n) >= (ell/40)(X/e) >= n ell/(80e)`.                    (5.6)

As `log log n=ell+o(1)` uniformly on the dyadic interval, (5.6) is the desired
absolute lower bound there.

## 6. From dyadic density to natural density

Apply the preceding argument with `X=2^j`.  If `epsilon_j 2^j` is the number
of exceptions in `[2^j,2^(j+1))`, then `epsilon_j ->0`.  Given `eta>0`, choose
`j_0` so that `epsilon_j<eta` for all `j>=j_0`.  For
`2^J<=Y<2^(J+1)`, the exceptions below `Y` are bounded by a fixed initial
quantity plus

`sum_{j_0<=j<=J} eta 2^j <=2 eta 2^J<=2 eta Y`.

Letting first `Y->infinity` and then `eta->0` proves natural density one.

## 7. Dependency status and falsification tests

The route is dependency-complete modulo the three explicitly stated standard
inputs.  The delicate input is the uniform interval upper-bound sieve in
Section 1; ordinary PNT or ordinary Mertens alone would not justify Lemma 2.
No continued-fraction uniformity, random-prime model, or unproved short-
interval asymptotic remains.

Concrete checks which can falsify implementation errors (but are not part of
the proof) are:

1. for fixed dyadic `X`, enumerate cross-band pairs and verify that every pair
   declared good comes with positive exponents and a value in `[X/e,X]`;
2. compare `W_bad/(M_A M_B)` as `X` grows;
3. for sampled `n in [X,2X)`, verify that a computed matching uses disjoint
   primes and that its chosen semigroup values are all at most `n`.

The proof itself gives only a deliberately nonoptimized absolute constant.
The band endpoints and `1/(80e)` can be improved, but this has no bearing on
the stated `F(n) >> n log log n` conclusion.
