# Bounded-defect variational route

## Exact layer model

For a block with fraction interval ([x_n,y_n]), set
\[
u_n=n(1-y_n),\qquad v_n=n(1-x_n),\qquad d=b-a.
\]
The defect-(d) row consists exactly of
\[
\frac{dn}{v_n}\le b\le\min\left(n,\frac{dn}{u_n}\right),
\qquad (b,d)=1. \tag{1}
\]
If (u_n\to u>0,v_n\to v<\infty), periodic coprime counting gives
\[
\frac{|B_n|}{n}\to
S(u,v)=\sum_{1\le d<v}\frac{\varphi(d)}d
\left(\min\left(1,\frac d u\right)-\frac d v\right). \tag{2}
\]

## Conflict graph

Rows (d>e) contain an incompatible pair at denominator offset (h) exactly when
\[
1\le h<d-e,qquad (c+h,d)=(c,e)=1. \tag{3}
\]
The CRT shows that some offset is arithmetically possible unless (d-e=1), or (d-e=2) with (d,e) both even. Indeed offset one works except for the even-even obstruction; for a larger gap, offset two removes that obstruction. For fixed rows, positive macroscopic overlap of their supports in (1) therefore produces a bad pair for all large (n).

Let (M=\lceil v\rceil-1) and let (L) be the largest odd integer at most (M). The unsafe pair (L,L-2) forces
\[
\frac vu\le\frac L{L-2}. \tag{4}
\]

## Finite variational conclusion

Optimizing (2) subject to all unsafe-row separation constraints gives
\[
S(u,v)\le\frac{16}{15}. \tag{5}
\]
Equality occurs only in the closure at
\[
(u,v)=\left(\frac53,5\right),
\]
with active rows (1,2,3,4). On the cells (M=1,2,3,4,5,6), the exact maxima are respectively
\[
\frac12,\quad\frac56,\quad\frac{11}{12},\quad
\frac{16}{15},\quad\frac{67}{90},\quad\frac{89}{105}.
\]
For odd (M\ge7), pairing even and odd rows with
\(arphi(r)\le r\) and \(arphi(2s)\le s\) gives a bound at most (1). The analogous even-(M) estimate is below (16/15) after finitely many small cells; those finite rational checks are to be certified by `computational/verify_variational.py` before (5) is promoted into the final proof.

## Exact scope

This route proves the sharp upper bound for every subsequence with (u_n,v_n) tending to finite positive limits. It does **not** yet handle (v_n\to\infty); using fixed-row CRT witnesses there is nonuniform because their periods grow with the row indices.
