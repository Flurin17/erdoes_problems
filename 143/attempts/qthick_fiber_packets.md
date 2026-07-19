# Quotient-rough fiber packets

## Status

This route proves an exact disjoint-packet lemma for the uniform $Q$-thick
reduction. It does not prove the required global estimate. The remaining
statement is an explicit aggregate Hall inequality for periodic packets.

Let $S$ be a finite set of integers satisfying
\[
|kn-m|\ge Q
\quad(n\ne m\in S,\ k\ge1),                             \tag{1}
\]
where $Q$ is a positive integer. Write
\[
n=Qb+r,\qquad 0\le r<Q,\qquad \theta=r/Q.
\]

## 1. Quotient-rough carriers

For $b\ge2$, put
\[
U_b=\{u\ge1:p\mid u\Longrightarrow p\ge b\},
\qquad C_b=bU_b,
\]
and
\[
\rho_b=\prod_{p<b}\left(1-\frac1p\right),
\qquad \delta_b=d(C_b)=\frac{\rho_b}{b}.                \tag{2}
\]
These are periodic sifted sets, so the displayed natural density follows by
finite inclusion-exclusion. The elementary product bound already proved in
`../PROOF.md` gives
\[
\delta_b\gg\frac1{b\log b}.                             \tag{3}
\]

The carriers are laminar. If $b<c$ and $C_b\cap C_c$ is nonempty, write
$bu=cv$. Every prime factor of $v$ is at least $c$. Comparing valuations
shows that $b\mid c$; write $c=kb$. Then $u=kv$, existence forces
$k\in U_b$, and $U_c\subset U_b$, so
\[
C_c\subset C_b.                                         \tag{4}
\]

## 2. Disjoint fiber-packet lemma

For $n=Qb+r$ with $b\ge2$, define
\[
K_n=\left[\frac{\theta+1/2}{b},
           \frac{\theta+1}{b}\right),
\qquad E_n=C_b\times K_n.                               \tag{5}
\]

**Lemma 1.** If $S$ satisfies (1), the sets $E_n$, $n\in S$, are pairwise
disjoint.

**Proof.** Suppose first that the carriers for $n=Qb+r$ and $m=Qc+s$ meet,
with $b<c$. By (4), write $c=kb$. At multiplier $k$, (1) gives
\[
|kn-m|=|kr-s|\ge Q.
\]
Since $kr-s> -Q$, necessarily $kr-s\ge Q$. With $\phi=s/Q$, this says
$k\theta-\phi\ge1$, and hence
\[
\sup K_m=\frac{\phi+1}{kb}
\le\frac{\theta}{b}
<\frac{\theta+1/2}{b}=\inf K_n.                         \tag{6}
\]
Thus intersecting carriers have disjoint fibers. Nonintersecting carriers
already give disjoint products. Finally, two distinct elements with the same
$b$ differ by less than $Q$, contradicting (1) at $k=1$. $\square$

For each fixed $z$, the active carriers are therefore disjoint, so
\[
\sum_{\substack{n\in S\\z\in K_n}}
 \delta_{\lfloor n/Q\rfloor}\le1.                       \tag{7}
\]
Also
\[
\mu(K_n):=\int_{K_n}\frac{dz}{z}
=\log\frac{\theta+1}{\theta+1/2}
\ge\log(4/3).                                           \tag{8}
\]
For
\[
w_n=\frac{Q}{n\log(n/Q)}
=\frac1{(b+\theta)\log(b+\theta)},
\]
(3) gives $w_n\ll\delta_b$. Consequently
\[
H_S(z)=\sum_{n\in S}\frac{w_n}{\mu(K_n)}1_{K_n}(z)
\ll1,
\qquad
\int_0^\infty H_S(z)\frac{dz}{z}=\sum_{n\in S}w_n.      \tag{9}
\]

The logarithmic domain in (9) has unbounded depth, so the pointwise estimate
does not close the argument. This failure is sharp for a $z$-only majorant.
For $Q=1$ and
\[
S_B=\{B,B+1,\ldots,\lfloor3B/2\rfloor\},
\]
the set is admissible and every $K_n=[1/(2n),1/n)$ contains a common
logarithmic interval of absolute positive length. On that interval,
$H_{S_B}(z)\gg1/\log B$. Taking $B=2^j$ produces disjoint test intervals
whose lower bounds have divergent sum $\sum_j1/j$. Cross-scale information
about one fixed $S$, rather than a universal envelope, is indispensable.

## 3. Physical packets and the exact Hall target

Define a periodic subset of the integers by
\[
R_n=\{nu+j:u\in U_b,\ 0\le j<Q\}.                       \tag{10}
\]
When $b\ge2$, the $Q$ translates in (10) are disjoint and
\[
d(R_n)=\frac Qn\rho_b\gg
\frac{Q}{n\log(n/Q)}=w_n.                               \tag{11}
\]
The packets are not pairwise disjoint. For example, with $Q=2$ and the
admissible set $\{5,7\}$, the choices $u=7\in U_2$ and $v=5\in U_3$ give
$5u=7v=35$.

The precise remaining proposal is the aggregate Hall inequality
\[
d\left(\bigcup_{n\in T}R_n\right)
\ge \kappa_a\sum_{n\in T}d(R_n)                         \tag{H}
\]
for every $T\subseteq S\subset[aQ,\infty)$, where
$\kappa_a>0$ is independent of the finite sets and of $Q$. Every density in
(H) exists because the union is finite and periodic.

If (H) holds, take $T=S$. The left side is at most $1$, while (11) gives
\[
\sum_{n\in S}\frac{Q}{n\log(n/Q)}\ll_a1,
\]
which is exactly the sufficient uniform estimate in `../PROOF.md`. The bin
$b=1$ causes no difficulty: an element below $2Q$ cannot have a larger
companion satisfying (1), so it is a single bounded term when $n\ge aQ$ and
$a>1$.

Inequality (H) is unproved and may be stronger than the desired estimate.
The next falsification tests are common-center antichains and normalized
divisor-cube families. Pairwise overlap bounds are already false; only an
aggregate, mass-sensitive union estimate remains plausible.
