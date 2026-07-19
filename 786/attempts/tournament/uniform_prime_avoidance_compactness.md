# Uniform avoidance of a bounded-harmonic set of primes

## Statement

For every `M < infinity` there is a constant `c(M) > 0` with the
following property.  If `x >= 1` and `S` is a set of primes satisfying

\[
 \sum_{\substack{p\in S\\p\le x}}\frac1p\le M,
\]

then

\[
 Q_S(x):=\#\{n\le x:p\nmid n\text{ for every }p\in S\}
 \ge c(M)x.
\]

The proof below is elementary modulo two standard estimates about primes:
Mertens' formula for reciprocal primes and the fixed-`k` estimate that the
number of squarefree integers at most `x` with `k` prime factors is `o_k(x)`.
It proves existence of `c(M)` but does not give a useful explicit value.

## 1. Contradiction sequence and fixed primes

Suppose the assertion is false.  There are `x_j` tending to infinity and
sets `S_j` such that

\[
 \sum_{p\in S_j}\frac1p\le M,
 \qquad
 \frac{Q_{S_j}(x_j)}{x_j}\longrightarrow0.                 \tag{1}
\]

Only primes at most `x_j` matter, so they are understood in the first sum.
After diagonalizing, the indicator of membership in `S_j` converges for
every fixed prime.  Let `F` be the set of primes which are eventually
present.  Fatou gives

\[
 \sum_{p\in F}\frac1p\le M,
 \qquad
 V_F:=\prod_{p\in F}\left(1-\frac1p\right)>0.             \tag{2}
\]

Put `R_j=S_j\setminus F`.  For every fixed `B`, eventually every prime in
`R_j` exceeds `B`.  Consequently

\[
 \sum_{p\in R_j}\frac1{p^2}\longrightarrow0.              \tag{3}
\]

Moreover, dominated convergence on the summable series over `F` gives

\[
 \sum_{p\in F\setminus S_j}\frac1p\longrightarrow0.       \tag{4}
\]

Thus `F` will contribute its exact Euler factor `V_F`, while `R_j` has no
individual atom of nonvanishing reciprocal weight.

## 2. The logarithmic-scale limit

Define a finite measure on `[0,1]` by

\[
 \nu_j=\sum_{p\in R_j}\frac1p\,
        \delta_{\log p/\log x_j}.
\]

Its mass is at most `M`, so, after taking a subsequence, it converges weakly
to a measure `nu`.  On every compact subinterval of `(0,1]`, the ambient
prime measures converge by Mertens' formula:

\[
 \sum_{p\le x_j}\frac1p\,
 \delta_{\log p/\log x_j}
 \ \Longrightarrow\ \frac{dt}{t}.
\]

More precisely, test against a nonnegative continuous function supported
away from zero and use `nu_j <= Lambda_j`.  It follows that

\[
 d\nu=h\,\delta_0+a(t)\frac{dt}{t},
 \qquad 0\le a(t)\le1,
 \qquad h+\int_0^1a(t)\frac{dt}{t}\le M.                  \tag{5}
\]

The atom `h delta_0` consists of primes which tend to infinity but are
subpolynomial in `x_j`.  It must not be confused with the true fixed primes
in `F`.

## 3. Factorial moments and inclusion-exclusion

For uniform `n` in `[1,x_j]`, let

\[
 \Omega_j(n)=\#\{p\in S_j:p\mid n\}.
\]

For every fixed `k`,

\[
 \mathbb E\binom{\Omega_j}{k}
 =\sum_{p_1<\cdots<p_k\in S_j}
   \frac{\lfloor x_j/(p_1\cdots p_k)\rfloor}{x_j}.        \tag{6}
\]

The sum may be restricted to products at most `x_j`.  Replacing the floor
term by `1/(p_1\cdots p_k)` costs `o(1)`: each summand costs at most `1/x_j`,
and the number of squarefree `d<=x_j` with `omega(d)=k` is `o_k(x_j)`.
A standard quantitative form is

\[
 \#\{d\le x:d\text{ squarefree},\ \omega(d)=k\}
 \ll_k\frac{x(1+\log\log x)^{k-1}}{\log x}.              \tag{7}
\]

For the residual primes, collisions in the product measure cost at most a
constant (depending on `k,M`) times `sum_{p in R_j}p^{-2}`, hence vanish by
(3).  The boundary `t_1+...+t_k=1` has zero limiting product measure: the
positive part of (5) is absolutely continuous, while all-zero tuples sum
to zero.  Hence weak convergence applies to the simplex
`t_1+...+t_k<=1`.

