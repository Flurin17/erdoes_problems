# A finite constant gap from dyadic ratio grids

## Status and theorem

This note gives a candidate complete negative solution of the finite
repetition-allowed version of Problem 786.  Its only non-elementary inputs
are standard, explicitly stated forms of the prime number theorem, the
Dickman smooth-number theorem, Mertens' prime-reciprocal theorem, and the
one-dimensional fundamental lemma of the sieve.  In particular, it does
not use a product model for all prime factors of a uniform integer.

### Theorem

There are absolute constants \(\delta>0\) and \(N_0\) such that, for every
\(N\geq N_0\), every completely additive function
\[
 f:\mathbb N\longrightarrow \mathbb Q,
\]
and every \(t\ne0\),
\[
 \bigl|\{n\leq N:f(n)=t\}\bigr|\leq(1-\delta)N.       \tag{1}
\]

Consequently no repetition-allowed product-length-rigid subset of
\([1,N]\) has size \((1-o(1))N\).  Indeed, the exact grading theorem proved
in `NOTES.md` puts every such set inside a nonzero level of a rational
completely additive function.

We prove the theorem by contradiction.  After dividing by \(t\), suppose
that there are \(N\to\infty\) and completely additive \(f=f_N\) for which
\[
 A=A_N:=\{n\leq N:f(n)=1\},\qquad
 m:=N-|A|=o(N).                                      \tag{2}
\]
All little-oh terms below refer to this sequence, with the fixed parameter
\(\alpha\) introduced below held constant.

## 1. Standard analytic inputs

We record exactly what is used.

### Input PNT (fixed proportional dyadic bands)

Fix \(0<a<b<1\).  Uniformly for integers
\(a\log_2N\leq i\leq b\log_2N\),
\[
 |\{p:2^i<p\leq2^{i+1}\}|\asymp_{a,b}\frac{2^i}{\log N}. \tag{3}
\]
The same estimate holds if \((2^i,2^{i+1}]\) is replaced by any fixed
positive-length multiplicative subinterval, for example
\((2^i,2^{i+1/4}]\) or \((2^{i+3/4},2^{i+1}]\).

### Input Dickman (a compact fixed-parameter consequence)

For every compact interval \(J\subset(0,\infty)\), there is
\(d_J>0\) such that, uniformly when
\(\log X/\log y\in J\),
\[
 \Psi(X,y):=|\{n\leq X:P^+(n)\leq y\}|\geq d_JX       \tag{4}
\]
for all sufficiently large \(X,y\).  When the displayed ratio is below
one this is trivial; otherwise it is the fixed-parameter Dickman theorem.

### Input Mertens

For every fixed \(0<a<1\),
\[
 \sum_{N^a<p\leq N}\frac1p=-\log a+o(1),             \tag{5}
\]
and
\[
 \sum_{p\leq y}\frac{\log p}{p-1}=\log y+o(\log y). \tag{6}
\]

### Input fundamental lemma for rough numbers

Put
\[
 \Phi(x,y)=|\{n\leq x:P^-(n)>y\}|,
 \qquad V(y)=\prod_{p\leq y}\left(1-\frac1p\right).
\]
We use the following standard one-dimensional fundamental-lemma
consequence.  There is a function \(\eta(s)\to0\) as \(s\to\infty\) such
that, for every fixed sufficiently large \(s\),
\[
 \sup_{x\geq y^s}
 \left|\frac{\Phi(x,y)}{xV(y)}-1\right|
 \leq \eta(s)+o_{y\to\infty}(1).                    \tag{7}
\]
Equivalently, one may use the standard Buchstab asymptotic uniformly for
\(\log x/\log y\geq s\), together with
\(e^\gamma\omega(u)\to1\).  Equation (7), including its uniformity, is the
only sieve theorem invoked below.  It should be checked against the chosen
reference before this draft is promoted to `PROOF.md`; no stronger claim
that the fixed-\(s\) error is \(o_y(1)\) is being made.

Section 6 derives from (7) the precise total-variation statement needed in
the proof.

