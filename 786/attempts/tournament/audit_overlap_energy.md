# Adversarial audit of the finite overlap--energy bound

## Verdict

The argument in `attempts/finite_overlap_energy.md` correctly proves, under
the repetition-allowed convention, that there is an absolute \(c>0\) such
that

\[
N-|A|\ge c\frac{N}{\log N}
\]

for every PLR \(A\subset[1,N]\) and all sufficiently large \(N\). I found no
mathematical gap in the six requested points. There is one minor wording gap
at lines 80--81: the existence of an arbitrary good prime in \(P_0\) would
not by itself identify the particular value \(a_0\) selected by the
rectangle lemma. The same lemma immediately repairs this: since
\(K_0=\{1\}\) and \(B_0/R_0<1\), (4) has zero exceptional columns, so
\(f(1)=1-a_0\), whence \(a_0=1\). Equivalently, the low-error row used to
define \(a_0\) has zero bad entries. This is expository, not a failure of the
proof.

The conclusion does not cover the internally repetition-free reading of the
source problem, because the exact grading theorem is not necessary in that
setting.

## 1. Enlargement to the full fiber

At lines 14--20, the grading theorem gives a rational completely additive
\(f\) with \(f(a)=1\) for every \(a\in A\). Hence

\[
A\subseteq B:=\{n\le N:f(n)=1\},\qquad
N-|A|\ge N-|B|=m.
\]

Thus a lower bound for the complement of \(B\) transfers in the correct
direction to \(A\). In fact \(B\) is itself repetition-allowed PLR: applying
\(f\) to an equality of a product of \(r\) elements of \(B\) with a product
of \(s\) elements of \(B\) gives \(r=s\). Also \(1\notin B\), since complete
additivity gives \(f(1)=0\ne1\). No maximality or surjectivity assumption is
being smuggled into the enlargement.

## 2. Global injectivity across all bands

Lines 24--45 are valid, with two details worth making explicit. The
half-open prime intervals are pairwise disjoint, because

\[
P_j=(N/(2C_j),N/C_j],\qquad
P_{j+1}=(N/(4C_j),N/(2C_j)].
\]

Moreover \(C_j\le C_J\le\sqrt N/4\), so every participating prime satisfies

\[
p>\frac{N}{2C_j}\ge\frac{N}{2C_J}\ge2\sqrt N>C_J.
\]

Suppose \(pk=q\ell\) for two entries from any two rectangles. If \(p=q\),
disjointness of the bands gives the same band and then \(k=\ell\). If
\(p\ne q\), primality gives \(p\mid\ell\), whereas
\(1\le\ell\le C_J<p\), a contradiction. Each entry also lies below \(N\)
because \(p\le N/C_j\) and \(k\le C_j\). Therefore each bad matrix entry is
charged to a distinct integer of \(E\), and (2),
\(\sum_jB_j\le m\), is sound.

## 3. Uniform dyadic PNT lower bound

For lines 46--50, set \(x_j=N/C_j\). Then

\[
4\sqrt N\le x_j\le N,
\qquad R_j=\pi(x_j)-\pi(x_j/2).
\]

The standard prime number theorem implies, for all sufficiently large real
\(x\), a fixed lower bound

\[
\pi(x)-\pi(x/2)\ge c'\frac{x}{\log x}
\]

