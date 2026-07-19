# Independent audit of the LPF profile charge

## Scope and verdict

I audited `profile_lpf_charge.md` independently, concentrating on the
largest-prime-factor partition, row and tuple multiplicities, the dyadic
summation, all moving-parameter quantifiers, and the last implication

\[
 |[1,N]\setminus\{f=1\}|=\omega(N/\log N).
\]

**Verdict: no mathematical gap was found in those parts of the argument.**
In particular, the two charges really are supported on disjoint sets of
integers, all tuple overcounting is bounded by a constant depending only on
the fixed reciprocal budget, and the contradiction proves the uniform
`omega` assertion even though the additive function may vary with (N).

The only step outside the main accounting argument that is compressed enough
to merit expansion in a final proof is the local PNT convolution passage
(20)--(25).  Its asserted estimates are consistent and sufficient; I give a
precise expansion target below.  This is a presentation repair, not a detected
counterexample or missing hypothesis.

## 1. Exact row disjointness

Let (X=\sqrt{N/2}), and let (M) be the largest power of two strictly below
(X).  Then, for all relevant (N),

\[
 \sqrt{N/8}\le M<\sqrt{N/2},\qquad \frac{N}{2M}>M.
\]

For (C_j=2^j\le M) and

\[
 P_j=(N/(2C_j),N/C_j]\cap\mathbb P,
\]

every (p\in P_j) satisfies (p>N/(2M)>M\ge C_j\).  Thus for every
(k\le C_j), (p) is the unique largest prime factor of (pk).

The prime intervals (P_j) are pairwise disjoint: the upper endpoint of
(P_{j+1}) is the excluded lower endpoint of (P_j).  If
(pk=q\ell), with (p\in P_j,q\in P_h,k\le C_j,\ell\le C_h), uniqueness of
the prime factor above (M) gives (p=q), then the disjointness of the
(P_j)'s gives (j=h), and finally (k=\ell).  Hence the map

\[
 (j,p,k)\longmapsto pk
\]

is injective.  Consequently

\[
 \sum_j B_j\le |E_>|,
\]

with no hidden multiplicity factor.  The strict inequalities also settle the
boundary (P^+(n)=M): every row error has (P^+(n)>M).

## 2. Lemma 1 and the dyadic reciprocal charge

If (f(p)=1), the target cofactor value is zero, and each active prime
(q\le C_j) supplies a different erroneous cofactor (k=q).  If (f(p)\ne1),
the target (t=1-f(p)) is nonzero, so the previously proved uniform
(cX/\log X) complement bound applies to the completely additive function
(f/t) at (X=C_j).  Together with
(A(C_j)\le\pi(C_j)\ll C_j/\log C_j), this gives a single absolute
(\kappa>0).  No constant depends on (p,j,f), or (N).

For (C_j\le M), put (x=N/C_j).  Then
(x\in[N/M,N]\subset[\sqrt{2N},N]), and the PNT in ((x/2,x]) yields,
uniformly over all these (j),

\[
 |P_j|\gg \frac{x}{\log x}\gg\frac{N}{C_j\log N}.
\]

For each active prime (q\in[C_0,M]), the first dyadic (C_j\ge q) still
satisfies (C_j\le M), and (C_j<2q).  Its single term already contributes
(1/C_j>1/(2q)); hence

\[
 \sum_{C_0\le C_j\le M}\frac{A(C_j)}{C_j}
 \ge \frac12\sum_{\substack{C_0\le q\le M\\f(q)\ne0}}\frac1q.
\]

This verifies both the direction and the constant in the interchange of
sums.  The finitely many primes below the fixed cofactor threshold (C_0)
add only an absolute reciprocal constant.  Therefore

\[
 m\le K N/\log N
 \quad\Longrightarrow\quad
 \sum_{\substack{q\le M\\f(q)\ne0}}\frac1q\le K_1(K),
\]

uniformly even for a sequence of different functions (f=f_N).

## 3. Tuple multiplicity and separation from row errors

In Lemma 3 the chosen interval (I=(N^a,N^{2a}]) comes from a finite menu
depending only on the fixed budget (K_1).  The construction chooses a prime

\[
 \ell\le N^{\delta_0},\qquad \delta_0<a/2,
\]

and (r) distinct primes (q_i\in I).  Thus

