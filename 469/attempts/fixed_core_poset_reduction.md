# Fixed-core poset reduction and bounded-support convergence

For fixed nonsemiperfect \(b\), define
\[
C_b=\{c:bc\text{ is semiperfect and }bd\text{ is not for every }d\mid c,\ d<c\}.
\]
No coprimality is assumed. Write \(I(n)=\sigma(n)/n\).

## Exact poset reduction

Let \(\mathcal A\) be the global set of divisibility-minimal semiperfect
integers and put \(q_b(x)=x/\gcd(x,b)\). Semiperfectness lifts to multiples,
every semiperfect integer has a minimal semiperfect divisor, and
\(a\mid bc\iff q_b(a)\mid c\). Therefore
\[
\{c:bc\text{ is semiperfect}\}=\bigcup_{a\in\mathcal A}q_b(a)\mathbb N,
\qquad C_b=\min_{\mid}\{q_b(a):a\in\mathcal A\}. \tag{1}
\]
In particular, testing the coatoms \(bc/p\), \(p\mid c\), suffices, and
\(C_b\) is a divisibility antichain.

If \(c\in C_b\) and a semiperfect \(m\mid bc\), then \(q_b(m)=c\): the
left side divides \(c\), while \(bq_b(m)\) is a semiperfect multiple of \(m\),
so minimality forces equality. With
\[
b_\parallel=\prod_{p\mid c}p^{v_p(b)},\qquad b_\perp=b/b_\parallel,
\]
every such \(m\) has the form \(cb_\parallel h\), \(h\mid b_\perp\).
Choosing canonically a minimal semiperfect divisor of \(bc\) gives an
injection
\[
\Phi_b:C_b\hookrightarrow\mathcal A,
\qquad \Phi_b(c)=c g(c),\quad g(c)\mid b. \tag{2}
\]
Since \(\Phi_b(c)\le bc\), divergence of one fixed fiber would imply
divergence of the original reciprocal series.

## Overflow gap

For nonsemiperfect \(B\), define
\[
g(B)=\min\{B-S:S<B,\ S\text{ a distinct proper-divisor subset sum}\}\ge1.
\]

**Lemma.** If \(Be\) is semiperfect, then
\[
e g(B)\le\sigma(B)(\sigma(e)-e),\qquad
I(e)-1\ge\frac{g(B)}{\sigma(B)}\ge\frac1{\sigma(B)}. \tag{3}
\]

For a selected divisor \(x\mid Be\), define
\[
f_B(x)=\prod_p p^{\max(v_p(x)-v_p(B),0)},\qquad y_B(x)=x/f_B(x).
\]
Then \(f_B(x)\mid e\), \(y_B(x)\mid B\), and fixed-overflow fibers have
distinct residuals. Grouping a witness gives \(Be=\sum_{f\mid e}fS_f\),
with each \(S_f\) a distinct divisor-subset sum of \(B\). Positivity gives
\(S_e\le B\); the top \(S_e\) uses proper divisors and cannot equal \(B\).
Hence
\[
e g(B)\le e(B-S_e)=\sum_{f<e}fS_f
\le\sigma(B)(\sigma(e)-e),
\]
proving (3), including when \((B,e)>1\).

For every factorization \(c=ae\), \(e>1\), of \(c\in C_b\), the integer
\(B=ba\) is nonsemiperfect. Thus
\[
I(e)-1\ge\frac{g(ba)}{\sigma(ba)}\ge\frac1{\sigma(ba)}. \tag{4}
\]
In particular \(I(c)\ge1+1/\sigma(b)\).

## Fixed-\(\omega\) convergence

Put
\[
F_k(B)=\sum_{c\in C_B,\ \omega(c)\le k}\frac1c.
\]
For every fixed \(k\),
\[
F_k(B)\ll_k(1+\log\sigma(B))^k<\infty. \tag{5}
\]

Proof is by induction. Let \(S=\sigma(B)\). If \(r=P^-(c)\), (3) gives
\[
1+S^{-1}\le I(c)<\prod_{p\mid c}\frac p{p-1}
\le(1-1/r)^{-k},
\]
so
\[
r\le[1-(1+1/S)^{-1/k}]^{-1}\le4kS. \tag{6}
\]
Write \(c=r^a u\), \((r,u)=1\). If \(u>1\), then \(Br^a\) is
nonsemiperfect and \(u\in C_{Br^a}\), with \(\omega(u)\le k-1\). Therefore
\[
F_k(B)\le\sum_{\substack{2\le r\le4kS\\ r\ {m prime}}}\sum_{a\ge1}
\frac{1+F_{k-1}(Br^a)}{r^a}. \tag{7}
\]
Now \(\sigma(Br^a)\le2Sr^a\), and for \(L=1+\log(2S)\),
\[
\sum_{a\ge1}\frac{(L+a\log r)^{k-1}}{r^a}
\ll_k\frac{(L+\log r)^{k-1}}{r-1}. \tag{8}
\]
Substitution of the inductive hypothesis and (8) into (7), followed by
enlarging the remaining prime sum to the integer harmonic sum up to \(4kS\),
proves (5). Consequently any divergent
fixed fiber must have unbounded \(\omega(c)\).

## Exact witness condition

Writing a witness in reciprocal form,
\[
1=\sum_{q\in Q}\frac1q,\qquad q\mid bc,\quad q>1,
\]
fiber minimality is equivalent to
\[
\operatorname{lcm}(b,Q)=bc\quad\text{for every witness }Q. \tag{9}
\]
Indeed, a smaller lcm is \(bd\) for a proper \(d\mid c\), and the same
identity witnesses \(bd\); conversely a witness for \(bd\) scales to \(bc\).
For each \(p\mid c\), (9) forces a denominator with full exponent
\(v_p(bc)\). Multiplying by \(bc\) and reducing modulo \(p\) shows there must
be at least two such denominators. Hence every witness satisfies
\[
c^2\mid\prod_{q\in Q}q. \tag{10}
\]

## Sharp prime-power carry bound

Suppose \(n=p^EU\), \((p,U)=1\), is semiperfect but \(n/p\) is not. Group a
witness by exact \(p\)-adic valuation:
\[
p^EU=\sum_{j=0}^Ep^jS_j.
\]
Successive reduction modulo \(p\) gives integer carries
\[
t_1=S_0/p,\qquad t_{j+1}=(t_j+S_j)/p,
\qquad S_E+t_E=U.
\]
One has \(S_0>0\), or division by \(p\) would witness \(n/p\). Thus all
carries are positive, and induction gives
\[
t_j<\frac{\sigma(U)}{p-1}.
\]
If \(t_i=t_j\) for \(i<j\), delete digit layers \(i,\ldots,j-1\) and shift
the later layers down. Equality of the entering carries splices the recurrence
and yields a witness for a divisor of \(n/p\), contradiction. The carries are
therefore distinct, so
\[
p\le\sigma(U),\qquad
E\le\left\lceil\frac{\sigma(U)}{p-1}\right\rceil-1. \tag{11}
\]
The ceiling-minus-one is needed when the ratio is integral. For \(c\in C_b\),
apply (11) to every \(p\mid c\), with \(E=v_p(bc)\), \(U=bc/p^E\).

## Remaining obstruction

The bounded-\(\omega\) estimate is not uniform in \(k\), and its constants
grow rapidly. Thus the unresolved part is uniform control of the
unbounded-prime-support tail. The injection (2) shows that a divergent fixed
fiber would already be a divergent subfamily of the original set.
