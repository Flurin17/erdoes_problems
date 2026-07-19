# Erdős Problem #415: solution under the strict every-pattern normalization

## Conventions and results

Throughout, $k,n$ are positive integers and $m$ is a nonnegative integer.
All logarithms are natural and $\log_j$ denotes the $j$-fold iterated
logarithm; every asymptotic formula is asserted only where its iterates are
defined.  A permutation $\sigma\in S_k$ occurs at $m$ when
\[
\phi(m+\sigma(1))<\cdots<\phi(m+\sigma(k));
\]
a tied block realizes no strict permutation.  The permutation lists positions
from the smallest totient to the largest.  Define
\[
 M(\sigma)=\min\{m+k:m\ge0\text{ and $\sigma$ occurs at }m\},
 \qquad M_k=\max_{\sigma\in S_k}M(\sigma),
\]
with value $+\infty$ if a required occurrence does not exist.  Under the
nontrivial **every-pattern** normalization of the source wording,
\[
 F(n)=\max\{k\ge1:M_k\le n\}.
\]
Equivalently, $F(n)\ge k$ means
\[
 \forall\sigma\in S_k\ \exists m=m(\sigma)\ge0:\quad m+k\le n
 \quad\hbox{and}\quad
 \phi(m+\sigma(1))<\cdots<\phi(m+\sigma(k)). \tag{0}
\]
Thus the witness may depend on the pattern.  This is an explicit
normalization of the ambiguous word “any”; the literal existential and
common-witness readings are different problems.  Requiring $m\ge1$ changes
only the $k=1$ boundary, since the $m=0$ block is tied for every $k\ge2$.

Put
\[
\mu=\sum_p\frac1p\log\frac p{p-1}.
\]
Then, as $k\to\infty$,
\[
\boxed{\log_3M_k
=k\bigl(\log_3k+\gamma-\mu\bigr)+o(k)}. \tag{1}
\]
Consequently, as $n\to\infty$,
\[
\boxed{F(n)
=\frac{\log_3n}{\log_6n+\gamma-\mu+o(1)}
\sim\frac{\log_3n}{\log_6n}}. \tag{2}
\]
In particular $F(n)=o(\log_3n)$.  Read literally, the first source question
therefore has the answer **yes with $c=0$**.  No positive constant $c$
satisfies the proposed scale; (2) is the nondegenerate sharp answer.

The two subsidiary conclusions are:

1. the decreasing pattern is **not** always last: already
   \[
   M((4,3,2,1))=826<M((3,2,1,4))=827;
   \]
2. the cited natural order is undefined as a strict pattern because
   $\phi(1)=\phi(2)$; under limiting natural density, its stable-index
   refinement and the aggregate of its two linear refinements both fail to
   maximize frequency at $k=3$.  This does not purport to settle every
   possible tie rule or probability model.

## Standard inputs

The proof uses the following standard theorems in their stated forms:

- prime number theorem: $\vartheta(x)=\sum_{p\le x}\log p=x+o(x)$;
- Mertens product theorem:
  \[
  \sum_{p\le x}\log\frac p{p-1}=\log\log x+\gamma+o(1);
  \]
- Chinese remainder theorem;
- divergence of $\sum_p1/p$ (qualitative packing also follows from Mertens);
- for the frequency theorem only, Sperner's theorem and the second
  Borel--Cantelli lemma for independent events.

No prime-tuples conjecture, independence heuristic, or external solution is
used.

## Part I. Arithmetic preliminaries

Set
\[
w_p=\log\frac p{p-1},\qquad
h(t)=\log\frac t{\phi(t)}=\sum_{p\mid t}w_p,
\qquad H(x)=\max_{t\le x}h(t).
\]
The series defining $\mu$ converges since $w_p/p=O(p^{-2})$.

### Lemma 1 (maximal loss)

If $P_r=p_1\cdots p_r\le x<P_{r+1}$, then
\[
H(x)=h(P_r)=\log_3x+\gamma+o(1). \tag{3}
\]

**Proof.**  If $t\le x$ has distinct prime divisors
$q_1<\cdots<q_s$, then $q_j\ge p_j$ and
$P_s\le\operatorname{rad}(t)\le t\le x$, so $s\le r$.  Since $w_p$
decreases with $p$,
\[
h(t)=\sum_{j\le s}w_{q_j}\le\sum_{j\le r}w_{p_j}=h(P_r).
\]
PNT gives $p_r\sim\log x$, and Mertens gives (3). $\square$

### Lemma 2 (mean baseline loss)

As $k\to\infty$,
\[
\sum_{i\le k}h(i)=\mu k+o(k). \tag{4}
\]

**Proof.**  Reverse the order of summation:
\[
\sum_{i\le k}h(i)
=\sum_{p\le k}w_p\left\lfloor\frac{k}{p}\right\rfloor.
\]
The floor errors total $O(\sum_{p\le k}w_p)=O(\log_2k)=o(k)$,
and the truncated convergent series $\sum w_p/p$ tends to $\mu$. $\square$