## 2. A globally disjoint same-band matching

Fix once and for all
\[
 0<\alpha<\frac1{20},
\]
to be chosen sufficiently small only in Section 7.  Write
\[
 L=\log_2N,
 \qquad a=\lceil\alpha L\rceil,
 \qquad b_0=\lfloor(1-3\alpha)L\rfloor,
 \qquad y=2^a.                                      \tag{8}
\]
For \(a\leq i\leq b_0\), let
\[
 \mathcal P_i=\{p:2^i<p\leq2^{i+1}\}.              \tag{9}
\]

Partition \(\mathcal P_i\) into classes according to the exact rational
value \(f(p)\).  Choose a largest class \(C_i\), write its value as \(c_i\),
and put
\[
 r_i=1-\frac{|C_i|}{|\mathcal P_i|}.                \tag{10}
\]
The complete multipartite graph joining primes of different values has a
matching of size
\[
 M_i\geq\frac12r_i|\mathcal P_i|.                   \tag{11}
\]
Indeed, if the largest class has at least half the vertices, match every
minority vertex into that class; otherwise a matching of size
\(\lfloor|\mathcal P_i|/2\rfloor\) exists.

For every matched pair \((p,q)\) and every \(y\)-smooth integer
\[
 k\leq\frac{N}{2^{i+1}},                             \tag{12}
\]
make the edge
\[
 \{kp,kq\}.                                         \tag{13}
\]
These edges, over every pair and every band, are globally vertex-disjoint.
To see this, note that \(p,q>2^i\geq2^a=y\), while all prime factors of
\(k\) are at most \(y\).  Thus an endpoint has exactly one prime factor
larger than \(y\), that prime identifies the matched pair and its side, and
unique factorization then recovers \(k\).  Each prime was used in at most
one matched pair.

The two values on (13) differ by \(f(p)-f(q)\ne0\), so every edge has an
endpoint outside \(A\).  By (4), uniformly over the present range of
\(i\),
\[
 \Psi(N/2^{i+1},y)\geq d_\alpha\frac{N}{2^i}         \tag{14}
\]
for a constant \(d_\alpha>0\).  The relevant smoothness parameter ranges
over a fixed compact subinterval of
\([2,(1-\alpha)/\alpha+1]\).

The disjoint edges therefore give
\[
 m\geq d_\alpha N\sum_{i=a}^{b_0}\frac{M_i}{2^i}.  \tag{15}
\]
By (3), \(|\mathcal P_i|/2^i\asymp_\alpha1/L\).  Equations
(2), (11), and (15) imply
\[
 \sum_{i=a}^{b_0}r_i=o(L).                          \tag{16}
\]

Choose a sequence \(\theta_N\to0\) such that all but \(o(L)\) indices in
\([a,b_0]\) satisfy
\[
 |C_i|\geq(1-\theta_N)|\mathcal P_i|.               \tag{17}
\]
For example, take
\[
 \theta_N=\sqrt{L^{-1}\sum_{i=a}^{b_0}r_i}
\]
when the expression is nonzero.  Call these indices **good**.  Thus the
number of bad indices is \(o(L)\), and modal primes occupy a uniformly
\(1-o(1)\) fraction of every fixed positive-length subinterval of a good
band.

## 3. Prime-versus-semiprime ratio grids

Set
\[
 B=\left\lfloor\frac{1-4\alpha}{2}L\right\rfloor,
 \qquad I=[a,B]\cap\mathbb Z.                       \tag{18}
\]
For large \(N\), \(B>2a\).  If \(i,j\in I\), then both target indices
\(i+j\) and \(i+j+1\) are at most \(b_0\).

For a band \(\mathcal P_i\), define two fixed subbands
\[
 \mathcal P_i^-=(2^i,2^{i+1/4}]\cap\mathcal P,
 \qquad
 \mathcal P_i^+=(2^{i+3/4},2^{i+1}]\cap\mathcal P. \tag{19}
\]
If \(i\) is good, (3) and (17) imply
\[
 |C_i\cap\mathcal P_i^-|, |C_i\cap\mathcal P_i^+|
 \geq \kappa_\alpha\frac{2^i}{L}                  \tag{20}
\]
for some \(\kappa_\alpha>0\) and all large \(N\).

