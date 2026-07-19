# Fixed-core gap threshold and multiplier fibers

This route fixes an abundant nonsemiperfect integer \(b\) and studies
divisibility-minimal multipliers
\[
 C_b=\{c:bc\text{ is semiperfect, while }bd\text{ is not semiperfect for
 every }d\mid c,\ d<c\}.
\]
It gives exact subset-sum criteria and isolates a summable first-threshold
layer. It does not prove that the whole fiber \(C_b\) is summable: the exact
remaining obstruction is an iterated chain of above-threshold extensions
which remain nonsemiperfect.

Write \(D(m)\) for all positive divisors, \(D^-(m)=D(m)\setminus\{m\}\),
and \(\Sigma(E)\) for the subset sums of a finite set \(E\). For
nonsemiperfect \(m\), put
\[
 K_m=\{m-s:s\in\Sigma(D^-(m)),\ s<m\},\qquad
 g(m)=\min K_m.                                                \tag{1}
\]
Thus \(g(m)\) is the exact distance from \(m\) to its largest
proper-divisor subset sum below \(m\). Put \(M_m=\sigma(m)\).

## 1. Exact boundary-layer criterion, with no coprimality assumption

For arbitrary \(c\), define
\[
 V_c(bc)=\{v:v\mid bc,\ c\nmid v\}.                            \tag{2}
\]
There is a disjoint partition
\[
 D^-(bc)=cD^-(b)\ \sqcup\ V_c(bc).                            \tag{3}
\]
Indeed a divisor of \(bc\) which is divisible by \(c\) is uniquely \(ce\)
with \(e\mid b\).

**Lemma 1 (exact boundary criterion).** If \(b\) is nonsemiperfect, then
\[
 bc\text{ is semiperfect}
 \quad\Longleftrightarrow\quad
 \exists r\in K_b:\ cr\in\Sigma(V_c(bc)).                    \tag{4}
\]

**Proof.** Split a witness using (3), and write the sum in the first part as
\(cS\), with \(S\in\Sigma(D^-(b))\). Positivity forces \(S\le b\), and
\(S=b\) is impossible because \(b\) is nonsemiperfect. Hence \(r=b-S\in
K_b\), and the second part sums to \(cr\). The argument reverses. \(\square\)

The sum of the boundary layer is
\[
 L_b(c):=\sum_{v\in V_c(bc)}v=\sigma(bc)-c\sigma(b).           \tag{5}
\]
Therefore every activating multiplier satisfies
\[
 c g(b)\le L_b(c).                                            \tag{6}
\]

**Lemma 2 (exact gap below the threshold).** Define
\[
 \Delta_b(c)=c g(b)-L_b(c).                                   \tag{7}
\]
If \(\Delta_b(c)>0\), then \(bc\) is nonsemiperfect and
\[
 \boxed{g(bc)=\Delta_b(c).}                                  \tag{8}
\]
If \(\Delta_b(c)=0\), then \(bc\) is semiperfect.

**Proof.** In a subset sum below \(bc\), the coefficient of \(c\) in (3)
is at most \(b-g(b)\); a coefficient greater than \(b\) already overshoots,
and equality \(b\) would make \(b\) semiperfect. The boundary contribution
is at most \(L_b(c)\). Thus the sum is at most
\[
 c(b-g(b))+L_b(c)=bc-\Delta_b(c).                              \tag{9}
\]
Choose a subset attaining \(b-g(b)\) in the first part and take all of
\(V_c(bc)\). This attains (9), proving both assertions. \(\square\)

The prime case is already exact. If \(p\nmid b\), then
\[
 bp\text{ is semiperfect}
 \Longleftrightarrow
 \exists r\in K_b:\ pr\in\Sigma(D(b)),                       \tag{10}
\]
so every activating prime satisfies \(p\le M_b/g(b)\). If
\(p^a\Vert b\) and \(u=b/p^a\), then
\[
 bp\text{ is semiperfect}
 \Longleftrightarrow
 \exists r\in K_b:\ pr\in\Sigma(D(u)),                       \tag{11}
\]
and necessarily \(p g(b)\le\sigma(u)\).

If \(b\) is abundant and \(e=M_b-2b\), complementation inside
\(D^-(b)\) gives
\[
 r\in K_b\Longleftrightarrow e+r\in\Sigma(D^-(b)).            \tag{12}
\]
Thus (10) is the explicit pair of conditions
\(e+r\in\Sigma(D^-(b))\) and \(pr\in\Sigma(D(b))\).

