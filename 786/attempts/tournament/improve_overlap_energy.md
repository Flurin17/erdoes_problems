# Improving the finite-overlap/energy argument

## Outcome

Write
\[
B=\{n\le N:f(n)=1\},\qquad E=[1,N]\setminus B,\qquad m=|E|,
\]
where \(f:\mathbb N\to\mathbb Q\) is completely additive. The
\(N/\log N\) proof can be sharpened structurally in two ways.

1. There is an exact finite alternative: either an adjacent change of
   cofactor color costs \(\gg N/\log N\), or \(m\) obeys an explicit
   implicit energy inequality. The last cofactor scale can be taken within
   a factor \(2\) of \(\sqrt{N/2}\), rather than \(\sqrt N/4\).
2. Continuing the rectangles down to primes of size \(N^{1/3}\) shows that
   the no-change branch is far more rigid than pair energy suggests: two
   separated polynomial prime ranges and the zero-colored cofactors produce
   \(\Omega(N)\) distinct exceptions.

Thus the real obstruction to a larger lower bound is a paid color cut, not
the final product-set estimate. Higher-fold products give valid
inequalities, but remain behind the same propagation barrier. A second
rigorous ingredient is a recursive row penalty: every prime row whose
prime color is not \(1\) contains \(\gg C/\log C\) errors, by applying the
proved theorem to its nonzero cofactor fiber. This conditionally yields an
\(N\log\log N/\log N\) bound and gives a concrete route toward an
unconditional improvement.

All prime-distribution estimates below are standard consequences of the
prime number theorem, including partial summation for reciprocal primes.
No external lookup is used.

## 1. An optimized exact alternative

Put \(C_j=2^j\) and
\[
P_j=\left\{p\text{ prime}:\frac{N}{2C_j}<p\le\frac{N}{C_j}\right\},
\qquad R_j=|P_j|.
\]
Let \(J\) be maximal subject to
\[
M:=C_J<\sqrt{N/2}.
\]
Then \(M\ge\sqrt{N/8}\). For \(p\in P_j\), let
\[
e(p,j)=|\{k\le C_j:pk\in E\}|,\qquad
B_j=\sum_{p\in P_j}e(p,j).
\]
All products in these rectangles are jointly distinct: every participating
prime exceeds \(M\), whereas every cofactor is at most \(M\). Hence
\[
\sum_{j=0}^J B_j\le m. \tag{1}
\]

For each \(j\), choose \(p_j\in P_j\) minimizing \(e(p,j)\), and define
\[
c_j=1-f(p_j),\qquad e_j=e(p_j,j).
\]
There is an exact identity
\[
e_j=|\{k\le C_j:f(k)\ne c_j\}|,\qquad
e_j\le \frac{B_j}{R_j}. \tag{2}
\]
If \(c_j\ne c_{j+1}\), the two prescribed colors cannot both hold at any
\(k\le C_j\). Therefore
\[
C_j\le e_j+e_{j+1}
\le \frac{B_j}{R_j}+\frac{B_{j+1}}{R_{j+1}}, \tag{3}
\]
and consequently
\[
B_j+B_{j+1}\ge C_j\min(R_j,R_{j+1}). \tag{4}
\]
Define the finite cut capacity
\[
D_N=\min\left(R_0,\min_{0\le j<J}
C_j\min(R_j,R_{j+1})\right). \tag{5}
\]

### Proposition 1 (cut or implicit energy)

Every \(f\) as above satisfies at least one of
\[
m\ge D_N, \tag{6}
\]
or
\[
m\ge
\frac{(M-m/R_J)_+^4}{2M^2(1+\log M)}. \tag{7}
\]

#### Proof

Suppose \(m<D_N\). Then \(B_0<R_0\), so the chosen top row has no error.
Its only cofactor is \(1\), and \(f(1)=0\), so \(c_0=0\). Equations
(1), (4), and (5) rule out every adjacent color change. Thus \(c_j=0\)
for every \(j\le J\). At the last scale,
\[
Z=\{k\le M:f(k)=0\}
\]
satisfies
\[
|Z|=M-e_J\ge M-\frac{m}{R_J}. \tag{8}
\]
Every element of \(Z\cdot Z\) is at most \(M^2<N\), has \(f\)-value zero,
and hence lies in \(E\).

