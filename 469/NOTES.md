# Notes for Erdős Problem #469

This file records distilled definitions, equivalent formulations,
calculations, and proved lemmas.  The authoritative statement is in
`PROBLEM.md`.

## Definitions

For \(n\geq1\), let
\[
D^*(n)=\{d\in\mathbb Z_{>0}:d\mid n,\ d<n\}.
\]
Call \(n\) **semiperfect** if some nonempty subset \(S\subseteq D^*(n)\)
satisfies \(\sum_{d\in S}d=n\).  Let \(A\) be the semiperfect integers for
which every proper divisor is not semiperfect.

The clauses “distinct” and “proper” say precisely that the witness is a
subset of \(D^*(n)\), not a multiset.  The empty subset and one-element
subsets cannot represent a positive \(n\), and 1 is not semiperfect.

## Exact reformulations

Let
\[
 Q_n(x)=\prod_{\substack{d\mid n\\d<n}}(1+x^d),\qquad
 E(n)=\sigma(n)-2n.
\]
Then the following are equivalent.

1. \(n\) is semiperfect.
2. \([x^n]Q_n(x)>0\).
3. \(E(n)\geq0\) and \(E(n)\) is a subset sum of \(D^*(n)\).
4. There is a set \(R\) of distinct divisors \(r>1\) of \(n\) such that
   \(\sum_{r\in R}1/r=1\).

For (3), complement a selected subset inside all the proper divisors, whose
sum is \(\sigma(n)-n\).  For (4), use the bijection \(d\leftrightarrow n/d\).
Consequently semiperfect numbers are nondeficient: \(\sigma(n)\geq2n\).
Every perfect number is semiperfect.

Writing \(n=\prod_i p_i^{a_i}\), the same assertion is the existence of
\(0/1\) coefficients on the exponent box
\(\prod_i\{0,\ldots,a_i\}\setminus\{(a_i)_i\}\) whose associated divisors
sum to \(n\).  In reciprocal form the chosen exponent vectors must sum to 1
after replacing \(p_i^{b_i}\) by \(p_i^{-b_i}\).

## Divisibility closure and minimality

### Lemma 1 (unconditional lifting)

If \(m\) is semiperfect and \(m\mid n\), then \(n\) is semiperfect.

Indeed, if \(m=\sum_{d\in S}d\) and \(n=qm\), then
\(n=\sum_{d\in S}qd\); the new summands are still distinct proper divisors.
No coprimality assumption is needed.

It follows that semiperfect numbers form a divisibility up-set, \(A\) is its
unique set of minimal elements, and \(A\) is a divisibility antichain.  More
locally,
\[
n\in A\quad\Longleftrightarrow\quad n\text{ is semiperfect and }n/p
\text{ is not semiperfect for every prime }p\mid n.                 \tag{1}
\]
For if a proper semiperfect \(m\mid n\) existed, choose
\(p\mid n/m\); then \(m\mid n/p\), and lifting makes \(n/p\)
semiperfect.

### Lemma 2 (full-support witnesses)

A semiperfect \(n\) lies in \(A\) if and only if every witness
\(n=\sum_{d\in S}d\) has \(\gcd(S)=1\).

If a witness has gcd \(g>1\), division gives a witness for the proper divisor
\(n/g\).  Conversely, a witness for a proper \(m\mid n\), scaled by \(n/m\),
is a witness for \(n\) whose gcd is greater than 1.  In the unit-fraction
form this says that **every** identity \(\sum_{r\in R}1/r=1\) with \(r\mid n\)
has
\[
\operatorname{lcm}(R)=n,
\]
because \(\gcd\{n/r:r\in R\}=n/\operatorname{lcm}(R)\).  Existence of just
one gcd-one witness is insufficient: \(12=6+3+2+1\), but 6 is a semiperfect
proper divisor.

### Lemma 3 (prime-layer saturation)

Let \(n\in A\), let \(p^a\Vert n\), and put \(m=n/p^a\).  Every witness for
\(n\) contains at least two summands not divisible by \(p\), and
\[
p\leq\sigma(m).                                                     \tag{2}
\]

By Lemma 2 there is at least one \(p\)-free selected summand.  Their positive
sum is congruent to 0 modulo \(p\), so there cannot be exactly one.  Every
such summand divides \(m\), and their sum is a positive multiple of \(p\) at
most \(\sigma(m)\), proving (2).  Dually, every reciprocal witness contains
at least two denominators with full \(p\)-adic exponent \(a\).  In particular
\(n^2\) divides the product of all denominators in every reciprocal witness.

