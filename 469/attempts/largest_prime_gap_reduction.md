# Largest-prime reduction using the subset-sum gap

This note gives a rigorous reduction for the full set \(A\), not merely for
primitive nondeficient integers. It proves convergence outside one explicit
"combinatorially inert" top-two-prime regime.

## Gap propagation

For a nonsemiperfect integer \(m\), let
\[
 g(m)=\min\{m-U:U<m,\ U\text{ is a subset sum of }D^*(m)\},
 \qquad R(m)=\frac{\sigma(m)}{g(m)}.                                \tag{1}
\]
The empty subset is harmless and ensures that the minimum exists.

**Lemma 1 (gap propagation and activation bound).** Let \(m\) be
nonsemiperfect and let \(p\nmid m\) be prime. Then
\[
 g(mp)\geq p\,g(m)-\sigma(m).                                      \tag{2}
\]
If \(mp\) is semiperfect, then
\[
 p\,g(m)\leq\sigma(m),\quad\text{equivalently}\quad p\leq R(m).     \tag{3}
\]

**Proof.** Every subset sum \(W\) of proper divisors of \(mp\) has a unique
layer decomposition
\[
 W=pU+V,
\]
where \(U\) is a subset sum of the proper divisors of \(m\), and \(V\) is a
subset sum of all divisors of \(m\). If \(W<mp\), then \(U<m\), and hence
\[
 mp-W=p(m-U)-V\geq p\,g(m)-\sigma(m),
\]
proving (2). If \(W=mp\), then \(U=m\) would be a semiperfect witness for
\(m\), so again \(U<m\). Thus
\[
 p(m-U)=V\leq\sigma(m),
\]
and (3) follows. \(\square\)

Consequently, if \(p>R(m)\), then \(mp\) is automatically nonsemiperfect and
\[
 R(mp)\leq
 \frac{\sigma(m)(p+1)}{p\,g(m)-\sigma(m)}
 =\frac{R(m)(p+1)}{p-R(m)}.                                        \tag{4}
\]
This is the subset-sum analogue of the exact deficiency-threshold recurrence
for primitive nondeficient integers.

The exact one-prime extension criterion is also worth recording. With the
notation in the proof, \(mp\) is semiperfect if and only if there is a
subset-sum gap \(h=m-U>0\) for which \(ph\) is a subset sum of all divisors
of \(m\). Thus (3) is only a necessary size condition; failure despite (3)
is a genuine subset-sum obstruction.

## Three summable largest-prime regimes

We use the standard Mertens upper bound
\[
 \prod_{r\leq y}(1-r^{-1})^{-1}\ll\log(2y),                         \tag{5}
\]
Chebyshev's prime bound, and the Brun--Titchmarsh interval upper bound.
The following harmonic consequences, proved in the companion largest-prime
primitive-nondeficient draft, will be used:
\[
 \sum_{v>1}\frac1{v\log^2(2P(v))}<\infty,\qquad
 \sum_{v>1}\frac1{v\sqrt{P(v)}}<\infty,\qquad
 \sum_{v>1}\frac{1+\log v}{vP(v)}<\infty.                           \tag{6}
\]

Let \(n\in A\), let \(p=P(n)\), and put \(a=v_p(n)\).

### 1. The largest prime has exponent at least two

The reciprocal sum of all integers in this regime is finite:
\[
 \sum_p\sum_{a\geq2}\frac1{p^a}\sum_{P(m)<p}\frac1m
 \ll\sum_p\frac{\log(2p)}{p^2}<\infty.                             \tag{7}
\]

### 2. The second-largest prime has exponent at least two

It remains to take \(a=1\), so \(n=mp\) and \(P(m)<p\). The proper divisor
\(m\) is nonsemiperfect. Lemma 1 gives
\[
 p\leq R(m)\leq\sigma(m)\leq m(1+\log m),                           \tag{8}
\]
where the last inequality follows from
\(\sigma(m)/m=\sum_{d\mid m}1/d\leq\sum_{j\leq m}1/j\).

