# Uniform finite gap via lattice concentration

## Status

This gives a complete constant-gap argument under two explicitly stated
standard finite theorems. Their exact formulations are recalled from
standard mathematical memory (no external lookup). The lattice reduction
has been independently checked; the lower-mean statement should receive the
same statement audit before promotion to PROOF.md.

## Standard inputs

**A. Halasz--Ruzsa exact-lattice concentration.** There is an absolute
constant \(C\) such that every integer-valued additive \(F\) satisfies

\[
 \max_{a\in\mathbb Z}\frac1x|\{n\le x:F(n)=a\}|
 \le \frac{C}{\sqrt{1+H_F(x)}},\qquad
 H_F(x)=\sum_{\substack{p\le x\\F(p)\ne0}}\frac1p.       \tag{A}
\]

This is finite and uniform, so \(F\) may depend on \(x\). It is the lattice
point-atom theorem, not a fixed-width real concentration assertion.

One recovers (A) from the standard interval theorem. In the normalization

\[
 Q_h(F;x)\ll(1+E_h)^{-1/2},\quad
 E_h=\inf_\tau\left\{(\tau/h)^2+
 \sum_{p\le x}\frac1p\min\left(1,
 \frac{|F(p)-\tau\log p|^2}{h^2}\right)\right\},          \tag{A'}
\]

take \(F\) integer-valued and
\[
 h<\min\left(\frac14,\frac1{4\sqrt{H_F(x)}\log x}\right).
\]
If \(|\tau|/h\ge\sqrt H/2\), the first term is at least \(H/4\).
Otherwise \(|\tau|\log p\le1/8\), so every nonzero integer \(F(p)\)
contributes one to the prime sum. Thus \(E_h\gg H\), and an interval of
width \(h<1\) isolates a single integer value.

**B. Finite Hildebrand--Wirsing lower mean.** For every fixed
\(0<\kappa<1\), there are \(c_\kappa>0\) and \(x_0(\kappa)\) such that,
for \(x\ge x_0(\kappa)\), every multiplicative \(g:\mathbb N\to[0,1]\)
satisfying

\[
 \sum_{p\le x}\frac{g(p)\log p}{p}\ge\kappa\log x        \tag{B1}
\]

obeys

\[
 \frac1x\sum_{n\le x}g(n)
 \ge c_\kappa
 \prod_{p\le x}\left[
 \left(1-\frac1p\right)
 \left(\sum_{\nu\ge0}\frac{g(p^\nu)}{p^\nu}\right)\right].\tag{B2}
\]

Equivalently, (B1) may be written
\[
 \sum_{p\le x}\frac{(1-g(p))\log p}{p}
 \le (1-\kappa)\log x+O(1).
\]
This is the standard endpoint lower-mean form; only qualitative uniformity
is used. The local prime-power factors are bounded in the application.

## Bounded harmonic sieving

**Lemma.** For every fixed \(M\) there is \(d_M>0\) such that, uniformly
over sets \(S\) of primes at most \(x\) with
\[
 \sum_{p\in S}\frac1p\le M,
\]
one has
\[
 |\{n\le x:p\nmid n\text{ for all }p\in S\}|\ge d_Mx.    \tag{1}
\]

**Proof from B.** Let \(g\) be the indicator of being \(S\)-free and put
\[
 \eta=e^{-(M+3)}.
\]
Prime-reciprocal Mertens gives
\[
 \sum_{x^\eta<p\le x}\frac1p=M+3+o(1).
\]
Since \(S\) uses at most \(M\) reciprocal mass globally, allowed primes
in this interval have reciprocal mass at least one for all large \(x\).
Since \(\log p\ge\eta\log x\) there,
\[
 \sum_{p\le x}\frac{g(p)\log p}{p}\ge\eta\log x.          \tag{2}
\]
Thus (B1) holds, say with \(\kappa=\eta/2\).

For this strongly multiplicative \(g\), the Euler product in (B2) is
exactly
\[
 \begin{aligned}
 &\prod_{p\le x}\left[
 \left(1-\frac1p\right)
 \left(\sum_{\nu\ge0}\frac{g(p^\nu)}{p^\nu}\right)\right]\\
 &\hspace{2cm}=\prod_{p\in S}\left(1-\frac1p\right)
 \ge \exp\left(-2\sum_{p\in S}\frac1p\right)
 \ge e^{-2M}.                                          \tag{3}
 \end{aligned}
\]
Here \(-\log(1-1/p)\le2/p\) for every prime \(p\). Equation (B2)
proves (1) for large \(x\); decrease \(d_M\) to absorb the finite initial
range. \(\square\)

This lemma is boundary-sensitive. For \(S=\{p>x^{1/u}\}\), the left side
is asymptotic to \(\rho(u)x\), much smaller than the naive independent-prime
prediction for large \(u\). The finite lower-mean theorem, not an Euler
product approximation, handles this example.

## Constant-gap theorem

**Theorem.** There is an absolute \(d>0\) such that every rational
completely additive \(f\), every nonzero rational \(t\), and every
\(N\ge2\) satisfy

\[
 |\{n\le N:f(n)=t\}|\le(1-d)N.                           \tag{4}
\]

**Proof.** Clear the finitely many denominators of \(f(p)\), \(p\le N\),
and of \(t\). This gives an integer completely additive \(F\) and nonzero
integer target \(a\) with identical fibres on \([1,N]\). Let

\[
 H=\sum_{\substack{p\le N\\F(p)\ne0}}\frac1p,
 \qquad M=\max(1,4C^2).
\]

If \(H\ge M\), (A) bounds the fibre by \(N/2\). If \(H<M\), take
\[
 S=\{p\le N:F(p)\ne0\}.
\]
Every \(S\)-free integer has \(F(n)=0\ne a\), so the complement of the
target fibre has at least \(d_MN\) elements by (1). Taking
\(d=\min(1/2,d_M)\), and decreasing it for the finite initial range if
necessary, proves (4). \(\square\)

By the grading theorem, every repetition-allowed finite PLR set is contained
in such a nonzero fibre. Thus (4) rules out finite density \(1-o(1)\) with
an absolute gap. It does not identify the optimal gap or prove the known
\(0.828499\ldots\) threshold construction extremal.