## Abundancy and terminology

Let \(I(n)=\sigma(n)/n\).  If \(d\mid n\) properly, then \(I(d)<I(n)\), as
is immediate from the prime-power product for \(I\).  Hence every proper
divisor of a perfect number is deficient, and therefore **every perfect
number belongs to \(A\)**.

Here “primitive abundant” means abundant with every proper divisor deficient,
and “weird” means abundant but not semiperfect.  These are not synonyms for
membership in \(A\): 70 is primitive abundant and weird, since its proper
divisors sum to 74 but a subset summing to 70 would have complementary sum 4,
which cannot be made from \(1,2,5,7,10,14,35\).  Conversely,
\[
350=175+70+50+25+14+10+5+1
\]
belongs to \(A\), although it has the abundant proper divisor 70.  All other
proper divisors of 350 are deficient, and 70 is not semiperfect, so the claim
follows from (1).  Thus a convergence proof restricted to primitive abundant
numbers misses genuine members of \(A\).

## Complete two-prime-support classification

### Theorem 4

The members of \(A\) with at most two distinct prime factors are exactly
\[
 n=2^a p,\qquad a\geq1,\quad 2^a<p<2^{a+1},                         \tag{3}
\]
where \(p\) is prime.  Their reciprocal sum converges.

A prime power is deficient.  An odd number supported on at most two primes is
also deficient, because
\[
I(n)<\frac32\frac54<2.
\]
For \(n=2^a p^b\), semiperfectness holds exactly when
\(p\leq2^{a+1}-1\).  Sufficiency already holds for \(2^ap\): select
\(p,2p,\ldots,2^{a-1}p\), whose sum is \(p(2^a-1)\), and select the binary
expansion of \(p\) from \(1,2,\ldots,2^a\).  Then lift by \(p^{b-1}\).
For necessity, if \(p>2^{a+1}-1\), group a putative witness by powers of
\(p\).  Reducing modulo \(p\), the bottom coefficient is a subset sum of
\(1,2,\ldots,2^a\), hence lies below \(p\) and must vanish.  Divide by \(p\)
and repeat; the top layer would finally have to sum to \(2^a\) using only
\(1,2,\ldots,2^{a-1}\), a contradiction.

Minimality forces \(b=1\); and the largest possible same-support proper
divisor \(2^{a-1}p\) is semiperfect exactly when \(p\leq2^a-1\).  This gives
(3), with endpoints simplified using the oddness of \(p\).  Finally there are
at most \(2^a\) candidates for each \(a\), each exceeding \(2^{2a}\), so
their reciprocal mass is at most \(\sum_a2^{-a}\).

## Squarefree boundary facts

- The only squarefree member of \(A\) with at most three prime factors is 6.
  For odd support of size at most three, abundance is already impossible.  If
  \(n=2pq\) with \(3\leq p<q\), nondeficiency is equivalent to
  \((p-3)(q-3)\leq12\).  The branch \(p=3\) contains 6; the only other case is
  70, which is not semiperfect.
- Every odd squarefree semiperfect number has at least five prime factors,
  since the maximum abundancy with four odd primes is
  \((4/3)(6/5)(8/7)(12/11)=768/385<2\).
- If \(r>7\) is prime, then \(70r\in A\) exactly for
  \(11\leq r\leq139\).  For \(r>144=\sigma(70)\), the large-prime lemma below
  rules out semiperfectness.  For primes \(11\leq r\leq139\), the divisors of
  70 have subset sums containing every integer in \([5,139]\), while
  \(69=35+14+10+7+2+1\); selecting a base-layer sum \(r\) and the indicated
  \(r\)-layer sum gives \(70r\).  All proper squarefree supports have at most
  three primes and are nonsemiperfect.

### Lemma 5 (large-prime nonactivation)

If \(m\) is not semiperfect, \(p\) is prime, and \(p>\sigma(m)\), then
\(pm\) is not semiperfect (coprimality is unnecessary).

Partition a witness for \(pm\) into divisors already dividing \(m\), of sum
\(X\), and the remaining divisors, all of the form \(pd\), of sum \(pY\).
Then \(pm=X+pY\) with \(0\leq X\leq\sigma(m)<p\).  Reduction modulo \(p\)
forces \(X=0\), and division by \(p\) gives a witness for \(m\), a
contradiction.

