# Finite uniform anti-concentration: repair skeptic

## Verdict

The unconditioned independent-geometric prime model does **not** approximate
the valuation vector of a uniform integer in \([1,N]\) uniformly over
\(N\)-dependent additive functions.  The first invalid inference in such an
argument is the passage
\[
 (v_p(U_N))_{p\in P}\Longrightarrow (G_p)_{p\in P}
 \quad\hbox{for every fixed finite }P
\]
to the same assertion with a moving set \(P=P_N\), moving weights, and the
moving exact event \(\sum_{p\in P_N}w_{p,N}v_p=1\).  Everything after that
passage, including compound-Poisson anti-concentration for the product
model, may be correct and still say nothing about the uniform finite model.

This is not a merely technical lack of a rate.  There is an explicit bounded
\(0/1\)-weight family for which the relevant total-variation error stays
bounded away from zero and the uniform nonzero atom exceeds \(1/2\).

## An explicit escaping family

Let
\[
 P_N=\{p:\sqrt N<p\leq N\},\qquad
 w_{p,N}=\mathbf 1_{p\in P_N},
 \qquad f_N(n)=\sum_{p\in P_N}v_p(n).
\]
For every fixed prime \(p\), \(w_{p,N}=0\) for all sufficiently large \(N\).
Thus the weights converge coordinatewise to the zero grading; their entire
nonzero support escapes to infinity.

If \(n\leq N\), at most one prime in \(P_N\) divides \(n\), and it occurs to
the first power.  Consequently \(f_N(n)\in\{0,1\}\), and no integer is counted
twice in
\[
 \#\{n\leq N:f_N(n)=1\}
   =\sum_{\sqrt N<p\leq N}\left\lfloor\frac Np\right\rfloor.
\]
The prime-reciprocal Mertens theorem gives
\[
 \frac1N\#\{n\leq N:f_N(n)=1\}
 =\sum_{\sqrt N<p\leq N}\frac1p+o(1)
 =\log 2+o(1).                                      \tag{1}
\]
The floor error is \(O(\pi(N))=o(N)\).  In particular the exact nonzero
level has limiting density \(\log 2>1/2\).  As an exact level of a completely
additive function, it is a valid repetition-allowed PLR set.

Now replace the actual valuations on \(P_N\) by independent geometric
variables
\[
 \Pr(G_p=k)=(1-p^{-1})p^{-k}.
\]
Then
\[
 \Pr\left(\sum_{p\in P_N}G_p=1\right)
 =\prod_{p\in P_N}\left(1-\frac1p\right)
    \sum_{p\in P_N}\frac1p
 \longrightarrow \frac{\log 2}{2}.                  \tag{2}
\]
Indeed, the sum tends to \(\log2\), while taking logarithms of the product
shows that it tends to \(e^{-\log2}=1/2\); the quadratic remainder is
\(O(\sum_{p>\sqrt N}p^{-2})=o(1)\).  Equations (1)--(2) imply the quantitative
obstruction
\[
 d_{\rm TV}\!\left(
   \mathcal L((v_p(U_N))_{p\in P_N}),
   \bigotimes_{p\in P_N}\mathcal L(G_p)
 \right)
 \geq \frac{\log2}{2}-o(1).                          \tag{3}
\]
Thus neither bounded reciprocal mass
\(\sum_{p\in P_N}1/p\to\log2\) nor uniformly rare individual divisibility
\(\max_{p\in P_N}1/p\to0\) is enough for a Poisson/product approximation.
The missing dependence accumulates: under the uniform model two primes from
\(P_N\) can never occur together, whereas the sum of the product-model pair
probabilities tends to \((\log2)^2/2\).

The optimized local threshold family already recorded in
`../threshold_grading.md` makes the stress test stronger.  For
\(2<u<3\), take \(w_{p,N}=1\) on
\((N^{1/u},N]\) and zero elsewhere.  At \(u=1+\sqrt e\), its uniform
level-one mass tends to
\[
 c_*=0.828499\ldots,
\]
whereas the independent-geometric level-one mass tends to
\[
 \frac{\log u}{u}=0.367\ldots.
\]
Therefore any proposed universal uniform bound of \(1/2+o(1)\), or any
claim of \(o(1)\) product-model error based only on small marginals and
bounded reciprocal mass, is decisively false.

