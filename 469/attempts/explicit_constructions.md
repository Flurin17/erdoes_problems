# Explicit constructions and fixed-core obstructions

This note investigates whether a divergent subfamily can be obtained by
adjoining primes to a weird (abundant but nonsemiperfect) core.  It does not
settle Problem 469.  The results below show that a fixed core, and several
natural low-complexity varying-core schemes, cannot produce divergence.

Write \(D(m)\) for the divisors of \(m\), \(D^-(m)=D(m)\setminus\{m\}\),
and \(\Sigma(E)\) for all subset sums of a finite set \(E\).  Put

\[
 \partial(m)=2m-\sigma(m).
\]

Thus \(m\) is deficient, perfect, or abundant according as
\(\partial(m)>0\), \(=0\), or \(<0\).

## 1. Exact one-new-prime formulas

### Defect recurrence

If \(p\nmid m\) is prime, then

\[
 \boxed{\partial(mp)=p\partial(m)-\sigma(m)},\qquad
 \sigma(mp)=(p+1)\sigma(m).                                      \tag{1}
\]

This is just multiplicativity of \(\sigma\).  In particular, if \(m\) is
deficient and

\[
 Q(m)=\frac{\sigma(m)}{\partial(m)},
\]

then \(mp\) is deficient, perfect, or abundant according as \(p>Q(m)\),
\(p=Q(m)\), or \(p<Q(m)\).  In the last case its abundance excess is exactly

\[
 \sigma(mp)-2mp=\sigma(m)-p\partial(m)
                 =\partial(m)(Q(m)-p).                           \tag{2}
\]

Consequently, whenever the right side of (2) is a subset sum of proper
divisors of \(mp\), deleting those divisors from the full set of proper
divisors gives a semiperfect certificate.  This observation is useful for
constructions, but minimality must still be checked separately.

### Exact subset-sum criterion

Suppose \(p\nmid m\) is prime and \(m\) is not semiperfect.  Splitting a
putative certificate into its \(p\)-free and \(p\)-divisible layers gives

\[
 mp=A+pB,qquad A\in\Sigma(D(m)),\quad B\in\Sigma(D^-(m)).        \tag{3}
\]

Since \(m\) is not semiperfect, (3) holds if and only if there is an integer
\(t\geq1\) such that

\[
 \boxed{pt\in\Sigma(D(m)),\qquad m-t\in\Sigma(D^-(m)).}          \tag{4}
\]

Indeed, take \(t=m-B\), so that \(A=pt\).  In particular,

\[
 p\leq \sigma(m).                                                \tag{5}
\]

Thus a fixed nonsemiperfect core has only finitely many one-new-prime
semiperfect extensions.  Moreover, if

\[
 p>\max_{d\mid m,\ d<m}\sigma(d),                                \tag{6}
\]

then every \(pd\), \(d\mid m,d<m\), is nonsemiperfect by (5).
Hence (4), nonsemiperfectness of \(m\), and (6) together prove
\(mp\in A\).

The same layer argument works with a coprime composite multiplier.  If
\((k,m)=1\), \(m\) is nonsemiperfect, and \(mk\) is semiperfect, then

\[
 1\leq \sigma(m)\left(\frac{\sigma(k)}k-1\right).                \tag{7}
\]

To prove (7), write a certificate by the divisor \(e\mid k\) occurring in
each term.  If \(S\) is the coefficient subset sum in the top layer \(e=k\),
then

\[
 k(m-S)=\sum_{e\mid k,\ e<k}eT_e,qquad 0\leq T_e\leq\sigma(m),
\]

and divide by \(k\).  Here \(m-S\geq1\), since equality zero would certify
\(m\).  For \(k=p^b\), (7) again forces \(p\leq\sigma(m)\), independently
of \(b\).

## 2. Complete analysis of the core 70

The proper divisors of \(70\) are

\[
 1,2,5,7,10,14,35.
\]

Their sum is \(74\), but they have no subset sum \(70\), so \(70\) is
weird.  A direct interval calculation gives

\[
\begin{aligned}
 \Sigma(D^-(70))&=[0,3]\cup[5,69]\cup[71,74],\\
 \Sigma(D(70))&=[0,3]\cup[5,139]\cup[141,144].                 \tag{8}
\end{aligned}
\]

For a prime \(p\nmid70\), (4) and (8) show that \(70p\) is semiperfect
exactly when

\[
 p=3\quad\hbox{or}\quad 11\leq p\leq139.                        \tag{9}
\]

For all primes in the second range, take \(t=1\): the proper divisors of
\(70\) other than \(5\) sum to \(69\), and \(p\) is a divisor-subset sum
by (8).  No \(p\geq149\) can work because (5) gives \(p\leq144\).

Every number \(70p\) in the second range is in \(A\).  Indeed, \(70\) is
nonsemiperfect, while for every proper \(d\mid70\)