## Subset-sum defect and extension lemmas

For a nonsemiperfect \(m\), define its one-sided defect
\[
g(m)=\min\{m-U:U<m\text{ is a subset sum of }D^*(m)\}.
\]
If \(p\mid n\), put \(N=n/p\) and \(m=n/p^{v_p(n)}\).  Splitting any witness
for \(n\in A\) into its \(p\)-free and \(p\)-divisible parts gives
\[
p\,g(N)\leq\sigma(m).                                               \tag{4}
\]
Indeed the \(p\)-free sum is \(pk>0\), and after dividing the other part by
\(p\), one has \(N=U+k\).  If \(N\) is deficient, then
\(g(N)\geq2N-\sigma(N)\).

For \(p\nmid m\), the exact extension criterion is: \(pm\) is semiperfect if
and only if there is an integer \(h\geq1\) such that \(m-h\) is a subset sum
of proper divisors of \(m\), and \(ph\) is a subset sum of all divisors of
\(m\).  This follows by writing a witness uniquely as \(pU+V=pm\).

## Fixed support size

### Theorem 6

For every fixed \(k\),
\[
\sum_{\substack{n\in A\\\omega(n)=k}}\frac1n<\infty.                \tag{5}
\]

The key uniform branching lemma is the following.  If \(n=uv\in A\),
\((u,v)=1\), \(t=\omega(v)\), and \(q\) is the least prime factor of \(v\),
then
\[
q\leq2t\,\sigma(u).                                                 \tag{6}
\]
Group a witness by its \(v\)-part.  If \(S_v\) denotes the sum of the
selected \(u\)-parts in the top group, then \(S_v\leq u\), and equality would
make \(u\) semiperfect, contrary to minimality.  Hence
\[
v\leq v(u-S_v)
   =\sum_{e\mid v,\ e<v}eS_e
   \leq\sigma(u)(\sigma(v)-v),
\]
so \(I(v)-1\geq1/\sigma(u)\).  On the other hand
\[
I(v)<\left(1+\frac1{q-1}\right)^t
       \leq\exp\!\left(\frac{t}{q-1}\right).
\]
If \(q-1\geq2t\sigma(u)\), the last expression minus 1 is strictly below
\(1/\sigma(u)\), a contradiction.  This proves (6).

Order the prime powers of \(n\) as
\(p_1^{a_1},\ldots,p_k^{a_k}\).  Applying (6) to each prefix gives
\[
p_j\leq C_k\prod_{i<j}p_i^{a_i}                                    \tag{7}
\]
for a constant depending only on \(k\), and in particular \(p_1\leq2k\).
To sum the resulting overcount, recursively choose \(p_j\) under (7) and
sum \(a_j\geq1\).  The elementary bounds
\[
\sum_{r\leq x}\frac1r\leq1+\log x,
\qquad
\sum_{a\geq1}\frac{(1+a\log r)^B}{r^a}<\infty
\]
show inductively that the remaining reciprocal mass after a fixed prefix is
bounded by a polynomial in the logarithm of that prefix.  Since the first
prime has only finitely many choices, (5) follows.  The constants currently
depend badly on \(k\); summing (5) over unbounded \(k\) is not justified.

## Counting criterion

If \(A(x)=|A\cap[1,x]|\), partial summation and dyadic grouping give
\[
\sum_{n\in A}\frac1n<\infty
\quad\Longleftrightarrow\quad
\int_1^\infty\frac{A(t)}{t^2}\,dt<\infty
\quad\Longleftrightarrow\quad
\sum_{j\geq0}\frac{A(2^j)}{2^j}<\infty.                             \tag{8}
\]
Thus \(A(x)\ll x/(\log x)^{1+\varepsilon}\) would suffice, while
\(A(x)=o(x)\) or \(A(x)\ll x/\log x\) alone would not.

## Exact current obstruction

Equations (2), (4), (6), and fixed-\(\omega\) convergence do not yet give a
bound uniform enough to sum over \(\omega(n)\).  The difficult coatoms are
abundant nonsemiperfect numbers with tiny subset-sum defect (70 has defect
1), together with deficient coatoms of very small deficiency.  Any complete
convergence proof must control their weighted extension trees; any divergence
proof must give an explicit infinite boundary family and verify minimality of
every proper divisor.