This example also defeats a coordinatewise compactness argument.  Although
\(w_{p,N}\to0\) for every fixed \(p\), the level-one masses do not converge
to the level-one mass of the zero grading.  Exact fibers are not continuous
under coordinatewise convergence when mass and support escape through
larger primes.

## What a product-model argument can legitimately prove

There is a useful quantitative repair when the active valuation vector has
controlled CRT complexity.  It also pinpoints exactly what the escaping
example violates.

**CRT truncation lemma.**  Let \(P\) be a finite set of primes supporting a
completely additive function
\(f(n)=\sum_{p\in P}w_pv_p(n)\), and choose integers \(K_p\geq1\).  Put
\[
 M=\prod_{p\in P}p^{K_p},\qquad
 \tau=\sum_{p\in P}p^{-(K_p+1)}.
\]
For every \(c\ne0\),
\[
 \Pr_{n\leq N}(f(n)=c)
 \leq \frac12+\min\left(1,\frac{M}{4N}\right)+2\tau. \tag{4}
\]

To prove this, set \(T_p=\min(v_p,K_p)\).  The vector \((T_p)_{p\in P}\)
is determined by the residue class modulo \(M\).  The distribution modulo
\(M\) of a uniform integer in \([1,N]\) is within
\[
 \frac{r(M-r)}{MN}\leq\min\left(1,\frac M{4N}\right),
 \qquad r=N\bmod M,
\]
in total variation of the uniform distribution on \(\mathbb Z/M\mathbb Z\).
Under the latter distribution, CRT makes the \(T_p\)'s independent and gives
them the same laws as \(\min(G_p,K_p)\) for independent geometric \(G_p\)'s.
The full and truncated vectors differ with probability at most \(\tau\) in
each model.  Finally, the compound-Poisson atom lemma bounds the nonzero atom
of \(\sum w_pG_p\) by \(1/2\), proving (4).

Hence a correct restricted conclusion is
\[
 M=o(N),\quad \tau=o(1)
 \quad\Longrightarrow\quad
 \sup_{c\ne0}\Pr_{n\leq N}(f(n)=c)\leq\frac12+o(1). \tag{5}
\]
One may also discard active primes outside \(P\) if the probability that any
of them divides \(U_N\) is \(o(1)\).  Fixed finite support is the simplest
case of (5).  The moving window above fails (5) spectacularly: taking even
one bit from every active prime makes \(M=\prod_{p\in P_N}p\) enormous.

Thus (4) repairs the logical inference but cannot settle the density-one
question.  In fact the active-prime chain lemma shows that every hypothetical
asymptotically full fiber must leave every fixed prime behind, precisely the
regime excluded by CRT tightness.

## Weakest useful repair for the density-one problem

The finite problem does not require a \(1/2\) bound, or even a fixed positive
density gap.  The existing chain lemma reduces it to a substantially weaker
rough-support statement.

It would suffice to prove the following.

**Rough-support deficit lemma (target).**  There are constants
\(\delta>0\) and \(y_0\) such that, uniformly in \(N\geq y\geq y_0\), every
rational completely additive \(f\) satisfying \(f(p)=0\) for all primes
\(p\leq y\), and every \(c\ne0\), obeys
\[
 \#\{n\leq N:f(n)\ne c\}
 \geq (1+\delta)\frac Ny-o(N/y).                     \tag{6}
\]
Here \(o(N/y)\) is as \(y\to\infty\), uniformly over \(N\geq y\), the
weights, and the target; a fixed-\(y\) asymptotic is not enough.

Indeed, let a level have complement size \(m=o(N)\), and set
\[
 Y=\left\lfloor\frac{N}{m+1}\right\rfloor.
\]
The active-prime chain bound forces \(f(p)=0\) for every \(p\leq Y\).  Since
\(Y\to\infty\), (6) would give
\[
 m\geq(1+\delta-o(1))\frac N Y
   \geq(1+\delta-o(1))(m+1),
\]
a contradiction.  The scale \(N/y\) is the self-consistency threshold: a
bound with leading constant only \(1\) merely reproduces the chain scale and
does not close the argument.  Thus (6), with any uniform improvement over
that constant, is a much weaker and more accurately targeted repair than a
universal constant-gap anti-concentration theorem.