## 2. Coprime divisor-layer tensor and the multiplicative threshold

Assume now that \((b,c)=1\). Unique factorization of divisors into a
\(b\)-part and a \(c\)-part turns (4) into the following exact criterion:
\[
 bc\text{ is semiperfect}
 \Longleftrightarrow
 \exists r\in K_b,\ X_d\in\Sigma(D(b)):\quad
 cr=\sum_{\substack{d\mid c\\d<c}}dX_d.                      \tag{13}
\]
Equivalently, for some \(r\in K_b\),
\[
 E_r(c):=M_b(\sigma(c)-c)-cr\ge0                              \tag{14}
\]
is a subset sum of the distinct lower-layer divisors
\[
 \{de:e\mid b,\ d\mid c,\ d<c\}.                             \tag{15}
\]
This is obtained by complementing the selected lower-layer subset inside
(15), whose total is \(M_b(\sigma(c)-c)\).

Here Lemma 2 reads
\[
 \Delta_b(c)=c g(b)-M_b(\sigma(c)-c).                         \tag{16}
\]
In particular every coprime activating multiplier obeys
\[
 \frac{\sigma(c)}c\ge
 \alpha_b:=1+\frac{g(b)}{M_b}.                                \tag{17}
\]

There is also a support-only form valid without coprimality. If
\(\beta_p=v_p(b)\) and \(a_p=v_p(c)\), then
\[
 \frac{\sigma(bc)}{c\sigma(b)}
 =\prod_{p\mid c}\left(1+
 \frac{1-p^{-a_p}}{p^{\beta_p+1}-1}\right).                  \tag{18}
\]
Combining (6) with (18), and putting
\(\eta_b=\log(1+g(b)/M_b)\), gives
\[
 \eta_b<\sum_{p\mid c}\frac1{p^{\beta_p+1}-1}
 \le\frac{\omega(c)}{P^-(c)-1}.                              \tag{19}
\]
Consequently
\[
 P^-(c)<1+\frac{\omega(c)}{\eta_b}.                           \tag{20}
\]
This is a genuine least-prime restriction, but it is a lower bound on the
reciprocal mass of the support, not by itself a summability estimate.

For a squarefree new-prime multiplier
\(c=p_1\cdots p_t\), \(p_1<\cdots<p_t\), (17) gives the sharper bound
\[
 p_1\le
 \frac1{(1+g(b)/M_b)^{1/t}-1}
 \le\frac{t(M_b+g(b))}{g(b)}.                                 \tag{21}
\]
If \(c\in C_b\), put \(d_j=p_1\cdots p_{j-1}\), \(m_j=bd_j\), and
\(s=t-j+1\). The prefix \(m_j\) is nonsemiperfect and its suffix activates
it, so
\[
 p_j\le
 \frac1{(1+g(m_j)/\sigma(m_j))^{1/s}-1}
 \le s(\sigma(m_j)+1).                                       \tag{22}
\]
Thus for fixed \(b,t\) there are only finitely many squarefree new-prime
supports. Crude iteration yields
\[
 p_j\le(3tM_b)^{2^{j-1}},\qquad
 c\le(3tM_b)^{2^t-1}.                                        \tag{23}
\]
The double-exponential dependence on \(t\) is precisely why this does not
sum the unbounded-support fibers.

## 3. Prime powers as a finite carry automaton

Let \(p\nmid u\), with \(u\) nonsemiperfect, and put
\(T_u=\Sigma(D(u))\). Form a directed graph on nonnegative integers by
\[
 x\longrightarrow y\quad\Longleftrightarrow\quad py-x\in T_u. \tag{24}
\]

**Lemma 3.** The number \(up^a\) is semiperfect if and only if (24) has a
length-\(a\) path from \(0\) to \(K_u\).

Indeed, if the top-layer coefficient is \(u-r\), the remaining equation is
\[
 p^ar=S_0+pS_1+\cdots+p^{a-1}S_{a-1},\qquad S_i\in T_u,        \tag{25}
\]
and successive carries satisfy \(px_{i+1}=x_i+S_i\), with
\(x_0=0,x_a=r\). Conversely a path supplies the layer subset sums.

