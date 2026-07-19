# Anchored Fourier and discrepancy route

## Status

This route gives exact phase-sensitive formulas and rigorous discrepancy bounds, but it does **not** presently locate the first admissible integer at the conjectural scale. Its precise obstruction is the sparse-support, high-conductor Fourier tail. In particular, density or magnitude information alone cannot exploit the prescribed anchor \(2k\).

## Setup and exact residue model

Let

\[
 \mathcal P=\{p:k<p<2k,\ p\text{ prime}\},\qquad
 q_p=p-k,
\]

and put

\[
 P=\prod_{p\in\mathcal P}p,\qquad
 M=\prod_{p\in\mathcal P}q_p,\qquad
 \delta=M/P.
\]

The allowed residues modulo \(p\) are

\[
 A_p=\{0,k+1,\ldots,p-1\}=\{-j:0\le j<q_p\}\pmod p.
\]

Thus

\[
 g(n)=\prod_{p\in\mathcal P}1_{A_p}(n\bmod p)
\]

is the indicator that none of \(n-k,\ldots,n-1\) is divisible by a prime in \((k,2k)\). The anchored counting function is

\[
 A_k(H)=\sum_{h=1}^H g(2k+h).
\]

There are exactly \(M\) allowed residue classes modulo \(P\), so the period density is exactly \(\delta\).

Throughout, \(e(x)=e^{2\pi i x}\) and \(D_H(\theta)=\sum_{h=1}^H e(h\theta)\).

Equivalently, in the product group

\[
 G=\prod_{p\in\mathcal P}\mathbb Z/p\mathbb Z,\qquad
 \mathcal B=\prod_{p\in\mathcal P}A_p,
\]

the CRT diagonal orbit is

\[
 \Phi(n)=(n\bmod p)_{p\in\mathcal P},
\qquad
 A_k(H)=\#\{1\le h\le H:\Phi(2k+h)\in\mathcal B\}.
\]

Thus the admissible set is literally a product box of cyclic arcs, but the sampled orbit is one-dimensional and anchored. Its box transform factorizes:

\[
 \widehat{1_{\mathcal B}}(\mathbf a)
 =\prod_{p\in\mathcal P}\frac{F_p(a_p)}p.
\]

## Exact tuple Fourier formula

For \(a\in\mathbb Z/p\mathbb Z\), define

\[
 F_p(a)=\sum_{j=0}^{q_p-1}e(aj/p).
\]

Fourier inversion on every local factor gives

\[
 \boxed{
 A_k(H)=H\delta+
 \sum_{\mathbf a\ne\mathbf0}
 \left(\prod_{p\in\mathcal P}\frac{F_p(a_p)}p\right)
 e(2k\theta(\mathbf a))D_H(\theta(\mathbf a)),
 }
 \tag{1}
\]

where

\[
 \theta(\mathbf a)=\sum_{p\in\mathcal P}\frac{a_p}{p}\pmod1.
\]

No nonzero tuple has integral \(\theta\): if \(p\) is in its support, multiplying by the product of the support primes and reducing modulo \(p\) leaves a nonzero term.

For \(1\le a<p\), the geometric sums are

\[
 F_p(a)=e\!\left(\frac{a(q_p-1)}{2p}\right)
 \frac{\sin(\pi a q_p/p)}{\sin(\pi a/p)},
\]

and

\[
 D_H(\theta)=e((H+1)\theta/2)
 \frac{\sin(\pi H\theta)}{\sin(\pi\theta)}.
\]

Consequently (1) records the explicit anchored phases. Pairing \(\mathbf a\) and \(-\mathbf a\) makes the reality of the sum manifest. These phases must not be discarded.

## Equivalent one-dimensional cyclic formula

Let \(B_p=(P/p)^{-1}\pmod p\) and

\[
 S(\ell)=\sum_{r\bmod P}g(r)e(-\ell r/P).
\]

CRT factorization gives

\[
 S(\ell)=\prod_{p\in\mathcal P}F_p(\ell B_p\bmod p),
 \qquad S(0)=M,
\]

and hence

\[
 \boxed{
 A_k(H)-H\delta=
 \frac1P\sum_{\ell=1}^{P-1}S(\ell)e(2k\ell/P)D_H(\ell/P).
 }
 \tag{2}
\]

For \(H=tP+r\), the discrepancy is exactly the discrepancy of the final \(r\) terms, so it suffices to study \(0\le H<P\).

