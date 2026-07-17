# Conditioned Euler and divisor-box route: repair-oriented skeptic

## Verdict

The unconditioned Euler-product argument has a genuine nonzero-atom bound,
but no positive mixture of its zeta laws is even remotely flat on
\([1,N]\).  Conditioning, translating, or passing to a divisor box can make
the reference law flat, but each operation destroys exactly the hypothesis
that made the atom bound useful:

* conditioning divides the bound by the probability of the conditioning
  event;
* a multiplicative translate changes the target to zero on the dangerous
  components;
* an additive translate destroys complete additivity and prime
  independence;
* a divisor box containing almost all of \([1,N]\) has exponentially many
  points, so its order-ideal truncation has exponentially small probability.

Thus a flat positive Euler majorant is not a viable missing lemma.  A much
weaker, genuinely sufficient replacement is the order-ideal inequality (R)
in the last section.  It asks only for \(N/y\) exceptions, not for a fixed
positive density of exceptions.

Throughout, for rational prime weights \(w_p\), write
\[
 f(n)=\sum_p w_pv_p(n),\qquad F_c=\{n:f(n)=c\}.
\]
The proved zeta fact from `PROOF.md` is
\[
 \mu_s(F_c)\leq \frac12
 \quad(s>1,\ c\ne0),
 \qquad
 \mu_s(n)=\frac{n^{-s}}{\zeta(s)}. \tag{1}
\]

## 1. Positive zeta mixtures cannot approximate the uniform law

Let \(\Lambda\) be any probability measure on \((1,\infty)\), and put
\[
 Q(n)=\int_{(1,\infty)}\frac{n^{-s}}{\zeta(s)}\,d\Lambda(s).
\]
By positivity and (1), \(Q(F_c)\leq1/2\) for every \(c\ne0\).  The following
two estimates explain why this does not transfer to uniform counting.

### Lemma 1 (endpoint and dyadic-block obstruction)

For \(N>1\),
\[
 NQ(N)\leq\frac1{e\log N}. \tag{2}
\]
Moreover, uniformly over positive zeta mixtures,
\[
 Q([N,2N])=O\!\left(\frac1{\log N}\right). \tag{3}
\]

**Proof.**  The integral comparison
\(\zeta(s)\geq\int_1^\infty x^{-s}\,dx=1/(s-1)\) gives
\[
 N\mu_s(N)\leq (s-1)N^{1-s}
 =\frac{t e^{-t}}{\log N}\leq\frac1{e\log N},
 \qquad t=(s-1)\log N.
\]
Integration in \(s\) proves (2).  For (3), there are at most \(N+1\)
terms and each is at most \(N^{-s}/\zeta(s)\).  The same maximization,
with an immaterial absolute factor, gives (3). \(\square\)

Consequently, if one seeks a pointwise minorant
\(Q(n)\geq\alpha_N/N\) on \([1,N]\), then (2) forces
\[
 \alpha_N\leq\frac1{e\log N}. \tag{4}
\]
Such a minorant and (1) would give only
\(|F_c\cap[1,N]|/N\leq1/(2\alpha_N)\), which is vacuous.  Equation (3)
also shows directly that \(Q\) has total-variation distance at least
\(1/2-o(1)\) from the uniform law on \([1,N]\): the latter puts mass
\(1/2+o(1)\) on \([N/2,N]\), whereas \(Q\) puts \(o(1)\) there.

### Lemma 2 (conditioning on \([1,N]\) still does not flatten)

Let \(Q_N\) be any positive zeta mixture conditioned on \([1,N]\).  With
\(H_N=\sum_{n\leq N}1/n\) and \(T_N=[\lceil N/2\rceil,N]\),
\[
 Q_N(T_N)\leq
 \frac{\sum_{n\in T_N}1/n}{H_N}
 =\frac{\log2+o(1)}{\log N}, \tag{5}
\]
and
\[
 Q_N(N)\leq\frac1{NH_N}. \tag{6}
\]
In particular,
\[
 \|Q_N-U_N\|_{\rm TV}\geq\frac12-o(1), \tag{7}
\]
where \(U_N\) is uniform on \([1,N]\).

