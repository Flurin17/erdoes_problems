# A constant finite gap from exact-atom concentration and a boundary sieve

## Result

Let (f:\mathbb N\to\mathbb R) be completely additive and let (t\ne0).
There is an absolute constant (c>0) such that, for all sufficiently large
(N), uniformly in (f) and (t),

\[
 \#\{n\le N:f(n)=t\}\le (1-c)N.                 \tag{1}
\]

The value of (c) obtained below is extremely small and is not intended to
be sharp.  The proof has two genuinely different ingredients.

1. The exact-atom theorem of Halász--Ruzsa says that a large atom forces the
   reciprocal-prime mass of the active primes to be bounded.
2. A separate, elementary boundary sieve says that a prime set of bounded
   reciprocal mass misses a positive proportion of the integers.  Its proof
   uses a lightly deleted polynomial prime band, a fixed-fold local
   convolution, and logarithmically many small anchors.

The second ingredient is essential.  Marginal Kubilius approximation does
not make the small-prime and rough parts independent.

## 1. The exact-atom theorem and its precise use

We use the following standard theorem.

**Halász--Ruzsa exact-atom theorem.**  There is an absolute constant (C)
such that, for every (x\ge2) and every real additive function (g),

\[
 \frac1x\sup_{z\in\mathbb R}\#\{n\le x:g(n)=z\}
 \le
 \frac{C}{\sqrt{1+H_g(x)}},
 \qquad
 H_g(x):=\sum_{\substack{p\le x\\g(p)\ne0}}\frac1p .           \tag{2}
\]

This is a pointwise theorem, uniform in an (x)-dependent (g).  General
additivity is enough; complete additivity is more than is needed.  No
condition on (g(p^a)), (a\ge2), is required for the displayed weaker
prime-only denominator.

Here is a check of the exact-value formulation and of the possible
Archimedean exception.  A standard interval version, with

\[
 Q_h(x;g)=\frac1x\sup_y
 \#\{n\le x:y<g(n)\le y+h\},
\]

states

\[
 Q_h(x;g)\ll (1+D_h^2)^{-1/2},                    \tag{3}
\]

where, up to harmless absolute normalizations,

\[
 D_h^2=min_{\lambda\in\mathbb R}
 \left\{
  \lambda^2+
  \sum_{p\le x}\frac1p
  \min\!\left(1,
   \left|\frac{g(p)}h-\lambda\log p\right|^2
  \right)
 \right\}.                                        \tag{4}
\]

Fix (x) and (g), and let (h\downarrow0).  Taking (\lambda=0) shows
that the minimum in (4) is at most (H_g(x)).  Any minimizing sequence is
therefore bounded, since (4) contains (\lambda^2).  For every prime with
(g(p)\ne0), its summand then tends to (1/p).  Hence

\[
 \lim_{h\downarrow0}D_h^2=H_g(x),                 \tag{5}
\]

the reverse inequality following from the preceding boundedness argument.
An exact fiber is contained in an interval of every positive length, so
(3)--(5) give (2).  Thus the logarithmic drift
(g(p)\approx\lambda\log p), which must be retained in an interval theorem,
does not survive the exact-atom limit.  Arbitrarily small but nonzero prime
weights still contribute fully to (H_g(x)).

## 2. The bounded-budget boundary sieve

The following is the missing finite-boundary statement that an independent
geometric model does not supply.

**Lemma (bounded reciprocal budget).**  For every fixed (K<\infty) there
are constants (c_K>0) and (N_K) such that, for every (N\ge N_K) and
every set (S) of primes at most (N) satisfying

\[
 \sum_{p\in S}\frac1p\le K,                       \tag{6}
\]

one has

\[
 \#\{n\le N:p\nmid n\text{ for every }p\in S\}
 \ge c_KN.                                         \tag{7}
\]

The constants are uniform over moving sets (S=S_N).

### 2.1 A harmonic supply of small (S)-free anchors

