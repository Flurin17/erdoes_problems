# Torus \(L^1\) rearrangement for geometric prime factors

This note audits a proposed Fourier estimate and, in particular, checks
whether lacunary integer weights can create enough major arcs to violate it.
They cannot.  The reason is an exact multiproduct rearrangement inequality;
it controls the total measure of all spikes, not merely the spike at the
origin.

Throughout, \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) has normalized Haar
measure \(m(dt)=dt/(2\pi)\).  Let \(P\) be a finite set of primes, let
\(a_p\in\mathbb Z\setminus\{0\}\), and put

\[
 q_p=\frac1p,\qquad H=\sum_{p\in P}q_p.
\]

The exact geometric characteristic function is

\[
 \Phi_{P,\mathbf a}(t)
 =\prod_{p\in P}\frac{1-q_p}{1-q_p e^{i a_p t}}.
 \tag{1}
\]

We prove

\[
 \|\Phi_{P,\mathbf a}\|_{L^1(\mathbb T)}
 \le e^{-H}I_0(H)
 \ll H^{-1/2},
 \tag{2}
\]

uniformly in the nonzero integer weights.  Here

\[
 I_0(H)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{H\cos t}\,dt.
\]

The same estimate holds for the simpler Halasz integrand

\[
 K_{P,\mathbf a}(t)
 =\exp\!\left(-\sum_{p\in P}q_p(1-\cos(a_p t))\right).
 \tag{3}
\]

Moreover, both the exponent \(1/2\) and the leading constant in (2) are
asymptotically sharp.

## 1. Exact multiproduct rearrangement

For \(0<q\le 1/2\), define

\[
 g_q(t)=\frac{1-q}{|1-qe^{it}|}
 =\left(1+\frac{2q(1-\cos t)}{(1-q)^2}\right)^{-1/2}.
 \tag{4}
\]

On \([0,\pi]\), this is nonincreasing.  Consequently every strict
superlevel set \(\{g_q>s\}\) is, up to null endpoints, either empty, all of
\(\mathbb T\), or an arc centered at \(0\).

We use the following elementary form of the many-function rearrangement
inequality.

**Lemma 1.**  If \(q_1,\ldots,q_r\in(0,1/2]\) and
\(a_1,\ldots,a_r\in\mathbb Z\setminus\{0\}\), then

\[
 \int_{\mathbb T}\prod_{j=1}^r g_{q_j}(a_jt)\,dm(t)
 \le
 \int_{\mathbb T}\prod_{j=1}^r g_{q_j}(t)\,dm(t).
 \tag{5}
\]

**Proof.**  The map \(t\mapsto a_jt\) preserves normalized Haar measure, so
for every \(s_j\ge0\),

\[
 m\{t:g_{q_j}(a_jt)>s_j\}
 =m\{t:g_{q_j}(t)>s_j\}.
 \tag{6}
\]

Layer cake and Tonelli give

\[
 \int_{\mathbb T}\prod_{j=1}^r g_{q_j}(a_jt)\,dm(t)
 =\int_{[0,\infty)^r}
 m\!\left(\bigcap_{j=1}^r
 \{g_{q_j}(a_jt)>s_j\}\right)d\mathbf s.
 \tag{7}
\]

For fixed \(\mathbf s\), the intersection in (7) has measure at most

\[
 \min_j m\{g_{q_j}>s_j\}.
 \tag{8}
\]

In the aligned case on the right of (5), the corresponding superlevel sets
are all arcs centered at zero.  Such arcs are nested by their lengths, so
their intersection has measure exactly the minimum in (8).  Comparing the
layer-cake integrands proves (5).  \(\square\)

The proof also applies verbatim to any collection of nonnegative functions
whose superlevel sets are centered arcs.  In particular, with

\[
 k_q(t)=e^{-q(1-\cos t)},
\]

it gives

\[
 \int_{\mathbb T}K_{P,\mathbf a}(t)\,dm(t)
 \le \int_{\mathbb T}e^{-H(1-\cos t)}\,dm(t)
 =e^{-H}I_0(H).
 \tag{9}
\]

