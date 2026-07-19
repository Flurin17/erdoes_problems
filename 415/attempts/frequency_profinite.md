# Route C: profinite frequency theorem and the natural-order counterexample

## Result

This route survives.  For every fixed $k$ and $\sigma\in S_k$, the natural
density
\[
d_k(\sigma)=\lim_{x\to\infty}\frac{N_\sigma(x)}x
\]
exists and is positive.  At $k=3$ the stable-index refinement of the source's
natural weak order is strictly less frequent than four other patterns.  Even
aggregating all linear extensions of the natural weak order does not maximize
frequency among weak orders of the same block shape.

## 1. The limiting arithmetic model

For independent uniform residues $U_p\in\mathbb Z/p\mathbb Z$, put
\[
w_p=\log\frac p{p-1},\qquad
X_i=\sum_p w_p\mathbf 1_{\{U_p\equiv-i\pmod p\}}.
\]
Because
\[
\mathbb E X_i=\sum_p\frac{w_p}{p}<\infty,
\]
the series converges almost surely and in $L^1$.  It is the Haar-profinite
model for
\[
\log\frac{m+i}{\phi(m+i)}.
\]

For a cutoff $Y$, the vector using only $p\le Y$ is periodic in $m$ modulo
$\prod_{p\le Y}p$, and its exact empirical distribution over one period is
the law of the corresponding truncated random vector.  Uniformly for each
fixed shift,
\[
\limsup_{N\to\infty}\frac1N\sum_{m<N}
\sum_{\substack{p>Y\\p\mid m+i}}w_p
\le\sum_{p>Y}\frac{w_p}{p}\le\frac1{\lfloor Y\rfloor}.
\]
The profinite tail has the same $L^1$ bound.  Thus the arithmetic vectors
converge weakly to $(X_1,\ldots,X_k)$.

## 2. Chamber boundaries have probability zero

Fix $i\ne j$.  Apart from finitely many primes dividing $i-j$, the
$p$-contribution to $X_i-X_j$ is
\[
\begin{cases}
+w_p,&\text{with probability }1/p,\\
-w_p,&\text{with probability }1/p,\\
0,&\text{with probability }1-2/p.
\end{cases}
\]
The activity events are independent and occur infinitely often almost surely,
because $\sum_p1/p$ diverges.  Conditional on the first $r$ active primes,
the signs are fair.  Sign choices giving one fixed sum form an antichain:
strict inclusion of the positive-sign sets strictly increases the sum.
Sperner's theorem therefore bounds every conditional atom by
\[
2^{-r}\binom r{\lfloor r/2\rfloor}=O(r^{-1/2})\to0.
\]
Hence $X_i-X_j$ is atomless.  Every strict-order chamber is consequently a
continuity set.

It follows from weak convergence that
\[
d_k(\sigma)
=\Pr(X_{\sigma(1)}>X_{\sigma(2)}>\cdots>X_{\sigma(k)}).
\]
The reversed inequalities occur because larger $X_i$ means smaller normalized
totient.  The raw totients have the same density: after subtracting the common
$\log m$,
\[
\log\phi(m+i)-\log m=-X_i(m)+\log(1+i/m),
\]
and the last term tends uniformly to zero away from the null chamber boundary.
Finite private-prime cylinders followed by Markov control of the tail show
that every chamber has positive probability.

## 3. Exact $k=3$ comparison

Remove the prime $2$ and call the remaining loss vector
$(Y_1,Y_2,Y_3)$.  It is fully $S_3$-exchangeable: for $p=3$ exactly one
coordinate is hit uniformly, and for $p>3$ either no coordinate or one
uniform coordinate is hit.  Put
\[
d=\log2,\qquad
q=\Pr\bigl(\max_iY_i-\min_iY_i>d\bigr).
\]
Parity is independent of $Y$.  After subtracting a common $d$ in one parity
state, the full vector has the same ranks as
\[
(Y_1,Y_2+\varepsilon d,Y_3),
\qquad \Pr(\varepsilon=1)=\Pr(\varepsilon=-1)=\tfrac12.
\]
Condition on three sorted distinct odd-prime loads.  Among the twelve
label/parity configurations, exactly two yield the spatially increasing
strict pattern and two the spatially decreasing strict pattern precisely when
the total range exceeds $d$; none do otherwise.  Consequently
\[
d_3(123)=d_3(321)=\frac q6,
\]
while reversal and pairwise symmetry give
\[
d_3(132)=d_3(213)=d_3(231)=d_3(312)
=\frac14-\frac q{12}.
\]

Both inequalities $0<q<1$ are strict.  For $q>0$, force the primes
$3,5,7$ onto one coordinate, avoid the other odd primes through a large
cutoff, and make the tail smaller than
\[
\log\frac{3\cdot5\cdot7}{2\cdot4\cdot6}-\log2
=\log\frac{35}{32}>0.
\]
For $q<1$, retain only the unavoidable $p=3$ contribution through a large
cutoff and make the tail range smaller than $\log(4/3)$; then the total range
is below $\log(3/2)+\log(4/3)=\log2$.  Each finite cylinder has positive
probability, and the tail condition has positive conditional probability by
Markov's inequality.

## 4. Consequences for the source's “natural” order

The reference tuple begins
\[
(\phi(1),\phi(2),\phi(3))=(1,1,2),
\]
so it is not a strict permutation.  Stable increasing-index tie-breaking gives
pattern $123$, but
\[
d_3(123)=q/6
<1/4-q/12=d_3(213).
\]
Thus the stable natural pattern is not most frequent.

There is also a tie-rule-independent comparison at the weak-order level.
Aggregate the two strict refinements of the natural block order
$\{1,2\}\prec\{3\}$; its density is
\[
d_3(123)+d_3(213)=\frac14+\frac q{12}.
\]
The same-shape competitor $\{1,3\}\prec\{2\}$ has density
\[
d_3(132)+d_3(312)=\frac12-\frac q6,
\]
larger by $(1-q)/4>0$.  Hence the natural weak order is not most frequent
under the aggregate-linear-extension interpretation either.

Finally, the Haar-preserving reflection
$x\mapsto-x-(k+1)$ gives
\[
d_k(\sigma)=d_k(r\circ\sigma),\qquad r(i)=k+1-i.
\]
No strict pattern can be a unique density maximizer for $k\ge2$.

## Limitation

This is a fixed-$k$ frequency theorem.  Positivity of a density is not uniform
enough in $k$ to control first-occurrence thresholds and is not used in the
proof of the main asymptotic.
