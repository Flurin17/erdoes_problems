# Largest-prime-factor charging for the cofactor profile

## Outcome

Let
\[
 B=\{n\leq N:f(n)=1\},\qquad E=[1,N]\setminus B,\qquad m=|E|,
\]
where (f) is a rational completely additive function.  This note proves
the uniform improvement
\[
 \boxed{m=\omega\!\left(\frac N{\log N}\right).} \tag{1}
\]
More explicitly, for every fixed (K>0), all sufficiently large (N)
satisfy
\[
 m>K\frac N{\log N}                                      \tag{2}
\]
for every such (f).  Consequently every repetition-allowed PLR subset of
([1,N]) omits (omega(N/\log N)) elements.

The two charges are separated by largest prime factor.  Bad entries in the
large-prime rows have largest prime factor above a cutoff (M\asymp\sqrt N).
They force the reciprocal mass of primes with nonzero weight below (M) to
be bounded.  Products made only from zero-weight primes have largest prime
factor below (M), hence are disjoint from all row charges.  A reciprocal
budget lemma, proved from the prime number theorem by a local convolution
argument, shows that bounded nonzero-prime mass leaves
\(gg_K N\log\log N/\log N\) such zero products.  This contradicts (2).

The known (cN/\log N) theorem is used recursively in individual rows.  No
uniform product-measure approximation for a moving prime support is used.

## 1. Exact largest-prime split

Let (C_j=2^j), and let (J) be maximal subject to
\[
 M:=C_J<\sqrt{N/2}.
\]
Thus (M\geq\sqrt{N/8}).  Put
\[
 P_j=\left\{p\text{ prime}:\frac{N}{2C_j}<p\leq\frac N{C_j}\right\},
 \qquad R_j=|P_j|.                                      \tag{3}
\]
For (p\in P_j), define its row error
\[
 e(p,j)=|\{k\leq C_j:f(pk)\ne1\}|,
 \qquad B_j=\sum_{p\in P_j}e(p,j).                     \tag{4}
\]

Every participating prime satisfies
\[
 p>\frac N{2M}>M\geq C_j.
\]
It follows that (p=P^+(pk)), and the products (pk), over every (j,p,k)
in (3)--(4), are jointly distinct.  Indeed, if (pk=q\ell) with (p\ne q),
then (p\mid\ell<p).  Therefore, with
\[
 E_>:=\{n\in E:P^+(n)>M\},\qquad E_\leq:=E\setminus E_>,
\]
we have the stronger tagged estimate
\[
 \sum_{j=0}^J B_j\leq |E_>|.                            \tag{5}
\]
This records where the errors live, rather than only bounding their sum by
(m).

Call a prime (q) **active** when (f(q)\ne0), and write
\[
 A(x)=|\{q\leq x:q\text{ prime and }f(q)\ne0\}|.        \tag{6}
\]

### Lemma 1 (every upper row detects active lower primes)

There are absolute constants (kappa>0) and (C_0) such that, whenever
(C_j\geq C_0),
\[
 e(p,j)\geq\kappa A(C_j)\qquad(p\in P_j).               \tag{7}
\]

#### Proof

The good entries in the (p)-row require
\[
 f(k)=1-f(p).                                             \tag{8}
\]
If (f(p)=1), every active prime (q\leq C_j) violates (8), so
\(e(p,j)\geq A(C_j)\).

If (f(p)\ne1), the target (t=1-f(p)) is nonzero.  Apply the already
proved (cN/\log N) theorem at scale (C_j) to the completely additive
function (f/t).  For an absolute (c_0>0),
\[
 |\{k\leq C_j:f(k)\ne t\}|\geq c_0\frac{C_j}{\log C_j}. \tag{9}
\]
The elementary prime-counting upper bound gives
\(A(C_j)\leq\pi(C_j)\leq C_1C_j/\log C_j\).  Thus (9) is at least
\((c_0/C_1)A(C_j)\).  Taking
\(kappa=\min(1,c_0/C_1)\) proves (7). \(square\)

