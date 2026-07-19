# Audit of the largest-prime-factor charging argument

## Verdict

The argument in `profile_lpf_charge.md` is correct, conditional only on the
previously proved uniform \(cX/\log X\) complement theorem and the ordinary
prime number theorem.  In particular, the moving choice of the active primes
does not invalidate Lemma 3.

The original proof compresses two points that deserve expansion:

1. the PNT estimate for exponent windows of length \(\asymp1/\log N\) in
   (20), including uniformity in the location of the window; and
2. the passage from the two-prime estimate (22) to the \(2k\)-prime estimate
   (25).

Both gaps are expository rather than substantive.  A complete uniform proof
is given below.  All constants may depend on the fixed reciprocal budget
\(K_1\), as permitted in Lemma 3, but not on \(N\), the deleted prime set, or
the particular interval selected by the pigeonhole step.

## 1. Preliminary rows and largest-prime tags

The products used in (3)--(5) are jointly distinct.  Indeed,
\(p>N/(2M)>M\geq k\), so \(p=P^+(pk)\).  If \(pk=q\ell\) for two tagged
products with \(p\ne q\), then the larger-prime tag on the left must divide
the cofactor on the right, which is smaller than that tag.  This is
impossible.  Thus every bad row entry is a different member of \(E_>\), and
(5) follows with no multiplicity loss.

Lemma 1 uses the earlier theorem in a legitimate way.  If \(f(p)\ne1\), then
\(t=1-f(p)\ne0\), and \(f/t\) is again completely additive.  Applying the
uniform complement theorem to its level-one fibre gives (9).  If \(f(p)=1\),
each active prime \(q\leq C_j\), viewed as the cofactor \(k=q\), is directly a
bad entry.  No density or independence assertion is used here.

For (11), the prime interval has lower endpoint
\(x=N/(2C_j)\geq N/(2M)>\sqrt{N/2}\), while \(\log x\asymp\log N\).  The PNT
therefore gives the displayed lower bound uniformly over all relevant
\(j\).  On interchanging sums in (12), an active prime \(q\) first appears at
the least dyadic \(C_j\geq q\); this \(C_j<2q\), and even if it is the final
scale its single contribution is at least \(1/(2q)\).  This proves (10).

## 2. Uniform PNT input for Lemma 3

Write \(L=\log N\).  We first record the exact local consequence of the PNT
that is needed.  Fix
\[
 0<\alpha<\beta<\infty,
 \qquad 0<\lambda_-<\lambda_+<\infty.
\]
Uniformly for \(u\in[\alpha,\beta]\) and
\(\lambda\in[\lambda_-,\lambda_+]\),
\[
 \sum_{N^u<p\leq N^{u+\lambda/L}}\frac1p
   =\frac{\lambda}{uL}+o\!\left(\frac1L\right).       \tag{A1}
\]
To see the claimed uniformity directly, put \(x=N^u\) and
\(y=e^\lambda x\), and use partial summation:
\[
 \sum_{x<p\leq y}\frac1p
 =\frac{\pi(y)}y-\frac{\pi(x)}x
   +\int_x^y\frac{\pi(v)}{v^2}\,dv .                  \tag{A2}
\]
The PNT error in \(\pi(v)=v(1+o(1))/\log v\) is uniform for
\(v\geq N^\alpha\), simply because the relative error tends to zero at
infinity.  The main integral is
\[
 \log\frac{\log y}{\log x}
 =\log\left(1+\frac{\lambda}{uL}\right)
 =\frac{\lambda}{uL}+O(L^{-2}),
\]
the main endpoint difference is \(O(L^{-2})\), and all PNT error terms are
\(o(1/L)\), uniformly in the displayed compact parameter ranges.  This
proves (A1).  It also gives the corresponding upper bound for a clipped
window: enclose the clipped interval in a full exponent interval of the
same fixed \(O(1/L)\) length.

