# Erdős Problem #786: strongest proved result

## Scope and status

This gives complete negative answers to both questions when \(r,s\geq1\)
and repetitions are allowed:

- every infinite product-length-rigid set has lower natural density at most
  \(1/2\);
- there is an absolute \(\eta>0\) such that every product-length-rigid
  \(A\subset[1,N]\) satisfies \(|A|\leq(1-\eta)N\), for all sufficiently
  large \(N\).

The internally repetition-free interpretation remains open because the
grading theorem below is sufficient but no longer necessary under that
convention.

## Theorem

Let \(A\subset\mathbb N\). Suppose that arbitrary repeated choices satisfy
\[
 a_1\cdots a_r=b_1\cdots b_s\quad\Longrightarrow\quad r=s.
\]
Then
\[
 \underline d(A)\leq\frac12.
\]
Consequently the infinite assertion is false for every
\(\epsilon\leq1/2\) under this convention.

### 1. Rigidity gives an exact additive grading

Write \(v(n)=(v_p(n))_p\in\mathbb Z^{(\mathcal P)}\). The set \(A\) cannot
contain \(1\), since \(1=1\cdot1\).

Let \(F=\mathbb Z^{(A)}\), and define
\[
 T(e_a)=v(a),\qquad \sigma(e_a)=1.
\]
If \(z\in\ker T\), split \(z=z^+-z^-\). A nonzero one-sided relation is
impossible because all elements of \(A\) exceed \(1\). Otherwise \(Tz=0\)
is an allowed product equality, so rigidity gives
\(\sigma(z^+)=\sigma(z^-)\). Thus
\[
 \ker T\subseteq\ker\sigma.
\]
Hence \(h(Tz)=\sigma(z)\) is a well-defined homomorphism on
\(\langle v(A)\rangle_{\mathbb Z}\), with \(h(v(a))=1\). Tensor with
\(\mathbb Q\) and extend to the algebraic direct sum
\(\mathbb Q^{(\mathcal P)}\). Writing \(w_p\) for the coordinate values gives
the rational completely additive function
\[
 f(n)=\sum_p w_pv_p(n),\qquad A\subseteq\{n:f(n)=1\}. \tag{1}
\]
The sum is finite for each integer. The \(w_p\) need not have a global common
denominator.

### 2. Compound-Poisson anti-concentration

**Lemma.** If \(X\) has a zero-drift compound-Poisson law on \(\mathbb Q\)
with finite Lévy measure, then
\[
 \Pr(X=x)\leq\frac12\qquad(x\neq0). \tag{2}
\]

**Proof.** First suppose the Lévy measure has finite support. Clear the
denominators of those finitely many jumps and of \(x\), obtaining integer
jumps \(m_j\) and a nonzero integer target \(L\). The characteristic function
is
\[
 \phi(t)=\exp\!\left(\sum_j\lambda_j(e^{im_jt}-1)\right).
\]
Its displayed exponent is a continuous \(2\pi\)-periodic logarithm, so the
nonvanishing closed curve \(\phi\) has winding number zero.

If \(a=\Pr(X=L)>1/2\), write
\[
 \phi(t)=ae^{iLt}+R(t),\qquad |R(t)|\leq1-a<a.
\]
The homotopy \(ae^{iLt}+uR(t)\), \(0\leq u\leq1\), never vanishes. Thus
\(\phi\) has the winding number \(L\neq0\) of \(ae^{iLt}\), a contradiction.

For general finite Lévy measure, exhaust its support by finite sets. Couple
the truncations \(X_j\) with \(X\); their mismatch probability is at most
\[
 1-\exp(-\nu(\text{omitted jumps}))\longrightarrow0.
\]
Therefore \(\Pr(X_j=x)\to\Pr(X=x)\), and the finite-support result proves
(2). \(\square\)

The restrictions “zero drift” and “\(x\neq0\)” are essential.

### 3. Dirichlet mass of an exact additive level

