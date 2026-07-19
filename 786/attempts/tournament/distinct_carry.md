# Carry/logarithm route for internally distinct factors

## Status

This note gives a rigorous sufficient condition for the internally-distinct
interpretation and evaluates the most immediate logarithmic attempt.  The
sufficient condition is exact.  The calculation shows that the unmodified
normalized logarithm misses its required summability threshold by order
\(N/\log N\), even after deleting \(o(N)\) integers.  It does not exclude
more flexible additive functions or nonconstant congruence representatives.

## 1. A summable-carry criterion

Let \(A\) be a finite set of positive integers.  Say that \(A\) is
internally-distinct product-length-rigid if every equality
\[
 \prod_{a\in S}a=\prod_{a\in T}a,
 \qquad S,T\subseteq A,
\]
implies \(|S|=|T|\).  Thus repetitions are forbidden within each side;
common elements may occur on both sides and may be cancelled.

### Lemma 1 (summable congruence approximation)

Let \(\phi:\mathbb N\to\mathbb R\) be completely additive.  Suppose that
there are an integer \(M>|A|\) and integers \(c_a\), one for each
\(a\in A\), such that
\[
 c_a\equiv1\pmod M
 \quad\text{for every }a\in A,
\]
and
\[
 \sum_{a\in A}|\phi(a)-c_a|<1.
\]
Then \(A\) is internally-distinct product-length-rigid.

### Proof

Suppose
\[
 \prod_{a\in S}a=\prod_{a\in T}a.
\]
Cancel \(S\cap T\), so that the remaining sets are disjoint.  Put
\(\varepsilon_a=1\) on \(S\), \(-1\) on \(T\), and \(0\) otherwise.
Complete additivity gives
\[
 \sum_{a\in A}\varepsilon_a\phi(a)=0.
\]
The integer
\[
 C:=\sum_{a\in A}\varepsilon_ac_a
\]
satisfies
\[
 |C|
 =\left|\sum_{a\in A}\varepsilon_a(c_a-\phi(a))\right|
 \leq\sum_{a\in A}|c_a-\phi(a)|<1.
\]
Hence \(C=0\).  Reducing modulo \(M\),
\[
 0=C\equiv\sum_a\varepsilon_a=|S|-|T|\pmod M.
\]
But \(||S|-|T||\leq |A|<M\), so \(|S|=|T|\).  Reinstating the cancelled
intersection preserves the length difference, proving the claim.
\(\square\)

The strict inequality below one is essential to this elementary argument:
it turns an approximately vanishing integer into the exactly vanishing
integer \(C=0\).  The modulus then recovers length because distinctness
bounds the possible length difference by \(|A|\).

## 2. Pure normalized logarithm has too much total slack

The first candidate is
\[
 \phi_N(a)=\frac{\log a}{\log N},
 \qquad c_a=1.
\]
It is completely additive and \(c_a\equiv1\pmod M\) for every modulus,
but its total approximation error is not summable on a density-one set.

### Proposition 2 (sharp density-one logarithmic slack)

If \(A_N\subseteq[N]\) and \(|A_N|=N-o(N)\), then
\[
 \sum_{a\in A_N}\left(1-\frac{\log a}{\log N}\right)
 \geq (1-o(1))\frac{N}{\log N}.
\]
This is sharp: taking \(A_N=[N]\) gives equality to first order.  Equivalently,
\[
 \inf_{|A|=N-o(N)}
 \sum_{a\in A}\left(1-\frac{\log a}{\log N}\right)
 =(1-o(1))\frac{N}{\log N},
\]
where the infimum is understood along arbitrary density-one sequences.

### Proof

Write \(|[N]\setminus A|=m=o(N)\).  The summand
\[
 s_N(a)=\frac{\log(N/a)}{\log N}
\]
is nonnegative and decreases with \(a\).  Among all subsets of size
\(N-m\), its sum is therefore minimized by retaining the largest
\(N-m\) integers, namely by \(A=\{m+1,\ldots,N\}\).  Thus
\[
 \sum_{a\in A}s_N(a)
 \geq\frac1{\log N}\sum_{a=m+1}^N\log\frac Na.
\]
The numerator is
\[
 (N-m)\log N-\log\frac{N!}{m!}.
\]
Stirling's estimate \(\log r!=r\log r-r+O(\log(r+1))\) gives
\[
 \sum_{a=m+1}^N\log\frac Na
 =N-m-m\log\frac Nm+O(\log N).
\]
With the convention \(m\log(N/m)=0\) at \(m=0\), the assumptions imply
\[
 m=o(N),
 \qquad
 m\log\frac Nm
 =N\frac mN\log\frac N m=o(N).
\]
The lower bound is consequently \((1-o(1))N/\log N\).

For sharpness, Stirling applied with \(m=0\) gives
\[
 \sum_{a=1}^N\left(1-\frac{\log a}{\log N}\right)
 =\frac{N+O(\log N)}{\log N}
 =(1+o(1))\frac N{\log N}.
\]
\(\square\)

Thus the pure choice \(\phi_N(a)=\log a/\log N\), \(c_a=1\) has total
error of order \(N/\log N\), whereas Lemma 1 needs total error below one.
Deleting \(o(N)\) elements cannot bridge this gap.  This is only an
obstruction to the pure-log implementation of the summable-carry lemma;
it is not an obstruction to internally-distinct rigidity itself.

