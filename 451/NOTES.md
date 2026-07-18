# Notes for Erdős Problem #451

## Normalized notation

For an integer $k\ge 1$, let
\[
\mathcal P_k=\{p\text{ prime}:k<p<2k\},\qquad
A_k=\{n\in\mathbb Z:n\bmod p\notin[1,k]\text{ for all }p\in\mathcal P_k\}.
\]
Then $n_k=\min(A_k\cap\{2k+1,2k+2,\ldots\})$.

## Lemma 1 (exact residue equivalence)

For every integer $n$ and $p\in\mathcal P_k$,
\[
p\nmid\prod_{i=1}^k(n-i)
\quad\Longleftrightarrow\quad
n\bmod p\in\{0,k+1,k+2,\ldots,p-1\}.
\]

**Proof.** The prime $p$ divides the product exactly when it divides $n-i$ for
some $i\in\{1,\ldots,k\}$, equivalently when $n\equiv i\pmod p$ for such an
$i$.  Since $k<p$, these are $k$ distinct residue classes.  Their complement
in $\mathbb Z/p\mathbb Z$ is the displayed set. $\square$

Equivalently, the length-$k$ integer interval $[n-k,n-1]$ contains no multiple
of any $p\in\mathcal P_k$.  It contains at most one multiple of each such $p$
because $k<p$.

Writing $p=k+r$ and $n=2k+t$, admissibility is equivalently
\[
t\bmod p\in\{r+1,\ldots,2r\}.                         \tag{1}
\]
The exact covering form is
\[
n\text{ forbidden}\iff n\in[mp+1,mp+k]
\]
for some $p\in\mathcal P_k$ and positive integer $m$.  Also
$\gcd(\binom{n-1}{k},P_k)=1$ is equivalent to admissibility.

## Immediate periodic facts

Writing $P_k=\prod_{p\in\mathcal P_k}p$, the Chinese remainder theorem gives
exactly $\prod_{p\in\mathcal P_k}(p-k)$ admissible classes modulo $P_k$.
Consequently $A_k$ has exact periodic density
$\prod_{p\in\mathcal P_k}(1-k/p)$.  This does not localize the first member of
$A_k$ above $2k$.

Every multiple of $P_k$ is admissible, so $n_k\le2k+P_k$.  By PNT,
$\log P_k=k+o(k)$.

## Prime-gap layer lemma

Let $p_1<\cdots<p_s$ be the primes in $(k,2k)$ and
$\Delta_k=\max\{p_1-k,2k-p_s,p_{j+1}-p_j\}$.  If $\Delta_k\le k/3$ and
$L=\lfloor k/\Delta_k\rfloor$, then
\[
n_k\ge Lp_s+k+1.                                      \tag{2}
\]
For fixed $m\le L$, the intervals $[mp_j+1,mp_j+k]$ meet and form
$B_m=[mp_1+1,mp_s+k]$.  Successive $B_m$ meet because
$2p_1\le2k+2\Delta_k\le3k-\Delta_k\le p_s+k$.
Thus their union covers every candidate through $Lp_s+k$.

The PNT gives $\Delta_k=o(k)$, hence $n_k/k\to\infty$.  Its classical
effective form $\vartheta(x)=x+O(xe^{-c\sqrt{\log x}})$ gives
$\Delta_k\ll ke^{-c'\sqrt{\log k}}$ and therefore
\[
n_k\ge k\exp(c''\sqrt{\log k})
\]
for some $c''>0$ and all sufficiently large $k$.

## Exact initial values

Two independent exhaustive formulations give
\[
(n_k)_{k=1}^{20}=(3,6,9,20,13,21,21,22,65,220,51,338,133,321,339,340,
113,114,368,550).
\]

The full table through $k=50$ and independently checkable covering
certificates are in `computational/values_1_50.tsv` and
`computational/certificates/`.

## Quotient-comb lower bound

For $N=n-1$, the intervals
\[
\left(\frac{N-k}{q},\frac Nq\right]
\]
are prime-free whenever $n$ is admissible.  A disjoint subfamily inside
$(k,2k)$ has total length $(\log2+o(1))k$, leaving all primes in a union of
$O(n/k)$ intervals of total length $(1-\log2+o(1))k$.  Splitting off short
components and applying Brun--Titchmarsh to the rest proves
\[
n_k\ge k^{2\log2-o(1)}.
\]
The full endpoint-checked proof is in `PROOF.md`; independent route details
and prime-gap-tail refinements are in `attempts/average_gap_tails.md`.

## Density asymptotic and conjectural scale

PNT away from $p=k$, together with Brun--Titchmarsh on dyadic shells near that
endpoint, gives
\[
\log\prod_{k<p<2k}\frac{p-k}{p}
=-(2\log2+o(1))\frac{k}{\log k}.
\]
The inverse density therefore suggests
$\log n_k\sim(2\log2)k/\log k$, but no anchored localization theorem has been
proved.  All claims in `PROOF.md` remain strictly weaker than this conjecture.

For $k=1$, $\mathcal P_1=\varnothing$, so every integer is admissible and the
strict inequality gives $n_1=3$.

## Ambiguities to preserve

The source does not explicitly quantify $k$.  We use the standard intended
reading $k\in\mathbb Z_{\ge1}$.  With an empty-product convention, $k=0$
would give $n_0=1$; this is not the adopted problem.
