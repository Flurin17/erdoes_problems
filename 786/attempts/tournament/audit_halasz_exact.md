# Audit: exact-atom Halasz--Ruzsa concentration

## Verdict

The following is a valid standard theorem. There is an absolute constant
\(C\) such that, for every \(x\geq 3\) and every real additive arithmetic
function \(f\),

\[
 Q_x(f):={1\over x}\sup_{a\in\mathbb R}
       \#\{n\leq x:f(n)=a\}
 \leq {C\over\sqrt{1+E_x(f)}},                 \tag{1}
\]

where

\[
 E_x(f):=\sum_{\substack{p\leq x\\f(p)\ne0}}{1\over p}.    \tag{2}
\]

This is usually called the Halasz concentration theorem or the
Halasz--Ruzsa exact concentration inequality. Here additive may have the
usual coprime-additive meaning; in particular, (1) applies to completely
additive and strongly additive functions. Some standard formulations
replace \(1/p\) by \((1-1/p)/p\), or change the fixed 1 in the
denominator. These versions are equivalent up to an absolute constant.

The quantifiers are finite and uniform: the constant is independent of
\(x\), of the range of \(f\), and of its values. Thus \(f=f_x\) may move
with \(x\). This really is an exact-atom assertion; it requires no lower
bound on the spacing of the nonzero \(f(p)\).

What (1) does **not** imply is

\[
 Q_x(f)=1-o(1)\quad\Longrightarrow\quad E_x(f)=o(1).        \tag{3}
\]

It gives only \(E_x(f)=O(1)\). A leading-one inequality, a tensorized
product-box version, or (3) itself is a stronger lemma and must not be
silently attached to the standard theorem.

## Reconstruction from the interval theorem

The logarithmic-drift term in the standard interval theorem is
essential. In a convenient normalization, put

\[
 Q_x(F;h)={1\over x}\sup_y
  \#\{n\le x:y\le F(n)<y+h\}.
\]

The Halasz--Ruzsa interval theorem gives

\[
 Q_x(F;h)\ll (1+\mathcal E_h(F;x))^{-1/2},                 \tag{4}
\]

where, up to harmless absolute changes in normalization,

\[
 \mathcal E_h(F;x)=\inf_{\tau\in\mathbb R}
 \left\{
  \left({\tau\over h}\right)^2+
  \sum_{p\le x}{1\over p}
   \min\left(1,
    \left|{F(p)-\tau\log p\over h}\right|^2
       \right)
 \right\}.                                                  \tag{5}
\]

This is a uniform finite-\(x\) theorem for general additive functions.
Versions with a harmless extra \(O(1/\log x)\) term give the same
corollary below.

Suppose first that \(F\) is integer valued and write \(H=E_x(F)\). The
case \(H<1\) is absorbed by the 1 in (1). For \(H\ge1\), choose

\[
 0<h<\min\left\{{1\over4},
                  {1\over4\sqrt H\log x}\right\}.           \tag{6}
\]

For any \(\tau\), either \(|\tau|/h\ge\sqrt H/2\), in which case the
first term of (5) is at least \(H/4\), or

\[
 |\tau|\log p<h\sqrt H\log x/2<1/8
 \quad(p\le x).
\]

In the second case, every prime with \(F(p)\ne0\) has
\(|F(p)-\tau\log p|>3/4>h\), so its summand in (5) is 1. Consequently

\[
 \mathcal E_h(F;x)\ge H/4.                                  \tag{7}
\]

An interval of length \(h<1\) contains at most one integer value of
\(F\). Equations (4) and (7) prove (1) for integer-valued \(F\).

This also explains exactly why the exceptional \(\tau\log p\) direction
does not invalidate the lattice exact-point theorem: if the drift is
large, the first term of (5) pays for it; if it is small, integrality
forces every active prime to contribute fully.

## Reduction of arbitrary real exact fibers to the lattice case

For fixed \(x\), let \(V\) be the finite-dimensional
\(\mathbb Q\)-vector space spanned by the finitely many values
\(f(p^j)\) with \(p^j\le x\). Consider the finite set of nonzero vectors

\[
 \{f(p):p\le x,\ f(p)\ne0\}
 \cup
 \{f(m)-f(n):m,n\le x,\ f(m)\ne f(n)\}.                    \tag{8}
\]

Choose a rational linear functional \(L:V\to\mathbb Q\) outside the
finite union of their annihilating hyperplanes, and clear a common
denominator. Then \(F=L\circ f\) is integer valued on \([1,x]\), may be
extended additively to all integers, and satisfies

\[
 F(m)=F(n)\iff f(m)=f(n),\qquad
 F(p)\ne0\iff f(p)\ne0                                    \tag{9}
\]