This is the precise reason that the numerous rational spikes created by
lacunary weights do not help: at every tuple of layer thresholds, their
union-of-arcs superlevel sets have no larger common intersection than the
single aligned arcs.

## 2. Comparison of the geometric factor with the Halasz factor

**Lemma 2.**  For \(0<q\le1/2\) and every \(t\in\mathbb T\),

\[
 g_q(t)\le e^{-q(1-\cos t)}.
 \tag{10}
\]

**Proof.**  Put \(y=1-\cos t\in[0,2]\) and

\[
 F_q(y)=\frac12\log\!\left(1+\frac{2qy}{(1-q)^2}\right)-qy.
 \tag{11}
\]

The function \(F_q\) is concave in \(y\).  Its endpoint values are

\[
 F_q(0)=0,
 \qquad
 F_q(2)=\log\frac{1+q}{1-q}-2q
 =2(\operatorname{arctanh}q-q)\ge0.
 \tag{12}
\]

A concave function lies above its endpoint chord, hence \(F_q(y)\ge0\) on
\([0,2]\).  By (4), this is exactly (10).  \(\square\)

Applying (10) factorwise in (1), and then applying (9), proves the first
inequality in (2).  Alternatively, Lemma 1 first aligns the exact geometric
factors and (10) then bounds their aligned product.

## 3. Elementary \(H^{-1/2}\) estimate

For \(|t|\le\pi\),

\[
 1-\cos t\ge\frac{2t^2}{\pi^2}.
\]

Therefore

\[
 e^{-H}I_0(H)
 \le\frac1{2\pi}\int_{-\infty}^{\infty}
 e^{-2Ht^2/\pi^2}\,dt
 =\sqrt{\frac{\pi}{8H}}.
 \tag{13}
\]

This proves (2) with a completely elementary absolute constant.  Conversely,
using \(1-\cos t\le t^2/2\) and integrating over
\(|t|\le H^{-1/2}\), for \(H\ge1\) one gets

\[
 e^{-H}I_0(H)\ge \frac{e^{-1/2}}{\pi\sqrt H}.
 \tag{14}
\]

Thus the aligned simpler integrand already has exact order \(H^{-1/2}\).
The standard one-dimensional Laplace estimate gives the sharper asymptotic

\[
 e^{-H}I_0(H)\sim\frac1{\sqrt{2\pi H}}.
 \tag{15}
\]

## 4. Sharpness for the exact geometric characteristic

The geometric factors can approximate the simpler integrand uniformly when
the active primes are large.  If \(q\le1/4\), the proof of Lemma 2 and
\(\log(1+x)\le x\) give, uniformly for \(y\in[0,2]\),

\[
 0\le -\log g_q(t)-qy
 \le qy\big((1-q)^{-2}-1\big)
 \le 8q^2.
 \tag{16}
\]

Consequently, if every active prime is at least \(5\), all weights are
\(a_p=1\), and \(S_2=\sum_{p\in P}p^{-2}\), then pointwise

\[
 e^{-8S_2}e^{-H(1-\cos t)}
 \le \prod_{p\in P}g_{1/p}(t)
 \le e^{-H(1-\cos t)}.
 \tag{17}
\]

For an explicit asymptotic family, let \(R\to\infty\), set \(Y=R^3\), and
take the first finite set of primes greater than \(Y\) whose reciprocal sum
is at least \(R\).  The divergence of \(\sum_p1/p\) ensures that this is
possible.  Minimality gives

\[
 H=R+O(R^{-3}),
 \qquad
 S_2\le Y^{-1}H=O(R^{-2}).
 \tag{18}
\]

Integrating (17), then using (15), yields

\[
 \|\Phi_{P,\mathbf 1}\|_1
 =(1+o(1))e^{-H}I_0(H)
 \sim\frac1{\sqrt{2\pi H}}.
 \tag{19}
\]

Hence no universal improvement to \(o(H^{-1/2})\) is possible, and the
leading constant in the upper comparison with \(e^{-H}I_0(H)\) is also
sharp.  Lacunary weights can split the aligned peak into many major arcs,
but Lemma 1 shows that they cannot increase its total \(L^1\) mass.