## Part II. Uniform construction of every pattern

Fix $\sigma\in S_k$.  Put $K=k^4$, $\delta=8/K$, and let $r_i$ be defined
by $\sigma(r_i)=i$.  Prescribe target losses
\[
T_i=H(k)+(k-r_i)\delta,
\qquad x_i=T_i-h(i)\ge0. \tag{5}
\]
Write $A(t)=\sum_{p\le t}w_p$.

Read the primes $p>K$ in increasing order.  For each $i$, take consecutive
unused primes until their total $w_p$-weight first reaches $x_i$; call this
set $P_i$.  Because $w_p<1/(K-1)$,
\[
x_i\le\sum_{p\in P_i}w_p<x_i+\frac1{K-1}. \tag{6}
\]
The sets are disjoint.  Their total weight $W$ is, by (3)--(5),
\[
\begin{aligned}
W
&=kH(k)-\sum_{i\le k}h(i)
  +\frac{\delta k(k-1)}2+o(1)\\
&=k(\log_3k+\gamma-\mu)+o(k). \tag{7}
\end{aligned}
\]

Let $y$ be the last allocated prime.  Every prime in $(K,y]$ was used by the
sequential packing, so Mertens gives
\[
W=A(y)-A(K)=\log_2y-\log_2K+o(1).
\]
Since $W\sim k\log_3k$, this implies $\log y\gg K$ and in particular
$1/\log y<\delta/8$ for all sufficiently large $k$.  Include every prime
through this (prime, hence integral) cutoff $y$ in one CRT modulus
\[
Q=\prod_{p\le y}p.
\]
For $p\in P_i$, impose $m\equiv-i\pmod p$.  For every other $p\le y$,
impose $m\equiv0\pmod p$.  Choose the CRT representative with
$Q\le m<2Q$.

Every assigned prime exceeds $k$, so it divides exactly its designated shift.
For $p\le k$, the condition $m\equiv0$ makes $p\mid m+i$ exactly when
$p\mid i$; every unassigned $k<p\le y$ misses the entire block.  Thus the
controlled loss $C_i$ satisfies
\[
T_i\le C_i<T_i+\frac1{K-1}. \tag{8}
\]

Every uncontrolled prime divisor of $m+i$ exceeds $y$.  Since $m+i<3Q$, its
total extra loss $E_i$ is bounded by
\[
0\le E_i
\le\frac{\log(3Q)}{(y-1)\log(y+1)}
=O(1/\log y)<\delta/4. \tag{9}
\]
Also
\[
\left|\log\frac{m+i}{m+j}\right|<k/Q<\delta/4. \tag{10}
\]
Equations (8)--(10) show, for adjacent ranks, that
\[
h(m+\sigma(r))-h(m+\sigma(r+1))
>\log\frac{m+\sigma(r)}{m+\sigma(r+1)}.
\]
This is exactly
\[
\phi(m+\sigma(r))<\phi(m+\sigma(r+1)),
\]
so the required strict pattern occurs.

The displayed Mertens identity also gives
$\log_2y=W+\log_2K+o(1)=W+o(k)$.  PNT gives
$\log Q=(1+o(1))y$, hence
\[
\log_3(m+k)\le\log_2y+o(1)
=k(\log_3k+\gamma-\mu)+o(k). \tag{11}
\]
This estimate is uniform in $\sigma$, proving the upper bound in (1).

## Part III. Universal obstruction from the decreasing pattern

Suppose
\[
\phi(m+1)>\phi(m+2)>\cdots>\phi(m+k),\qquad m+k\le n. \tag{12}
\]
Then $h(m+i)$ is strictly increasing, because for $i<j$,
\[
h(m+j)-h(m+i)
=\log\frac{m+j}{m+i}+\log\frac{\phi(m+i)}{\phi(m+j)}>0. \tag{13}
\]

Let $P_r\le k<P_{r+1}$ and $R=P_{r-1}$.  Among the first $R$ shifts one
is divisible by $R$, say $R\mid m+j$ with $j\le R$, so
$h(m+j)\ge h(R)$.  Moreover $p_r\sim\log k$,
$R\le k/p_r$, and hence $R\log_3k=o(k)$.  Since
\[
h(R)=\log_3k+\gamma+o(1),
\]
monotonicity (13) yields
\[
\sum_{i=1}^kh(m+i)
\ge k(\log_3k+\gamma)+o(k). \tag{14}
\]

A prime $p\le k$ divides at most $k/p+1$ terms of the block.  Its aggregate
contribution to (14), summed over all such primes, is at most
\[
k\sum_{p\le k}\frac{w_p}{p}+\sum_{p\le k}w_p
=\mu k+o(k). \tag{15}
\]
Therefore primes $p>k$ occurring in the block have total weight
\[
S\ge k(\log_3k+\gamma-\mu)+o(k). \tag{16}
\]