At the period scale this already gives an explicit, unconditional anchored upper bound:

\[
 A_k(P)=M>0,\qquad n_k\le 2k+P.
\]

Equivalently, the least multiple of \(P\) exceeding \(2k\) is admissible and is at most \(2k+P\). By PNT,

\[
 \log P=\vartheta(2k)-\vartheta(k)=(1+o(1))k,
\]

so \(n_k\le \exp((1+o(1))k)\). This is far above the reciprocal-density prediction.

## A proved local coefficient lemma

For \(1\le q\le(p-1)/2\),

\[
 \max_{a\ne0\bmod p}
 \left|\sum_{j=0}^{q-1}e(aj/p)\right|
 =\frac{\sin(\pi q/p)}{\sin(\pi/p)}.
 \tag{3}
\]

Proof. By symmetry take \(x=\pi a/p\in[\pi/p,\pi/2]\). On \(x<\pi/q\), the ratio \(\sin(qx)/\sin x\) decreases because \(x\cot x\) is strictly decreasing. On \(x\ge\pi/q\), the ratio is at most \(\csc(\pi/q)\le q/2\), whereas its value at \(a=1\) is at least \(2q/\pi>q/2\). The case \(q=1\) is immediate. \(\square\)

Define

\[
 R_p=\frac{\sin(\pi q_p/p)}{q_p\sin(\pi/p)},
 \qquad \lambda_p=-\log R_p,
 \qquad \Lambda=\sum_{p\in\mathcal P}\lambda_p.
\]

Then \(2/\pi\le R_p\le1\), and (3) yields

\[
 \frac{|S(\ell)|}{M}
 \le\prod_{p\nmid\ell}R_p
 =\exp\!\left(-\Lambda+\sum_{p\mid\ell}\lambda_p\right).
 \tag{4}
\]

In particular,

\[
 \frac{|S(\ell)|}{M}
 \le \min\left\{1,
 \exp\!\left[-\Lambda+
 \log(\pi/2)\frac{\log\ell}{\log(k+1)}\right]
 \right\}.
 \tag{5}
\]

The ordinary PNT applied to the continuous weight in (3) gives

\[
 \Lambda=(C_F+o(1))\frac{k}{\log k},
\]

where

\[
 C_F=\int_1^2-log\!\left(
 \frac{\sin(\pi(1-1/t))}{\pi(1-1/t)}
 \right)dt>0.
\]

Unlike the density weight below, this integrand extends continuously to \(t=1\).

## Phase-aware Selberg--Vaaler sandwich

Apply degree-\(L\) Selberg minorants and majorants to the half-open arc

\[
 I=(2k/P,(2k+H)/P].
\]

They give an exact sandwich

\[
 \sum_{|\ell|\le L}\widehat T_L^-(\ell)S(-\ell)
 \le A_k(H)\le
 \sum_{|\ell|\le L}\widehat T_L^+(\ell)S(-\ell),
 \tag{6}
\]

where endpoints may be shifted infinitesimally to count the half-open lattice arc exactly,

\[
 \widehat T_L^\pm(0)=H/P\pm1/(L+1),
\]

and, for \(0<|\ell|\le L\),

\[
 \widehat T_L^\pm(\ell)=
 e\!\left(-\frac{\ell(2k+H/2)}P\right)
 \frac{\sin(\pi\ell H/P)}{\pi\ell}+E_\ell^\pm,
 \qquad |E_\ell^\pm|\le\frac1{L+1}.
\]

Formula (6), before absolute values, is the strongest proved phase-sensitive truncated statement in this route.

Applying the triangle inequality only after (6), and using (4), gives the rigorous anchored discrepancy bound

\[
 \boxed{
 |A_k(H)-H\delta|
 \le \frac{M}{L+1}
 +2M\sum_{\ell=1}^L
 \left(\frac1{L+1}+\min\{H/P,1/(\pi\ell)\}\right)
 \exp\!\left(-\Lambda+\sum_{p\mid\ell}\lambda_p\right).
 }
 \tag{7}
\]

The exponential is to be capped at \(1\). If

\[
 \rho_L=\min\{1,\exp[-\Lambda+\log(\pi/2)\log L/\log(k+1)]\},
\]

then a convenient corollary is