\[
 \ell<N^{a}<q_i,
\]

and (n=\ell q_1\cdots q_r) has exactly one prime factor at most
(N^{\delta_0}).  Unique factorization therefore recovers (ell) from (n),
so constructions belonging to different (ell)'s are disjoint.  For fixed
(ell), a given squarefree product has exactly (r!) ordered
representations, not an (N)-dependent number.  Since the finite menu fixes
an upper bound for (r), this loss is absorbed into (c_{K_1}).

The reciprocal-to-cardinality conversion in (28) has the correct direction:
if (Q=q_1\cdots q_r>N/(2\ell)), then (1/Q<2\ell/N).  Hence reciprocal
mass at least (c/L) forces at least (cN/(2\ell L)) ordered tuples.  Summing
over (ell) and dividing by (r!) gives

\[
 \gg_{K_1}\frac N{\log N}
 \sum_{\substack{\ell\le N^{\delta_0}\\\ell\in\mathcal Z_N}}\frac1\ell
 \gg_{K_1}\frac{N\log\log N}{\log N}.
\]

Repeated (q_i)'s have total reciprocal mass

\[
 O_r\!\left(\sum_{q>N^a}q^{-2}\right)=O_r(N^{-a})=o(1/\log N),
\]

so their removal does not affect the lower bound.

After choosing the initial dyadic exponent sufficiently small,
(2a<1/4).  Thus every constructed prime factor is below (N^{1/4}).  Since

\[
 M\ge\sqrt{N/8}>N^{1/4}
\]

for all sufficiently large (N) (indeed (N>64) suffices for the strict
second inequality), all tuple products have (P^+(n)<M).  This is disjoint
from the strict row support (P^+(n)>M).  There is no uncharged equality case.

## 4. Quantifiers and the `omega` conclusion

Fix an arbitrary finite (K).  If a counterexample to the uniform assertion
existed for infinitely many (N), choose along that sequence a possibly
varying completely additive (f_N) with

\[
 m_N\le K N/\log N.
\]

Proposition 2 supplies a reciprocal budget (K_1(K)) independent of (N)
and of the choice of (f_N).  Lemma 3 is explicitly uniform over all moving
prime sets satisfying that fixed budget, so, once (N\ge N_0(K_1)),

\[
 m_N\ge c_{K_1}\frac{N\log\log N}{\log N}.
\]

Here (c_{K_1}>0) may be very small, but it is fixed after (K) is fixed.
Eventually (c_{K_1}\log\log N>K), contradicting the assumed upper bound.
Because this works for every fixed (K), it is exactly the uniform statement

\[
 \inf_f\frac{|[1,N]\setminus\{f=1\}|}{N/\log N}\longrightarrow\infty.
\]

The grading reduction then transfers it in the correct direction: if
(A\subseteq\{f=1\}), then
(N-|A|\ge N-|\{f=1\}|).

## 5. First gap and weakest repair

There is **no first invalid inference in the audited accounting or final
quantifier argument**.

For a dependency-complete presentation, the weakest useful repair is to
expand (20)--(25) into a short standalone lemma.  State that for each fixed
(a>0), fixed (0<u<v<\infty), and intervals (W_N) of exponent length
(\theta/\log N) whose centers remain in the interior of the two-fold sum
interval, partial summation and the PNT give uniformly

\[
 (\mu_N*\mu_N)(W_N)\asymp_a\frac1{\log N},
 \qquad
 \sup_x\mu_N(W_N-x)\ll_a\frac1{\log N}.
\]

Then explicitly partition the compact interval (J) into cells of width
(h/\log N), with (h<\log 2/(4k)).  The interior margin in (24) leaves
(\asymp(\log N)^{k-1}) admissible choices of the first (k-1) cells, and
the forced last cell remains in (J); multiplying (k) cell masses gives
(\gg1/\log N).  This removes the only appreciable compression without
altering the proof.

Two harmless wording/typographical repairs are also advisable:

1. In (32), replace `|E_\leq|geq` by `|E_\leq|\geq`.
2. The sentence after (30) should say that the two charges *may be added
   whenever both estimates have separately been established*.  The dichotomy
   itself establishes (29) or (30), not automatically both.  The proof of the
   `omega` conclusion uses only the bounded-active-mass branch, so this wording
   does not affect validity.
