# Second wave on the uniform $Q$-thick bottleneck

## Status

The general problem remains open. This wave tested the sufficient estimate
\[
\sum_{n\in S}\frac{Q}{n\log(n/Q)}\le C_a,
\qquad
S\subset[aQ,\infty),\quad |kn-m|\ge Q,                 \tag{1}
\]
uniformly in finite $S$ and positive integers $Q$. No counterfamily to (1)
was found. Several stronger proof templates were refuted, while a finite
target-weight theorem and a quantitative rounding lemma were proved.

For $m<n$, writing $r=n\bmod m$, the exact grid condition is
\[
Q\le r\le m-Q.                                           \tag{2}
\]
Indeed, these are exactly the distances from $n$ to the two nearest integer
multiples of $m$. After division by $Q$, (2) is the original real condition.

## 1. Exact target-weight result through cutoff $10$

Let $f(x)=1/(x\log x)$.

**Theorem 1.** Every finite real admissible $A\subset[2,10]$ satisfies
\[
\sum_{x\in A}f(x)\le f(2)+f(3)+f(5)+f(7).               \tag{3}
\]
Equality holds only for $A=\{2,3,5,7\}$. Thus (3) holds simultaneously on
every $Q$-grid.

**Proof.** The empty case is immediate. Let $a=\min A$. For $y>a$, the
constraints involving $a$ place $y$ in a safe band
\[
I_k=[ka+1,(k+1)a-1],\qquad k\ge1.                       \tag{4}
\]

If $a=2$, every later point is an odd integer, so
$A\subset\{2,3,5,7,9\}$. Admissibility makes this integer set primitive.
The only divisibility relation among the odd labels is $3\mid9$, and
$f(3)>f(9)$. Hence the unique maximum is $\{2,3,5,7\}$.

Suppose $a=2+\delta$ with $0<\delta<1$. Every $I_k$ has length
$\delta<1$, so it contains at most one point. Map $a$ to $2$ and a point of
$I_k$ to $2k+1$. Since
\[
x\ge ka+1=2k+1+k\delta,
\]
this map can only increase $f$-weight. If two image labels satisfy
\[
2\ell+1=t(2k+1),
\]
then $t\ge3$ is odd and $\ell=tk+(t-1)/2$. Write
\[
x=2k+1+u\delta,\quad u\in[k,k+1],\qquad
y=2\ell+1+v\delta,\quad v\in[\ell,\ell+1].
\]
Then
\[
|tx-y|=\delta|tu-v|\le\frac{t+1}{2}\delta.              \tag{5}
\]
Every image label is at most $10$, so $t\le10/3$. If
$13\delta<6$, a divisibility relation between image labels would make the
right side of (5) less than $1$, contrary to admissibility. The image is
therefore primitive, and the $a=2$ case proves (3).

If instead $\delta\ge6/13$, then $a\ge32/13$ and
$\min I_4=4a+1>10$. Only $I_1,I_2,I_3$ can occur, at most once each, and
their lower endpoints give
\[
\sum_{x\in A}f(x)
\le f(a)+f(a+1)+f(2a+1)+f(3a+1)
\le f(2)+f(3)+f(5)+f(7).
\]

If $a=3$, the safe bands are $[3k+1,3k+2]$. Unit separation permits at
most their endpoint pair, so through $10$,
\[
\sum_{x\in A}f(x)
\le f(3)+f(4)+f(5)+f(7)+f(8)+f(10).
\]
Here
\[
f(4)=\frac14f(2),\qquad f(8)=\frac1{12}f(2),\qquad
f(10)<f(8),                                               \tag{6}
\]
and hence $f(4)+f(8)+f(10)<f(2)$.

If $3<a<4$, only $I_1,I_2$ meet $[2,10]$. Each has length below $2$, so
the lower-position vector is strictly beyond $\{3,4,5,7,8\}$. The result
follows from $f(4)+f(8)=f(2)/3<f(2)$.

Finally, if $a\ge4$, unit separation gives
\[
\sum_{x\in A}f(x)\le\sum_{j=4}^{10}f(j).
\]
Besides (6), one has
\[
f(6)<\frac12f(3),\qquad f(9)=\frac16f(3).
\]
Cancelling $f(5)+f(7)$ proves (3). Every $a>2$ case is strict, while the
$a=2$ case has the unique equality set already identified. $\square$

The theorem is finite evidence only; its proof does not give a uniform tail
bound.

## 2. Crystallization for arbitrary decreasing weights is false

Take $Q=2$ and
\[
A=\{7/2,5,6,8,9\}.
\]
Its numerators are $7,10,12,16,18$. Their pairwise remainders are
\[
3,5,2,4;\qquad 2,6,8;\qquad 4,6;\qquad 2,
\]
all satisfying (2), so $A$ is admissible.

