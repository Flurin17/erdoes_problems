# Countermodel to the support-edge graph relaxation

Let $f$ be completely additive, let the target level be $1$, and put

\[
S=\{p\text{ prime}:f(p)\ne 0\}.
\]

Two necessary conditions for $A\subseteq\{n:f(n)=1\}$ are:

1. every $S$-free integer is outside $A$; and
2. $A$ is independent in every edge $n--pn$ with $p\in S$ and
   $pn\le N$.

These two conditions alone are compatible with density $1-o(1)$.

## Proposition (near-full graph-independent countermodel)

Put $y=\log N$, let $S$ consist of all primes larger than $y$, and set

\[
I_N=\{n\le N:n>N/y\text{ and some }p\in S\text{ divides }n\}.
\]

Then $I_N$ excludes every $S$-free vertex, is independent under every
edge $n--pn$ with $p\in S$, and

\[
|I_N|=N-o(N).
\]

### Proof

The exclusion assertion is part of the definition.  If $p>y$ and
$n,pn\le N$, then $n\le N/p<N/y$, so $n\notin I_N$.  Hence no relevant
edge has both endpoints in $I_N$.

The complement has size at most

\[
N/y+\Psi(N,y),
\]

where $\Psi(N,y)$ is the number of $y$-smooth integers at most $N$.
Rankin's bound with exponent $1/2$ gives

\[
\Psi(N,y)
\le N^{1/2}\prod_{p\le y}(1-p^{-1/2})^{-1}.
\]

Using

\[
\log(1-p^{-1/2})^{-1}\ll p^{-1/2}+p^{-1}
\]

and bounding the prime sums by the corresponding sums over all integers,
the product is

\[
\exp(O(\sqrt y+\log y)).
\]

For $y=\log N$, this is $N^{o(1)}$, and consequently

\[
\Psi(N,\log N)\le N^{1/2+o(1)}=o(N).
\]

Also $N/y=o(N)$, completing the proof.

## Why bounded grids are blind

More generally, suppose all factors $a_i,b_j$ lie in the slab
$(N/y,N]$ and

\[
\prod_{i=1}^r a_i=\prod_{j=1}^s b_j,
\qquad s>r.
\]

Taking logarithms gives

\[
s(\log N-\log y)\le r\log N,
\]

and therefore

\[
s\ge \frac{\log N}{\log y}.
\]

Thus, for $y=\log N$, every forbidden unequal-length relation contained
in the slab has longer side of length at least

\[
(1+o(1))\frac{\log N}{\log\log N}.
\]

This scale is genuine: take $t=\lfloor\sqrt{\log N}\rfloor$ and
$k=\lfloor\log N/\log t\rfloor$.  Then the consecutive powers
$t^k,t^{k-1}$ lie in $(N/\log N,N]$ and satisfy

\[
(t^k)^{k-1}=(t^{k-1})^k.
\]

A $2\times2$ multiplicative rectangle only gives a balanced affine
relation (the coefficients sum to zero), which is automatically compatible
with all four vertices lying on one affine level.  Hence neither bounded
stars nor bounded Boolean/rectangle grids can repair the graph relaxation.
A successful argument needs growing-depth relations with nonzero coefficient
sum, or must use the numerical values of the prime weights rather than just
their support.

## Secondary extremal picture

For a pure cutoff grading, $f(p)=0$ for $p\le N^{1/u}$ and $f(p)=1$
above the cutoff, the level $f=1$ has asymptotic density

\[
D(u)=2-2\rho(u)-\log u\qquad(2<u<3),
\]

maximized at (u=1+\sqrt e).  The same constant has a local star
interpretation.  If (X\le y^{u-1}), then the (y)-smooth and one-rough-prime
parts of \([1,X]\) have limiting proportions \(\rho(v)\) and
(1-\rho(v)\), where (v=\log X/\log y\).  For (1\le v\le u-1<2),

\[
\rho(v)=1-\log v.
\]

They balance at (v=\sqrt e), exactly giving (u=1+\sqrt e).  This
explains why cutoff examples are the sharp obstruction to a *fixed-cutoff*
star exchange, while the top-slab construction above is the sharper
obstruction to the support graph itself.
