# Erdős Problem #786: strongest proved result

## Scope and status

This gives a complete negative answer to the **infinite** question when
\(r,s\geq1\) and repetitions are allowed. Every product-length-rigid set has
lower natural density at most \(1/2\).

The finite density-\(1-o(1)\) question remains open. The internally
repetition-free interpretation also remains open because the grading theorem
below is no longer necessary under that convention.

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

The order \(N/\log N\) is still \(o(N)\); the finite density-one question
therefore remains open.

## Audit

Two fresh agents independently certified the compound-Poisson/winding proof
and the density/finite-exponent calculation. Separate agents certified an
independent geometric-variable/Sperner proof of a weaker universal density
gap. A further fresh audit certified every step of the overlap--energy proof
of (11), including its global injectivity, uniform prime count, base
rectangle, energy parametrization, and constant choices. Audit details are
in attempts/audits_infinite.md and attempts/tournament/audit_overlap_energy.md.
