# Finite overlap: robust prime--cofactor rectangles

## Proposed mechanism

Let \(f\) be a rational completely additive function and set
\[
A_t(X)=\{n\le X:f(n)=t\},\qquad E_t(X)=[1,X]\setminus A_t(X).
\]
On a prime--cofactor rectangle, membership in the fiber is the equation
\[
f(p)+f(k)=t. \tag{1}
\]
Thus all good entries in one row have the same cofactor color, and two rows
of different prime colors cannot have a common good cofactor. If the products
\(pk\) are distinct, every bad entry consumes a different member of
\(E_t(X)\). This gives an exact connectivity principle: overlapping rows
have equal prime weights unless their exceptional entries cover the whole
overlap.

The lemmas below make this robust. They give useful global structure when
\(|E_t(X)|=o(X/\log X)\), and scale-by-scale structure under the weaker
hypothesis \(o(X)\). They do not by themselves settle the finite problem:
one logarithmic-scale cut costs only \(\asymp X/\log X=o(X)\). The remaining
question is whether complete additivity prevents many such cuts from being
realized simultaneously.

## 1. Exact row overlap

### Lemma 1 (overlap must be paid for)

Let \(P\) be a finite set of primes. For each \(p\in P\), let \(K_p\) be a
finite set of positive integers such that \(pk\le X\) for \(k\in K_p\), and
put
\[
e_p=|\{k\in K_p:pk\in E_t(X)\}|.
\]
If \(p,q\in P\) and \(f(p)\ne f(q)\), then
\[
\begin{split}
|K_p\cap K_q|
&\le |\{k\in K_p\cap K_q:pk\in E_t(X)\}|\\
&\quad+|\{k\in K_p\cap K_q:qk\in E_t(X)\}|. \tag{2}
\end{split}
\]
In particular, if \(K_p=[1,d_p]\), then
\[
f(p)\ne f(q)\quad\Longrightarrow\quad
\min(d_p,d_q)\le e_p+e_q. \tag{3}
\]

#### Proof

If both \(pk\) and \(qk\) lie in \(A_t(X)\), then (1) gives
\[
f(p)+f(k)=t=f(q)+f(k),
\]
so \(f(p)=f(q)\). Therefore, when the two prime weights differ, every
cofactor in the overlap makes at least one corresponding product
exceptional. The union bound proves (2), and (3) follows. \(\square\)

The threshold in (3) is sharp using only row-error counts. If the overlap
has size \(d=e_p+e_q\), partition it into sets of sizes \(e_q,e_p\), make
only the first row good on the first set and only the second row good on the
second set, and assign the two sets different cofactor colors.

## 2. Robust rectangle and connectivity lemmas

Call \(P\times K\) an *injective prime--cofactor rectangle* if \(pk\le X\)
for every \((p,k)\in P\times K\) and all these products are distinct. A
convenient sufficient condition is
\[
\max K<\min P,\qquad (\max P)(\max K)\le X. \tag{4}
\]
Indeed, \(pk=q\ell\) with distinct \(p,q\in P\) would imply
\(p\mid\ell\), contrary to (4).

### Lemma 2 (one nearly monochromatic block)

Let \(P\times K\) be an injective rectangle, write
\[
R=|P|,\qquad C=|K|,
\]
and let
\[
B=|\{(p,k)\in P\times K:pk\in E_t(X)\}|.
\]
If \(B<RC\), there is \(a\in\mathbb Q\) such that
\[
|\{k\in K:f(k)\ne t-a\}|\le \frac BR, \tag{5}
\]
and
\[
|\{p\in P:f(p)\ne a\}|
\le \frac{B}{C-B/R}. \tag{6}
\]
Consequently, if \(B\le\eta RC\) with \(0\le\eta<1\), all but at most
\(\eta C\) columns have cofactor color \(t-a\), and all but at most
\[
\frac{\eta}{1-\eta}R \tag{7}
\]
rows have prime color \(a\).

#### Proof

For \(p\in P\), let
\[
b_p=|\{k\in K:pk\in E_t(X)\}|,
\]
so \(\sum_{p\in P}b_p=B\). Choose \(p_0\) with \(b_{p_0}\le B/R\), and put
\(a=f(p_0)\). On every good entry of this row, (1) forces
\(f(k)=t-a\), proving (5).

Let \(K_0\) be the good cofactors in the \(p_0\)-row. Then
\[
|K_0|\ge C-B/R. \tag{8}
\]
If \(f(p)\ne a\), Lemma 1 says that \(pk\) is exceptional for every
\(k\in K_0\). Each such row contributes at least \(|K_0|\) bad entries.
Summing these disjoint matrix entries and using (8) proves (6). \(\square\)

