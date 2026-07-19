# Uniform exact-atom decay is false

## Question tested

Let
\[
 f_N(n)=\sum_{p\leq N}w_{p,N}v_p(n)
\]
with arbitrary real (even rational) weights.  The proposed uniform
anti-concentration statement was
\[
 \sup_{t\ne0}\frac1N\#\{n\leq N:f_N(n)=t\}=o(1). \tag{1}
\]
Statement (1) is false, both for fixed weights and for a support which
escapes to infinity with \(N\).

## Counterexample 1: a fixed prime

Take \(w_{2,N}=1\) and \(w_{p,N}=0\) for every odd prime.  Then
\(f_N(n)=v_2(n)\), and hence
\[
 \#\{n\leq N:f_N(n)=1\}
 =\left\lfloor\frac N2\right\rfloor
  -\left\lfloor\frac N4\right\rfloor
 =\frac N4+O(1). \tag{2}
\]
Thus even a stationary rational grading has a macroscopic nonzero atom.
Its limiting characteristic function is
\[
 \frac1N\sum_{n\leq N}e^{i\theta f_N(n)}
 \longrightarrow
 \sum_{k\geq0}2^{-k-1}e^{ik\theta}
 =\frac1{2-e^{i\theta}}, \tag{3}
\]
whose Fourier coefficient at level one is \(1/4\).

## Counterexample 2: escaping support and the boundary obstruction

Let
\[
 {\cal P}_N=\{p:\sqrt N<p\leq N\},\qquad
 w_{p,N}={\bf1}_{p\in{\cal P}_N}.
\]
For \(n\leq N\), no two primes in \({\cal P}_N\) can divide \(n\), and
none can divide it to exponent two.  Consequently \(f_N(n)\in\{0,1\}\).
Moreover the sets of multiples of the primes in \({\cal P}_N\) are
pairwise disjoint, so
\[
 \begin{aligned}
 \frac1N\#\{n\leq N:f_N(n)=1\}
 &=\frac1N\sum_{\sqrt N<p\leq N}\left\lfloor\frac Np\right\rfloor\\
 &=\sum_{\sqrt N<p\leq N}\frac1p
   +O\left(\frac{\pi(N)}N\right)\\
 &=\log2+o(1). \tag{4}
 \end{aligned}
\]
The last line is prime-reciprocal Mertens (and the elementary bound
\(\pi(N)\ll N/\log N\)).  More generally, replacing \(\sqrt N\) by
\(N^{1/u}\), for fixed \(1<u\leq2\), gives a level-one proportion
\(\log u+o(1)\).

Writing \(\lambda_N\) for the left side of (4), the empirical
characteristic function is exactly
\[
 \phi_N(\theta)=1+\lambda_N(e^{i\theta}-1), \tag{5}
\]
and therefore tends to the characteristic function of a
\(\operatorname{Bernoulli}(\log2)\) variable.  Fourier inversion cannot
give uniform atom decay because the limiting distribution itself has a
level-one atom of mass \(\log2\).

This example also pinpoints the failure of an independent-geometric prime
model.  That model has characteristic function
\[
 \psi_N(\theta)=
 \prod_{p\in{\cal P}_N}
 \frac{1-1/p}{1-e^{i\theta}/p}.
\]
Since \(\sum_{p\in{\cal P}_N}p^{-1}\to\lambda=\log2\) and
\(\sum_{p\in{\cal P}_N}p^{-2}=o(1)\),
\[
 \log\psi_N(\theta)\to\lambda(e^{i\theta}-1).
\]
It predicts a \(\operatorname{Poisson}(\lambda)\) law and hence level-one
mass \(\lambda e^{-\lambda}=\lambda/2\), only half the true answer.  In
the actual model the second factorial moment is zero, while in the product
model it tends to \(\lambda^2\).  The hard constraint \(n\leq N\), not a
minor error term, destroys independence for the moving prime support.

## What remains usable

Neither Fourier analysis, Turan--Kubilius, nor a product-prime model can
prove (1) without an additional dispersion hypothesis.  A plausible
correct replacement is the standard Halasz concentration theorem for
additive functions (exact formulation recalled from memory): an exact atom
is \(O((1+H_N)^{-1/2})\), where
\[
 H_N=\sum_{\substack{p\leq N\\w_{p,N}\ne0}}\frac1p,
\]
with a concentration-function version for intervals.  This theorem should
be checked in its precise uniform form before use.  Both counterexamples
above have bounded \(H_N\), so they do not contradict such a repair.

For Problem 786 the conclusion is only a route obstruction: arbitrary
nonzero additive levels need not be \(o(N)\).  It neither supplies a
density-one level nor rules one out.  A successful negative argument must
instead prove a bound strictly below one, or combine a conditional
anti-concentration theorem with structural information forcing its
dispersion parameter to diverge.
