# A dyadic-cell replacement for the local prime convolution

## Outcome

Let
\[
 B_f(N)=\{n\le N:f(n)=1\},\qquad E_f(N)=[1,N]\setminus B_f(N),
\]
where \(f:\mathbb N\to\mathbb Q\) is completely additive. This note gives
an independent proof of the lower-prime-factor input used in
profile_lpf_charge.md. It uses only prime counts in ordinary dyadic
intervals and an elementary lattice-sum argument; in particular, it does
not use the local prime-convolution estimate (20) from that note.

Combined with the already proved largest-prime row charge, it proves
uniformly in the possibly \(N\)-dependent function \(f\) that
\[
 |E_f(N)|=\omega\!\left(\frac N{\log N}\right).         \tag{1}
\]

The central point is the following statement. Write
\[
 \mathcal Z=\{p\le M:p\text{ is prime and }f(p)=0\}
\]
and suppose \(M\ge c\sqrt N\). If
\[
 \sum_{\substack{p\le M\\p\notin\mathcal Z}}\frac1p\le K,       \tag{2}
\]
then, for a constant depending only on \(K\) and \(c\), there are
\[
 \gg_K \frac{N\log\log N}{\log N}                     \tag{3}
\]
squarefree integers \(n\le N\), all of whose prime factors belong to
\(\mathcal Z\) and are at most \(N^{1/4}\). Thus all of these integers
have \(f(n)=0\).

All constants below may depend on \(K\), but never on the particular set
\(\mathcal Z=\mathcal Z_N\). This is what permits the grading weights to
move with \(N\).

## 1. Dense dyadic-cell sums

We first isolate the elementary combinatorial input. Let \(L\to\infty\),
let \(a>0\) be fixed, and put
\[
 J_L=\{j\in\mathbb Z:aL+2\le j\le 2aL-2\}.             \tag{4}
\]
Fix \(0<\theta<1/4\), and define the central pair-sum interval
\[
 H_L=\{h\in\mathbb Z:(3-\theta)aL\le h\le(3+\theta)aL\}. \tag{5}
\]

### Lemma 1 (robust pair sums)

There is an absolute \(\eta_0>0\) with the following property. If
\(G_L\subset J_L\) and
\[
 |J_L\setminus G_L|\le\eta_0 aL,                       \tag{6}
\]
then every \(h\in H_L\) has at least \(c_\theta aL\) ordered
representations
\[
 h=j_1+j_2,\qquad j_1,j_2\in G_L,                       \tag{7}
\]
once \(L\) is sufficiently large.

#### Proof

Without the restriction to \(G_L\), the permitted values of \(j_1\) form
the intersection
\[
 J_L\cap(h-J_L).
\]
For \(h\) in (5), this intersection has at least
\((1-\theta)aL-O(1)\) integer points. A missing element of \(J_L\) can
destroy at most one representation in the first coordinate and at most
one in the second. Hence at most \(2|J_L\setminus G_L|\) representations
are lost. Taking, for example, \(\eta_0=(1-\theta)/8\) proves the claim.
\(\square\)

### Lemma 2 (iterated central sums)

Fix \(a,\theta>0\) and an integer \(k\ge2\). Suppose a compact interval
\(I\) lies in the interior of
\[
 [k(3-\theta)a,k(3+\theta)a].                          \tag{8}
\]
Uniformly for integers \(T\) with \(T/L\in I\), the number of tuples
\((h_1,\ldots,h_k)\in H_L^k\) satisfying
\[
 h_1+\cdots+h_k=T                                      \tag{9}
\]
is at least \(c_{a,\theta,k,I}L^{k-1}\).

#### Proof

After division by \(L\), (9) counts lattice points of mesh \(1/L\) in a
slice of the fixed box
\([(3-\theta)a,(3+\theta)a]^k\). On every compact subinterval of the
interior of the possible sum interval, that slice contains a
\((k-1)\)-dimensional box of side bounded below by a positive constant.
Rounding the first \(k-1\) coordinates to the lattice and using (9) to
define the last gives \(\gg L^{k-1}\) solutions. Equivalently, restrict
every variable to a sufficiently short fixed subinterval around one
interior representation of \(T/L\). \(\square\)

Combining the two lemmas, if (6) holds and \(T/L\in I\), then the number
of ordered \(2k\)-tuples
\[
 (j_1,\ldots,j_{2k})\in G_L^{2k},\qquad
 j_1+\cdots+j_{2k}=T,                                  \tag{10}
\]
is at least
\[
 c_{a,\theta,k,I}L^{2k-1}.                              \tag{11}
\]
Indeed, first choose the \(k\) pair sums by Lemma 2 and then independently
choose a representation of each pair sum by Lemma 1. This pairing device
is why no error proportional to \(k|J_L\setminus G_L|\) occurs.

