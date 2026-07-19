# A constant-density obstruction from scale profiles and the fundamental sieve lemma

## Result

This note closes the last transfer step in `scale_cut_profile.md`.  It proves
the following asymptotic obstruction.

> **Theorem.** There is an absolute constant \(\delta>0\) such that, for all
> sufficiently large \(N\), every rational completely additive function
> \(f\) and every nonzero rational \(t\) satisfy
> \[
>   |\{n\le N:f(n)=t\}|\le (1-\delta)N.                 \tag{1}
> \]

Consequently a finite repetition-allowed PLR set cannot have cardinality
\(N-o(N)\).  In valuation-vector language, one must delete at least
\(\delta N\) rows of the valuation matrix of \([1,N]\) before the remaining
rows can lie in an affine hyperplane not containing the origin.

The only external input beyond the prime number theorem and the already
proved scale-profile lemma is the standard one-dimensional fundamental
lemma of the sieve, stated precisely below.  A direct reduction from that
lemma to the required total-variation estimate is included, so there is no
moving-support product-model assumption.

## 1. The scale-profile input

We use the following result proved in `scale_cut_profile.md`.

**Scale-profile lemma.** Fix \(0<\alpha<1/20\).  Suppose \(N_j\to\infty\),
\(f_j\) are rational completely additive, \(t_j\ne0\), and
\[
 D_j:=|\{n\le N_j:f_j(n)\ne t_j\}|=o(N_j).             \tag{2}
\]
Then
\[
 \sum_{N_j^\alpha<p\le N_j^{1-3\alpha}\atop f_j(p)\ne0}
       \frac1p=o(1).                                   \tag{3}
\]

For orientation, (3) is not a product-model assertion.  Its proof packs
globally vertex-disjoint multiplicative edges.  First it shows that almost
every dyadic prime band is nearly monochromatic.  Prime--semiprime lifts by
\(N^\alpha\)-smooth cofactors then force, on all but \(o((\log N)^2)\)
pairs of bands, both profile equations
\[
 c_i+c_j=c_{i+j},\qquad c_i+c_j=c_{i+j+1}.
\]
A dense Pexider lemma forces the modal profile to vanish, and the initial
edge packing controls all nonmodal primes in reciprocal mass.  Every product
used in the packing retains its complete large-prime signature, so no
unbounded overlap is hidden in (3).

## 2. Precise small-prime transfer

For \(y\ge2\), put
\[
 V(y)=\prod_{p\le y}\left(1-\frac1p\right),
 \qquad
 \Phi(x,y)=|\{m\le x:P^-(m)>y\}|.
\]
We use the following standard form of the fundamental lemma of the
one-dimensional sieve.

**Fundamental sieve lemma.** There is a function \(\eta(u)\to0\) as
\(u\to\infty\) such that, uniformly for \(y\to\infty\) and
\(x\ge y^u\),
\[
 \Phi(x,y)=xV(y)\bigl(1+O(\eta(u))+o_y(1)\bigr).       \tag{4}
\]
The constants are absolute.  One may take a standard fundamental-lemma
error of the shape \(\eta(u)=\exp(-c u\log u)\); only convergence to zero
is used here.

Let \(U_N\) be uniform on \([1,N]\), take \(y=N^{1/u}\), and write
\[
 S_y(U_N)=(v_p(U_N))_{p\le y}.
\]
Let \((G_p)_{p\le y}\) be independent geometric variables with
\[
 \Pr(G_p=k)=(1-p^{-1})p^{-k},\qquad k\ge0.             \tag{5}
\]

**Lemma 1 (total-variation transfer).** For fixed \(u\ge4\),
\[
 d_{\rm TV}\!\left(\mathcal L(S_y(U_N)),
          \bigotimes_{p\le y}\mathcal L(G_p)\right)
 \le {4\over u}+O(\eta(u/2))+o_u(1).                 \tag{6}
\]

### Proof

A valuation vector corresponds uniquely to a \(y\)-smooth integer
\[
 d=\prod_{p\le y}p^{a_p}.
\]
Under the independent law (5),
\[
 \Pr\left(\prod_{p\le y}p^{G_p}=d\right)=\frac{V(y)}d.\tag{7}
\]
Under the uniform-integer law, the same vector occurs precisely when
\(U_N=dm\), where \(m\) has no prime factor at most \(y\).  Hence
\[
 \Pr(S_y(U_N)=v(d))=\frac1N\Phi(N/d,y).               \tag{8}
\]

For \(d\le\sqrt N\), the residual range \(x=N/d\) satisfies
\[
 x\ge\sqrt N=y^{u/2}.
\]
Equations (4), (7), and (8) therefore show, uniformly over all such \(d\),
\[
 \Pr(S_y(U_N)=v(d))
 =\frac{V(y)}d\bigl(1+O(\eta(u/2))+o_u(1)\bigr).      \tag{9}
\]
Summing (9) gives an \(O(\eta(u/2))+o_u(1)\) contribution to total
variation on this part of the state space.

