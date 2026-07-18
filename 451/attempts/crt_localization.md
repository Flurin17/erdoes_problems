# CRT localization and beam search

## Proved benchmark

Let $P_k=\prod_{k<p<2k}p$, let $p_*$ be the largest factor, and put
$Q=P_k/p_*$.  For large $k$, $Q>2k$ and the $k+1$ values
$Q,2Q,\ldots,(k+1)Q$ are distinct modulo $p_*$.  Only $k$ residues are
forbidden, so one of these values is admissible modulo $p_*$; every other
relevant prime divides it.  Hence
\[
n_k\le(k+1)P_k/p_*=(1/2+o(1))P_k=\exp(k+o(k)).
\]

## Beam-extension lemma

Suppose $X\subset[0,Q)$ satisfies all processed prime constraints, and $p\nmid
Q$ is new.  Define
\[
\mu_p(X)=\max_{a\bmod p}|\{x\in X:x\equiv a\pmod p\}|.
\]
For $0\le T<p$, among the lifts $x+tQ$ with $x\in X$ and $0\le t\le T$,
at least
\[
(T+1)(|X|-k\mu_p(X))
\]
are allowed modulo $p$.  This follows because each lift layer loses at most
$k\mu_p(X)$ elements, and the pairs $(x,t)$ give distinct integers.

## Exact obstruction

Filtering at one prime changes the distribution modulo a future prime through
their joint distribution.  One-prime marginal balance therefore does not
iterate.  A sharp construction needs a hereditary multi-marginal discrepancy
lemma for every adaptively generated low beam.  In Fourier form, the same
missing statement is cancellation among the correlated inverse-CRT
frequencies in an anchored interval of length
$\delta_k^{-1}\exp(o(k/\log k))$.

Marginal balance is not enough, even for an initial interval.  Take
$k=1008$, $p=1009$, $r=1013$, and
\[
 X=\{0,1,\ldots,32p-1\}.
\]
Every class modulo $p$ occurs exactly $32$ times, while the class counts
modulo $r$ differ from their mean by less than one.  Since $p=k+1$, its allowed
set is the singleton $A_p=\{0\}$.  Filtering $X$ by $A_p$ leaves
$0,p,2p,\ldots,31p$, supported on only $32$ of the $1013$ residue classes
modulo $r$.  Thus excellent one-dimensional marginals can become almost
maximally nonuniform after one legal filter.

More generally, for $k=p-1$, a prime $r\in(p,2p)$, and
$1\ll m\ll r$, the prefix $X=[0,mp)$ has exact $p$-marginals and asymptotically
uniform $r$-marginals, but its $A_p$-filtered subset occupies only $m$ classes
modulo $r$.  The exact repair must control rectangles, or equivalently
conditional distributions.  If
\[
n_{a,b}=|\{x\in X:x\equiv a\pmod p,\ x\equiv b\pmod r\}|,
\qquad n_a=\sum_b n_{a,b},
\]
then for the filtered set $Y$,
\[
 |Y_b|-\frac{|Y|}{r}
 =\sum_{a\in A_p}\left(n_{a,b}-\frac{n_a}{r}\right).
\]
Consequently relative conditional $\varepsilon$-uniformity in every $p$-row
is inherited without loss, but separate marginal uniformity gives no bound at
all.  This closes the marginal-only beam node; the surviving open lemma is
hereditary conditional (joint) discrepancy for the actual low-prefix beams.

Finite beam success is only evidence.  For example, an all-zero branch can be
far from optimal even when it is a valid final CRT class.  The next useful
node is a two-prime hereditary extension lemma; failure there would eliminate
the full beam induction.
