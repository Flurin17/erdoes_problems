# Largest-prime decomposition for primitive nondeficient numbers

This route proves a complete auxiliary theorem: the reciprocals of the
primitive nondeficient integers have finite sum. This does **not** settle
Problem 469, since a divisibility-minimal semiperfect integer can have an
abundant but nonsemiperfect proper divisor (the notes record \(70\mid350\)).
It isolates the remaining difficulty to semiperfect activation above
primitive weird cores.

## Definitions and standard analytic inputs

Call \(n\) primitive nondeficient if
\[
 \sigma(n)\geq 2n,
 \qquad \sigma(d)<2d\quad(d\mid n,\ d<n).
\]
For a deficient integer \(v\), put
\[
 D(v)=2v-\sigma(v)>0,
 \qquad T(v)=\frac{\sigma(v)}{D(v)}.
\]

We use the following standard upper-bound forms of Mertens' theorem,
Chebyshev's theorem, and the Brun--Titchmarsh interval sieve:
\[
 \prod_{r\leq y}\left(1-\frac1r\right)^{-1}\ll\log(2y),             \tag{1}
\]
where products indexed by \(r\) are over primes,
\[
 \sum_{x<r\leq Rx}\frac1r\ll\frac{1+\log R}{\log x}
 \quad(x\geq3,R\geq1),                                             \tag{2}
\]
and
\[
 \#\{r\text{ prime}:x<r\leq x+y\}\ll \frac{y}{\log y}
 \quad(2\leq y\leq x).                                             \tag{3}
\]
In (2), splitting into dyadic intervals reduces the assertion to
Chebyshev's bound. Only upper bounds, with absolute constants, are used.

We will also use three immediate consequences. If \(P(v)\) is the largest
prime factor of \(v>1\), then
\[
 \sum_{v>1}\frac1{v\log^2(2P(v))}<\infty,\qquad
 \sum_{v>1}\frac1{v\sqrt{P(v)}}<\infty,\qquad
 \sum_{v>1}\frac{1+\log v}{vP(v)}<\infty.                           \tag{4}
\]
Indeed, grouping by \(r=P(v)\) gives
\[
 \sum_{P(v)=r}\frac1v
 =\frac1{r-1}\prod_{s<r}\left(1-\frac1s\right)^{-1}
 \ll\frac{\log(2r)}r.                                               \tag{5}
\]
This proves the second series in (4), and the first follows from
\(\sum_r1/(r\log r)<\infty\), itself a consequence of Chebyshev and partial
summation. Moreover, logarithmically differentiating the finite Euler
product gives
\[
 \sum_{P(w)<r}\frac{\log w}{w}
 =\prod_{s<r}(1-s^{-1})^{-1}
   \sum_{s<r}\frac{\log s}{s-1}
 \ll \log^2(2r).                                                     \tag{6}
\]
Writing \(v=r^aw\), \(a\geq1\), in (6) shows
\(\sum_{P(v)=r}(1+\log v)/v\ll\log^2(2r)/r\), proving the third
series in (4).

## Exact largest-prime crossing algebra

Let \(p\nmid m\), suppose \(m\) is deficient, and write
\(s=\sigma(m)\), \(D=2m-s\), and \(C=2m-Dp\). Direct expansion gives, for
every \(a\geq0\),
\[
 (p-1)\{\sigma(mp^a)-2mp^a\}=p^aC-s.                               \tag{7}
\]
Consequently, if \(mp^a\) is nondeficient while \(mp^{a-1}\) is deficient,
then
\[
 p^{a-1}C<s\leq p^aC.                                               \tag{8}
\]
In particular \(C>0\), and \(a\) is the unique exponent at which this fixed
pair \((m,p)\) crosses the nondeficiency threshold. In the case \(a=1\),
\[
 pC-s=(p-1)(s-pD),
\]
so the exact criterion is
\[
 mp\text{ is nondeficient}\quad\Longleftrightarrow\quad
 p\leq T(m)=\frac{s}{D}.                                            \tag{9}
\]
The equality endpoint in (9) is allowed. Notice also that
\(T(m)\leq s<2m\).

## The easy exponent cases

Let \(p=P(n)\), \(a=v_p(n)\), and \(n=mp^a\). The reciprocal sum of **all**
integers for which \(a\geq2\) is finite:
\[
 \sum_p\sum_{a\geq2}\frac1{p^a}
       \sum_{P(m)<p}\frac1m
 \ll\sum_p\frac{\log(2p)}{p^2}<\infty.                             \tag{10}
\]
Thus only \(a=1\) remains.

Now assume \(n\) is primitive nondeficient and \(n=mp\), where
\(p=P(n)>P(m)=q\). The proper divisor \(m\) is deficient, and (9) gives
\(p<2m\). Write \(m=uq^b\), with \(P(u)<q\). If \(b\geq2\), overcounting
all possible \(u,b,p\) gives reciprocal mass at most
\[
 \sum_q\sum_{b\geq2}\frac1{q^b}
 \sum_{P(u)<q}\frac1u
 \sum_{q<p<2uq^b}\frac1p.                                         \tag{11}
\]
The innermost sum is at most \(1+\log(2uq^b)\). By (1) and (6), the
contribution for fixed \(q,b\) is
\[
 \ll q^{-b}\{\log^2(2q)+b\log^2(2q)\}.
\]
Summing \(b\geq2\), then \(q\), proves convergence of (11). Hence the only
hard-looking case has
\[
 n=uqp,\qquad P(u)<q<p,                                              \tag{12}
\]
with both top primes occurring to the first power.

