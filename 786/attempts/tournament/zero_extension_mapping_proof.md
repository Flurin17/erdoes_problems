# Zero-extension by active-prime rectangles

## Outcome

Let \(f:\mathbb N\to\mathbb Q\) be completely additive and put

\[
 B_f(y)=|\{n\le y:f(n)\ne0\}|.
\]

There is a sharp elementary zero-extension lemma in the sparse range.  If
\(b=B_f(x)\) and

\[
 b^2+b<x,
\]

then the number \(S_f(x)\) of \(x\)-smooth integers \(n\le x^2\) for
which \(f(n)\ne0\) satisfies

\[
 \boxed{S_f(x)\le 2bx.} \tag{1}
\]

The order \(bx\) cannot be improved: if \(x/2<p\le x\) is prime and
\(f(n)=v_p(n)\), then \(B_f(x)=1\), while all \(pm\), \(m\le x\), are
\(x\)-smooth nonzero-valued integers at most \(x^2\).

For arbitrary \(b=o(x)\), the same rectangles give an exact weighted
inequality.  Combining it with the already proved uniform nonzero-level
deficit

\[
 |\{n\le y:f(n)\ne u\}|\ge
 \frac{\kappa y}{\log(ey)}\qquad(u\ne0) \tag{2}
\]

gives, whenever \(b+1<x\),

\[
 \boxed{
 S_f(x)\le \frac{2}{\kappa} bx\log x\,
 \frac{\log(e(b+1))}{\log(x/(b+1))}.} \tag{3}
\]

Thus a zero fibre at scale \(x\) extends to density one among the
\(x\)-smooth integers up to \(x^2\) whenever the right side of (3) is
\(o(x^2)\).  In particular this holds under

\[
 \frac bx\frac{\log x\,\log(e(b+1))}
                    {\log(x/(b+1))}=o(1). \tag{4}
\]

The estimate (3) does not cover every sequence \(b=o(x)\).  The precise
loss is not an overlap defect: the weighted rectangle ledger below has no
uncontrolled multiplicity.  It is the \(\log y\) loss in (2).  Removing
that loss uniformly would amount to proving a linear deficit for every
nonzero additive level, much stronger than the present finite theorem.

## 1. Active primes must be large

Write

\[
 \mathcal P_x=\{p\le x:p\text{ prime and }f(p)\ne0\}.
\]

### Lemma 1

If \(p\in\mathcal P_x\), then

\[
 p>\frac{x}{b+1}. \tag{5}
\]

#### Proof

Partition \([1,x]\) into its \(p\)-adic chains

\[
 \{r,pr,p^2r,\ldots\}\cap[1,x],\qquad p\nmid r.
\]

Along such a chain the values of \(f\) are
\(f(r)+j f(p)\), and hence are all distinct because \(f(p)\ne0\).
Thus each chain contains at most one zero of \(f\).  The number of chains
is \(x-\lfloor x/p\rfloor\), so

\[
 b\ge \lfloor x/p\rfloor.
\]

Since \(x/p<\lfloor x/p\rfloor+1\), (5) follows. \(\square\)

This uses only complete additivity and the torsion-free target; there is
no distributional input.

## 2. Exact weighted rectangle ledger

For \(p\in\mathcal P_x\), let

\[
 t_p=\lfloor x/p\rfloor,
 \qquad
 R_p=\{k\le t_p:f(k)\ne-f(p)\}.
\]

Every pair \((p,k)\), \(k\in R_p\), produces an exception \(pk\le x\).
Products from different rows need not be distinct.  They can nevertheless
be charged without loss by logarithmic weights.

### Lemma 2 (weighted active-prime rectangles)

One has the exact inequality

\[
 \boxed{
 \sum_{p\in\mathcal P_x}\frac{\log p}{\log x}
  |R_p|\le b.} \tag{6}
\]

More generally, (6) holds with \(\log p/\log x\) replaced by any
nonnegative weights \(a_p\) satisfying

