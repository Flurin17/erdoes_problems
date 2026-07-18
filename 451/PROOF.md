# Erdős Problem #451: strongest current result

## Status and dependencies

The sharp asymptotic remains open locally.  The following nonmatching bounds
are dependency-complete:
\[
 k^{,2\log 2-o(1)}\le n_k\le \exp((1+o(1))k).       \tag{1}
\]
The proof uses two standard results in the following forms:

1. the prime number theorem
   $\pi(2x)-\pi(x)=(1+o(1))x/\log x$;
2. the shifted Brun--Titchmarsh inequality
   $\pi(u+v)-\pi(u)\le 2v/\log v$ for $v>1$ (harmless
   endpoint rounding is absorbed below).

The lower bound in (1) means that for each fixed
$\beta<2\log 2$, one has $n_k>k^\beta$ for all sufficiently large $k$.

## Exact covering equivalence

For $p\in(k,2k)$, the product condition fails exactly when
\[
 n\in[mp+1,mp+k]                                      \tag{2}
\]
for some positive integer $m$.  Indeed, (2) is precisely the assertion that
$mp=n-i$ for an $i\in\{1,\ldots,k\}$.

We first record that
\[
 \frac{n_k}{k}\longrightarrow\infty.                 \tag{3}
\]
Let $p_1<\cdots<p_s$ be the primes in $(k,2k)$ and let $\Delta_k$ be the
largest internal or endpoint gap in the augmented list
$k,p_1,\ldots,p_s,2k$.  The PNT in fixed proportional intervals gives
$\Delta_k=o(k)$ and $p_s=(2-o(1))k$.  Put
$L=\lfloor k/\Delta_k\rfloor$.  For each $1\le m\le L$, the intervals in
(2), as $p$ runs through $p_1,\ldots,p_s$, meet and form
\[
 [mp_1+1,mp_s+k].
\]
For large $k$, successive such layers also meet because
$2p_1\le p_s+k$.  Hence all candidates through $Lp_s+k$ are forbidden.
Since $L\to\infty$, (3) follows.

## Quotient teeth

Let $n=n_k$, put $N=n-1$ and $x=N/k$.  By (3), $x\to\infty$.  For every
positive integer $q$, define the tooth
\[
 T_q=\left(\frac{N-k}{q},\frac Nq\right].             \tag{4}
\]
If a prime $p\in(k,2k)$ belongs to $T_q$, then
\[
 N-k<qp\le N,
\]
and integrality makes this equivalent to
$qp\in[n-k,n-1]$, contradicting admissibility.  Thus every $T_q$ is free of
primes from $(k,2k)$.

Set
\[
 A=\left\lfloor\frac x2\right\rfloor,
 \qquad B=\lceil x\rceil-2,
 \qquad \mathcal Q=\{A+1,\ldots,B\}.
\]
For $q\in\mathcal Q$ the whole tooth lies strictly inside $(k,2k)$.  Moreover,
if $q<r$ are in $\mathcal Q$, then
\[
 \frac Nr\le\frac N{q+1}<\frac{N-k}{q},
\]
so these teeth are pairwise disjoint and separated by genuine gaps.  Their
total length is
\[
 \sum_{q\in\mathcal Q}|T_q|
 =k\sum_{q=A+1}^{B}\frac1q
 =(\log2+O(x^{-1}))k.                                 \tag{5}
\]

Let
\[
 E=(k,2k)\setminus\bigcup_{q\in\mathcal Q}T_q.
\]
Every prime in $(k,2k)$ lies in $E$.  By (5), $E$ has total length
\[
 H=(1-\log2+o(1))k                                    \tag{6}
\]
and at most
\[
 r=|\mathcal Q|+1=O(x)=O(n/k)                         \tag{7}
\]
interval components.  The lower-open endpoint in (4) is essential: equality
$qp=N-k=n-k-1$ lies just outside the product interval.

## Componentwise Brun--Titchmarsh

Fix $1<\beta<2\log2$ and suppose, for a contradiction along an infinite
sequence, that $n_k\le k^\beta$.  From (6)--(7), with $D=H/r$,
\[
 D\gg \frac{k^2}{n_k}\ge k^{2-\beta}.                \tag{8}
\]
Split the components of $E$ at
\[
 T=\frac{D}{(\log D)^2}.
\]
The components shorter than $T$ contain at most
\[
 r(T+1)=\frac{H}{(\log D)^2}+r=o(k/\log k)            \tag{9}
\]
integers, hence that many primes.

Round each remaining real component outwards to an integer interval.  Its
length changes by $O(1)$, so the total change is $O(r)=o(k/\log k)$.
Brun--Titchmarsh and (6) then bound the primes in all long components by
\[
 \frac{2(H+O(r))}{\log(T-O(1))}
 \le\left(\frac{2(1-\log2)}{2-\beta}+o(1)\right)
       \frac{k}{\log k}.                              \tag{10}
\]
The coefficient in (10) is strictly less than $1$ precisely when
$\beta<2\log2$.  Equations (9)--(10) contradict the PNT count
\[
 \pi(2k)-\pi(k)=(1+o(1))\frac{k}{\log k},
\]
because every one of these primes must lie in $E$.  This proves the lower
bound in (1).  If $\beta\le1$, the conclusion already follows from $n_k>2k$.

## Explicit upper construction

Let
\[
 P_k=\prod_{k<p<2k}p
\]
and let $p_*$ be the largest prime below $2k$.  Put $Q=P_k/p_*$.  By the PNT,
$p_*=(2-o(1))k$, $Q>2k$ for large $k$, and
\[
 \log P_k=\vartheta(2k)-\vartheta(k)=k+o(k).
\]
The $k+1$ residues
\[
 Q,2Q,\ldots,(k+1)Q\pmod {p_*}
\]
are distinct, whereas only the $k$ residues $1,\ldots,k$ are forbidden.
Choose $1\le t\le k+1$ with $tQ$ allowed modulo $p_*$.  Every other prime in
$(k,2k)$ divides $tQ$, giving allowed residue $0$, and $tQ>2k$.  Consequently
\[
 n_k\le(k+1)\frac{P_k}{p_*}
      =\left(\frac12+o(1)\right)P_k
      =\exp((1+o(1))k),
\]
which proves the upper bound in (1).  For $k=1$ the forbidden set is empty and
$n_1=3$.

## Remaining gap

The exact full-period density is
\[
 \delta_k=\prod_{k<p<2k}\left(1-\frac{k}{p}\right),
 \qquad
 \log\delta_k=-(2\log2+o(1))\frac{k}{\log k}.
\]
This suggests, but does not prove,
$\log n_k\sim(2\log2)k/\log k$.  Establishing a first representative near
$\delta_k^{-1}$ requires an anchored localization theorem; the CRT density
alone does not supply one.
