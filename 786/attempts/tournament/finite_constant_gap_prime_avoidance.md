# A finite constant gap from point concentration and prime avoidance

## Result

This note treats the repetition-allowed interpretation of the product-length
condition.  It proves the following asymptotic statement.

> **Theorem.** There are absolute constants \(\eta>0\) and \(N_0\) such that,
> for every \(N\ge N_0\), every completely additive rational-valued function
> \(f\), and every nonzero rational \(t\),
> \[
> \#\{n\le N:f(n)=t\}\le (1-\eta)N.
> \]
> Consequently no repetition-allowed product-length-rigid subset of
> \([1,N]\) has cardinality \(N-o(N)\).

The proof is non-effective.  Its only non-self-contained input is the standard
Halász--Ruzsa point-concentration theorem for integer-valued strongly additive
functions, stated precisely below.  The bounded-harmonic-mass prime-avoidance
lemma, including its uniformity for an \(N\)-dependent set of primes, is proved
here from Mertens' prime-reciprocal theorem.

## 1. From product-length rigidity to an additive level

For completeness, write \(v(n)=(v_p(n))_{p\le N}\).  If \(A\subseteq[1,N]\)
is product-length rigid with repetitions allowed, then every rational relation
\[
\sum_{a\in A}c_a v(a)=0
\]
has \(\sum_{a\in A}c_a=0\).  Otherwise, clearing denominators and moving the
negative coefficients to the other side gives an equality of two products of
elements of \(A\) with unequal numbers of factors.  Conversely, such a product
equality gives such a relation.

It follows by elementary rational linear algebra that the prescription
\(v(a)\mapsto1\), \(a\in A\), defines a rational linear functional on the span
of the vectors \(v(a)\).  Extend it to the ambient rational vector space.  Thus
there are rational weights \(w_p\) such that
\[
f(n):=\sum_{p\le N}w_pv_p(n),\qquad f(a)=1\quad(a\in A).
\]
After multiplying the finitely many weights \(w_p\) with \(p\le N\) by a
common denominator, define the weights for primes \(p>N\) arbitrarily (say,
to be zero).  It is then enough to bound a nonzero integer level of an
integer-valued completely additive function.  Enlarging
\(A\) to the full level can only help.  We therefore work with
\[
L=\{n\le N:F(n)=T\},\qquad T\in\mathbb Z\setminus\{0\},
\]
where \(F\) is integer-valued and completely additive.

## 2. Active primes escape if the deficit tends to zero

Call a prime \(p\) **active** if \(F(p)\ne0\), and put
\[
\mathcal P={p\le N:F(p)\ne0\},\qquad m=N-|L|.
\]

For an active prime \(p\), partition \([1,N]\) into its \(p\)-adic chains
\[
r,rp,rp^2,\ldots\qquad(p\nmid r).
\]
Along such a chain the values of \(F\) are
\(F(r)+jF(p)\), so at most one member belongs to \(L\).  The number of chains
is \(N-\lfloor N/p\rfloor\).  Hence
\[
|L|\le N-\left\lfloor\frac Np\right\rfloor,
\qquad
m\ge\left\lfloor\frac Np\right\rfloor.                 \tag{2.1}
\]
In particular, if \(m=o(N)\), then
\[
\min\mathcal P>\frac{N}{m+1}\longrightarrow\infty.     \tag{2.2}
\]

## 3. The standard point-concentration input

We use the following standard theorem and do not prove it here.

> **Halász--Ruzsa point-concentration theorem (external input).** There is an
> absolute constant \(C_0\) such that, for every integer-valued strongly
> additive function \(g\), meaning
> \[
> g(n)=\sum_{p\mid n}g(p),
> \]
> and every \(x\ge2\),
> \[
> \sup_{b\in\mathbb Z}\frac1x\#\{n\le x:g(n)=b\}
> \le
> \frac{C_0}{\sqrt{1+V_g(x)}},                           \tag{3.1}
> \]
> where
> \[
> V_g(x)=\sum_{\substack{p\le x\\g(p)\ne0}}
> \frac{1-1/p}{p}.
> \]

