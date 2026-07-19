# Prefix-specific joint discrepancy

Let $p\ne r$ be primes in $(k,2k)$, put $a=p-k$, and let
$A_p=\{0,k+1,\ldots,p-1\}$.  For the literal prefix $[0,H)$ define
\[
y_b=|\{0\le x<H:x\bmod p\in A_p, x\equiv b\pmod r\}|.
\]

Write $H=qpr+u$, $0\le u<pr$.  For $c\in A_p$, let
\[
x_{b,c}=b+r[(c-b)r^{-1}]_p\in[0,pr).
\]
Then exactly
\[
y_b=qa+\sum_{c\in A_p}1_{x_{b,c}<u}.                \tag{1}
\]
If $u=mr+w$, $0\le w<r$, the tail has either $m$ or $m+1$ distinct
residues modulo $p$ in each $r$-class.  Therefore
\[
\left|y_b-rac{|Y|}{r}\right|<a,                   \tag{2}
\]
and, when $H\ge p$,
\[
\left|\frac{y_b}{|Y|}-rac1r\right|
<\frac1{\lfloor H/p\rfloor}.                        \tag{3}
\]

The scale in (2) is real.  For
$k=75,p=101,r=103,H=101\cdot13$, one gets
$y_{76}=13$ and $y_1=0$, while $a=26$.  Even more starkly, when $p=k+1$ and
$X=[0,mp)$ with $1\ll m\ll r$, the original $p$-marginals are exact and the
$r$-marginals are asymptotically uniform, but filtering by the legal singleton
$A_p=\{0\}$ leaves only the $m$ residues of $0,p,\ldots,(m-1)p$ modulo $r$.
Thus marginal balance and prefix order do not imply conditional balance.

After earlier filters of product modulus $Q$ and allowed-box size $M$, the
same complete-period argument gives only absolute discrepancy $<M$ and
relative loss $O(rQ/H)$.  Since $Q\ge k^s$ after $s$ filters, at
$H=\exp(Ck/\log k)$ this controls at most $O(k/\log^2k)$ filters, compared
with $\asymp k/\log k$ relevant primes.  The route therefore closes at the
same support threshold as the Fourier calculation; a viable induction needs
collective conditional discrepancy, not sequential one-prime marginals.