Now fix one of the exponents \(a\) in the finite menu chosen in (16)--(18),
and let
\[
 \mu=\sum_{N^a<p\leq N^{2a}}p^{-1}\delta_{\log p/L}.
\]
Take \(W=[s,s+h]\), where \(h=\lambda/L\), with \(\lambda\) in any fixed
compact subinterval of \((0,\infty)\), and suppose
\(W\subset[2.9a,3.1a]\).  For all sufficiently large \(N\), the exponents
\(t\in[a,2a]\) for which \(W-t\subset[a,2a]\) contain an interval of length
at least \(0.7a\).  On that interval, (A1) gives
\[
 \sum_{\substack{N^a<q\leq N^{2a}\\
                  \log q/L\in W-t}}\frac1q
 \geq c_0\frac h a .                                  \tag{A3}
\]
The reciprocal prime mass of the admissible \(t\)-interval is bounded below
by an absolute positive constant: partial summation from the PNT gives
\(\sum_{N^u<p\leq N^v}1/p=\log(v/u)+o(1)\) when
\(u,v\asymp a\) and \(v-u\gg a\).  Summing (A3) over the first prime proves
\[
 (\mu*\mu)(W)\geq c\frac h a.                          \tag{A4}
\]
For every real \(x\), the set \((W-x)\cap[a,2a]\) is contained in an
exponent interval of length \(h\).  The upper-bound form of (A1) therefore
gives
\[
 sup_x\mu(W-x)\leq C\frac h a.                        \tag{A5}
\]
The constants in (A4)--(A5) are uniform over the finite menu of \(a\)'s.
Their threshold in \(N\) may depend on the smallest menu element, hence on
\(K_1\), which is allowed.

Let \(\nu\) be the reciprocal measure of the deleted primes in this
interval and \(\mu^0=\mu-\nu\).  Since \(\|\nu\|\leq\varepsilon_0\),
\[
 (\nu*\mu)(W)
 \leq \|\nu\|\sup_x\mu(W-x)
 \leq C\varepsilon_0\frac h a.                        \tag{A6}
\]
Moreover,
\[
 \mu^{*2}-(\mu^0)^{*2}=\nu*\mu+\mu^0*\nu
 \leq2\nu*\mu
\]
as positive measures.  Choosing \(\varepsilon_0<c/(4C)\) in
(A4)--(A6) yields
\[
 ((\mu^0)^{*2})(W)\geq c'\frac h a                    \tag{A7}
\]
for every one of these local windows.  This proves (20)--(22) uniformly
even though the deleted prime set may vary arbitrarily with \(N\).

For clarity, the pigeonhole step fixes one block
\(i_0,\ldots,i_0+H-1\).  All its prime intervals lie below \(M_N\) for
large \(N\), because their upper endpoints are at most \(N^{1/4}\) while
\(M_N\geq c\sqrt N\).  If every interval in the block lost reciprocal mass
more than \(\varepsilon_0\), their disjointness would give total loss more
than \(H\varepsilon_0>K_1\), contradicting (14).  Thus the selected \(a\)
belongs to a fixed finite menu.

## 3. Rigorous convolution from (22) to (25)

Set
\[
 \eta=(\mu^0)^{*2},\qquad
 J=[2.95a,3.05a].
\]
Choose \(i_0\) large enough that, for the integer \(k\) nearest to
\(1/(3a)\), the compact interval \([1-2\delta,1]\) lies a fixed positive
distance inside \(kJ\).  This is possible uniformly over the finite menu:
the displacement of \(3ka\) from \(1\) is at most \(3a/2\), whereas the
half-width of \(kJ\) tends to \(1/60\) as \(a\) decreases.  Put \(r=2k\).

Here is a discrete proof that avoids any unmentioned local-limit theorem.
For the target window
\[
 T_s=[s-\log2/L,s],\qquad s\in[1-\delta,1],
\]
partition the interior of \(J\) into cells of length
\[
 h=\frac{\log2}{20kL}.
\]
For large \(N\), (A7) assigns every such cell mass at least \(c_a/L\).
The midpoint of \(T_s\) has, uniformly in \(s\), positive distance from the
boundary of \(kJ\).  Consequently there are \(\gg_a L^{k-1}\) choices of
cells for the first \(k-1\) variables such that a cell for the last variable
can be chosen inside \(J\) with the sum of the \(k\) cell centres at the
midpoint of \(T_s\), up to an error at most one cell length.  One concrete
way to see the count is to restrict each of the first \(k-1\) centres to a
fixed small interval about \(s/k\); the required last centre then remains a
fixed positive distance inside \(J\).  There are \(\gg_a L\) available
cells for each free centre.