Every carry satisfies
\[
 0\le x_i<\frac{\sigma(u)}{p-1}.                              \tag{26}
\]
If \(a\) is the first activating exponent, the path has no repeated vertex,
since deleting a cycle gives a shorter accepted path. Therefore
\[
 a\le\left\lceil\frac{\sigma(u)}{p-1}\right\rceil-1.          \tag{27}
\]
If \(p^r\Vert b\), write \(b=p^ru\). All exponents through \(r\) are
nonsemiperfect (otherwise semiperfectness lifts to \(b\)), so a first
same-prime activation \(bp^e\) satisfies
\[
 r+e\le\left\lceil\frac{\sigma(u)}{p-1}\right\rceil-1.        \tag{28}
\]

## 4. The summable first-threshold layer

For a fixed rational \(\alpha=A/B>1\), call \(n\) **primitive
\(\alpha\)-nondeficient** when
\[
 B\sigma(n)\ge An,qquad B\sigma(d)<Ad\quad(d\mid n,\ d<n).   \tag{29}
\]

**Theorem 4.** For every fixed rational \(\alpha>1\), the primitive
\(\alpha\)-nondeficient integers have finite reciprocal sum.

The proof of the primitive-nondeficient theorem in
`primitive_nondeficient_largest_prime.md` transfers with an integer-scaled
defect. For completeness, the exact algebra is as follows. For an
\(\alpha\)-deficient \(m\), put
\[
 \delta(m)=Am-B\sigma(m)>0,qquad
 T(m)=\frac{B\sigma(m)}{\delta(m)}.                            \tag{30}
\]
For \(p\nmid m\),
\[
 \delta(mp)=p\delta(m)-B\sigma(m),                            \tag{31}
\]
so \(mp\) crosses the threshold exactly when \(p\le T(m)\). In the hard
squarefree-top case write \(n=uqp\), with \(P(u)<q<p\), and set \(t=T(u)\).
Primitivity gives
\[
 q>t,qquad p\le\frac{t(q+1)}{q-t},qquad q<2t+\tfrac12.       \tag{32}
\]
The same dyadic Brun--Titchmarsh/Chebyshev calculation gives, uniformly for
\(t\ge4\),
\[
 \sum_{\substack{q,p\ {\rm prime}\\
 q>t+1,\ q<p\le t(q+1)/(q-t)}}\frac1{qp}
 \ll\frac1{\log^2t}+\frac1{\sqrt t}.                         \tag{33}
\]
The possible endpoint \(t<q\le t+1\) contributes
\(O((1+\log u)/t)\), since the denominator in (30) is a positive integer.
Nonemptiness and \(q>P(u)\) give \(t>(P(u)-1/2)/2\). Summation over \(u\)
then uses the convergent standard tails
\[
 \sum_{u>1}\frac1{u\log^2(2P(u))},\qquad
 \sum_{u>1}\frac1{u\sqrt{P(u)}},\qquad
 \sum_{u>1}\frac{1+\log u}{uP(u)}.                           \tag{34}
\]
Top or second exact prime-power exponent at least two is bounded by
\(\sum_p(\log p)/p^2\). For bounded \(P(u)\), (30) gives
\(T(u)\le B\sigma(u)<Au\), and the corresponding fixed-support Euler
products converge. These are exactly the cases in the recorded proof, and
establish the theorem with constants allowed to depend on \(A,B\).

Apply the theorem with
\[
 \alpha=\alpha_b=1+\frac{g(b)}{M_b}.                           \tag{35}
\]
If a coprime \(c\in C_b\) has
\(\sigma(d)/d<\alpha_b\) for every proper \(d\mid c\), then (17) makes
\(c\) primitive \(\alpha_b\)-nondeficient. Hence
\[
 \sum_{\substack{c\in C_b,\ (b,c)=1\\
 \sigma(d)/d<\alpha_b\ (d\mid c,d<c)}}\frac1c<\infty.        \tag{36}
\]

## 5. Exact recursive relative-weird obstruction

Let \(c\in C_b\) be coprime to \(b\), and choose a divisibility-minimal
divisor \(d\mid c\) satisfying \(\sigma(d)/d\ge\alpha_b\), which exists by
(17). If \(d=c\), then \(c\) belongs to the summable layer (36). If \(d<c\),
then
\[
 b_1=bd\quad\hbox{is nonsemiperfect},
 \qquad c/d\in C_{b_1}.                                      \tag{37}
\]
Indeed \(bd\) is attached to a proper multiplier of \(c\). Moreover
\(b_1(c/d)=bc\) is semiperfect, while for every proper \(f\mid c/d\), the
multiplier \(df<c\), so \(bdf\) is nonsemiperfect.

