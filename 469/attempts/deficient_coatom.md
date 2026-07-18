# Deficient largest-coatom route

## Outcome and exact scope

Write
\[
I(n)=\frac{\sigma(n)}n
\]
and let \(P(n)\) denote the largest prime factor of \(n>1\).  This
route proves the following statement, which is stronger than convergence
for primitive nondeficient integers.

**Theorem (deficient largest coatom).**  Let
\[
\mathcal C=
\left\{n>1:I(n)\ge 2\quad\hbox{and}\quad
 I\!\left(\frac n{P(n)}\right)<2\right\}.
\]
Then
\[
\sum_{n\in\mathcal C}\frac1n<\infty. \tag{1}
\]

Thus (1) includes every primitive nondeficient integer, because for such
an integer every proper divisor is deficient.  It also includes many
integers which are not primitive: only the coatom obtained by removing
one copy of the largest prime is assumed deficient.

For Problem 469, every semiperfect integer is nondeficient.  Therefore
(1) proves convergence of the subfamily for which \(n/P(n)\) is
deficient.  It does **not** settle the problem: minimal semiperfectness
only says that \(n/P(n)\) is nonsemiperfect.  It may be abundant and
nonsemiperfect (weird), and the argument below gives no control in that
case.

## Standard analytic inputs

The proof uses only the following standard upper bounds.

1. Chebyshev's estimate
   \[
   \pi(y)\ll \frac{y}{\log(2y)}.
   \]
2. The upper half of Mertens' product estimate
   \[
   \prod_{\ell<y}\left(1-\frac1\ell\right)^{-1}
   \ll \log(2y),                                      \tag{2}
   \]
   where products and sums indexed by \(\ell\) are over primes.
3. Brun--Titchmarsh in the elementary short-interval form
   \[
   \pi(Y+Z)-\pi(Y)\ll \frac{Z}{\log Z}
   \qquad(2\le Z\le Y).                              \tag{3}
   \]

Chebyshev's estimate and multiplicative dyadic decomposition give, for
\(3\le y<z\),
\[
R(y,z):=\sum_{y<\ell\le z}\frac1\ell
 \ll \frac1{\log y}+\log\!\left(\frac{\log z}{\log y}\right), \tag{4}
\]
and also \(\sum_{\ell\le z}1/\ell\ll\log\log(3z)\).
Only (3) is used for short intervals; (4) itself needs only Chebyshev.

## Deficiency coordinates

For a deficient integer \(m\), put
\[
D(m)=2m-\sigma(m)>0,
\qquad
X(m)=\frac{\sigma(m)}{D(m)}
     =\frac{I(m)}{2-I(m)}.                            \tag{5}
\]
We have \(X(m)\ge1\) and \(X(m)<2m\).  If \(q\nmid m\) is prime and
\(b\ge1\), write
\[
H_b(q)=1+\frac1q+\cdots+\frac1{q^b},
\qquad S_b(q)=H_b(q)-1.
\]
Whenever \(mq^b\) is deficient, multiplicativity gives
\[
X(mq^b)=\frac{H_b(q)}{1/X(m)-S_b(q)}.                 \tag{6}
\]

## Largest prime occurring at least twice

First sum over the larger unrestricted set of integers for which the
largest prime \(p\) occurs to exponent \(a\ge2\).  Writing
\(n=p^a r\), with \(P(r)<p\), (2) gives
\[
\begin{aligned}
\sum_p\sum_{a\ge2}\frac1{p^a}
   \sum_{P(r)<p}\frac1r
 &=\sum_p\frac1{p(p-1)}
   \prod_{\ell<p}\left(1-\frac1\ell\right)^{-1}  \\
 &\ll\sum_p\frac{\log(2p)}{p^2}<\infty.            \tag{7}
\end{aligned}
\]
No nondeficiency or coatom condition is needed in this case.

## Two-largest-prime reduction

