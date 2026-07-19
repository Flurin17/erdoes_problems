# Adaptive bounded corrections still do not produce a dense exact level

## Result

Put (K=\lfloor\log\log N\rfloor).  Fix (C<\infty), and for every
prime (p\leq N) choose an integer (B_N(p)), completely arbitrarily
apart from

\[
 \left|B_N(p)-{K\log p\over\log N}\right|\leq C.               \tag{1}
\]

Extend (B_N) completely additively.  Then

\[
 \max_{c\in\mathbb Z}{1\over N}
 |\{n\leq N:B_N(n)=c\}|
 \ll_C(\log K)^{-1/4}=o(1).                                   \tag{2}
\]

Thus independently rounding each prime up or down, moving band boundaries
prime by prime, or applying any other fixed finite menu of local corrections
cannot repair the exact-atom failure of rounded normalized logarithms.  The
choices in (1) need not depend only on the band; they may be adversarial.

## Finite-choice circle lemma

Let (E\subset\mathbb Z) be nonempty with (|E|\leq D).  If (q) is prime,
(q\geq q_0(D)), and (1\leq a<q), then, uniformly in real (z),

\[
 {1\over q}\sum_{j=0}^{q-1}\min_{e\in E}
 \left(1-\cos {2\pi(a(j+e)-z)\over q}\right)\geq c_D>0.       \tag{3}
\]

Multiplication by (a) permutes the residues modulo (q).  For one (e),
the residues where the loss is below (eta) occupy an arc containing
(O(q\sqrt\eta+1)) residues.  The union over (E) has
(O(Dq\sqrt\eta+D)) residues.  Taking a sufficiently small constant
multiple of (D^{-2}) for (eta) leaves at least half the residues with
loss at least (eta), which proves (3).

Write

\[
 x_p={K\log p\over\log N}.
\]

We need the following consequence.  Suppose (q=o(K^{1/3})) is prime,
(q\geq q_0(C)),
(1\leq a<q), and (|\gamma|\leq K^{-3/4}).  Under (1),

\[
 \sum_{p\leq N}{1-
 \cos\!\left({2\pi\over q}(aB_N(p)-\gamma x_p)\right)\over p}
 \geq c_C\log K.                                               \tag{4}
\]

To prove this, split the primes into bands

\[
 N^{j/K}<p\leq N^{(j+1)/K},\qquad q^2\leq j<K.                 \tag{5}
\]

On band (j), condition (1) gives

\[
 B_N(p)=j+e,
 \qquad e\in E_C:=\{e\in\mathbb Z:|e|\leq C+1\}.              \tag{6}
\]

Replacing (gamma x_p) by (gamma j) changes the loss by
(O(|\gamma|/q)).  Group the (j)'s into consecutive blocks of (q).
Within a block, freeze (gamma j) at the left endpoint, at cost
(O(|\gamma|)).  Formula (3), with (E=E_C), gives a positive constant
average loss on each block.  Also

\[
 \sum_{N^{j/K}<p\leq N^{(j+1)/K}}{1\over p}
 =\log(1+1/j)+O\left({K\over j\log N}\right).                  \tag{7}
\]

This follows from the standard PNT form of Mertens' theorem.  The weights
(1/j) vary by (1+O(1/q)) within a block because (j\geq q^2).
Consequently (3) and (7) give

\[
 c_C\sum_{q^2\leq j<K}{1\over j}+o(\log K)=c_C\log K.
\]

The accumulated freezing cost is (O(|\gamma|\log K)=o(1)), and the
accumulated error in (7) is (O(K\log K/\log N)=o(1)).  This proves (4).
The minimization over all of (E_C) before (3) is what makes the estimate
uniform in the prime-by-prime choices.

## Every small-modulus character is non-pretentious

Choose a prime

\[
 q\asymp(\log K)^{1/4};                                       \tag{8}
\]

Bertrand's postulate suffices.  For (1\leq a<q), put

\[
 g_a(n)=\exp(2\pi i aB_N(n)/q).
\]

We claim, uniformly in (a),

\[
 \min_{|t|\leq K}\mathbb D_N(g_a,n^{it})^2
 \geq c_C{\log K\over q^2},                                  \tag{9}
\]

where

\[
 \mathbb D_N(g,h)^2
 =\sum_{p\leq N}{1-\Re(g(p)\overline{h(p)})\over p}.
\]

Suppose instead that the left side at some (t) is less than
(delta\log K/q^2).  Since (g_a^q=1), the pointwise inequality
(|z^q-w^q|\leq q|z-w|) gives

\[
 \mathbb D_N(1,n^{iqt})^2<\delta\log K.                       \tag{10}
\]

We use the standard archimedean estimates

\[
 \mathbb D_N(1,n^{iu})^2
 =\int_{\log2}^{\log N}{1-\cos(uv)\over v}\,dv+O(1)
 \geq c\log(1+|u|\log N)-O(1)                                \tag{11}
\]

