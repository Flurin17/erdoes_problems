# Partial proof: a coupled lower bound for Erdős Problem #425

## Status

This is a dependency-complete **partial result**, not a solution of the
constant problem.  It proves that there is an absolute \(\eta>0\) such that
\[
 \liminf_{n\to\infty}
 \frac{F(n)-\pi(n)}
      {n^{3/4}(\log n)^{-3/2}}
 \ge c_0+\eta,
 \qquad
 c_0=\frac{2^{11/4}}{3^{3/4}}=2.951151\ldots .
\]
It also gives an explicit subsequence on which the normalized excess is at
least an exact radical constant
\[
 c_*=3.0009864793\ldots>3.
\]
It does not prove a matching upper bound, the existence of the limit, or the
fixed-\(r\) assertion.

All logarithms are natural.

## 1. Two graph lemmas

### Lemma 1 (semiprime replacement)

Let \(X,Y\) be disjoint prime sets, let \(G\subseteq X\times Y\) be
\(C_4\)-free, and suppose \(xy\le n\) for every \(xy\in E(G)\).  Then
\[
 A_G=\bigl(\{p\le n:p\text{ prime}\}\setminus(X\cup Y)\bigr)
       \cup\{xy:(x,y)\in E(G)\}
\]
has distinct products on its unordered pairs of distinct elements.

Proof.  Unique factorization makes the edge labels distinct.  In an equality
between products of two members of \(A_G\), the two sides contain the same
number of semiprime members, because their total numbers of prime factors
counted with multiplicity agree.  Prime-prime equalities are trivial.
A prime-semiprime equality decodes uniquely because the retained prime class
is disjoint from \(X\cup Y\). Finally, compare the multisets of \(X\)- and
\(Y\)-endpoints in two semiprime pairs. If either endpoint multiset is
repeated, those multisets already determine the unordered edge pair uniquely.
If both contain two distinct vertices, the only different pairing is the
other perfect matching, and the four edges form a \(C_4\).  ∎

### Lemma 2 (rectangular \(C_4\)-free graphs)

Suppose \(m=m(N)\le N\), \(m,N\to\infty\), and \(m/N\) is bounded below by a
positive constant.  There is a \(C_4\)-free bipartite graph with part sizes
\(m,N\) and
\[
 e=(1+o(1))m\sqrt N.
\]

Proof.  Choose the least prime \(q\ge\sqrt N\).  The prime number theorem
implies \(q=(1+o(1))\sqrt N\).  The point-line incidence graph of the
projective plane of order \(q\) is \(C_4\)-free, has
\(v=q^2+q+1=(1+o(1))N\) vertices on each side, and is \((q+1)\)-regular.
Choose uniformly an exact \(m\)-subset on one side and an exact \(N\)-subset
on the other.  The expected retained edge count is
\[
 v(q+1)\frac m v\frac N v=(1+o(1))m\sqrt N.
\]
Some restriction attains at least its expectation.  ∎

The only standard inputs are the prime number theorem and the elementary
finite-projective-plane construction over a prime field.

## 2. The interval architecture

Put
\[
 L_n=\frac{\sqrt n}{\log n}.
\]
Choose numbers
\[
 b_{-1}>b_0>b_1>\cdots>0,\qquad b_{-1}b_0=1.
\]
For a fixed integer \(J\ge0\), define disjoint prime intervals
\[
 X_j=\{p:b_{j+1}\sqrt n<p\le b_j\sqrt n\},
\]
\[
 Y_j=\{p:\sqrt n/b_{j-1}<p\le\sqrt n/b_j\}
 \qquad(0\le j\le J).
\]
Every \(x\in X_j\), \(y\in Y_j\) satisfies \(xy\le n\).  For fixed \(J\),
the prime number theorem gives
\[
 |X_j|=(2x_j+o(1))L_n,\qquad
 |Y_j|=(2y_j+o(1))L_n,
\]
where
\[
 x_j=b_j-b_{j+1},\qquad
 y_j=\frac1{b_j}-\frac1{b_{j-1}}.
\]
When \(x_j\le y_j\), Lemma 2 supplies a \(C_4\)-free component with
\[
 e_j=(2\sqrt2\,x_j\sqrt{y_j}+o(1))L_n^{3/2}.
\]
The components have disjoint vertex sets, so their union is \(C_4\)-free.
Lemma 1 then gives
\[
 |A|=\pi(n)+
 \left(2\sqrt2\sum_{j=0}^{J}x_j\sqrt{y_j}+o(1)\right)L_n^{3/2},
\]
because deleting the \(O_J(L_n)\) endpoint primes is lower order.

