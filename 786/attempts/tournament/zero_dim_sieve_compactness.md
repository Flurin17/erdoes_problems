# A compactness proof of the bounded-product sieve lemma

This note proves the qualitative quantitative statement needed for the
zero-kernel route.  It uses only Mertens' prime reciprocal theorem and a
compactness argument; in particular, it does not import a uniform
Hildebrand--Wirsing lower-mean theorem.

## Theorem

For every \(K<\infty\) there is a constant \(c_K>0\) such that, for every
real \(x\geq 1\) and every finite set \({\cal P}\) of primes satisfying
\[
 \prod_{p\in{\cal P}}\left(1-\frac1p\right)^{-1}\leq K,
\]
one has
\[
 \#\{n\leq x:p\nmid n\text{ for every }p\in{\cal P}\}\geq c_Kx. \tag{1}
\]

The proof gives existence, but not a useful closed formula, for \(c_K\).

## 1. Absolute inclusion--exclusion

Primes larger than \(x\) may be discarded.  Put
\[
 H({\cal P})=\sum_{p\in{\cal P}}\frac1p.
\]
The product hypothesis gives
\[
 H({\cal P})\leq \log K=:L.                              \tag{2}
\]
If \(n\) is uniform on \([1,x]\), let
\[
 \Omega_{\cal P}(n)=\#\{p\in{\cal P}:p\mid n\}.
\]
For every \(j\geq0\),
\[
 \begin{aligned}
 \mathbb E{\Omega_{\cal P}\choose j}
 &=\sum_{p_1<\cdots<p_j\atop p_i\in{\cal P}}
   \frac{\lfloor x/(p_1\cdots p_j)\rfloor}{x}\\
 &\leq \sum_{p_1<\cdots<p_j\atop p_i\in{\cal P}}
       \frac1{p_1\cdots p_j}
 \leq \frac{L^j}{j!}.                                  \tag{3}
 \end{aligned}
\]
Consequently inclusion--exclusion is absolutely summable in expectation:
\[
 \mathbb P(\Omega_{\cal P}=0)
 =\sum_{j\geq0}(-1)^j\mathbb E{\Omega_{\cal P}\choose j},
 \qquad
 \sum_{j\geq0}\left|\mathbb E{\Omega_{\cal P}\choose j}\right|
 \leq e^L.                                               \tag{4}
\]
This uniform factorial tail is what permits the compactness argument below.

## 2. The only possible scaling limits

Suppose (1) is false.  There are \(x_m\to\infty\) and prime sets
\({\cal P}_m\subseteq[2,x_m]\) satisfying (2) for which the left side of
(1), divided by \(x_m\), tends to zero.  The assertion \(x_m\to\infty\)
causes no loss, since the sifted set always contains \(1\).

Pass to a diagonal subsequence on which membership of every fixed prime
stabilizes.  The primes which remain fixed contribute the positive factor
\[
 V_0=\prod_{p\text{ eventually present}}\left(1-\frac1p\right)>0. \tag{5}
\]
After those coordinates are separated, the minimum of every remaining
moving prime set tends to infinity.  Introduce its harmonic scaling measure
\[
 \mu_m=\sum_{p\text{ moving}}\frac1p\,
       \delta_{\log p/\log x_m}
\]
on \([0,1]\).  Its mass is at most \(L\), so a further subsequence converges
weakly.  Mertens' theorem, in the form
\[
 \sum_{x^\alpha<p\leq x^\beta}\frac1p
 \longrightarrow \log(\beta/\alpha)
 \quad(0<\alpha<\beta\leq1),                            \tag{6}
\]
shows that the limit has the form
\[
 \mu=h\delta_0+a(u)\frac{du}{u},
 \qquad h\geq0,\quad 0\leq a(u)\leq1,\quad
 h+\int_0^1a(u)\frac{du}{u}\leq L.                     \tag{7}
\]
Here \(h\) records harmonic mass which escapes to logarithmic scale zero.