for (|u|\leq1), and

\[
 \mathbb D_N(1,n^{iu})^2
 \geq\log\log N-O(\log\log(3+|u|))                            \tag{12}
\]

for (1\leq|u|\leq qK).  Formula (11) is Mertens partial summation;
(12) is the usual comparison with
(log\zeta(1+1/\log N+iu)), using
(|\zeta(\sigma+iu)|\ll\log(3+|u|)) away from the pole.  Only
these familiar quantitative Halasz estimates are used.

With (u=qt), (10)--(12) first force (|qt|<1), and then give

\[
 |qt|\log N\leq K^{C_0\delta}                                 \tag{13}
\]

for an absolute (C_0).  Fix (delta) with (C_0\delta<1/4), and set

\[
 \gamma={qt\log N\over2\pi K}.
\]

Then (|\gamma|\leq K^{-3/4}) for large (N).  But a prime summand of
(mathbb D_N(g_a,n^{it})^2) equals

\[
 1-\cos\!\left({2\pi\over q}(aB_N(p)-\gamma x_p)\right).
\]

The band estimate (4) makes this distance at least (c_C\log K),
contradicting the assumed (delta\log K/q^2).  This proves (9).

## Halasz, Fourier inversion, and exact atoms

The standard quantitative Halasz theorem gives, for completely
multiplicative (|g|=1),

\[
 \left|{1\over N}\sum_{n\leq N}g(n)\right|
 \ll(1+\mathcal M)e^{-\mathcal M}+K^{-1/2},
 \qquad
 \mathcal M=\min_{|t|\leq K}\mathbb D_N(g,n^{it})^2.          \tag{14}
\]

By (8)--(9), every nontrivial (g_a) has
(mathcal M\gg_C\sqrt{\log K}).  Therefore

\[
 \max_{1\leq a<q}\left|{1\over N}\sum_{n\leq N}
 e^{2\pi iaB_N(n)/q}\right|=o(q^{-1}).                         \tag{15}
\]

Fourier inversion on (mathbb Z/q\mathbb Z) yields, uniformly in (r),

\[
 {1\over N}|\{n\leq N:B_N(n)\equiv r\pmod q\}|
 ={1\over q}+o(q^{-1}).                                       \tag{16}
\]

Every exact level is contained in one residue class.  Equations (8) and
(16) prove (2).

## Exact obstruction for unbounded but modulus-hidden corrections

There is a complementary statement with no size restriction.  Let

\[
 b_N(p)=\lfloor x_p\rfloor,\qquad B_N(p)=b_N(p)+d_p,
 \qquad S_q=\{p\leq N:d_p\not\equiv0\pmod q\}.                \tag{17}
\]

Then, for every integer (c),

\[
 {1\over N}|\{n\leq N:B_N(n)=c\}|
 \leq {1\over N}|\{n\leq N:b_N(n)\equiv c\pmod q\}|
       +\sum_{p\in S_q}{1\over p}.                            \tag{18}
\]

Indeed, outside the integers divisible by a prime in (S_q), the two
additive functions are congruent modulo (q); the exceptional set has size
at most (N\sum_{p\in S_q}1/p).  For the (q) in (8), the modular
equidistribution already proved for the uncorrected rounded-log function
turns (18) into

\[
 {1\over N}|\{B_N=c\}|
 \leq {1\over q}+o(q^{-1})+\sum_{p\in S_q}{1\over p}.          \tag{19}
\]

Thus arbitrary corrections that are multiples of a growing modulus apart
from a prime set of harmonic mass (o(1)) still have only (o(N))-sized
atoms.  If (S_q\subset(N^{1/u},N]) for fixed (u), all
(N^{1/u})-smooth integers avoid (S_q), so Dickman's theorem sharpens
(19) to

\[
 {1\over N}|\{B_N=c\}|
 \leq1-\rho(u)+{1\over q}+o(1).                               \tag{20}
\]

There is also an exact lexicographic obstruction.  If
(B_N(p)=b_N(p)+Md_p) with (M>K), then (B_N(n)=c) pins
(b_N(n)\) modulo (M).  Since (0\leq b_N(n)\leq K), it pins at most one
exact value of (b_N(n)); a correction in a separated higher digit cannot
enlarge a level.  Likewise, if
(B_N(p)=Mb_N(p)+d_p), (|d_p|\leq D), and
(M>2D\lfloor\log_2N\rfloor), the lower-digit sum is too small to allow
two different values of (b_N(n)) in one level.

## Remaining regime

The theorem rules out bounded local repairs.  Formula (19) also rules out
huge common-multiple corrections with only harmonically sparse low-digit
exceptions.  A successful density-one rounded-log construction would need
corrections growing with (K), visible on large prime sets modulo every
slowly growing modulus, with substantial carries between scales.  The
finite-choice constant in (3) deteriorates in that regime, so a genuinely
multiscale carry argument would be needed.
