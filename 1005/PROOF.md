# Proof draft: Erdős #1005

## Status of this document

This document contains the complete solution. Fresh adversarial audits separately certified its cusp-envelope, primitive-density, bounded-cusp, and convention/endpoint steps after the repairs recorded in `STATUS.md`.

## Normalized theorem and elementary upper bound

Let \(E_n\) be the maximum index span of an all-pairs-compatible consecutive block in the inclusive Farey sequence \(F_n\). By Lemma 2.1 of `NOTES.md`, the coordinate vectors \((a,b)\) in such a block form a chain in product order.

Sort a block of cardinality \(M\) in that product order. Between successive distinct integer points, \(a+b\) rises by at least one. Since an admissible block for \(n\ge4\) cannot contain both \(0/1\) and \(1/1\), its ranks lie in an interval of length at most \(2n-2\). Therefore
\[
E_n=M-1\le2n-2. \tag{1}
\]

## Four-defect construction

Put \(m=\lceil n/5\rceil\) and take the complete Farey interval
\[
I_n=\left[\frac{m-1}{m},\frac{3m-2}{3m-1}\right]. \tag{2}
\]
Write each member as
\[
\frac ab=1-\frac db,qquad d=b-a.
\]
Membership in (2) is equivalent to
\[
md\le b\le\min((3m-1)d,n),qquad (b,d)=1. \tag{3}
\]
Because \(n\le5m\), only \(d=1,2,3,4\) occur: \(d\ge6\) contradicts \(md\le n\), and \(d=5\) can occur only at \(b=n=5m\), which is not primitive.

For rows \(d>e\), and denominators \(b>c\), the original coordinates \((b-d,b)\), \((c-e,c)\) are incomparable exactly when
\[
0<b-c<d-e. \tag{4}
\]
Rows whose defects differ by one are automatically safe. It remains to inspect \((d,e)=(3,1),(4,1),(4,2)\):

- For \((3,1)\), (3) gives \(b\ge3m,c\le3m-1\). The only possible bad gap is \(b-c=1\), forcing \(b=3m\), but then \((b,3)>1\).
- For \((4,1)\), \(b-c\ge4m-(3m-1)=m+1\ge3=d-e\).
- For \((4,2)\), both primitive denominators are odd, so their positive difference cannot be one.

Thus \(I_n\) is admissible.

For \(n\ge16\), its four row counts simplify exactly to
\[
C(n)=n+2\left\lfloor\frac{n+1}{2}\right\rfloor
-\left\lfloor\frac n3\right\rfloor-3\left\lceil\frac n5\right\rceil. \tag{5}
\]
Indeed the rows contribute, in order,
\[
2m,\quad \#\{2m\le b\le n:b\text{ odd}\},\quad
\#\{3m\le b\le n:3\nmid b\},\quad
\#\{4m\le b\le n:b\text{ odd}\}.
\]
The leading terms are \(2n/5,3n/10,4n/15,n/10\). Consequently
\[
E_n\ge C(n)-1=\frac{16}{15}n+O(1). \tag{6}
\]

The elementary bounds established so far are
\[
\boxed{\frac{16}{15}n+O(1)\le E_n\le2n-2}. \tag{7}
\]

The same asymptotic bounds hold for cardinality and for endpoint-deleted conventions, since those differ by at most one.

## Matching global upper bound

We prove that every compatible block \(B_n\) has
\[
|B_n|\le\left(\frac{16}{15}+o(1)\right)n. \tag{10}
\]
Choose a fraction \(P=p/q\in B_n\) of minimum denominator. If \(q=1\), handle the endpoint directly as follows. For \(P=0/1\), put \(A_n=nu\). The numerator-\(k\) row has limiting contribution \((\varphi(k)/k)(1-k/A)n\). If \(A>2\), the pairs \(1/b,2/(b-1)\), for suitable even \(b\), are reduced, lie in the block, and are incompatible. Hence \(A\le2\) and the coefficient is at most \(F(2)=1/2\). For \(P=1/1\), use defect rows \(k=b-a\). If \(A=n(1-\ell)>3\), suitable \(b\not\equiv0\pmod3\) make \((b-3)/b,(b-2)/(b-1)\) a bad pair. Hence \(A\le3\) and the coefficient is at most \(F(3)=5/6\). Here \(F\) is the function in (21); if either scale diverged, the same residue-row harmonic sum used in Case 3 would contradict the rank bound.

Assume henceforth \(q\ge2\). Then \(P\) is unique: the two neighbors of \(P\) in \(F_{q-1}\) separate it from every other denominator-\(q\) fraction, and neither neighbor can lie in the block. Thus the block lies between the two Stern--Brocot parents of \(P\), and we split it at \(P\).

If \(A=r/s\) is one parent, with \(|ps-qr|=1\), every point there is uniquely
\[
X_{t,k}=tP+kA,\qquad t\ge1,\quad k\ge0,\quad (t,k)=1. \tag{11}
\]
The denominator cap and angular endpoint give
\[
0\le k\le K_t:=\min\left(\lfloor\lambda t\rfloor,
\left\lfloor\frac{n-qt}{s}\right\rfloor\right). \tag{12}
\]
We distinguish the three possible scales of \(q\).

