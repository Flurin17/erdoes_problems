# Averaged prime-gap tails and the quotient comb

## Status

This route gives a rigorous unconditional lower bound

\[
n_k\ge k^{2\log 2-o(1)}=k^{1.38629\ldots-o(1)}.
\]

It also gives an exact necessary prime-gap-tail condition and a conditional
translation from estimates for almost-all short intervals to lower bounds for
\(n_k\).  It does **not** give a matching upper bound, so it does not solve the
problem.

Throughout, the prime interval is the open interval \((k,2k)\), and
\(n>2k\) is an integer.  Put

\[
K=k+1,\qquad A=n-k,\qquad B=n-1.
\]

Thus admissibility means that no prime \(p\in(k,2k)\) has a multiple in the
integer interval \([A,B]\).

## 1. Exact quotient-comb formulations

### Forbidden teeth

For an integer \(q\ge1\), put

\[
T_q=[A/q,B/q].
\]

If \(n\) is admissible, then \(T_q\) contains no prime in \((k,2k)\): a
prime \(p\in T_q\) would give \(qp\in[A,B]\).  The full teeth lying strictly
inside \((k,2k)\) are indexed by

\[
L=\left\lfloor {B\over2k}\right\rfloor+1,
\qquad
U=\left\lceil {A\over k}\right\rceil-1.
\]

Indeed, these choices give \(B/q<2k\) and \(A/q>k\).  Consecutive teeth are
disjoint (their interiors are separated), and

\[
|T_q|={B-A\over q}={k-1\over q}.
\]

Consequently, if \(n/k\to\infty\),

\[
\sum_{q=L}^{U}|T_q|
=(k-1)\sum_{q=L}^{U}{1\over q}
=(\log2+o(1))k.                                      \tag{1}
\]

The endpoint teeth omitted by the strict-containment convention are harmless
in (1), but the displayed floors and ceilings are the exact ones.

### Safe bands

There is a second exact formulation which is better suited to an upper-bound
sieve.  For a prime \(p\in(k,2k)\), set \(j=\lceil n/p\rceil\).  The residue
\(n\bmod p\) is admissible precisely when it is \(0\) or at least \(K\).
Equivalently, \(p\) belongs to the closed safe band

\[
I_j=\left[{n\over j},{n-K\over j-1}\right].           \tag{2}
\]

Empty bands are ignored.  Every admissible prime occurs in exactly one band,
and all relevant nonempty bands have

\[
a=\left\lfloor {n\over2k}\right\rfloor+1
\le j\le
b=\left\lfloor {n\over K}\right\rfloor.             \tag{3}
\]

Conversely, a prime in one of (2)--(3) has residue \(0\) or at least \(K\),
so (2) is an equivalence, not merely a necessary condition.  The bands are
pairwise disjoint and lie in \([K,2k)\).  Their lengths are

\[
\ell_j={n-jK\over j(j-1)}.
\]

They telescope exactly:

\[
\sum_{j=a}^{b}\ell_j
={n\over a-1}-{n\over b}
-K\sum_{r=a-1}^{b-1}{1\over r}.                      \tag{4}
\]

In particular, uniformly whenever \(t=n/k\to\infty\),

\[
\sum_{j=a}^{b}\ell_j=(1-\log2)k+O(k/t+1).            \tag{5}
\]

An equivalent open-endpoint version uses
\(q=\lfloor B/p\rfloor\): every prime must lie in

\[
\left({B\over q+1},{A\over q}\right),
\quad
\left\lfloor {B\over2k}\right\rfloor
\le q\le
\left\lceil {B\over k}\right\rceil-1,               \tag{6}
\]

after intersection with \((k,2k)\).  Both endpoints in (6) are strict.

## 2. An unconditional Brun--Titchmarsh lower bound

We use the standard Brun--Titchmarsh interval estimate in the form

\[
\#\{p\in[x,x+y]:p\text{ prime}\}
\le {2y\over\log y}+O(1)\qquad(y>1),                 \tag{BT}
\]

and the prime number theorem in the form
\(\vartheta(2k)-\vartheta(k)=(1+o(1))k\).

Fix

\[
0<\delta<2\log2-1
\]

and suppose, toward a contradiction, that an admissible \(n\) satisfies
\(n\le k^{1+\delta}\).  The already elementary/PNT consequence
\(n_k/k\to\infty\) handles bounded \(n/k\), so it is enough to consider
\(t=n/k\to\infty\).  Choose a fixed \(\varepsilon>0\) so that

\[
\delta+\varepsilon<2\log2-1,
\]

and put \(H=k^{1-\delta-\varepsilon}\).

Apply (BT) separately to every safe band with \(\ell_j\ge H\), and weight
each prime by at most \(\log(2k)\).  Since there are \(O(t)=O(k^\delta)\)
bands, (5) gives

\[
\sum_{\substack{p\in(k,2k)\\p\text{ in a long band}}}\log p
\le
\left({2(1-\log2)\over1-\delta-\varepsilon}+o(1)\right)k
+O(k^\delta\log k).                                  \tag{7}
\]

For a short band, the number of integers it contains is at most
\(\ell_j+1\).  There are \(O(k^\delta)\) such bands, so their total weighted
prime mass is

\[
O\bigl(\log k\,(k^\delta H+k^\delta)\bigr)=o(k).      \tag{8}
\]