Take unordered \(i\leq j\) in \(I\).

* Products of one modal prime from each minus subband lie in the numerical
  dyadic interval \((2^{i+j},2^{i+j+1}]\), because
  \[
   2^{i+j}<pq\leq2^{i+j+1/2}.
  \]
* Products of one modal prime from each plus subband lie in the numerical
  dyadic interval \((2^{i+j+1},2^{i+j+2}]\), because
  \[
   2^{i+j+3/2}<pq\leq2^{i+j+2}.
  \]

When \(i=j\), use unordered distinct prime pairs.  Unique factorization
shows in every case that each family contains at least
\[
 \kappa'_\alpha\frac{2^{i+j}}{L^2}                 \tag{21}
\]
distinct semiprimes.

We now make one global allocation.  For every triple
\[
 (i,j,\varepsilon),\qquad i\leq j,\quad i,j\in I,\quad
 \varepsilon\in\{0,1\},                            \tag{22}
\]
for which the two source indices and the target
\[
 t=i+j+\varepsilon                                  \tag{23}
\]
are good, select
\[
 \left\lfloor\zeta\frac{2^{i+j}}{L^2}\right\rfloor \tag{24}
\]
semiprimes from the corresponding family, where \(\zeta>0\) is a
sufficiently small constant depending only on \(\alpha\).

For a fixed target \(t\), at most \(O(L)\) triples request a prime in
\(C_t\), and their total request is at most
\[
 C\zeta\frac{2^t}{L}.                               \tag{25}
\]
On the other hand, (3) and goodness give
\[
 |C_t|\geq c_\alpha\frac{2^t}{L}.                  \tag{26}
\]
Choosing \(\zeta<c_\alpha/(2C)\), assign to every selected semiprime a
different prime \(r\in C_t\).  Assignments for different target bands are
automatically disjoint.  Semiprimes belonging to different source triples
are distinct by unique factorization and the convention \(i\leq j\).

For every assigned pair
\[
 2^t<d=pq\leq2^{t+1},\qquad r\in C_t,              \tag{27}
\]
and every \(y\)-smooth
\[
 k\leq\frac{N}{2^{t+1}},                            \tag{28}
\]
make the edge
\[
 \{kd,kr\}.                                         \tag{29}
\]

All edges (29), over all source and target bands, are globally
vertex-disjoint.  The number \(kr\) has exactly one prime factor larger
than \(y\), while \(kd=kpq\) has exactly two, counted with multiplicity;
we chose distinct primes when \(i=j\).  Hence the two sides cannot collide.
Within either side, the prime or unordered prime pair larger than \(y\) is
recovered uniquely, that prime or semiprime was assigned only once, and
then \(k\) is recovered.

If
\[
 c_t\ne c_i+c_j,                                    \tag{30}
\]
then the endpoints of (29) have different \(f\)-values:
\[
 f(kr)=f(k)+c_t,qquad f(kd)=f(k)+c_i+c_j.           \tag{31}
\]
Thus every edge arising from a failed relation (30) meets the complement
of \(A\).

The smoothness parameters in (28) again range over a compact interval
depending only on \(\alpha\).  Consequently (4) gives
\[
 \Psi(N/2^{t+1},y)\geq d'_{\alpha}\frac{N}{2^t}.   \tag{32}
\]
Combining (24) and (32), every failed relation supplies at least
\(c_\alpha N/L^2\) disjoint edges.  Therefore, if \(\mathcal F\) is the
set of failed good relations among (22),
\[
 m\geq c_\alpha\frac{N}{L^2}|\mathcal F|.           \tag{33}
\]
By (2),
\[
 |\mathcal F|=o(L^2).                               \tag{34}
\]