The parametrization of \(ab=cd\), with
\[
a=gr,\quad c=gs,\quad (r,s)=1,\quad b=sh,\quad d=rh,
\]
gives
\[
\#\{a,b,c,d\le M:ab=cd\}\le 2M^2(1+\log M). \tag{9}
\]
Cauchy--Schwarz and (8)--(9) prove (7). \(\square\)

The prime number theorem gives
\[
D_N\gg\frac{N}{\log N},\qquad
R_JM\gg\frac{N}{\log N}. \tag{10}
\]
Together with \(M^2\ge N/8\), Proposition 1 proves the same order as the
existing argument while exposing the constants that should actually be
optimized: a minimum cut capacity and the positive fixed point of (7).
The convenient uniform condition \(B_j\le\eta R_jC_j\), \(\eta<1/3\),
is not needed.

This also gives a sharp warning: improving the lower bound for
\(|Z\cdot Z|\), even to \(\gg N\), strengthens only the second branch.
It does not rule out the cut branch (6).

## 2. Higher-fold zero products

Stop at a dyadic \(M_r=C_{J_r}\) satisfying \(M_r^r\le N\), and suppose no
color cut has occurred before that scale. Put
\[
Z_r=\{k\le M_r:f(k)=0\}.
\]
Then
\[
|Z_r|\ge M_r-\frac{m}{R_{J_r}}, \tag{11}
\]
and every member of \(Z_r^r\) lies in \(E\). If
\[
\nu_r(n)=|\{(z_1,\ldots,z_r)\in[1,M_r]^r:z_1\cdots z_r=n\}|
\]
and
\[
\mathcal E_r(M_r)=\sum_n\nu_r(n)^2,
\]
then Cauchy--Schwarz gives the exact inequality
\[
m\ge |Z_r^r|
\ge \frac{(M_r-m/R_{J_r})_+^{2r}}{\mathcal E_r(M_r)}. \tag{12}
\]

For comparison, the standard fixed-\(r\) divisor-moment estimate
\[
\mathcal E_r(M)\le\sum_{n\le M^r}d_r(n)^2
\ll_r M^r(\log M)^{r^2-1} \tag{13}
\]
would give only
\[
|Z_r^r|\gg_r\frac{N}{(\log N)^{r^2-1}}
\]
when \(M_r\asymp N^{1/r}\) and \(Z_r\) has fixed positive density. The
special \(r=2\) parametrization (9) is much better than (13). Sharper
higher-dimensional multiplication-table estimates could improve (12), but
there is a more basic obstruction:

> To obtain (11), the anchored color must first be propagated from \(C=1\)
> to \(C=M_r\). A single intervening color cut still has capacity
> \(\Theta(N/\log N)\), independently of \(r\).

Thus \(r\)-fold energy alone cannot improve the order. It can strengthen
the contradiction only after assuming that no cut of the already critical
size occurred.

There is also a density obstruction to reusing only the terminal set at
\(M\asymp\sqrt N\). If it misses \(d\) points, its restriction to
\([1,N^{1/r}]\) is guaranteed to contain anything only when
\(d<N^{1/r}\). For \(r\ge3\), the natural \(d\asymp M\) allowed by an
\(N/\log N\) hypothesis can swallow the entire smaller interval. A
separate rectangle ending at \(N^{1/r}\) is necessary, returning to the
same cut barrier.

## 3. Continuing below the square-root prime scale

Pairwise injectivity is lost below \(\sqrt N\), but bounded overlap is
enough. Continue the rectangles until
\[
C_j\le N^{2/3}/8. \tag{14}
\]
Every participating prime then exceeds \(4N^{1/3}\). An integer at most
\(N\) has at most two distinct prime divisors exceeding \(4N^{1/3}\), so
\[
\sum_jB_j\le2m. \tag{15}
\]
The row identity (2) and adjacent overlap inequality (3) remain exact;
injectivity was used only to charge bad matrix entries to \(E\).

