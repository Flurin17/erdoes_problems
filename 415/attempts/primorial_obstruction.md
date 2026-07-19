# Route B: primorial-propagation obstruction

## Result

This route survives and is independent of the construction architecture.  If
\[
\phi(m+1)>\phi(m+2)>\cdots>\phi(m+k),\qquad m+k\le n,
\]
then
\[
\log_3 n
\ge k\bigl(\log_3 k+\gamma-\mu\bigr)+o(k),
\qquad
\mu=\sum_p\frac1p\log\frac p{p-1}.
\]
Thus the decreasing pattern alone supplies the matching lower bound for the
every-pattern threshold.

## 1. Loss is monotone in a decreasing totient block

Put
\[
h(t)=\log\frac t{\phi(t)}.
\]
For $i<j$, strict decrease of the totients gives
\[
h(m+j)-h(m+i)
=\log\frac{m+j}{m+i}+\log\frac{\phi(m+i)}{\phi(m+j)}>0.
\]
Hence $h(m+1),\ldots,h(m+k)$ is strictly increasing.

## 2. An unavoidable early primorial anchor

Let $P_r=p_1\cdots p_r\le k<P_{r+1}$ and put $R=P_{r-1}$.  Every interval
of $R$ consecutive integers contains a multiple of $R$, so for some
$1\le j\le R$,
\[
R\mid m+j.
\]
The maximal-order argument from Route A gives
\[
h(R)=\log_3 k+\gamma+o(1).
\]
More explicitly, $h(P_r)=\log_3 k+\gamma+o(1)$ and
$h(R)=h(P_r)-\log(p_r/(p_r-1))=h(P_r)-o(1)$.

PNT gives $p_r\sim\log k$, so
$R=P_r/p_r\le k/p_r=o(k)$ and
$R\log_3 k=o(k)$.  Monotonicity after the anchored index yields
\[
\sum_{i=1}^k h(m+i)
\ge(k-R+1)h(R)
=k(\log_3 k+\gamma)+o(k). \tag{1}
\]

## 3. Small primes cannot supply the propagated load

In an interval of length $k$, a prime $p$ divides at most $k/p+1$ terms.
Therefore the aggregate contribution from primes $p\le k$ is at most
\[
\begin{aligned}
\sum_{p\le k}w_p\left(\frac{k}{p}+1\right)
&=k\sum_{p\le k}\frac{w_p}{p}+\sum_{p\le k}w_p\\
&=\mu k+o(k),
\end{aligned}
\]
where $w_p=\log(p/(p-1))$, the first sum converges to $\mu$, and the second
is $O(\log_2 k)=o(k)$.

Subtracting this from (1), primes $p>k$ occurring in the block have total
weight
\[
S\ge k(\log_3 k+\gamma-\mu)+o(k). \tag{2}
\]

## 4. The obstruction is universal

A prime $p>k$ divides at most one of the $k$ consecutive integers.  Let $D$
be the squarefree product of all such primes occurring in the block.  Then
\[
h(D)=S,\qquad
D\mid\prod_{i=1}^k(m+i)\le n^k. \tag{3}
\]

Let
\[
H(x)=\max_{t\le x}h(t).
\]
The prime-exchange argument says the maximum is attained at the largest
primorial not exceeding $x$; PNT and Mertens give
\[
H(x)=\log_3x+\gamma+o(1). \tag{4}
\]
Equations (2)--(4) imply
\[
\log_3(n^k)
\ge k(\log_3 k+\gamma-\mu)+o(k). \tag{5}
\]

The right side tends to infinity faster than $\log_2 k$.  Consequently (5)
itself forces $\log_2 n$ to dominate $\log k$, and
\[
\log_3(n^k)
=\log(\log k+\log_2 n)
=\log_3n+o(1).
\]
This proves the result.

## Alternative finite inequality

For a completely explicit version, choose any primorial
$R_z=\prod_{p\le z}p\le k$ and write
\[
A_z=\sum_{p\le z}w_p,\quad
\mu_k=\sum_{p\le k}\frac{w_p}{p},\quad
C_k=\sum_{p\le k}w_p.
\]
Then every decreasing block satisfies
\[
S\ge(k-R_z+1)A_z-k\mu_k-C_k.
\]
Taking $z=\tfrac12\log k$ already gives the same two leading terms.

## What this does and does not show

The argument constrains every possible realization; it makes no assumption
about CRT, sieves, or how the block was found.  Combined with Route A it proves
that the decreasing pattern is asymptotically as hard as the worst pattern,
through the full $O(k)$ term in $\log_3 M_k$.  It does **not** say that its
finite first-occurrence endpoint is maximal for every $k$; that claim is in
fact false at $k=4$ (see `computational/verify_k4_counterexample.py`).
