# Exact limits of the nonzero-multiplier graph

Let \(f:\mathbb N\to\mathbb Q\) be completely additive, and put
\[
S_f(N)=\{n\le N:f(n)\ne0\}.
\]
Define the **full nonzero-multiplier graph** \(G_f(N)\) on \([N]\): for every
\(q\) with \(f(q)\ne0\), include every edge \(\{a,aq\}\) for which \(aq\le N\).

## Support and cover lemma

The support \(S_f(N)\) is a vertex cover of \(G_f(N)\). Indeed, if both
endpoints of \(\{a,aq\}\) lay outside the support, then
\[
0=f(aq)=f(a)+f(q)=f(q),
\]
contrary to the definition of an edge.

**Lemma (the \(q\)-chain bound).** If \(f(q)\ne0\), then
\[
|S_f(N)|\ge \lfloor N/q\rfloor.
\]

**Proof.** Partition \([N]\) into the chains
\[
r,rq,rq^2,\ldots\le N\qquad(q\nmid r).
\]
On such a chain the values are \(f(r)+j f(q)\), so at most one vertex has
value zero. There are exactly \(N-\lfloor N/q\rfloor\) chains, since their
initial vertices are the integers not divisible by \(q\). Hence at most that
many vertices lie outside \(S_f(N)\). \(\square\)

The proof uses the arithmetic progression of the actual \(f\)-values; the
corresponding bare graph has much less force.

## A full-matching obstruction at \(\sqrt N\)

Define, on primes,
\[
f_N(p)=\begin{cases}
1,&p>\sqrt N,\\
0,&p\le\sqrt N,
\end{cases}
\]
and extend completely additively. If \(q\le N\) and \(f_N(q)\ne0\), then
\(q\) has a prime divisor exceeding \(\sqrt N\), and hence \(q>\sqrt N\).
Consequently every edge \(\{a,aq\}\) in the **full** graph \(G_{f_N}(N)\)
has \(a\le N/q<\sqrt N\). Thus
\[
\nu(G_{f_N}(N))\le\tau(G_{f_N}(N))\le\lfloor\sqrt N\rfloor,
\]
because \([\lfloor\sqrt N\rfloor]\) covers every edge.

An integer at most \(N\) contains at most one prime exceeding \(\sqrt N\),
and that prime occurs to exponent one. Thus support and level-one fiber
coincide in this example, and
\[
\begin{aligned}
|S_{f_N}(N)|
 &=|\{n\le N:f_N(n)=1\}|\\
 &=\sum_{\sqrt N<p\le N}\left\lfloor\frac Np\right\rfloor\\
 &=(\log 2+o(1))N.
\end{aligned}
\]
The last line follows from the standard reciprocal-prime Mertens estimate;
the total floor error is \(O(\pi(N))=o(N)\). The support therefore has
positive limiting density although the full graph has matching number only
\(O(\sqrt N)\).

## Even support plus cover is too weak

Fix a large constant \(R\), define \(f_R(p)=\mathbf 1_{p>R}\), and extend
completely additively. Let
\[
C_N=[\lfloor N/R\rfloor]\ \cup\
\{n\le N:n\text{ is }R\text{-smooth}\}.
\]
Every zero-support integer is \(R\)-smooth, so lies in \(C_N\). Every
nonzero multiplier \(q\) satisfies \(q>R\); hence every edge \(\{a,aq\}\)
has \(a\le N/q<N/R\), so \(a\in C_N\). Thus \(C_N\) covers the full graph.

For fixed \(R\), the number of \(R\)-smooth integers up to \(N\) is
\(O_R((1+\log N)^{\pi(R)})=o_R(N)\): their exponent vectors have every
coordinate at most \(\log_2N\). Consequently
\[
\frac{|C_N|}{N}\le\frac1R+o_R(1).
\]
Its complement is therefore an independent subset of the support with
density at least \(1-1/R-o_R(1)\).

This behavior is impossible for the genuine level-one fiber. For example,
fix any prime \(p>R\). Every multiple of \(p^2\) has \(f_R(n)\ge2\), so
\[
\limsup_{N\to\infty}\frac{|\{n\le N:f_R(n)=1\}|}{N}
\le 1-\frac1{p^2}<1.
\]
In fact that level has density zero: for primes \(R<p\le T\), a level-one
integer is divisible by at most one of them, whereas the residue density of
integers divisible by at most one is
\[
\prod_{R<p\le T}\left(1-\frac1p\right)
\left(1+\sum_{R<p\le T}\frac1{p-1}\right)=o_{T\to\infty}(1)
\]
by the reciprocal-prime Mertens estimate.

Thus matching cannot prove a constant gap, and even the bare
support-plus-cover relaxation is insufficient. A successful argument must
use higher-order additive consistency beyond pairwise multiplier edges.