The escaping threshold examples do not contradict (6): their complements
are of order \(N\), while \(N/y=o(N)\).  On the other hand, (6) cannot be
obtained by replacing the uniform valuation law with unconditioned
geometric variables.  It must retain the factor-size budget
\(\sum_pv_p(n)\log p\leq\log N\), for example through an exact
largest-prime/Buchstab-type decomposition or an explicitly conditioned
divisor-box model.

## Route disposition and falsification tests

1. Reject any step that upgrades fixed-cylinder convergence to a moving
   active support without an event-uniform error.  The family above is an
   explicit counterexample, not just a warning.
2. Reject claims that bounded \(\sum 1/p\), \(\max 1/p=o(1)\), or pairwise
   small errors imply a product approximation.  The accumulated forbidden
   pairs have constant mass.
3. The zeta measure does not become flat on \([1,N]\) for any \(s>1\): the
   weights at \(1\) and \(N\) differ by the factor \(N^s\).  The proved
   rearrangement consequence is valid, but treating it as a near-uniform
   transfer is another invalid inference.
4. Retain the CRT lemma as a valid restricted result and use (6), not a
   false \(1/2+o(1)\) assertion, as the next finite bottleneck.  A proposed
   proof of (6) should first be tested on every threshold
   \(w_{p,N}=\mathbf1_{p>N^{1/u}}\), since these are the simplest instances
   where the size constraint creates macroscopic dependence.

## Follow-up: the exact rough-support bottleneck and what sieve can prove

### 1. Correct minimal quantifiers

The fixed-gain statement (6) is sufficient, but it is stronger than the
cleanest self-consistent target.  Define
\[
 D_{f,c}(N)=\#\{n\leq N:f(n)\ne c\}.
\]
The exact target is the following sequential assertion.

> **(Rough).**  For every sequence \(N_j\to\infty\), \(y_j\to\infty\),
> rational completely additive functions \(f_j\) satisfying
> \(f_j(p)=0\) for all primes \(p\leq y_j\), and targets \(c_j\ne0\), if
> \(D_{f_j,c_j}(N_j)=o(N_j)\), then eventually
> \[
> D_{f_j,c_j}(N_j)\geq
> \left\lfloor\frac{N_j}{y_j}\right\rfloor.          \tag{R}
> \]

Only the instances in which \(y_j\) is selected from the deficit are needed.
Indeed, suppose a full fiber has deficit \(d=o(N)\), and put
\[
 Y=\left\lfloor\frac{N}{d+1}\right\rfloor.
\]
The active-prime chain bound forces \(f(p)=0\) for every \(p\leq Y\), while
\[
 \left\lfloor\frac N Y\right\rfloor\geq d+1.         \tag{21}
\]
Applying (R) with \(y=Y\) gives \(d\geq d+1\), a contradiction.

This corrects a nuance in the discussion after (6): a **merely
asymptotic** lower bound \((1-o(1))N/y\) does not close the argument, because
its error can be much larger than the one-integer gap in (21).  But the
exact floor bound with leading constant \(1\) does close it.  Statement (6),
or any fixed multiplicative gain over \(N/y\), is an analytically robust
way to prove (R), not the logically minimal formulation.

The conditions \(y\to\infty\) and \(D=o(N)\) are part of the target.  Without
them, (R) is false as a pointwise statement for arbitrary smaller choices of
\(y\).  For example, the exact \(N=60\) optimizer in `modal_compute.md` has
weights zero at \(2,3\), weights one from \(5\) onward, and deficit \(21\).
It satisfies the bound at \(y=3\), since \(21\geq20\), but the same function
also vanishes at all primes \(p\leq2\) and does not have deficit
\(\lfloor60/2\rfloor\).  This finite example is outside the sequential
near-full regime and shows why the quantifiers cannot be suppressed.

### 2. Exact rough-kernel formulation

