# Modular certificates and an exact bounded-witness lift

## Mechanism

A modular grading (f_m(a)\equiv1\pmod m) only gives
\(r\equiv s\pmod m).  For a finite set, however, every failure of exact PLR
has a bounded integer witness.  Modular certificates whose least common
multiple exceeds that bound therefore imply exact PLR for arbitrary lengths.

## Bounded-witness lemma

Let (S\subset[2,N]), let (d=\pi(N)), and let (V) be its valuation matrix.
Put (L=\lfloor\log_2N\rfloor).  If (S) is not PLR, then it has an
unequal-length product relation supported on at most (d+1) distinct elements
and having total multiplicity at most
\[
B_N=(d+1)L^d. \tag{1}
\]

**Proof.**  Let (r=\operatorname{rank}_{\mathbb Q}V).  Failure of PLR means
\(\operatorname{rank}[V\mid\mathbf1]=r+1).  Choose (r+1) rows and (r)
valuation columns such that the resulting square matrix
\(C=[B\mid\mathbf1]) has nonzero determinant.  Let (z_i) be the signed
cofactors of the last column.  Then
\[
z^TB=0,\qquad \sum_i z_i=\det C\ne0.
\]
The chosen columns have rank (r), so on these rows they span the restrictions
of every valuation column; hence (z^TV=0).  Each valuation row has Euclidean
norm at most \(\Omega(n)\le L\).  Hadamard's inequality yields
\(|z_i|\le L^r\), hence
\(\|z\|_1\le(r+1)L^r\le B_N\).  Nonzero nonnegative valuation vectors prevent
all coefficients from having the same sign.  Splitting (z=z^+-z^-) gives
the claimed product equality, and (\sum z_i\ne0) makes its lengths unequal.
∎

## Exact modular-lift corollary

Suppose that for moduli (m_1,\ldots,m_t) there are prime weights modulo
(m_j) satisfying (Vw_j=\mathbf1\pmod {m_j}).  Every bad witness (z)
would obey
\[
\sum_i z_i\equiv0\pmod {m_j}\quad(1\le j\le t).
\]
Thus (\operatorname{lcm}(m_1,\ldots,m_t)) divides the nonzero integer
\(\sum z_i\).  If the lcm exceeds (B_N), this contradicts (1), so (S) is
exactly PLR.

For an infinite set, compatible certificates into a product
\(\prod_j\mathbb Z/m_j\mathbb Z) with unbounded lcm also give exact rigidity:
the diagonal element ((1,1,\ldots)) has infinite additive order.

## Density target and limitation

If certificate (j) fails on at most (\delta_jN) integers, their common
level set has size at least \((1-\sum_j\delta_j)N\).  The remaining bottleneck
is therefore to achieve simultaneously
\[
\operatorname{lcm}(m_j)>B_N,
\qquad \sum_j\delta_j=o(1).
\]
No such concentration lemma is known locally.  Random uniform prime labels
are unsuitable: for a large prime modulus their expected level mass is about
(1/m), not (1-o(1)).

## Falsification and next action

For any proposed modular construction, form its common level set and use the
rank test.  If it fails, the cofactor proof above extracts an explicit bad
relation, showing exactly where an insufficient lcm or inconsistent grading
entered.  The next action is to combine this lift with a genuinely
high-concentration modular construction, if one exists.