Uniformly in this range, the prime number theorem gives
\[
R_jC_j\ge c_0\frac{N}{\log N} \tag{16}
\]
for an absolute \(c_0>0\). Consequently, under
\[
m\le\varepsilon\frac{N}{\log N}, \tag{17}
\]
every chosen row has relative error at most
\[
\delta:=\frac{2\varepsilon}{c_0}. \tag{18}
\]
Moreover, (3), (15), and (16) show that an adjacent color change forces
\[
2m\ge c_1\frac{N}{\log N} \tag{19}
\]
for an absolute \(c_1>0\). Thus sufficiently small fixed \(\varepsilon\)
also makes \(B_0<R_0\), so the top chosen row has color zero. It then
rules out every color change, and every chosen cofactor color is zero.

This one-row conclusion transfers to most primes in the band. Let
\[
W_j=|\{p\in P_j:f(p)\ne1\}|.
\]
The chosen row supplies at least \((1-\delta)C_j\) zero-colored cofactors.
For every prime counted by \(W_j\), all products with those cofactors are
bad. Hence
\[
W_j(1-\delta)C_j\le B_j,
\]
and therefore
\[
\frac{W_j}{R_j}\le\frac{\delta}{1-\delta}. \tag{20}
\]

### Proposition 2 (linear cross-band amplification)

There are absolute constants \(\varepsilon_0,c_2>0\) such that, if (17)
holds with \(\varepsilon\le\varepsilon_0\) and there is no color cut in the
extended family (14), then
\[
m\ge c_2N. \tag{21}
\]

#### Proof

Use the disjoint polynomial prime ranges
\[
I_1=[N^{3/8},N^{2/5}],\qquad
I_2=[N^{9/20},N^{19/40}]. \tag{22}
\]
Call a prime good if its \(f\)-value is \(1\). Equation (20), and the fact
that reciprocal weights vary by at most a factor \(2\) in a dyadic band,
show that
\[
\sum_{\substack{p\in I_1\\f(p)=1}}\frac1p
\ge(1-2\theta-o(1))\log\frac{16}{15},
\quad
\sum_{\substack{q\in I_2\\f(q)=1}}\frac1q
\ge(1-2\theta-o(1))\log\frac{19}{18}, \tag{23}
\]
where \(\theta=\delta/(1-\delta)\). We used the standard consequence
\[
\sum_{N^\alpha<p\le N^\beta}\frac1p
=\log(\beta/\alpha)+o(1)
\]
of the prime number theorem. Boundary dyadic bands contribute \(o(1)\).

For every good \(p\in I_1,q\in I_2\), choose the power of two \(C(p,q)\)
with
\[
C(p,q)\le\frac{N}{pq}<2C(p,q). \tag{24}
\]
Its exponent lies between \(1/8\) and \(7/40\), so this is one of the
scales in (14). At least \((1-\delta)C(p,q)\) integers \(k\le C(p,q)\)
have \(f(k)=0\). Every such \(k\) gives
\[
f(pqk)=2,
\]
so \(pqk\in E\).

All these products are distinct. Indeed,
\(k<N^{7/40}<p<q\), and the two prime ranges are disjoint. Unique
factorization recovers \(q\), then \(p\), then \(k\). Thus (23)--(24)
give
\[
\begin{split}
m
&\ge\sum_{\substack{p\in I_1,\ q\in I_2\\f(p)=f(q)=1}}
(1-\delta)C(p,q)\\
&\ge\frac{1-\delta}{2}N
\left(\sum_{\substack{p\in I_1\\f(p)=1}}\frac1p\right)
\left(\sum_{\substack{q\in I_2\\f(q)=1}}\frac1q\right)
\ge c_2N
\end{split} \tag{25}
\]
for sufficiently small absolute \(\delta\). \(\square\)

Proposition 2 gives a second proof of the \(N/\log N\) theorem. Under a
sufficiently small \(N/\log N\) hypothesis, a cut is impossible by (19),
whereas the no-cut branch is impossible by (21). More importantly, it
shows that pair energy is not the limiting step: once the anchored color
reaches primes of size \(N^{1/3}\), complete additivity amplifies the
contradiction from \(N/\log N\) to \(N\).

## 4. A recursive penalty for non-\(1\) prime rows

