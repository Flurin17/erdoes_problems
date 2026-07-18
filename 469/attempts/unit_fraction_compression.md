# Unit-fraction compression route

## Status

This file records rigorous restrictions obtained from an exact distinct-unit-fraction
representation.  They give a nontrivial convergent subfamily and strong lower bounds
on the largest denominator, but they do **not** prove convergence of the whole set in
Problem 469.  The remaining case consists of representations having a very large
largest denominator; the shadow inequality below loses too much information there.

Throughout, let

\[
  2\le q_1<\cdots<q_k=Q,\qquad
  \sum_{i=1}^k\frac1{q_i}=1,
  \qquad N=\operatorname{lcm}(q_1,\ldots,q_k),
\]

and put \(P=\prod_iq_i\) and \(d_i=N/q_i\).  Then the \(d_i\) are
distinct proper divisors of \(N\),

\[
  \sum_i d_i=N,\qquad \gcd_i d_i=1.
\]

Conversely, such a divisor partition gives the displayed unit-fraction identity.
If \(n\) is divisibility-minimal semiperfect and a divisor partition of \(n\) is
divided by \(n\), the lcm of its denominators must be \(n\): otherwise the same
identity, multiplied by the smaller lcm, makes a proper divisor of \(n\)
semiperfect.  Thus all the lemmas below apply to every member of the set in Problem
469.

## 1. Every one-denominator shadow is lcm-full

For each \(i\), set \(L_{-i}=\operatorname{lcm}_{j\ne i}q_j\).  The identity gives

\[
  \frac1{q_i}
   =1-\sum_{j\ne i}\frac1{q_j}
   =\frac{A_i}{L_{-i}}
\]

for a positive integer \(A_i\).  Hence \(L_{-i}=A_iq_i\), so \(q_i\mid L_{-i}\)
and therefore

\[
  \operatorname{lcm}_{j\ne i}q_j=N.                 \tag{1.1}
\]

Several useful consequences are immediate.

* For every prime power \(p^a\Vert N\), at least two denominators have
  \(p\)-adic exponent \(a\).
* Consequently
  \[
     q_i^2\mid P\quad(1\le i\le k),\qquad N^2\mid P.       \tag{1.2}
  \]
* The two distinct multiples of \(p^a\) just found are at most \(Q\), so
  \(p^a\le Q/2\).  Hence
  \[
     N\mid \Lambda_{\lfloor Q/2\rfloor},
     \qquad \Lambda_y:=\operatorname{lcm}(1,2,\ldots,y).  \tag{1.3}
  \]

There is also a pairwise-overlap form.  Assign each maximal prime power
\(p^a\Vert N\) to one pair of denominators in which it occurs.  Multiplying the
prime powers assigned to the pair \(i,j\) gives pairwise coprime numbers
\(r_{ij}\mid\gcd(q_i,q_j)\), and therefore

\[
  N\mid\prod_{i<j}\gcd(q_i,q_j)
    \mid\prod_{i<j}(q_j-q_i).                         \tag{1.4}
\]

## 2. Length and maximum-denominator bounds

First, distinctness gives the packing inequality

\[
  H_Q-H_{Q-k}=\sum_{r=Q-k+1}^{Q}\frac1r\le1.          \tag{2.1}
\]

Put \(x_i=Q/q_i\).  Then \(x_i\ge1\) and \(\sum_i x_i=Q\), so expansion of
\(\prod_i(1+(x_i-1))\) gives

\[
  \prod_i x_i\ge1+\sum_i(x_i-1)=Q-k+1.
\]

Together with (1.2), this yields

\[
  N^2(Q-k+1)\le P(Q-k+1)\le Q^k.                     \tag{2.2}
\]

Moreover, (2.1) and the integral comparison

\[
  \sum_{r=Q-k+1}^{Q}\frac1r
  \ge \int_{Q-k+1}^{Q+1}\frac{dt}{t}
\]

show that \(Q-k+1\ge(Q+1)/e\).  Thus

\[
  N^2<eQ^{k-1},
  \qquad
  k>1+\frac{2\log N-1}{\log Q}.                      \tag{2.3}
\]

There is also a literal entropy formulation.  The numbers \(1/q_i\) form a
probability vector, so

\[
  \log k\ge \sum_i\frac{\log q_i}{q_i}
  \ge \frac{\log P}{Q}
  \ge \frac{2\log N}{Q}.
\]

In particular, \(Q\ge2\log N/\log k\).  This is weaker than the cofactor-band
bound below, but identifies exactly what the unconditioned Shannon estimate sees.

There is a bound depending only on \(k\).  Let

\[
  L_j=\operatorname{lcm}(q_1,\ldots,q_j),\qquad
  R_j=1-\sum_{i\le j}\frac1{q_i}.
\]

Since the denominators are distinct, \(q_1\le k-1\).  For \(j\le k-2\), the
positive rational \(R_j\) is an integral multiple of \(1/L_j\), while

