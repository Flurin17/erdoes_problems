# Largest-prime profile induction

## Outcome

The proposed recursion has a rigorous conditional closure, but not an
unconditional one.  If the zero fibre of the grading is not exceptionally
dense on a harmonic majority of the dyadic cofactor scales, then the known
nonzero-level bound can be summed with largest-prime tags to give

\[
   |[1,N]\setminus f^{-1}(t)|
   \gg \frac{N\log\log N}{\log N}\qquad(t\ne0).
\]

The only way this induction can fail is now explicit.  On almost every
relevant outer band, almost every prime must have weight (t), thereby
sending the cofactor target to zero.  At a zero-target node, almost every
prime in almost every descendant band must have weight zero, and the zero
fibre must remain exceptionally dense.  Thus the obstruction is a
**one-(t)-tag followed by an all-zero spine**.  A threshold grading realizes
this profile exactly, so repeated invocation of the nonzero-level theorem
alone cannot close the argument.  The final section states a precise
complementary lemma which would close it.

This file concerns the repetition-allowed convention, where the grading
theorem is necessary.

## 1. Uniform lower envelope for nonzero targets

For a rational completely additive function (f), a rational target (u),
and an integer (X\ge1), put

\[
 D_f(u;X)=|\{n\le X:f(n)\ne u\}|.
\]

The proved finite theorem, after replacing (f) by (f/u), applies to
every (u\ne0).  Shrinking its absolute constant to cover the finitely many
small (X), there is an absolute (kappa>0) such that

\[
 D_f(u;X)\ge L(X):=\frac{\kappa X}{\log(eX)}
 \quad\text{for every }f, u\ne0, X\ge1. \tag{1}
\]

No analogous assertion is possible for (u=0), since (f\equiv0) has
zero deficiency at zero.  The point of the recursion below is to keep this
exception visible.

## 2. Exact tagged recurrence

Fix an integer (N), and let

\[
 C_j=2^j,
 \qquad
 P_j=\left\{p\text{ prime}:\frac{N}{2C_j}<p\le\frac{N}{C_j}\right\},
 \qquad R_j=|P_j|, \tag{2}
\]

where (0\le j\le J) and (C_J) is the largest power of two not exceeding
(sqrt N/4).  For any rational (t), define

\[
 Q_j(t)=|\{p\in P_j:f(p)=t\}|. \tag{3}
\]

### Lemma 1 (largest-prime tagged recurrence)

For every completely additive (f) and every (t\ne0),

\[
 \boxed{
 D_f(t;N)\ge
 \sum_{j=0}^{J}
 \left((R_j-Q_j(t))L(C_j)+Q_j(t)D_f(0;C_j)\right).}
 \tag{4}
\]

For the zero target, if

\[
 Z_j=|\{p\in P_j:f(p)=0\}|,
\]

then

\[
 \boxed{
 D_f(0;N)\ge
 \sum_{j=0}^{J}
 \left((R_j-Z_j)L(C_j)+Z_jD_f(0;C_j)\right).}
 \tag{5}
\]

#### Proof

Every (pk), with (p\in P_j) and (1\le k\le C_j), is at most (N).
All these products, over all (j,p,k), are distinct.  Indeed the prime
bands are disjoint, every participating prime is greater than
(2\sqrt N>C_J), and (pk=q\ell) with (p\ne q) would imply
(p\mid\ell) although (ell\le C_J<p).

For a fixed row (p\in P_j), the product (pk) misses the target (t)
exactly when

\[
 f(k)\ne t-f(p).
\]

Consequently the number of missed products in that row is exactly
(D_f(t-f(p);C_j)).  If (f(p)\ne t), its cofactor target is nonzero, so
(1) gives at least (L(C_j)) misses.  If (f(p)=t), the cofactor target is
zero and the exact number is (D_f(0;C_j)).  Summing is legitimate by the
global injectivity just proved, and gives (4).

For target zero, a row with (f(p)\ne0) has nonzero cofactor target
(-f(p)) and hence at least (L(C_j)) misses, while a row with (f(p)=0)
has exactly (D_f(0;C_j)) misses.  This proves (5).  \(□\)

