# Notes for Erdős Problem #786

## Definitions and conventions

For \(n\geq1\), write
\[
 v(n)=(v_p(n))_{p\text{ prime}}\in\mathbb Z_{\geq0}^{(\mathcal P)}.
\]

Under the repetition-allowed reading, \(A\subset\mathbb N\) is
product-length rigid (PLR) when, for all \(r,s\geq1\),
\[
 \prod_{i=1}^r a_i=\prod_{j=1}^s b_j,\quad a_i,b_j\in A
 \quad\Longrightarrow\quad r=s.
\]

Under the internally repetition-free reading, each list has distinct
elements. After cancelling common elements, only coefficients in
\(\{-1,0,1\}\) occur. The readings differ: \(\{4,8\}\) is PLR with distinct
factors because its subset products are \(1,4,8,32\), but
\(4^3=8^2\) violates the repetition-allowed property.

The infinite density target is first read as natural density. Lower and upper
density are kept distinct. The set may depend on \(\epsilon\).

## Structural lemmas

### Integer-relation criterion

Assume \(1\notin A\). Then \(A\) is repetition-allowed PLR if and only if
every finitely supported integer family satisfies
\[
 \sum_{a\in A}z_av(a)=0
 \quad\Longrightarrow\quad
 \sum_{a\in A}z_a=0. \tag{1}
\]

To prove this, split \(z=z^+-z^-\). Equality of valuation sums is equality of
the corresponding products. A nonzero one-sided relation is impossible
because every \(a>1\); otherwise PLR equates the two multiplicity sums. The
converse follows by recording multiplicities in any product equality.

### Global grading theorem

For \(A\subset\mathbb N\setminus\{1\}\), the following are equivalent:

1. \(A\) is repetition-allowed PLR.
2. There is a homomorphism
   \(h:\langle v(A)\rangle_{\mathbb Z}\to\mathbb Z\) with \(h(v(a))=1\).
3. There is a rational linear functional
   \(L:\mathbb Q^{(\mathcal P)}\to\mathbb Q\) with \(L(v(a))=1\).
4. There are rational prime weights \(w_p\) such that the completely
   additive function
   \[
   f(n)=\sum_pw_pv_p(n)
   \]
   satisfies \(f(a)=1\) for every \(a\in A\).
5. \(0\notin\operatorname{aff}_{\mathbb Q}(v(A))\).

Let \(T:\mathbb Z^{(A)}\to\mathbb Z^{(\mathcal P)}\) send \(e_a\) to
\(v(a)\), and let \(\sigma(e_a)=1\). Criterion (1) says
\(\ker T\subseteq\ker\sigma\), exactly the condition that
\(h(Tz)=\sigma(z)\) be well-defined. Tensor with \(\mathbb Q\) and extend
linearly to the algebraic direct sum. A rational affine relation placing zero
in the affine hull is, after clearing denominators, precisely an integer
relation whose coefficient sum is nonzero.

For finite \(A\subset[1,N]\), if \(V_A\) is the valuation matrix, this gives
the exact arbitrary-length test
\[
 \operatorname{rank}_{\mathbb Q}V_A
 =
 \operatorname{rank}_{\mathbb Q}[V_A\mid\mathbf1]. \tag{2}
\]

For the repetition-free convention only
\[
 z\in\ker T\cap\{-1,0,1\}^{(A)}
 \quad\Longrightarrow\quad
 \sum_a z_a=0
\]
is necessary. A grading remains sufficient but is no longer necessary.

### Primitive cancellation

Cancelling a common occurrence from both sides preserves the product equality
and the length difference. Hence every bad relation has one with disjoint
multiset supports. A minimum-total-length bad relation has no proper
unequal-length subrelation.

### Boundary obstructions

- \(1\notin A\), since \(1=1\cdot1\).
- \(x,y,z\in A\) with \(xy=z\) is forbidden.
- \(x,y\in A\) with \(x^u=y^v\), \(u\neq v\), is forbidden under repetitions.
- Sharing a radical is not itself an obstruction; proportional valuation
  vectors are.

## Infinite obstruction

The complete proof is in PROOF.md. Its key probabilistic lemma is:

> A zero-drift compound-Poisson distribution on \(\mathbb Q\) with finite
> Lévy measure has every nonzero atom at most \(1/2\).