**Proof.**  Conditioning reweights the mixing measure and makes \(Q_N\) a
positive mixture of
\[
 q_{s,N}(n)=\frac{n^{-s}}{H_{N,s}},
 \qquad H_{N,s}=\sum_{m\leq N}m^{-s}.
\]
Relative to \(q_{1,N}\), this is a tilt by the decreasing function
\(n^{-(s-1)}\).  A decreasing tilt can only reduce the probability of the
upper interval \(T_N\), proving (5).  Also
\[
 H_{N,s}=\sum_{n\leq N}\frac1n n^{-(s-1)}
 \geq N^{-(s-1)}H_N,
\]
so \(q_{s,N}(N)\leq1/(NH_N)\); mixtures preserve this inequality.
Equation (7) follows from the event \(T_N\). \(\square\)

Thus neither unconditioned nor \([1,N]\)-conditioned positive mixtures can
be the desired flat comparison measure.  Signed Mellin inversion is not a
repair: positivity is what permits averaging the inequalities (1).

## 2. Moving the zeta parameter below one is not an Euler law

The truncated power law \(n^{-s}/H_{N,s}\) becomes close to uniform when
\(s\to0\), and at \(s=0\) it is exactly uniform.  This does not interpolate
the Euler-product proof.  For \(0<s\leq1\), if independent geometric prime
exponents have parameters \(p^{-s}\), then
\[
 \sum_p\Pr(v_p>0)=\sum_pp^{-s}.
\]
this diverges.  By independence and Borel--Cantelli,
infinitely many prime exponents are positive almost surely, so their product
is not a finite integer.  Equivalently, the compound-Poisson intensity
\(\sum_{p,k}p^{-ks}/k\) is infinite.  At \(s\leq0\), even the individual
``geometric parameter'' \(p^{-s}\) is not in \((0,1)\).  The boundary
\(s>1\) in (1) is therefore structural, not a removable analytic
inconvenience.

## 3. Shifts repair flatness only by losing the atom bound

There are two different shifts, and both fail for a precise reason.

### Multiplicative shifts

Let \(X\sim\mu_s\) and consider \(dX\).  Complete additivity gives
\[
 \Pr(f(dX)=c)=\Pr(f(X)=c-f(d)). \tag{8}
\]
The right side is bounded by \(1/2\) only when \(f(d)\ne c\).  If
\(f(d)=c\), the shifted target is zero, for which there is no universal
bound.  This is a real obstruction: take \(f=v_q\), \(d=q\), and \(c=1\).
Then
\[
 \Pr(f(qX)=1)=\Pr(q\nmid X)=1-q^{-s}, \tag{9}
\]
which can be arbitrarily close to one.

More generally, for a positive mixture of laws \(dX_s\), let \(\beta\) be
the mixing mass of components whose base satisfies \(f(d)=c\).  Splitting
the components in (8) yields only
\[
 Q(F_c)\leq\frac12+\frac\beta2. \tag{10}
\]
Controlling \(\beta\) uniformly is itself a fiber anti-concentration problem
for the base distribution.

Multiplicative shifts can indeed remove the flatness obstruction, which
shows why (10), rather than (1), is the decisive issue.  If \(D\) is uniform
on \([1,N]\) and \(X\sim\mu_s\) independently, then the law of \(DX\) is
within \(1-1/\zeta(s)\) in total variation of the law of \(D\), by coupling
on the event \(X=1\).  Taking \(s\to\infty\) makes it arbitrarily close to
uniform.  But then the bases in \(F_c\) contribute precisely to \(\beta\),
and (10) reduces asymptotically to
\(x\leq(1+x)/2\), which gives only \(x\leq1\).

### Additive shifts

A kernel proportional to \((n+h)^{-s}\) can be made nearly flat on a short
interval by taking \(h\) large, but \(f(n+h)\) has no additive relation to
\(f(n)\), and the prime valuations are no longer the Euler-independent
coordinates used in (1).  There cannot be an inherited atom theorem: with
\(f=v_q\), \(h=q-1\), and \(X\sim\mu_s\),
\[
 \Pr(f(X+h)=1)\geq\Pr(X=1)=\frac1{\zeta(s)}\longrightarrow1
 \quad(s\to\infty). \tag{11}
\]