Equations (4)--(5), rather than a heuristic density relation, are the exact
recurrences for this route.  They can be iterated.  At a child problem of
size (C_j), every new tag prime is larger than its new cofactor but smaller
than the parent tag.  Thus an iterated leaf has a strictly decreasing chain
of largest-prime tags.  Its tag chain can be recovered from its prime
factorization, so substitution of (5) into (4), and then of (5) into itself,
does not create double counting.

## 3. Conditional (N\log\log N/\log N) closure

The prime number theorem in dyadic intervals gives an absolute (c_P>0)
such that, uniformly for (2\le j\le J) and all sufficiently large (N),

\[
 R_j\ge c_P\frac{N}{C_j\log(N/C_j)}
       \ge c_P\frac{N}{C_j\log N}. \tag{6}
\]

Since (log(e2^j)\le2j) for (j\ge2), (1) and (6) imply, with
(b=c_P\kappa/2>0),

\[
 R_jL(C_j)\ge b\frac{N}{j\log N}. \tag{7}
\]

Set

\[
 \beta_j=1-\frac{Q_j(t)}{R_j},
 \qquad
 r_j=\frac{D_f(0;C_j)}{L(C_j)}. \tag{8}
\]

Then (4) and (7) give the quantitative profile recurrence

\[
 D_f(t;N)\ge
 b\frac{N}{\log N}
 \sum_{j=2}^{J}
 \frac{\beta_j+(1-\beta_j)r_j}{j}. \tag{9}
\]

In particular, because a convex combination of (1) and (r_j) is at
least (min(1,r_j)),

\[
 D_f(t;N)\ge
 b\frac{N}{\log N}
 \sum_{j=2}^{J}\frac{\min(1,r_j)}{j}. \tag{10}
\]

This completely closes the intended induction in the nonexceptional case.
If

\[
 D_f(0;C_j)\ge L(C_j)
 \quad(2\le j\le J), \tag{11}
\]

then

\[
 D_f(t;N)
 \ge b\frac{N}{\log N}\sum_{j=2}^{J}\frac1j
 \gg \frac{N\log\log N}{\log N}. \tag{12}
\]

More generally, (10) gives this conclusion whenever the scales on which
(r_j\) is bounded below have harmonic weight (gg\log\log N).

Conversely, if for a fixed (K)

\[
 D_f(t;N)\le K\frac{N}{\log N}, \tag{13}
\]

then (9) forces

\[
 \sum_{j=2}^{J}
 \frac{\beta_j+(1-\beta_j)r_j}{j}\le\frac Kb. \tag{14}
\]

The full harmonic sum is (log\log N+O(1)).  Thus, outside a set of
bounded harmonic weight, both (eta_j) and (r_j) must be small: almost
every prime in (P_j) has weight (t), and almost every integer up to
(C_j) has weight zero.  This is a rigorous structural consequence, not an
informal modal assertion.

## 4. What induction says at a zero-target node

Apply (5) at a node of size (X), using its own bands and writing

\[
 \alpha_ell
 =1-\frac{|\{q\in P_ell(X):f(q)=0\}|}{|P_ell(X)|},
 \qquad
 s_ell=\frac{D_f(0;2^ell)}{L(2^ell)}. \tag{15}
\]

Here (alpha_ell) is the proportion of active (nonzero-weight) tag primes.
The same proof as above yields

\[
 D_f(0;X)\ge
 b\frac{X}{\log X}
 \sum_{ell=2}^{J_X}
 \frac{\alpha_ell+(1-\alpha_ell)s_ell}{ell}. \tag{16}
\]

If the zero target is exceptional at this node,

\[
 D_f(0;X)<L(X), \tag{17}
\]

then (16) implies the scale-independent restriction

\[
 \sum_{ell=2}^{J_X}
 \frac{\alpha_ell+(1-\alpha_ell)s_ell}{ell}
 <\frac{\kappa}{b}. \tag{18}
\]

Hence an exceptional zero node can persist through many logarithmic scales
only if almost every descendant tag prime has weight zero and the child
zero target is again exceptional.  Iterating (18) gives the promised
profile:

\[
 \text{one outer tag of weight (t)}
 \quad\longrightarrow\quad
 \text{a descending chain of tags of weight (0)}. \tag{19}
\]

Every departure from (19) reaches a nonzero cofactor target and pays the
known cost (1).  The strictly descending largest-prime tags make all those
payments disjoint.