There are only \(o(L)\) bad indices.  Pairs with a bad source number
o(L^2), and for each bad target there are only \(O(L)\) decompositions.
Thus (34) implies that, among all ordered \((i,j)\in I^2\), each of
\[
 c_i+c_j=c_{i+j},                                   \tag{35}
\]
and
\[
 c_i+c_j=c_{i+j+1}                                  \tag{36}
\]
fails only \(o(L^2)\) times.  Passing from unordered to ordered pairs only
changes constants.

## 4. The shifted-Cauchy stability lemma

We prove the exact stability statement needed above.

### Lemma

Let \(I=[A_0,B_0]\cap\mathbb Z\) have length \(n\to\infty\), and suppose
\(I\cap(I+I)\) has length \(\gg n\).  Let \(c\) take values in
\(\mathbb Q\) on \(I\cup(I+I+\{0,1\})\).  If
\[
 c_i+c_j=c_{i+j},\qquad c_i+c_j=c_{i+j+1}            \tag{37}
\]
each fail for only \(o(n^2)\) pairs \((i,j)\in I^2\), then
\[
 c_i=0                                               \tag{38}
\]
for all but \(o(n)\) indices in \(I\cup(I+I)\).

### Proof

Translate the intervals by writing
\[
 F(x)=c_{A_0+x}\quad(0\leq x<n),
 \qquad
 G(s)=c_{2A_0+s}\quad(0\leq s\leq2n-1).            \tag{39}
\]
Suppose the first equation in (37) has at most \(\epsilon n^2\)
exceptions, where \(\epsilon=o(1)\).  Thus
\[
 F(x)+F(z)=G(x+z)                                   \tag{40}
\]
for all but \(\epsilon n^2\) pairs.

For \(1\leq h\leq3n/4\), put
\[
 \Delta_h(x)=F(x+h)-F(x),\qquad0\leq x<n-h.         \tag{41}
\]
For \(x,z<n-h\), apply (40) to \((x+h,z)\) and
\((x,z+h)\).  Unless one of those two pairs is exceptional, their equal
sums give
\[
 \Delta_h(x)=\Delta_h(z).                           \tag{42}
\]
The two maps into the exceptional set are injective, so at most
\(2\epsilon n^2\) ordered pairs \((x,z)\) violate (42).  Since
\(n-h\geq n/4\), a largest value class of \(\Delta_h\) contains all but
\(O(\epsilon n)\) admissible \(x\).  Denote its value by \(d_h\).

If \(h,k,h+k\leq3n/4\), the interval of possible starting points for all
three increments has length at least \(n/4\).  Avoiding the three
\(O(\epsilon n)\)-sized exceptional sets, choose \(x\) for which
\[
 d_{h+k}=\Delta_{h+k}(x)
 =\Delta_h(x)+\Delta_k(x+h)=d_h+d_k.                \tag{43}
\]
For all sufficiently large \(n\), such an \(x\) exists.  Hence, with
\(u=d_1\),
\[
 d_h=hu\qquad(1\leq h\leq3n/4).                    \tag{44}
\]

Average over anchors \(r\in[n/4,n/2]\).  For a fixed separation
\(h\leq3n/4\), only \(O(\epsilon n)\) starting points have a nonmodal
increment.  Summing over \(h\), only \(O(\epsilon n^2)\) pairs \((r,x)\)
fail
\[
 F(x)-F(r)=u(x-r).                                  \tag{45}
\]
Some anchor \(r\) therefore has only \(O(\epsilon n)\) bad \(x\).  With
\(v=F(r)-ur\),
\[
 F(x)=ux+v                                           \tag{46}
\]
for all but \(O(\epsilon n)\) values of \(x\).

Let
\[
 T=\{s:0\leq s\leq2n-2,\ G(s)\ne us+2v\}.        \tag{47}
\]
Whenever \(s=x+z\), both inputs satisfy (46), and (40) holds, we have
\(G(s)=us+2v\).  Therefore
\[
 \sum_{s\in T}R(s)=O(\epsilon n^2),                \tag{48}
\]
where
\[
 R(s)=|\{(x,z)\in[0,n-1]^2:x+z=s\}|.
\]
The representation counts are
\(1,2,\ldots,n-1,n,n-1,\ldots,1\); the sum of the \(q\) smallest is at
least \(q^2/4\).  It follows that
\[
 |T|=O(\sqrt\epsilon\,n).                           \tag{49}
\]