## 3. Exact optimization

Write
\[
 r_j=\frac{b_j}{b_{j-1}}\quad(j\ge0).
\]
Then
\[
 S:=\sum_{j\ge0}x_j\sqrt{y_j}
 =\sum_{j\ge0}\sqrt{b_j}(1-r_{j+1})\sqrt{1-r_j}.
\]

For \(r,s\in(0,1)\),
\[
 (1-s)\sqrt{1-r}+\sqrt{s(2-s)}\le\sqrt{2-r}.                 \tag{1}
\]
Indeed, with \(a=\sqrt{1-r}\) and \(u=1-s\), the left side is
\[
 au+\sqrt{1-u^2}\le\sqrt{a^2+1}
\]
by Cauchy--Schwarz.  Equality holds exactly when
\[
 1-s=\sqrt{\frac{1-r}{2-r}}.                                \tag{2}
\]

Multiplying (1), with \(r=r_j,s=r_{j+1}\), by \(\sqrt{b_j}\) and
telescoping gives
\[
 S\le\sqrt{b_0}\sqrt{2-r_0}.
\]
Since \(b_{-1}b_0=1\), \(r_0=b_0^2\), and hence
\[
 S^2\le b_0(2-b_0^2).
\]
The right side is maximized at \(b_0=\sqrt{2/3}\), giving
\[
 \sup S=\left(\frac{32}{27}\right)^{1/4}
       =\frac{2^{5/4}}{3^{3/4}}.                             \tag{3}
\]

Equality is achieved by
\[
 b_{-1}=\sqrt{\frac32},\qquad b_0=\sqrt{\frac23},
\]
and, writing \(\delta_j=1-r_j\), recursively taking
\[
 \delta_0=\frac13,\qquad
 \delta_{j+1}=\sqrt{\frac{\delta_j}{1+\delta_j}},\qquad
 b_{j+1}=(1-\delta_{j+1})b_j.                                \tag{4}
\]
The map \(f(t)=\sqrt{t/(1+t)}\) is increasing, and
\(f(t)>t\) exactly for \(0<t<(\sqrt5-1)/2\). Hence the sequence
\(\delta_j\) increases to the unique positive fixed point
\((\sqrt5-1)/2\). Consequently \(r_j\) tends to
\((3-\sqrt5)/2<1\), so \(b_j\to0\) geometrically and the terminal Bellman
potential vanishes.

It remains to check the orientation \(x_j\le y_j\).  Put
\[
 R_j=\frac{\delta_j}{\delta_{j+1}}
    =\sqrt{\delta_j(1+\delta_j)}.
\]
At \(j=0\), \(b_0^2=R_0=2/3\).  Since \(\delta_j\) increases, \(R_j\)
increases, while
\[
 b_{j+1}^2=b_j^2(1-\delta_{j+1})^2<R_j<R_{j+1}.
\]
Induction gives \(b_j^2\le R_j\), and therefore
\[
 \frac{x_j}{y_j}
 =\frac{b_j^2\delta_{j+1}}{\delta_j}\le1.
\]

## 4. Conclusion

For every \(\varepsilon>0\), choose \(J\) so the first \(J+1\) terms of
(3)--(4) are within \(\varepsilon/(2\sqrt2)\) of \(S\).  Keep this \(J\)
fixed and let \(n\to\infty\).  The construction in Section 2 then gives
\[
 F(n)\ge\pi(n)+
 \left(\frac{2^{11/4}}{3^{3/4}}-\varepsilon+o(1)\right)
 \frac{n^{3/4}}{(\log n)^{3/2}}.
\]
Since \(\varepsilon\) is arbitrary, the asserted liminf bound follows.

The architecture is optimized only among these disjoint interval-incidence
components.  Sections 5--7 construct a coupled two-level component that
strictly improves it; no matching global upper bound is claimed.

## 5. An exact binary mixed-rank graph

Let \(q=2^k\), let \(F=\mathbb F_q\), and write
\(\operatorname{Tr}:F\to\mathbb F_2\) for the absolute trace.  Choose
\(\gamma\in F\) with \(\operatorname{Tr}(\gamma)=1\), put
\(\sigma(b)=b^{q/2}\), and set
\[
 G=F\oplus\mathbb F_2,\qquad H=F\oplus0.
\]
For \(a,b\in F\), define the \(\mathbb F_2\)-linear maps
\[
 S_a(x)=ax,\qquad
 T_b(x,t)=
 \left(bx+t\sigma(b),\operatorname{Tr}(\gamma\sigma(b)x)\right).
\]

