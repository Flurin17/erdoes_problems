# Finite uniform additive fibers: divisor removal, Sperner, and the exact escape

## Question attacked

Let
\[
 f(n)=\sum_{p\leq N}w_pv_p(n),\qquad w_p\in\mathbb Q,
\]
and let \(c\ne0\). Is there an absolute \(\delta>0\) such that every exact
fiber
\[
 L=L_N(f,c):=\{n\leq N:f(n)=c\}
\]
satisfies \(|L|\leq(1-\delta)N\)? Such a bound would answer the finite
repetition-allowed question negatively. An arbitrary PLR set contained in
this fiber can be enlarged to the full fiber, which is still PLR, so it is
enough to study \(L\).

After scaling and changing sign, take \(c=1\). Put \(B=[1,N]\setminus L\)
and \(m=|B|\).

The outcome of this route is not yet a universal gap. It gives three exact
lemmas, identifies why a direct Sperner packing cannot work in the
near-full regime, and reduces the remaining issue to two precise uniform
Kubilius/sieve statements.

## 1. Composite divisor removal and the small-base phenomenon

**Lemma 1 (composite chain bound).** If \(q\geq2\) and \(f(q)\ne0\), then
\[
 |B|\geq \left\lfloor\frac Nq\right\rfloor. \tag{1}
\]

**Proof.** Partition \([1,N]\) into the chains
\[
 \{b,bq,bq^2,\ldots\},\qquad q\nmid b.
\]
The values on a chain are \(f(b)+jf(q)\), so a fiber contains at most one
member of each chain. The number of chains is
\(N-\lfloor N/q\rfloor\), proving (1). This argument does not require \(q\)
to be prime. \(\square\)

Set
\[
 Y=\frac{N}{m+1}.
\]
Lemma 1 implies
\[
 f(q)=0\quad(q\leq Y),\qquad
 w_p\ne0\Longrightarrow p>Y. \tag{2}
\]
The composite assertion in (2) is formally stronger than the prime-chain
form, although complete additivity makes its first part follow from the
vanishing of all prime weights up to \(Y\).

Let
\[
 \mathcal P_+=\{p:w_p>0\}.
\]
Every \(n\in L\) has a divisor in \(\mathcal P_+\), since a number supported
only on weights \(\leq0\) has \(f(n)\leq0\). More is true.

**Lemma 2 (all positive-prime removals land in the small exceptional
prefix).** If \(n\in L\) and \(p\in\mathcal P_+\) divides \(n\), then
\[
 b=\frac np\in B\cap[1,m]. \tag{3}
\]

**Proof.** We have \(f(b)=1-w_p\ne1\), so \(b\in B\). By (2),
\(p>Y=N/(m+1)\), and hence \(b\leq N/p<m+1\). \(\square\)

Thus, in a hypothetical \(m=o(N)\) example, every retained integer is an
upward positive-prime neighbor of an exceptional integer at most \(m\).
This explains how the same small exceptional prefix can absorb the losses
from very many active-prime chains.

A useful exact decomposition makes the role of signs transparent. For
each \(n\), write uniquely
\[
 n=bq,
\]
where \(q\) contains all prime-power factors of \(n\) from
\(\mathcal P_+\), and \(b\) is divisible by no prime in \(\mathcal P_+\).
Then \(f(b)\leq0\), while \(q\mapsto f(q)\) is strictly increasing under
proper divisibility in the \(\mathcal P_+\)-smooth semigroup. Consequently,
for each fixed \(b\),
\[
 \{q\leq N/b:q\text{ is }\mathcal P_+\text{-smooth and }bq\in L\} \tag{4}
\]
is a divisibility antichain not containing \(1\). The fibers indexed by
\(\mathcal P_+\)-free \(b\)'s partition \([1,N]\). This removes all
negative weights from the local problem, but Section 3 shows that the
antichain conclusion alone is much too weak.

## 2. An exact disjoint-cube Littlewood--Offord bound