Some formulations replace \(V_g\) by
\(\sum_{p\le x,g(p)\ne0}1/p\); these are equivalent here up to an absolute
factor because
\[
\frac12\sum_{g(p)\ne0}\frac1p\le V_g(x)
\le\sum_{g(p)\ne0}\frac1p.                              \tag{3.2}
\]
It is important that (3.1) is an exact lattice point-concentration theorem.
An analogous assertion for arbitrary short real intervals is not what is used.

Given the completely additive \(F\), define its strongly additive companion
\[
g(n)=\sum_{p\mid n}F(p).
\]
The functions \(F\) and \(g\) agree unless \(p^2\mid n\) for some active
prime \(p\).  If \(y=\min\mathcal P\), the exceptional proportion is at most
\[
\frac1N\sum_{p\in\mathcal P}\left\lfloor\frac N{p^2}\right\rfloor
\le\sum_{p\ge y}\frac1{p^2}
\le\frac1{y-1}.                                         \tag{3.3}
\]
Thus, when \(y\to\infty\), every point mass of \(F\) is at most the largest
point mass of \(g\), plus \(o(1)\).

Put
\[
H(\mathcal P)=\sum_{p\in\mathcal P}\frac1p.
\]
Equations (3.1)--(3.3) imply that if a nonzero level of \(F\) has density
\(1-o(1)\) and \(\min\mathcal P\to\infty\), then
\[
H(\mathcal P)=O(1).                                     \tag{3.4}
\]
For example, once the point mass of \(g\) is at least \(1/2\), (3.1) and
(3.2) give \(H(\mathcal P)\le 8C_0^2\).

## 4. Uniform prime avoidance with bounded harmonic mass

The next proposition is the main self-contained lemma.

> **Proposition 4.1 (bounded-budget prime avoidance).** Fix \(H<\infty\).
> There is \(c(H)>0\) with the following sequentially uniform property.  If
> \(N_j\to\infty\) and \(\mathcal P_j\) is a set of primes at most \(N_j\)
> such that
> \[
> y_j:=\min\mathcal P_j\longrightarrow\infty,
> \qquad
> \sum_{p\in\mathcal P_j}\frac1p\le H,                 \tag{4.1}
> \]
> then
> \[
> \liminf_{j\to\infty}\frac1{N_j}
> \#\{n\le N_j:p\nmid n\text{ for every }p\in\mathcal P_j\}
> \ge c(H).                                             \tag{4.2}
> \]

### 4.1 Compact logarithmic prime profiles

Define a finite measure on \([0,1]\) by
\[
\nu_j=\sum_{p\in\mathcal P_j}\frac1p\,
\delta_{\log p/\log N_j}.                              \tag{4.3}
\]
Its total mass is at most \(H\).  By weak compactness of bounded finite
measures on the compact interval \([0,1]\), every subsequence has a further
subsequence converging weakly to a finite measure \(\nu\).

Mertens' theorem
\[
\sum_{p\le x}\frac1p=\log\log x+B+o(1)                \tag{4.4}
\]
implies that the full-prime profile converges vaguely on \((0,1]\) to
\(dt/t\).  More explicitly, for every nonnegative continuous \(\varphi\)
compactly supported in \((0,1]\), partial summation in (4.4) gives
\[
\lim_{j\to\infty}\sum_{p\le N_j}
\frac1p\varphi\!\left(\frac{\log p}{\log N_j}\right)
=\int_0^1\varphi(t)\frac{dt}{t}.                       \tag{4.5}
\]
Because \(\mathcal P_j\) is a subset of the primes, (4.5) implies
\[
\nu|_{(0,1]}\le\frac{dt}{t}.                            \tag{4.6}
\]
Consequently every limit has the form
\[
\nu=h\delta_0+a(t)\frac{dt}{t},
\qquad h\ge0,\quad 0\le a(t)\le1\text{ a.e.},
\qquad h+\int_0^1a(t)\frac{dt}{t}\le H.               \tag{4.7}
\]
The atom at zero records active primes of size \(N_j^{o(1)}\).  Hypothesis
\(y_j\to\infty\) is still essential: it makes every individual prime weight
\(1/p\) tend to zero and will remove diagonal terms below.