The point of (7) is that no dominant-color choice is needed.  A row of
prime color (1) directly sees all active prime cofactors; every other row
pays the recursive nonzero-fiber penalty.

### Proposition 2 (reciprocal active-prime charge)

There is an absolute (c_2>0) such that
\[
 |E_>|\geq c_2\frac N{\log N}
 \left(\sum_{\substack{C_0\leq q\leq M\\ f(q)\ne0}}\frac1q\right).
                                                               \tag{10}
\]

#### Proof

The prime number theorem in dyadic intervals, uniformly for
\(C_j\leq M\), gives
\[
 R_j\geq c_3\frac{N}{C_j\log N}.                       \tag{11}
\]
Combining (5), (7), and (11), and summing only over (C_j\geq C_0), gives
\[
 |E_>|\geq c_4\frac N{\log N}
       \sum_{C_0\leq C_j\leq M}\frac{A(C_j)}{C_j}.      \tag{12}
\]
Interchange the two finite sums.  For each active prime
\(q\in[C_0,M]\), the dyadic tail beginning at the first (C_j\geq q)
contributes at least (1/(2q)).  Hence
\[
 \sum_j\frac{A(C_j)}{C_j}
 \geq\frac12\sum_{\substack{C_0\leq q\leq M\\f(q)\ne0}}\frac1q,
\]
which proves (10). \(square\)

In particular, if (m\leq KN/\log N), then
\[
 \sum_{\substack{q\leq M\\f(q)\ne0}}\frac1q\leq K_1(K),             \tag{13}
\]
where the finitely many primes below (C_0) have been absorbed into
(K_1(K)).

## 2. A reciprocal-budget prime-tuple lemma

The next lemma is the lower-largest-prime counterpart of Proposition 2.
It is stated for arbitrary moving sets of primes; this is important because
the weights of (f) may depend on (N).

### Lemma 3 (bounded reciprocal deletion leaves many products)

Fix (K_1<\infty), and let (M_N\geq c\sqrt N), where (c>0) is fixed.
For each (N), let \(\mathcal Z_N\) be a set of primes at most (M_N)
satisfying
\[
 \sum_{\substack{p\leq M_N\\p\notin\mathcal Z_N}}\frac1p\leq K_1.
                                                               \tag{14}
\]
There is a constant (c_{K_1}>0) such that, for all sufficiently large
(N),
\[
 \#\left\{n\in(N/2,N]:
       n\text{ is squarefree and every }p\mid n\text{ belongs to }
       \mathcal Z_N\right\}
 \geq c_{K_1}\frac{N\log\log N}{\log N}.               \tag{15}
\]
Moreover, the integers counted in (15) may be required to have all prime
factors below (N^{1/4}).

#### Proof

We give the prime-tuple argument, including the uniformity with respect to
the deleted prime set.

Put (L=\log N).  Choose once and for all a small absolute
\(\varepsilon_0>0\), as specified in the local two-prime estimate below.
For integers (i\geq i_0), where (i_0) is a sufficiently large absolute
constant, set
\[
 a_i=2^{-i-1},\qquad
 I_i=(N^{a_i},N^{2a_i}].                                  \tag{16}
\]
The intervals (I_i) are disjoint, have upper exponent below (1/4), and
standard partial summation from the prime number theorem gives
\[
 \sum_{p\in I_i}\frac1p=\log2+o(1)                       \tag{17}
\]
for each fixed (i).

Among any
\[
 H=\left\lfloor K_1/\varepsilon_0\right\rfloor+2
\]
consecutive intervals in (16), one, say (I=(N^a,N^{2a}]), obeys
\[
 \sum_{\substack{p\in I\\p\notin\mathcal Z_N}}\frac1p
 \leq\varepsilon_0.                                     \tag{18}
\]
Otherwise (14) is violated.  There are only (H) possible values of (a),
all fixed once (K_1) is fixed.  We may enlarge (i_0) so that each is as
small as needed below.