Every \(n\leq N\) has a unique factorization
\[
 n=ab,\qquad P^+(a)\leq y,\qquad P^-(b)>y,           \tag{22}
\]
where \(b=1\) is allowed.  Since \(f(a)=0\), membership in a fiber depends
only on the \(y\)-rough kernel \(b\).  Consequently
\[
 D_{f,c}(N)=
 \sum_{\substack{b\leq N,\ P^-(b)>y\\ f(b)\ne c}}
       \Psi(N/b,y).                                  \tag{23}
\]
This is an exact smooth/rough, or Buchstab-type, reformulation of (R).  The
term \(b=1\) gives the familiar lower bound
\[
 D_{f,c}(N)\geq\Psi(N,y).                            \tag{24}
\]

Equation (23) identifies what a successful Buchstab argument must retain:
the same prime labels \(w_p\) color rough kernels at every scale.  If those
colors are discarded, Buchstab decomposition is only a partition of the
integer count and supplies no fiber deficit beyond (24).

### 3. Tests against threshold gradings

For the optimized fixed-power threshold in `../threshold_grading.md`,
\[
 y=N^{1/u},\qquad f(n)=\Omega_{>y}(n),qquad 2<u<3,
\]
the deficit is
\[
 D_{f,1}(N)=(1-c(u)+o(1))N,
\]
where \(c(u)=2-2\rho(u)-\log u<1\).  Hence
\[
 \frac{D_{f,1}(N)}{N/y}
 =(1-c(u)+o(1))y\longrightarrow\infty.               \tag{25}
\]
At \(u=1+\sqrt e\), this ratio is
\((0.171500\ldots+o(1))N^{1/(1+\sqrt e)}\).  Thus the
best known threshold construction is very far from falsifying (R).

The same conclusion holds for **every** moving one-threshold family, not
only fixed \(u\), using a simple two-case argument.  Put
\[
 K(n)=\sum_{y<p\leq N}\mathbf1_{p\mid n},qquad
 H=\sum_{y<p\leq N}\frac1p,qquad
 \mu=\mathbb E K(U_N).
\]
The floor errors and the prime number theorem give
\[
 0\leq H-\mu\leq\frac{\pi(N)}N=O(1/\log N),           \tag{26}
\]
and
\[
 \mathbb E[K(K-1)]
 =\sum_{\substack{p,q>y\\p\ne q}}
   \frac1N\left\lfloor\frac N{pq}\right\rfloor
 \leq H^2.
\]
It follows that
\[
 \operatorname{Var}K\leq H+o(1).                    \tag{27}
\]
If \(H\to\infty\), Chebyshev gives
\[
 \Pr(K=1)\leq\frac{H+o(1)}{(\mu-1)^2}=O(1/H)=o(1).
\]
Since \(\Omega_{>y}(n)=1\) implies \(K(n)=1\), the threshold deficit is
\((1-o(1))N\), much larger than \(N/y\).

If \(H\) stays bounded, prime-reciprocal Mertens gives
\[
 H=\log\left(\frac{\log N}{\log y}\right)+o(1).
\]
Thus \(\log N/\log y\leq U\) for some fixed \(U\), and
\(y\geq N^{1/U}\).  The fixed-\(U\) Dickman theorem then gives
\[
 D_{f,1}(N)\geq\Psi(N,y)
 \,\geq\Psi(N,N^{1/U})=(\rho(U)+o(1))N.              \tag{28}
\]
Again this is much larger than \(N/y\).  Equations (26)--(28) therefore
certify the whole one-threshold class against (R), including the slowly
moving regimes not covered by a single fixed-\(u\) asymptotic.

### 4. Tests against multi-band weights

Consider any fixed-power multi-band grading: for fixed
\(0<\alpha<1\), all nonzero prime weights occur above
\(y=N^\alpha\), with arbitrary rational values and arbitrary further band
boundaries.  Every \(y\)-smooth integer has value zero, so for every nonzero
target
\[
 D_{f,c}(N)\geq
 \Psi(N,N^\alpha)=(\rho(1/\alpha)+o(1))N
 \gg \frac N y.                                     \tag{29}
\]
Thus adding finitely many fixed power-scale bands, changing signs, or using
nonbinary weights cannot threaten (R).  The only relevant multi-band stress
test has its lowest active scale \(y=N^{o(1)}\), where the smooth kernel can
be smaller than \(N/y\), and has band boundaries and weights moving with
\(N\).