The proved \(N/\log N\) theorem can be fed back into every row. Let
\(c_*>0\) be a constant for which it holds at all sufficiently large
arguments. If \(t\ne0\), applying the theorem to \(f/t\) gives
\[
|\{k\le C:f(k)\ne t\}|\ge c_*\frac{C}{\log C}. \tag{26}
\]
Consequently, for any prime \(p\),
\[
f(p)\ne1\quad\Longrightarrow\quad
|\{k\le C:pk\in E\}|\ge c_*\frac{C}{\log C}, \tag{27}
\]
because the required cofactor value \(1-f(p)\) is nonzero.

For \(p>\sqrt N\), all prime--cofactor products are globally distinct.
Thus (27) gives the unconditional weighted estimate
\[
m\ge c_*
\sum_{\substack{\sqrt N<p\le N/C_*\\f(p)\ne1}}
\frac{N/p}{\log(N/p)}, \tag{28}
\]
where \(C_*\) is a fixed threshold beyond which (26) is valid.

There is a useful bandwise version. Define
\[
H(C)=|\{k\le C:f(k)\ne0\}|,\qquad
\vartheta_j=\frac{|\{p\in P_j:f(p)\ne1\}|}{R_j}.
\]
For \(C_j\le\sqrt{N/2}\), joint injectivity and the exact row descriptions
give
\[
\begin{split}
m&\ge\sum_jB_j,\\
B_j&\ge R_j\left((1-\vartheta_j)H(C_j)
+\vartheta_jc_*\frac{C_j}{\log C_j}\right).
\end{split} \tag{29}
\]
In particular,
\[
m\ge\sum_jR_j\min\left(H(C_j),
c_*\frac{C_j}{\log C_j}\right). \tag{30}
\]

This goes beyond overlap connectivity. For example, if some fixed
\(\vartheta>0\) satisfies \(\vartheta_j\ge\vartheta\) on all dyadic
cofactor scales \(C_*\le C_j\le\sqrt{N/2}\), then the prime number theorem
and (29) give
\[
\begin{split}
m
&\gg N\sum_{1\ll j\le(\log_2N)/2}
\frac1{j(\log_2N-j)}\\
&\gg\frac{N\log\log N}{\log N}.
\end{split} \tag{31}
\]
Therefore an extremizer at the \(N/\log N\) scale must have a specific
shape: on a harmonic majority of the large-prime scales, almost all primes
must have value exactly \(1\), and then (29) forces the nonzero cofactor
count \(H(C_j)\) to be small on those scales.

The missing unconditional step is to exploit these simultaneous
conclusions about the profile \(H(C)\). Terminal pair energy uses only one
scale and discards the harmonic information in (29).

## 5. General cross-band equation

