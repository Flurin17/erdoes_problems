# Quantitative smooth-number deletion bound

Let \(A\subset[1,N]\) be repetition-allowed PLR, let \(m=N-|A|\), and assume
\(m=o(N)\). The active-prime chain lemma gives
\[
 m\geq\Psi(N,y),\qquad
 y=\left\lfloor\frac{N}{m+1}\right\rfloor. \tag{1}
\]
This note extracts a uniform quantitative consequence of (1).

## Theorem

As \(N\to\infty\),
\[
 m\geq
 N\exp\!\left(-(1+o(1))
 \sqrt{\log N\,\log\log N}\right). \tag{2}
\]

## Proof

Put
\[
 X=\log N,\qquad L=\log y.
\]
If \(L\leq2\log X\), then the claimed upper bound
\[
 L\leq(1+o(1))\sqrt{X\log X} \tag{3}
\]
is immediate. Assume \(L>2\log X\), and set
\[
 k=\left\lceil\frac XL\right\rceil,\qquad
 z=N^{1/k}.
\]
Then \(z\leq y\), because \(k\geq X/L\). Every product of \(k\) distinct
primes at most \(z\) is \(y\)-smooth and at most \(z^k=N\).

Use only primes in \((z/2,z]\). By the prime number theorem,
\[
 Q:=\pi(z)-\pi(z/2)\geq c\frac z{\log z}
\]
for all sufficiently large \(N\), with an absolute \(c>0\). Here
\(\log z=X/k\), and the assumption \(L>2\log X\) ensures \(Q\geq2k\).
Unique factorization therefore gives
\[
 \Psi(N,y)\geq\binom Qk\geq\left(\frac Qk\right)^k. \tag{4}
\]
Since \(k\log z=X\), we have
\(\log\log z+\log k=\log(k\log z)=\log X\), and hence
\[
 \begin{aligned}
 \log\binom Qk
 &\geq k\bigl(\log z-\log\log z-\log k+O(1)\bigr)\\
 &=X-k\log(k\log z)+O(k)\\
 &=X-k\log X+O(k)\\
 &\geq X-\frac{X\log X}{L}-O\!\left(\log X+\frac XL\right). \tag{5}
 \end{aligned}
\]
The definition of \(y\) gives \(y(m+1)\leq N\), hence
\[
 \log(m+1)\leq X-L. \tag{6}
\]
Combining (1), (5), and (6) yields
\[
 L\leq\frac{X\log X}{L}
 +O\!\left(\log X+\frac XL\right).
\]
Multiplying by \(L\),
\[
 L^2\leq X\log X+O(L\log X+X).
\]
Together with the already trivial range \(L\leq2\log X\), this proves (3).

Finally, because \(y=\lfloor N/(m+1)\rfloor\),
\[
 m+1>\frac{N}{y+1}.
\]
Using (3) gives
\[
 \log\frac{N}{m+1}
 \leq\log(y+1)
 \leq(1+o(1))\sqrt{X\log X},
\]
which is (2).

## Scope

The prime number theorem is the only standard external input in this
quantitative extraction. The result still allows a sublinear exceptional set,
so it does not decide the finite question.
