# Threshold grading: a (0.82849\ldots)-density finite construction

## Mechanism

Fix (2<u<3), put (y=N^{1/u}), and assign the rational prime weights
\[
w_p=\begin{cases}0,&p\le y,\\1,&p>y.\end{cases}
\]
Let
\[
A_N(u)=\{n\le N:\Omega_{>y}(n)=1\},\qquad
\Omega_{>y}(n)=\sum_{p>y}v_p(n).
\]
This is an exact level set of a completely additive function, hence is PLR
with repetitions and arbitrary product lengths.

## Lemma chain and proof

For fixed (2<u<3), an integer (n\le N) has at most two prime factors
larger than (y=N^{1/u}), counted with multiplicity: three such factors would
have product (>y^3>N).  Let (P_k(N,u)) denote the proportion of integers
with exactly (k\in\{0,1,2\}) such factors.

The standard fixed-(u) Dickman smooth-number theorem states
\[
P_0(N,u)=\frac{\Psi(N,N^{1/u})}{N}=\rho(u)+o(1). \tag{1}
\]
This theorem is used as a precisely stated standard dependency; it is not
proved here.

Double-counting large-prime incidences gives
\[
P_1+2P_2
=\frac1N\sum_{n\le N}\Omega_{>y}(n)
=\sum_{y<p\le N}\sum_{e\ge1}\frac1N\left\lfloor\frac N{p^e}\right\rfloor.
\]
The terms (e\ge2) contribute (o(1)): their main terms are at most
\(\sum_{p>y}p^{-2}=o(1)), and their accumulated floor errors are also
(o(1)) because only (p\le\sqrt N) can occur.  The (e=1) terms equal
\[
\sum_{y<p\le N}\frac1p+o(1)=\log u+o(1) \tag{2}
\]
by the standard Mertens theorem for prime reciprocals.  Since
\(P_0+P_1+P_2=1), (1)--(2) imply
\[
\boxed{\quad P_1(N,u)=2-2\rho(u)-\log u+o(1).\quad} \tag{3}
\]

On (2<u<3), Dickman's differential equation gives
\(u\rho'(u)=-\rho(u-1)), while
\(\rho(u-1)=1-\log(u-1)).  Differentiating the main term in (3) gives
\[
c'(u)=\frac{2\rho(u-1)-1}{u}.
\]
Thus its unique maximum on this interval occurs at
\[
u_*=1+\sqrt e,
\]
and
\[
|A_N(u_*)|=(c_*+o(1))N,
\qquad
c_*=2-2\rho(1+\sqrt e)-\log(1+\sqrt e)
=0.82849\ldots .
\]
The numerical value is only illustrative; the exact expression is the
mathematical claim.

## Density and scope

This rigorously improves the elementary threshold (y=\sqrt N), whose
density is \(\log2+o(1)\), but it remains bounded away from (1).  It solves
neither requested asymptotic question.

## Weakest step and falsification

The construction itself is complete subject to the two named standard
analytic number theory inputs.  The unsupported extension is whether
multi-band or recursively chosen non-binary weights can drive the atom mass
to (1-o(1)).  Any such claim can be falsified by computing the exact rank
test on its proposed level set and by comparing its predicted factor-pattern
mass with direct deterministic counts.

## Next action

Optimize two- and three-band weights by partitioning the possible normalized
large-prime factor patterns, and analyze the exact ascending-prime modal
recursion described in `modal_recursion.md`.