Under zeta probability \(\mu_s(n)=n^{-s}/\zeta(s)\), a rational completely
additive function is exactly such a compound-Poisson variable. Thus
\[
 \frac1{\zeta(s)}\sum_{f(n)=c}n^{-s}\leq\frac12
 \qquad(c\neq0,s>1). \tag{3}
\]
Partial summation and the grading theorem give
\[
 \underline d(A)\leq\frac12 \tag{4}
\]
for every repetition-allowed infinite PLR set. This resolves the infinite
question negatively under that convention.

The proof does not bound upper natural density alone and does not apply as a
necessary obstruction to the repetition-free convention.

## Finite results

### Threshold construction

For fixed \(2<u<3\), put \(y=N^{1/u}\) and
\[
 f(n)=\sum_{p>y}v_p(n).
\]
The exact level \(A_N(u)=\{n\leq N:f(n)=1\}\) is PLR. Let \(P_k\) be the
proportion having \(k\) prime factors above \(y\), counted with multiplicity.
Only \(k=0,1,2\) occur. The standard fixed-\(u\) Dickman theorem gives
\[
 P_0=\rho(u)+o(1),
\]
and prime-incidence counting plus Mertens' theorem gives
\[
 P_1+2P_2=\log u+o(1).
\]
Therefore
\[
 P_1=2-2\rho(u)-\log u+o(1). \tag{5}
\]
Since \(u\rho'(u)=-\rho(u-1)\) and
\(\rho(u-1)=1-\log(u-1)\), (5) is maximized at
\[
 u_*=1+\sqrt e.
\]
The resulting density is
\[
 c_*=2-2\rho(1+\sqrt e)-\log(1+\sqrt e)
 =0.828499\ldots . \tag{6}
\]

### Dirichlet lower bound on deletions

If \(m_N=N-|A_N|\), the zeta anti-atom inequality and rearrangement give
\[
 \sum_{n=m_N+1}^{N}n^{-s}\leq\frac12\zeta(s).
\]
Taking \(s=1+c/\log N\) yields
\[
 m_N+1\geq N^{\beta_*-o(1)}, \tag{7}
\]
where \(\beta_*=0.227092\ldots\) is the unique root of
\[
 (1-\beta)\beta^{\beta/(1-\beta)}=\frac12.
\]
No matching construction is known, so this exponent is not called sharp.

### Active-prime and smooth-number bound

If \(f(p)\neq0\), a level set meets each \(p\)-adic chain at most once:
\[
 m_N\geq\left\lfloor\frac Np\right\rfloor. \tag{8}
\]
Thus all weights vanish for
\[
 p\leq y_N=\left\lfloor\frac{N}{m_N+1}\right\rfloor,
\]
and every \(y_N\)-smooth integer is omitted:
\[
 m_N\geq\Psi(N,y_N). \tag{9}
\]
The fixed-\(u\) Dickman asymptotic implies
\[
 m_N=o(N)\quad\Longrightarrow\quad m_N=N^{1-o(1)}. \tag{10}
\]
This remains compatible with \(m_N=N/\log N\).

### Bounded bad witnesses and modular lift

Let \(d=\pi(N)\) and \(L=\lfloor\log_2N\rfloor\). If a finite set is not
PLR, a cofactor/Hadamard argument produces an unequal-length relation
supported on at most \(d+1\) elements and with total multiplicity at most
\[
 B_N=(d+1)L^d. \tag{11}
\]
Consequently modular grading certificates whose moduli have least common
multiple greater than \(B_N\) imply exact PLR. This solves the unbounded
length issue but not the dense-level construction.

## Transfer cautions

- A modular level-one certificate gives only \(r\equiv s\pmod m\) without
  (11), an unbounded-lcm family, or another torsion-free lift.
- Coordinatewise compactness preserves fixed forbidden relations but can lose
  density.
- Unions of dense rigid blocks can create cross-block relations.
- Exclusive protected prime markers give exact cross-block rigidity but have
  density at most \(1/e\).

## Current finite bottleneck

Under repetitions, decide whether an \(N\)-dependent completely additive
rational function can have an exact nonzero level containing \(1-o(1)\) of
\([1,N]\). A positive construction must delete \(N^{1-o(1)}\) elements; a
negative result needs anti-concentration sufficiently uniform for the
uniform measure on \([1,N]\).

For distinct factors, the grading reduction is unavailable. A top-slab
reduction makes every unequal-cardinality relation long, but a sparse
transversal theorem for the resulting relation hypergraph is still missing.
