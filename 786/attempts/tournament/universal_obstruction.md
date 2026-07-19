# A quantitative uniform obstruction: four iterated logarithms

## Result

Let (f:\mathbb N\to\mathbb Q) be completely additive and put

\[
 B_f(N)=\{n\leq N:f(n)=1\},\qquad m_f(N)=N-|B_f(N)|.
\]

The largest-prime row charge and the zero-prime product construction can be
made quantitative even when their reciprocal budget grows with (N).  They
give the uniform estimate

\[
 \boxed{\quad m_f(N)\gg
   \frac{N}{\log N}\log\log\log\log N.\quad}             \tag{1}
\]

All iterated logarithms are understood only for sufficiently large (N).
In particular, (1) gives an explicit rate in the already proved
(m_f(N)=\omega(N/\log N)) result.  The proof is uniform in an arbitrary
(N)-dependent grading (f).

The only earlier input is the audited uniform bound

\[
 X-|\{n\leq X:g(n)=1\}|\geq cX/\log X                 \tag{2}
\]

for every completely additive (g), together with ordinary dyadic prime
number estimates and Mertens' estimate.  No product-measure approximation is
used.

## 1. Reciprocal mass of active primes

Call a prime (q) active if (f(q)\ne0).  Let (M) be the largest power of
two below (\sqrt{N/2}).  The largest-prime row argument (repeated briefly
below) gives an absolute constant (c_0>0) such that

\[
 m_f(N)\geq c_0\frac N{\log N}
       \sum_{\substack{q\leq M\\f(q)\ne0}}\frac1q-O(N/\log N).       \tag{3}
\]

Indeed, for (C_j=2^j\leq M) take

\[
 P_j=\left(\frac N{2C_j},\frac N{C_j}\right]\cap\mathbb P.
\]

Every (pk), with (p\in P_j) and (k\leq C_j), has unique largest prime
factor (p>M), and all these products are jointly distinct as (j,p,k)
vary.  If (f(p)=1), every active prime (q\leq C_j), used as a cofactor,
is an error in the (p)-row.  If (f(p)\ne1), the required cofactor value
is nonzero, and (2), after rescaling (f), supplies
(\gg C_j/\log C_j\) errors.  Since
(\pi(C_j)\ll C_j/\log C_j), in either case the row has at least a fixed
multiple of

\[
 A(C_j)=|\{q\leq C_j:q\text{ is active}\}|
\]

errors.  Also

\[
 |P_j|\gg\frac{N}{C_j\log N}.
\]

Summing the disjoint rows and interchanging the (j,q) sums proves (3);
the finitely many primes below the fixed threshold needed in (2) account
for the harmless (O(N/\log N)) term.

Write

\[
 L_1=\log N,\quad L_2=\log\log N,\quad
 L_3=\log\log\log N,\quad L_4=\log\log\log\log N,
\]

and normalize

\[
 R=\frac{m_f(N)L_1}{N}.
\]

Equation (3) implies

\[
 H:=\sum_{\substack{q\leq M\\f(q)\ne0}}\frac1q
 \leq C_0(R+1)                                           \tag{4}
\]

with an absolute (C_0).

## 2. A zero-prime band with moving exponent

We prove (1) by contradiction.  Fix a sufficiently small absolute
(\gamma>0), to be chosen at the end, and suppose

\[
 R<\gamma L_4.                                           \tag{5}
\]

Choose a small absolute (\varepsilon>0).  Starting at a sufficiently
large fixed index (i_0), consider the consecutive disjoint prime bands

\[
 I_i=(N^{a_i},N^{2a_i}],\qquad a_i=2^{-i-1}.             \tag{6}
\]

Take

\[
 s=\left\lceil\frac{H+1}{\varepsilon}\right\rceil.
\]

Among the first (s) bands in (6), one band

\[
 I=(N^a,N^{2a}]                                         \tag{7}
\]

satisfies

\[
 \sum_{\substack{p\in I\\f(p)\ne0}}\frac1p\leq\varepsilon.       \tag{8}
\]

Moreover, (4)--(6) give

\[
 a\geq \exp(-C_1(R+1)),\qquad a<1/8.                  \tag{9}
\]

Under (5), (a\log N\to\infty).  Thus all prime estimates below are
ordinary uniform dyadic estimates at arguments tending to infinity; no
short-interval PNT is being invoked.

Use logarithms to base (2) temporarily and put
(L=\log_2N).  Apart from two endpoint cells, partition (7) into

\[
 D_j=(2^j,2^{j+1}],\qquad aL+2\leq j\leq2aL-2.          \tag{10}
\]

The dyadic PNT gives

\[
 |D_j\cap\mathbb P|\geq c_1\frac{2^j}{j}.              \tag{11}
\]

Call (j) good if at least half of the lower bound in (11) consists of
zero-weight primes.  A bad cell contributes at least (c_2/j\gg1/(aL))
to the active reciprocal sum in (8).  On choosing (\varepsilon) small
enough, the set (G) of good indices therefore satisfies

\[
 |[aL+2,2aL-2]\cap\mathbb Z\setminus G|\leq\eta aL,     \tag{12}
\]

where (\eta>0) is any fixed sufficiently small absolute constant.

## 3. Explicit many-factor count

Fix a small absolute (\theta>0).  From (12), every integer

\[
 h\in[(3-\theta)aL,(3+\theta)aL]                       \tag{13}
\]

