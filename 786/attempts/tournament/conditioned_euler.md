# Conditioned Euler and divisor-box measures: a flatness/acceptance obstruction

## Verdict

The natural conditioned-product implementation of the compound-Poisson idea
cannot give a uniform finite density gap. There is a sharp conflict between
the two properties that the transfer needs:

1. the unconditioned product law must assign probability \(>1/2+\eta\) to
   \([1,N]\), so that the universal nonzero-atom bound \(1/2\) remains
   nontrivial after conditioning; and
2. the conditional law on \([1,N]\) must not put nonvanishing mass on an
   \(o(N)\)-element set, so that uniform density \(1-o(1)\) implies
   conditional probability \(1-o(1)\).

For the canonical power-Euler family these requirements are mutually
exclusive. If the conditional law is \(O(1/N)\)-flat, the acceptance
probability tends to zero exponentially in \(N/\log N\). If the acceptance
probability is bounded below, the conditional law instead puts \(1-o(1)\)
of its mass on \([1,N/\log N]\), an \(o(N)\)-element set. Uniform divisor
boxes have the same acceptance obstruction.

This is a precise impossibility result for the canonical conditioned Euler,
two-sided-flat independent-coordinate, full divisor-box, and fully contained
active-box schemes. It is **not** an impossibility theorem for every
nonstationary product law: a law which is only one-sided/uniformly
integrable, suppresses individual large primes, and compensates on
composites is not ruled out here.

## What a transfer measure would have to do

Let
\[
 f(n)=\sum_{p\leq N}w_pv_p(n),\qquad c\ne0,
\]
and let \(X\) have independent geometric prime exponents. Then \(f(X)\) is
a zero-drift compound-Poisson variable (finite prime support suffices), so
\[
 \Pr(f(X)=c)\leq \frac12. \tag{1}
\]
Put \(E_N=\{X\leq N\}\), \(\alpha_N=\Pr(E_N)\), and
\(\nu_N=\mathcal L(X\mid E_N)\). For the exact level
\(A_N=\{n\leq N:f(n)=c\}\), (1) gives
\[
 \nu_N(A_N)\leq \frac{1}{2\alpha_N}. \tag{2}
\]
Thus this argument can give a fixed gap only if
\(\liminf\alpha_N>1/2\). To turn (2) into a statement about uniform
cardinality, it is enough, and for arbitrary exceptional sets necessary,
that
\[
 |B_N|=o(N)\quad\Longrightarrow\quad \nu_N(B_N)=o(1). \tag{UI}
\]
The stronger hypothesis
\(\max_{n\leq N}\nu_N(n)\leq K/N\) implies (UI).

## The canonical power-Euler family

Fix \(s=s_N>0\). For every prime \(p\leq N\), independently choose
\[
 \Pr(V_p=k)=(1-p^{-s})p^{-sk}\quad(k\geq0),
 \qquad X=\prod_{p\leq N}p^{V_p}. \tag{3}
\]
Every integer \(n\leq N\) has all its prime factors in this product, and
\[
 \Pr(X=n)=C_N(s)n^{-s},\qquad
 C_N(s)=\prod_{p\leq N}(1-p^{-s}).
\]
Consequently
\[
 \nu_{N,s}(n)=\frac{n^{-s}}{H_N(s)},\qquad
 H_N(s)=\sum_{m\leq N}m^{-s},                         \tag{4}
\]
and
\[
 \alpha_N(s)=C_N(s)H_N(s).                            \tag{5}
\]

### Proposition 1 (flatness forces vanishing acceptance)

Suppose that for some fixed \(K\), along an unbounded sequence of \(N\),
\[
 \max_{n\leq N}\nu_{N,s_N}(n)\leq \frac K N.          \tag{6}
\]
Then \(s_N\log N=O_K(1)\), and
\[
 \alpha_N(s_N)\leq (1+K_N)(1-q_0)^{K_N}=o(1),         \tag{7}
\]
where \(K_N=\pi(N)-\pi(N/2)\sim N/(2\log N)\) and one
may take \(q_0=(2K)^{-2}\) for all sufficiently large \(N\).

#### Proof

