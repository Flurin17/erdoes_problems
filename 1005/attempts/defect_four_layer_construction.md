# Four-defect construction

## Result

For $m=\lceil n/5\rceil$, the complete Farey interval
\[
I_n=\left[\frac{m-1}{m},\frac{3m-2}{3m-1}\right]
\]
is admissible. For $n\ge16$ its cardinality is
\[
C(n)=n+2\left\lfloor\frac{n+1}{2}\right\rfloor
-\left\lfloor\frac n3\right\rfloor-3\left\lceil\frac n5\right\rceil,
\]
so its span is $C(n)-1=(16/15)n+O(1)$.

## Defect layers

Write $a/b=1-d/b$, where $d=b-a$. Membership in $I_n$ is exactly
\[
md\le b\le\min((3m-1)d,n),\qquad (b,d)=1.
\]
Because $n\le5m$, only $d=1,2,3,4$ occur; a putative $d=5$ forces $b=n=5m$, which is not primitive.

For $d>e$ and $b>c$, the points $(b-d,b)$ and $(c-e,c)$ are incomparable exactly when
\[
0<b-c<d-e. \tag{1}
\]
Rows differing by one are safe. The remaining pairs are:

- $(d,e)=(3,1)$: a bad gap forces $b=3m$, but $(3,3m)>1$.
- $(d,e)=(4,1)$: $b-c\ge m+1\ge3=d-e$.
- $(d,e)=(4,2)$: both primitive denominators are odd, so their positive difference is not one.

Thus $I_n$ is admissible.

## Exact count

The rows contribute
\[
\begin{aligned}
d=1 &: 2m,\\
d=2 &: \#\{2m\le b\le n:b\text{ odd}\},\\
d=3 &: \#\{3m\le b\le n:3\nmid b\},\\
d=4 &: \#\{4m\le b\le n:b\text{ odd}\}.
\end{aligned}
\]
Their leading terms are
\[
\frac25n,\quad\frac3{10}n,\quad\frac4{15}n,\quad\frac1{10}n,
\]
which sum to $16n/15$.

## Scope

This route supplies the sharp construction. Its global optimality is proved by the minimum-denominator trichotomy in `PROOF.md`.