### 4.2 Exact inclusion-exclusion and its limit

Let
\[
\Phi_j=\#\{n\le N_j:p\nmid n\text{ for every }p\in\mathcal P_j\}.
\]
Exact inclusion-exclusion gives
\[
\frac{\Phi_j}{N_j}=\sum_{k\ge0}(-1)^kT_{j,k},           \tag{4.8}
\]
where
\[
T_{j,k}=
\sum_{\substack{p_1<\cdots<p_k\in\mathcal P_j\\
                  p_1\cdots p_k\le N_j}}
\frac1{N_j}\left\lfloor\frac{N_j}{p_1\cdots p_k}\right\rfloor.
                                                                    \tag{4.9}
\]
The convention is \(T_{j,0}=1\).  Uniformly in \(j\),
\[
0\le T_{j,k}\le
\sum_{p_1<\cdots<p_k}\frac1{p_1\cdots p_k}
\le\frac{H^k}{k!}.                                     \tag{4.10}
\]
Therefore the tails of (4.8) are absolutely and uniformly bounded by
\(\sum_{k>K}H^k/k!\).

Fix \(k\).  First replace the floor in (4.9) by the reciprocal product.  The
total error is at most \(N_j^{-1}\) times the number of admissible \(k\)-sets.
Fix \(0<\epsilon<1\), and write \(d=p_1\cdots p_k\).  For \(d\le
N_j^{1-\epsilon}\),
\[
\frac1{N_j}\#\{(p_1,\ldots,p_k):d\le N_j^{1-\epsilon}\}
\le N_j^{-\epsilon}\sum_{p_1<\cdots<p_k}\frac1d
\le N_j^{-\epsilon}\frac{H^k}{k!}.                    \tag{4.11}
\]
For \(N_j^{1-\epsilon}<d\le N_j\), the floor error is bounded by the
reciprocal sum over that shell, since \(1/N_j\le1/d\).  In terms of (4.3),
that reciprocal sum is at most
\[
\frac1{k!}\nu_j^{\otimes k}
\{(t_1,\ldots,t_k):1-\epsilon< t_1+\cdots+t_k\le1\}.    \tag{4.12}
\]

The only possible atom of \(\nu\) is at zero.  Hence the convolution
\(\nu^{*k}\) has no atom at any positive point, in particular at \(1\).
Weak convergence, followed by \(\epsilon\downarrow0\), shows that (4.12)
tends to zero in the required double limit.  Together with (4.11), this proves
that the floor replacement has \(o(1)\) error for every fixed \(k\).

Next remove repeated coordinates from the product measure.  For \(k\ge2\),
the total weight of ordered tuples with a repetition is at most
\[
\binom{k}{2}
\left(\sum_{p\in\mathcal P_j}\frac1{p^2}\right)
\left(\sum_{p\in\mathcal P_j}\frac1p\right)^{k-2}
\le \binom{k}{2}\frac{H^{k-1}}{y_j}=o(1).              \tag{4.13}
\]
Finally, the boundary of the simplex
\[
\Delta_k=\{(t_1,\ldots,t_k)\in[0,1]^k:t_1+\cdots+t_k\le1\}
\]
has \(\nu^{\otimes k}\)-measure zero: all mass away from zero is absolutely
continuous, while the all-zero atom has sum zero.  Weak convergence of product
measures now gives
\[
T_{j,k}\longrightarrow
\frac1{k!}\nu^{\otimes k}(\Delta_k).                   \tag{4.14}
\]
Using the uniform tail bound (4.10) in (4.8), we obtain the ordinary, not
logarithmic, density limit
\[
\frac{\Phi_j}{N_j}\longrightarrow D(\nu),              \tag{4.15}
\]
where
\[
D(\nu)=\sum_{k\ge0}\frac{(-1)^k}{k!}
\nu^{\otimes k}(\Delta_k).                              \tag{4.16}
\]

