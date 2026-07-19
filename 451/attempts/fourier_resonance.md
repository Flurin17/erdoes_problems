# High-conductor Fourier resonance obstruction

This file records an obstruction, not an upper or lower estimate for $n_k$.

Let $q_p=p-k$ and
\[
F_p(a)=\sum_{j=0}^{q_p-1}e(aj/p).
\]
Fix $0<c<1$, put $L_p=\lfloor cp/q_p\rfloor$, and consider
\[
\Theta(x)=\sum_p\frac{x_p}{p}\pmod1,qquad0\le x_p\le L_p.
\]
These points are distinct: an integral difference reduces modulo each prime
to $x_p-y_p\equiv0\pmod p$, and $|x_p-y_p|<p$.

If two points lie in the same non-wrapping arc of width $1/(KH)$, their
difference gives a character with
\[
0<|\theta|\le1/(KH),qquad d\ge KH,                  \tag{1}
\]
because a nonzero rational of exact denominator $d$ has magnitude at least
$1/d$.  Also $|a_p|q_p/p\le c$, so
\[
\frac{|F_p(a_p)|}{q_p}
\ge\frac{\sin(\pi c)}{pi c}                         \tag{2}
\]
on every active coordinate.

The phase coloring needs the integer lift.  Write
$S(x)=\sum_px_p/p=N_x+t_x$ with all $t_x$ in the same arc, and color by
\[
\beta(x)=\sum_px_p-(k+1)N_x\pmod2.                  \tag{3}
\]
For $a=x-y$, the exact product-coefficient phase is
\[
(-1)^{\sum a_p-(k+1)(N_x-N_y)}e(-(k+1)\theta/2).
\]
Thus equal colors in (3), after multiplying by the anchor and the Dirichlet
kernel, place all contributions in one positive phase sector of angular width
$O(1/K)$.  Coloring only by coordinate parity is false when the integer-lift
parity changes.

The number of box points has exponential rate
\[
I(c)=\int_1^2
\log\left(\left\lfloor\frac{ct}{t-1}\right\rfloor+1\right)dt.
\]
For $c=0.9$, direct interval decomposition gives
\[
I(c)=\log2+0.9\sum_{n\ge2}
\frac{\log(1+1/n)}{n-0.9}=1.4234\ldots>\log4.
\]
The strict inequality is elementary rather than numerical evidence: using
$\log2>69/100$ and $\log(1+x)\ge2x/(2+x)$, the terms through $n=50$ already
give the rational lower bound $1.3965\ldots>1.387>\log4$; all omitted terms
are positive.  The decimal is only a display of that rational sum.

Hence, even at the conjectural $H=\exp((\log4+o(1))k/\log k)$, the
high-conductor set contains exponentially many distinct $1/H$-close,
nonoscillatory, phase-coherent modes satisfying (1)--(2).  This rules out any
large-sieve argument whose gain comes only from $d>H$, presumed $1/H$
frequency separation, or individual Dirichlet-kernel oscillation.  It does
not prove that the whole tail is large: the products in (2) may still be
exponentially small, so further collective phase information is required.