It remains to consider \(n\in\mathcal C\) for which the largest prime
has exponent one.  Factor uniquely as
\[
n=pq^b m,
\qquad p>q>P(m),qquad b\ge1,                         \tag{8}
\]
with the convention \(m=1\) if \(q\) is the only prime below \(p\).
Set \(r=mq^b=n/p\).  The defining coatom condition says that \(r\) is
deficient; hence its divisor \(m\) is deficient as well.  Put
\(x=X(m)\).

Since \(r\) is deficient, (6) has positive denominator and
\[
S_b(q)<\frac1x.
\]
As \(S_b(q)>1/q\), this implies \(q>x\).  On the other hand,
\(n=pr\) is nondeficient exactly when
\[
p\le X(r).                                            \tag{9}
\]
In particular \(X(r)>q\).  Using (6),
\[
q\left(\frac1x-S_b(q)\right)<H_b(q),
\]
and hence
\[
\frac qx<1+(q+1)S_b(q)
 <1+\frac{q+1}{q-1}\le4.                             \tag{10}
\]
Thus every tuple in (8) satisfies
\[
x<q<4x,
\qquad P(m)<4x.                                       \tag{11}
\]
The constant 4 is deliberately inessential (a slightly sharper
calculation gives \(q<3x\)).

## The two-prime kernel

For fixed deficient \(m\), let \(K(m)\) be the sum
\[
K(m)=
\sum_{\substack{x<q<4x\\q\ \mathrm{prime}}}
\sum_{\substack{b\ge1\\mq^b\ \mathrm{deficient}\\X(mq^b)>q}}
\frac1{q^b}
\sum_{\substack{q<p\le X(mq^b)\\p\ \mathrm{prime}}}\frac1p . \tag{12}
\]
We claim
\[
K(m)\ll \frac1{\log^2(2x)}+\frac{\log(2m)}x.         \tag{13}
\]

### The case \(b=1\)

Here (6) is the exact identity
\[
U:=X(mq)=\frac{x(q+1)}{q-x}.                          \tag{14}
\]
The condition \(U>q\) implies
\[
q<x+\sqrt{x^2+x}<3x.                                 \tag{15}
\]
Put \(t=q-x>0\).

There is a small rational-gap case which must not be discarded.  If
\(0<t<1\), there is at most one integer \(q\).  Moreover
\[
D(mq)=qD(m)-\sigma(m)=D(m)(q-x)=D(m)t              \tag{16}
\]
is a positive integer.  Consequently \(t\ge1/D(m)\ge1/m\).
Equations (14), (15), and \(x<2m\) give \(U\ll m^3\).  Hence (4) and
its initial-segment consequence show that this possible \(q\) contributes
at most
\[
\frac1q R(q,U)\ll\frac{\log(2m)}x.                  \tag{17}
\]

Now suppose \(t\ge1\).  For \(1\le T\le2x\), place the primes \(q\)
with \(T<t\le2T\) in one dyadic gap band.  If \(T\ge\sqrt{x}\),
Brun--Titchmarsh gives \(O(T/\log(2x))\) such primes (the finitely many
small \(x\) are absorbed into the constant).  From (14),
\[
\frac Uq\ll\frac xT,
\]
so (4) gives
\[
R(q,U)\ll
\frac{1+\log^+(x/T)}{\log(2x)}.
\]
The contribution of this band is therefore
\[
\ll \frac{T}{x}\,
   \frac{1+\log^+(x/T)}{\log^2(2x)}.
\]
Its dyadic sum is \(O(\log^{-2}(2x))\).  For
\(1\le t<\sqrt{x}\), ignore primality: there are at most
\(\sqrt{x}+1\) possible integers \(q\), while (4) gives
\(R(q,U)\ll1\).  Their total is
\(O(x^{-1/2})=O(\log^{-2}(2x))\).  Together with (17), this proves
the \(b=1\) part of (13).

### The case \(b\ge2\)