The exact small computation gives no counterexample in that regime.  Its
nonbinary \(N=9\) optimizer has \(w_2,w_3\ne0\), so it does not satisfy an
expanding zero-weight prefix.  The \(N=60\) optimizer discussed above is a
single threshold rather than a genuine asymptotic multi-band escape.

There is nevertheless a sharp warning from the abstract scale cuts in
`finite_overlap.md`.  At the model cutoff \(y=\log N\), one Ferrers
prime--cofactor cut costs
\[
 \left(\frac1{1-\theta}+o(1)\right)\frac N{\log N},
\]
which is exactly the order \(N/y\), and its leading constant approaches
\(1\) as \(\theta\downarrow0\).  Those abstract row colors are not known to
come from one completely additive function, so this is not a counterexample.
It does show that graph connectivity or uncolored band counting cannot be
expected to prove a substantially larger deficit without using the global
additive coupling of the bands.

### 5. What ordinary sieve proves, and its exact failure point

Let
\[
 S=\{p\leq N:w_p\ne0\},\qquad H_S=\sum_{p\in S}\frac1p.
\]
Every member of a nonzero fiber is divisible by a prime in \(S\).  The
union bound therefore gives the genuine easy range
\[
 D_{f,c}(N)
 \geq N-\sum_{p\in S}\left\lfloor\frac Np\right\rfloor
 \geq N(1-H_S).                                     \tag{30}
\]
In particular, (R) holds whenever \(H_S\leq1-1/y\).

A support-only lower-bound sieve tries to improve (30) by counting integers
with no prime factor in \(S\).  That cannot prove (R) in the hard range.  To
see this with an explicit scale, take
\[
 y=\lceil\log N\rceil,qquad S=\{p:y<p\leq N\}.
\]
The integers avoiding \(S\) are exactly the \(y\)-smooth integers, and
Rankin's bound at exponent \(1/2\) gives
\[
 \Psi(N,y)
 \leq N^{1/2}\prod_{p\leq y}(1-p^{-1/2})^{-1}
 \leq N^{1/2}\exp(O(\sqrt y))
 =N^{1/2+o(1)}
 =o(N/y).                                            \tag{31}
\]
Thus neither the zero-weight kernel nor an ordinary prime-avoidance sieve
reaches the required scale.  This is a limitation of the method, not a
counterexample to (R): for the equal-weight threshold, (27) shows that the
many nonsmooth off-level integers supply the missing deficit.

Plain Buchstab iteration does not fix this.  Applied to (23) without the
condition \(f(b)\ne c\), it counts all rough kernels and reconstructs \(N\).
Keeping only \(b=1\) reproduces the inadequate bound (31).  Keeping the
condition requires a uniform estimate for a rationally colored affine slice
of the rough kernels,
\[
 \sum_{\substack{b\leq N,\ P^-(b)>y\\f(b)=c}}
       \Psi(N/b,y)
 \leq N-\left\lfloor\frac Ny\right\rfloor,           \tag{32}
\]
which is exactly the missing additive anti-concentration assertion, not a
standard sieve consequence.

One possible conditional package is the dichotomy isolated in
`finite_uniform.md`: a bounded-harmonic prime-avoidance theorem (PA), plus a
triangular-array Kubilius--Littlewood--Offord theorem (UKLO) when
\(H_S\to\infty\).  PA is plausibly sieve/Buchstab in nature.  UKLO is not;
it must control the common rational labels and their cancellations across
all moving bands.  Together they would give a constant deficit and hence
far more than (R), but neither should be silently cited without a precise
uniform theorem.

**Conclusion.**  Sieve/Dickman/Buchstab estimates prove (R) for fixed-power
thresholds and multi-band gradings, and the elementary second-moment argument
proves it for every one-threshold escape.  An ordinary support-only sieve
does not prove (R) in the decisive \(y=N^{o(1)}\) multi-band regime, as
(31) shows.  The weakest surviving task is a colored rough-kernel or
cross-band concentration estimate; calling the exact identity (23) a
Buchstab argument does not supply that estimate.