### 4.3 Positivity: the GEM hole functional and its renewal equation

Write \(\nu=h\delta_0+\mu\), where
\[
\mu(dt)=a(t)\frac{dt}{t}.
\]
Because zero coordinates do not change a simplex sum, expanding (4.16) gives
\[
D(\nu)=e^{-h}q_a(1),                                   \tag{4.17}
\]
where, for \(0\le r\le1\),
\[
q_a(r)=\sum_{k\ge0}\frac{(-1)^k}{k!}I_k(r),
\qquad
I_k(r)=\int_{t_1+\cdots+t_k\le r}
\prod_{i=1}^k a(t_i)\frac{dt_i}{t_i}.                  \tag{4.18}
\]
The series is absolutely convergent because, with
\[
A(r)=\int_0^r a(t)\frac{dt}{t},
\]
one has \(I_k(r)\le A(r)^k\) and \(A(1)\le H\).

Probabilistically, \(q_a(r)\) is a GEM(1) hole probability.  If
\(U_1,U_2,\ldots\) are independent uniform variables on \((0,1)\), the GEM
parts of total mass \(r\) are
\[
X_1=rU_1,
\qquad
X_i=rU_i\prod_{\ell<i}(1-U_\ell)\quad(i\ge2).
\]
Mark a part of size \(t\) independently with probability \(a(t)\).  The
ordered factorial-moment identity
\[
\mathbb E\!\sum_{i_1,\ldots,i_k\ \mathrm{distinct}}
G(X_{i_1},\ldots,X_{i_k})
=\int_{t_1+\cdots+t_k\le r}G(t_1,\ldots,t_k)
\prod_{i=1}^k\frac{dt_i}{t_i}                          \tag{4.19}
\]
shows by inclusion-exclusion that (4.18) is precisely the probability that
there is no marked part.  Indeed the expected number of marked parts is
\(A(r)<\infty\), so it is finite almost surely, while (4.19) gives
\(\sum_k\mathbb E\binom{Z}{k}\le e^{A(r)}\) for their number \(Z\); hence the
infinite inclusion-exclusion is absolutely integrable.  Identity (4.19)
follows inductively from the fact
that the first part is uniform on \((0,r)\) and, conditional on its size \(u\),
the remaining parts form an independent GEM partition of mass \(r-u\).  In
the induction, tuples omitting the first part contribute the coefficient
\((r-\sum t_i)/r\), while the \(k\) possible positions of the first part
together contribute \((\sum t_i)/r\); the coefficients sum to one.

For a completely analytic verification, multiply \(I_k(r)\) by
\(r=(r-\sum t_i)+\sum t_i\).  Fubini gives
\[
rI_k(r)=\int_0^r I_k(v)\,dv
+k\int_0^r a(u)I_{k-1}(r-u)\,du.                       \tag{4.20}
\]
Summing (4.20) with coefficients \((-1)^k/k!\) yields the renewal equation
\[
r q_a(r)=\int_0^r(1-a(u))q_a(r-u)\,du.                 \tag{4.21}
\]

The functions \(I_k(r)\), and hence \(q_a(r)\), are continuous; this also
follows from the uniform convergence in (4.18), since \(\mu^{*k}\) has no
atoms at positive points.  Moreover
\[
|q_a(r)-1|\le e^{A(r)}-1\longrightarrow0
\qquad(r\downarrow0),                                  \tag{4.22}
\]
because \(A(r)\to0\).  Thus \(q_a\) is positive near zero.  If it had a
first zero \(r_0>0\), then \(q_a(r_0-u)>0\) for every \(0<u<r_0\).  The
integrand in (4.21) is nonnegative, so equality at \(r_0\) would force
\(a(u)=1\) for almost every \(u\in(0,r_0)\).  But then
\[
\int_0^{r_0}a(u)\frac{du}{u}=\infty,
\]
contrary to (4.7).  Therefore
\[
q_a(1)>0,
\qquad D(\nu)>0                                         \tag{4.23}
\]
for every admissible profile \(\nu\).

