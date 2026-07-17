# Proof draft: Erdős #1005

## Status of this document

This is a **partial result**, not a complete solution. It proves a new explicit lower bound with candidate constant \(16/15\), and an unconditional linear upper bound with constant \(2\). The matching \(16/15\) upper bound is supported by a bounded-defect variational reduction, but its finite certificate and uniform global extension remain named dependencies in `STATUS.md`.

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

Combining (1) and (6), the currently proved global estimate is
\[
\boxed{\frac{16}{15}n+O(1)\le E_n\le2n-2}. \tag{7}
\]

The same asymptotic bounds hold for cardinality and for endpoint-deleted conventions, since those differ by at most one.

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

## Remaining dependency for the candidate answer

The computation and bounded-layer variational calculation both point to
\[
E_n=\left(\frac{16}{15}+o(1)\right)n.
\]
What is not yet proved globally is that a compatible angular interval with growing defect/transverse scale cannot exceed \(16n/15+o(n)\). `attempts/growing_layers_bottleneck.md` records the first exact nonuniform step; no claim of a complete \(16/15\) upper bound is made here.