Use now the second equation in (37).  Restricting harmlessly to
\(x+z+1\leq2n-2\), all but \(o(n^2)\) pairs \((x,z)\) simultaneously have
both inputs satisfying (46), the output \(x+z+1\) outside \(T\), and the
shifted equation valid.  (The omitted upper corner consists of just the
pair \((n-1,n-1)\).)  For one such pair,
\[
 u(x+z)+2v=F(x)+F(z)=G(x+z+1)=u(x+z+1)+2v,
\]
so
\[
 u=0.                                                \tag{50}
\]
Equations (46), (49), and (50) say that \(c=v\) at all but \(o(n)\)
points of \(I\), while \(c=2v\) at all but \(o(n)\) points of \(I+I\).
Their overlap has size \(\gg n\), so one point is exceptional to neither
description.  There \(v=2v\), hence \(v=0\).  This proves (38). \(\square\)

Apply the lemma with the interval (18).  Its length is \(\asymp L\), and
\[
 |I\cap(I+I)|=B-2a+O(1)
 =\left(\frac{1-8\alpha}{2}+o(1)\right)L\gg L.      \tag{51}
\]
Equations (35)--(36) therefore imply
\[
 c_i=0                                               \tag{52}
\]
for all but \(o(L)\) indices
\[
 i\in I\cup(I+I)=[a,2B]\cap\mathbb Z.              \tag{53}
\]

## 5. The middle active-prime mass vanishes

If (52) holds in band \(i\), every active prime in that band is nonmodal,
so there are at most \(r_i|\mathcal P_i|\) of them.  In the \(o(L)\)
exceptional bands, use all primes.  By (3), (16), and (52),
\[
 \begin{aligned}
 \sum_{\substack{y<p\leq 2^{2B+1}\\f(p)\ne0}}\frac1p
 &\leq
 \sum_{\substack{a\leq i\leq2B\\c_i=0}}
       \frac{r_i|\mathcal P_i|}{2^i}
 +\sum_{\substack{a\leq i\leq2B\\c_i\ne0}}
       \frac{|\mathcal P_i|}{2^i}  \\
 &=o(1).                                             \tag{54}
 \end{aligned}
\]
This is an exact-support statement: prime weights are not being declared
small; primes with nonzero weight have total reciprocal mass \(o(1)\).

Put
\[
 z=2^{2B+1}.                                        \tag{55}
\]
By (5) and the definition of \(B\),
\[
 \sum_{z<p\leq N}\frac1p
 =-\log(1-4\alpha)+o(1).                            \tag{56}
\]
The harmless floor and factor two in (55) disappear in the limit.

For uniform \(U_N\in[1,N]\), the union bound, (54), and (56) give
\[
 \Pr\bigl(p\mid U_N\text{ for some active }p>y\bigr)
 \leq -\log(1-4\alpha)+o(1).                       \tag{57}
\]
Define the small-prime part
\[
 S_y(n)=\sum_{p\leq y}f(p)v_p(n).                   \tag{58}
\]
If no active prime greater than \(y\) divides \(n\), then
\(f(n)=S_y(n)\) exactly.  Hence (2) and (57) imply
\[
 \Pr(S_y(U_N)=1)
 \geq1+\log(1-4\alpha)-o(1).                       \tag{59}
\]

No independence after conditioning is asserted here: we simply discard
the exceptional integers in (57), and then use the unconditional law of
\(S_y(U_N)\).

## 6. Small-prime total variation and an exact atom gap

### Lemma 1 (small-prime valuation transfer)