The positive integer \(D(mq^b)\) is at least one, while \(mq^b\) is
deficient.  Therefore
\[
X(mq^b)=\frac{\sigma(mq^b)}{D(mq^b)}<2mq^b.          \tag{18}
\]
Using the initial-segment form of (4), and then summing the geometric
tail in \(b\),
\[
\sum_{b\ge2}\frac1{q^b}R\bigl(q,X(mq^b)\bigr)
 \ll\frac{1+\log m+\log q}{q^2}.                    \tag{19}
\]
Even summing (19) over all integers \(x<q<4x\) gives
\[
\ll\frac{1+\log m+\log(2x)}x
 \ll\frac{\log(2m)}x,                              \tag{20}
\]
because \(x<2m\).  This completes the proof of (13).

## Summing over the core

The case \(m=1\) is finite directly: (11) leaves only finitely many
choices of \(q\), and the sum over \(b\) is geometrically convergent.
Assume \(m>1\), and put \(Q=P(m)\).  By (11), \(Q<4x\); also
\(x<2m\).  Thus (13) implies, with finitely many small \(Q\) absorbed,
\[
\frac{K(m)}m
 \ll \frac1{m\log^2(2Q)}+\frac{\log(2m)}{mQ}.       \tag{21}
\]

Group the cores by their exact largest prime.  Mertens' bound (2) gives
\[
A_Q:=\sum_{P(m)=Q}\frac1m
 =\frac1{Q-1}\prod_{\ell<Q}\left(1-\frac1\ell\right)^{-1}
 \ll\frac{\log(2Q)}Q.                               \tag{22}
\]
The logarithmic derivative of the same Euler product gives
\[
\begin{aligned}
B_Q:=\sum_{P(m)=Q}\frac{\log(2m)}m
 &\ll A_Q\left(1+\frac{Q\log Q}{Q-1}
       +\sum_{\ell<Q}\frac{\log\ell}{\ell-1}\right) \\
 &\ll\frac{\log^2(2Q)}Q,                            \tag{23}
\end{aligned}
\]
where the last estimate follows from Chebyshev by dyadic blocks.
Equations (21)--(23) reduce the total to
\[
\sum_{Q\ \mathrm{prime}}\frac1{Q\log(2Q)}
+\sum_{Q\ \mathrm{prime}}\frac{\log^2(2Q)}{Q^2}.       \tag{24}
\]
The second sum converges even over all integers; the first converges by
Chebyshev's bound on each dyadic prime block.  This proves (1).

All endpoint directions used above are exact: the coatom is strictly
deficient, while \(n\) may be perfect, so the upper inequality
\(p\le X(r)\) is inclusive.  Thus perfect-number endpoints are included.

## Why strict deficiency and why weird coatoms remain

Strict coatom deficiency is genuinely necessary for this theorem.
For every prime \(p>3\),
\[
n=6p
\]
is abundant, while \(n/P(n)=6\) is perfect.  Hence allowing
\(I(n/P(n))\le2\) in place of strict deficiency would contain the
divergent family
\[
\sum_{p>3}\frac1{6p}=\infty.
\]

For the set in Problem 469, a perfect proper divisor cannot occur,
because every perfect integer is semiperfect (the sum of all its proper
divisors equals the integer).  Thus, after applying the theorem, the
unresolved largest-coatom case is precisely
\[
n\text{ minimal semiperfect},
\qquad n/P(n)\text{ abundant but nonsemiperfect}.     \tag{25}
\]
That is, the coatom in (25) is weird.  In this regime \(D(m)\le0\), so
the positive threshold coordinate \(X(m)=\sigma(m)/D(m)\), the stopping
interval (10), and the two-prime kernel all disappear.  Any completion
of Problem 469 must therefore use the subset-sum obstruction of weird
coatoms (or prove that their extensions have a separately summable
reciprocal mass); abundance inequalities alone do not close the gap.
