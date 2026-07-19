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

## 5. Sharp threshold lemmas

Put
\[
w_p=\log\frac p{p-1},\qquad
h(t)=\sum_{p\mid t}w_p,\qquad
\mu=\sum_p\frac{w_p}{p}.
\]

1. If $P_r\le x<P_{r+1}$ are consecutive primorials, then
   \[
   \max_{t\le x}h(t)=h(P_r)=\log_3x+\gamma+o(1).
   \]
2. Reversing sums gives
   \[
   \sum_{i\le k}h(i)=\mu k+o(k).
   \]
3. Full cutoff control by CRT, disjoint private primes $>k^4$, and target gaps
   $8/k^4$ realize every prescribed pattern with
   \[
   \log_3M(\sigma)
   \le k(\log_3k+\gamma-\mu)+o(k)
   \]
   uniformly in $\sigma$.
4. In a decreasing totient block, the losses $h(m+i)$ strictly increase.  A
   multiple of the preceding primorial occurs among $o(k)$ initial shifts and
   propagates loss $\log_3k+\gamma+o(1)$ through almost the whole block.
   Small primes supply only $\mu k+o(k)$ total loss; primes $>k$ are private.
   Their squarefree product divides the block product, yielding the matching
   universal lower bound.

Thus
\[
\log_3M_k=k(\log_3k+\gamma-\mu)+o(k)
\]
and
\[
F(n)=\frac{\log_3n}{\log_6n+\gamma-\mu+o(1)}.
\]

## 6. Finite extremal-pattern counterexample

Exhaustive independent computations give
\[
\begin{aligned}
\phi(823),\ldots,\phi(826)&=(822,408,400,348),\\
\phi(824),\ldots,\phi(827)&=(408,400,348,826),
\end{aligned}
\]
with no earlier occurrences of the corresponding patterns.  Hence
\[
M((4,3,2,1))=826<827=M((3,2,1,4)).
\]
The decreasing pattern is asymptotically extremal but not finitely last for
every $k$.

## 7. Frequency theorem

For fixed $k$, independent uniform residues $U_p\pmod p$ define the convergent
loss vector
\[
X_i=\sum_pw_p\mathbf1_{U_p\equiv-i\pmod p}.
\]
Finite-prime truncations are periodic, arithmetic and profinite tails vanish
in mean, and pair differences are atomless by conditional fair signs plus
Sperner's theorem.  Therefore every strict pattern has a positive natural
density equal to its Haar chamber probability.

For $k=3$, removing $p=2$ gives an exchangeable odd-prime vector $Y$.  If
\[
q=\Pr(\max Y_i-\min Y_i>\log2),
\]
then $0<q<1$ and
\[
d(123)=d(321)=q/6,
\quad
d(132)=d(213)=d(231)=d(312)=1/4-q/12.
\]
This disproves the stable natural refinement.  The aggregate natural weak
order has density $1/4+q/12$, less than the same-shape competitor's
$1/2-q/6$.

## 8. Submission normalization and exact formal target

For positive integers $n,k$, the nontrivial every-pattern reading is the
quantified assertion
\[
\mathcal A(n,k):\quad
\forall\sigma\in S_k\ \exists m=m(\sigma)\in\mathbb Z_{\ge0},\quad
m+k\le n,\quad
\phi(m+\sigma(1))<\cdots<\phi(m+\sigma(k)).
\]
In particular the witness is pattern-dependent.  The readings
$\exists\sigma\exists m$ and $\exists m\forall\sigma$ are different problems;
the latter is impossible for $k\ge2$.  With strict ties excluded,
$\mathcal A(n,k)\Rightarrow k!+k\le n$ for $k\ge2$, because $m=0$ is tied and
each of the remaining $n-k$ starts realizes at most one pattern.

The exact limit formulation retaining the second-order constant is
\[
\lim_{k\to\infty}
\left(\frac{\log_3M_k}{k}-\log_3k\right)=\gamma-\mu,
\]
equivalently
\[
\lim_{n\to\infty}
\left(\frac{\log_3n}{F(n)}-\log_6n\right)=\gamma-\mu.
\]
A faithful formal main theorem must define $M_k$ and $F$ using
`Nat.totient`, prove occurrence of every pattern, and prove these limits.  A
formalization only of threshold inversion or of the finite $k=4$
counterexample is valuable but is not the formal counterpart of the sharp
main theorem.

The literal source question does not require $c>0$.  Since the sharp formula
gives $F(n)/\log_3n\to0$, the literal answer is “yes, with $c=0$”; the
nondegenerate positive-constant conjecture is false.

Exact small thresholds under $m\ge0$ are
\[
M_1=1,\qquad M_2=6,\qquad M_3=315.
\]
Taking $m\ge1$ changes only $M_1$ (from $1$ to $2$).  At the decisive cutoff,
$F(826)=3$, the decreasing 4-pattern has appeared, and the pattern $3214$ has
not.  This directly refutes the decreasing-first-missing formulation.
