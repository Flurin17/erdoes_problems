# Notes: Erdős #415

## 1. Normalized definitions

For $\sigma\in S_k$, the consecutive block beginning at $m+1$ has strict
pattern $\sigma$ if
\[
\phi(m+\sigma(1))<\cdots<\phi(m+\sigma(k)).
\]
The permutation lists the positions in increasing order of totient.  A block
with a tie has no strict pattern.  Unless otherwise marked, $m\ge0$; exact
computations will also report what changes when $m\ge1$.

Let
\[
M(\sigma)=\min\{m+k:\sigma\text{ occurs at }m\},\qquad
M_k=\max_{\sigma\in S_k}M(\sigma).
\]
The normalized every-pattern interpretation is
\[
F(n)=\max\{k:M_k\le n\}.
\]

The literal existential interpretation of “any” asks only for at least one
strict block and measures the longest consecutive block of pairwise-distinct
totients.  A common-witness reading is impossible for $k\ge2$.  These are not
the main problem.  All logarithms below are natural.

## 2. Elementary structural facts

### Heredity of the every-pattern property

Extend prescribed $\tau\in S_j$ by declaring positions $j+1,\ldots,k$
successively largest.  Truncating an occurrence of the extension lowers its
endpoint by $k-j$, so
\[
M_j\le M_k-(k-j).
\]
Thus finite thresholds strictly increase and
\[
F(n)\ge k\iff M_k\le n,
\qquad F(n)=k\iff M_k\le n<M_{k+1}.
\]

### Tie convention

There are $k!$ strict chambers in $\mathbb R^k$ but additional equality faces.
A totient block on such a face belongs to no chamber.  Ignoring it is legitimate
when enumerating strict occurrences only if it remains present in the scan and
is classified as “tie/no pattern”; arbitrary tie-breaking would change both
first occurrences and frequencies.

Since $\phi(1)=\phi(2)=1$, $m=0$ gives no strict occurrence for any $k\ge2$.
Thus the $m\ge0$ and $m\ge1$ conventions differ only at $k=1$.

### Exact tiny cases

From $\phi(1),\ldots,\phi(6)=(1,1,2,2,4,2)$,
\[
M_1=1,\quad M((1,2))=3,\quad M((2,1))=M_2=6.
\]

### Totient-ratio representation

For every positive integer $t$,
\[
\phi(t)=t\,r(t),\qquad
r(t)=\prod_{p\mid t}\left(1-\frac1p\right).
\]
Thus a construction controlling $r(m+i)$ must leave gaps large enough to absorb
the factor ratios $(m+i)/(m+j)$.  For $m$ much larger than $k$, these ratios lie
between $m/(m+k)$ and $(m+k)/m$, but this observation alone gives no control of
unprescribed prime divisors in $r(m+i)$.

## 3. Inverting the threshold

Write $L_3(x)=\log\log\log x$ where defined.  If one proves the sufficiently
uniform two-sided estimate
\[
L_3(M_k)=\alpha k+o(k),
\]
then monotonicity/heredity and bracketing between $M_k$ and $M_{k+1}$ give
\[
F(n)=(\alpha^{-1}+o(1))L_3(n).
\]
Indeed, with $K=F(n)$ one has $M_K\le n<M_{K+1}$, so
$(\alpha-o(1))K\le L_3(n)<(\alpha+o(1))(K+1)$ once $K\to\infty$.
Equivalently,
\[
\log\log M_k=\exp((\alpha+o(1))k).
\]
Conversely, if $F(n)\sim cL_3(n)$ with $c>0$, then all thresholds are finite
and strict growth gives $F(M_k)=k$, hence $L_3(M_k)\sim k/c$.  The desired
constant is $c=1/\alpha$.  The existence and growth of all $M_k$
remain to be proved; this section is only the exact inverse reduction.

## 4. Questions kept separate

1. **One pattern:** bound $M(\sigma)$ for a fixed prescribed $\sigma$.
2. **Every pattern:** bound $M_k=\max_\sigma M(\sigma)$ uniformly.
3. **Extremal pattern:** the source descent is
   $D_k=(k,k-1,\ldots,1)$.  Its clean formulation is $M(D_k)=M_k$.
   If all $M(\sigma)$ are finite, two different patterns cannot have the same
   first endpoint, because an endpoint fixes one window and a strict window
   has one pattern.  Thus co-last and unique-last then coincide.
4. **Frequency:** for fixed $k$ define
   \[
   N_\sigma(x)=\#\{0\le m\le x-k:\sigma\text{ occurs at }m\}.
   \]
   One must specify whether “most likely” means maximal $N_\sigma(x)$ for all
   large $x$, maximal limiting density (if it exists), or a heuristic model.
   Moreover the cited natural list has the tie $\phi(1)=\phi(2)$ for every
   $k\ge2$ and hence defines only a weak order.  Stable tie-breaking, all
   linear extensions, and exact weak-pattern matching are different questions.

For each window, the sum of strict-pattern indicators is $1$ if its totients
are pairwise distinct and $0$ otherwise.  Thus retaining tied windows in the
unconditional denominator is exact, and conditioning on tie-free windows does
not change the finite-cutoff argmax.

## 5. Initial dependency targets

- compatible prime-set prescription for all shifts;
- strict-gap lemma absorbing $(m+i)$ and uncontrolled prime factors;
- optimized CRT-modulus estimate uniform in $\sigma$;
- universal, architecture-independent obstruction of matching scale;
- exact small-$k$ data to falsify extremality and frequency guesses.

No item in this list is yet asserted proved.