## 4. Conditioning has an unavoidable mass denominator

For any probability law \(Q\), event \(B\) of mass \(b>0\), and fiber with
\(Q(F_c)\leq1/2\), the only unconditional consequence is
\[
 Q(F_c\mid B)\leq\min\!\left(1,\frac1{2b}\right). \tag{12}
\]
Hence conditioning preserves a nontrivial gap only when \(b\) is bounded
away from \(1/2\) on the upper side.  Regions on which a zeta density is
approximately flat live at one large scale, but Lemma 1 gives them mass
\(O(1/\log N)\).  Conditioning on such a region makes (12) vacuous.  On the
other hand, conditioning on \([1,N]\) can have large mass, but Lemma 2 shows
that its conditional law remains logarithmic rather than uniform.  This is
the flatness-versus-mass tradeoff that a conditioning argument must overcome;
conditioning by itself does not do so.

## 5. Divisor boxes: exact product structure, exponentially rare truncation

For a finite prime set \(P\) and caps \(L_p\geq1\), let
\[
 \mathcal B(P,L)=
 \left\{\prod_{p\in P}p^{e_p}:0\leq e_p\leq L_p\right\},
\]
and choose \(D\) uniformly from this box.  The exponents are independent
uniform variables.  If some \(w_p\ne0\), conditioning on all other
exponents shows that the equation \(f(D)=c\) permits at most one value of
\(e_p\).  Therefore
\[
 \Pr(f(D)=c)\leq\frac1{L_p+1}\leq\frac12. \tag{13}
\]
If all box coordinates have weight zero, the probability is zero for
\(c\ne0\).  Thus the unconditioned box has an even simpler atom proof than
the zeta law.

Now take
\[
 M_N=\operatorname{lcm}(1,2,\ldots,N),\qquad
 L_p=\lfloor\log_pN\rfloor\quad(p\leq N).
\]
Every \(n\leq N\) is a divisor of \(M_N\), so conditioning the uniform
divisor of \(M_N\) on \(D\leq N\) gives exactly \(U_N\).  But
\[
 \Pr(D\leq N)=
 \frac{N}{\prod_{p\leq N}(L_p+1)}
 \leq \frac{N}{2^{\pi(N)}}
 =\exp\!\left(-\Theta\!\left(\frac N{\log N}\right)\right), \tag{14}
\]
where the final estimate uses the standard prime number theorem.  Dividing
(13) by (14) yields no information.

This is not merely an inefficiency of using the full lcm box.

### Lemma 3 (any box covering a dense set has huge dimension)

Suppose \(S_N\subset[1,N]\), \(|S_N|=N-o(N)\), and every element of \(S_N\)
lies in a divisor box with prime-coordinate set \(P_N\).  Then
\[
 |P_N\cap(N^{3/4},N]|\geq(\log(4/3)-o(1))N^{3/4}, \tag{15}
\]
and hence the box has at least
\[
 2^{(\log(4/3)-o(1))N^{3/4}} \tag{16}
\]
points.  Its uniform measure assigns probability at most
\(N/2^{(\log(4/3)-o(1))N^{3/4}}\) to \([1,N]\).

**Proof.**  If a prime \(p\in(N^{3/4},N]\) is absent from \(P_N\), all
\(\lfloor N/p\rfloor\) of its multiples are absent from \(S_N\).  The sets
of multiples belonging to two distinct primes in this interval are
disjoint, since their product exceeds \(N\).  Thus
\[
 \sum_{\substack{N^{3/4}<p\leq N\\p\notin P_N}}
 \left\lfloor\frac Np\right\rfloor=o(N). \tag{17}
\]
The standard Mertens theorem for prime reciprocals and \(\pi(N)=o(N)\)
give
\[
 \sum_{N^{3/4}<p\leq N}\left\lfloor\frac Np\right\rfloor
 =N\log(4/3)+o(N). \tag{18}
\]
Each included prime contributes at most \(N^{1/4}\) to this sum.  Equations
(17)--(18) prove (15).  Every included prime supplies at least two exponent
choices, proving (16). \(\square\)