## Two-prime threshold kernel

The proper divisor \(u\) is deficient. Put
\(\delta=D(u)\), \(t=T(u)=\sigma(u)/\delta\). Exact calculation gives
\[
 D(uq)=\delta(q-t),
 \qquad
 T(uq)=\frac{t(q+1)}{q-t}.                                          \tag{13}
\]
Since \(uq\) is a proper divisor of the primitive nondeficient number \(n\),
it is deficient, so \(q>t\). Since \(uqp\) is nondeficient, (9) and (13)
give
\[
 q<p\leq \frac{t(q+1)}{q-t}.                                       \tag{14}
\]
Nonemptiness of (14) forces
\[
 q^2-2tq-t<0,
 \qquad q<t+\sqrt{t^2+t}<2t+\tfrac12.                              \tag{15}
\]

We need the following uniform two-prime estimate.

**Lemma.** For \(t\geq4\),
\[
 \sum_{\substack{q,p\ {\rm prime}\\
                  q>t+1,\ q<p\leq t(q+1)/(q-t)}}\frac1{qp}
 \ll\frac1{\log^2 t}+\frac1{\sqrt t}.                             \tag{16}
\]

**Proof.** Put \(h=q-t>1\). By (15), \(q\asymp t\) and \(h\ll t\).
For \(1<h\leq\sqrt t\), there are at most \(O(\sqrt t)\) integer choices
for \(q\), and
\[
 \frac{t(q+1)}{q(q-t)}\ll\frac t h\ll t.
\]
Thus (2) makes the inner \(p\)-sum \(O(1)\), and this range contributes
\(O(t^{-1/2})\).

For \(h>\sqrt t\), split into dyadic intervals \(d<h\leq2d\), starting at
\(d=\sqrt t\). By (3), there are \(O(d/\log d)\) eligible primes \(q\).
For each of them, (2) gives
\[
 \sum_{q<p\leq t(q+1)/(q-t)}\frac1p
 \ll\frac{1+\log^+(t/d)}{\log t}.
\]
Since \(d\geq\sqrt t\), the contribution of this dyadic interval is
\[
 \ll \frac d t\,
       \frac{1+\log^+(t/d)}{\log^2 t}.
\]
The sum of \((d/t)(1+\log^+(t/d))\) over the relevant doubling values of
\(d\) is bounded. This proves (16). \(\square\)

There is a small rational-endpoint exception not covered by (16). The
interval \(t<q\leq t+1\) contains at most one integer. Since
\(t=\sigma(u)/D(u)\), its positive denominator satisfies
\[
 qD(u)-\sigma(u)\geq1.
\]
Therefore (13) gives
\[
 T(uq)=\frac{\sigma(u)(q+1)}{qD(u)-\sigma(u)}<2u(q+1).
\]
Using the ordinary harmonic sum for \(p\), the contribution of this one
possible \(q\) is
\[
 \ll\frac{1+\log u}{t}.                                             \tag{17}
\]

## Convergence theorem

**Theorem.** If \(\mathcal P\) is the set of primitive nondeficient
integers, then
\[
 \sum_{n\in\mathcal P}\frac1n<\infty.
\]

**Proof.** Equations (10) and (11) dispose of all cases except (12).
For (12), sum first over \(p,q\) for each fixed \(u\). If the inner sum is
nonempty, (15) and \(q>P(u)\) imply
\[
 t>\frac{P(u)-1/2}{2}.                                               \tag{18}
\]
The finitely many prime supports \(P(u)\leq7\) cause no problem: here all
possible \(u\) are supported on a fixed finite set of primes, while
\(q<4u+1\) and \(p<2uq=O(u^2)\). Thus the contribution is bounded by a
fixed multiple of
\(\sum_{P(u)\leq7}(1+\log u)^2/u<\infty\).
For the rest, (16)--(18) bound the total contribution by
\[
 \ll\sum_{u>1}\frac1u\left\{
    \frac1{\log^2(2P(u))}+\frac1{\sqrt{P(u)}}
    +\frac{1+\log u}{P(u)}\right\},
\]
which converges by (4). The case \(u=1\) gives only the finite endpoint
case \(n=6\). This completes the proof. \(\square\)

## Consequence and remaining bottleneck for Problem 469

Every nondeficient integer has a divisibility-minimal nondeficient divisor.
Thus, for \(n\in A\), either \(n\) itself is primitive nondeficient, or \(n\)
has a proper primitive nondeficient divisor \(w\). In the latter case \(w\)
cannot be semiperfect, by the defining minimality of \(n\); hence \(w\) is a
primitive abundant nonsemiperfect (primitive weird) core. The theorem above
proves convergence of the \(n=w\) primitive layer and of the reciprocal sum
of all possible cores \(w\).

The unresolved step is uniform control of the semiperfect activation trees
above those cores. A bound of the form
\[
 \sum_{\substack{n\in A\\w\mid n\text{ for a chosen minimal
 nondeficient core }w}}\frac1n\ll\frac1w
\]
with bounded overlap would finish Problem 469. The large-prime activation
bound \(p\leq\sigma(m)\) makes every individual extension step finite, but
does not yet bound the total weighted branching uniformly in \(w\).