\[
 \sum_{\substack{p\in\mathcal P_x\\p\mid n}}a_p\le1
 \quad(n\le x). \tag{7}
\]

#### Proof

Charge the pair \((p,k)\) to \(n=pk\).  By the definition of \(R_p\),
\(f(n)\ne0\), so every charged \(n\) belongs to a set of size \(b\).
For fixed \(n\), its total charge is at most the left side of (7).
Summing over exceptional \(n\) proves the general assertion.  For the
displayed choice,

\[
 \sum_{\substack{p\in\mathcal P_x\\p\mid n}}\log p
 \le \log n\le\log x,
\]

which proves (6). \(\square\)

Notice that

\[
 |R_p|=|\{k\le t_p:f(k)\ne-f(p)\}|. \tag{8}
\]

Since \(-f(p)\ne0\), (2), (6), and
\(t_p\ge x/(2p)\) give

\[
 \sum_{p\in\mathcal P_x}
 \frac{\log p}{p\log(ex/p)}
 \le \frac{2b\log x}{\kappa x}. \tag{9}
\]

Here we used \(\log(et_p)\le\log(ex/p)\).

By Lemma 1,

\[
 \frac{\log(ex/p)}{\log p}
 \le
 \frac{\log(e(b+1))}{\log(x/(b+1))}. \tag{10}
\]

Multiplying the summand in (9) by the ratio in (10) yields

\[
 \sum_{p\in\mathcal P_x}\frac1p
 \le
 \frac{2b\log x}{\kappa x}
 \frac{\log(e(b+1))}{\log(x/(b+1))}. \tag{11}
\]

If \(n\le x^2\) is \(x\)-smooth and \(f(n)\ne0\), at least one of its
prime divisors belongs to \(\mathcal P_x\); otherwise complete additivity
would give \(f(n)=0\).  The union bound over multiples therefore gives

\[
 S_f(x)
 \le\sum_{p\in\mathcal P_x}\left\lfloor\frac{x^2}{p}\right\rfloor
 \le x^2\sum_{p\in\mathcal P_x}\frac1p. \tag{12}
\]

Equations (11)--(12) prove (3).

## 3. Sparse range: a globally injective ledger

Assume \(b^2+b<x\).  Lemma 1 implies

\[
 t_p\le b<\frac{x}{b+1}<p_0
 \qquad(p\in\mathcal P_x), \tag{13}
\]

where \(p_0=\min\mathcal P_x\).  Every prime factor of every
\(k\le t_p\) is below \(p_0\), hence has \(f\)-weight zero.  Therefore
\(f(k)=0\), and all products \(pk\), \(k\le t_p\), are exceptional.

Moreover these products are globally distinct.  Indeed, if
\(pk=q\ell\) with distinct active primes \(p,q\), then \(q\mid k\), but
\(k<p_0\le q\), a contradiction.  Consequently

\[
 \sum_{p\in\mathcal P_x}t_p\le b. \tag{14}
\]

Since \(t_p\ge x/(2p)\),

\[
 \sum_{p\in\mathcal P_x}\frac1p\le\frac{2b}{x}. \tag{15}
\]

Combining (15) with (12) proves (1).

## 4. A support-only dichotomy for the active harmonic mass

Put

\[
 H_x=\sum_{p\in\mathcal P_x}\frac1p,
 \qquad \delta=\frac bx.
\]

For \(n\le x\), let \(T(n)\) be the number of distinct active prime
divisors of \(n\).  If \(T(n)=1\), then
\(f(n)=v_p(n)f(p)\ne0\) for the unique active divisor \(p\).  Moreover,

\[
 \mathbb E_{n\le x}T(n)
 =\sum_{p\in\mathcal P_x}\frac{\lfloor x/p\rfloor}{x}
 \ge H_x-\frac{|\mathcal P_x|}{x}
 \ge H_x-\delta, \tag{16}
\]