For (T\ge2), put

\[
 \mathcal L_S(T)=\{\ell\le T:p\nmid\ell\ (p\in S)\}.
\]

There is a constant (b_K>0) such that, for all sufficiently large (T),

\[
 \sum_{\ell\in\mathcal L_S(T)}\frac1\ell\ge b_K\log T.          \tag{8}
\]

Indeed, for (\sigma>1), Euler products give

\[
 \sum_{\substack{n\ge1\\p\nmid n\ (p\in S)}}n^{-\sigma}
 =\zeta(\sigma)\prod_{p\in S}(1-p^{-\sigma}).                  \tag{9}
\]

Since

\[
 -\log(1-p^{-\sigma})\le\frac1{p-1}\le\frac2p,
\]

the product in (9) is at least (e^{-2K}).  Let

\[
 A=2K+\log4,
 \qquad \sigma=1+\frac A{\log T}.
\]

Using (\zeta(\sigma)\ge1/(\sigma-1)) and

\[
 \sum_{n>T}n^{-\sigma}
 \le T^{-\sigma}+\int_T^\infty u^{-\sigma}\,du
 \le T^{-1}+\frac{e^{-A}}{\sigma-1},              \tag{10}
\]

we obtain, after increasing the lower threshold for (T),

\[
 \sum_{\ell\in\mathcal L_S(T)}\ell^{-\sigma}
 \ge \frac{e^{-2K}}{2(\sigma-1)}.
\]

Because (\ell^{-1}\ge\ell^{-\sigma}), (8) follows, for example with

\[
 b_K=\frac{e^{-2K}}{3(2K+\log4)}.                 \tag{11}
\]

This Dirichlet-series argument is only being used to produce anchors.  It
does not assert an Euler-product density at the endpoint (N).

### 2.2 Find a polynomial band with many zero primes in most dyadic cells

Fix a sufficiently small absolute (\varepsilon>0).  Let

\[
 J=\left\lceil\frac K\varepsilon\right\rceil+1,
 \qquad a_s=4^{-s-4}\quad(1\le s\le J).
\]

The exponent intervals ([a_s,2a_s]) are pairwise disjoint.  By (6), for
some (s), writing (a=a_s),

\[
 \sum_{\substack{p\in S\\N^a<p\le N^{2a}}}\frac1p<\varepsilon. \tag{12}
\]

Here (a>0) is fixed once (K) is fixed, although it can be very small.
Put (L=\log_2N).  By the prime number theorem in dyadic intervals, there
is an absolute (c_0>0) such that, for all sufficiently large (N) and all
integers (j\in[aL,2aL]),

\[
 \#\{p:2^j<p\le2^{j+1}\}\ge c_0\frac{2^j}{j}.                  \tag{13}
\]

Call such a cell (j) good if it contains at least
(c_0 2^j/(2j)) primes outside (S), and bad otherwise.  A bad cell
contributes at least

\[
 \frac{c_0}{4j}\ge\frac{c_0}{8aL}                              \tag{14}
\]

to the sum in (12).  Consequently the number of bad cells is at most

\[
 \frac{8\varepsilon aL}{c_0}.                                  \tag{15}
\]

Choose (\varepsilon) once and for all so that the last quantity is at
most (aL/100).

### 2.3 A local convolution of zero-prime products

Let

\[
 I_2=\{h\in\mathbb Z:(3-\tfrac14)aL\le h
                         \le(3+\tfrac14)aL\}.
\]

For each (h\in I_2), there are at least (c_1aL) ordered pairs of good
cell indices (j,j'in[aL,2aL]) with (j+j'=h).  Indeed, before deleting
bad cells the intersection has length at least (3aL/4-O(1)), and (15)
removes at most twice the number of bad indices.

Let (\mathcal Q_h) be the set of products (pq), where (p,q\notin S)
are distinct primes from good cells whose indices sum to (h).  Equations
(13) and the preceding pair count imply