Fix \(s>1\) and give \(n\) probability
\[
 \mu_s(n)=\frac{n^{-s}}{\zeta(s)}.
\]
The variables \(V_p=v_p(n)\) are independent with
\[
 \Pr(V_p=k)=(1-p^{-s})p^{-ks}.
\]
Writing \(q=p^{-s}\), a geometric variable has the representation
\[
 V_p=\sum_{k\geq1}kN_{p,k},\qquad
 N_{p,k}\sim\operatorname{Pois}(q^k/k),
\]
because
\[
 \exp\!\left(\sum_{k\geq1}\frac{q^k}{k}(z^k-1)\right)
 =\frac{1-q}{1-qz}.
\]
Thus \(f(n)\) under \(\mu_s\) is zero-drift compound Poisson, with total
nonzero intensity at most
\[
 \sum_p\sum_{k\geq1}\frac{p^{-ks}}k=\log\zeta(s)<\infty.
\]
The lemma yields, for every \(c\neq0\),
\[
 \frac1{\zeta(s)}
 \sum_{\substack{n\geq1\\f(n)=c}}n^{-s}\leq\frac12. \tag{3}
\]
Finite Lévy truncation avoids any global-denominator assumption.

### 4. Transfer to lower natural density

By (1) and (3),
\[
 \frac1{\zeta(s)}\sum_{a\in A}a^{-s}\leq\frac12. \tag{4}
\]
Let \(d=\underline d(A)\). Given \(\eta>0\), choose \(X\) such that
\[
 A(x)=|A\cap[1,x]|\geq(d-\eta)x\qquad(x\geq X).
\]
Partial summation gives
\[
 \sum_{a\in A}a^{-s}
 =s\int_1^\infty A(x)x^{-s-1}\,dx
 \geq\frac{s(d-\eta)X^{1-s}}{s-1}.
\]
Since \((s-1)\zeta(s)\to1\) as \(s\downarrow1\), equation (4) implies
\(d-\eta\leq1/2\). Let \(\eta\downarrow0\).

This proves a lower-density bound, not an upper-natural-density bound.

## Finite consequences

Let \(A_N\subset[1,N]\) be repetition-allowed PLR and
\(m_N=N-|A_N|\). Extend its grading with zero weights on primes above \(N\).
Equation (3) gives
\[
 \sum_{a\in A_N}a^{-s}\leq\frac12\zeta(s).
\]
The decreasing weights \(n^{-s}\) imply
\[
 \sum_{n=m_N+1}^{N}n^{-s}\leq\frac12\zeta(s). \tag{5}
\]
Put \(\gamma_N=\log(m_N+1)/\log N\) and take
\(s=1+c/\log N\). If \(\gamma_N\leq\beta<1\) on a subsequence, an integral
lower bound in (5) gives
\[
 e^{-\beta c}-e^{-c}\leq\frac12\qquad(c>0). \tag{6}
\]
The maximum is
\[
 M(\beta)=(1-\beta)\beta^{\beta/(1-\beta)}.
\]
If \(\beta_*\) is the unique root
\[
 (1-\beta_*)\beta_*^{\beta_*/(1-\beta_*)}=\frac12,
 \qquad \beta_*=0.227092\ldots,
\]
then
\[
 m_N+1\geq N^{\beta_*-o(1)}. \tag{7}
\]
This exponent is not claimed sharp.

A second necessary condition is stronger if \(m_N=o(N)\). If \(f(p)\neq0\),
a fixed level meets each \(p\)-adic chain at most once, so
\[
 m_N\geq\left\lfloor\frac Np\right\rfloor. \tag{8}
\]
Consequently \(f(p)=0\) for every
\[
 p\leq y_N:=\left\lfloor\frac{N}{m_N+1}\right\rfloor.
\]
All \(y_N\)-smooth integers have grading zero and are omitted:
\[
 m_N\geq\Psi(N,y_N). \tag{9}
\]
The standard fixed-\(u\) Dickman asymptotic now gives
\[
 m_N=o(N)\quad\Longrightarrow\quad m_N=N^{1-o(1)}. \tag{10}
\]
This still permits \(m_N=N/\log N\), so the finite question remains open.

### Stronger finite theorem: \(m_N\gg N/\log N\)

There is an absolute \(c>0\) such that every repetition-allowed PLR
\(A\subset[1,N]\) satisfies
\[
 N-|A|\geq c\frac{N}{\log N}. \tag{11}
\]

To prove this, enlarge \(A\) to the full level
\[
 B=\{n\leq N:f(n)=1\},
\]
and write \(E=[1,N]\setminus B\), \(m=|E|\). It is enough to bound \(m\).