### Lemma 3 (connectivity of overlapping rectangles)

Apply Lemma 2 to injective rectangles \(P\times K\) and \(P'\times K'\),
obtaining dominant prime colors \(a,a'\). Let their bad-entry counts be
\(B,B'\), and write \(R=|P|\), \(R'=|P'|\). If
\[
|K\cap K'|>\frac BR+\frac{B'}{R'}, \tag{9}
\]
then \(a=a'\).

#### Proof

By (5), at most \(B/R\) elements of \(K\) fail to have color \(t-a\), and
at most \(B'/R'\) elements of \(K'\) fail to have color \(t-a'\). Condition
(9) leaves a cofactor in the intersection having both prescribed colors.
Thus \(t-a=t-a'\). \(\square\)

For a collection of rectangles, join two rectangle-vertices whenever (9)
holds. Lemma 3 says that the dominant prime color is constant on every
connected component. This uses actual overlap sizes, not a heuristic
independence assumption.

## 3. The large-prime Ferrers graph

For \(p>\sqrt X\), put
\[
d_p=\left\lfloor\frac Xp\right\rfloor,\qquad
e_p=|\{k\le d_p:pk\in E_t(X)\}|.
\]
The map
\[
(p,k)\longmapsto pk,\qquad
p>\sqrt X,\quad 1\le k\le d_p, \tag{10}
\]
is injective: its cofactor is \(<\sqrt X<p\), so the product cannot have a
second representation with another prime above \(\sqrt X\). Hence
\[
\sum_{\sqrt X<p\le X}e_p\le |E_t(X)|. \tag{11}
\]

### Corollary 4 (weighted Ferrers connectivity)

Make a graph on the primes \(p>\sqrt X\), joining \(p,q\) whenever
\[
e_p+e_q<\min(d_p,d_q). \tag{12}
\]
Then \(f(p)\) is constant on each connected component, and the total row
error satisfies (11).

This is stronger than saying that most individual rows are good: every
change of prime weight has to pay for a complete common initial interval of
cofactors.

## 4. Dyadic consequence and the \(X/\log X\) threshold

For integers \(j\ge0\), put
\[
C_j=2^j,\qquad
P_j=\left\{p\text{ prime}:\frac{X}{2C_j}<p\le\frac X{C_j}\right\}. \tag{13}
\]
Restrict to \(j\) for which \(C_j<\sqrt{X/2}\), and let \(C_J\) be the
largest such power of two. Every prime in every \(P_j\) then exceeds every
cofactor in \([1,C_J]\). Thus the rectangles
\[
P_j\times[1,C_j] \tag{14}
\]
are jointly injective. If \(B_j\) is the bad-entry count of the \(j\)-th
rectangle, then
\[
\sum_jB_j\le |E_t(X)|. \tag{15}
\]
The prime number theorem, used only in its standard dyadic-interval form,
gives uniformly over these bands
\[
|P_j|\asymp\frac{X}{C_j\log X},\qquad
|P_j|C_j\asymp\frac X{\log X}. \tag{16}
\]

Two consequences follow.

1. If \(|E_t(X)|=o(X/\log X)\), every rectangle in (14) has bad proportion
   \(o(1)\), uniformly in \(j\). Adjacent rectangles satisfy (9), so their
   dominant colors agree. The top rectangle has cofactor set \(\{1\}\), and
   \(f(1)=0\); hence the common dominant cofactor color is exactly zero.
   For some \(C_J\asymp\sqrt X\),
   \[
   |\{k\le C_J:f(k)\ne0\}|=o(C_J), \tag{17}
   \]
   and, in every band \(P_j\), all but \(o(|P_j|)\) primes have weight \(t\).

2. More generally, fix \(0<\eta<1/3\), and call a band bad when
   \(B_j>\eta|P_j|C_j\). If \(|E_t(X)|=o(X)\), (15)--(16) show that the
   number of bad bands is \(o(\log X)\). On every consecutive run of good
   bands, Lemmas 2 and 3 give one common dominant prime color and
   complementary, nearly constant cofactor colors. Thus an \(o(X)\)
   exceptional set permits only \(o(\log X)\) possible color-change
   locations among the \(\Theta(\log X)\) bands.

For the adjacent-band check in the second assertion, Lemma 2 leaves at most
\(\eta C_j\) exceptional cofactor colors in \([1,C_j]\), and at most
\(\eta C_{j+1}=2\eta C_j\) in \([1,C_{j+1}]\). Since
\(3\eta C_j<C_j\), their two prescribed colors meet on the common interval.

When \(t=1\), (17) says that a hypothetical fiber missing
\(o(X/\log X)\) integers has a threshold-like shape: almost every cofactor
up to the square-root scale has weight zero, while almost every prime in the
associated upper bands has weight one. This is not yet a contradiction,
because lower prime bands may control the remaining smooth integers.

## 5. Sharp density-only obstruction at one scale

The order \(X/\log X\) above cannot be improved by connectivity and
cardinality alone. Work in the full Ferrers domain (10), fix
\(L=X^\theta\) with \(0<\theta<1/2\), and delete precisely
\[
\mathcal D_L=
\{pk:\sqrt X<p\le X/L,\ 1\le k\le L\}. \tag{18}
\]
These products are distinct, and the prime number theorem gives
\[
|\mathcal D_L|
=L\bigl(\pi(X/L)-\pi(\sqrt X)\bigr)
=\left(\frac1{1-\theta}+o(1)\right)\frac X{\log X}
=o(X). \tag{19}
\]
After these entries are removed, rows of degree at most \(L\) use only
cofactors \(k\le L\), while rows of degree greater than \(L\) have no
remaining entry with \(k\le L\). The incidence graph is therefore cut
across that scale. Its two sides may be assigned different abstract row
colors while satisfying (1) on every retained edge.

Repeating this deletion at \(s=o(\log X)\) separated scales costs
\(O(sX/\log X)=o(X)\) and produces many incidence components. The cuts may
be spaced so that the prime-reciprocal mass between consecutive cuts is
\(O(1/s)\). Then the prime number theorem (or Mertens' prime-reciprocal
estimate) bounds the number of retained entries in every component by
\(O(X/s)\). Taking \(s\to\infty\) gives no component containing a positive
proportion of all entries. This is a sharp counterexample to any claim that
arbitrary \(o(X)\) deletions leave a giant connected prime--cofactor graph.
It is deliberately **not** claimed to construct a completely additive
\(f\): the abstract cofactor colors need not arise from prime weights. That
is exactly the surviving arithmetic bottleneck.

## 6. Lemma chain, unsupported step, and falsification

The proved chain is:

1. A repetition-allowed PLR set lies in an exact nonzero additive fiber.
2. Different row weights on an injective rectangle require every common
   cofactor to be paid for by an exception (Lemma 1).
3. A rectangle with bad proportion \(\eta\) has one cofactor color on at
   least \(1-\eta\) of its columns and, for \(\eta<1/2\), one prime color on
   at least \(1-\eta/(1-\eta)\) of its rows (Lemma 2).
4. Sufficiently overlapping nearly monochromatic rectangles have the same
   color (Lemma 3).
5. Above the square-root scale all entries are globally injective, so their
   entire error budget is at most \(|E_t(X)|\) (Corollary 4).
6. This forces threshold-like behavior at error \(o(X/\log X)\), and long
   monochromatic runs at error \(o(X)\).

The weakest unsupported step is precise:

> **Additive scale-change lemma needed.** Prove that a completely additive
> \(f\) cannot realize \(o(\log X)\) different dominant cofactor colors on
> the nested dyadic runs above while keeping
> \(|\{n\le X:f(n)\ne1\}|=o(X)\); equivalently, show that every genuine color
> change creates further exceptions, beyond the \(\asymp X/\log X\)
> incidence cut, through products of primes from different scale blocks.

The cut (18) shows why such a proof must use complete additivity of the
cofactor colors, not graph expansion alone.

A concrete falsification test for any proposed strengthening is the
two-row boundary case of Lemma 1: prescribe unequal prime weights and split
an overlap of size \(d\) into complementary bad sets of total size \(d\).
Any assertion forcing equality when \(e_p+e_q\ge d\) is false without new
arithmetic input. At the multi-scale level, (18) is the corresponding test:
a single \(L=X^\theta\) cut disproves any claim that arbitrary \(o(X)\)
deletions preserve global connectivity.

## 7. Next action

Keep the exact rectangles but add cross-products. On two consecutive
monochromatic runs with dominant prime weights \(a\ne b\), count integers
whose largest two prime factors come from the two runs. Complete additivity
assigns these integers the forced contribution \(a+b\), independently of
the abstract cut coloring. A lower bound showing that a positive proportion
of such cross-products miss level \(1\), after charging the known rectangle
errors only once, would close the unsupported scale-change lemma.