because every active prime is itself exceptional, and

\[
 \mathbb E_{n\le x}T(n)(T(n)-1)
 \le\sum_{\substack{p,q\in\mathcal P_x\\p\ne q}}\frac1{pq}
 \le H_x^2. \tag{17}
\]

The pointwise inequality

\[
 1_{\{T=1\}}\ge T-T(T-1)
\]

therefore gives

\[
 \boxed{2\delta\ge H_x-H_x^2.} \tag{18}
\]

In particular,

\[
 H_x\le\frac12\quad\Longrightarrow\quad H_x\le4\delta. \tag{19}
\]

Thus the desired implication \(\delta\to0\Rightarrow H_x\to0\) is
elementary once the harmonic mass is known to be below \(1/2\).  More
precisely, the two roots of \(H-H^2=2\delta\) show that any subsequence on
which \(H_x\) does not tend to zero must satisfy \(H_x\ge1-O(\delta)\).
Counting integers with exactly one active prime cannot by itself eliminate
this genuinely large-mass alternative.

## 5. A componentwise anti-concentration claim is false

A tempting way to eliminate the large-mass alternative is to decompose
integers by their inactive core and claim that, in every active valuation
simplex, the zero fibre has size at most one half.  This is false even for
actual prime costs.

Take active primes

\[
 Q=\{101,103\},\qquad P=\{149,151,157,163,167\},
\]

give the primes in \(Q\) weight \(-1\), those in \(P\) weight \(+1\),
and take the component cutoff

\[
 X=167\cdot103=17201.
\]

The allowed active monomials are exactly:

* the unit monomial;
* the seven single primes;
* the three degree-two monomials on \(Q\);
* the ten products \(pq\), \(p\in P,q\in Q\).

Indeed \(103^2<X<149^2\), while \(101^3>X\).  The zero fibre consists
of the unit and the ten mixed products, so it has size \(11\), whereas
the nonzero fibre has size \(7+3=10\).  By taking \(n\) negative-weight
primes in a short interval near \(Y\), many positive-weight primes in a
short interval near \(\lambda Y\), \(1<\lambda<2\), and a cutoff just
above the mixed products but below positive-positive and triple-negative
products, the componentwise zero proportion can be made arbitrarily close
to one.  Hence any proof of \(H_x\to0\) must use the global multiplicity
of cores or cross-scale information; a uniform atom bound inside each
valuation simplex is unavailable.

## 6. Why two-factor product-set coverage is false

One cannot replace the active-prime argument by the assertion that every
\(x\)-smooth \(n\le x^2\) is a product of two integers at most \(x\).
For example, take a prime \(q\) of size \(x^{3/5}\) and put \(n=q^3\).
Then \(n<x^2\) and is \(x\)-smooth, but its only nontrivial proper
divisors are \(q\le x\) and \(q^2>x\), so no factorization \(n=ab\) has
both \(a,b\le x\).  Thus density of the zero set in \([1,x]\) plus the
inclusion \(Z\cdot Z\subseteq Z\) does not by itself control all smooth
integers at the next squared scale.

## 7. Remaining bottleneck

The exact statement to improve is (8).  A row for an active prime \(p\)
can be almost entirely neutralized only if the cofactor interval
\([1,t_p]\) is highly concentrated on the nonzero value \(-f(p)\).
The present theorem (2) says that at least
\(\kappa t_p/\log(et_p)\) entries escape this concentration.  The weighted
ledger (6) then handles every overlap exactly.  Hence a full implication

\[
 B_f(x)=o(x)\quad\Longrightarrow\quad S_f(x)=o(x^2)
\]

for arbitrary moving functions \(f=f_x\) is not obtained here; its hard
case is precisely a tower of near-full nonzero cofactor levels.  This is
the same zero-spine obstruction identified by the largest-prime profile
recurrence, now expressed as an injection problem rather than as a modal
heuristic.