For \(C_j=2^j\), define
\[
 P_j=\left\{p\text{ prime}:\frac{N}{2C_j}<p\leq\frac{N}{C_j}\right\},
 \qquad K_j=[1,C_j],
\]
where \(0\leq j\leq J\) and \(C_J\) is the largest power of two at most
\(\sqrt N/4\). Every product \(pk\), \(p\in P_j\), \(k\in K_j\), is at most
\(N\). These products are globally distinct across all the rectangles:
every participating prime exceeds \(2\sqrt N>C_J\), so
\(pk=q\ell\) with \(p\neq q\) would force \(p\mid\ell<p\).

Let \(R_j=|P_j|\), and let \(B_j\) count rectangle entries whose product is
in \(E\). Then
\[
 \sum_jB_j\leq m. \tag{12}
\]
The prime number theorem in dyadic intervals gives an absolute \(c_0>0\)
such that
\[
 R_jC_j\geq c_0\frac{N}{\log N} \tag{13}
\]
uniformly in \(j\).

An elementary rectangle lemma will be used repeatedly. In any
\(R\)-by-\(C\) prime--cofactor rectangle with \(D\) bad entries, choose a row
with at most \(D/R\) bad entries and call its prime weight \(a\). Every good
column in that row satisfies \(f(k)=1-a\); therefore
\[
 |\{k:f(k)\neq1-a\}|\leq D/R. \tag{14}
\]

Suppose \(m\leq\varepsilon N/\log N\). By (12)--(14), every rectangle has a
prescribed cofactor value with at most
\(\eta C_j\) exceptions, where \(\eta=\varepsilon/c_0\).
For \(\eta<1/3\), the prescribed values in two adjacent nested intervals
\(K_j\subset K_{j+1}\) agree: their exceptional subsets cover fewer than
\(\eta C_j+2\eta C_j<C_j\) points of the overlap.

At \(j=0\), the sole cofactor is \(1\). If \(\eta<1\), it is
nonexceptional in (14), so \(0=f(1)=1-a_0\). Hence every prescribed
cofactor value is zero. In particular
\[
 Z=\{k\leq C_J:f(k)=0\}
 \quad\text{satisfies}\quad
 |Z|\geq(1-\eta)C_J. \tag{15}
\]

Every product of two elements of \(Z\) is at most \(C_J^2\leq N\), has
grading zero, and lies in \(E\). To bound the number of distinct products,
let \(M=C_J\). The number of solutions
\[
 ab=cd,\qquad a,b,c,d\leq M,
\]
is at most \(2M^2(1+\log M)\): write
\(a=gr,c=gs\), \((r,s)=1\), whence \(b=sh,d=rh\), and sum
\(\lfloor M/\max(r,s)\rfloor^2\) over the at most \(2q\) pairs with
\(\max(r,s)=q\). Cauchy--Schwarz and (15) now give
\[
 m\geq|Z\cdot Z|
 \geq\frac{|Z|^4}{2M^2(1+\log M)}
 \gg\frac{N}{\log N}. \tag{16}
\]
Fix \(\eta_0<1/3\), obtain the absolute implied constant in (16) with
\(\eta\leq\eta_0\), and then choose \(\varepsilon>0\) smaller than both
\(c_0\eta_0\) and that constant. This contradicts
\(m\leq\varepsilon N/\log N\), proving (11).

The next argument supersedes (11) qualitatively and closes the finite
density-one question.

### Absolute finite theorem: a fixed positive density must be omitted

There is an absolute \(\eta>0\) such that every rational completely
additive \(f\), every \(t\neq0\), and all sufficiently large \(N\) satisfy
\[
 \bigl|\{n\leq N:f(n)=t\}\bigr|\leq(1-\eta)N. \tag{17}
\]
Together with the grading theorem, this proves
\[
 |A|\leq(1-\eta)N                                      \tag{18}
\]
for every repetition-allowed PLR set \(A\subset[1,N]\).

We use one precisely stated standard dependency.

**Halász--Ruzsa exact-concentration theorem.** There is an absolute
constant \(C\) such that, for every real additive function \(g\),
\[
 \frac1x\sup_z|\{n\leq x:g(n)=z\}|
 \leq \frac{C}{\sqrt{1+H_g(x)}},
 \qquad
 H_g(x)=\sum_{\substack{p\leq x\\g(p)\neq0}}\frac1p. \tag{19}
\]
The theorem is finite and uniform, so \(g\) may depend on \(x\).

