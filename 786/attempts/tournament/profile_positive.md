# Tournament route: a rounded-log scale gradient, and its exact-atom failure

## Proposed mechanism

The most direct way to exploit the fact that a uniformly chosen integer
`n <= N` has `log n / log N = 1-o(1)` is to approximate the completely
additive function `log n / log N` by a rational, finitely valued grading.
Let
\[
 L=\log N,\qquad K=\lfloor\log\log N\rfloor
\]
(changing (K) to (3) for the finitely many small (N) is harmless), and
give a prime (p\leq N) the rational weight
\[
 w_N(p)=\frac1K\left\lfloor\frac{K\log p}{L}\right\rfloor . \tag{1}
\]
Thus there are (K+O(1)) prime bands, the primes up to
(N^{1/K}) have weight zero, and the weights then increase by (1/K) at
each power (N^{j/K}).  Put
\[
 f_N(n)=\sum_p w_N(p)v_p(n),\qquad
 F_N(n)=Kf_N(n)\in\mathbb Z. \tag{2}
\]
This is a genuine rational completely additive grading, so every nonzero
exact level of (F_N) is repetition-allowed PLR.

At coarse resolution this looks promising: (F_N(n)) is close to (K) for
most (n\leq N).  The result below shows that this appearance is deceptive.
The rounding errors from the growing number of logarithmic bands are
equidistributed modulo a slowly growing modulus.  Consequently **every
exact atom has density tending to zero**.  This gives a rigorous failure
mechanism for this natural positive family, not an obstruction to arbitrary
rational prime weights.

## Result for the family

Let
\[
 M_N=\max_{c\in\mathbb Z\setminus\{0\}}
       \frac1N|\{n\leq N:F_N(n)=c\}|.
\]
Then, with (K=\lfloor\log\log N\rfloor),
\[
 \frac{c_0}{\log K}\ \leq\ M_N\
 \ \ll\ (\log K)^{-1/4}. \tag{3}
\]
In particular (M_N=o(1)), rather than (1-o(1)).  The lower bound in
(3) only records the genuine coarse concentration which motivated the
construction; no optimal local-limit estimate is claimed.

The upper bound uses the standard quantitative Halasz mean-value theorem.
All of the problem-specific estimates needed to invoke it are proved below.

## Lemma 1: coarse concentration and a nonzero atom

For (n\leq N), define the nonnegative rounding defect
\[
 R_N(n)=\frac{K\log n}{L}-F_N(n)
 =\sum_{p\leq N}
   \left\{\frac{K\log p}{L}\right\}v_p(n). \tag{4}
\]
Then
\[
 \frac1N\sum_{n\leq N}R_N(n)
   =\frac12\log K+O(1), \tag{5}
\]
and hence
\[
 \frac1N\sum_{n\leq N}(K-F_N(n))
   =\frac12\log K+O(1). \tag{6}
\]

### Proof

For a prime (p\),
\[
 \frac1N\sum_{n\leq N}v_p(n)
 =\sum_{a\geq1}\frac1N\left\lfloor\frac N{p^a}\right\rfloor
 =\frac1{p-1}+o(1)
\]
after summing the errors over all (p\leq N).  The last summed error is
(o(1)) by the prime number theorem.  Therefore the mean in (5) is
\[
 \sum_{p\leq N}
 \frac{\{K\log p/L\}}{p-1}+o(1). \tag{7}
\]
Replacing (p-1) by (p) costs (o(1)): below (N^{1/K}) the numerator
is (K\log p/L), and above that point the primes themselves tend to
infinity.  Mertens partial summation transforms (7) into
\[
 \int_{K\log2/L}^{K}\frac{\{u\}}u\,du+O(1). \tag{8}
\]
The interval (0<u<1) contributes (1+o(1)), while, for (j\geq1),
\[
 \int_j^{j+1}\frac{u-j}{u}\,du
 =1-j\log(1+1/j)=\frac1{2j}+O(j^{-2}).
\]
Summing proves (5).

Moreover
\[
 K-F_N(n)=\frac{K\log(N/n)}L+R_N(n). \tag{9}
\]
The average of the first term is (K/L+o(K/L)=o(1)), by Stirling's
formula, proving (6).  Since (0\leq F_N(n)\leq K), Markov's inequality
shows that a fixed positive proportion of the integers have
\[
 K-C\log K\leq F_N(n)\leq K
\]
for an absolute (C).  These are (O(\log K)) integer levels, and their
lower endpoint is positive for large (N).  Pigeonholing proves the lower
bound in (3).  \(\square\)

