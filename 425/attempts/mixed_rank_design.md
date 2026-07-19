# Route: binary mixed-rank design and a larger lower bound

## Exact finite typed design

Let \(q=2^k\), \(F=\mathbb F_q\), and let
\(\operatorname{Tr}:F\to\mathbb F_2\) be the absolute trace. Choose
\(\gamma\in F\) with \(\operatorname{Tr}(\gamma)=1\), put
\(\sigma(b)=b^{q/2}\), and write \(G=F\oplus\mathbb F_2\), with
\(H=F\oplus0\). Define
\[
 S_a(x)=ax,\qquad
 T_b(x,t)=
 \left(bx+t\sigma(b),\operatorname{Tr}(\gamma\sigma(b)x)\right).
\]

### Lemma 1 (mixed full-rank differences)

If \(a\ne a'\), then \(S_a-S_{a'}\) is invertible. If \(b\ne b'\), then
\(T_b-T_{b'}\) is invertible. Finally,
\[
 x\longmapsto T_b(x,0)-(S_a(x),0)
\]
is injective \(F\to G\) whenever \(a\ne b\).

Proof. The first assertion is immediate. The map \(b\mapsto T_b\) is
\(\mathbb F_2\)-linear, so it is enough to prove that \(T_d\) is invertible
for \(d\ne0\). Put \(r=\sigma(d)\), so \(r^2=d\). If
\(T_d(x,t)=0\), then
\[
 r^2x+tr=0,\qquad \operatorname{Tr}(\gamma r x)=0.
\]
The first equation gives \(x=t/r\), and the second gives
\(0=t\operatorname{Tr}(\gamma)=t\). Thus \(t=x=0\). For the mixed map,
its first coordinate is \((a+b)x\), which vanishes only at \(x=0\) when
\(a\ne b\). \(\square\)

Choose disjoint sets \(A,B\subseteq F\), with \(0\notin B\). Let
\[
 Y=G\times G,\qquad Y_1=H\times H,\qquad Y_2=Y\setminus Y_1.
\]
For every \((a,c)\in A\times F\), make a type-\(X_1\) left vertex with
neighborhood
\[
 L^1_{a,c}=
 \{((x,0),(S_a(x)+c,0)):x\in F\}\subseteq Y_1.
\]
For every \((b,d)\in B\times G\), make a type-\(X_2\) left vertex with
neighborhood
\[
 L^2_{b,d}=\{(z,T_b(z)+d):z\in G\}\subseteq Y.
\]

### Theorem 2 (typed \(C_4\)-free graph)

The resulting bipartite graph is \(C_4\)-free and has
\[
 |X_1|=|A|q,\quad |X_2|=2|B|q,\quad
 |Y_1|=q^2,\quad |Y_2|=3q^2.
\]
Every \(X_1\)-vertex has degree \(q\), and every \(X_2\)-vertex has degree
\(2q\). Because \(0\notin B\), every \(X_2\)-neighborhood has exactly
\(q/2\) points in \(Y_1\) and \(3q/2\) in \(Y_2\).

Proof. Two affine graphs with the same linear part and different intercepts
are disjoint. The intersection of two affine graphs with distinct linear
parts is the solution set of one difference-map equation. Lemma 1 shows
that this has at most one solution within either type and across the two
types. Thus two distinct left vertices have at most one common right
neighbor. The counts and degrees are immediate. For \(b\ne0\), membership
of \(((x,0),T_b(x,0)+d)\) in \(Y_1\) imposes one nonzero trace-functional
equation on \(x\), hence has \(q/2\) solutions. \(\square\)

The construction permits any densities
\[
 |A|/q\to\alpha,\qquad |B|/q\to\beta,\qquad \alpha+\beta<1.
\]

## The first two Bellman levels

For the first two relevant levels of the Bellman sequence in PROOF.md, put
\[
 x=\frac1{\sqrt{18}},\quad y=\sqrt{\frac32},\quad
 d=\sqrt{\frac{\sqrt3-1}{2}},\quad
 b_2=\frac{\sqrt3-1}{\sqrt{18}},
\]
\[
 z=b_2d,\qquad w=\frac{\sqrt6+3\sqrt2}{2},\qquad Y_*=\frac w3.
\]
At exact scale matching the old coefficient
\[
 C_{\rm diag}=x\sqrt y+z\sqrt w
\]
is replaced by
\[
 C_{\rm mix}=(x+2z)\sqrt{\frac w3}.
\]
This is a strict improvement. Since \(y/w=d^2\) and
\(z=x(\sqrt3-1)d\), the inequality reduces to
\[
 (5-2\sqrt3)d<1.
\]
After squaring, this is
\[
 \frac{57\sqrt3-97}{2}<1,
\]
equivalently \(19\sqrt3<33\), whose square is \(1083<1089\).

## Prime-interval application on a subsequence

Put \(U(n)=2\sqrt n/\log n\). For every fixed reciprocal interval, the
prime number theorem gives its number of primes as its normalized length
times \(U(n)(1+o(1))\).

Fix \(0<\lambda<1\) sufficiently close to one. Choose
\(q=2^k\to\infty\) and integers \(n_k\to\infty\) so that
\[
 q^2=(\lambda Y_*+o(1))U(n_k).
\]
The strict factor \(\lambda\) absorbs the prime-number-theorem errors on the
type-\(Y_2\) interval; later let \(\lambda\uparrow1\) along a diagonal
sequence. Choose
\[
 |A|=\left\lfloor\frac{(x-o(1))U(n_k)}q\right\rfloor,\qquad
 |B|=\left\lfloor\frac{(z-o(1))U(n_k)}{2q}\right\rfloor.
\]
The inequality
\[
 \frac{x+z/2}{\lambda Y_*}<1
\]
holds for \(\lambda\) sufficiently close to one and ensures
\(|A|+|B|\le q\). Theorem 2 then labels a \(C_4\)-free graph on
subsets of the four prime intervals. Its edge count is
\[
 |A|q^2+4|B|q^2
 =(x+2z+o(1))U(n_k)q
 =(\sqrt\lambda C_{\rm mix}+o(1))U(n_k)^{3/2}.
\]
All unused primes are retained; only graph endpoints are deleted. The graph
uses only \(X_1Y_1,X_2Y_1,X_2Y_2\), so its semiprimes are at most \(n_k\).
The collision proof in PROOF.md applies unchanged to its disjoint union with
all other components in a fixed reciprocal-annulus truncation. Letting the
truncation tend to infinity after the fixed-interval PNT limit, and then
letting \(\lambda\uparrow1\), loses nothing from the displayed limsup.

Since
\[
 U(n)^{3/2}=2\sqrt2\,n^{3/4}(\log n)^{-3/2},
\]
this proves
\[
 \limsup_{n\to\infty}
 \frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}
 \ge c_*,
\]
where
\[
 c_*
 =\frac{2^{11/4}}{3^{3/4}}
  +2\sqrt2\left[
    (x+2z)\sqrt{\frac w3}-x\sqrt y-z\sqrt w
  \right]
 =3.0009864793225986\ldots>3.
\]
The inequality with \(3\) has a rational certificate.  The increment over
\(c_0\) simplifies to
\[
 \frac23\sqrt{\frac w3}
 \left(1-(5-2\sqrt3)d\right).                                 \tag{4}
\]
Now \(c_0>2951/1000\), because
\[
 27\cdot2951^4=2047578695373627<2048\cdot10^{12}.
\]
Also \(\sqrt3<17321/10000\), as is checked by squaring, and hence
\[
 ((5-2\sqrt3)d)^2=\frac{57\sqrt3-97}{2}
 <0.86485<0.93^2.
\]
Thus the parenthesis in (4) exceeds \(7/100\).  Finally
\(\sqrt6>61/25\) and \(\sqrt2>141/100\), again by squaring, give
\(w>667/200>1323/400\), so \(\sqrt{w/3}>21/20\).  Therefore (4) is
greater than \(49/1000\), and
\[
 c_*>\frac{2951}{1000}+\frac{49}{1000}=3.
\]
The exact radical expression, not the decimal, is the theorem.

## Removing the power-of-two phase loss

The same design gives a strict improvement for every sufficiently large
\(n\), although no single Bellman pair works for every phase.  For the
Bellman sequence write
\[
 x_j=b_j\delta_{j+1},\qquad y_j=\frac{\delta_j}{b_j},
 \qquad c_j=\frac{y_{j+1}}3,
\]
and put
\[
 D_j=x_j\sqrt{y_j}+x_{j+1}\sqrt{y_{j+1}},\qquad
 C_j=(x_j+2x_{j+1})\sqrt{c_j}.
\]
Thus \(D_j\) is the coefficient, in units of \(U(n)^{3/2}\), of the two
separate Bellman components at levels \(j,j+1\), while \(C_j\) is the
coefficient of the mixed component when \(q^2=c_jU(n)\).

Let
\[
 \delta=\frac{\sqrt5-1}{2},\qquad r=1-\delta=\delta^2.
\]
The recurrence for \(\delta_j\) converges geometrically to \(\delta\), and
there is a constant \(B>0\) such that
\[
 b_j=B\delta^{2j}(1+o(1)).                                      \tag{5}
\]
Indeed the derivative of \(t\mapsto\sqrt{t/(1+t)}\) at its fixed point is
\(1/(2(1+\delta))<1\), and the resulting errors in
\(b_{j+1}/b_j\) are summable.  Consequently
\[
 \frac{C_j}{D_j}\longrightarrow
 \frac{1+2r}{\sqrt{3r}(1+\sqrt r)}
 =\frac{4-\sqrt5}{\sqrt3}>1.                                  \tag{6}
\]
The last strict inequality is equivalent, after two positive squarings, to
\(81>80\).

There is also ample room for all four vertex classes.  Directly from the
Bellman recurrence,
\[
 \frac{y_{j+1}}{y_j}=1+\frac1{\delta_{j+1}}<3
\]
for all sufficiently large \(j\), while
\[
 \frac{x_j+x_{j+1}/2}{c_j}\longrightarrow0.                    \tag{7}
\]
The first inequality fits the \(q^2\) type-\(Y_1\) vertices inside the
\(Y_j\) prime interval and the identity \(3c_j=y_{j+1}\) fits the
\(3q^2\) type-\(Y_2\) vertices inside the \(Y_{j+1}\) interval.  The second
inequality permits disjoint direction sets \(A,B\), because the required
numbers of directions are asymptotic to
\[
 \frac{x_jU(n)}q+\frac{x_{j+1}U(n)}{2q}.
\]

Choose \(\rho>0\) and \(J_0\) so that
\(C_j\ge(1+\rho)D_j\) and all the resource inequalities above hold for
\(j\ge J_0\).  Choose
\[
 0<a<b<1\quad\hbox{so small that}\quad 2^{-b}(1+\rho)>1.        \tag{8}
\]
Set
\[
 \theta_j=\frac12\log_2c_j.
\]
Equation (5) gives
\[
 \theta_j=j(-\log_2\delta)+C+o(1).                             \tag{9}
\]
The number \(-\log_2\delta\) is irrational.  Otherwise
\(\delta^v=2^{-u}\) for some positive integers \(u,v\); taking norms from
\(\mathbb Q(\sqrt5)\) to \(\mathbb Q\) would give
\((-1)^v=2^{-2u}\), a contradiction.  Hence every tail of
\((\theta_j\bmod1)\) is dense.  The open sets
\[
 E_j=\{\tau\in\mathbb R/\mathbb Z:
       \{\tau+\theta_j\}\in(a,b)\},\qquad j\ge J_0,
\]
cover the circle.  Compactness supplies a fixed finite subcover indexed by
a finite set \(I\subseteq\{J_0,J_0+1,\ldots\}\).

For a given large \(n\), put \(\tau=\tfrac12\log_2U(n)\), choose
\(j\in I\) with \(\tau\in E_j\), and take
\[
 q=2^{\lfloor\theta_j+\tau\rfloor},\qquad
 \lambda=\frac{q^2}{c_jU(n)}.
\]
Then
\[
 2^{-2b}<\lambda<2^{-2a}<1.                                   \tag{10}
\]
The constant slack in (7), (10), together with the prime number theorem on
the fixed finite family of intervals, embeds Theorem 2 with source classes
of sizes
\[
 (x_j+o(1))U(n),\qquad (x_{j+1}+o(1))U(n)
\]
and right classes of sizes \(q^2,3q^2\).  Floors and endpoint deletions cost
only \(O(U(n))=o(U(n)^{3/2})\).  Its coefficient is
\(\sqrt\lambda C_j\), and (6), (8), (10) give the uniform gain
\[
 \sqrt\lambda C_j-D_j
 \ge \bigl(2^{-b}(1+\rho)-1\bigr)D_j.
\]
Since \(I\) is finite, the right side has a positive minimum \(g\).

Finally fix a Bellman truncation past \(\max I+1\) whose omitted tail is
less than \(g/2\).  For each \(n\), replace the two separate components
\(j,j+1\) selected above by their mixed component and retain every other
component in the truncation.  All components use disjoint prime vertices;
the only products in the mixed component lie in
\[
 X_jY_j,\qquad X_{j+1}Y_j,\qquad X_{j+1}Y_{j+1},
\]
so they are at most \(n\).  The clean replacement argument therefore
applies to their union.  Taking the prime-number-theorem errors smaller than
the remaining fixed gain proves the following.

### Theorem 3 (strict uniform improvement)

There is an absolute constant \(\eta>0\) such that
\[
 \liminf_{n\to\infty}
 \frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}
 \ge \frac{2^{11/4}}{3^{3/4}}+\eta.
\]

The order of choices is essential: first choose the finite phase cover
\(I\), then the Bellman truncation, and only then let \(n\to\infty\).  Thus
all prime-number-theorem estimates concern a fixed finite set of intervals.

## Closed dependency graph

1. **Binary difference maps:** proved in Lemma 1 by direct kernel
   calculation.
2. **Typed affine \(C_4\)-free graph:** proved in Theorem 2 from the three
   difference-map conditions, including the exact \(Y_1/Y_2\) degree split.
3. **Prime replacement collision lemma:** proved in `PROOF.md`, Lemma 1.
4. **Bellman interval architecture and baseline sum:** proved in `PROOF.md`,
   Sections 2--4.
5. **First-pair resource inequalities and coefficient:** proved above by
   exact radical arithmetic; the only analytic input is PNT on fixed
   intervals.
6. **Power-of-two phase coverage:** irrationality is proved by the quadratic
   norm argument; density of an irrational rotation and compactness are the
   elementary standard inputs.
7. **Uniform PNT and truncation order:** closed by fixing the finite phase
   cover and Bellman truncation before taking \(n\to\infty\).

There is no open dependency in the two lower-bound theorems.  The open
problem is optimization: neither this construction nor current upper bounds
identify the global leading constant.