\[
 |A_k(H)-H\delta|
 \ll M\left[L^{-1}+\rho_L\{1+\log^+(LH/P)\}\right].
 \tag{8}
\]

Thus all frequencies \(L=\exp(o(k))\) are exponentially attenuated. This does not reach the required spatial resolution.

## Density scale, with endpoint warning

One expects the reciprocal-density scale because

\[
 \log\delta=\sum_{k<p<2k}\log(1-k/p)
 =-(2\log2+o(1))\frac{k}{\log k}.
 \tag{9}
\]

Indeed

\[
 \int_1^2\log(1-1/t)\,dt=-2\log2.
\]

The integrand is singular at \(t=1\), so bounded-test-function PNT alone does not justify (9). A rigorous proof first applies PNT on \(p\ge(1+\varepsilon)k\), then controls \(p-k<\varepsilon k\) in dyadic shells by Brun--Titchmarsh; shells shorter than \(k^{1/2}\) contribute \(o(k/\log k)\) trivially. Letting \(\varepsilon\downarrow0\) proves (9).

Thus the density heuristic predicts

\[
 H_* =\delta^{-1+o(1)}
 =\exp\!\left((\log4+o(1))\frac{k}{\log k}\right).
\]

This remains a heuristic for the *anchored* first representative.

## Why magnitude-only arguments fail

1. **Translation obstruction.** Translating every \(A_p\) by the same integer \(t\) preserves all local and global Fourier magnitudes, but replaces \(g(n)\) by \(g(n-t)\). Hence magnitude-only data cannot distinguish the anchor \(2k\). Any such proof would actually establish a uniform maximum-gap theorem. Since there are only \(M=\delta P\) allowed points on the cyclic period, some cyclic zero block has length at least \(\lceil\delta^{-1}\rceil-1\), and a common translation can place this block at any desired anchor.

2. **Parseval is period-scale.** Centering both the interval and \(g\) gives

\[
 |A_k(H)-H\delta|
 \le\sqrt{PH\delta(1-\delta)(1-H/P)}.
\]

Main-term domination requires \(H>P(1-\delta)\), essentially a full period, whereas the target is \(H=\exp(O(k/\log k))\) and \(\log P=(1+o(1))k\).

3. **Near-zero CRT resonance.** A tuple can have all local frequencies nonzero yet satisfy \(\theta=1/P\). Then \(D_H(\theta)\sim H\) for \(H=o(P)\). The statement that every nonzero local mode oscillates once \(H\gg k\) is therefore false.

4. **Resolution versus attenuation.** To resolve an interval of length \(H\), (6) needs \(L\gtrsim P/H=\exp(k-o(k))\). At such frequencies, \(\ell\) can be divisible by nearly every prime, erasing the attenuation in (4).

5. **Sparse-support conductor barrier.** A character supported on primes in \(S\) has exact conductor \(d_S=\prod_{p\in S}p\). If \(d_S\asymp H_*\), then

\[
 |S|=O(\log H_*/\log k)=O(k/\log^2k),
\]

only \(o(|\mathcal P|)\) coordinates. Such a mode may have frequency \(1/d_S\), so its Dirichlet kernel is nonoscillatory at scale \(H_*\); choosing support primes just above \(k\) also makes the normalized local coefficients close to \(1\).

6. **Low-conductor truncation misses the density mechanism.** At target scale, conductors \(d\le H_*\) involve only \(o(k/\log k)\) primes, while \(\log\delta\) is accumulated across \(\asymp k/\log k\) restrictions.

7. **Averaging changes the question.** Second moments over the starting point can prove a result for most or some anchors, but do not control the fixed anchor \(2k\).

## Closed low-support calculation

Put $q_p=p-k$, and define the centered shifted factor
\[
 F_p(h)=\frac{p}{q_p}1_{\{q_p+1,\ldots,2q_p\}}(h\bmod p)-1.
\]
It has period $p$, mean zero, and local $L^1$ mass $2k$.  In the exact ANOVA
expansion, the total contribution $T_s$ from characters supported on exactly
$s$ primes satisfies
\[
 |T_s|\le \delta,2^{s-1}k^s\binom{m}{s},
 \qquad m=|\mathcal P|.                              \tag{11}
\]
For a fixed support $S$, the product $\prod_{p\in S}F_p(h)$ has mean zero
modulo $d_S=\prod_{p\in S}p$; complete periods cancel, and a prefix has
absolute signed mass at most half its full $L^1$ mass $(2k)^s$.