## 5. The obstruction is genuine for this recurrence

The profile (19) is not an artefact of an estimate.  For each (N), define

\[
 f_N(p)=
 \begin{cases}
 0,&p\le\sqrt N,\\
 t,&p>\sqrt N,
 \end{cases}
 \tag{20}
\]

and extend completely additively.  Every prime in every top-level (P_j)
has weight (t), while every (k\le C_J\le\sqrt N/4) has weight zero.
Thus

\[
 \beta_j=0,
 \qquad D_{f_N}(0;C_j)=0,
 \qquad r_j=0, \tag{21}
\]

at every scale in (9).  Every recursively generated zero node also has
zero deficiency.  The entire right side produced by the tagged induction
is therefore zero.

Nevertheless the actual complement of the (t)-level is large.  An
integer (n\le N) has value (t) exactly when it has one prime factor
greater than (sqrt N); all (sqrt N)-smooth integers have value zero.
The standard fixed-(u) Dickman estimate already used elsewhere in this
problem gives

\[
 D_{f_N}(t;N)=\Psi(N,\sqrt N)
 =(1-\log2+o(1))N. \tag{22}
\]

Thus there is ample deletion mass, but it lies outside the rectangles used
by (4).  This is a concrete falsification of any attempted proof that
merely substitutes the nonzero-target bound recursively and assumes a cost
must eventually occur.

## 6. Minimal missing lemma

Let

\[
 \mathcal R_N
 =\bigcup_{j=2}^{J}\{pk:p\in P_j, 1\le k\le C_j\},
 \qquad
 E_t(N)=\{n\le N:f(n)\ne t\}. \tag{23}
\]

The recurrence proves, inside this disjoint tagged region,

\[
 |E_t(N)\cap\mathcal R_N|
 \ge b\frac{N}{\log N}
 \sum_{j=2}^{J}\frac{\min(1,r_j)}j. \tag{24}
\]

Consequently the following is the precise complementary statement needed
to finish this route.

> **Zero-spine charging lemma (open).**  There is an absolute (b'>0)
> such that, for every completely additive (f), every (t\ne0), and all
> sufficiently large (N),
> \[
> |E_t(N)\setminus\mathcal R_N|
> \ge b'\frac{N}{\log N}
> \sum_{j=2}^{J}\frac{(1-r_j)_+}{j}. \tag{25}
> \]

Indeed, adding (24) and (25), and using

\[
 \min(1,r)+(1-r)_+=1,
\]

would prove the unconditional stronger bound

\[
 D_f(t;N)\gg\frac{N\log\log N}{\log N}. \tag{26}
\]

Equation (25) is the weakest scalar complement to (24): it charges only the
part of each harmonic scale not already paid for by the recursive
nonzero-level theorem, and it demands the charge outside the tagged region
so there is no overlap.  The threshold example (20) is consistent with it,
because its left side is of order (N), much larger than its required
(N\log\log N/\log N).

Proving (25) requires genuinely new input about the zero spine, not another
application of (1).  Plausible mechanisms are a Buchstab decomposition of
integers generated by zero-weight primes, or a second-largest-prime charge
which counts either two (t)-weighted tags or an untagged zero-smooth
integer.  Both must reserve sets disjoint from (mathcal R_N).

## 7. Falsification test and next action

The route survives exactly if (25), or a comparably strong disjoint
zero-spine penalty, is true.  A direct falsification target is an
(N)-dependent grading for which

\[
 \sum_{j=2}^{J}\frac{(1-r_j)_+}{j}\asymp\log\log N
 \quad\text{but}\quad
 |E_t(N)\setminus\mathcal R_N|=O(N/\log N). \tag{27}
\]

Single-threshold profiles do not do this; they have a linear supply of
untagged smooth omissions.  The next mathematical action should therefore
be one of:

1. prove (25) by decomposing the complement of (mathcal R_N) according to
   its largest two prime factors and charging an exceptional zero scale to a
   unique such pair; or
2. optimize two- and three-threshold prime-weight profiles specifically
   against (27).  A profile satisfying (27) would rigorously kill the
   proposed induction and identify the extra state variable a valid
   recurrence must retain.

At present (4)--(19) and the conditional improvement (12) are proved; the
unconditional improvement (26) is not claimed.