Define reciprocal-prime measures on logarithmic exponent space by
\[
 \mu_N=\sum_{p\in I}\frac1p\,\delta_{\log p/L},\qquad
 \nu_N=\sum_{\substack{p\in I\\p\notin\mathcal Z_N}}
              \frac1p\,\delta_{\log p/L},\qquad
 \mu_N^0=\mu_N-\nu_N.                                   \tag{19}
\]
Thus \(\|\nu_N\|\leq\varepsilon_0\).  On the fixed interval
([a,2a]), the PNT and partial summation say that \(\mu_N\) tends locally
to (dt/t).  We need the following local form.  If
\(|W|\asymp1/L\) and
\[
 W\subset[(3-1/10)a,(3+1/10)a],
\]
then
\[
 (\mu_N*\mu_N)(W)\geq c\frac{|W|}{a},
 \qquad
 \sup_x\mu_N(W-x)\leq C\frac{|W|}{a},                  \tag{20}
\]
with absolute (c,C>0).  To verify (20), write the convolution as a prime
sum and apply the dyadic-interval PNT to the second prime.  In the limiting
integral the first estimate is
\[
 \int_{[a,2a]\cap(W-[a,2a])}\frac{dt}{t(s-t)}
 \gg\frac1a
\]
times (|W|); throughout the displayed central interval the overlap has
length at least (0.8a).  The same calculation with an upper PNT bound
gives the second estimate.  This also proves (20) uniformly for intervals
whose lengths are any fixed constant multiple of (1/L).

Since all measures are positive,
\[
 \mu_N^{*2}-(\mu_N^0)^{*2}
   =\nu_N*\mu_N+\mu_N^0*\nu_N
   \leq2\nu_N*\mu_N.                                    \tag{21}
\]
Equations (18), (20), and (21) show, after choosing the absolute
\(\varepsilon_0<c/(4C)\), that
\[
 (\mu_N^0)^{*2}(W)\geq c'\frac{|W|}{a}                  \tag{22}
\]
for every such (W).  This is the robustness step: deleting a small total
reciprocal mass cannot punch a local hole in the two-prime convolution.

Let
\[
 J=[(3-1/20)a,(3+1/20)a].                                \tag{23}
\]
Choose the integer (k) nearest to (1/(3a)), and put (r=2k).  Since
(a) was forced sufficiently small, there is an absolute
\(\delta>0\), depending only on the finite menu of possible (a)'s, such
that
\[
 [1-2\delta,1]\subset\operatorname{int}(kJ).             \tag{24}
\]
Convolving (22) (k) times gives, uniformly for
\(s\in[1-\delta,1]\),
\[
 (\mu_N^0)^{*r}([s-\log2/L,s])\geq\frac{c_a}{L}.         \tag{25}
\]
For completeness, (25) can be seen without invoking a local-limit theorem:
partition (J) into intervals of length (asymp1/L).  For a fixed target
window, (24) leaves \(\asymp L^{k-1}\) admissible choices of the first
(k-1) cells; (22) gives mass \(\gg1/L\) to each cell, including the forced
last one.  Their products sum to \(\gg1/L\).  Since the possible (a)'s
form a finite set depending only on (K_1), the constants and the possible
values of (r) may be made uniform in (N).

Tuples with a repeated prime contribute (o(1/L)) to (25).  Indeed, after
choosing a repeated pair their reciprocal mass is at most
\[
 \sum_{q>N^a}\frac1{q^2}=O(N^{-a}),
\]
and the remaining (r-2) reciprocal measures have bounded total mass.
Thus (25), with a smaller constant, counts ordered tuples of distinct primes.