**Lemma 3 (finite divisor cubes).** Let \(p_1,\ldots,p_k\) be distinct
active primes and put \(Q=\prod_{i=1}^kp_i\). Then
\[
 m\ \geq\left(2^k-\binom{k}{\lfloor k/2\rfloor}\right)
 \#\{x\leq N/Q:(x,Q)=1\}. \tag{5}
\]
In particular, with \(X=\lfloor N/Q\rfloor\),
\[
 m\ \geq\left(2^k-\binom{k}{\lfloor k/2\rfloor}\right)
 \left(X\frac{\varphi(Q)}Q-2^k\right). \tag{6}
\]

**Proof.** For every \(x\leq N/Q\) coprime to \(Q\), consider the Boolean
cube
\[
 C_x=\left\{x\prod_{i=1}^kp_i^{\epsilon_i}:
                 \epsilon_i\in\{0,1\}\right\}.
\]
These cubes lie in \([1,N]\) and are pairwise disjoint. On \(C_x\), the
fiber equation is
\[
 \sum_i\epsilon_iw_{p_i}=1-f(x). \tag{7}
\]
Reverse the \(i\)-th Boolean coordinate whenever \(w_{p_i}<0\). Up to an
additive constant, the left side becomes
\(\sum_i\delta_i|w_{p_i}|\). The subsets attaining a fixed value form an
antichain: strict inclusion strictly increases this positive sum. Sperner's
theorem therefore bounds their number by
\(\binom{k}{\lfloor k/2\rfloor}\). This proves (5). Finally,
inclusion--exclusion gives
\[
 \#\{x\leq X:(x,Q)=1\}
 =\sum_{d\mid Q}\mu(d)\left\lfloor\frac Xd\right\rfloor
 \geq X\frac{\varphi(Q)}Q-2^k,
\]
which proves (6). \(\square\)

This lemma is valid for arbitrary signs and arbitrary nonzero rational
weights. It is the exact finite analogue of the Littlewood--Offord step one
would want inside a Kubilius model.

Unfortunately, it cannot by itself yield a constant gap after (2). In the
near-full regime every chosen active prime exceeds \(Y\), so
\[
 Q>Y^k,
 \qquad
 \left|\bigcup_x C_x\right|
 =2^k\#\{x\leq N/Q:(x,Q)=1\}
 \leq N\left(\frac2Y\right)^k. \tag{8}
\]
For \(m=o(N)\), \(Y\to\infty\), and every single disjoint cube family has
vanishing uniform mass. Summing (5) over many choices of primes introduces
exactly the large incidence multiplicities at the small bases described in
Lemma 2.

## 3. Why a pure divisor-poset/Sperner proof is impossible

The failure in (8) is not just an inefficient packing. The antichain
relaxation itself admits density \(1-o(1)\).

For a set \(S\) of primes, write \(x\prec_S z\) when \(z/x\) is a nonunit
\(S\)-smooth integer. Take
\[
 y=\lceil\log N\rceil,
 \qquad S=\{p\leq N:p>y\},
\]
and define
\[
 T=\{n:N/y<n\leq N\text{ and }n\text{ has a prime divisor in }S\}. \tag{9}
\]
Then \(T\) is a root-avoiding \(S\)-antichain. Indeed, if \(x,z\in T\) and
\(z/x\) is a nonunit \(S\)-smooth integer, then \(z/x>y\), whence
\(z>(N/y)y=N\), a contradiction.

Moreover,
\[
 |T|\geq N-N/y-\Psi(N,y)=N-o(N). \tag{10}
\]
For completeness, the last estimate needs no Dickman theorem. Rankin's
bound with exponent \(1/2\) gives
\[
 \Psi(N,y)
 \leq N^{1/2}\prod_{p\leq y}(1-p^{-1/2})^{-1}
 \leq N^{1/2}\exp(O(\sqrt y))=o(N) \tag{11}
\]
when \(y=\lceil\log N\rceil\).

Thus even an antichain which avoids every minimal (all-passive) element can
occupy \(1-o(1)\) of \([1,N]\). Such a top-slab antichain is not generally a
single weighted additive level. Any successful Sperner argument must use
the fact that the **same prime weights couple all the different components
and all multiplicative scales**; componentwise width bounds discard exactly
the needed information.

## 4. Harmonic-mass reduction to two uniform lemmas