Thus any divergent fiber must be carried by arbitrarily long chains
\[
 b=b_0\mid b_1\mid b_2\mid\cdots,qquad b_i=b_{i-1}d_i,        \tag{38}
\]
where \(d_i\) is a primitive crossing of the current rational threshold but
\(b_i\) remains nonsemiperfect. Each individual primitive-crossing layer is
summable by Theorem 4. The missing estimate is uniform control as
\[
 R(b_i):=\frac{\sigma(b_i)}{g(b_i)}\longrightarrow\infty.      \tag{39}
\]
This is substantive: prime crossing mass by itself can grow on the order of
\(\log\log R\), so (36) cannot be iterated with an absolute constant.

## 6. The core 70 and an explicit recursive obstruction

Direct interval joining gives
\[
\begin{aligned}
 \Sigma(D^-(70))&=[0,3]\cup[5,69]\cup[71,74],\\
 \Sigma(D(70))&=[0,3]\cup[5,139]\cup[141,144].                \tag{40}
\end{aligned}
\]
Consequently
\[
 M_{70}=144,qquad g(70)=1,qquad \alpha_{70}=145/144.         \tag{41}
\]
The exact prime test shows that every prime at most 139 lies in \(C_{70}\),
while no prime at least 149 does. (The shared primes 2, 5, and 7 are checked
by (11); 3 and the primes from 11 through 139 follow from (10).) Hence every
composite member of \(C_{70}\) has all prime factors at least 149. No pure
power \(p^a\), \(p\ge149\), activates 70, since
\[
 \frac{\sigma(p^a)}{p^a}-1<\frac1{p-1}\le\frac1{148}<\frac1{144}. \tag{42}
\]

For a squarefree pair \(c=pq\), \(149\le p<q\), (13) forces \(r=1\), since
\[
 r\le144\frac{p+q+1}{pq}<2.                                  \tag{43}
\]
Thus the exact criterion is
\[
 pq=X_1+pX_p+qX_q,qquad X_1,X_p,X_q\in\Sigma(D(70)),         \tag{44}
\]
or
\[
 (p-X_q)(q-X_p)=X_pX_q+X_1.                                  \tag{45}
\]
The capacity condition gives
\[
 (p-144)(q-144)\le20880,                                     \tag{46}
\]
so \(p\le283\) and \(q\le144+20880/(p-144)\). The entire
two-new-prime fiber is therefore finite. For example
\[
 149\cdot1489=49\cdot149+144\cdot1489+144,                    \tag{47}
\]
which, with a top coefficient 69, proves
\(149\cdot1489\in C_{70}\).

The primitive threshold layer is not the whole fiber mechanism. Put
\[
 p=283,qquad q=293,qquad d=pq=82919.                         \tag{48}
\]
Both prime divisors are below \(145/144\), while
\[
 144\sigma(d)-145d=169>0.                                    \tag{49}
\]
Thus \(d\) is primitive \(145/144\)-nondeficient. Nevertheless \(70d\) is
not semiperfect. Equation (43) forces the gap parameter to be one; writing
\(X_p=144-A\) and \(X_q=144-B\) in (44) gives
\[
 X_1=283A+293B-25.                                            \tag{50}
\]
For \(A=B=0\) the right side is negative, while if either is positive it is
greater than 144, contradicting (40).

Moreover this new nonsemiperfect core has exact gap
\[
 g(70d)=114.                                                  \tag{51}
\]
The all-lower-layers selection overshoots the target by 169. A deletion
confined to the base layer has size at most 144, and the next available
individual lower-layer divisors are 283 and 293. Thus the least deletion
greater than 169 is 283, leaving deficit \(283-169=114\). Moving the top
coefficient down by another unit loses \(d=82919\), far more than all lower
layers can repair. This proves (51).

The relative-weird core really can be activated at the next support level.
Since
\[
 114\cdot307=119\cdot293+131,                                 \tag{52}
\]
and \(119,131\in\Sigma(D(70))\), the right side is a divisor-subset sum of
\(70d\). Together with a proper-divisor subset sum \(70d-114\), equation
(10) proves that \(70d\cdot307\) is semiperfect. Explicitly,
\[
 70pqr=69pqr+143pr+144qr+144r+119q+131,\quad r=307.            \tag{53}
\]
All coefficients are the required divisor-subset sums of 70.

