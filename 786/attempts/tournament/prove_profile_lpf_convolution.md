# Proof of the local prime-convolution input in Lemma 3

## Verdict

The local estimate (20), and the passage from (20) to (25), are valid in
the parameter regime in which Lemma 3 uses them.  The precise uniformity
is as follows.

* The exponent interval \(I=(N^a,N^{2a}]\) has fixed \(a>0\) while
  \(N\to\infty\).
* A local exponent window has length \(h/\log N\), where \(h>0\) is
  fixed.  More generally, \(h\) may range in a fixed compact subinterval
  of \((0,\infty)\).
* All constants in the lower and upper estimates below are absolute when
  the locations are fixed multiples of \(a\).  The threshold from which
  the estimates hold may depend on \(a\) and \(h\).
* In the application, \(a\) belongs to a finite set depending only on the
  fixed reciprocal budget \(K_1\), and only finitely many fixed window
  widths are used.  Taking the maximum of the corresponding thresholds
  gives exactly the required uniformity in the moving deleted-prime set
  and in \(N\).

Thus there is no need for a short-interval PNT.  An interval of exponent
length \(h/\log N\) is the fixed-ratio interval \((x,e^h x]\), and the
ordinary PNT suffices.  What would *not* follow from this argument is a
version with \(a=a_N\to0\), or \(h=h_N\to0\), without quantitative lower
bounds on \(N^{a_N}\) and on the PNT error.  Lemma 3 makes neither such
claim.

## 1. The fixed-ratio reciprocal-prime estimate

Write \(L=\log N\).  We use the following direct consequence of the PNT.

### Lemma 1

Fix

\[
 0<\alpha<\beta<\infty,
 \qquad 0<h_-\leq h_+<\infty.
\]

Uniformly for \(y\in[\alpha,\beta]\) and \(h\in[h_-,h_+]\),

\[
 \sum_{N^y<p\leq N^{y+h/L}}\frac1p
   =\frac{h}{yL}(1+o(1)).                                      \tag{1}
\]

The \(o(1)\) depends only on the four displayed fixed parameters.

#### Proof

Put \(x=N^y\), so that \(N^{y+h/L}=e^h x\).  Partial summation gives

\[
 \sum_{x<p\leq e^h x}\frac1p
 =\frac{\pi(e^h x)}{e^h x}-\frac{\pi(x)}x
   +\int_x^{e^h x}\frac{\pi(t)}{t^2}\,dt.                    \tag{2}
\]

The ordinary PNT is uniform here: since every \(t\geq N^\alpha\),

\[
 \pi(t)=\frac{t}{\log t}(1+o(1))                              \tag{3}
\]

uniformly over all the variables in (2).  For a fixed compact range of
\(h\), substitution in (2) gives

\[
 \begin{aligned}
 \sum_{x<p\leq e^h x}\frac1p
 &=\frac1{\log(e^h x)}-\frac1{\log x}
   +\int_x^{e^h x}\frac{dt}{t\log t}
   +o\!\left(\frac1{\log x}\right)\\
 &=\log\!\left(\frac{\log x+h}{\log x}\right)
   +O\!\left(\frac{h}{(\log x)^2}\right)
   +o\!\left(\frac1{\log x}\right)\\
 &=\frac{h}{\log x}(1+o(1)).
 \end{aligned}                                                \tag{4}
\]

For complete precision concerning the last relative error, first fix
\(h_->0\), and then take the relative PNT error in (3) smaller than a
sufficiently small multiple of \(h_-\).  Since \(\log x=yL\), (4) is
(1).  \(\square\)

The same argument gives the following useful one-sided form.  If an
exponent interval \(V\) of length at most \(h/L\) meets
\([a,2a]\), with fixed \(a,h>0\), then for all sufficiently large \(N\),

\[
 \sum_{\substack{p\in(N^a,N^{2a}]\\ \log p/L\in V}}\frac1p
 \leq C\frac{h}{aL},                                         \tag{5}
\]

where \(C\) is absolute.  Indeed, the intersection can be enlarged to an
exponent interval of length \(h/L\) with lower endpoint at least \(a/2\),
and Lemma 1 applies.  Notice that the bound is linear in the prescribed
fixed width \(h\).