\[
 |\mathcal Q_h|\ge c_a\frac{2^h}{L}                              \tag{16}
\]

uniformly for (h\in I_2).  To check (16), each good cell pair supplies

\[
 \gg\frac{2^{j+j'}}{jj'}\gg_a\frac{2^h}{L^2}
\]

prime pairs, there are (\gg aL) cell pairs, and an unordered semiprime
is counted at most twice.  The diagonal case is handled by choosing two
distinct primes; its cell contains a number of primes tending to infinity.

Choose the integer (k) nearest to (1/(3a)).  Then

\[
 |3ak-1|\le\frac{3a}{2}.                                        \tag{17}
\]

The (k)-fold sum of (I_2) contains a fixed neighborhood of (L): its
center is (3akL), while its half-width is (akL/4=(1/12+O(a))L).
In particular, if

\[
 \delta=\frac a{10},                                            \tag{18}
\]

then, for every sufficiently large (N) and every
(R\in[(1-\delta)L-2k,L]),

\[
 \#\{(h_1,\ldots,h_k)\in I_2^k:h_1+\cdots+h_k=R\}
 \ge c_{a,k}L^{k-1}.                                            \tag{19}
\]

For completeness, (19) is the elementary lattice-box convolution bound:
after scaling by (L), the target lies in a compact subinterval of the
interior of the (k)-fold sum of the fixed interval
([(3-1/4)a,(3+1/4)a]).  Choose (k-1) coordinates in fixed small
subintervals about an interior representation; the final coordinate is
then in the original interval.  This gives (\gg L^{k-1}) integer choices,
uniformly on that compact target interval.

Now let (X\in[N^{1-\delta},N]), and put

\[
 R=\lfloor\log_2X\rfloor-2k.
\]

For every tuple counted in (19), select one semiprime from each
(\mathcal Q_{h_i}).  Their product is at most

\[
 2^{h_1+2}\cdots2^{h_k+2}=2^{R+2k}\le X.
\]

Using (16) and (19), the number of representations produced is at least

\[
 c_{a,k}L^{k-1}\frac{2^R}{L^k}gg_{a,k}\frac X{\log N}.         \tag{20}
\]

Every resulting integer is composed only of primes outside (S).  A fixed
integer has at most ((2k)!) representations of the displayed type: its
multiset of (2k) prime factors is fixed, and one only assigns those factors
to ordered pairs.  Therefore (20) gives the genuine distinct-product bound

\[
 \#\{q\le X:q\text{ is a product of }2k
       \text{ primes in }(N^a,N^{2a}]\setminus S\}
 \ge d_K\frac X{\log N}                                       \tag{21}
\]

for some (d_K>0), uniformly for (X\in[N^{1-\delta},N]).

### 2.4 Attach the anchors

Take (T=N^\delta), with (\delta) as in (18).  For every
(\ell\in\mathcal L_S(T)), apply (21) with (X=N/\ell).  Every product
(n=\ell q) is (S)-free and at most (N).  Products belonging to
different anchors are distinct: every prime factor of (q) exceeds
(N^a>T), so (q) is exactly the part of (n) supported on the chosen
polynomial band and (\ell) is the complementary part.  Thus (8) and
(21) yield

\[
 \begin{aligned}
 \#\{n\le N:n\text{ is }S\text{-free}\}
 &\ge \sum_{\ell\in\mathcal L_S(T)}
       d_K\frac{N}{\ell\log N}\\
 &\ge d_Kb_K\delta N.
 \end{aligned}                                                   \tag{22}
\]

This proves the bounded-budget lemma with (c_K=d_Kb_K\delta>0).

## 3. Deduction of the universal finite gap

Let

\[
 S_f(N)=\{p\le N:f(p)\ne0\},
 \qquad H=\sum_{p\in S_f(N)}\frac1p.
\]

Choose a fixed (K) so large that

\[
 \frac C{\sqrt{1+K}}\le\frac12,                                \tag{23}
\]