Every proper multiplier is nonsemiperfect. The pair \(pq\) was handled
above, and the other pair coatoms fail even the capacity condition:
\[
 283\cdot307=86881>144(283+307+1)=85104,
\]
\[
 293\cdot307=89951>144(293+307+1)=86544.                      \tag{54}
\]
The singleton primes exceed 139. Hence
\[
 \boxed{283\cdot293\cdot307\in C_{70}}.                      \tag{55}
\]

Equations (48)--(55) exhibit an actual recursive relative-weird transition,
not merely a weakness of the estimates. They also show exactly what remains
for the fixed-fiber reciprocal question: unboundedly many such transitions
would have to be controlled (or constructed with enough harmonic mass).

## 7. Set-valued defects, sampled holes, and a full reset

The scalar \(g(m)\) is too lossy for the recursion.  Retain instead
\[
 T_m=\Sigma(D(m)),\qquad
 K_m=\{m-s>0:s\in\Sigma(D^-(m)),\ s<m\}.                     \tag{56}
\]
For every new prime \(p\nmid m\), divisor-layer decomposition gives
\[
 T_{mp}=T_m+pT_m,qquad
 K_{mp}=(pK_m-T_m)\cap\mathbb Z_{>0}.                         \tag{57}
\]
If \(m\) is nonsemiperfect, then \(mp\) activates exactly when
\(pK_m\cap T_m\ne\varnothing\).  If it remains nonsemiperfect, then
\[
 g(mp)=\min\{pr-s>0:r\in K_m,\ s\in T_m\}.                  \tag{58}
\]

These identities turn failed primes into sampled subset-sum holes.  With
\(M=\sigma(m)\), define
\[
 H_m(x)=\sum_{\substack{r\in K_m\\r\le x}}\frac1r,
 \qquad {\cal H}_m=\{1\le h\le M:h\notin T_m\}.
\]
For any set \({\cal F}\) of new primes such that \(mp\) is nonsemiperfect,
\[
 \boxed{\displaystyle
 \sum_{p\in{\cal F}}\frac{H_m(M/p)}p
 \le\sum_{h\in{\cal H}_m}\frac{\omega(h)}h.}               \tag{59}
\]
Indeed each pair \((p,r)\) on the left maps to the hole \(h=pr\), and its
weight is \(1/h\); its multiplicity is at most \(\omega(h)\).  Restricting
to \(p>\sqrt M\) removes the factor \(\omega(h)\), since \(h\le M\) has at
most one prime divisor exceeding \(\sqrt M\).

The gap set cannot collapse in cardinality along a failed new-largest-prime
edge.  If \(p>P^+(m)\), take
\[
 B=\{0,1\}\cup\{q:q\mid m,\ q\text{ prime}\}
 \subset T_m\cap[0,p).
\]
Reduction modulo \(p\) shows that \((r,b)\mapsto pr-b\) is injective on
\(K_m\times B\), while all its values are positive.  Hence
\[
 |K_{mp}|\ge(\omega(m)+2)|K_m|,
 \qquad
 \sum_{u\in K_{mp}}\frac1u
 \ge\frac{\omega(m)+2}{p}\sum_{r\in K_m}\frac1r.           \tag{60}
\]

Nevertheless the scalar minimum can reset completely.  Put
\[
 m_1=70\cdot149,qquad m_2=m_1\cdot4051.
\]
From (40), \(g(70)=1\) and \(g(m_1)=149-144=5\).  Since
\[
 5\cdot4051=149\cdot135+140,
 \qquad 140\notin T_{70},                                   \tag{61}
\]
4051 is an eligible failed prime.  But
\[
 5\cdot4051-1=149\cdot135+139\in T_{m_1},                  \tag{62}
\]
so \(g(m_2)=1\).  The next prime activates because
\[
 4177=4051+70+35+14+7\in T_{m_2}.                           \tag{63}
\]
The explicit witness and all six cover checks are recorded in `NOTES.md`
and verified by `computational/verify_reset_chain.py`; they prove
\[
 \boxed{70\cdot149\cdot4051\cdot4177\in A}.                \tag{64}
\]

Thus a proof cannot assume that \(g\), or equivalently
\(R=\sigma/g\), changes monotonically in a favorable direction.  The
sharpened unresolved estimate is a uniform upper bound for the weighted
sampled-hole budget (59), coupled to the amplification (60), strong enough
to make terminal reciprocal mass summable over arbitrary chains.  The
factor \(\omega(h)\) for small primes and the possible thinness of truncated
gap sets are the first exact obstructions.