## Lemma 2: the modular sawtooth is non-pretentious

For completely multiplicative unit-modulus functions (g,h), write
\[
 \mathbb D_N(g,h)^2
 =\sum_{p\leq N}\frac{1-\Re(g(p)\overline{h(p)})}{p}. \tag{10}
\]
Let (2\leq q\leq(\log K)^{1/4}), (1\leq a<q), and
\[
 g_{a,q}(n)=\exp(2\pi i aF_N(n)/q). \tag{11}
\]
There is an absolute (c>0) such that, uniformly in these (a,q),
\[
 \min_{|t|\leq K}\mathbb D_N(g_{a,q},n^{it})^2
 \geq c\frac{\log K}{q^2}. \tag{12}
\]

### Proof

Set \(\theta=2\pi a/q\).  Mertens' theorem, uniformly over the bands
\((N^{j/K},N^{(j+1)/K}]\), gives
\[
 \begin{aligned}
 \mathbb D_N(g_{a,q},1)^2
 &=\sum_{j=1}^{K-1}(1-\cos(\theta j))
       \log(1+1/j)+o(1)\\
 &=\log K-\Re\sum_{j<K}\frac{e^{i\theta j}}j+O(1).
 \end{aligned} \tag{13}
\]
The elementary geometric-sum estimate
\[
 \left|\sum_{j<K}\frac{e^{i\theta j}}j\right|
 \leq C+\log q
\]
therefore yields, uniformly in the displayed range of (q),
\[
 \mathbb D_N(g_{a,q},1)^2\geq(1-o(1))\log K. \tag{14}
\]
For completeness, the uniform Mertens error in (13) is (o(1)): the
standard PNT form
\(sum_{p\leq x}p^{-1}=\log\log x+B+O(1/\log x)\)
gives total band error
\(O(K\log K/L)=o(1)\).

We use two standard elementary estimates for the archimedean twists:
for (|u|\leq1),
\[
 \mathbb D_N(1,n^{iu})^2
 =\int_{\log2}^{L}\frac{1-\cos(uv)}v\,dv+O(1), \tag{15}
\]
and, uniformly for (1\leq|u|\leq K(\log K)^{1/4}),
\[
 \mathbb D_N(1,n^{iu})^2
 \geq \log\log N-O(\log\log(3+|u|)). \tag{16}
\]
Equation (15) is Mertens partial summation.  Equation (16) follows by
comparing the prime sum with
\(\log\zeta(1+1/L+iu)\) and using the classical bound
\(|\zeta(\sigma+iu)|\ll\log(3+|u|)\) away from the pole.  Only the much
weaker consequence that (16) is \(\gg K\) in the stated range is used.

Now let (d=\mathbb D_N(g_{a,q},n^{it})\), with (|t|\leq K).  Since
(g_{a,q}^q=1), the pointwise inequality
\(|z^q-w^q|\leq q|z-w|\) on the unit circle gives
\[
 \mathbb D_N(1,n^{iqt})\leq qd. \tag{17}
\]
Suppose, for a sufficiently small absolute \(\delta>0\), that
\[
 d<\frac{\delta}{q}\sqrt{\log K}. \tag{18}
\]
Then (16) and (17) first force (|qt|<1), since
(K\gg\log K).  From (15), applied at (t) and (qt), one has
\[
 \mathbb D_N(1,n^{it})^2
 \leq \mathbb D_N(1,n^{iqt})^2+O(1+\log q)
 \leq \delta^2\log K+o(\log K). \tag{19}
\]
Indeed the integral in (15) is (O(1)) while (|u|L\leq2), and is
\(\log(|u|L)+O(1)\) afterward; replacing (u) by (qu) can only increase
this logarithmic main term, up to (O(1)).

The triangle inequality for \(\mathbb D_N\), (18), and (19) now give
\[
 \mathbb D_N(g_{a,q},1)
 \leq\mathbb D_N(g_{a,q},n^{it})+
       \mathbb D_N(n^{it},1)
 \leq (2\delta+o(1))\sqrt{\log K},
\]
contradicting (14) when \(\delta\) is fixed sufficiently small.  Thus
(d\gg q^{-1}\sqrt{\log K}), proving (12).  \(\square\)