has at least (c_3aL) ordered representations

\[
 h=j_1+j_2,\qquad j_1,j_2\in G.                        \tag{14}
\]

This is elementary: before deleting bad cells, the permitted (j_1)'s
form an interval of length at least ((1-\theta)aL-O(1)), and every
deleted index destroys at most two representations.

Put

\[
 k=\left\lfloor\frac1{3a}+\frac12\right\rfloor,
 \qquad r=2k.                                           \tag{15}
\]

Increase the fixed (i_0), if necessary, so that (a) is small compared
with (\theta).  For every zero-weight anchor prime

\[
 \ell\leq N^{a/100},                                   \tag{16}
\]

set

\[
 T_\ell=\lfloor\log_2(N/\ell)\rfloor-r.                \tag{17}
\]

The average (T_\ell/k) lies in the interior of (13), with margin
(\gg aL).  To count (k)-tuples (h_1+\cdots+h_k=T_\ell), choose the
first (k-1) values in an interval of radius (c aL/k) around that
average; the forced last value then remains in (13).  Consequently there
are at least

\[
 \left(\frac{c_4aL}{k}\right)^{k-1}                    \tag{18}
\]

such (h)-tuples.  Combining (14) and (18) gives at least

\[
 (c_3aL)^k\left(\frac{c_4aL}{k}\right)^{k-1}           \tag{19}
\]

ordered (r)-tuples of good indices with sum (T_\ell).

For a good (j), let (Z_j) be the number of zero-weight primes in
(D_j).  Equations (10)--(12) give

\[
 Z_j\geq c_5\frac{2^j}{aL}.                            \tag{20}
\]

The least (Z_j) is much larger than (r), by (5), (9), and
(aL\to\infty).  Hence primes can be chosen successively and distinctly,
losing at most a factor (2^{-r}).  For each index tuple in (19), the
number of ordered choices of distinct zero-weight primes
(q_s\in D_{j_s}) is at least

\[
 2^{-r}\prod_{s=1}^rZ_{j_s}
 \geq \left(\frac{c_6}{aL}\right)^r2^{T_\ell}.         \tag{21}
\]

An ordered prime tuple determines its index tuple.  After multiplying
(19) and (21), then dividing by at most (r!) orderings of the same
squarefree product, we obtain at least

\[
 \exp(-C_2r\log(r+2))\frac{2^{T_\ell}}{aL}             \tag{22}
\]

distinct products.  By (17),

\[
 2^{T_\ell}\geq\frac{N}{2^{r+1}\ell},
\]

and the extra (2^{-r}) is absorbed by the exponential factor in (22).
Thus (22) is at least

\[
 \exp(-C_3r\log(r+2))\frac{N}{\ell\log N}.            \tag{23}
\]

Every resulting integer

\[
 n=\ell q_1\cdots q_r\leq N                           \tag{24}
\]

has (f(n)=0), hence is outside (B_f(N)).  Also
(\ell<N^{a}<q_s\), so (\ell) is the unique prime factor below
(N^{a/100}).  The families for different anchors are disjoint.  Finally,
all prime factors in (24) are below (N^{2a}<N^{1/4}<M); these omissions
are separated by largest prime factor from the errors used in (3).

## 4. Summing anchors and closing the estimate

Mertens' estimate, (4), (5), and (9) imply

\[
\begin{aligned}
 \sum_{\substack{\ell\leq N^{a/100}\\f(\ell)=0}}
       \frac1\ell
 &\geq \log\log(N^{a/100})-H-O(1)\\
 &=L_2+\log a-O(H+1)\\
 &\geq \tfrac12L_2                                      \tag{25}
\end{aligned}
\]

for all sufficiently large (N).  Summing (23) over these anchors yields

\[
 R\geq L_2\exp(-C_4r\log(r+2)).                        \tag{26}
\]

On the other hand, (4), (9), and (15) give

\[
 r\leq\exp(C_5(R+1)).                                  \tag{27}
\]

Under the contradictory assumption (5),

\[
 r\leq C L_3^{C_5\gamma}.
\]

Choose (\gamma>0) so small that, for all sufficiently large (N),

\[
 C_4r\log(r+2)\leq L_3^{1/2}.                          \tag{28}
\]

Equations (26) and (28) now give

\[
 R\geq\exp(L_3-L_3^{1/2})\gg L_4,
\]

contradicting (5).  This proves (1).

## 5. Checks and limitations

1. The moving band exponent causes no uniform-PNT issue: under the only
   branch where the construction is used, (a\log N\to\infty), and all
   prime intervals are ordinary factor-two intervals.
2. The factor count (r) is no longer fixed.  Formulae (18)--(23) retain
   the losses (k^{k}), (r!), and (2^r); together they cost only
   (\exp(O(r\log r))), which is precisely what permits the (L_4) gain.
3. Repeated primes are excluded during the successive choices, rather than
   removed by a fixed-(r) asymptotic.
4. The anchor cutoff must move with (a).  Nevertheless
   (\log\log(N^{a/100})=L_2+\log a+O(1)), and
   (|\log a|+H=O(L_4)=o(L_2)).
5. This is still not a constant-density obstruction.  It rules out an
   (O(N/\log N)) deletion scheme, with an explicit four-log margin, but
   an adaptive density-(1-o(1)) scheme could in principle delete much
   more than the lower bound in (1).