The maximum in (4) is \(1/H_N(s)\). Hence (6) says
\(H_N(s)\geq N/K\). Splitting the sum at \(\sqrt N\) gives
\[
 H_N(s)\leq \sqrt N+N(\sqrt N)^{-s}.
\]
For large \(N\), this forces
\[
 e^{-s\log N/2}\geq \frac1{2K},
 \qquad s\log N\leq2\log(2K).                         \tag{8}
\]

Now consider the primes \(p\in(N/2,N]\). If \(X\leq N\), at most one of
their exponents is nonzero, and that exponent must equal \(1\). Writing
\(q_p=p^{-s}\), independence gives the exact probability of this necessary
large-prime event:
\[
 \prod_{N/2<p\leq N}(1-q_p)
 \left(1+\sum_{N/2<p\leq N}q_p\right).                \tag{9}
\]
By (8), \(q_p\geq N^{-s}\geq q_0\), while the sum in parentheses is at
most \(1+K_N\). Equation (9) is at most the right side of (7), which tends
to zero by the prime number theorem. Since \(E_N\) is contained in this
large-prime event, (7) follows. \(\square\)

The proof gives exponential decay
\(\exp(-\Omega_K(N/\log N))\), up to the displayed polynomial factor.
Conditioning can make (4) flat, but it divides the bound \(1/2\) in (2) by
an acceptance probability tending rapidly to zero.

### Proposition 2 (nonvanishing acceptance destroys uniform integrability)

Fix \(\eta>0\). If
\[
 \alpha_N(s_N)\geq\eta,                               \tag{10}
\]
along an unbounded sequence, then
\[
 s_N\geq1-\frac{\log\log N+O_\eta(1)}{\log N}.         \tag{11}
\]
For \(M_N=\lfloor N/\log N\rfloor=o(N)\), one then has
\[
 \nu_{N,s_N}([1,M_N])=1-o_\eta(1).                    \tag{12}
\]
In particular, (UI) fails in the strongest possible way.

#### Proof

Let
\[
 \Lambda_N=\sum_{N/2<p\leq N}p^{-s_N}.
\]
From (9) and \(1-x\leq e^{-x}\),
\[
 \alpha_N(s_N)\leq e^{-\Lambda_N}(1+\Lambda_N).       \tag{13}
\]
The right side decreases from \(1\), so (10) implies
\(\Lambda_N=O_\eta(1)\). The prime number theorem and
\(p^{-s_N}\geq N^{-s_N}\) give
\[
 \Lambda_N\geq K_NN^{-s_N}
 \gg \frac{N^{1-s_N}}{\log N},
\]
so there is a fixed \(C_\eta\) for which
\[
 s_N\geq1-\frac{\log\log N+C_\eta}{\log N}.
\]
This proves (11).

Write
\[
 \delta_N=\frac{\log\log N+C_\eta}{\log N},
 \qquad s_0=1-\delta_N,
\]
enlarging \(C_\eta\) once if needed. Then \(s_N\geq s_0\). The probability of an
initial interval under weights \(n^{-s}\) is nondecreasing in \(s\). This
follows from the monotone likelihood ratio, or by differentiating and using
\(\operatorname{Cov}(1_{n\leq M},\log n)\leq0\). It is enough to check
(12) at \(s=s_0\).

Integral comparison for the decreasing function
\(x^{-1+\delta_N}\) yields
\[
 \frac{\sum_{M_N<n\leq N}n^{-1+\delta_N}}
      {\sum_{n\leq N}n^{-1+\delta_N}}
 \leq
 \frac{(N^{\delta_N}-M_N^{\delta_N})/\delta_N
       +M_N^{-1+\delta_N}}
      {(N^{\delta_N}-1)/\delta_N}.                    \tag{14}
\]
Here \(N^{\delta_N}\asymp_\eta\log N\to\infty\), and
\[
 1-\left(\frac{M_N}{N}\right)^{\delta_N}
 =1-\exp(-\delta_N\log\log N)
 =O_\eta\!\left(\frac{(\log\log N)^2}{\log N}\right)=o(1).
\]
The extra term in (14) is also \(o(1)\) after division by the denominator.
Thus the tail in (14) is \(o(1)\), proving (12). \(\square\)

### Corollary (complete no-go for this family)