\[
  R_j=\sum_{i>j}\frac1{q_i}<\frac{k-j}{q_{j+1}}.
\]

It follows that

\[
  q_{j+1}\le(k-j)L_j-1,\qquad
  L_{j+1}<(k-j)L_j^2.                                 \tag{2.4}
\]

At the final step, \(1/q_k=A/L_{k-1}\), so \(q_k\mid L_{k-1}\) and
\(N=L_{k-1}\).  Iterating (2.4) gives

\[
  N< (k-1)^{2^{k-2}}
      \prod_{j=1}^{k-2}(k-j)^{2^{k-2-j}}
    \le (k-1)^{2^{k-1}-1}.                            \tag{2.5}
\]

In particular,

\[
  k\ge \log_2\log N-O(\log\log\log N).              \tag{2.6}
\]

The double-exponential scale in (2.5) cannot be improved in general.  The
Sylvester recursion \(s_1=2\), \(s_{j+1}=\prod_{i\le j}s_i+1\), with the final
denominator \(\prod_{i<k}s_i\), gives a \(k\)-term identity whose lcm is at least
\(6^{2^{k-3}}\).  These examples are not divisibility-minimal after the first
stage, so this only tests the universal unit-fraction estimate, not Problem 469
itself.

## 3. Cofactor-band compression

The crude prime-power ceiling \(p^a\le Q/2\) can be strengthened substantially.
Fix an integer \(H\ge2\).  For \(U\subseteq\{1,\ldots,H\}\), \(|U|\ge2\), define

\[
  A(U):=\sum_{u\in U}\frac{\operatorname{lcm}(U)}u,
\]

and let \(S_H\) be the finite set of primes dividing at least one \(A(U)\).

Suppose \(p^a\Vert N\) and \(p^a>Q/(H+1)\).  The denominators attaining maximal
\(p\)-adic exponent have the form \(p^au\), where the \(u\)'s are distinct,
\(p\)-free, and at most \(H\).  There are at least two of them by (1.1); call
their set of cofactors \(U\).  Write \(M=N/p^a\) and \(L=\operatorname{lcm}(U)\).
Reducing \(\sum_iN/q_i=N\) modulo \(p\) kills all terms belonging to denominators
of smaller \(p\)-adic exponent and gives

\[
  0\equiv\sum_{u\in U}\frac Mu
   =\frac ML A(U)\pmod p.
\]

Since \(p\nmid M/L\), it follows that \(p\mid A(U)\), hence \(p\in S_H\).
Therefore every maximal prime power of \(N\) is either at most \(Q/(H+1)\) or
has its base prime in \(S_H\), and

\[
  N\le
  \Lambda_{\lfloor Q/(H+1)\rfloor}Q^{|S_H|}.          \tag{3.1}
\]

For each \(U\),
\(A(U)\le H\operatorname{lcm}(U)\le HH!\).  Counting its possible prime factors
very crudely gives

\[
  |S_H|\le2^H\log_2(HH!)=O(2^HH\log H).              \tag{3.2}
\]

Use the elementary Chebyshev bound \(\Lambda_x\le4^x\), and choose

\[
  H=\left\lfloor\log_2Q-5\log_2\log Q\right\rfloor.
\]

Then

\[
  \log\Lambda_{\lfloor Q/(H+1)\rfloor}
   \le\left(2(\log2)^2+o(1)\right)\frac Q{\log Q},
\]

whereas (3.2) gives \(|S_H|\log Q=o(Q/\log Q)\).  Hence

\[
  \boxed{\displaystyle
  \log N\le
  \left(2(\log2)^2+o(1)\right)\frac Q{\log Q}}
                                                               \tag{3.3}
\]

and, on inversion,

\[
  \boxed{\displaystyle
  Q\ge
  \left(\frac1{2(\log2)^2}+o(1)\right)
  (\log N)(\log\log N).}                              \tag{3.4}
\]

If the prime number theorem estimate \(\log\Lambda_x\sim x\) is admitted, the
constant \(2(\log2)^2\) in (3.3) improves to \(\log2\).  No prime number theorem
is needed for (3.3)--(3.4).

There is also a counting version.  For identities with \(Q\le Y\), use the same
choice of \(H=H(Y)\) and put \(x=\lfloor Y/(H+1)\rfloor\).  Every resulting lcm
divides

\[
  M_Y:=\Lambda_x
       \prod_{\substack{p\in S_H\\p\le Y}}
       p^{\lfloor\log_pY\rfloor}.                     \tag{3.5}
\]

The standard Chebyshev estimate \(\pi(t)=O(t/\log t)\) gives

\[
  \log\tau(\Lambda_x)=O(x/\log x)=O(Y/(\log Y)^2),
\]

and the exceptional-prime factor contributes only
\(o(Y/(\log Y)^2)\) to \(\log\tau(M_Y)\).  Consequently

\[
  \#\{N:\text{some such identity has }Q\le Y\}
  \le\tau(M_Y)
  =\exp\!\left(O\!\left(\frac{Y}{(\log Y)^2}\right)\right).  \tag{3.6}
\]