### Lemma 3 (three full-rank conditions)

If \(a\ne a'\), then \(S_a-S_{a'}\) is invertible.  If \(b\ne b'\),
then \(T_b-T_{b'}\) is invertible.  If \(a\ne b\), then
\[
 x\longmapsto T_b(x,0)-(S_a(x),0)                              \tag{5}
\]
is injective from \(F\) to \(G\).

Proof.  The first assertion is immediate.  The assignment \(b\mapsto T_b\)
is \(\mathbb F_2\)-linear, so for the second assertion it suffices to show
that \(T_d\) is invertible when \(d\ne0\).  Put \(r=\sigma(d)\), so
\(r^2=d\).  If \(T_d(x,t)=0\), then
\[
 r^2x+tr=0,\qquad \operatorname{Tr}(\gamma r x)=0.
\]
The first equation gives \(x=t/r\), and the second then gives
\(t\operatorname{Tr}(\gamma)=t=0\).  Thus \(x=0\).  Finally, the first
coordinate of (5) is \((b-a)x\), proving injectivity.  ∎

Choose disjoint direction sets \(A_0,B_0\subseteq F\), with \(0\notin B_0\).
Take the right vertex set \(Y=G^2\), partitioned as
\[
 Y_1=H^2,\qquad Y_2=Y\setminus Y_1.
\]
For \((a,c)\in A_0\times F\), make a type-1 left vertex whose neighborhood is
\[
 L^1_{a,c}=\{((x,0),(S_a(x)+c,0)):x\in F\}\subseteq Y_1.       \tag{6}
\]
For \((b,d)\in B_0\times G\), make a type-2 left vertex whose neighborhood is
\[
 L^2_{b,d}=\{(z,T_b(z)+d):z\in G\}.                            \tag{7}
\]

### Lemma 4 (typed \(C_4\)-free graph)

The graph (6)--(7) is \(C_4\)-free and has
\[
 |X_1|=|A_0|q,\quad |X_2|=2|B_0|q,\quad
 |Y_1|=q^2,\quad |Y_2|=3q^2.                                  \tag{8}
\]
Every type-1 vertex has degree \(q\), and every type-2 vertex has degree
\(2q\).  Each type-2 neighborhood contains exactly \(q/2\) points of
\(Y_1\) and \(3q/2\) points of \(Y_2\).

Proof.  Two affine graphs with the same linear part and different intercepts
are disjoint.  Intersections with different linear parts are solution sets of
one difference-map equation.  Lemma 3 shows that such an equation has at
most one solution both within either type and across the two types.  Thus two
distinct left vertices have at most one common neighbor, which is equivalent
to \(C_4\)-freeness.  The counts and total degrees are immediate.

For the last assertion, a point of (7) belongs to \(Y_1\) only when its first
coordinate is \((x,0)\).  Its second coordinate then belongs to \(H\) when
one affine equation in the nonzero functional
\(x\mapsto\operatorname{Tr}(\gamma\sigma(b)x)\) holds.  Because
\(b\ne0\), this equation has exactly \(q/2\) solutions.  ∎

## 6. A subsequence constant exceeding three

Continue with the equality sequence (4).  Direct evaluation gives
\[
 \delta_1=\frac12,\qquad \delta_2=\frac1{\sqrt3},\qquad
 \delta_3=d:=\sqrt{\frac{\sqrt3-1}{2}},
\]
\[
 b_1=\frac1{\sqrt6},\qquad
 b_2=\frac{\sqrt3-1}{\sqrt{18}}.
\]
For Bellman levels \(1,2\), write
\[
 x=x_1=\frac1{\sqrt{18}},\qquad y=y_1=\sqrt{\frac32},
\]
\[
 z=x_2=b_2d,\qquad
 w=y_2=\frac{\sqrt6+3\sqrt2}{2},\qquad c=\frac w3.             \tag{9}
\]
The separate components contribute
\[
 D=x\sqrt y+z\sqrt w                                          \tag{10}
\]
in units of \(U(n)^{3/2}\), where
\[
 U(n)=\frac{2\sqrt n}{\log n}.
\]

We apply Lemma 4 with its four vertex classes embedded, respectively, into
the prime intervals \(X_1,X_2,Y_1,Y_2\).  These are legitimate edge types:
\[
 X_1Y_1,\qquad X_2Y_1,\qquad X_2Y_2,                            \tag{11}
\]
because the upper endpoints in each product are at most \(n\).  The formulas
in (9) give \(c<y\) and
\[
 \frac{x+z/2}{c}<1.                                           \tag{12}
\]

Fix \(0<\lambda<1\) sufficiently close to one.  As \(q=2^k\to\infty\),
choose integers \(n\to\infty\) so that
\[
 q^2=(\lambda c+o(1))U(n).                                    \tag{13}
\]
This is possible because \(U(t)\) is continuous and increasing for large
real \(t\), and replacing a real solution by a neighboring integer changes
it by a relative \(o(1)\).  The prime number theorem and the strict resource
slack give enough primes for \(q^2\) vertices in \(Y_1\) and \(3q^2\)
vertices in \(Y_2\).  Choose the direction sets so that
\[
 |A_0|q=(x+o(1))U(n),\qquad 2|B_0|q=(z+o(1))U(n).              \tag{14}
\]
Floors and a vanishing safety margin absorb the prime-number-theorem errors.
Condition (12)--(13) gives \(|A_0|+|B_0|\le q\), so the direction sets may be
chosen disjoint with \(0\notin B_0\).

By (8), the mixed component has
\[
 |A_0|q^2+4|B_0|q^2
 =\left((x+2z)\sqrt{\lambda c}+o(1)\right)U(n)^{3/2}           \tag{15}
\]
edges.  Use a fixed Bellman truncation, replace levels \(1,2\) by this mixed
component, and retain every other component.  The prime vertex sets are
disjoint, so the union is \(C_4\)-free; Lemma 1 excludes every product
collision.  Formally, choose \(\lambda_m\uparrow1\) and truncation indices
\(J_m\to\infty\), then choose \(q_m\) sufficiently large that the PNT errors
on the finitely many intervals through \(J_m\) are smaller than all resource
slack.  This diagonal sequence loses neither the mixed coefficient nor the
Bellman tail.  Since
\[
 U(n)^{3/2}=2\sqrt2\,n^{3/4}(\log n)^{-3/2},
\]
we obtain
\[
 \limsup_{n\to\infty}
 \frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}
 \ge c_*,                                                       \tag{16}
\]
where
\[
 c_*=\frac{2^{11/4}}{3^{3/4}}
 +2\sqrt2\left[(x+2z)\sqrt{\frac w3}-x\sqrt y-z\sqrt w\right]. \tag{17}
\]

For completeness, (17) is strictly greater than \(3\) by exact rational
bounds.  Since \(y/w=d^2\) and \(z=x(\sqrt3-1)d\), its increment over
\(c_0\) simplifies to
\[
 \frac23\sqrt{\frac w3}\left(1-(5-2\sqrt3)d\right).           \tag{18}
\]
First,
\[
 c_0>\frac{2951}{1000},\qquad
 27\cdot2951^4=2047578695373627<2048\cdot10^{12}.
\]
Next \(\sqrt3<17321/10000\), by squaring, and therefore
\[
 ((5-2\sqrt3)d)^2=\frac{57\sqrt3-97}{2}<0.86485<0.93^2.
\]
Thus the last parenthesis in (18) exceeds \(7/100\).  Finally
\(\sqrt6>61/25\) and \(\sqrt2>141/100\), also by squaring, imply
\[
 w>\frac{667}{200}>\frac{1323}{400},\qquad
 \sqrt{w/3}>\frac{21}{20}.
\]
The increment in (18) is consequently greater than \(49/1000\), and hence
\[
 c_*>\frac{2951+49}{1000}=3.
\]

## 7. Removing the power-of-two phase loss

It remains to obtain a strict gain for every sufficiently large \(n\), not
only along (13).  For general adjacent Bellman levels put
\[
 x_j=b_j\delta_{j+1},\qquad y_j=\frac{\delta_j}{b_j},\qquad
 c_j=\frac{y_{j+1}}3,
\]
\[
 D_j=x_j\sqrt{y_j}+x_{j+1}\sqrt{y_{j+1}},\qquad
 C_j=(x_j+2x_{j+1})\sqrt{c_j}.                                \tag{19}
\]
Here \(D_j\) is the old two-level coefficient and \(C_j\) is the exact-scale
mixed coefficient, both in units of \(U(n)^{3/2}\).

Let
\[
 \delta=\frac{\sqrt5-1}{2},\qquad r=1-\delta=\delta^2.
\]
The recurrence in (4) converges geometrically to \(\delta\).  Indeed, the
derivative of \(t\mapsto\sqrt{t/(1+t)}\) at its fixed point is
\(1/(2(1+\delta))<1\).  The resulting relative errors in
\(b_{j+1}/b_j\) are summable, so for some \(B>0\),
\[
 b_j=B\delta^{2j}(1+o(1)).                                    \tag{20}
\]
Using (19)--(20) and \(\sqrt r=\delta\) gives
\[
 \frac{C_j}{D_j}\longrightarrow
 \frac{1+2r}{\sqrt{3r}(1+\sqrt r)}
 =\frac{4-\sqrt5}{\sqrt3}>1.                                 \tag{21}
\]
The last inequality reduces, after two positive squarings, to \(81>80\).
Moreover, the recurrence gives
\[
 \frac{y_{j+1}}{y_j}=1+\frac1{\delta_{j+1}}<3                 \tag{22}
\]
for all sufficiently large \(j\), and
\[
 \frac{x_j+x_{j+1}/2}{c_j}\longrightarrow0.                  \tag{23}
\]

Choose \(\rho>0\), \(J_0\), and then \(0<a<b<1\) so that, for every
\(j\ge J_0\),
\[
 C_j\ge(1+\rho)D_j,\qquad
 x_j+x_{j+1}/2<2^{-2b}c_j,\qquad
 2^{-b}(1+\rho)>1.                                            \tag{24}
\]
Enlarge \(J_0\) if needed so that (22) has fixed positive slack.  Define
\[
 \theta_j=\frac12\log_2c_j.
\]
Equation (20) implies
\[
 \theta_j=j(-\log_2\delta)+C+o(1).                            \tag{25}
\]
The number \(-\log_2\delta\) is irrational.  Otherwise
\(\delta^v=2^{-u}\) for positive integers \(u,v\); norms from
\(\mathbb Q(\sqrt5)\) to \(\mathbb Q\) would give
\((-1)^v=2^{-2u}\), which is impossible.  The elementary density theorem
for an irrational rotation, together with the \(o(1)\) in (25), shows that
every tail of \((\theta_j\bmod1)\) is dense.

For \(j\ge J_0\), let
\[
 E_j=\{\tau\in\mathbb R/\mathbb Z:
          \{\tau+\theta_j\}\in(a,b)\}.
\]
These open sets cover the circle.  By compactness, a fixed finite set
\(I\subseteq\{J_0,J_0+1,\ldots\}\) already gives a subcover.  For any large
\(n\), put \(\tau=\tfrac12\log_2U(n)\), choose \(j\in I\) with
\(\tau\in E_j\), and set
\[
 q=2^{\lfloor\theta_j+\tau\rfloor},\qquad
 \lambda=\frac{q^2}{c_jU(n)}.
\]
Then
\[
 2^{-2b}<\lambda<2^{-2a}<1.                                  \tag{26}
\]

Equations (22), (24), and (26) give constant slack for all four graph parts:
\[
 q^2<y_jU(n),\qquad 3q^2<y_{j+1}U(n),\qquad
 \frac{x_jU(n)}q+\frac{x_{j+1}U(n)}{2q}<q.                   \tag{27}
\]
Because \(I\) is finite, the prime number theorem is uniform over all the
intervals now in use.  After inserting vanishing safety margins and taking
floors, Lemma 4 embeds with source sizes
\((x_j+o(1))U(n)\), \((x_{j+1}+o(1))U(n)\) and right sizes
\(q^2,3q^2\).  Floors and deleted endpoints cost only
\(O(U(n))=o(U(n)^{3/2})\).  The gain over the two old components is at least
\[
 \sqrt\lambda C_j-D_j
 \ge\left(2^{-b}(1+\rho)-1\right)D_j.                         \tag{28}
\]
The minimum \(g\) of the right side over the finite set \(I\) is positive.

Finally, choose a fixed Bellman truncation beyond \(\max I+1\) whose omitted
tail is less than \(g/2\).  For each \(n\), replace the selected components
\(j,j+1\) by the mixed component and retain every other component in the
truncation.  The components have disjoint prime vertex sets, and (11), with
the indices shifted to \(j,j+1\), lists every mixed edge type.  Hence every
edge product is at most \(n\), the union is \(C_4\)-free, and Lemma 1 applies.
After the uniform prime-number-theorem error becomes smaller than the
remaining fixed gain, (28) proves that some absolute \(\eta>0\) satisfies
\[
 \liminf_{n\to\infty}
 \frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}
 \ge \frac{2^{11/4}}{3^{3/4}}+\eta.
\]
The finite phase cover is chosen first, the Bellman truncation second, and
only then is \(n\) allowed to tend to infinity; thus no uniform prime number
theorem over a growing family of intervals is being assumed.