### Case 1: \(q/n\to\alpha>0\)

Only boundedly many rows \(t\) occur. If a parent denominator \(s\to\infty\), (12) gives only \(o(n)\) points on that side. Since the two parent denominators sum to \(q\), at most one side contributes linearly; on that side \((r,s)\) is fixed after taking a subsequence.

Put
\[
\beta=\frac{s\lambda}{n},\qquad
g_t=\min(\beta t,1-\alpha t)_+.
\]
Periodic coprime counting gives
\[
C:=\lim\frac{|B_n|}{n}
=\frac1s\sum_{t\le J}\frac{\varphi(t)}t g_t,qquad
\alpha\in[1/(J+1),1/J). \tag{13}
\]

**Lemma 6.1 (finite cusp envelope).** Subject to compatibility, \(C\le16/15\). Equality is possible only for
\[
(r,s,J,\alpha,\beta)=(1,1,4,1/5,2/5). \tag{14}
\]

**Proof.** Put \(m=r+s\). The translation \((a,b)\mapsto(a+1,b-1)\) gives an inversion between rows \(t\) and \(t+m\), with \(k\)-shift \(p+q=(qm+O(1))/s\). Fixed-row CRT supplies primitive representatives whenever
\[
g_t>\alpha m,qquad t+m\le J, \tag{15}
\]
except when both \(m,t\) are even. In that sole parity exception, translation by \((1,-2)\) uses row gap \(m_1=2r+s\) and gives \(g_t\le\alpha m_1\) when \(t+m_1\le J\). The exception is exact: two forbidden residue classes exhaust a prime field only at prime two, with two even row moduli and an odd shift.

Set
\[
y=1/\alpha\in(J,J+1],\qquad x=\beta/\alpha,qquad
h_t=\min(xt,y-t).
\]
Then \(C=(sy)^{-1}\sum(\varphi(t)/t)h_t\), and a constraint \(g_t\le\alpha M\), \(t+M\le J\), gives \(x\le M/t\).

If \(s\ge2\) and \(J\le m\), dropping weights gives \(C\le J/(2s)<1\). If \(J>m\), put \(k=J-m\). When \(m\) or \(k\) is odd, row \(k\) gives \(x\le m/k\), and tent summation gives \(\sum h_t=m(y-J/2)<sy\). When both are even, row \(k-1\) gives \(x\le m/(k-1)\), and the retained last tent gives \(\sum h_t\le(m/2+1)y\le sy\), since \(r,s\) are then odd and \(r\le s-2\). The case \(s=1,r=0\) is also at most one.

For \(r=s=1\), use \(\varphi(t)/t\le1\) on odd \(t\) and at most \(1/2\) on even \(t\). Odd \(J\) gives \(C\le1\), while \(J=2\) gives directly \(C\le5/6\). If \(J=2h\ge6\), row \(J-3\) and exact tent summation give
\[
C\le\frac{6h^2-11}{2(2h-3)(2h+1)}\le\frac{16}{15}.
\]
For \(J=4\), row one gives \(x\le2\), and
\[
C\le\frac{2+(y-2)/2+2(y-3)/3+(y-4)/2}{y}
=\frac53-\frac3y\le\frac{16}{15}.
\]
Equality forces \(y=5,x=2\), exactly (14). The remaining endpoint \(\alpha=1\) has no positive-length row and coefficient zero. \(\square\)

This proves (10) in Case 1.

### Case 2: \(q\to\infty\) and \(q=o(n)\)

Put \(T=n/q\to\infty\), \(x=p/q\), and
\[
L=n(x-\ell),\qquad R=n(u-x),\qquad W=L+R,
\]
where \([\ell,u]\) is the block interval. In coordinates
\[
y=b/n,qquad z=(pb-qa)/q,
\]
the block wedge has cross-section
\[
-Ry\le z\le Ly,qquad0<y\le1, \tag{16}
\]
and lattice covolume \(1/n\).

We use the elementary primitive-density lemma
\[
\#\{1\le i\le U,1\le j\le V:(i,j)=1\}
=\frac6{\pi^2}UV+o(UV) \tag{17}
\]
when \(U,V\to\infty\). Möbius inversion proves (17), with error
\(O((U+V)\log\min(U,V)+UV/\min(U,V))\). Coarse rectangular approximation gives the same density in fixed-shape convex polygons and after affine unimodular integer maps.

Let \(\tau(a,b)=(a+1,b-1)\). It sends
\[
(y,z)\mapsto(y-1/n,z-\kappa),qquad
\kappa=(p+q)/q\le2. \tag{18}
\]
If \(W\ge\kappa+\varepsilon\), truncate (16) to bounded widths summing to \(\kappa+\varepsilon/2\). The truncated wedge and its \(\tau\)-preimage have a convex overlap of fixed positive normalized area. Split it into \(z\ge\kappa\), \(0\le z\le\kappa\), and \(z\le0\); one piece has positive area.