Now fix (0<\delta_0<\min(\delta,a/2)\).  The PNT, (14), and Mertens
partial summation give
\[
 \sum_{\substack{\ell\leq N^{\delta_0}\\
                   \ell\in\mathcal Z_N}}
       \frac1\ell
 \geq\log\log N-O_{K_1}(1).                             \tag{26}
\]
For each prime \(\ell\) in (26), take
\(s=1-\log\ell/L\) in (25).  It follows that the reciprocal weight of
ordered, distinct (r)-tuples (q_1,\ldots,q_r\in I\cap\mathcal Z_N)
satisfying
\[
 \frac N{2\ell}<q_1\cdots q_r\leq\frac N\ell           \tag{27}
\]
is at least (c_a/L).  Since every product in (27) exceeds
\(N/(2\ell)\), the number of ordered tuples is at least
\[
 c_a\frac{N}{\ell L}.                                   \tag{28}
\]

Every resulting integer
\(n=\ell q_1\cdots q_r\) lies in ((N/2,N]), is squarefree, and has exactly
one prime factor below (N^{\delta_0}); all the other factors exceed
(N^a).  Unique factorization therefore makes the constructions for
different \(\ell\) disjoint, and within one \(\ell\) the only overcount is
the at most (r!) orderings of the (q_i).  Sum (28), use (26), and absorb
(r!) into the constant.  This proves (15).  Finally all the factors are
at most (N^{2a}<N^{1/4}). \(square\)

## 3. The multiscale profile inequality and the omega bound

Let
\[
 \mathcal Z_N=\{q\leq M:q\text{ prime and }f(q)=0\}.
\]
Every integer composed only of primes in \(\mathcal Z_N\) has (f)-value
zero and hence belongs to (E).  The particular integers constructed in
Lemma 3 have largest prime factor below (N^{1/4}<M), so all of them lie in
(E_\leq).  Proposition 2 and Lemma 3 are therefore genuinely disjoint
charges, not two lower bounds on the same exceptional integers.

We can record the resulting profile alternative as follows.  For every
fixed (K_1), either
\[
 \sum_{\substack{q\leq M\\f(q)\ne0}}\frac1q>K_1,
\]
in which case (10) gives
\[
 |E_>|\gg K_1\frac N{\log N},                            \tag{29}
\]
or the sum is at most (K_1), in which case Lemma 3 gives
\[
 |E_\leq|\gg_{K_1}\frac{N\log\log N}{\log N}.           \tag{30}
\]
In both cases the two sides may be added because their largest-prime ranges
are disjoint.

To prove (1), suppose otherwise.  Then for some fixed (K), along an
unbounded sequence of (N) there are completely additive (f=f_N) with
\[
 m\leq K\frac N{\log N}.                                 \tag{31}
\]
Proposition 2 makes the active-prime reciprocal sum at most a fixed
(K_1=K_1(K)).  Lemma 3, applied to the zero-weight primes, then yields
\[
 m\geq |E_\leq|geq c_{K_1}\frac{N\log\log N}{\log N},  \tag{32}
\]
which contradicts (31) once \(\log\log N>K/c_{K_1}\).  This proves (1).

Finally, if (A\subset[1,N]) is repetition-allowed PLR, the grading theorem
places (A) inside such a level (B).  Since
\(N-|A|\geq N-|B|=m\), the same omega lower bound holds for (A).

## 4. Dependency and audit checklist

The proof uses only:

1. the exact grading theorem;
2. the already proved uniform (cX/\log X) complement bound for a nonzero
   additive fiber, applied at cofactor scale (X=C_j);
3. the prime number theorem in fixed polynomial and dyadic intervals, plus
   partial summation;
4. unique factorization.

The largest-prime tag is essential twice: (5) puts every row error above
(M), while the tuple construction puts every zero product below (M).
Thus the earlier overlap warning does not apply.

The sharp incidence-cut falsification model also passes the intended test.
An abstract cut can keep the reciprocal active-prime mass bounded while
paying only (O(N/\log N)), but it does not impose complete additivity on
the lower primes.  Here complete additivity turns the untouched lower
prime mass into the zero products counted by Lemma 3.  Any audit should
focus especially on the uniform deleted-measure estimate (20)--(25), the
removal of repeated primes, and the separation (P^+(n)>M) versus
(P^+(n)<M).