For support one, if $t_p=H\bmod p$ and
$J_q(t)=\max(0,\min(t,2q)-q)$, then exactly
\[
 T_1=\delta\sum_{p\in\mathcal P}
 \left(\frac{p}{q_p}J_{q_p}(t_p)-t_p\right),
 \qquad |T_1|\le\delta km.
\]
For support two, every fixed pair contributes at most $2k^2$, giving
$|T_2|\le2\delta k^2\binom m2$.  Thus, at
$H=\exp(Ck/\log k)$, every fixed support size is $o(H\delta)$; (11) first
loses force at support of order $k/\log^2k$.  Fixed-order correlations cannot
decide the conjectural scale.

## High-conductor energy obstruction

For exact support conductor $d\mid P$, local Parseval gives
\[
 \sum_{(b,d)=1}|c_d(b)|^2
 =\delta^2\prod_{p\mid d}\frac{k}{p-k}.              \tag{12}
\]
When $H=\exp(O(k/\log k))$, every $d\le H$ has
$O(k/\log^2k)$ prime factors.  Since the positive offsets $p-k$ are distinct,
(12) implies that the total energy below $H$ is
$\delta^2\exp(o(k/\log k))$, whereas total Fourier energy is $\delta$.
Consequently
\[
 \sum_{d>H}\sum_{(b,d)=1}|c_d(b)|^2=(1-o(1))\delta.  \tag{13}
\]

For $H<d$, orthogonality gives
$\sum_{b\bmod d}|D_H(b/d)|^2=dH$.  Blockwise Cauchy--Schwarz therefore yields
only
\[
 |T_d|\le
 \delta\sqrt{dH\prod_{p\mid d}\frac{k}{p-k}},        \tag{14}
\]
which already loses a factor containing $\sqrt{d/H}$.  Equations (13)--(14)
close the ordinary conductor-orthogonality and $L^2$ large-sieve nodes:
almost all energy lies exactly where these norms lose spatial resolution.

## Required phase-sensitive repair and dependency graph

Write the exact signed remainder from (1) as \(R_{2k}(H)\), so

\[
 A_k(H)=\delta H+R_{2k}(H).
\]

The literal weakest existence lemma is \(R_{2k}(H)>-\delta H\). At the conjectural scale, put \(m=k/\log k\) and

\[
 H_\pm=\exp((\log4\pm\varepsilon)m).
\]

A robust sufficient pair would be

\[
 A_k(H_-)\le e^{o(m)}\delta H_-,
 \qquad
 A_k(H_+)\ge e^{-o(m)}\delta H_+.
 \tag{10}
\]

By (9) and integrality, (10) would imply \(A_k(H_-)=0\) and \(A_k(H_+)>0\), hence

\[
 \log(n_k-2k)\sim(\log4)k/\log k.
\]

The dependency graph is

\[
 \text{residue equivalence}
 \longrightarrow \text{exact phased Fourier identity}
 \longrightarrow
 \begin{cases}
 \text{density asymptotic (9)},\\
 \text{signed lower-scale estimate in (10)},\\
 \text{signed upper-scale estimate in (10)}
 \end{cases}
 \longrightarrow \text{sharp logarithmic asymptotic}.
\]

The two signed estimates are open. The most concrete next attempt is to group complete Fourier blocks by their support conductor before taking absolute values, split at \(d\le H\) and \(d>H\), and seek collective cancellation in the \(d>H\) tail. The latter is the exact bottleneck: individual terms there need not oscillate, so cancellation must come from their full anchored phases, not from Dirichlet-kernel magnitudes.

## Falsification tests for any proposed closure

- Translate all local allowed arcs by a common \(t\). If the proof is unchanged, it proves a uniform max-gap result and must be checked against the translation obstruction.
- Test the CRT character with frequency \(1/P\); any claim that all nonzero modes oscillate must handle it.
- At a proposed \(H\), enumerate support conductors \(d\asymp H\) with primes closest to \(k\), where normalized coefficients are largest.
- Verify that any use of (9) controls the singular \(p\downarrow k\) endpoint rather than applying a bounded-weight PNT illegally.
- Keep the factors \(e(2k\theta)\), the arguments of \(F_p(a)\), and the sign of \(D_H(\theta)\) until after conductor blocks are summed.
