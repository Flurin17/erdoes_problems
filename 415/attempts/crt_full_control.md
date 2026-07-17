# Route A: full-control CRT construction

## Result

This route survives.  With $\log_j$ denoting the $j$-fold natural logarithm,
it proves uniformly for every $\sigma\in S_k$ that
\[
\log_3 M(\sigma)
\le k\bigl(\log_3 k+\gamma-\mu\bigr)+o(k),
\qquad
\mu:=\sum_p\frac1p\log\frac p{p-1}.
\]
The series defining $\mu$ converges because its summand is $O(p^{-2})$.

The only standard analytic inputs are the prime number theorem in the form
$\vartheta(x)=x+o(x)$ and Mertens' product theorem
\[
A(x):=\sum_{p\le x}\log\frac p{p-1}
=\log\log x+\gamma+o(1).
\]

## 1. Baseline losses

Put
\[
w_p=\log\frac p{p-1},\qquad
h(t)=\log\frac t{\phi(t)}=\sum_{p\mid t}w_p,
\qquad H_k=\max_{1\le i\le k}h(i).
\]
If $P_r=p_1\cdots p_r\le k<P_{r+1}$, replacing any $r$ prime
divisors by the first $r$ primes shows that $H_k=h(P_r)$.  PNT and Mertens
therefore give
\[
H_k=\log_3 k+\gamma+o(1).
\]
Also, by reversing the order of summation,
\[
\sum_{i\le k}h(i)
=\sum_{p\le k}w_p\left\lfloor\frac{k}{p}\right\rfloor
=\mu k+o(k).
\]
The floor errors total $O(A(k))=o(k)$, and the tail of the convergent series
for $\mu$ is $o(1)$.

## 2. Private-prime allocation

Fix $K=k^4$ and $\delta=8/K$.  If $r_i$ is the rank determined by
$\sigma(r_i)=i$, set
\[
T_i=H_k+(k-r_i)\delta,
\qquad x_i=T_i-h(i)\ge0.
\]
Read the primes $p>K$ in increasing order.  For each $i$, assign consecutive
unused primes until their total $w_p$-weight first reaches $x_i$.  Since
$w_p<1/(K-1)$ and $\sum_p w_p=\infty$, this produces disjoint sets $P_i$
with
\[
x_i\le\sum_{p\in P_i}w_p<x_i+\frac1{K-1}.
\]
The total assigned weight $W$ satisfies
\[
\begin{aligned}
W
&=\sum_i x_i+o(1)\\
&=kH_k-\sum_{i\le k}h(i)
  +\frac{\delta k(k-1)}2+o(1)\\
&=k\bigl(\log_3 k+\gamma-\mu\bigr)+o(k).
\end{aligned}
\]

Mertens shows that the last allocated prime $y$ satisfies
\[
W=A(y)-A(K),\qquad \log_2 y=W+\log_2K+o(1).
\]
Since $W\sim k\log_3k$, one has $\log y\gg K$; thus the tail estimate in
Section 4 is automatically below $\delta/4$ for large $k$.  No unpriced
enlargement of the cutoff is used.

## 3. Exact residue prescription

Let $Q=\prod_{p\le y}p$.  Prescribe one residue modulo every prime $p\le y$:

- for $p\le K$ and for every unassigned $K<p\le y$, put $m\equiv0\pmod p$;
- for $p\in P_i$, put $m\equiv-i\pmod p$.

CRT gives a class $a\pmod Q$.  Choose $m=a+Q$, so $Q\le m<2Q$.
Because every assigned prime exceeds $k$, it divides exactly its designated
shift.  For $p\le k$, the condition $m\equiv0\pmod p$ makes
$p\mid m+i$ exactly when $p\mid i$.  Every unassigned $k<p\le y$ divides no
shift.  Thus the controlled loss $C_i$ of $m+i$ satisfies
\[
T_i\le C_i<T_i+\frac1{K-1}.
\]

This also proves the exact compatibility point: congruences
$m\equiv-i\pmod{a_i}$ are jointly soluble iff
$\gcd(a_i,a_j)\mid i-j$.  Private primes $>k$ make the $a_i$ pairwise
coprime, so compatibility is automatic.

## 4. Uncontrolled cofactor and size errors

Every uncontrolled prime divisor of $m+i$ exceeds $y$.  Since $m+i<3Q$, if
$s$ distinct such primes divide $m+i$, then
$(y+1)^s<3Q$.  Hence their loss $E_i$ obeys
\[
0\le E_i
\le \frac{\log(3Q)}{(y-1)\log(y+1)}
=O\left(\frac1{\log y}\right)<\frac\delta4.
\]
Here $\log Q=\vartheta(y)=(1+o(1))y$.  Also
\[
\left|\log\frac{m+i}{m+j}\right|
\le\log\frac{m+k}{m+1}<\frac{k}{Q}<\frac\delta4
\]
for all sufficiently large $k$.

For consecutive ranks $r,r+1$, the actual losses
$L_i=\log((m+i)/\phi(m+i))=C_i+E_i$ therefore satisfy
\[
L_{\sigma(r)}-L_{\sigma(r+1)}
>\delta-\frac1{K-1}-\frac\delta4
>\frac\delta4.
\]
This exceeds the possible logarithmic factor
$\log((m+\sigma(r))/(m+\sigma(r+1)))$.  Consequently
\[
\phi(m+\sigma(r))<\phi(m+\sigma(r+1))
\]
strictly for every $r$.  Notice that merely ordering $\phi(t)/t$ would not
have sufficed; the last displayed comparison is the required raw-totient
transfer.

## 5. Endpoint cost

PNT gives $\log Q=(1+o(1))y$, and hence
\[
\log_3(m+k)\le\log_3(3Q)
=\log_2y+o(1)
=W+o(k).
\]
Substitution of the value of $W$ proves the claimed uniform upper bound.

## Audit points

- Assigned primes are all $>K>k$, so no prime is accidentally shared.
- Every prime through $y$ receives a residue; unassigned small factors cannot
  appear.
- The tail estimate is re-proved for the chosen representative $Q\le m<2Q$;
  it is not assumed invariant under shifting a CRT solution.
- The target gap is $8/k^4$, while allocation, cofactor, and size errors are
  each strictly smaller components of that gap.
- The $o(k)$ terms are uniform in $\sigma$ because the total rank-ladder cost
  depends only on $k$.