For the strictly decreasing weight $g(x)=1/(x+5)$, the best primitive
integer subset of $[2,9]$ is
\[
R=\{4,5,6,7,9\}.
\]
To check this, the only primitive five-sets are $R$ and
$\{5,6,7,8,9\}$, and $R$ is heavier. Every primitive set of at most four
elements is coordinatewise no earlier than $P=\{2,3,5,7\}$, while
\[
g(R)-g(P)
=\frac19+\frac1{11}+\frac1{14}-\frac17-\frac18
=\frac{31}{5544}>0.
\]
Finally,
\[
g(A)-g(R)=\frac2{17}+\frac1{13}-\frac19-\frac1{12}
=\frac1{7956}>0.                                        \tag{7}
\]
Thus no compression theorem valid for every decreasing objective can prove
(1). This example is not a counterexample for $f$; the prime set has much
larger $f$-weight.

## 3. A logarithmic-loss primitive rounding theorem

**Proposition 2.** Let $X\ge2$ and let $A\subset[2,X]$ be finite and
admissible. There are $A'\subset A$ and an injective adjacent rounding
$r:A'\to\mathbb Z\cap[2,X+1]$ such that $r(A')$ is primitive and
\[
\sum_{x\in A'}f(x)
\ge\frac{\log2}{2\log(2(X+1))}\sum_{x\in A}f(x),         \tag{8}
\]
\[
\sum_{x\in A'}f(r(x))
\ge\frac{\log2}{6\log(2(X+1))}\sum_{x\in A}f(x).        \tag{9}
\]

**Proof.** Partition the integral points arbitrarily between two types. For a
nonintegral point, use one of the following representations:
\[
x=n+e,\quad n=\lfloor x\rfloor,\quad e\in[1/2,1)
\]
for the floor type, and
\[
x=n-e,\quad n=\lceil x\rceil,\quad e\in(1/2,1)
\]
for the ceiling type. Points whose fractional part is below $1/2$ are put in
the ceiling type; all others are put in the floor type. Set $r(x)=n$ and
\[
J_x=[e/n,(e+1)/n).                                      \tag{10}
\]
For an integral point $x=n$, instead set $r(x)=n$ and
\[
J_x=[L,1/n),\qquad L=\frac1{2(X+1)}.                    \tag{11}
\]
All these intervals lie in $D=[L,1]$ and have logarithmic measure at least
$\log2$.

Fix one type. Equal rounded labels cannot occur, because the corresponding
real points would be less than $1$ apart. Suppose two nonintegral rounded
labels satisfy $n'=kn$ with $k\ge2$. For either type, admissibility gives
$ke-e'\ge1$, and hence $J_{x'}$ lies wholly below $J_x$. If the smaller
label is nonintegral and the larger one integral, the same conclusion follows
from $ke\ge1$. If the smaller label is integral and the larger one
nonintegral, their gap at multiplier $k$ is $e'<1$, so the pair cannot occur.
Two divisible integral labels likewise cannot occur. Thus for every $t\in D$,
the labels belonging to points with $t\in J_x$ form a primitive set.

Choose the type of total $f$-weight at least half the weight of $A$. Tonelli
for this finite sum gives
\[
\int_D\sum_{\substack{x\text{ in the chosen type}\\t\in J_x}}
 f(x)\,\frac{dt}{t}
\ge \log2\sum_{x\text{ in the chosen type}}f(x).
\]
Since $D$ has logarithmic measure $\log(2(X+1))$, averaging produces a
$t$ and a subset $A'$ satisfying (8). For floor-rounded and integral points,
$f(r(x))\ge f(x)$. For a ceiling-rounded point,
$r(x)<x+1\le3x/2$ and $\log r(x)\le2\log x$, so
$f(r(x))\ge f(x)/3$. This proves (9). $\square$

The logarithmic loss in (8) prevents this proposition from proving (1).

## 4. Full endpoint rounding can fail

For every integer $a\ge5$, put
\[
m_0=a,\qquad m_1=a^2-1,\qquad m_2=m_1^2-1
\]
and
\[
A_a=\{m_0+1/2,m_1+1/2,m_2+1/2\}.                       \tag{12}
\]
This set is admissible. For an adjacent pair with lower integer part $m$ and
upper integer part $m^2-1$, doubling the two half-integers gives
$P=2m+1$ and $Q=2m^2-1$. The distances from $Q$ to its two nearest multiples
of $P$ are $m$ and $m+1$, so the undoubled gaps exceed $1$. For the
nonadjacent pair, with $P=2a+1$ and $Q=2m_2+1$, direct reduction gives
\[
8Q\equiv1\pmod P.
\]
Since $P\ge11$, this rules out $Q\equiv0,1,-1\pmod P$. Hence
$|kP-Q|\ge2$ for every integer $k$, which is exactly the required undoubled
gap. The reverse ordered orientation is automatic because the two points are
already more than $1$ apart.

Nevertheless, no selection of a floor or ceiling label for every point of
$A_a$ is primitive. For each adjacent pair,
\[
m_i\mid m_{i+1}+1,\qquad m_i+1\mid m_{i+1},
\]
so the two points must choose the same side. All three choices must therefore
agree. All-floor labeling fails because $m_0\mid m_2$, and all-ceiling
labeling fails because $m_0+1\mid m_2+1$.

Deleting the largest point resolves the obstruction and has weight
$\asymp1/(a^4\log a)$. Thus repetitions of this gadget at ordinary or
geometric parameter scales have summable cheapest deletion cost. The example
refutes full endpoint rounding, but not the bounded-weight deletion lemma
formulated below.

## 5. Exact limits of two local proof templates

### Static tubes

Let $F$ be a finite set of positive integer multipliers and fix a target $t$.
For a $Q$-admissible integer set $S$, consider those $n\in S$ for which
\[
|kn-t|<Q/2
\]
for some $k\in F$. After choosing one witness $k$ for each such $n$, the
witnesses form a divisibility antichain: if $k'=dk$, subtraction would give
$|n-dn'|<Q$, contradicting $Q$-admissibility. Hence the number of hits is at
most the divisibility width of $F$.

This is sharp. If $D\subset F$ is an antichain and $L$ is a common multiple
of $D$, then
\[
S=\{QL/k:k\in D\}
\]
is $Q$-admissible and all the corresponding tubes meet at $QL$. Indeed, a
forbidden equality between two elements would say that one member of $D$
divides another. Thus any static local estimate that uses only this single
target and these multiplier incidences cannot improve on divisibility width.

### Finitely many separated shells

**Lemma 3.** For every integer $R\ge1$, there are a primitive integer set
$P$ and arbitrarily widely separated intervals
\[
I_j=[M_j,(1+\varepsilon)M_j),\qquad
\varepsilon=\frac1{32R},\qquad 1\le j\le R,
\]
such that
\[
\sum_{n\in P\cap I_j}\frac1n\ge\frac{3}{256R}           \tag{13}
\]
for every $j$.

**Proof.** Choose the integer scales recursively, imposing any desired lower
bound on $M_{j+1}/M_j$. Let $U_j=I_j\cap\mathbb Z$, and retain from $U_j$
only integers not divisible by an integer retained in an earlier block. Take
$M_j$ large enough that the raw harmonic mass of $U_j$ is at least
$\varepsilon/2$, every earlier raw block has mass at most $2\varepsilon$,
and $N_{<j}/M_j\le\varepsilon/16$, where $N_{<j}$ is the number of earlier
retained integers. The union-bound deletion cost in block $j$ is at most
\[
\sum_{d\in P,\ d<M_j}
\left(\frac{\varepsilon}{d}+\frac1{M_j}\right)
\le\varepsilon(2R\varepsilon)+\frac{N_{<j}}{M_j}
\le\frac{\varepsilon}{8}.
\]
Thus the retained mass is at least $3\varepsilon/8$, which is (13). No two
integers in one narrow block divide one another, and the recursive deletion
prevents cross-block divisibility. $\square$

This lemma rules out a support-only obstruction saying that one of any fixed
number of sufficiently separated shells must have negligible mass. It does
not rule out every quantitative inequality involving finitely many shells.

## 6. Sharpened bottleneck

The uniform estimate (1) has survived the targeted counterexample search, but
the following stronger proof templates have failed:

1. domination by an integer optimizer for every decreasing weight;
2. unconditional primitive floor/ceiling rounding;
3. a static one-target tube estimate better than divisibility width;
4. a fixed-arity support obstruction on widely separated shells.

One precise sufficient repair of the rounding route is:

> For every finite admissible $A\subset[a,\infty)$, delete a subset of
> universally bounded total $f$-weight so that the remaining points admit
> adjacent integer labels forming a primitive set, with labels comparable in
> weight to their points.

The three-point gadgets in (12) show that such a result must charge entire
implication cycles, not just individual divisible endpoint pairs. Equivalently,
one could prove a carrier-conditioned multiscale Hall inequality that charges
common-center antichains by their actual $1/(x\log x)$ mass rather than their
cardinality. No such estimate is proved here, and no general solution is
claimed.
