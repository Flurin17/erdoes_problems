# Strongest coherent partial result for Erdős Problem #469

The full convergence question remains open locally.  This file proves the
strongest dependency-complete global partial theorem obtained in this run.

## Theorem

For every fixed integer \(k\geq1\),
\[
\sum_{\substack{n\in A\\\omega(n)=k}}\frac1n<\infty.
\]

## Coprime-cut lemma

Suppose \(n=uv\in A\), \((u,v)=1\), \(t=\omega(v)\), and \(q=P^-(v)\).
Then
\[
q\leq2t\sigma(u).                                                    \tag{1}
\]

Choose a semiperfect representation of \(n\) and group its selected divisors
according to their \(v\)-part:
\[
uv=\sum_{e\mid v}eS_e,
\]
where each \(S_e\) is a subset sum of divisors of \(u\).  In the top group
\(e=v\), only proper divisors of \(u\) are available.  Also \(S_v\leq u\),
because every other group is nonnegative.  Equality would make \(u\)
semiperfect, contradicting the minimality of \(n\).  Thus \(u-S_v\geq1\), and
\[
v\leq v(u-S_v)
  =\sum_{\substack{e\mid v\\e<v}}eS_e
  \leq\sigma(u)(\sigma(v)-v).
\]
Consequently
\[
\frac{\sigma(v)}v-1\geq\frac1{\sigma(u)}.                           \tag{2}
\]
On the other hand,
\[
\frac{\sigma(v)}v
 <\prod_{p\mid v}(1-1/p)^{-1}
 \leq\left(1+\frac1{q-1}\right)^t
 \leq\exp\!\left(\frac{t}{q-1}\right).
\]
If \(q-1\geq2t\sigma(u)\), the last expression is strictly below
\(1+1/\sigma(u)\), contradicting (2).  This proves (1).

## Recursive prime bound

Write
\[
n=\prod_{j=1}^k p_j^{a_j},\qquad p_1<\cdots<p_k,
\quad U_j=\prod_{i<j}p_i^{a_i}.
\]
Applying (1) to \(u=U_j\) and the remaining suffix gives
\[
p_j\leq2(k-j+1)\sigma(U_j).                                         \tag{3}
\]
Moreover
\[
\frac{\sigma(U_j)}{U_j}
 <\prod_{i<j}\frac{p_i}{p_i-1}
 \leq\prod_{i<j}\frac{i+1}{i}=j,
\]
because the \(i\)-th smallest distinct prime is at least \(i+1\).  Hence,
with \(B_k=2k^2\),
\[
p_j\leq B_kU_j                                                     \tag{4}
\]
for every \(j\), and in particular \(p_1\leq B_k\).

## Summing the recursive overcount

Fix \(B\geq2\).  Let \(H_t(x)\) be the total reciprocal multiplier obtained
by choosing \(t\) further integer prime-power surrogates \(q^a\), allowing
repetitions and composites, subject at each step to \(2\leq q\leq Bx\), where
the new prefix is \(xq^a\).  Thus
\[
H_0(x)=1,
\qquad
H_t(x)=\sum_{2\leq q\leq Bx}\sum_{a\geq1}
       q^{-a}H_{t-1}(xq^a).                                        \tag{5}
\]
Put \(W(x)=1+\log x\) and \(c_B=1+\log B\).  Inductively,
\[
H_t(x)\leq C_{B,t}W(x)^t                                           \tag{6}
\]
for finite constants depending only on \(B,t\).  Indeed, if (6) holds at
level \(t-1\), then \(q\leq Bx\) gives
\[
W(xq^a)\leq W(x)(1+ac_B),
\qquad q^{-a}\leq q^{-1}2^{-(a-1)},
\]
while
\[
\sum_{2\leq q\leq Bx}\frac1q\leq c_BW(x).
\]
Substitution in (5) proves the next case because
\[
\sum_{a\geq1}2^{-(a-1)}(1+ac_B)^{t-1}<\infty.
\]

Every actual \(n\in A\) with \(\omega(n)=k\) is included in (5) with
\(B=B_k\), by (4).  Its total reciprocal mass is therefore at most
\(H_k(1)<\infty\), proving the theorem.

## Missing dependency for the full problem

The constants \(B_k\) and \(C_{B_k,k}\) grow rapidly with \(k\), so these
bounds cannot be summed over all \(k\).  This is not just an endpoint issue:
350 and 770 have abundant nonsemiperfect proper divisors, and the exact defect
tree admits multi-step resets such as
\(70\to70\cdot149\to70\cdot149\cdot1489\).  A complete solution needs a
\(k\)-uniform weighted bound on those weird-core extension trees, or a
divergent explicit family built from them.
