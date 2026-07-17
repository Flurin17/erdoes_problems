# Four-defect construction

## Result

For (m=lceil n/5ceil), the complete Farey interval
\[
I_n=\left[\frac{m-1}{m},\frac{3m-2}{3m-1}\right]
\]
is admissible. For (n\ge16) its cardinality is
\[
C(n)=n+2\left\lfloor\frac{n+1}{2}\right\rfloor
-\left\lfloor\frac n3\right\rfloor-3\left\lceil\frac n5\right\rceil,
\]
so its span is (C(n)-1=(16/15)n+O(1)).

## Defect layers

Write a fraction as
\[
\frac ab=1-\frac db,\qquad d=b-a.
\]
Membership in (I_n) is exactly
\[
md\le b\le\min((3m-1)d,n),\qquad (b,d)=1.
\]
Because (n\le5m), a primitive point can occur only for (d=1,2,3,4): a putative (d=5) forces (n=5m,b=5m), which is not primitive.

For defects (d>e) and denominators (b>c), the corresponding coordinates are incomparable exactly when
\[
0<b-c<d-e. \tag{1}
\]
Differences (d-e=1) are therefore harmless. The remaining pairs are:

- ((d,e)=(3,1)): the denominator bands have (b\ge3m,c\le3m-1). The only possible gap in (1) is one, forcing (b=3m), but ((3,3m)>1).
- ((4,1)): (b-c\ge4m-(3m-1)=m+1\ge3=d-e).
- ((4,2)): primitive denominators on both even-defect layers are odd, so their positive difference cannot be one.

Thus every pair in (I_n) is compatible.

## Exact count

The four rows contribute
\[
\begin{aligned}
d=1 &: 2m,\\
d=2 &: \#\{2m\le b\le n:b\text{ odd}\},\\
d=3 &: \#\{3m\le b\le n:3\nmid b\},\\
d=4 &: \#\{4m\le b\le n:b\text{ odd}\}.
\end{aligned}
\]
Elementary floor simplification gives the displayed (C(n)) for (n\ge16). In particular the four asymptotic contributions are
\[
\frac25n,quad\frac3{10}n,quad\frac4{15}n,quad\frac1{10}n,
\]
whose sum is (16n/15).

## Internal optimality and limitation

Within the two-parameter family \([1-1/H,1-1/D]), taking (D\ge3H) creates a defect-(1)/defect-(3) gap-one inversion, while (H<n/5) activates a defect-(5) inversion. Thus (H=\lceil n/5\rceil,D=3H-1) is the extremal member of this family. This is a rigorous lower bound, not by itself a global upper bound.