## 2. Extracting good cells from a reciprocal budget

We now prove (3). Logs in the dyadic-cell argument are to base \(2\);
this only changes constants. Set \(L=\log_2N\).

Choose once and for all the \(\theta\) from Section 1 and a sufficiently
small absolute \(\varepsilon>0\). Let
\[
 H=\lfloor K/\varepsilon\rfloor+1.                     \tag{12}
\]
Choose a sufficiently large absolute \(i_0\), and for
\(i=i_0,\ldots,i_0+H-1\) put
\[
 a_i=2^{-i-1},\qquad I_i=(N^{a_i},N^{2a_i}].            \tag{13}
\]
The intervals \(I_i\) are pairwise disjoint. By (2), one of them, say
\(I=(N^a,N^{2a}]\), satisfies
\[
 \sum_{\substack{p\in I\\p\notin\mathcal Z}}\frac1p
 \le\varepsilon.                                       \tag{14}
\]
The possible values of \(a\) form a finite set depending only on \(K\).
We take \(i_0\) large enough that \(2a<1/4\) for every one of them.

Partition \(I\), apart from its two boundary cells, into ordinary dyadic
prime intervals
\[
 D_j=(2^j,2^{j+1}],\qquad j\in J_L,                    \tag{15}
\]
with \(J_L\) as in (4). The prime number theorem in dyadic intervals,
uniformly for this fixed finite menu of \(a\)'s, gives an absolute
constant \(c_0>0\) such that
\[
 \#\{p\in D_j:p\text{ prime}\}\ge c_0\frac{2^j}{j}      \tag{16}
\]
for every \(j\in J_L\) and all sufficiently large \(N\).

Call \(j\) good when
\[
 Z_j:=\#(\mathcal Z\cap D_j)\ge\frac{c_0}{2}\frac{2^j}{j}. \tag{17}
\]
If \(j\) is bad, (16) shows that \(D_j\) contains at least
\((c_0/2)2^j/j\) primes outside \(\mathcal Z\). Since every such prime is
at most \(2^{j+1}\), its contribution to (14) is at least
\[
 \frac{c_0}{4j}\ge\frac{c_0}{9aL}                     \tag{18}
\]
for all large \(L\). Consequently
\[
 \#\{j\in J_L:j\text{ is bad}\}\le\frac{9\varepsilon}{c_0}aL. \tag{19}
\]
Choose \(\varepsilon\) at the outset so that
\(9\varepsilon/c_0\le\eta_0\). Thus the set \(G_L\) of good indices
satisfies Lemma 1.

There is no circular dependence here. The required smallness of
\(\varepsilon\) is absolute. Although the number of eventual prime
factors can be very large as a function of \(K\), errors are removed once
at the two-cell level by Lemma 1 and do not accumulate with that number of
factors.

## 3. Products near \(N\) without a local prime convolution

For the selected \(a\), set
\[
 k=\left\lceil\frac1{3a}\right\rceil,\qquad r=2k.       \tag{20}
\]
By increasing the absolute \(i_0\), we may ensure
\[
 3a<\frac{\theta}{12}.                                 \tag{21}
\]
The center \(3ak\) of the interval in (8) belongs to
\([1,1+3a]\), whereas its half-width is
\(\theta ak\ge\theta/3\). It follows from (21) that there is a number
\(\delta>0\), uniform over the finite menu of possible \(a\)'s, such that
\[
 [1-2\delta,1+\delta]
 \subset \operatorname{int}[k(3-\theta)a,k(3+\theta)a]. \tag{22}
\]
Shrink \(\delta\), if necessary, so that
\[
 0<\delta<\tfrac12\min_i a_i.                          \tag{23}
\]

Fix a prime
\[
 \ell\le N^\delta,\qquad \ell\in\mathcal Z,             \tag{24}
\]
and define
\[
 T_\ell=\left\lfloor\log_2(N/\ell)\right\rfloor-r.      \tag{25}
\]
Uniformly over (24),
\(T_\ell/L\in[1-2\delta,1+\delta]\) for all large \(N\). Equations
(11) and (22) therefore give at least
\[
 c_KL^{r-1}                                             \tag{26}
\]
ordered good-index tuples with sum \(T_\ell\).