Let \(P_1,\ldots,P_r\) be disjoint prime sets, and let \(K\) be a cofactor
set satisfying
\[
\max K<\min_i\min P_i,\qquad
\left(\prod_i\max P_i\right)\max K\le N.
\]
Suppose all primes in \(P_i'\subset P_i\) have color \(a_i\), and all
cofactors in \(K'\subset K\) have color \(1-a_0\). The product map on
\(P_1'\times\cdots\times P_r'\times K'\) is injective. Hence
\[
a_1+\cdots+a_r\ne a_0
\quad\Longrightarrow\quad
m\ge |K'|\prod_{i=1}^r|P_i'|. \tag{32}
\]

For dyadic prime bands, write \(L=\log_2N\), and let \(b_x\) denote the
dominant color of primes of absolute logarithmic size \(2^x\). When all
relevant rectangles are good, (32) imposes the discrete Cauchy relation
\[
b_{x_1+\cdots+x_r}=b_{x_1}+\cdots+b_{x_r} \tag{33}
\]
whenever the sum is at most \(L\) and the residual cofactor scale satisfies
\[
L-(x_1+\cdots+x_r)<\min_i x_i,
\]
up to harmless endpoint shifts from dyadic widths. (A bounded-overlap
version can cover a somewhat larger domain.) The linear profile
\(b_x=x/L\) satisfies all these equations and would be the unique solution
if the equations held on the full additive domain with \(b_L=1\). Such a
color gradient is incompatible with long nested cofactor intervals being
almost monochromatic, explaining why many scale cuts ought to be
expensive.

The most abrupt abstract step sequence,
\[
b_x=0\quad(0\le x<L),\qquad b_L=1, \tag{34}
\]
satisfies every interior relation \(b_{x+y}=b_x+b_y\), but it fails on the
boundary \(x+y=L\). Importantly, the boundary is not cheap after the prime
weights are included. A complementary pair of logarithmic prime bands of
sizes \(2^x\) and \(2^{L-x}\) contributes
\[
\asymp \frac{N}{x(L-x)}
\]
distinct exceptional semiprimes. Summing for
\(1\ll x\le L/2\) gives
\[
\sum_x\frac{N}{x(L-x)}
\asymp\frac{N\log L}{L}
=\frac{N\log\log N}{\log N}. \tag{35}
\]
Thus the simplest realization of a single scale step already exhibits a
\(\log\log N\) gain. This is conditional on having the asserted prime
colors on all those bands, but it is positive evidence for the cross-band
route rather than a counterexample to it.

The correct falsification test remains the incidence cut from the finite
overlap model: arbitrary cofactor colors can be separated for
\(\Theta(N/\log N)\) deletions. That construction is deliberately not
completely additive. Therefore any improvement must explicitly prove that
an additive realization of the cut either has a large weighted set of
violations such as (35), or recursively incurs the nonzero-fiber row costs
in (26)--(30). Graph connectivity alone cannot provide that conclusion.

## 6. Dependency chain and bottleneck

The rigorous chain established here is:

1. Adjacent unequal cofactor colors have the exact cut cost (4).
2. Below the minimum cut capacity, the terminal zero fiber satisfies the
   implicit energy inequality (7).
3. The same statement has the \(r\)-fold form (12), but every fixed \(r\)
   remains behind the same cut capacity.
4. Rectangles continue to primes above \(N^{1/3}\) with total overlap at
   most \(2\), as in (15).
5. If the anchored zero color reaches that range, Proposition 2 forces
   \(\Omega(N)\) exceptions.
6. If a prime row has color other than \(1\), its nonzero cofactor target
   invokes the base theorem recursively and costs \(\gg C/\log C\), giving
   (28)--(30).

The weakest unsupported step toward a larger lower bound is now precise:

> **Multiscale cofactor-profile lemma needed.** Combine the row sum (29)
> with products of zero-colored cofactors and (32) to prove that errors
> created at different cofactor scales cannot all be supported on the same
> \(O(N/\log N)\) integers. A first target is a factor tending to infinity
> in a disjointly tagged version of
> \[
> \sum_jB_j+|Z\cdot Z|.
> \]
> Equivalently, prove a stability version of (33): a color profile with
> few interval changes either has weighted relation-violation mass at least
> the boundary mass in (35), or forces a nonzero cofactor fiber on enough
> scales for (29) to have the same order.

One cannot simply add (29) to a product-set bound, because the same
exceptional integer may be counted in a prime row and as a zero product.
Nor can one sum cut capacities without controlling how many participating
large prime divisors an exceptional integer has. A repair needs an explicit
bounded-overlap or weighted-incidence argument.

## 7. Concrete next actions

1. Use the exact profile inequality (29), not only dominant run colors.
   Partition \(E\) by largest prime factor so that row errors and zero
   products are charged to disjoint largest-prime ranges.
2. Attempt induction on \(C\) using (26): a nonzero cofactor target pays
   \(C/\log C\), while a zero target supplies multiplicative products. The
   induction must retain a largest-prime tag to prevent overlap.
3. For an \(r\)-fold experiment, use (32) with disjoint polynomial prime
   ranges and a tagged cofactor interval. Optimize
   \(|K'|\prod_i|P_i'|\) divided by the maximum number of selected prime
   tags that one exceptional integer can carry.
4. Test every proposed scale lemma against both sharp models: the single
   incidence cut, which costs \(\Theta(N/\log N)\) but is not additive,
   and the abstract step profile (34), whose weighted boundary violations
   have the larger size (35).

The route survives, but its correct form is recursive cross-band counting,
not a stronger terminal energy estimate.