Let
\[
 S(f)=\{p\leq N:w_p\ne0\},
 \qquad H_N(f)=\sum_{p\in S(f)}\frac1p. \tag{12}
\]
Two elementary consequences are
\[
 L\subseteq\bigcup_{p\in S(f)}p\mathbb N,
 \qquad
 \frac{|L|}{N}\leq H_N(f). \tag{13}
\]
Hence a near-full nonzero fiber has \(H_N(f)\geq1-o(1)\). Lemma 1 also
shows that a sequence of near-full fibers has
\[
 \min S(f)\longrightarrow\infty. \tag{14}
\]

The following two statements would close the route. They are recorded
precisely so that neither is hidden inside the phrase “apply Kubilius.”

**(PA) Bounded-harmonic prime avoidance.** If \(N_j\to\infty\),
\(S_j\) is a set of primes at most \(N_j\),
\(\min S_j\to\infty\), and
\(\sum_{p\in S_j}1/p\leq K<\infty\), then
\[
 \liminf_{j\to\infty}\frac1{N_j}
 \#\{n\leq N_j:p\nmid n\text{ for every }p\in S_j\}>0. \tag{PA}
\]
The positive lower bound may depend on \(K\).

**(UKLO) Uniform triangular-array Kubilius--Littlewood--Offord.** If
\(f_j\) is completely additive,
\(\min S(f_j)\to\infty\), and \(H_{N_j}(f_j)\to\infty\), then
\[
 \max_t\frac1{N_j}\#\{n\leq N_j:f_j(n)=t\}\longrightarrow0. \tag{UKLO}
\]

Here is the exact conditional deduction. Suppose nonzero fibers of density
tending to \(1\) existed. By Lemma 1 their least active primes tend to
infinity. If their \(H_N\)'s have a bounded subsequence, (PA) supplies a
positive proportion of integers with no active prime divisor; all those
integers have value \(0\) and lie outside the nonzero fiber, a contradiction.
If no bounded subsequence exists, pass to one on which \(H_N\to\infty\);
(UKLO) is then a contradiction. Therefore (PA) and (UKLO) together imply
the existence of an absolute asymptotic gap \(\delta>0\).

A remembered form of Halász's concentration theorem for additive functions
looks like
\[
 \max_t\frac1N\#\{n\leq N:f(n)=t\}
 \ll H_N(f)^{-1/2} \tag{15}
\]
possibly with an additional truncation/error term. Its exact hypotheses
and triangular-array uniformity have **not** been verified here, so (15) is
not being invoked as a proved result. A version uniform enough for weights
depending on \(N\) would establish (UKLO).

Statement (PA) is a separate sieve issue and cannot be replaced by the union
bound once \(H_N\geq1\). It also necessarily has very poor dependence on
\(K\): for fixed \(u\), taking
\(S=\{p>N^{1/u}\}\) gives harmonic mass asymptotic to \(\log u\), while the
avoiding set is the \(N^{1/u}\)-smooth integers, of density \(\rho(u)\).
Thus a bound in (PA) at \(K=\log u\) can be no larger than \(\rho(u)\).

## 5. Weakest unsupported step and next tests

The weakest missing input is now explicit: prove (PA), for example by a
lower-bound sieve inside a suitably chosen smooth-number population. Once
(PA) forces \(H_N\to\infty\), prove (UKLO) either from an exact Halász
concentration theorem or by a self-contained Kubilius approximation plus
the oriented Sperner argument of Lemma 3.

Concrete falsification tests are:

1. For (PA), construct prime sets \(S_N\) with bounded
   \(\sum_{p\in S_N}1/p\), least prime tending to infinity, and whose
   multiples cover \(1-o(1)\) of \([1,N]\). Such a construction would kill
   the whole harmonic-mass dichotomy.
2. For (UKLO), construct rational weights with \(H_N\to\infty\) but with one
   exact additive atom of positive uniform density. Signed weights and
   alternating prime bands are the most relevant stress test.
3. Any proposed divisor-cube summation must be checked against (9)--(11).
   If it uses only comparability or componentwise antichain width, the set
   \(T\) is already a counterexample to the claimed gap.

The next constructive action is therefore not another unweighted cube
packing. It is to prove a scale-uniform version of (PA), then write the
precise finite Halász/Kubilius inequality needed for (UKLO), including all
error terms when both the active primes and their rational weights depend on
\(N\).