One can bias the exponent marginals heavily toward zero so that \(D\leq N\)
is no longer rare.  But then the one-coordinate estimate behind (13)
becomes \(\max_e\Pr(e_p=e)\), which can be arbitrarily close to one, and the
conditional weights on integers are not flat.  This is the same tradeoff in
product-box language.

## 6. Weakest useful replacement

A fixed uniform atom gap is much stronger than is needed.  The active-prime
chain argument suggests the following order-ideal statement.

> **Replacement lemma (R), minimal sufficient scale.**  For all sufficiently
> large \(N\), in the range \(y=y(N)\to\infty\), let \(f\) be any rational
> completely additive function satisfying \(f(p)=0\) for every prime
> \(p\leq y\).  Then, for every \(c\ne0\),
> \[
> \left|\{n\leq N:f(n)\ne c\}\right|
> \geq \left\lfloor\frac Ny\right\rfloor. \tag{R}
> \]

Only the self-consistent instances of (R) are required.  In particular, it
is enough to prove (R) when its left side is \(o(N)\); no fixed positive
density loss is requested.

The statement is already automatic whenever
\(\Psi(N,y)\geq\lfloor N/y\rfloor\), because every \(y\)-smooth integer has
value zero and hence misses a nonzero target.  In particular this covers
\(y\geq\sqrt N\), since the integers \(1,\ldots,\lfloor y\rfloor\) alone
are \(y\)-smooth.  The new content is the range in which the smooth-number
obstruction is smaller than \(N/y\), notably the slowly growing \(y\)
allowed by the present self-consistency bound.

### Why (R) settles the finite repetition-allowed question negatively

Suppose \(A_N\subset[1,N]\) is contained in \(F_c\), with
\(|A_N|=N-m_N\) and \(m_N=o(N)\).  If \(f(p)\ne0\), a fixed level meets each
\(p\)-adic chain at most once, and hence
\[
 m_N\geq\left\lfloor\frac Np\right\rfloor. \tag{19}
\]
Set
\[
 y_N=\left\lfloor\frac{N}{m_N+1}\right\rfloor.
\]
Then \(y_N\to\infty\), and (19) forces \(f(p)=0\) for every \(p\leq y_N\).
The complement of the full fiber has size at most \(m_N\), whereas (R)
would give
\[
 \left|[1,N]\setminus F_c\right|
 \geq\left\lfloor\frac N{y_N}\right\rfloor
 \geq m_N+1,
\]
a contradiction.

The scale in (R) is essentially the weakest clean target compatible with
this argument: the known chain obstruction is of order \(N/y\), and a
lower bound of that size, fed back at
\(y=\lfloor N/(m+1)\rfloor\), already rules out \(m=o(N)\).  By contrast,
trying to manufacture a measure within \(o(1)\) of \(U_N\) asks for far more
than the proof needs and runs into Lemmas 1--3.

## Unsupported step, falsification test, and next action

The sole unsupported mathematical step here is (R).  Everything before it
is a proved limitation on proposed measure transfers.

A concrete falsification of (R) is a sequence
\[
 N_j\to\infty,\quad y_j\to\infty,
\]
together with rational weights supported on primes \(>y_j\) and nonzero
targets \(c_j\), for which fewer than \(\lfloor N_j/y_j\rfloor\) integers
in \([1,N_j]\) miss the target.  This is a sharper computational target than
searching vaguely for a large fiber.

The next constructive action should therefore work directly in the
truncated divisor order ideal \(\{v(n):n\leq N\}\), not in an unconditioned
product law: prove that a nonzero affine hyperplane whose normal vanishes on
coordinates \(p\leq y\) leaves at least \(\lfloor N/y\rfloor\) valuation
vectors outside.  A plausible mechanism is to pack \(\lfloor N/y\rfloor\)
disjoint multiplicative chains or small divisor boxes and force one
off-level point in each; any such packing must explicitly respect the
boundary \(n\leq N\), which is precisely the dependence erased by the Euler
models above.