No choice of \(s_N>0\) in (3) simultaneously has
\[
 \liminf_N\alpha_N(s_N)>\frac12
 \quad\text{and}\quad
 \{|B_N|=o(N)\Rightarrow\nu_{N,s_N}(B_N)=o(1)\}.
\]
At the critical choice \(s=1\), standard Mertens estimates give
\[
 \alpha_N(1)=
 \left(\prod_{p\leq N}(1-1/p)\right)H_N(1)
 \longrightarrow e^{-\gamma}>\frac12,
\]
but
\[
 \nu_{N,1}([1,N/\log N])\longrightarrow1.
\]
This sits exactly on the acceptance side of the dichotomy and explains why
harmonic/Dirichlet mass cannot see a deletion of \(N/\log N\) small
integers.

## A general large-prime obstruction to two-sided-flat products

The large-prime argument does not depend on geometric laws.

### Proposition 3

For every \(p\in(N/2,N]\), let \(V_p\) be an independent nonnegative
integer random variable; allow arbitrary additional independent prime
coordinates and assume their product is well-defined. Put
\(X=\prod p^{V_p}\), \(E_N=\{X\leq N\}\), and suppose
\(\Pr(E_N)>0\). If the conditional law satisfies, for one fixed \(K\),
\[
 \frac1{KN}\leq\Pr(X=n\mid E_N)\leq\frac K N
 \qquad(1\leq n\leq N),                               \tag{15}
\]
then
\[
 \Pr(E_N)\leq
 (1+K^2K_N)(1+K^{-2})^{-K_N}=o(1).                   \tag{16}
\]

#### Proof

Set \(a_p=\Pr(V_p=0)\), \(b_p=\Pr(V_p=1)\), and
\(r_p=b_p/a_p\). Condition (15) makes these quantities positive and,
because conditioning cancels in a point-probability ratio,
\[
 r_p=\frac{\Pr(X=p\mid E_N)}{\Pr(X=1\mid E_N)}
 \in[K^{-2},K^2].                                    \tag{17}
\]
The event \(E_N\) permits only the all-zero pattern or a single exponent
equal to \(1\) on this prime slab. Hence
\[
 \Pr(E_N)\leq\left(\prod_pa_p\right)
                    \left(1+\sum_pr_p\right).         \tag{18}
\]
Since \(a_p+b_p\leq1\), we have
\(a_p\leq(1+r_p)^{-1}\leq(1+K^{-2})^{-1}\). Combining
this with (17) and (18) proves (16). \(\square\)

This rules out genuine two-sided pointwise flattening for any
independent-prime-exponent law with useful acceptance. It deliberately does
not replace the lower bound in (15) by (UI): the large primes themselves
are only \(o(N)\) points, and a uniformly-integrable candidate may suppress
them.

## Uniform divisor boxes

Let
\[
 L_N=\operatorname{lcm}(1,2,\ldots,N)
     =\prod_{p\leq N}p^{\lfloor\log_pN\rfloor},
\]
and choose a divisor of \(L_N\) uniformly, equivalently choosing every prime
exponent independently and uniformly in its allowed interval. All
\(n\leq N\) are divisors and have the same unconditioned probability, so
the conditional law given \(X\leq N\) is exactly uniform. Moreover, if a
prime weight in the box is nonzero, conditioning on all other coordinates
shows
\[
 \Pr(f(X)=c)\leq\frac12.                              \tag{19}
\]
Thus this is the flattest possible product candidate. Nevertheless, on the
\(K_N\) primes in \((N/2,N]\), all exponent boxes are \(\{0,1\}\), and
\(X\leq N\) allows at most one \(1\). Therefore
\[
 \Pr(X\leq N)\leq\frac{K_N+1}{2^{K_N}}=o(1).          \tag{20}
\]
Indeed, since every \(n\leq N\) is a divisor,
\[
 \Pr(X\leq N)=\frac{N}{\tau(L_N)}.
\]
The same argument applies to any uniform divisor box containing every
integer in \([1,N]\): every \(p\in(N/2,N]\) must have exponent states
\(0,1\), and larger exponent ranges only decrease the acceptance bound in
(20).

## Fully contained active boxes multiplied by kernel integers

There is a second natural attempt specific to a dense grading. If all
weights below \(y\) vanish, choose a rectangular box on active primes
\(p\geq y\), multiply it independently by an arbitrary integer supported on
zero-weight primes, and require the whole support to lie in \([1,N]\). This
preserves the product anti-atom bound without conditioning, but its support
is too sparse.