Let \(y=N^{1/u+o(1)}\), where \(u>1\) is fixed.  Let
\((G_p)_{p\leq y}\) be independent geometric variables with
\[
 \Pr(G_p=k)=(1-p^{-1})p^{-k},\qquad k\geq0.          \tag{60}
\]
There is \(\varepsilon(u)\to0\) as \(u\to\infty\) such that
\[
 d_{\rm TV}\left(
  \mathcal L((v_p(U_N))_{p\leq y}),
  \mathcal L((G_p)_{p\leq y})
 \right)
 \leq\varepsilon(u)+o_{N\to\infty}(1).             \tag{61}
\]

#### Proof

For an exponent vector with associated \(y\)-smooth integer
\(d=\prod_{p\leq y}p^{a_p}\), unique factorization gives the exact masses
\[
 \Pr((v_p(U_N))=(a_p))=\frac{\Phi(N/d,y)}N,         \tag{62}
\]
and
\[
 \Pr((G_p)=(a_p))=\frac{V(y)}d.                    \tag{63}
\]
If \(D=\prod_{p\leq y}p^{G_p}\), it follows that the total-variation
distance equals
\[
 \frac12\mathbb E\left|
  1_{D\leq N}\frac{D\Phi(N/D,y)}{NV(y)}-1
 \right|.                                           \tag{64}
\]

Let \(u_N=\log N/\log y=u+o(1)\), and take
\(s=u_N/2\).  On
\[
 D\leq N/y^s,                                       \tag{65}
\]
the ratio in (64) differs from one by at most
\(\eta(u/3)+o(1)\), say, by (7), for all large \(N\).

Moreover, (6) gives
\[
 \mathbb E\log D
 =\sum_{p\leq y}\frac{\log p}{p-1}
 =(1+o(1))\log y.                                   \tag{66}
\]
The logarithm of the boundary in (65) is
\((u_N/2)\log y\), so Markov's inequality yields
\[
 \Pr(D>N/y^s)\leq\frac{3}{u}                       \tag{67}
\]
for all sufficiently large \(N\).  For completeness, write
\(\delta_u=\eta(u/3)+o(1)\), let \(\mathcal I\) be the model event (65),
and put \(b=\Pr(D\notin\mathcal I)\).  If \(R(D)\) denotes the
Radon--Nikodym factor inside (64), then \(|R-1|\leq\delta_u\) on
\(\mathcal I\), and the actual boundary mass is at most
\[
 1-\mathbb E[1_{\mathcal I}R]\leq b+\delta_u.
\]
Consequently
\[
 2d_{\rm TV}
 \leq\delta_u+\mathbb E[1_{\mathcal I^c}(R+1)]
 \leq2\delta_u+2b.
\]
Together with (67), this proves (61), for example with
\[
 \varepsilon(u)=2\eta(u/3)+\frac6u,                \tag{68}
\]
after enlarging constants. \(\square\)

The important quantifier order is: \(u\) is fixed first, (61) has the
possibly positive error \(\varepsilon(u)\), and only afterward is
\(N\to\infty\).  We later choose one sufficiently large fixed \(u\).

### Lemma 2 (uniform nonzero atom gap for independent geometrics)

Let \(G_p\) be independent variables (60), and let \(w_p\in\mathbb Q\).
For
\[
 T=\sum_{p\leq y}w_pG_p,                            \tag{69}
\]
every nonzero atom satisfies
\[
 \Pr(T=t)\leq q_0<0.915,\qquad t\ne0,              \tag{70}
\]
where one may take
\[
 q_0=e^{-1/8}+\frac1{32}.                           \tag{71}
\]

#### Proof

Let
\[
 \Lambda=\sum_{w_p\ne0}\frac1p.                   \tag{72}
\]
If \(\Lambda<1/4\), then for \(t\ne0\),
\[
 \Pr(T=t)\leq\Pr(G_p>0\text{ for some }w_p\ne0)
 \leq\Lambda<\frac14.                              \tag{73}
\]

Suppose \(\Lambda\geq1/4\).  If some active prime has \(1/p\geq1/8\),
the largest atom of \(w_pG_p\) is \(1-1/p\leq7/8\).  Convolution with
independent variables cannot increase the largest atom, proving (70).