It remains only to bound the two tails.  If
\(D_y=\prod_{p\le y}p^{G_p}\), then
\[
 \mathbb E\log D_y
 =\sum_{p\le y}\frac{\log p}{p-1}
 =\log y+O(1).                                        \tag{10}
\]
Thus Markov's inequality gives
\[
 \Pr(D_y>\sqrt N)\le\frac{2+o(1)}u.                  \tag{11}
\]
For the \(y\)-smooth part \(d_y(U_N)\) of a uniform integer, the exact
floor-sum estimate gives
\[
 \begin{aligned}
 \mathbb E\log d_y(U_N)
 &=\sum_{p\le y}\log p\sum_{a\ge1}
       \frac1N\left\lfloor\frac N{p^a}\right\rfloor\\
 &\le\sum_{p\le y}\frac{\log p}{p-1}
 =\log y+O(1),
 \end{aligned}                                       \tag{12}
\]
and hence
\[
 \Pr(d_y(U_N)>\sqrt N)\le\frac{2+o(1)}u.             \tag{13}
\]
The sum of (9), (11), and (13) proves (6). \(\square\)

An important point is that (6) is obtained by comparing each exact rough
cofactor count with (4).  It is not the invalid fixed-cylinder-to-moving-
support passage ruled out by `finite_uniform_skeptic.md`.

## 3. Independent nonzero atoms

For arbitrary rational weights \((w_p)_{p\le y}\), the random sum
\[
 X=\sum_{p\le y}w_pG_p                                 \tag{14}
\]
has a zero-drift compound-Poisson law on \(\mathbb Q\).  Indeed, with
independent Poisson variables,
\[
 G_p=\sum_{k\ge1}kN_{p,k},qquad
 N_{p,k}\sim\operatorname{Pois}\left(\frac1{kp^k}\right),
\]
and the total Levy mass is finite.  The winding-number lemma already proved
in `PROOF.md` therefore gives
\[
 \sup_{c\ne0}\Pr(X=c)\le\frac12.                      \tag{15}
\]
Combining (6) and (15), for every completely additive \(f\), every nonzero
\(t\), and \(y=N^{1/u}\),
\[
 \Pr\left(\sum_{p\le y}f(p)v_p(U_N)=t\right)
 \le\frac12+\varepsilon(u)+o_u(1),                   \tag{16}
\]
where
\[
 \varepsilon(u)=\frac4u+O(\eta(u/2))\longrightarrow0.
\]

## 4. Constant-gap contradiction

Suppose (1) were false.  Then there would be a sequence \(N_j\to\infty\),
completely additive \(f_j\), and nonzero \(t_j\), for which (2) holds.
Fix \(u>20\), put \(\alpha=1/u\), and apply the scale-profile lemma.

Let \(H_j\) be the event that \(U_{N_j}\) has a prime divisor
\(p>N_j^{1-3/u}\).  By the union bound, the PNT, and partial summation,
\[
 \Pr(H_j)
 \le\sum_{N_j^{1-3/u}<p\le N_j}\frac1p
 =-\log(1-3/u)+o(1).                                  \tag{17}
\]
Let \(M_j\) be the event that \(U_{N_j}\) has an active prime divisor in
the middle range
\[
 N_j^{1/u}<p\le N_j^{1-3/u},\qquad f_j(p)\ne0.
\]
Equation (3) and another union bound give
\[
 \Pr(M_j)=o(1).                                       \tag{18}
\]

Outside \(H_j\cup M_j\), every prime factor above \(N_j^{1/u}\) has
\(f_j\)-weight zero.  Therefore
\[
 f_j(U_{N_j})
 =\sum_{p\le N_j^{1/u}}f_j(p)v_p(U_{N_j}).            \tag{19}
\]
Equations (16)--(19) yield
\[
 \frac1{N_j}|\{n\le N_j:f_j(n)=t_j\}|
 \le\frac12+\varepsilon(u)-\log(1-3/u)+o(1).         \tag{20}
\]
Choose the fixed \(u\) so large that
\[
 \varepsilon(u)-\log(1-3/u)<\frac14.
\]
Then (20) is at most \(3/4+o(1)\), contradicting (2).

This sequential contradiction implies a uniform constant \(\delta>0\):
if no such constant existed, one could choose for each \(j\) an
\(N_j\ge j\) and a nonzero level with complement at most \(N_j/j\), giving
exactly the forbidden sequence.

## 5. Dependency status and audit targets

The proof is dependency-complete modulo two named inputs:

1. the combinatorial scale-profile lemma proved in
   `scale_cut_profile.md`; and
2. the standard fundamental lemma of the one-dimensional sieve in the
   precise uniform form (4).

The main audit targets are therefore: (i) global disjointness in the two
edge packings behind (3); (ii) quantitative uniformity of (4) for
\(x\ge y^{u/2}\); and (iii) the direction of the two union bounds in
(17)--(18).  The transfer itself keeps the factor-size constraint exactly
through \(\Phi(N/d,y)\).
