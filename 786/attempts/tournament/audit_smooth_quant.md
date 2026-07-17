# Adversarial audit of the quantitative smooth-number bound

## Verdict

The claimed implication
\[
 m=o(N)\quad\Longrightarrow\quad
 m\ge N\exp\!\left(-(1+o(1))
        \sqrt{\log N\,\log\log N}\right)
\]
is correct. I found no floor/ceiling, prime-counting, binomial, or
asymptotic error that changes the conclusion. Two transitions in
finite_smooth_quantitative.md are terse: the assertion \(Q\ge2k\) needs a
uniform calculation involving the ceiling in \(k\), and the passage from the
quadratic inequality to leading constant \(1\) needs a one-line bootstrap.
Both close as follows.

## 1. Floors and the active-prime cutoff

For an active prime \(p\), the \(p\)-adic-chain argument gives
\[
 m\ge \left\lfloor\frac Np\right\rfloor.
\]
With \(y=\lfloor N/(m+1)\rfloor\), every prime \(p\le y\) satisfies
\[
 p\le \frac N{m+1},\qquad
 \left\lfloor\frac Np\right\rfloor\ge m+1.
\]
It therefore cannot be active. Hence every \(y\)-smooth integer has grading
zero and is outside the level \(f=1\), proving \(m\ge\Psi(N,y)\) with no
off-by-one loss. Also, \(m=o(N)\) implies \(N/(m+1)\to\infty\), so
\(y\to\infty\) and \(L=\log y\) is defined and tends to infinity.

The other exact floor relation is
\[
 y\le \frac N{m+1}<y+1,
\]
so both \(y(m+1)\le N\) and \(m+1>N/(y+1)\) used in the proof have the
correct directions.

## 2. The ceiling in \(k\) and the prime interval

Put \(X=\log N\), assume \(L>2\log X\), and set
\[
 k=\left\lceil\frac XL\right\rceil,
 \qquad t=\log z=\frac Xk.
\]
The lower ceiling inequality \(k\ge X/L\) gives \(t\le L\), hence \(z\le y\).
For the omitted uniform lower estimate, use \(L\le X\) and
\[
 k\le \frac XL+1,
 \qquad
 t\ge \frac{XL}{X+L}.
\]
The last expression is increasing in \(L\); consequently
\[
 t>\frac{2X\log X}{X+2\log X}
   =(2-o(1))\log X,
 \qquad z\ge X^{\,2-o(1)}.
\]
The prime number theorem in dyadic intervals supplies an absolute \(c>0\)
such that, for all sufficiently large \(z\),
\[
 Q=\pi(z)-\pi(z/2)\ge c\frac z{\log z}.
\]
Since \(k\log z=X\), this yields
\[
 \frac Qk\ge c\frac z{k\log z}=c\frac zX
       \ge X^{1-o(1)}\longrightarrow\infty.
\]
Thus \(Q\ge2k\) uniformly in the whole range \(L>2\log X\). This also
verifies that the PNT is being applied with \(z\to\infty\), despite the
\(N\)-dependent choice of \(z\).

## 3. Product count and binomial inequality

Every choice of \(k\) distinct primes from \((z/2,z]\) produces a distinct
integer by unique factorization. All its prime factors are at most
\(z\le y\), and its value is at most \(z^k=N\). Therefore it contributes to
\(\Psi(N,y)\), and the count \(\binom Qk\) has neither collisions nor an
endpoint problem.

The inequality used in (4) is valid for all integers \(Q\ge k\):
\[
 \binom Qk
 =\prod_{j=0}^{k-1}\frac{Q-j}{k-j}
 \ge \prod_{j=0}^{k-1}\frac Qk
 =\left(\frac Qk\right)^k,
\]
because \(Q\ge k\) implies \((Q-j)/(k-j)\ge Q/k\).

## 4. Error terms and the leading constant

Writing the lower bounds with a fixed constant rather than a signed
\(O\)-term, there is an absolute \(C\) such that
\[
 \begin{aligned}
 \log\binom Qk
 &\ge k(\log z-\log\log z-\log k-C)\\
 &=X-k\log X-Ck,
 \end{aligned}
\]
where the identity is exact because \(k\log z=X\). Since
\(k\le X/L+1\),
\[
 \log\binom Qk
 \ge X-\frac{X\log X}{L}
      -O\!\left(\log X+\frac XL\right).
\]
Now
\[
 X-L\ge\log(m+1)\ge\log m
       \ge\log\Psi(N,y)\ge\log\binom Qk,
\]
so
\[
 L^2\le X\log X+O(L\log X+X). \tag{A}
\]
Let \(S=\sqrt{X\log X}\) and \(u=L/S\). Dividing (A) by \(S^2\) gives
\[
 u^2\le1+O\!\left(u\sqrt{\frac{\log X}{X}}
                       +\frac1{\log X}\right).
\]
Solving this quadratic inequality (so no prior boundedness assumption on
\(u\) is needed) gives \(u\le1+o(1)\). Hence
\[
 L\le(1+o(1))\sqrt{X\log X}.
\]
In the complementary range \(L\le2\log X\), this is immediate because
\(2\log X=o(\sqrt{X\log X})\).

## 5. Conversion from \(y\) to \(m\)

Because \(y\to\infty\),
\[
 \log(y+1)=L+\log(1+1/y)=L+o(1)
 \le(1+o(1))S.
\]
The exact floor inequality \(N/(m+1)<y+1\) therefore implies
\[
 \log(m+1)\ge X-(1+o(1))S.
\]
The right-hand side tends to infinity like \(X\), so this estimate itself
implies \(m\to\infty\). Replacing \(m+1\) by \(m\) changes its logarithm by
\(o(1)=o(S)\). Thus
\[
 \log m\ge X-(1+o(1))S,
\]
which is exactly the stated lower bound.

## Certification

Conditional only on the standard prime number theorem (and the already
proved exact additive grading/active-chain lemma), the quantitative bound is
certified. The two terse points above require exposition, not a weaker
constant or a repair lemma.