Otherwise every active \(1/p<1/8\).  Greedily choose a set \(E\) of active
primes for which
\[
 \frac18\leq\lambda:=\sum_{p\in E}\frac1p<\frac14. \tag{74}
\]
Let
\[
 T_E=\sum_{p\in E}w_pG_p,
 \qquad K=|\{p\in E:G_p>0\}|.
\]
If \(K=1\), then \(T_E\ne0\), irrespective of signs or magnitudes.
Therefore
\[
 \Pr(T_E=0)
 \leq\Pr(K=0)+\Pr(K\geq2)
 \leq e^{-\lambda}+\mathbb E\binom K2
 \leq e^{-1/8}+\frac{\lambda^2}{2}
 <e^{-1/8}+\frac1{32}.                              \tag{75}
\]
Every nonzero atom of \(T_E\) is at most
\[
 \Pr(K\geq1)\leq\mathbb EK=\lambda<\frac14.        \tag{76}
\]
Thus the largest atom of \(T_E\) is at most \(q_0\); convolution with the
remaining independent summands proves (70). \(\square\)

By data processing, Lemma 1 and Lemma 2 apply to arbitrary weights
depending on \(N\).  With
\[
 T_y=\sum_{p\leq y}f(p)G_p,                         \tag{77}
\]
we obtain
\[
 \Pr(S_y(U_N)=1)
 \leq q_0+\varepsilon(1/\alpha)+o(1).               \tag{78}
\]

## 7. Contradiction and uniformity

Since \(q_0<1\), choose the fixed \(\alpha>0\) in (8) sufficiently small
that
\[
 -\log(1-4\alpha)<\frac{1-q_0}{3},
 \qquad
 \varepsilon(1/\alpha)<\frac{1-q_0}{3}.            \tag{79}
\]
This is possible by Lemma 1.  Equations (59), (78), and (79) are
incompatible for large \(N\): the lower bound in (59) exceeds the upper
bound in (78) by at least \((1-q_0)/3-o(1)\).  This contradicts (2).

We have proved that no sequence of nonzero levels can have density tending
to one.  This qualitative contradiction implies the uniform assertion
(1): otherwise, for every integer \(j\), choose \(N_j\geq j\), a grading,
and a nonzero level of density greater than \(1-1/j\), producing exactly
the forbidden sequence.

## 8. Audit checklist and limitations

1. **Global disjointness.**  Within each of the two matching constructions,
   every lifted endpoint is classified by its complete multiset of prime
   factors greater than \(y\).  Same-band edges have one such factor;
   ratio-grid edges pair a one-factor pattern with a two-factor pattern.
   Assigned target primes and selected semiprimes are never reused.  The
   matchings of Sections 2 and 3 need not be mutually disjoint, since their
   lower bounds (15) and (33) are invoked separately.
2. **Floors.**  The lower band starts at
   \(a=\lceil\alpha\log_2N\rceil\), so every source prime is strictly
   larger than the smoothness cutoff \(y=2^a\).  Using a floor here would
   leave a genuine gap in the collision argument.
3. **Moving weights.**  No compactness of the rational weights is used.
   Only exact equality or inequality of weights matters.
4. **Exceptional middle primes.**  The proof obtains reciprocal mass
   \(o(1)\), not merely numerically small weights.  Integers divisible by
   one of those exactly active primes are discarded by a union bound.
5. **Boundary/product model.**  The independent model is used only for
   primes \(p\leq N^\alpha\), with the fixed error
   \(\varepsilon(1/\alpha)\).  The large-prime remainder is never assumed
   independent.  This avoids the square-root-threshold counterexample.
6. **Unverified standard input.**  The only item that should be checked
   against a standard reference before promotion is the uniform
   rough-number estimate (7).  The derivation (62)--(68) makes clear the
   exact strength required; no web lookup was used in this solving run.
7. **Convention.**  This theorem resolves only the repetition-allowed
   finite reading, through the additive-grading equivalence.  It does not
   address the internally repetition-free variant.