Each $p>k$ divides at most one shift.  Let $D$ be their squarefree product.
Then
\[
h(D)=S,\qquad D\mid\prod_{i=1}^k(m+i)\le n^k. \tag{17}
\]
By Lemma 1 applied at $n^k$,
\[
S=h(D)\le H(n^k)=\log_3(n^k)+\gamma+o(1). \tag{18}
\]
The lower bound (16) itself makes $\log_2n$ dominate $\log k$, so
$\log_3(n^k)=\log_3n+o(1)$.  Equations (16)--(18) give the lower bound in
(1).  This obstruction applies to every possible construction.

## Part IV. Inversion

Let $L=\log_3n$ and $a=\gamma-\mu$.  Strict threshold heredity gives
\[
M_{F(n)}\le n<M_{F(n)+1}.
\]
Using (1) on both sides and the slow variation
$\log_3(L/(\log_3L+a))=\log_3L+o(1)$ gives first
\[
\frac{L}{F(n)}=\log_3F(n)+a+o(1).
\]
This relation implies $F(n)=L/(\log_3L+O(1))$ and therefore
$\log_3F(n)=\log_3L+o(1)$.  Substitution yields
\[
F(n)=\frac{L}{\log_3L+a+o(1)}.
\]
Since $\log_3L=\log_6n$, this is (2).

## Part V. The decreasing pattern is not always last

The deterministic finite certificate in
`computational/verify_k4_counterexample.py` evaluates every endpoint through
$827$ by trial-division totients and independently checks those values by gcd
counting.  It proves
\[
\begin{aligned}
&\phi(823),\ldots,\phi(826)=(822,408,400,348),\\
&\phi(824),\ldots,\phi(827)=(408,400,348,826),
\end{aligned}
\]
and exhaustively verifies that these are the first endpoints of patterns
$(4,3,2,1)$ and $(3,2,1,4)$ respectively.  Thus
\[
M((4,3,2,1))=826<827=M((3,2,1,4)),
\]
disproving finite decreasing extremality.  The main proof nevertheless shows
that decreasing is asymptotically extremal through the $o(k)$ remainder in
(1).

## Part VI. Frequencies and the natural order

For fixed $k$, take independent uniform residues $U_p\pmod p$ and set
\[
X_i=\sum_pw_p\mathbf1_{\{U_p\equiv-i\pmod p\}}.
\]
The series converges almost surely and in $L^1$ because
$\sum_pw_p/p<\infty$.  Finite-prime truncations are periodic over the integers,
and both their arithmetic and random tails have mean tending to zero.  Hence
the empirical loss vectors converge weakly to $(X_1,\ldots,X_k)$.

For $i\ne j$, all but finitely many prime contributions to $X_i-X_j$ are
$0,\pm w_p$, with the two signs equally likely conditional on activity.
Infinitely many primes are active almost surely.  Conditional on the first
$r$ active primes, equal signed sums form an antichain, so Sperner's theorem
bounds every atom by $O(r^{-1/2})$.  Thus pair differences are atomless and
strict chambers are continuity sets.  Every chamber also has positive Haar
mass: fix the residues of the finitely many primes $p\le k$, then use disjoint
private primes $p>k$ (their total $w_p$-weight diverges) to top up the
coordinates to the requested order with fixed positive gaps, and avoid all
other primes through a finite cutoff.  This cylinder has positive measure.
Choose the cutoff so the expected total remaining tail is smaller than one
quarter of the minimum gap; Markov's inequality leaves a positive-measure
subset on which the tail preserves the chamber.  It follows that every pattern
has the positive natural density
\[
d_k(\sigma)=
\Pr(X_{\sigma(1)}>\cdots>X_{\sigma(k)}). \tag{19}
\]
The factor $(m+i)/m\to1$ transfers (19) from normalized to raw totients.

For $k=3$, remove the prime $2$ and denote the resulting exchangeable vector
by $Y$.  Put
\[
q=\Pr(\max_iY_i-\min_iY_i>\log2).
\]
A direct count of the six labelings and two parity states gives
\[
d_3(123)=d_3(321)=q/6,
\]
and
\[
d_3(132)=d_3(213)=d_3(231)=d_3(312)=1/4-q/12.
\]
Finite prime cylinders with tail control prove $0<q<1$.

The reference values $(1,1,2)$ do not define a strict natural pattern.  Stable
tie-breaking selects $123$, which is strictly less frequent than $213$.
Aggregating both refinements, the natural weak order
$\{1,2\}\prec\{3\}$ has density $1/4+q/12$, while the same-shape competitor
$\{1,3\}\prec\{2\}$ has density $1/2-q/6$, larger by $(1-q)/4$.
Thus the natural-order assertion is false under both canonical repairs.

## Dependency status

- Parts I--IV are a complete proof of the corrected sharp asymptotic.
- Part V is a reproducible exhaustive finite certificate with two independent
  totient implementations.
- Part VI is a complete fixed-$k$ density theorem and counterexample; it is
  independent of Parts I--IV.