\[
 \frac{\sigma(pd)}{pd}
 =\left(1+\frac1p\right)\frac{\sigma(d)}d
 \leq \frac{12}{11}\cdot\frac95<2.                             \tag{10}
\]

Thus all remaining proper divisors are deficient.  The case \(p=3\) is not
minimal because \(6\mid210\).

The primes already dividing the core give two further members:

\[
\begin{aligned}
350&=175+70+50+35+14+5+1,\\
490&=245+98+70+49+14+7+5+2.                                    \tag{11}
\end{aligned}
\]

For \(350\), the maximal proper divisors are \(175,70,50\); for \(490\),
they are \(245,98,70\).  Apart from the weird number \(70\), all are
deficient, proving minimality.  In contrast, \(140\) is nonminimal because
\(28\mid140\).  Hence the exact minimal prime-multiplier list for this core
is

\[
 p\in\{5,7\}\cup\{p\text{ prime}:11\leq p\leq139\}.             \tag{12}
\]

This is a useful finite family, not a divergent one.

## 3. A checked two-new-prime construction

Although neither \(70\cdot149\) nor \(70\cdot1489\) is semiperfect,

\[
 N=70\cdot149\cdot1489=15,530,270
\]

does belong to \(A\).  Put \(p=149\), \(q=1489\).  The numerical identity

\[
 70pq=69pq+49p+144q+144                                      \tag{13}
\]

is a valid distinct-proper-divisor certificate because

\[
\begin{aligned}
69&=1+2+7+10+14+35 &&\text{(proper divisors of 70)},\\
49&=14+35,\\
144&=1+2+5+7+10+14+35+70.
\end{aligned}
\]

The four layers \(pqD^-(70),pD(70),qD(70),D(70)\) are disjoint, and the
top layer does not contain \(70pq\), so (13) is legitimate.

For minimality, the maximal proper divisors \(70p\) and \(70q\) are
nonsemiperfect by (9).  The other three maximal proper divisors are
\(35pq,14pq,10pq\).  Since

\[
 \left(1+\frac1p\right)\left(1+\frac1q\right)
 <\left(\frac{150}{149}\right)^2<\frac{36}{35},
\]

their abundancy indices are respectively less than

\[
 \frac{48}{35}\frac{36}{35},\qquad
 \frac{12}{7}\frac{36}{35},\qquad
 \frac95\frac{36}{35},
\]

all of which are below \(2\).  They are deficient.  Every proper divisor of
\(N\) lies below one of these five maximal proper divisors; semiperfectness
is upward-closed under multiplication, so none of those divisors can be
semiperfect.  This completes the check that \(N\in A\).

## 4. Why a fixed weird core cannot drive divergence

Let \(W\) be nonsemiperfect, \(L=\sigma(W)\), and let \(p\leq q\) be new
distinct primes.  If \(Wpq\) is semiperfect, a certificate has the form

\[
 Wpq=T_0+pT_1+qT_2+pqS,                                       \tag{14}
\]

where \(0\leq T_i\leq L\) are divisor-subset sums of \(W\), and \(S\) is
a proper-divisor subset sum.  Put \(k=W-S\).  Then \(k\geq1\) and

\[
 q(pk-T_2)=T_0+pT_1.                                          \tag{15}
\]

If \(Wpq\) is divisibility-minimal, the factor on the left of (15) cannot
vanish: otherwise \(T_0=T_1=0\), and \(pW=pS+T_2\) would certify the proper
divisor \(Wp\).  Hence

\[
 q\leq L(p+1).                                                  \tag{16}
\]

If \(p>L\), then \(pk-T_2\geq p-L\); using \(q\geq p\) in (15) gives

\[
 p(p-L)\leq L(p+1),
\]

and therefore \(p\leq2L\).  This is already true if \(p\leq L\), so every
minimal two-new-prime extension satisfies

\[
 \boxed{p\leq2L,\qquad q\leq L(2L+1).}                          \tag{17}
\]

Thus a fixed core has only finitely many two-new-prime extensions as well.

More generally, if \(r_1<\cdots<r_t\) are new primes and
\(W\prod_i r_i\) is semiperfect, grouping a certificate by new-prime support
gives

\[
 1\leq L\left(\prod_{i=1}^t\left(1+\frac1{r_i}\right)-1\right)
 \leq \frac{L(2^t-1)}{r_1}.                                    \tag{18}
\]

For a minimal extension, each prefix core is nonsemiperfect, so (18) can be
reapplied successively to bound \(r_2,r_3,\ldots,r_t\).  Therefore, for
each fixed \(W\) and fixed \(t\), there are only finitely many minimal
extensions by \(t\) new primes.  Any divergent construction of this type
would have to vary the core essentially or use an unbounded number of new
prime factors.

