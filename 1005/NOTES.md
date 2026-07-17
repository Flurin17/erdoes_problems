# Notes: Erdős #1005

## 1. Normalized definitions

Let
\[
F_n=(x_i=a_i/b_i)_{i=0}^{N},\qquad N=\sum_{q=1}^n\varphi(q),
\]
be the reduced fractions in \([0,1]\), including \(0/1\) and \(1/1\), in strictly increasing order. Define
\[
C(i,j)\iff (a_i-a_j)(b_i-b_j)\ge0.
\]

The intended longest-block span is
\[
E_n=\max\{r:\exists s,\ 0\le s\le s+r\le N,\ C(i,j)
\text{ for all }s\le i<j\le s+r\}.
\]
Its block cardinality is \(E_n+1\). The source's upper index \(k+f(n)\) therefore naturally makes \(f(n)\) a span; if “length” means cardinality, add one.

The literal universal closure is
\[
U_n=\max\{r: C(i,j)\text{ whenever }0\le i<j\le N\text{ and }j-i\le r\}.
\]
Equivalently every fitted window of span \(r\) is admissible. If
\[
\delta_n=\min\{j-i:\neg C(i,j)\},
\]
then \(U_n=\delta_n-1\), with the natural convention \(U_n=N\) if no bad pair exists.

Merely adding an existential quantifier to the source's displayed \(k\) but comparing only the anchor \(k\) to later \(l\) is a third, weaker reading. With \(0/1\) included, the anchor \(0/1\) is compatible with all terms, so this gives the full span \(N=\Theta(n^2)\). It does not express “every pair in a block” and is not the intended reading.

## 2. Exact compatibility lemma

**Lemma 2.1.** If \(i<j\), then \(C(i,j)\) fails exactly when
\[
a_i<a_j\quad\text{and}\quad b_i>b_j.
\]
Consequently a block is admissible exactly when its primitive coordinate points \((a_i,b_i)\) form a chain in the coordinatewise product order.

**Proof.** If \(b_i<b_j\) but \(a_i\ge a_j\), then
\[
\frac{a_i}{b_i}>\frac{a_i}{b_j}\ge\frac{a_j}{b_j},
\]
contrary to \(x_i<x_j\). Thus the sign pattern \(a_i>a_j,b_i<b_j\) is impossible. The product is negative precisely in the remaining opposite-sign pattern \(a_i<a_j,b_i>b_j\). Equality in either coordinate makes it zero. Pairwise absence of this pattern is exactly pairwise product-order comparability. \(\square\)

This is not denominator monotonicity. In \(F_5\),
\[
2/5,\ 1/2,\ 3/5,\ 2/3
\]
is an admissible consecutive block although its numerator sequence \(2,1,3,2\) and denominator sequence \(5,2,5,3\) are both nonmonotone.

## 3. Farey neighbor identities

**Lemma 3.1.** Reduced fractions \(a/b<c/d\) are consecutive in \(F_n\) exactly when
\[
bc-ad=1,\qquad b+d>n.
\]

**Proof.** The standard mediant induction is included for dependency completeness. For any reduced or unreduced \(p/q\) strictly between a determinant-one pair, both \(pb-aq\) and \(cq-pd\) are positive integers, and
\[
q=d(pb-aq)+b(cq-pd)\ge b+d. \tag{3.1}
\]
Starting with \(F_1=(0/1,1/1)\), insert the mediant between each adjacent pair whose denominator sum is the new order. Equation (3.1) shows no smaller-denominator fraction can intervene and every new reduced fraction occurs uniquely. This proves determinant one for neighbors at every order. If \(b+d\le n\), the mediant intervenes; if \(b+d>n\), (3.1) excludes any intervening denominator at most \(n\). \(\square\)

**Lemma 3.2 (coupled recurrence).** For three consecutive terms,
\[
(a_{i+1},b_{i+1})=k_i(a_i,b_i)-(a_{i-1},b_{i-1}),
\quad
k_i=\left\lfloor\frac{n+b_{i-1}}{b_i}\right\rfloor.
\]

**Proof.** Both \((a_{i+1},b_{i+1})\) and \((-a_{i-1},-b_{i-1})\) solve \(xb_i-a_i y=1\). Since \((a_i,b_i)\) is primitive, their difference is an integer multiple \(k_i(a_i,b_i)\). The inequalities \(b_{i+1}\le n<b_i+b_{i+1}\) uniquely give the displayed floor. \(\square\)

Under \((x,y)=(b_{i-1}/n,b_i/n)\), the denominator dynamics lie in the Farey triangle \(0<x,y\le1,x+y>1\) and are
\[
T(x,y)=\left(y,\left\lfloor\frac{1+x}{y}\right\rfloor y-x\right).
\]
The numerator recurrence must also be tracked: denominator dynamics alone do not decide compatibility.

## 4. Local compatibility and endpoints

**Lemma 4.1.** Farey terms at index distance one or two are always compatible. Hence \(U_n\ge2\) for \(n\ge2\).

**Proof.** For adjacent \(a/b<c/d\), a bad pattern would have \(c>a,d<b\), giving
\[
1=bc-ad=b(c-a)+a(b-d)\ge b\ge2,
\]
a contradiction. For three consecutive terms write \((e,f)=t(c,d)-(a,b)\). If the endpoints were bad, then \(e>a,f<b\), and
\[
t=be-af=b(e-a)+a(b-f)\ge a+b.
\]
But \(td=b+f<2b\). The middle denominator is \(d\ge2\), so \(t<b\), contradicting \(t\ge a+b\). Endpoint cases are immediate. \(\square\)

**Lemma 4.2.** Both \(0/1\) and \(1/1\) are compatible with every Farey fraction.

**Proof.** For \(a/b\in[0,1]\),
\[
(0-a)(1-b)=a(b-1)\ge0,
\qquad
(a-1)(b-1)\ge0.
\]
\(\square\)

For every \(n\ge4\) an interior bad pair exists: if \(n\) is even use \(1/n,2/(n-1)\); if \(n\) is odd use \(1/n,2/(n-2)\). Thus the full sequence is not admissible. An admissible interval cannot contain both endpoints, so removing one or both endpoints changes \(E_n\) by at most one. Removing endpoints does not change gaps between interior bad pairs and hence does not change \(U_n\).

For the literal reading, explicit bad pairs also give a linear upper bound. If \(n\) is even, the fractions strictly between \(1/n\) and \(2/(n-1)\) are exactly \(1/q\) with \(n/2\le q<n\), so their index gap is \(n/2+1\) and \(U_n\le n/2\). If \(n\ge7\) is odd, the fractions strictly between \(1/n\) and \(2/(n-2)\) are \(1/q\) with \((n-2)/2<q<n\), together with \(2/n\). Their index gap is \((n+5)/2\), so \(U_n\le(n+3)/2\). To justify the enumerations, a fraction \(a/b<2/D\) with \(a\ge3\) would require \(b>aD/2>n\); the \(a=2\) cases are then decided by reducedness and the denominator cap.

## 5. Exact boundary cases

Direct exhaustive comparison gives:

| \(n\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|
| intended span \(E_n\) | 1 | 2 | 4 | 4 | 6 | 6 |
| literal span \(U_n\) | 1 | 2 | 4 | 2 | 3 | 3 |

For example,
\[
F_4=(0/1,1/4,1/3,1/2,2/3,3/4,1/1).
\]
The pair \(1/4,2/3\) is bad at gap three, so \(U_4=2\). The block from \(1/3\) through \(1/1\) has span four; both possible span-five windows contain the bad pair, so \(E_4=4\).

These finite values are checks, not a proof of any asymptotic.