with an absolute \(c'>0\). Since the smallest \(x_j\) tends to infinity,
this applies simultaneously to every band; no estimate depending on \(j\)
is needed. Multiplication by \(C_j\) gives

\[
R_jC_j\ge c'\frac{N}{\log x_j}
          \ge c'\frac{N}{\log N}.
\]

Thus (3) holds uniformly with \(c_0=c'\). In particular every \(R_j>0\)
once \(N\) is sufficiently large, so all divisions by \(R_j\) are valid.

## 4. Rectangle propagation and the \(K_0\) anchor

The rectangle fact at lines 52--59 is exact: a row with at most \(B/R\)
bad entries prescribes \(f(k)=1-a\) on all of its good columns. From (2),
(3), and the contradictory hypothesis (5), one has for every \(j\)

\[
\frac{B_j}{R_jC_j}\le\frac{m}{R_jC_j}
\le\frac{\varepsilon}{c_0}=\eta,
\]

which is (6). (The source's phrase “Equations (3)--(5)” should be read as
also using the essential estimate (2).)

For adjacent bands, the exceptional sets for the prescribed cofactor
values \(1-a_j\) and \(1-a_{j+1}\), restricted to the common interval
\(K_j\), have total size at most

\[
\eta C_j+\eta C_{j+1}=3\eta C_j<C_j.
\]

Consequently there is a common nonexceptional \(k\), so
\(1-a_j=f(k)=1-a_{j+1}\). This justifies propagation through every band.
At \(j=0\), (4) and \(B_0/R_0\le\eta<1\) imply directly that the sole
column \(1\) is nonexceptional; hence \(a_0=1\). It follows that \(a_J=1\)
and (4) at the last rectangle gives

\[
|\{k\le C_J:f(k)=0\}|\ge(1-\eta)C_J.
\]

No row-majority estimate, nor any equality of the actual chosen rows across
bands, is required.

## 5. Multiplicative-energy parametrization

Lines 99--113 count ordered solutions correctly. Given \(ab=cd\), let
\(g=(a,c)\), \(a=gr\), and \(c=gs\), so \((r,s)=1\). Then
\(rb=sd\), and coprimality uniquely forces

\[
b=sh,\qquad d=rh.
\]

Writing \(q=\max(r,s)\), both \(g\) and \(h\) have at most
\(\lfloor M/q\rfloor\) choices. There are at most \(2q\) ordered coprime
pairs \((r,s)\) with maximum \(q\) (indeed \(2\varphi(q)\) for \(q>1\)).
Therefore the full multiplication-table energy is at most

\[
\sum_{q\le M}2q\left\lfloor\frac Mq\right\rfloor^2
\le2M^2(1+\log M).
\]

If \(r_Z(n)=|\{(a,b)\in Z^2:ab=n\}|\), then
\(\sum_n r_Z(n)=|Z|^2\) and
\(\sum_n r_Z(n)^2\) is bounded by that full energy. Cauchy--Schwarz hence
gives exactly

\[
|Z\cdot Z|\ge
\frac{|Z|^4}{2M^2(1+\log M)}.
\]

Also \(M=C_J\le\sqrt N/4\), so every element of \(Z\cdot Z\) is at most
\(N\); complete additivity gives it value \(0\), so it belongs to \(E\).
Thus the comparison \(m\ge|Z\cdot Z|\) has neither a multiplicity nor a
range error.

## 6. Constants and absence of circularity

The choices can be ordered explicitly. First fix, for example,
\(\eta_0=1/4\). Next take the absolute \(c_0>0\) and threshold supplied by
the dyadic PNT bound. Since \(C_J\) is the largest power of two at most
\(\sqrt N/4\), for large \(N\)

\[
\frac{\sqrt N}{8}<M=C_J\le\frac{\sqrt N}{4}.
\]

Using \(\eta\le\eta_0\) and \(1+\log M\le\log N\) for sufficiently large
\(N\), the energy estimate permits the explicit absolute choice

\[
c_1=\frac{(1-\eta_0)^4}{128},
\qquad m\ge c_1\frac{N}{\log N}.
\]

Finally choose

\[
0<\varepsilon<\min(c_0\eta_0,c_1).
\]

The first inequality makes the rectangle propagation applicable, and the
second contradicts (5) after the energy bound is obtained. Here \(c_1\)
depends only on the already fixed \(\eta_0\), not on \(\varepsilon\), \(f\),
\(A\), or \(N\). Hence there is no circular dependence; taking
\(c=\varepsilon\) proves the claimed theorem after enlarging the fixed
threshold for \(N\) as above.

## Certification

Subject only to the standard dyadic-interval consequence of the prime
number theorem, the \(N/\log N\) deletion lower bound is dependency-complete
for repetition-allowed PLR sets. The minor \(K_0\) wording repair above
should be incorporated if this proof is promoted into `PROOF.md`.
