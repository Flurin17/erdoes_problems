# Bounded-defect variational route

For a block with interval $[x_n,y_n]$, set
\[
u_n=n(1-y_n),\qquad v_n=n(1-x_n),\qquad d=b-a.
\]
Defect row $d$ consists exactly of
\[
\frac{dn}{v_n}\le b\le\min\left(n,\frac{dn}{u_n}\right),
\qquad (b,d)=1. \tag{1}
\]
If $u_n\to u>0$ and $v_n\to v<\infty$, periodic coprime counting gives
\[
\frac{|B_n|}{n}\to
S(u,v)=\sum_{1\le d<v}\frac{\varphi(d)}d
\left(\min\left(1,\frac d u\right)-\frac d v\right). \tag{2}
\]

Rows $d>e$ have a potential bad pair at offset $h$ exactly when
\[
1\le h<d-e,qquad (c+h,d)=(c,e)=1. \tag{3}
\]
CRT shows that an offset exists unless $d-e=1$, or $d-e=2$ with both rows even. Positive macroscopic overlap of any other fixed pair is forbidden.

The exact finite-envelope optimization in Lemma 6.1 of `PROOF.md` proves
\[
S(u,v)\le\frac{16}{15},
\]
with equality only at $(u,v)=(5/3,5)$ and active rows $1,2,3,4$. This route is now a proved component of the global upper bound; growing layers are handled separately by the minimum-denominator trichotomy.