For clarity, (19) is the exact-point consequence of the interval theorem
\[
 Q_h(x;g)\ll(1+E_h)^{-1/2},                              \tag{20}
\]
where
\[
 E_h=\inf_{\tau\in\mathbb R}\left\{
 \left(\frac\tau h\right)^2+
 \sum_{p\leq x}\frac1p
 \min\left(1,\left|\frac{g(p)-\tau\log p}{h}\right|^2\right)
 \right\}.                                               \tag{21}
\]
The Archimedean term in (21) is essential. To verify the exact-point
specialization needed here, first clear the finitely many denominators of
the rational values \(g(p)\), \(p\leq x\), so that every nonzero prime
value is an integer.
Choose
\[
 0<h<\min\left\{\frac14,
       \frac1{4\sqrt{1+H_g(x)}\log x}\right\}.             \tag{22}
\]
For every \(\tau\), either \(|\tau|/h\geq\sqrt{H_g(x)}\), or
\(|\tau|\log x<1/4\), in which case every active prime contributes
\(1/p\) to (21). Hence \(E_h\geq H_g(x)\), and an exact atom fits in an
interval of length \(h\). This proves the needed form (19), including
uniformity for moving rational weights.

It remains to handle bounded \(H_g(N)\) without replacing the finite
factorization law by independent geometric variables.

**Boundary-sieve lemma.** For every fixed \(K<\infty\), there is
\(c_K>0\) such that, if \(f\) is completely additive and
\[
 \sum_{\substack{p\leq\sqrt N\\f(p)\neq0}}\frac1p\leq K,     \tag{23}
\]
then at least \(c_KN\) integers \(n\in(N/2,N]\) satisfy
\[
 f(n)=0,\qquad P^+(n)<N^{1/4}.                             \tag{24}
\]

**Proof.** We first need a harmonic supply of integers avoiding a set of
primes. If \({\cal S}\) is any finite prime set with
\(\sum_{p\in{\cal S}}1/p\leq K\), then, uniformly in \({\cal S}\),
\[
 \sum_{\substack{b\leq X\\p\mid b\Rightarrow p\notin{\cal S}}}
 \frac1b\geq d_K\log X                                  \tag{25}
\]
for all sufficiently large \(X\). Indeed, put
\(A=2K+\log2\) and \(\sigma=1+A/\log X\). The full Dirichlet series of
the integers avoiding \({\cal S}\) is
\[
 \zeta(\sigma)\prod_{p\in{\cal S}}(1-p^{-\sigma})
 \geq \frac{e^{-2K}\log X}{A}.                           \tag{26}
\]
The unrestricted tail beyond \(X\) is at most
\[
 \int_X^\infty u^{-\sigma}\,du
 =\frac{e^{-A}\log X}{A}
 =\frac{e^{-2K}\log X}{2A}.                              \tag{27}
\]
Subtract (27) from (26) and use \(b^{-1}\geq b^{-\sigma}\) to obtain
(25), for example with \(d_K=e^{-2K}/(2A)\).

Now put \(L=\log N\). Choose a sufficiently large absolute \(i_0\), and
consider a fixed finite list, depending only on \(K\), of disjoint bands
\[
 I_i=(N^{a_i},N^{2a_i}],\qquad a_i=2^{-i-1},\qquad
 i_0\leq i<i_0+\lfloor K/\varepsilon_0\rfloor+2.           \tag{28}
\]
Here \(\varepsilon_0>0\) is a sufficiently small absolute constant.
By (23), one band \(I=(N^a,N^{2a}]\) satisfies
\[
 \sum_{\substack{p\in I\\f(p)\neq0}}\frac1p\leq\varepsilon_0. \tag{29}
\]
Choose \(i_0\) so that \(2a<1/4\) for every possible selected band.

On exponent space define
\[
 \mu=\sum_{p\in I}\frac1p\,\delta_{\log p/L},\qquad
 \nu=\sum_{\substack{p\in I\\f(p)\neq0}}
              \frac1p\,\delta_{\log p/L},qquad
 \mu_0=\mu-\nu.                                           \tag{30}
\]
The PNT in fixed-ratio prime intervals gives, for every interval \(W\) of
length comparable with \(1/L\) contained in
\([(3-1/10)a,(3+1/10)a]\),
\[
 (\mu*\mu)(W)\geq c\frac{|W|}{a},
 \qquad
 \sup_x\mu(W-x)\leq C_0\frac{|W|}{a}.                     \tag{31}
\]
Indeed, the limiting convolution density at \(s\) is
\[
 \int_{[a,2a]\cap[s-2a,s-a]}\frac{du}{u(s-u)}\asymp\frac1a, \tag{32}
\]
and exponent width \(1/L\) is a fixed multiplicative ratio on the prime
scale. Since
\[
 \mu^{*2}-\mu_0^{*2}=\nu*\mu+\mu_0*\nu\leq2\nu*\mu,
\]
(29)--(31), with \(\varepsilon_0<c/(4C_0)\), imply
\[
 \mu_0^{*2}(W)\geq c'\frac{|W|}{a}.                         \tag{33}
\]