For each such index tuple choose distinct primes
\[
 q_s\in\mathcal Z\cap D_{j_s}\quad(1\le s\le r).        \tag{27}
\]
For fixed \(r\), (17) tends uniformly to infinity with \(N\). Even when
some cells repeat, choosing the primes successively therefore leaves at
least
\[
 2^{-r}\prod_{s=1}^r Z_{j_s}
 \ge c_K\frac{2^{j_1+\cdots+j_r}}{L^r}
 =c_K\frac{2^{T_\ell}}{L^r}                            \tag{28}
\]
ordered choices. Since
\[
 \frac{N}{2^{r+1}\ell}<2^{T_\ell}\le\frac{N}{2^r\ell}, \tag{29}
\]
summing (28) over the index tuples in (26), and then dividing by at most
\(r!\) orderings of the same prime set, produces at least
\[
 c_K\frac{N}{\ell\log N}                               \tag{30}
\]
distinct squarefree integers
\[
 n=\ell q_1\cdots q_r\le N.                            \tag{31}
\]
In fact (15), (25), and (29) put these integers in
\((N/2^{r+1},N]\).

By (23), \(\ell<N^a<q_s\). Hence \(\ell\) is the unique prime factor of
(31) below \(N^\delta\). The families arising from different anchor
primes \(\ell\) are therefore disjoint. Also every
\(q_s\le N^{2a}<N^{1/4}\), and the same holds for \(\ell\).

Finally, Mertens' estimate and (2) give
\[
 \sum_{\substack{\ell\le N^\delta\\\ell\in\mathcal Z}}
       \frac1\ell
 \ge \log\log N-O_K(1).                                \tag{32}
\]
Summing (30) over (24) proves (3). Every constructed integer is composed
only of zero-weight primes, so complete additivity gives \(f(n)=0\).
This completes the dyadic-cell proof of the lower-prime-factor lemma.

## 4. Consequence for the exceptional set

For completeness, combine the lemma with the exact upper-row charge from
profile_lpf_charge.md. Let \(M\asymp\sqrt N\), and split
\[
 E_f(N)=E_>\sqcup E_\le,\qquad
 E_>=\{n\in E_f(N):P^+(n)>M\}.                         \tag{33}
\]
The row argument there proves, with an absolute \(c_1>0\),
\[
 |E_>|\ge c_1\frac N{\log N}
       \sum_{\substack{C_0\le p\le M\\f(p)\ne0}}\frac1p, \tag{34}
\]
It relies only on the previously proved uniform
\(cX/\log X\) complement bound at cofactor scale and on the exact
largest-prime tagging of the rows.

Suppose, contrary to (1), that along an unbounded sequence there are
functions \(f=f_N\) and a fixed \(C\) with
\[
 |E_f(N)|\le C\frac N{\log N}.                          \tag{35}
\]
Then (34) bounds the displayed active-prime reciprocal sum by a constant;
the finitely many primes below \(C_0\) add only another absolute constant.
Thus the full active-prime reciprocal sum is at most \(K=K(C)\).
Apply (3) to the zero-weight primes. Its products have largest prime
factor below \(N^{1/4}<M\), so all lie in \(E_\le\), and hence
\[
 |E_f(N)|\ge c_K\frac{N\log\log N}{\log N},             \tag{36}
\]
contradicting (35) for large \(N\). This proves (1).

If \(A\subset[1,N]\) is repetition-allowed product-length-rigid, the
grading theorem places \(A\) in a fiber \(f=1\). Therefore
\(N-|A|\ge|E_f(N)|\), and the same omega bound follows for \(A\).

## 5. Dependency ledger and falsification checks

Proved here:

1. bounded reciprocal mass of nonzero-weight primes leaves a polynomial
   prime band with small deleted mass;
2. small deleted reciprocal mass makes all but a small fraction of the
   ordinary dyadic cells good;
3. dense cell sets have uniformly many central pair sums;
4. pairing first, and only then taking \(k\)-fold sums, gives the exact
   \(L^{r-1}\) supply of index tuples without an \(r\)-fold deletion loss;
5. dyadic prime counts turn those tuples into distinct zero-weight
   integers, with moving weights handled uniformly.

External inputs already established elsewhere in the problem folder are
the grading theorem and the uniform \(cX/\log X\) fiber-complement theorem
used in (34). The only standard analytic input newly used here is the
prime number theorem in dyadic intervals (plus Mertens' estimate, obtained
from it by partial summation).

The sharp checks are:

- deleting all primes in a few ordinary dyadic cells is harmless because
  Lemma 1 loses at most twice the number of deleted cells;
- a large number \(r=r(K)\) of factors does not multiply that loss, because
  every central pair sum is repaired before the \(k\)-fold convolution;
- different anchors cannot collide, since the anchor is the unique factor
  below \(N^\delta\);
- repeated prime factors are excluded before counting, and cost only a
  fixed factor because every good cell contains \(N^{a+o(1)}\) primes;
- all constants are uniform over the finite band menu selected from (13),
  so \(f\) and its prime weights may change arbitrarily with \(N\).

No unresolved step remains in this alternate lower-prime-factor lemma.