## 2. The two-prime local convolution

Fix \(0<a\leq 10^{-2}\), put

\[
 I=(N^a,N^{2a}],\qquad
 \mu=\sum_{p\in I}\frac1p\,\delta_{\log p/L},                 \tag{6}
\]

and let \(W=[s,s+h/L]\) be an exponent interval with

\[
 [s,s+h/L]\subset[2.9a,3.1a].                                \tag{7}
\]

Here \(h>0\) is fixed.  Then, for all sufficiently large \(N\),

\[
 c\frac{|W|}{a}\leq(\mu*\mu)(W),                             \tag{8}
\]

and, for every real \(x\),

\[
 \mu(W-x)\leq C\frac{|W|}{a}.                                \tag{9}
\]

The positive constants \(c,C\) can be chosen absolute.  The threshold
may depend on \(a,h\).  The same constants work for \(h\) in any fixed
compact subset of \((0,\infty)\).

To prove (8), restrict the first prime to

\[
 N^{5a/4}<p\leq N^{7a/4}.                                    \tag{10}
\]

If \(t=\log p/L\) lies in this interval, (7) implies

\[
 1.15a\leq s-t\leq1.85a.
\]

For sufficiently large \(N\), the full exponent interval
\([s-t,s-t+h/L]\) is contained in \([a,2a]\).  Lemma 1, uniformly in
\(t\), therefore gives

\[
 \sum_{\substack{q\in I\\s-t\leq\log q/L\leq s-t+h/L}}
       \frac1q
 \geq c_1\frac{h}{aL}.                                      \tag{11}
\]

A second application of the PNT (or Lemma 1 with a fixed exponent-ratio
interval) gives

\[
 \sum_{N^{5a/4}<p\leq N^{7a/4}}\frac1p
   =\log(7/5)+o(1)\geq c_2.                                 \tag{12}
\]

Summing (11) with weights \(1/p\) proves

\[
 (\mu*\mu)(W)\geq c_1c_2\frac{h}{aL}
   =c_1c_2\frac{|W|}{a}.                                   \tag{13}
\]

For (9), \(W-x\) is an exponent interval of length \(h/L\).  If it does
not meet \([a,2a]\), its \(\mu\)-mass is zero; otherwise (5) proves (9).
This establishes the precise version of (20).

## 3. Robustness under reciprocal-mass deletion

Let \(\nu\leq\mu\) be any positive atomic submeasure with
\(\|\nu\|\leq\varepsilon\), and put \(\mu^0=\mu-\nu\).  No regularity of
the support of \(\nu\) is assumed.  Positivity and commutativity give

\[
 \begin{aligned}
 \mu^{*2}-(\mu^0)^{*2}
 &=\nu*\mu+\mu^0*\nu,\\
 \bigl(\mu^{*2}-(\mu^0)^{*2}\bigr)(W)
 &\leq2\|\nu\|\sup_x\mu(W-x).
 \end{aligned}                                               \tag{14}
\]

Combining (8), (9), and (14),

\[
 (\mu^0)^{*2}(W)
 \geq(c-2C\varepsilon)\frac{|W|}{a}.                        \tag{15}
\]

Consequently the absolute choice

\[
 \varepsilon_0=\frac{c}{4C}                                 \tag{16}
\]

ensures

\[
 (\mu^0)^{*2}(W)\geq\frac c2\frac{|W|}{a}                  \tag{17}
\]

for every local window in (7).  This proves (21)--(22), uniformly in the
identity and location of all deleted primes.  In particular, the deleted
set may vary arbitrarily with \(N\).

There is a small order-of-quantifiers point worth recording.  Formula
(16) can be chosen before the reciprocal-budget pigeonhole step.  Once
\(K_1\) is fixed, that step produces a finite menu of values of \(a\).
After the menu is known, one chooses a common sufficiently large \(N_0\)
for (17).  This is all that the contradiction for a fixed \(K_1\) needs.

## 4. From two-prime windows to an \(r\)-prime target window

We include a detailed replacement for the cell-count sentence leading to
(25).  This avoids any implicit appeal to a local limit theorem.

Put

\[
 J=[(3-1/20)a,(3+1/20)a],\qquad \lambda=(\mu^0)^{*2}.          \tag{18}
\]