for all relevant \(m,n,p\). Applying the integer theorem to \(F\)
proves the real theorem with exactly the same active-prime sum. This
finite generic-projection argument is also a safeguard against an
incorrect minimum-spacing assumption.

Alternatively, one can apply (4) directly and take \(h\) smaller than
all finitely many relevant nonzero gaps and active prime values.

## Prime powers and the archimedean trap

The theorem permits arbitrary values on higher prime powers. In the
analytic proof, their total reciprocal weight is bounded:

\[
 \sum_p\sum_{j\ge2}{1\over p^j}=O(1),
\]

so they affect only the absolute constant. There is therefore no
missing hypothesis of strong additivity. Complete and strong
additivity, the two cases used in Problem 786, are certainly covered.

It would be wrong to delete the first term in (5), or to use a
pointwise Halasz distance without retaining its archimedean decay. If
\(F(p)\) follows a large multiple of \(\log p\), the prime-distance part
can be small for a range of Fourier frequencies. The proof of (4)
controls this through the twist parameter and the decay/spacing of

\[
 {1\over x}\sum_{n\le x}n^{i\tau}
 \asymp {x^{i\tau}\over1+i\tau}.
\]

For positive-width interval concentration the logarithmic direction is
a genuine exception. For example, \(f(n)=\log n\) has positive
concentration in a fixed-width interval even though each exact fiber is
a singleton. This example does not contradict (1).

As sanity checks, \(f(p)=1\) gives the modal order
\(x/\sqrt{\log\log x}\) for \(\Omega(n)\), showing that the exponent
\(1/2\) is sharp, while \(f(p)=\log p\) gives singleton exact fibers.

## The proposed mean-spectrum shortcut

There is no universal \(\delta>-1\) for which

\[
 \Re {1\over x}\sum_{n\le x}g(n)\ge\delta+o(1)              \tag{10}
\]

holds uniformly for moving **complex** completely multiplicative
functions \(|g|=1\). Put

\[
 g_x(n)=n^{i\pi/\log x}
       =\exp\!\left(\pi i{\log n\over\log x}\right).
\]

Euler summation gives

\[
 {1\over x}\sum_{n\le x}g_x(n)
 ={x^{i\pi/\log x}\over1+i\pi/\log x}+o(1)
 \longrightarrow -1.                                      \tag{11}
\]

Thus applying a real Hall spectrum constant directly to
\(g=e^{\pi i f}\) is invalid for general real \(f\). This is the same
moving archimedean obstruction visible in (5).

The constant \(-0.656999\ldots\) belongs instead to the spectrum theorem
for real-valued multiplicative functions (in particular
\(g\in\{-1,1\}\)). In its usual form the lower endpoint is

\[
 \delta_1=1-2\log(1+\sqrt e)
     +4\int_1^{\sqrt e}{\log t\over t+1}\,dt
     =-0.656999\ldots .                                    \tag{12}
\]

It is a lower bound on real mean values, not the exact-atom theorem and
not a leading-one upper stability estimate. A rational finite grading
can be cleared to integer coefficients, making \((-1)^{F(n)}\) real,
but every further parity-stability assertion still needs a separate
argument.

In the present project that separate Hall input is unnecessary once the
bounded-harmonic-mass prime-avoidance lemma is available. If
\(Q\) is a set of primes with \(\sum_{p\in Q}1/p\le M\), and every
\(Q\)-free set in \([1,Y]\) has size at least \(c(M)Y\), then the
disjoint sets

\[
 \{pb:b\le x/p,\ b\text{ is }Q\text{-free}\},\qquad p\in Q,
\]

consist of integers having exactly one \(Q\)-prime to exponent 1. Since
\(\lfloor x/p\rfloor\ge x/(2p)\), their union has density at least

\[
 {c(M)\over2}\sum_{p\in Q}{1\over p}.                      \tag{13}
\]

Thus odd-parity density tending to zero forces the harmonic mass to
zero without any unverified complex mean-spectrum shortcut.

## Safe dependency statement

The following may safely be quoted in the main proof:

> **Halasz--Ruzsa exact concentration theorem.** There is an absolute
> \(C\) such that for every \(x\ge3\), every real additive arithmetic
> function \(f\), and every \(a\in\mathbb R\),
> \[
> \#\{n\le x:f(n)=a\}
> \le Cx\left(1+
> \sum_{\substack{p\le x\\f(p)\ne0}}{1\over p}
> \right)^{-1/2}.
> \]

It is unsafe to append a leading constant 1, conclusion (3), or a
tensor/product-box extension unless that stronger statement is proved
separately.