For example, dyadic summation of (3.6) proves convergence for the subfamily with
\(Q\le c(\log N)(\log\log N)^2\), for a sufficiently small absolute \(c>0\).

A stronger, still elementary weighted-divisor tail follows already from (1.3).
For \(y<X\), \(L=\log X\), \(u=\log y\), and \(g=L/u\), Rankin's inequality gives

\[
 \sum_{\substack{d\mid\Lambda_y\\d\ge X}}\frac1d
 \le X^{-t}\prod_{p\le y}(1-p^{-1+t})^{-1}.           \tag{3.7}
\]

For \(t=z/(2u)\le1/4\), a decomposition of primes into the intervals
\((e^{m-1},e^m]\), together with \(\pi(v)=O(v/\log v)\), gives uniformly

\[
  \log\prod_{p\le y}(1-p^{-1+t})^{-1}
  =O(\log u+e^z).                                      \tag{3.8}
\]

Indeed, the first-prime-power contribution is bounded by a constant times
\(\sum_{m\le2u}e^{tm}/m\le O(\log u+e^z)\), and all higher prime powers contribute
\(O(1)\).  Taking \(z=\tfrac12\log g\) (in the range relevant below) yields

\[
 \log\sum_{\substack{d\mid\Lambda_y\\d\ge X}}\frac1d
 \le-\frac14g\log g+O(\log u+\sqrt g).                \tag{3.9}
\]

Since every lcm with maximum denominator at most \(Y\) divides
\(\Lambda_{\lfloor Y/2\rfloor}\), (3.9) and dyadic summation show the following
genuine partial convergence result: for sufficiently small absolute \(c>0\),
the reciprocal sum converges over all represented \(N\) for which there exists
an identity whose maximum denominator \(Q\) satisfies

\[
  Q\le
  \exp\!\left(
    c\,\frac{(\log N)(\log\log\log N)}{\log\log N}
  \right).                                             \tag{3.10}
\]

More invariantly, the same proof works whenever
\(\log Q=o((\log N)(\log\log\log N)/\log\log N)\).
Minimality is not needed for this subfamily once the lcm is known to equal \(N\).

## 4. Shadow counting and its exact obstruction

Let \(\mathcal F_{N,k}\) be the family of \(k\)-element denominator sets having
sum of reciprocals one and lcm \(N\).  Every one-element deletion has lcm \(N\)
by (1.1), and it determines the missing denominator uniquely from

\[
  \frac1q=1-\sum_{t\in T}\frac1t.
\]

Thus

\[
  k|\mathcal F_{N,k}|\le G_{k-1}(N),                  \tag{4.1}
\]

where the number of \(s\)-subsets of divisors \(>1\) having lcm exactly \(N\) is

\[
  G_s(N)=\sum_{d\mid N}\mu(N/d){\tau(d)-1\choose s}. \tag{4.2}
\]

Globally, if \(\mathcal F_k(Q)\) denotes identities contained in
\(\{2,\ldots,Q\}\), then

\[
  k|\mathcal F_k(Q)|\le {Q-1\choose k-1},             \tag{4.3}
\]

and, because deletion preserves the lcm, the weighted form is

\[
  k\sum_{S\in\mathcal F_k(Q)}\frac1{\operatorname{lcm}(S)}
  \le
  \sum_{\substack{T\subseteq\{2,\ldots,Q\}\\|T|=k-1}}
       \frac1{\operatorname{lcm}(T)}.                 \tag{4.4}
\]

Equation (4.4) is not a convergence proof.  Its right-hand majorant has infinite
mass even for a fixed shadow size \(s\): for every \(a\ge2\), take

\[
  T_a=\{a,2a,\ldots,sa\}.
\]

Then

\[
  \operatorname{lcm}(T_a)=a\operatorname{lcm}(1,\ldots,s),
\]

so

\[
  \sum_{a\ge2}\frac1{\operatorname{lcm}(T_a)}
  =\frac1{\operatorname{lcm}(1,\ldots,s)}
    \sum_{a\ge2}\frac1a
  =\infty.                                             \tag{4.5}
\]

Most of these shadows do not extend to a unit-fraction identity.  Passing from the
left side of (4.4) to all lcm-full shadows discards precisely the exact reciprocal
constraint that could make the family sparse.  Divisibility-minimality supplies no
known mechanism for removing the harmonic family (4.5) from the majorant.

## Current bottleneck

The estimates above settle the contribution from representations whose largest
denominator satisfies (3.10), and (3.4) shows that every representation starts at
least near the scale \((\log N)(\log\log N)\).  They give no adequate count when
\(Q\) is much larger, in particular when \(Q=N^{\theta}\) or \(Q\) is comparable
to \(N\).  A full convergence proof still needs a sparse charging principle that
uses divisibility-minimality in this large-\(Q\) range, or else an explicit
divergent minimal family.