For fixed \(j\), the factorial moment in (3) now converges to the sum of
the corresponding fixed-prime contribution and
\[
 \frac1{j!}\int_{u_1+\cdots+u_j\leq1}
       \mu(du_1)\cdots\mu(du_j),                         \tag{8}
\]
with the usual removal of diagonals already represented by the fixed-prime
coordinates.  For completeness, the floor in (3) causes no hidden boundary
term.  On \(u_1+\cdots+u_j\leq1-\varepsilon\), the product is at most
\(x_m^{1-\varepsilon}\), and the total floor error is at most
\(x_m^{-\varepsilon}\), since distinct prime tuples give distinct products.
The complementary boundary strip is bounded by the \(j\)-fold harmonic
product measure.  Its limiting mass tends to zero with \(\varepsilon\),
because the positive-scale part in (7) is absolutely continuous and hence
the hyperplane \(u_1+\cdots+u_j=1\) has measure zero.  Products with scaled
sum greater than one contribute zero on both sides.

The uniform bound (3) allows the limit to pass through the whole series
(4).  Thus the alleged limiting sifted density is
\[
 V_0e^{-h}q_a(1),                                       \tag{9}
\]
where
\[
 q_a(r)=\sum_{j\geq0}\frac{(-1)^j}{j!}
 \int_{u_1+\cdots+u_j\leq r}
 \prod_{i=1}^j a(u_i)\frac{du_i}{u_i}.                  \tag{10}
\]
The series is absolutely and locally uniformly convergent because
\(\int_0^1a(u)\,du/u\leq L\).  The factor \(e^{-h}\) in (9) is the
convolution-exponential contribution of the atom at zero.  The exact
Euler factors of genuinely fixed primes are kept in \(V_0\), rather than
being incorrectly replaced by \(e^{-\sum1/p}\).

## 3. The generalized Dickman factor is strictly positive

Extend \(a\) by zero on \((1,\infty)\).  The Laplace transform of (10) is
\[
 \widehat q_a(s)=\int_0^\infty e^{-sr}q_a(r)\,dr
 =\frac1s\exp\left\{-\int_0^1e^{-su}a(u)\frac{du}{u}\right\}. \tag{11}
\]
Differentiating (11) and inverting the Laplace transform gives the renewal
equation
\[
 r q_a(r)=\int_0^r(1-a(u))q_a(r-u)\,du.                 \tag{12}
\]
Moreover \(q_a(r)\to1\) as \(r\downarrow0\).  Equation (12) forces
\[
 q_a(r)>0\qquad(r>0).                                   \tag{13}
\]
Indeed, if \(r_0\) were its first zero, then \(q_a(r_0-u)>0\) for
\(0<u<r_0\).  The nonnegative right side of (12) could vanish only if
\(a(u)=1\) almost everywhere on \((0,r_0)\), contradicting
\(\int_0^{r_0}a(u)\,du/u<\infty\).  The same first-zero argument also shows
directly that the solution cannot cross below zero.

Every factor in (9) is therefore strictly positive, contradicting the
assumed convergence of the sifted density to zero.  This proves (1).

## Remarks on rigor and quantitative content

1. The diagonal separation of fixed primes can be written as two nested
   limits: first retain primes at most \(B\), then let \(m\to\infty\), and
   finally let \(B\to\infty\).  Absolute bound (3) makes these passages
   uniform.  It also shows that an infinite stabilized set has the positive
   convergent Euler product in (5).
2. The contradiction proof is uniform in moving prime sets and hence really
   produces a constant \(c_K>0\); it is not merely a result for one fixed
   set of primes.
3. No explicit formula for \(c_K\) is extracted.  A plausible extremal
   profile is \(a=\mathbf1_{(1/K,1]}\), whose factor is a Dickman value, but
   proving that rearrangement statement is a separate and stronger claim.