Precisely, let
\[
 M=\prod_{p\in S}p^{E_p},\qquad E_p\geq1,\quad p\geq y,
\]
and let \(B\) be the full divisor box of \(M\), so
\(|B|=\prod_{p\in S}(E_p+1)\). If an independent multiplier \(D\) is
supported in \([1,N/M]\), then every product \(bD\) lies in \([1,N]\), but
\[
 |\operatorname{supp}(bD)|
 \leq |B|\frac NM
 =N\prod_{p\in S}\frac{E_p+1}{p^{E_p}}
 \leq N\prod_{p\in S}\frac2p
 \leq\frac{2N}{y}.                                   \tag{21}
\]
Here \(E+1\leq2^E\leq2p^{E-1}\) for \(p\geq2\). Thus, once the
active-prime chain lemma gives \(y\to\infty\), every nontrivial fully
contained active box is supported on \(o(N)\) integers and fails (UI).
Allowing the multiplier range to depend on the selected box element amounts
to conditioning and returns to the acceptance problem.

## A useful reformulation of the remaining gap

Condition (UI) has a strong consequence on logarithmic scale. For every
sequence \(T_N\to\infty\),
\[
 B_N=[1,\lfloor Ne^{-T_N}\rfloor]
\]
has size \(o(N)\), and hence
\[
 \nu_N(B_N)=o(1).                                    \tag{22}
\]
If also \(\alpha_N>1/2+\eta\), then
\[
 \Pr(Ne^{-T_N}<X\leq N)
 =\alpha_N(1-o(1))>\frac12+\frac\eta2                \tag{23}
\]
for all sufficiently large \(N\). Thus any surviving independent-exponent
candidate must place more than half of its unconditioned mass in a
multiplicative shell immediately below \(N\), even when the logarithmic
width \(T_N\) tends to infinity arbitrarily slowly, while distributing that
mass over \(\Omega(N)\) integers. Deterministic or low-dimensional products
can satisfy the shell condition but fail diffusion; the power-Euler family
has enough diffusion but fails the shell condition.

This isolates a plausible missing theorem: an entropy/concentration
inequality saying that a product of independent prime-power coordinates
cannot simultaneously have the shell mass (23) and conditional diffusion
(UI). Such a theorem would close the product-measure route in full.

## Dependency chain and surviving gap

The route's exact chain is:

1. An independent geometric Euler law gives
   \(\Pr(f(X)=c)\leq1/2\) for \(c\ne0\).
2. Conditioning on \(X\leq N\) changes this to (2), so useful transfer
   needs acceptance \(>1/2+\eta\) and (UI).
3. For the power-Euler family, Proposition 1 rules out flatness with useful
   acceptance, while Proposition 2 rules out even (UI) whenever acceptance
   is nonvanishing.
4. Proposition 3 rules out two-sided-flat conditioning for arbitrary
   independent exponent laws.
5. Full uniform divisor boxes and fully contained active boxes fail by
   (20) and (21).

The weakest unsupported step for a broader impossibility theorem is:

> Prove that every independent-exponent law with
> \(\Pr(X\leq N)>1/2+\eta\) fails (UI), without assuming power weights or a
> pointwise lower bound.

Proposition 3 cannot do this because a candidate may give negligible mass
to every prime in \((N/2,N]\), which is itself only an \(o(N)\)-sized set,
and compensate on a positive-density family of composites. A proof would
need a multi-slab or entropy-energy inequality, not another single-slab
estimate.

## Concrete falsification test and next action

Any proposed conditioned-product repair should report all three quantities
\[
 \alpha_N=\Pr(X\leq N),\qquad
 U_N(m)=\max_{|B|\leq m}\Pr(X\in B\mid X\leq N),
 \qquad \Pr(f(X)=c).
\]
It survives this obstruction only if, for some fixed \(\eta>0\),
\[
 \alpha_N>\frac12+\eta,\qquad
 U_N(m_N)=o(1)\ \text{for every }m_N=o(N),\qquad
 \Pr(f(X)=c)\leq\frac12.
\]
Testing only point masses or only \(\alpha_N\) is insufficient. The next
viable action is to seek the multi-slab theorem in the displayed open step.
Conversely, a counterexample to that statement would be exactly the
non-power, large-prime-suppressing product measure that this route still
needs.