For the fixed primes, first truncate `F` at `B`, pass to the limit, and
then let `B` tend to infinity.  The omitted mixed terms are bounded by
`(sum_{p in F, p>B}1/p)M^{k-1}`.  Equivalently, the limiting fixed-`k`
moment is the convolution of the elementary symmetric sums of `(1/p)_{p
in F}` with the diffuse simplex integrals.  Summing the generating
function will therefore give the exact factor `V_F`.

There is no unbounded-order inclusion-exclusion problem.  Uniformly in
`j`,

\[
 \mathbb E\binom{\Omega_j}{k}
 \le e_k((1/p)_{p\in S_j})
 \le\frac{M^k}{k!}.                                      \tag{8}
\]

Thus, for `0<=z<=1`,

\[
 \mathbb E z^{\Omega_j}
 =\sum_{k\ge0}(z-1)^k\mathbb E\binom{\Omega_j}{k}         \tag{9}
\]

converges absolutely and uniformly.  We may pass to the limit term by
term.  Finally,

\[
 0\le \mathbb E z^{\Omega_j}-\Pr(\Omega_j=0)\le z,        \tag{10}
\]

so `z` may tend to zero uniformly in `j`.

Writing `q_b` for (12) with `a` replaced by `b`, the fixed-order moment
calculation gives the limiting probability generating function

\[
 \lim_{j\to\infty}\mathbb E z^{\Omega_j}
 =\prod_{p\in F}\left(1-\frac{1-z}{p}\right)
   e^{-(1-z)h}q_{(1-z)a}(1).
\]

Indeed, a fixed prime supplies its Bernoulli factor, repetitions of the
diffuse atom at zero exponentiate, and the positive logarithmic-scale part
is the simplex series.  It follows from (5)--(10) that

\[
 \frac{Q_{S_j}(x_j)}{x_j}
 \longrightarrow V_F e^{-h}q_a(1),                       \tag{11}
\]

where, extending `a` by zero beyond `1`,

\[
 q_a(r)=\sum_{k\ge0}\frac{(-1)^k}{k!}
 \int_{\substack{t_1+\cdots+t_k\le r\\t_i>0}}
 \prod_{i=1}^k a(t_i)\frac{dt_i}{t_i}.                   \tag{12}
\]

The series is absolutely and locally uniformly convergent.

## 4. Strict positivity of the generalized Dickman factor

Let `Q(s)` be the Laplace transform of `q_a`.  Termwise integration in
(12) gives

\[
 Q(s)=\frac1s\exp\left(-\int_0^1e^{-st}a(t)\frac{dt}{t}\right).
\]

Differentiation, followed by uniqueness of Laplace transforms, gives the
renewal equation

\[
 r q_a(r)=\int_0^r(1-a(u))q_a(r-u)\,du.                  \tag{13}
\]

Each simplex integral in (12) is continuous in `r`, and the series is
locally uniformly convergent, so `q_a` is continuous.  The right side of
(13) is continuous as well.  Hence the identity obtained initially almost
everywhere from Laplace-transform uniqueness holds at every `r`.

Also `q_a(r)` tends to `1` as `r` decreases to zero, because
`int_0^r a(t)dt/t` tends to zero.  In particular `q_a` is positive near
zero.  If `r_0` were its first zero, then (13) and positivity below `r_0`
would force

\[
 a(u)=1\quad\text{for almost every }0<u<r_0.
\]

This is impossible, since it would make `int_0^{r_0}a(u)du/u` infinite.
Therefore

\[
 q_a(r)>0\qquad(r>0).                                    \tag{14}
\]

Equations (2), (11), and (14) show that the limit in (11) is strictly
positive, contradicting (1).  This proves the statement.

## Remarks

1. The argument is compactness-based, so it yields no explicit numerical
   `c(M)`.  A quantitative Hildebrand/Wirsing lower-mean theorem supplies
   one, but is not needed for existence.
2. For the bang-bang profile `a(t)=1_{alpha<t<=1}`, one has
   `int a(t)dt/t=log(1/alpha)` and `q_a(1)=rho(1/alpha)`, the Dickman
   function.  This explains why any explicit uniform constant is naturally
   extremely small when `M` is large.
3. Fixed small primes contribute `prod(1-1/p)`, not `exp(-sum1/p)`.
   Only escaping primes whose individual reciprocal weights vanish produce
   the Poisson factor `e^{-h}`.