Every prime in \((k,2k)\) would have to lie in a safe band.  But the
coefficient in (7) is strictly less than \(1\), while PNT says that the total
weighted prime mass is \((1+o(1))k\), a contradiction.  Therefore, for every
fixed \(\delta<2\log2-1\),

\[
n_k>k^{1+\delta}
\quad\hbox{for all sufficiently large }k.
\]

Equivalently,

\[
\boxed{\displaystyle n_k\ge k^{2\log2-o(1)}.}        \tag{9}
\]

The factor \(2\) in Brun--Titchmarsh and the denominator
\(\log H=(1-\delta-\varepsilon)\log k\) are essential.  Replacing
\(\log H\) by \(\log k\) would give a false stronger exponent.

## 3. The exact length-weighted prime-gap-tail obstruction

Delete the primes in \((k,2k)\) from that interval and let \(G\) run over
the lengths of the resulting components, including the two truncated edge
components.  Set

\[
h={k-1\over U}.
\]

Each full tooth is contained in one such component and has length at least
\(h\).  Grouping teeth by their actual host component (rather than falsely
assuming distinct hosts) proves the exact necessary inequality

\[
\sum_{G\ge h}G
\ge (k-1)\sum_{q=L}^{U}{1\over q}.                   \tag{10}
\]

Thus, for an admissible \(n\) with \(n/k\to\infty\),

\[
\sum_{G\ge(1+o(1))k^2/n}G\ge(\log2+o(1))k.           \tag{11}
\]

This is the clean tail bottleneck: a positive fraction of all length in
\((k,2k)\) must lie in gaps at least of order \(k^2/n\).

For a useful conditional form, let \(M_k(H)\) be the Lebesgue measure of
starts \(x\in[k,2k-H]\) for which \((x,x+H)\) is prime-free.  Componentwise,

\[
M_k(H)=\sum_G(G-H)_+,
\qquad
\sum_{G\ge2H}G\le2M_k(H).                            \tag{12}
\]

Hence any rigorously proved estimate

\[
H=o(k),\qquad M_k(H)=o(k)                             \tag{13}
\]

implies

\[
n_k\ge(1-o(1)){k^2\over2H}.                          \tag{14}
\]

The factor \(2\) in (12)--(14) cannot be discarded by this argument.  A
remembered ``almost all short intervals contain primes'' theorem could be
inserted only after its exact uniform range and hypotheses are stated and
checked; no such external theorem is assumed here.

## 4. Why PNT or mean gaps alone do not close the route

It is invalid to assign different teeth to distinct prime gaps.  The interval
between adjacent teeth is merely allowed to contain primes; it is not forced
to contain one.  A single prime gap may swallow many consecutive teeth.
Inequality (10), which groups by the actual host gap, is the weakest clean
repair.

It is also invalid to multiply the safe-band support length
\((1-\log2+o(1))k\) by the ambient density \(1/\log k\).  PNT does not
control primes in a moving disconnected union with component scale about
\(k^2/n\).  A uniform union estimate with sieve constant \(C\), for
\(n/k=k^{\alpha+o(1)}\), would instead have the capacity coefficient

\[
{C(1-\log2)\over1-\alpha}{k\over\log k}.
\]

Thus \(C=2\) yields precisely (9), while a hypothetical constant-\(1\)
estimate would yield only \(n_k\ge k^{1+\log2-o(1)}\).  Ordinary PNT and the
fact that the mean prime gap is about \(\log k\) imply neither such a union
estimate nor (13) at a shrinking scale.

## 5. Reproducible numerical falsification target (evidence only)

A direct experiment should compute

\[
F_k(z)={1\over k}\sum_{G\ge z\log k}G.
\]

The route predicts that an admissible \(n\) would require
\(F_k(k^2/(n\log k))\gtrsim\log2\).  A deterministic sieve experiment at
\(k=10^3,10^4,10^5,10^6\) gave the following values for
\(z=.5,.75,1,1.1,1.2,1.5,2,3\), respectively:

```
10^3:  .9470 .8550 .6450 .6450 .5570 .4180 .2860 .1020
10^4:  .9159 .7803 .7116 .6196 .6196 .4888 .2778 .1156
10^5:  .9445 .8041 .7252 .6225 .6225 .5083 .3196 .1146
10^6:  .8943 .7977 .7121 .6602 .6175 .4902 .3454 .1343
```

The exponential-gap heuristic gives \((z+1)e^{-z}\); its \(\log2\)
threshold is \(z\approx1.1161\).  These data motivate a possible
\(k^2/\log k\) lower scale but prove nothing.  A production computation must
record its script, exact command, sentinel convention, runtime, and an
independent small-case check under `computational/`.

## 6. Current bottleneck and falsification tests

The sharp lower-bound bottleneck is either:

1. prove an unconditional length-weighted tail estimate contradicting (11)
   at the conjecturally relevant scale; or
2. replace the factor-\(2\) upper-bound sieve on the moving safe-band union by
   an asymptotically sharp estimate, with accumulated endpoint errors
   controlled.

Concrete falsification tests are:

- search for admissible \(n\le k^{1+\delta}\) with
  \(\delta<2\log2-1\) (this would expose an error in the theorem above);
- verify (4) and the band equivalence prime-by-prime in exhaustive small
  cases, especially when an endpoint is integral;
- measure whether the left side of (11) can remain at least
  \((\log2-o(1))k\) when its threshold grows faster than \(\log k\).

The matching upper bound and hence the sharp asymptotic for \(n_k\) remain
open in this route.