Even the most immediate varying-core continuation of \(70\) cannot give a
minimal infinite family.  If \(70pq\in A\) and \(p\leq q\) are new primes,
then (9) first forces \(149\leq p\leq q\), since otherwise the proper divisor
\(70p\) is already semiperfect.  Any certificate for \(70pq\) can be
written

\[
 70pq=pqS+pU+qV+T,
\]

where \(S\in\Sigma(D^-(70))\) and \(T,U,V\in\Sigma(D(70))\).  Hence
\(S\leq69\) and \(T,U,V\leq144\).  With \(k=70-S\),

\[
 kpq=pU+qV+T\leq144(p+q+1)<2pq,
\]

so \(k=1\).  It follows that

\[
 (p-V)(q-U)=UV+T\leq144^2+144=20880.                           \tag{19}
\]

Therefore

\[
 (p-144)^2\leq20880<145^2,
\]

so \(p\leq283\), and then

\[
 q\leq144+\frac{20880}{p-144}\leq4320.                         \tag{20}
\]

Thus the cores \(70q\), \(q\geq149\), admit only finitely many minimal
semiperfect extensions by one further distinct prime.  Repetition does not
help: a certificate for \(70q^2\) would give

\[
 q^2\leq qU+T\leq144(q+1),
\]

which is false for \(q\geq149\).

There is a separate summability obstruction for the standard
\(2^apq\) shape.  Put \(H=2^a\) with \(a\geq1\), \(M=2H-1\), and let \(p,q\) be distinct
odd primes.  If \(Hpq\in A\), then \(Hp\) and \(Hq\) are not semiperfect.
Since

\[
 Hp\text{ is semiperfect}\quad\Longleftrightarrow\quad p\leq M,
\]

we have \(p,q>M\).  Semiperfectness implies nondeficiency, and direct
expansion of \(\sigma(Hpq)\geq2Hpq\) gives

\[
 (p-M)(q-M)\leq M(M+1).                                       \tag{21}
\]

Writing \(u=p-M\), \(v=q-M\), and overcounting primes by all positive
integers, the reciprocal mass in the fixed \(a\)-layer is at most

\[
 \frac1H
 \sum_{uv\leq M(M+1)}\frac1{(M+u)(M+v)}=O\!\left(\frac1H\right). \tag{22}
\]

The constant is absolute.  To see this, the inner \(v\)-sum is at most
\(\log(1+2M/u)\).  For \(u\leq M\), average
\(\log(3M/u)\) and use \(\log(M!)\geq M\log M-M\); for \(u>M\), use
\(\log(1+2M/u)\leq2M/u\) and sum \(O(M/u^2)\).  Since
\(\sum_a H^{-1}<\infty\), no squarefree \(2^apq\) subfamily can be the
desired divergent construction.

There is also no danger from merely raising the exponents on a family of
cores whose reciprocal sum already converges.  For example, for every
\(m=2^apq\) with distinct odd primes \(p,q\geq5\), the reciprocal mass of its entire
same-prime-support upward closure is

\[
 \sum_{i,j,k\geq0}\frac1{m2^ip^jq^k}
 =\frac1m\frac1{1-1/2}\frac1{1-1/p}\frac1{1-1/q}<\frac3m.       \tag{23}
\]

Hence repeated-prime examples such as \(70\mapsto350\) do not by themselves
turn a summable core stratum into a divergent family.

## 5. LCM obstruction to recursive Egyptian-fraction constructions

A semiperfect certificate for \(n\) is equivalently an identity

\[
 1=\sum_{q\in Q}\frac1q
\]

with distinct divisors \(q>1\) of \(n\).  If
\(L=\operatorname{lcm}(Q)<n\), the same identity certifies the proper
divisor \(L\).  Thus every certificate for a member of \(A\) must have
\(L=n\).

Moreover, deleting any one denominator preserves this LCM.  Indeed, with
\(L_i=\operatorname{lcm}(Q\setminus\{q_i\})\), subtraction from the identity
shows \(1/q_i=A/L_i\) for an integer \(A\), and hence \(q_i\mid L_i\).
It follows that each maximal prime-power exponent in \(L\) occurs in at
least two denominators.  Standard term-splitting Egyptian-fraction
recursions retain the old LCM as a divisor of the new LCM, so whenever their
LCM grows, the new number has a semiperfect proper divisor.  Such recursions
cannot construct members of \(A\).

## Current obstruction

The examples above prove that weird cores can have genuine minimal
semiperfect upgrades, including an upgrade requiring two new primes.  They
also rule out divergence from any one fixed core with a bounded number of
new primes, from routine Egyptian refinements, or merely from raising a
fixed finite prime support.  They do **not** control a sufficiently numerous
family of varying weird cores with growing prime support.  That remains the
precise gap in this construction route.
