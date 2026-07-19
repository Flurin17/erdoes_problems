# Audit of zero-kernel stability and the parity input

## Verdict

The argument in `zero_kernel_harmonic.md` is correct after one citation is
made slightly more conservative.  Its only analytic input is the following
uniform parity lemma.

> **Prime-parity lemma.**  For every \(\eta>0\) there is
> \(c(\eta)>0\) such that, uniformly for sets of primes
> \(Q=Q_x\subseteq[2,x]\),
> \[
>  \sum_{p\in Q}\frac1p\geq\eta
>  \quad\Longrightarrow\quad
>  \frac1x\#\{n\leq x:\sum_{p\in Q}v_p(n)\equiv1\pmod2\}
>  \geq c(\eta)-o(1).
> \tag{1}
> \]

This lemma is a standard consequence of Hall's one-sided real
multiplicative mean theorem.  There is, however, no need to rely on a
leading-constant-one normalization of that theorem.  The ordinary uniform
Hall estimate with an absolute implied constant, combined with the
bounded-product sieve lemma already proved in
`zero_dim_sieve_compactness.md`, proves (1).  This removes the only
citation-normalization risk in the current draft.

## A robust proof of the parity lemma

Put
\[
 g_Q(n)=(-1)^{\sum_{p\in Q}v_p(n)},\qquad
 h(Q)=\sum_{p\in Q}\frac1p.
\]
Then \(g_Q\) is a real completely multiplicative function, and the density
on the left of (1) is
\[
 \frac{1-M_Q(x)}2,
 \qquad M_Q(x)=\frac1x\sum_{n\leq x}g_Q(n).             \tag{2}
\]

We use the standard one-sided form of Hall's real mean-value theorem: there
are absolute constants \(C<\infty\) and \(\kappa>0\) such that, uniformly
for every real multiplicative \(g\) with \(|g(n)|\leq1\),
\[
 \frac1x\sum_{n\leq x}g(n)
 \leq C\exp\!\left\{-\kappa
       \sum_{p\leq x}\frac{1-g(p)}p\right\}+o(1).       \tag{3}
\]
Only a one-sided estimate is required.  Any of the usual uniform error
terms in Hall's theorem is adequate here.  For \(g_Q\), (3) becomes
\[
 M_Q(x)\leq C e^{-2\kappa h(Q)}+o(1).                  \tag{4}
\]

Choose a fixed \(H_0=H_0(C,\kappa)\) so large that
\(Ce^{-2\kappa H_0}\leq1/2\).  If \(h(Q)>H_0\), (2)--(4)
give odd-parity density at least \(1/4-o(1)\).

It remains to treat
\[
 \eta\leq h(Q)\leq H_0.                               \tag{5}
\]
In this range
\[
 \prod_{q\in Q}\left(1-\frac1q\right)^{-1}
 \leq K_0,
 \tag{6}
\]
where \(K_0<\infty\) depends only on \(H_0\).  Indeed,
\(-\log(1-1/q)\leq1/q+O(1/q^2)\), and the sum of the
second terms over all primes is absolutely bounded.

Apply the bounded-product sieve lemma at the cutoff \(x/p\).  For every
\(p\in Q\), it gives
\[
 \#\{m\leq x/p:q\nmid m\text{ for every }q\in Q\}
 \geq c_{K_0}\frac{x}{p}.                              \tag{7}
\]
Each integer \(n=pm\) counted in (7) has exactly one \(Q\)-prime in its
factorization, with exponent one, and hence has odd \(Q\)-valuation
parity.  The sets obtained from distinct \(p\)'s are disjoint, because the
unique \(Q\)-prime dividing \(n\) recovers \(p\).  Summing (7) yields
\[
 \#\{n\leq x:\Omega_Q(n)\equiv1\pmod2\}
 \geq c_{K_0}x h(Q)
 \geq c_{K_0}\eta x.                                  \tag{8}
\]
Together with the large-mass case, this proves (1), with for example
\[
 c(\eta)=\min\{1/4,c_{K_0}\eta\}.                     \tag{9}
\]

The proof is pointwise uniform in the moving set \(Q_x\); no limiting
Euler product and no fixed-support assumption occurs.  Notice also that
the generic big-Oh Hall estimate alone does **not** justify the sharper
formula \((1-e^{-2\kappa\eta})/2\) for small \(\eta\).  Formula (9) is
all the zero-kernel proof needs.

## Audit of the 2-adic-layer reduction

Let
\[
 \delta_x=x^{-1}\#\{n\leq x:f_x(n)\neq0\}=o(1),
 \qquad P_x=\{p\leq x:f_x(p)\neq0\}.
\]

1.  The \(p\)-adic-chain argument gives
    \(\lfloor x/p\rfloor\leq\delta_xx\) for every
    \(p\in P_x\).  Hence
    \[
      \min P_x\geq \frac{x}{\delta_xx+1}\longrightarrow\infty.
    \tag{10}
    \]
    This is stronger than needed for the hybrid proof above, but it also
    validates any triangular-array version of Hall whose error is stated
    under \(\min Q_x\to\infty\).

2.  Clearing the finitely many denominators of \(f_x(p)\), \(p\leq x\),
    gives integer weights \(a_p\).  If the first 2-adic layer represented
    in \(n\) is \(j\), reduction of
    \(\sum_pa_pv_p(n)=0\) after division by \(2^j\) forces
    \(\sum_{p:v_2(a_p)=j}v_p(n)\) to be even.  Thus odd parity in that
    first layer certifies \(f_x(n)\neq0\).

3.  The elementary events used in the draft,
    \(E_j=\{T_{<j}=0,T_j=1\}\), are disjoint.  The pointwise inequality
    \[
      \mathbf1_{E_j}\geq T_j-2{T_j\choose2}-T_jT_{<j}
    \]
    is valid in every case.  Divisor counting therefore gives, for every
    finite layer prefix of harmonic mass \(h\),
    \[
      \delta_x\geq h-h^2-o(1),                         \tag{11}
    \]
    after discarding the \(o(1)\) set on which a represented prime occurs
    to exponent at least two.  The latter error is at most
    \(\sum_{p\in P_x}p^{-2}=o(1)\) by (10).

4.  Choose \(a>0\) below half the parity constant for harmonic mass
    \(1/2\), and stop at the first layer prefix of mass at least \(a\).
    If its mass is at most \(1-a\), (11) gives a fixed positive
    complement density.  Otherwise the final layer has mass greater than
    \(1-2a\geq1/2\); (1), after excluding the lower layers by the union
    bound, again gives a fixed positive complement density.  Both
    alternatives contradict \(\delta_x=o(1)\).

It follows that
\[
 H_x:=\sum_{p\leq x:f_x(p)\neq0}\frac1p=o(1).          \tag{12}
\]
Finally every \(x\)-smooth integer \(n\leq x^2\) with \(f_x(n)\neq0\)
is divisible by at least one active prime, so
\[
 \#\{n\leq x^2:P^+(n)\leq x,\ f_x(n)\neq0\}
 \leq x^2H_x=o(x^2).                                   \tag{13}
\]

Thus the zero-extension implication is valid for arbitrary moving rational
completely additive functions.  The proof does not extend unchanged to a
target group with 2-torsion; the rational/torsion-free hypothesis is used
when integer weights and their 2-adic layers are introduced.