### 4.4 Compactness upgrades pointwise positivity to a uniform bound

Let \(K_H\) be the set of finite positive measures \(\nu\) on \([0,1]\) such
that
\[
\nu([0,1])\le H,
\qquad
\nu|_{(0,1]}\le dt/t.                                  \tag{4.24}
\]
It is weakly compact.  Indeed, bounded positive measures on the compact space
\([0,1]\) are relatively compact; (4.24) is closed because it may be tested
against nonnegative continuous functions compactly supported in \((0,1]\),
and total mass is the integral of the continuous function \(1\).

The combined functional \(D\) in (4.16) is continuous on \(K_H\).  For each
fixed \(k\), weak convergence of product measures and the null boundary of
\(\Delta_k\) give continuity of the \(k\)-th term.  The tails are uniformly
bounded by \(\sum_{k>K}H^k/k!\).  It is important to use this combined
functional: under weak convergence, positive-scale mass can drift to zero, so
the separate quantities \(h\) and \(q_a\) need not themselves be continuous.

By (4.23), \(D\) is strictly positive everywhere on the compact set \(K_H\).
It therefore has a positive minimum
\[
c_*(H):=\min_{\nu\in K_H}D(\nu)>0.                     \tag{4.25}
\]
If Proposition 4.1 failed, a violating sequence would have a profile
subsequence converging to some \(\nu\in K_H\), while (4.15) would give a
limiting avoidance density \(D(\nu)\ge c_*(H)\), a contradiction.  This proves
the proposition (for example, \(c(H)=c_*(H)/2\) works eventually).

The argument handles an atom at exponent zero arising from primes that tend to
infinity but are \(N^{o(1)}\).  It does not claim that fixed active primes are
encoded by that atom; fixed primes would retain diagonal mass.  In the present
application (2.2) removes all fixed active primes.

## 5. Completion of the finite constant-gap proof

Suppose the theorem were false.  Then there would be \(N_j\to\infty\),
integer-valued completely additive \(F_j\), and nonzero integer targets \(T_j\)
such that
\[
L_j=\{n\le N_j:F_j(n)=T_j\},
\qquad |L_j|=N_j-o(N_j).                                \tag{5.1}
\]
Let \(\mathcal P_j=\{p\le N_j:F_j(p)\ne0\}\).  By (2.1),
\(y_j=\min\mathcal P_j\to\infty\).  Define the strongly additive companions
\(g_j\) as in Section 3.  Equations (3.1)--(3.3) show that
\[
\sum_{p\in\mathcal P_j}\frac1p\le M                  \tag{5.2}
\]
for some absolute \(M\) and all sufficiently large \(j\).

Proposition 4.1 now supplies \(c(M)N_j\) integers, up to a lower-order term,
which are divisible by no active prime.  Every such integer has
\(F_j(n)=0\), so none belongs to the nonzero level \(L_j\).  Hence
\[
N_j-|L_j|\ge c(M)N_j+o(N_j),
\]
contradicting (5.1).  The theorem follows.

## Dependency and audit ledger

- Self-contained here: rational additive-level reduction, active-prime chain
  bound, completely-to-strongly-additive reduction, the full uniform
  bounded-budget prime-avoidance proposition, the GEM/renewal positivity
  argument, and the compactness upgrade.
- Standard background used: Mertens' prime-reciprocal theorem, elementary weak
  compactness/product-measure facts, and elementary rational linear algebra.
- External theorem not proved here: the Halász--Ruzsa point-concentration
  theorem (3.1).  Its exact lattice formulation, not a real interval analogue,
  is required.
- Independent audits of Proposition 4.1 checked the floor replacement,
  diagonal removal, simplex-boundary nullity, renewal first-zero argument, and
  the combined-functional continuity.  A specific audit repair incorporated
  above is that \(h\) and \(q_a\) must not be asserted separately continuous
  when profile mass drifts to exponent zero.
