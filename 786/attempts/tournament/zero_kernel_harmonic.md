# Zero-kernel stability via 2-adic layers

Let \(f=f_x:\mathbb N\to\mathbb Q\) be completely additive and put
\[
B_f(x)=\#\{n\le x:f(n)\ne0\}=\delta x,
\quad P=\{p\le x:f(p)\ne0\},
\quad H=\sum_{p\in P}\frac1p.
\]
This note proves
\[
\delta=o(1)\quad\Longrightarrow\quad H=o(1).             \tag{1}
\]

Only the following standard uniform mean-value result is used.

**Hall--Halasz parity stability.**  For every \(\eta>0\) there is
\(c(\eta)>0\), uniformly for moving prime sets
\(Q=Q_x\subseteq\{p\le x\}\), such that
\[
\sum_{p\in Q}\frac1p\ge\eta
\Longrightarrow
\frac1x\#\left\{n\le x:\sum_{p\in Q}v_p(n)\equiv1\pmod2\right\}
\ge c(\eta)-o(1).                                        \tag{2}
\]
This is the near-equality corollary of the **sharp normalized one-sided**
form of Hall's real mean-value theorem.  Applied to the completely
multiplicative function \(g_Q\) which is \(-1\) on \(Q\) and \(+1\) on
the other primes, that theorem supplies an absolute \(\kappa>0\) such that
\[
 \frac1x\sum_{n\le x}g_Q(n)
 \le \exp\left(-2\kappa\sum_{p\in Q}\frac1p\right)+o(1). \tag{3}
\]
The normalized leading constant one is important; a generic
\(\ll e^{-2\kappa\sum 1/p}\) estimate would not imply the needed gap for
small fixed harmonic mass.  In the present application every
\(p\in Q\) tends to infinity by (4), and the error in (3) is uniform for
such moving \(Q\).  Since the odd-parity density is
\((1-x^{-1}\sum_{n\le x}g_Q(n))/2\), one may take
\[
c(\eta)=\frac{1-e^{-2\kappa\eta}}2.                      \tag{3a}
\]
Only positivity of \(c(\eta)\) is used.  The estimate is pointwise-uniform
in \(Q\), so triangular arrays and primes moving with \(x\) are allowed.

## Preliminary bounds

If \(p\in P\), partition \([1,x]\) into its \(p\)-adic chains.  The
values of \(f\) along a chain form an arithmetic progression with nonzero
difference \(f(p)\), so the zero kernel contains at most one point of each
chain.  Consequently
\[
B_f(x)\ge\left\lfloor\frac xp\right\rfloor,
\qquad p\ge y_x:=\frac{x}{B_f(x)+1}\longrightarrow\infty. \tag{4}
\]

Let \(T(n)=\#\{p\in P:p\mid n\}\).  If \(T(n)=1\), then
\(f(n)=v_p(n)f(p)\ne0\).  Since
\({\bf1}_{T=1}\ge T-2{T\choose2}\), divisor moment counting gives
\[
\delta\ge H-H^2-\frac{\#P}{x}=H-H^2-o(1).                 \tag{5}
\]
Thus (1) follows once \(H\) is bounded above by any fixed number below one.

## 2-adic layers

Clear the denominators of the finitely many \(f(p)\), obtaining nonzero
integers \(a_p\) such that zero values are characterized by
\[
\sum_{p\in P}a_pv_p(n)=0.                                \tag{8}
\]
Put
\[
P_j=\{p\in P:v_2(a_p)=j\},\qquad
h_j=\sum_{p\in P_j}\frac1p,qquad L_j=\sum_{i<j}h_i.      \tag{9}
\]
If (8) holds, no lower-layer prime divides \(n\), and a layer-\(j\)
prime does divide \(n\), then reduction of (8)/\(2^j\) modulo two gives
\[
\sum_{p\in P_j}v_p(n)\equiv0\pmod2.                     \tag{10}
\]

Fix a finite layer prefix and write \(h=\sum_{j\le r}h_j\).  For uniform
\(n\le x\), let \(T_j(n)=\#\{p\in P_j:p\mid n\}\) and
\(T_{<j}=\sum_{i<j}T_i\).  The events
\(E_j=\{T_{<j}=0,T_j=1\}\) are disjoint, and pointwise
\[
\mathbf 1_{E_j}\ge T_j-2{T_j\choose2}-T_jT_{<j}.          \tag{11}
\]
Using
\[
\mathbb ET_j=h_j+o(1),\quad
2\mathbb E{T_j\choose2}\le h_j^2,\quad
\mathbb E(T_jT_{<j})\le h_jL_j,                           \tag{12}
\]
where the first errors sum to at most \(\pi(x)/x=o(1)\), yields
\[
\begin{aligned}
\mathbb P\left(\bigcup_{j\le r}E_j\right)
&\ge h-\sum_jh_j^2-\sum_jh_jL_j-o(1)\\
&=h-\frac{h^2+\sum_jh_j^2}{2}-o(1)\\
&\ge h-h^2-o(1).                                         \tag{13}
\end{aligned}
\]
Apart from the event that a prime in this prefix divides \(n\) to exponent
at least two, an \(E_j\)-integer violates (10), and hence is outside the
zero kernel.  For a prefix of harmonic mass \(h=O(1)\), (4) gives
\[
\sum_{j\le r}\sum_{p\in P_j}\frac1{p^2}\le\frac{h}{y_x}=o(1).
\]
Therefore every bounded-mass prefix satisfies
\[
\delta\ge h-h^2-o(1).                                    \tag{14}
\]

## Closing the bounded-mass gap

Let \(c_0=c(1/2)>0\) be supplied by (2), and fix
\[
0<a<\min\{1/4,c_0/2\}.                                   \tag{15}
\]
Suppose \(H\ge a\), and let \(r\) be the first layer index with
\(S_r=\sum_{j\le r}h_j\ge a\).

If \(S_r\le1-a\), (14) gives
\(\delta\ge a(1-a)-o(1)\), impossible when \(\delta=o(1)\).

Otherwise
\[
S_{r-1}<a,\qquad h_r>1-2a\ge1/2.                          \tag{16}
\]
By (2), layer \(P_r\) has odd valuation parity on at least
\((c_0-o(1))x\) integers.  The union bound says that lower-layer primes
divide at most \(S_{r-1}x<ax\) integers.  On the difference, (10) rules
out a zero value.  Hence
\[
\delta\ge c_0-a-o(1)>c_0/2-o(1),                          \tag{17}
\]
again impossible.

Thus eventually \(H<a<1\).  Returning to (5) gives
\[
(1-a)H\le\delta+o(1),                                    \tag{18}
\]
which proves (1).

As an immediate extension consequence, if \(f_{\le x}\) is obtained by
setting all weights at primes greater than \(x\) to zero, then
\[
\#\{n\le x^2:f_{\le x}(n)\ne0\}
\le\sum_{p\in P}\left\lfloor\frac{x^2}{p}\right\rfloor
\le x^2H=o(x^2).                                         \tag{19}
\]