## Lemma 3: exact atoms vanish

Take
\[
 q=\left\lfloor(\log K)^{1/4}\right\rfloor
\]
(again changing it to (2) for small (N)).  The standard quantitative
Halasz theorem says that for a completely multiplicative (g),
\(|g|\leq1\),
\[
 \left|\frac1N\sum_{n\leq N}g(n)\right|
 \ll (1+\mathcal M)e^{-\mathcal M}+K^{-1/2},\qquad
 \mathcal M=\min_{|t|\leq K}\mathbb D_N(g,n^{it})^2. \tag{20}
\]
Applying (12) to every nontrivial character (g_{a,q}) gives
\[
 \max_{1\leq a<q}
 \left|\frac1N\sum_{n\leq N}e^{2\pi iaF_N(n)/q}\right|
 \ll e^{-c\sqrt{\log K}}\operatorname{poly}(\log K)+K^{-1/2}
 =o(q^{-1}). \tag{21}
\]
Fourier inversion on \(\mathbb Z/q\mathbb Z\) therefore gives, uniformly
in (r),
\[
 \frac1N|\{n\leq N:F_N(n)\equiv r\pmod q\}|
 =\frac1q+o(q^{-1}). \tag{22}
\]
Every exact level is contained in one residue class, so
\[
 \max_c\frac1N|\{n\leq N:F_N(n)=c\}|
 \leq\frac1q+o(q^{-1})
 \ll(\log K)^{-1/4}. \tag{23}
\]
This proves the upper bound in (3).

## Exact failure mechanism

Identity (9) isolates the obstruction.  For typical (n), the term
(K\log(N/n)/L) is (o(1)), while the additive sawtooth
\[
 \sum_p\{K\log p/L\}v_p(n)
\]
has mean ((1/2)\log K+O(1)).  On exponent scale the active primes carry
harmonic mass
\[
 \sum_{N^{1/K}<p\leq N}\frac1p=\log K+O(1). \tag{24}
\]
For every slowly growing modulus (q\) used above, the rounding sawtooth has
pretentious distance \(\gg q^{-1}\sqrt{\log K}\) from every archimedean
character.  It therefore becomes equidistributed modulo (q).  Approximate
conservation of logarithmic size confines (F_N) to only (O(\log K))
plausible levels at coarse scale, but it cannot select a single exact level.

This argument also covers a fixed translation of all band boundaries (with
the zero band retained): (13) changes only by a bounded phase and the same
\(\log K\) distance remains.  It does **not** cover arbitrary multi-band
rational weights with rapidly growing, band-dependent denominators.

## Lemma chain, unsupported extension, and test

The precise chain is:

1. Rounded normalized logarithms give the rational grading (1)--(2).
2. The grading is coarsely concentrated: Lemma 1 proves a nonzero exact atom
   of size at least \(\gg1/\log K\).
3. For each small modulus, its nontrivial root-of-unity twists have the
   distance lower bound (12).
4. Quantitative Halasz plus Fourier inversion makes all residues uniform;
   hence every exact atom is (o(1)).

The weakest genuinely open extension is the following.  A general primitive
integer band vector can hide its rounding corrections in integers divisible
by every small modulus (for example by using a huge common near-slope plus
sparse coprime perturbations).  No argument here proves that some modulus
must see divergent harmonic mass of those corrections.  Such a structural
lemma would extend the failure from rounded-log gradients to much broader
scale-gradient families.

A concrete falsification test for the proved family is deterministic.  For
chosen (N,K), sieve smallest prime factors, compute
\(F_N(m)=F_N(m/p)+\lfloor K\log p/\log N\rfloor\) exactly after assigning
prime bands by integer comparisons (p^K\) versus (N^j), and record:

- the mean deficit (K-F_N(m)), predicted to be
  \((1/2)\log K+O(1)\);
- the largest exact atom, bracketed asymptotically by (3);
- all residue frequencies modulo
  (q=\lfloor(\log K)^{1/4}\rfloor\), predicted by (22) to be uniform.

The next positive action, if one continues this route, is not to add more
ordinary equal-width bands.  It is to construct a primitive rational band
vector whose error from a linear log-slope has bounded harmonic support
modulo every (q\leq q_N\to\infty).  The calculation above gives an exact
criterion that such a putative escape must defeat.