where (C) is from (2).  If (H\ge K), equation (2) bounds every fiber by
(N/2).  If (H<K), the bounded-budget lemma gives at least (c_KN)
integers divisible by no active prime.  Complete additivity gives (f(n)=0)
on all of them, so none belongs to a nonzero fiber.  Therefore

\[
 \#\{n\le N:f(n)=t\}
 \le \max(1/2,1-c_K)N
 =(1-c)N,                                                       \tag{24}
\]

with (c=\min(1/2,c_K)>0).  This proves (1).

For the repetition-allowed interpretation of Problem 786, every rigid set
in ([1,N]) lies in a nonzero exact level of a rational completely additive
function.  Hence (24) gives a negative answer to the finite density-(1-o(1))
question as well as an absolute density gap.

## 4. What Kubilius approximation does and does not prove

For (y\le N), set

\[
 D_y(n)=\prod_{p\le y}p^{v_p(n)},
 \qquad V(y)=\prod_{p\le y}(1-1/p),
\]

and let (D_y^*=\prod_{p\le y}p^{G_p}), where the (G_p) are independent
with

\[
 \Pr(G_p=j)=(1-1/p)p^{-j}.
\]

For a (y)-smooth integer (d), the exact laws are

\[
 \Pr(D_y(U_N)=d)=\frac{\Phi(N/d,y)}N,
 \qquad
 \Pr(D_y^*=d)=\frac{V(y)}d,                                    \tag{25}
\]

where (\Phi(X,y)) counts (y)-rough integers at most (X).  The standard
Kubilius fundamental lemma implies total-variation convergence in the safe
range

\[
 u=\frac{\log N}{\log y}\longrightarrow\infty.                 \tag{26}
\]

Quantitative versions have error of shape
(\exp[-c u\log(u+1)]), plus a finite-(N) term; no particular numerical
constant is needed here.  Data processing transfers this approximation to
an arbitrary moving weighted sum over primes (p\le y).

Fixed (u) is outside that conclusion.  For example, with
(w_p=1_{p>\sqrt N}), actual size exclusion gives

\[
 \Pr_{n\le N}(f(n)=1)\longrightarrow\log2,
\]

whereas the independent geometric model gives ((\log2)/2).  More
generally, the product model assigns positive mass to (D_y^*>N) when
(u) is fixed, while the actual variable never exceeds (N).

Even in the safe marginal range (26), one may not convolve the small-prime
score with an allegedly independent rough contribution.  Writing
(n=ab), with (a) (y)-smooth and (b) (y)-rough, gives the exact
disintegration

\[
 \Pr(f(n)=t)
 =\frac1N\sum_{\substack{b\le N\\P^-(b)>y}}
 \#\{a\le N/b:a\text{ is }y\text{-smooth},
                  f(a)=t-f(b)\}.                                \tag{27}
\]

Conditional on (b), the smooth factor is uniformly counted up to the
moving boundary (N/b); it is not distributed with the harmonic weights
(V(y)/a).  Already for (y=2), the marginal (v_2(n)) is asymptotically
geometric, but conditional on the odd part (b>N/2) it is identically zero.
Thus a black-box Kubilius convolution cannot establish (1).

The proof above avoids this invalid step.  Halász--Ruzsa handles large
active reciprocal mass directly in the arithmetic model, while the
polynomial-band construction handles the bounded-mass boundary regime.

## Audit targets

The decisive points to audit are:

1. the exact-atom limit (5), especially boundedness of the minimizing
   logarithmic drift;
2. uniformity of the dyadic PNT estimate over the finitely many exponent
   bands selected after (K) is fixed;
3. the lattice convolution interval in (19) and the (2k) upper-size slack;
4. the representation bound ((2k)!) and uniqueness after attaching an
   anchor;
5. the order of quantifiers: (K,a,k,\delta) are fixed first, and only then
   (N\to\infty).

