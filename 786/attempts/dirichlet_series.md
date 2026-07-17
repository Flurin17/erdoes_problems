# Dirichlet-series and compound-Poisson route

## Mechanism and result

The grading theorem puts every repetition-allowed PLR set inside a nonzero
level of a rational completely additive function. Under
\(\mu_s(n)=n^{-s}/\zeta(s)\), prime valuations are independent geometric
variables, hence their weighted sum is zero-drift compound Poisson. A
winding-number argument bounds every nonzero atom by \(1/2\).

Therefore every such infinite PLR set has lower density at most \(1/2\).
For finite \(A_N\), with \(m_N=N-|A_N|\),
\[
 m_N+1\geq N^{\beta_*-o(1)},\qquad
 (1-\beta_*)\beta_*^{\beta_*/(1-\beta_*)}=\frac12.
\]
The full proof is in ../PROOF.md.

## Lemma chain

1. PLR implies \(A\subseteq f^{-1}(1)\).
2. Zeta-distributed prime valuations are independent geometric variables.
3. Their weighted sum has finite compound-Poisson Lévy measure for \(s>1\).
4. A zero-drift compound-Poisson law has no nonzero atom above \(1/2\).
5. Partial summation bounds lower density.
6. Rearrangement and \(s=1+c/\log N\) give the finite exponent.

## Bottleneck and falsification

The infinite result is complete after audit. The finite problem needs a
uniform analogue for nearly uniform measure on \([1,N]\); zeta measures
overweight small integers.

The atom lemma must exclude zero and deterministic drift. Each finite
truncation may clear only its own denominators. The density conclusion is
about lower density, not upper natural density.