Let \(J=[(3-1/20)a,(3+1/20)a]\). By increasing \(i_0\), choose an
integer \(k=k(a)\) such that \(1\) lies in the interior of \(kJ\). For
some \(\delta=\delta_K>0\),
\[
 [1-2\delta,1]\subset\operatorname{int}(kJ).                \tag{34}
\]
Set \(r=2k\). Partition a slightly smaller copy of \(J\) into cells of
length \(\asymp1/L\). For a target window of length \(\log2/L\), there
are \(\gg_K L^{k-1}\) choices of the first \(k-1\) cells for which the
forced last cell remains in \(J\). Each cell has \(\mu_0^{*2}\)-mass
\(\gg_K1/L\) by (33). Therefore, uniformly for
\(s\in[1-\delta,1]\),
\[
 \mu_0^{*r}([s-\log2/L,s])\geq\frac{c_K'}L.                 \tag{35}
\]
Tuples with a repeated prime have reciprocal mass
\[
 O_r\!\left(\sum_{q>N^a}\frac1{q^2}
       \left(\sum_{p\in I}\frac1p\right)^{r-2}\right)
 =O_r(N^{-a})=o(1/L),                                      \tag{36}
\]
so (35) still holds, with a smaller constant, for tuples of distinct
zero-weight primes.

Choose \(0<\delta_0<\min(\delta,a/2)\), put
\(X=N^{\delta_0}\), and let \({\cal B}\) be the integers \(b\leq X\)
all of whose prime factors have weight zero. Apply (35) with
\(s=1-\log b/L\). It gives reciprocal mass \(\gg_K1/L\) of ordered
tuples \((q_1,\ldots,q_r)\) of distinct zero-weight primes in \(I\) with
\[
 \frac{N}{2b}<q_1\cdots q_r\leq\frac Nb.                   \tag{37}
\]
Every reciprocal summand in (37) is at most \(2b/N\); hence there are
\(\gg_K N/(bL)\) ordered tuples. Forgetting order costs at most \(r!\).

The map
\[
 (b,\{q_1,\ldots,q_r\})\longmapsto bq_1\cdots q_r          \tag{38}
\]
is injective: every prime factor of \(b\) is below \(N^a\), while every
\(q_i\) is above \(N^a\). Its values lie in \((N/2,N]\), have grading
zero, and have largest prime factor below \(N^{2a}<N^{1/4}\). Finally,
(25), applied to the active primes up to \(X\), gives
\[
 \sum_{b\in{\cal B}}\frac1b\gg_K\log X\asymp_K L.          \tag{39}
\]
Summing \(N/(bL)\) over (39) proves (24). \(\square\)

We now prove (17). Choose a fixed \(K\) so large that the right side of
(19) is at most \(1/2\) whenever \(H_f(N)\geq K\). In that case every
fiber has size at most \(N/2\). If \(H_f(N)<K\), the boundary-sieve lemma
supplies at least \(c_KN\) zero-valued integers, all outside the nonzero
\(t\)-fiber. Thus (17) holds with
\[
 \eta=\min(1/2,c_K)>0.                                    \tag{40}
\]
This is deliberately qualitative; the threshold construction of density
\(0.828499\ldots\) shows that the optimal \(\eta\) is at most
\(0.171500\ldots\).

## Audit

Two fresh agents independently certified the compound-Poisson/winding proof
and the density/finite-exponent calculation. A further fresh audit certified
every step of the overlap--energy proof of (11). For the decisive finite
gap, independent audits checked (i) the exact Halász--Ruzsa specialization,
including the Archimedean term and moving weights, and (ii) the complete
boundary-sieve proof, including the local \(1/\log N\) convolution,
repeated-prime removal, anchor injectivity, and order of quantifiers. The
audit files are `attempts/audits_infinite.md`,
`attempts/tournament/audit_overlap_energy.md`,
`attempts/tournament/audit_halasz_exact_concentration.md`, and
`attempts/tournament/audit_rough_concentration_active_core.md`.