Choose a positive integer \(k\) for which a compact interval
\(S\) is contained in the interior of \(kJ\).  In the application,
\(k\) is the integer nearest to \(1/(3a)\), \(a\) is chosen sufficiently
small, and one takes

\[
 S=[1-\delta,1]\Subset kJ                                  \tag{19}
\]

for some fixed \(\delta>0\).  Let \(H>0\) be fixed.  We claim that

\[
 \lambda^{*k}([s-H/L,s])\geq\frac{c_{a,k,H,S}}{L}
 \qquad(s\in S)                                             \tag{20}
\]

for all sufficiently large \(N\).

Choose a fixed

\[
 0<\eta<\frac{H}{10(k+1)}.                                  \tag{21}
\]

Applying (17) to every interval \(C\subset J\) of length
\(\eta/L\) gives

\[
 \lambda(C)\geq \frac{c\eta}{2aL}=:\frac{b}{L}.             \tag{22}
\]

Partition \(J\), apart from two end pieces, into half-open cells of length
\(\eta/L\).  Since \(S\Subset kJ\), the \((k-1)\)-dimensional sections

\[
 \left\{(x_1,\ldots,x_{k-1})\in J^{k-1}:
 s-\sum_{i<k}x_i\in J\right\}                               \tag{23}
\]

have volume bounded below uniformly for \(s\in S\).  This can be seen
directly by shrinking \(J\) slightly and using compactness, or from the
strict positivity on the interior of the \(k\)-fold convolution of the
indicator of \(J\).  Hence, for every \(s\in S\), there are at least

\[
 c_{J,k,S}L^{k-1}                                           \tag{24}
\]

ordered choices of the first \(k-1\) cells such that the cell nearest to
the residual target also lies inside \(J\), with a fixed margin from its
endpoints.

For each such choice, select the residual \(k\)-th cell so that the sum
of the \(k\) cell centers differs from \(s-H/(2L)\) by at most
\(\eta/(2L)\).  By (21), the Minkowski sum of these \(k\) cells is
contained in \([s-H/L,s]\).  The corresponding boxes in \(J^k\) are
pairwise disjoint because the first \(k-1\) cells identify the box.
Using (22) in each coordinate and then (24),

\[
 \begin{aligned}
 \lambda^{*k}([s-H/L,s])
 &\geq c_{J,k,S}L^{k-1}\left(\frac bL\right)^k\\
 &=\frac{c_{J,k,S}b^k}{L},
 \end{aligned}                                               \tag{25}
\]

which proves (20).  Taking \(H=\log2\), \(r=2k\), and using
\(\lambda^{*k}=(\mu^0)^{*r}\) is exactly (25) of
profile_lpf_charge.md.

## 5. Repeated primes and the finite-menu uniformity

For completeness, the reciprocal mass in \((\mu^0)^{*r}\) of tuples with
some repeated prime is at most

\[
 \binom r2
 \left(\sum_{q>N^a}\frac1{q^2}\right)
 \left(\sum_{p\in I}\frac1p\right)^{r-2}
 =O_{a,r}(N^{-a}).                                          \tag{26}
\]

This is \(o(1/L)\), so removing repeated-prime tuples from (25) only
changes its constant.  The estimate is uniform over the deleted set
because replacing \(\mu^0\) by \(\mu\) only increases the right-hand side
of the upper bound.

Finally, in the reciprocal-budget pigeonhole argument one fixes

\[
 H_0=\left\lfloor K_1/\varepsilon_0\right\rfloor+2
\]

and examines \(H_0\) disjoint intervals
\((N^{2^{-i-1}},N^{2^{-i}}]\), beginning at a sufficiently large fixed
index.  At least one has deleted reciprocal mass at most
\(\varepsilon_0\).  The resulting set of possible exponents \(a\), and
hence the possible \(k,r,\eta\), is finite and depends only on \(K_1\).
All thresholds in Lemmas 1--4 can therefore be maximized over this finite
set.  The constants in (25)--(26) may depend on \(K_1\), as Lemma 3
explicitly permits, while the estimates remain uniform in \(N\) and in
the moving set of retained primes.

This closes the analytic dependency in Lemma 3 under the stated
PNT/Mertens inputs.