Let \(q=P(m)\), write \(m=uq^b\), and suppose \(b\geq2\). Overcounting all
possibilities and using the ordinary harmonic bound for \(p\), the reciprocal
mass is at most a constant times
\[
 \sum_q\sum_{b\geq2}\frac1{q^b}
 \sum_{P(u)<q}\frac{1+\log u+b\log q}{u}.                           \tag{9}
\]
By (5) and logarithmic differentiation of its finite Euler product,
\[
 \sum_{P(u)<q}\frac1u\ll\log(2q),\qquad
 \sum_{P(u)<q}\frac{\log u}{u}\ll\log^2(2q).
\]
Thus (9) is
\[
 \ll\sum_q\frac{\log^2(2q)}{q^2}<\infty.                            \tag{10}
\]

### 3. The penultimate prime is inert for size reasons

Only
\[
 n=uqp,\qquad P(u)<q<p                                             \tag{11}
\]
remains. All of \(u,uq,up\) are nonsemiperfect because they are proper
divisors of \(n\). Put \(t=R(u)\). Suppose first that
\[
 q>t.                                                              \tag{12}
\]
By (4) and the semiperfectness of \(uqp\),
\[
 q<p\leq R(uq)\leq\frac{t(q+1)}{q-t}.                              \tag{13}
\]
In particular,
\[
 q<t+\sqrt{t^2+t}<2t+\tfrac12.                                    \tag{14}
\]

For completeness, the standard two-prime kernel estimate is
\[
 \sum_{\substack{q,p\ {\rm prime}\\
                  q>t+1,\ q<p\leq t(q+1)/(q-t)}}\frac1{qp}
 \ll\frac1{\log^2 t}+\frac1{\sqrt t}\qquad(t\geq4).                 \tag{15}
\]
To prove it, put \(h=q-t\). For \(1<h\leq\sqrt t\), use the trivial
\(O(\sqrt t)\) count for \(q\) and Chebyshev on the inner prime reciprocal
sum, obtaining \(O(t^{-1/2})\). For dyadic \(d<h\leq2d\) with
\(d\geq\sqrt t\), Brun--Titchmarsh gives \(O(d/\log d)\) primes \(q\), and
Chebyshev gives
\[
 \sum_{q<p\leq t(q+1)/(q-t)}\frac1p
 \ll\frac{1+\log^+(t/d)}{\log t}.
\]
The shell contribution is
\[
 \ll\frac1{\log^2t}\frac dt(1+\log^+(t/d)),
\]
whose dyadic sum is bounded.

The interval \(t<q\leq t+1\) contains at most one integer. Writing
\(t=\sigma(u)/g(u)\), its positive integer denominator obeys
\[
 qg(u)-\sigma(u)\geq1.
\]
Equations (2) and (4), together with
\(\sigma(u)\leq u(1+\log u)\), show that this exceptional \(q\) contributes
\[
 \ll\frac{1+\log u}{t}                                             \tag{16}
\]
to the \(q,p\) kernel.

If the inner kernel is nonempty, (14) and \(q>P(u)\) imply
\(t>(P(u)-1/2)/2\). Summing (15)--(16) over \(u\), with the exterior factor
\(1/u\), is therefore bounded by the three convergent series in (6).
Bounded prime supports are handled by their convergent Euler products and
logarithmic moments. Hence the subfamily (12) has convergent reciprocal sum.

## Exact remaining regime

Combining (7), (10), and the preceding kernel estimate proves:

**Theorem 2 (global largest-prime reduction).** The reciprocal sum over all
\(n\in A\) converges outside the subfamily having a factorization
\[
 n=uqp,\qquad P(u)<q<p,\qquad q\,g(u)\leq\sigma(u),                 \tag{17}
\]
where \(p,q\) occur to the first power and all three proper divisors
\[
 u,\qquad uq,\qquad up                                             \tag{18}
\]
are nonsemiperfect.

Because \(uq\) is nonsemiperfect despite the necessary size inequality in
(17), its obstruction is now purely combinatorial: for every subset sum
\(U<u\) of \(D^*(u)\), the number \(q(u-U)\) fails to be a subset sum of
the full divisor set of \(u\). The current largest-prime method has no
uniform estimate for the reciprocal mass of these small-but-inactive primes
\(q\). Controlling this precise regime, rather than the large primes or high
exponents, is the remaining bottleneck.