Choose the left-parent convention \(ps-qr=1\). In the left and right Stern--Brocot coordinates, these pieces are boxes of scales \(T\) and \(q\). If \(K=p+q,H=r+s,H'=K-H\), the three forms of \(\tau\) are
\[
(t,k)\mapsto(t+H,k-K),\quad
(t,k)\mapsto(t+k-H',K-k),\quad
(v,l)\mapsto(v-H',l+K), \tag{19}
\]
with determinant \(\pm1\) linear parts. After shrinking away from the two splitting lines, every positive-area piece and its image have area \(\Theta(Tq)=\Theta(n)\), coordinate extents \(\Theta(T),\Theta(q)\), and boundary \(O(T+q)=o(n)\). To make (17) uniform, fix a normalized mesh size \(\eta>0\) and approximate each convex region by finitely many rectangles of dimensions \(\eta T\) by \(\eta q\). Each translated rectangle is an inclusion--exclusion of four anchored rectangles with endpoints \(O(T),O(q)\), so (17) applies with error \(o(n)\). First let \(n\to\infty\), then \(\eta\to0\). It follows that \(\delta+o(1)\), \(\delta=6/\pi^2>1/2\), of the overlap points are primitive before \(\tau\), and the same proportion afterward. Inclusion--exclusion gives a point primitive both ways. It and its translate lie in the block but have numerator increased and denominator decreased, a contradiction. Hence
\[
W\le\kappa+o(1). \tag{20}
\]

Applying (17) separately to the two side triangles in (16), whose total area is \(W/2\), gives the following. A side of positive limiting width has density \(\delta\); a vanishing-width side contains \(O(nW_{\rm side}+T+qW_{\rm side})=o(n)\) points. Therefore
\[
|B_n|=\frac6{\pi^2}\frac{Wn}{2}+o(n)
\le\left(\frac6{\pi^2}+o(1)\right)n,
\]
stronger than (10).

### Case 3: \(q\) is bounded

After a subsequence, \(P=p/q\) is fixed. Put
\[
A_n=qn(x-\ell),\qquad B_n=qn(u-x).
\]
Both are bounded. If, for example, \(A_n\to\infty\), then for every \(k\le\min(A_n/4,\sqrt n)\), the residue subfamily \(t\equiv1\pmod k\) supplies \(\gg n/(qk)\) primitive points in layer \(k\). Summing over \(k\) contradicts \(|B_n|\le2n+O(1)\).

Pass to \(A_n\to A,B_n\to B\). Fixed-layer counting on both sides gives
\[
\frac{|B_n|}{n}\longrightarrow\frac{F(A)+F(B)}q,qquad
F(X)=\sum_{1\le k<X}\frac{\varphi(k)}k\left(1-\frac kX\right). \tag{21}
\]
Let \(K=p+q\). In signed transverse rows, \(\tau\) shifts row \(k\) to \(k-K\). Every integer strictly inside \((K-B,A)\), other than zero and \(K\), gives a forbidden macroscopic overlap, with the sole CRT exception that \(K,k\) are even and the longitudinal shift is odd.

If \(K\) is odd and \(A,B\le K\), absence of such an integer gives \(A+B\le K+1\). If \(A>K\), the forbidden rows adjacent to \(K\) force \(A\le K+1,B\le1\); then \(F(B)=0\) and \(F(A)\le(K+1)/2\le q\). The case \(B>K\) is symmetric. Thus (21) is at most one.

If \(K\) is even, then \(p,q\) are odd and every odd signed row is forbidden. Hence \(A+B\le K+2\le2q\). From \(\varphi(k)/k\le1\) for odd \(k\) and at most \(1/2\) for even \(k\), direct summation gives \(F(X)\le3X/8\), so (21) is at most \(3/4\). At \(P=1/1\) and \(P=0/1\), the one-sided versions give \(F(3)=5/6\) and \(F(2)=1/2\), respectively.

The three cases exhaust every subsequence, proving (10). Together with (6),
\[
\boxed{E_n=\left(\frac{16}{15}+o(1)\right)n}. \tag{22}
\]
Block cardinality is \(E_n+1\), so it has the same asymptotic.

## Literal universal reading

Let
\[
\delta_n=\min\{j-i:i<j,\ a_i<a_j,\ b_i>b_j\}.
\]
Then the literal universal-in-starting-index value is exactly
\[
U_n=\delta_n-1. \tag{8}
\]
Terms at index distance one or two are always compatible by Lemma 4.1 of `NOTES.md`, so \(U_n\ge2\). Explicit bad pairs give
\[
U_n\le \frac n2\quad(n\text{ even}),
\qquad
U_n\le\frac{n+3}{2}\quad(n\ge7\text{ odd}), \tag{9}
\]
as detailed in `NOTES.md`. This reading is a different extremum from \(E_n\).

## Dependencies

The proof uses only elementary Farey/Stern--Brocot identities, Möbius inversion for the primitive-lattice density (17), finite CRT, and the explicit tent-sum inequalities in Lemma 6.1. No numerical computation is used as a proof step.