The total variation of a sum inside the selected cells, including the
rounding error in the last centre, is less than the width of \(T_s\), by the
factor \(20k\) in the definition of \(h\).  Thus every corresponding cell
box contributes to \(\eta^{*k}(T_s)\).  These boxes are disjoint in their
first \(k-1\) coordinates, so (A7) gives
\[
 \eta^{*k}(T_s)
 \geq c_a L^{k-1}(c_a/L)^k
 \geq \frac{c'_a}{L}.                                  \tag{A8}
\]
Since \(\eta^{*k}=(\mu^0)^{*2k}=(\mu^0)^{*r}\), this is exactly (25).
The argument is uniform over the finite menu after taking the minimum of
the finitely many positive constants.

The repeated-prime removal is also uniform.  The reciprocal mass of tuples
having equality in any fixed pair of coordinates is at most
\[
 \left(\sum_{q>N^a}\frac1{q^2}\right)
 \left(\sum_{q\in I}\frac1q\right)^{r-2}
 =O_a(N^{-a}).                                         \tag{A9}
\]
There are only \({r\choose2}\) pairs, and \(r\) ranges over a finite menu.
Thus the total repeated-coordinate mass is \(o(1/L)\), strictly smaller
than the lower bound in (A8) for large \(N\).

## 4. The final prime and the conversion from mass to cardinality

Choose one fixed
\[
 0<\delta_0<\min\{\delta,\tfrac12\min_a a\},
\]
where the minimum is over the finite menu.  Then
\(N^{\delta_0}<M_N\) for large \(N\), and the PNT consequence
\(\sum_{p\leq x}1/p=\log\log x+O(1)\), together with (14), gives
\[
 \sum_{\substack{\ell\leq N^{\delta_0}\\
                   \ell\in\mathcal Z_N}}\frac1\ell
 \geq\log\log N-O_{K_1}(1).                           \tag{A10}
\]
For each such prime \(\ell\), (A8) applies with
\(s=1-\log\ell/L\).  Its convolution mass is the sum of
\(1/(q_1\cdots q_r)\) over ordered tuples satisfying (27).  Since each such
product is greater than \(N/(2\ell)\), every summand is at most
\(2\ell/N\).  Therefore the number of ordered tuples is at least
\(c_aN/(\ell L)\), which is (28), up to an absorbed constant.

All \(q_i>N^a>N^{\delta_0}\), whereas \(\ell\leq N^{\delta_0}\).  After
the repeated-prime tuples have been removed, the resulting integer is
squarefree and \(\ell\) is its unique prime factor below
\(N^{\delta_0}\).  Hence different \(\ell\)'s give disjoint integers, and
for one \(\ell\) unique factorisation leaves at most \(r!\) orderings.
Summing with (A10) proves (15).  The choice of \(i_0\) ensures
\(q_i\leq N^{2a}<N^{1/4}\), and the same is true of \(\ell\); all these
primes belong to \(\mathcal Z_N\) because \(N^{1/4}<M_N\) for large
\(N\).

## 5. Disjoint charge and conclusion

Every row error in Proposition 2 has largest prime factor greater than
\(M\).  Every integer supplied by Lemma 3 has largest prime factor less
than \(N^{1/4}<M\).  Thus the two charges are genuinely disjoint.

If \(m\leq K N/\log N\), Proposition 2 bounds the reciprocal mass of active
primes below \(M\) by a constant depending only on \(K\).  Lemma 3 then
gives
\[
 m\geq c_K\frac{N\log\log N}{\log N},
\]
contradicting the assumed upper bound for sufficiently large \(N\).  Since
this works for every fixed \(K\), the conclusion is the uniform statement
\(m=\omega(N/\log N)\).

No first false inference or exceptional parameter regime was found.  The
only changes needed for a self-contained presentation are the explicit
uniform PNT lemma (A1), the cell proof (A8), and the harmless clarification
that \(\delta_0\) is chosen uniformly over the finite menu of possible
exponents.
