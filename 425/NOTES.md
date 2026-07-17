# Notes for Erdős Problem #425

All logarithms are natural.  Statements labeled “standard input” are not
proved here; all other lemmas in this file include their proof or a direct
proof reference within the file.

## 1. Normalized statement

For a positive integer $n$, write $[n]=\{1,\dots,n\}$.  For a finite set
$A$ of positive integers and $0\le r\le |A|$, define
\[
 \mu_{A,r}:\binom Ar\longrightarrow\mathbb N,
 \qquad \mu_{A,r}(S)=\prod_{a\in S}a.
\]
Thus the factors in a product are distinct elements of $A$; repetitions and
diagonal pairs are not in the domain.  Let
\[
 F_r(n)=\max\{|A|:A\subseteq[n],\ \mu_{A,r}\text{ is injective}\},
 \qquad F(n)=F_2(n).
\]

The source's first sentence uses $A\subseteq[N]$ while naming the function
$F(n)$.  With unrelated $N$ and $n$ this leaves a free variable and does not
define a one-variable function.  The two coherent repairs—replace $N$ by $n$,
or name the function $F(N)$ and then rename the dummy variable—are identical.
We therefore normalize to $N=n$.  A fixed independent $N$ would make $F(n)$
constant, while an unstated $N=N(n)$ would define an underdetermined two-scale
problem.

The pair question is precisely whether there is a real $c$ such that
\[
 \lim_{n\to\infty}
 \frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}=c.
\]
The fixed-$r$ question is read as follows: for every fixed integer $r\ge2$,
do there exist $C_r$ and $n_0(r)$ such that, for all $n\ge n_0(r)$ and all
$A\subseteq[n]$,
\[
 \mu_{A,r}\text{ injective}
 \quad\Longrightarrow\quad
 |A|\le\pi(n)+C_r n^{(r+1)/(2r)}?
\]
The source does not support a constant uniform in varying $r$.  Indeed, if
$r=n$ and $A=[n]$, there is only one $r$-subset, whereas an absolute-uniform
version of the displayed bound fails for large $n$.

## 2. Pair-product collision lemmas

### Lemma 2.1 (four-distinct criterion)

The following are equivalent for a finite $A\subset\mathbb N$.

1. $\mu_{A,2}$ is injective.
2. If $a,b,c,d\in A$, $a\ne b$, $c\ne d$, and $ab=cd$, then
   $\{a,b\}=\{c,d\}$.
3. There are no four pairwise distinct $a,b,c,d\in A$ with $ab=cd$.

Proof.  Only (2)$\Rightarrow$(3) needs no comment.  If two colliding valid
pairs share an element, cancellation forces their other elements to agree,
so the pairs are identical.  Hence every nontrivial collision uses four
distinct elements, proving the converse.  ∎

In particular, equations $ab=c^2$ are allowed: the diagonal $\{c,c\}$ is
not in $\binom A2$.  For example, $\{1,2,4\}$ is admissible.

### Lemma 2.2 (multiplicative rectangles)

Every nontrivial equation $ab=cd$ has the form
\[
 (gx)(hy)=(gy)(hx),
\]
where $a=gx$, $c=gy$, $b=hy$, $d=hx$, and $(x,y)=1$.

Proof.  Put $g=(a,c)$, $a=gx$, $c=gy$.  From $xb=yd$ and $(x,y)=1$,
there is an integer $h$ with $b=hy$ and $d=hx$.  The converse identity is
immediate.  ∎

Consequently, in the bipartite divisor graph having an edge $(u,v)$ labelled
$uv$ whenever $uv\in A$, pair-product injectivity is exactly the absence of a
$C_4$ whose four edge labels are pairwise distinct.  Ordinary $C_4$-freeness
is stronger: repeated labels can occur among different factorizations of one
element.

### Lemma 2.3 (valuation and restricted-energy formulations)

Let $v(a)=(v_p(a))_p$.  Then $A$ is admissible exactly when all sums
$v(a)+v(b)$ with $\{a,b\}\in\binom A2$ are distinct.

For
\[
 k_A(t)=\#\{\{a,b\}\in\tbinom A2:ab=t\},
\]
this is also equivalent to
\[
 \sum_t k_A(t)^2=\binom{|A|}{2}.
\]
If ordered restricted energy counts $(a,b,c,d)$ with $a\ne b$, $c\ne d$,
and $ab=cd$, then admissibility is equivalent to
\[
 E^\times_{\ne}(A)=2|A|(|A|-1).
\]

Proof.  The valuation assertion is unique factorization.  Since
$\sum_tk_A(t)=\binom{|A|}{2}$ and $k^2\ge k$, equality holds exactly when
each $k_A(t)$ is $0$ or $1$.  Each unordered representation has two
orientations on each side, giving the ordered formula.  ∎

Ordinary multiplicative energy is not interchangeable with restricted
energy.  If
\[
 T(A)=\#\{(c,\{a,b\}):c\in A,\ \{a,b\}\in\tbinom A2,\ ab=c^2\},
\]
then direct separation of diagonal and non-diagonal ordered pairs gives
\[
 E^\times(A)=E^\times_{\ne}(A)+|A|+4T(A).
\]

### Lemma 2.4 (the element $1$)

If $1\notin B$, then $B\cup\{1\}$ is pair-admissible exactly when $B$ is
pair-admissible and no element of $B$ is the product of two distinct elements
of $B$.

Proof.  The only new products are $1\cdot b=b$.  Two such products cannot
collide, and a collision with an old pair product is exactly $b=xy$ for
distinct $x,y\in B$.  ∎

Thus adjoining $1$ is not automatic; for instance, $\{2,3,6\}$ is admissible
but adjoining $1$ creates $1\cdot6=2\cdot3$.

## 3. Arithmetic layers and exact semiprime graphs

Write $\Omega(m)=\sum_pv_p(m)$ and $\omega(m)=|\{p:p\mid m\}|$.

- Primes are unit valuation vectors.
- Pure prime powers $p^k$ lie on one coordinate ray.
- Squarefree semiprimes $pq$ are edges on prime vertices.
- Squares $p^2$ are loops and must not be silently placed in a simple graph.

The number of pure prime powers of exponent at least two is
\[
 \sum_{k=2}^{\lfloor\log_2n\rfloor}\pi(n^{1/k})=O(\sqrt n)
 =o\!\left(n^{3/4}(\log n)^{-3/2}\right).
\]
This count does not make prime powers freely addable; for example
$p^2\cdot qr=(pq)(pr)$ is a genuine collision when all four displayed
elements are present.

For a threshold $y$, every integer has the unique smooth/rough split
\[
 m=s_y(m)r_y(m),\qquad
 s_y(m)=\prod_{p\le y}p^{v_p(m)},\quad
 r_y(m)=\prod_{p>y}p^{v_p(m)}.
\]
If $y\ge n^{1/(k+1)}$, then a $y$-rough integer at most $n$ has at most $k$
prime factors counted with multiplicity.  At $y=\sqrt n$, every integer with
a prime factor $q>\sqrt n$ has the unique form $qu$, where $u<\sqrt n$.

### Lemma 3.1 (semiprime graph equivalence)

Let $G$ be a simple graph on a set of primes and
\[
 B(G)=\{pq:\{p,q\}\in E(G)\}.
\]
Then $B(G)$ is pair-admissible if and only if $G$ is $C_4$-free.

Proof.  A $C_4$ on $p_1,p_2,q_1,q_2$ gives
\[
 (p_1q_1)(p_2q_2)=(p_1q_2)(p_2q_1).
\]
Conversely, unique factorization says two edge pairs with equal products have
the same prime-degree vector.  If the two edges share a vertex, that degree
pattern determines the pair.  If they are disjoint, a different decomposition
is the other perfect matching on the same four vertices, and the four edges
form a $C_4$.  ∎

If loops $p^2$ are admitted, one must additionally forbid the looped-triangle
configuration $\{p^2,qr,pq,pr\}$.

### Lemma 3.2 (clean replacement construction)

Let $X,Y$ be disjoint prime sets, let $G\subseteq X\times Y$ be a bipartite
$C_4$-free graph with $xy\le n$ on every edge, and put
\[
 A=\bigl(\{p\le n:p\text{ prime}\}\setminus(X\cup Y)\bigr)
   \cup\{xy:(x,y)\in E(G)\}.
\]
Then $A$ is pair-admissible and
\[
 |A|=\pi(n)-|X|-|Y|+e(G).
\]

Proof.  Edge labels are distinct by unique factorization.  The number
$\Omega$ shows that colliding pairs would have the same number of semiprime
members.  Prime-prime collisions are trivial.  In a prime-semiprime collision,
the retained prime class and the disjoint endpoint classes $X,Y$ decode all
three factors uniquely.  Two-semiprime collisions are exactly the $C_4$
configuration of Lemma 3.1.  ∎

This lemma separates the contributions of retained primes and semiprimes.
Prime powers contribute only $o$ of the target scale by count.  Integers with
at least three prime factors, integers with a prescribed small prime factor,
and rough integers still require global upper-bound control; no negligibility
claim for those classes has yet been proved.

## 4. Why the secondary scale appears

Let
\[
 L=\frac{\sqrt n}{\log n}.
\]
By the prime number theorem (standard input),
\[
 \pi(\sqrt n)=(2+o(1))L.
\]
The standard extremal result
\[
 \operatorname{ex}(m,C_4)=\left(\frac12+o(1)\right)m^{3/2}
\]
then gives a clean first construction: use a nearly extremal $C_4$-free graph
on the primes at most $\sqrt n$, replace those primes by its edge products,
and retain all larger primes.  Lemma 3.2 (or its one-part analogue) gives
\[
 |A|=\pi(n)+(\sqrt2+o(1))L^{3/2}.
\]
The endpoint cost is only $O(L)=o(L^{3/2})$.  Thus the exponent and logarithm
come from
\[
 \#\{p\le\sqrt n\}\asymp L,
 \qquad \operatorname{ex}(L,C_4)\asymp L^{3/2}.
\]

An unbalanced hyperbolic rectangle gives a stronger candidate lower constant.
For $0<t<1$, take
\[
 X=\{p:p\le t\sqrt n\},\qquad
 Y=\{p:t\sqrt n<p\le t^{-1}\sqrt n\}.
\]
Then every $xy$ is at most $n$, and PNT gives
\[
 |X|=(2t+o(1))L,\qquad
 |Y|=(2(t^{-1}-t)+o(1))L.
\]
A projective-plane incidence graph on the larger side, restricted on the
smaller side, suggests and (subject to the standard finite-field-size
selection being written uniformly) yields
\[
 e(G)=(1+o(1))\min\{|X|\sqrt{|Y|},\ |Y|\sqrt{|X|}\}.
\]
In the regime $|X|\le|Y|$, the coefficient
\[
 2t\sqrt{2(t^{-1}-t)}
\]
is maximized at $t=3^{-1/2}$ and equals
\[
 c_{\rm rect}=\frac4{3^{3/4}}\approx1.754765.
\]
This single rectangle is superseded by the following proved multiscale
theorem.

### Theorem 4.1 (Bellman-optimized reciprocal annuli)

\[
 \liminf_{n\to\infty}
 \frac{F(n)-\pi(n)}
      {n^{3/4}(\log n)^{-3/2}}
 \ge \frac{2^{11/4}}{3^{3/4}}=2.951151\ldots .
\]

For decreasing boundaries \(b_{-1},b_0,b_1,\ldots\), with
\(b_{-1}b_0=1\), pair
\[
 X_j=(b_{j+1}\sqrt n,b_j\sqrt n],\qquad
 Y_j=(\sqrt n/b_{j-1},\sqrt n/b_j].
\]
The coefficient is
\[
 2\sqrt2\sum_{j\ge0}
 (b_j-b_{j+1})\sqrt{1/b_j-1/b_{j-1}}.
\]
Writing \(r_j=b_j/b_{j-1}\), the Bellman inequality
\[
 (1-s)\sqrt{1-r}+\sqrt{s(2-s)}\le\sqrt{2-r}
\]
telescopes. Equality starts with \(b_0=\sqrt{2/3}\) and obeys
\[
 \delta_0=1/3,\qquad
 \delta_{j+1}=\sqrt{\delta_j/(1+\delta_j)},\qquad
 r_j=1-\delta_j.
\]
The complete collision, projective-plane sizing, orientation, and limiting
argument is in PROOF.md. This optimizes the disjoint interval-incidence
architecture only; coupled components remain a separate question.

For reference, the elementary bipartite $C_4$ count gives, for part sizes
$s,t$ and $e$ edges,
\[
 e\le t+s\sqrt t,\qquad e\le s+t\sqrt s.
\]
Indeed, two vertices on one side have at most one common neighbor, so
$\sum_y\binom{d(y)}2\le\binom s2$; Cauchy--Schwarz and rearrangement give the
first bound, and symmetry gives the second.

## 5. Fixed-$r$ structure

Write $P_r(A)$ for injectivity of $\mu_{A,r}$ and $m=|A|$.

### Lemma 5.1 (exact collision-rank criterion)

Define $\kappa(A)$ to be the least $k$ for which there are disjoint
$U,V\subseteq A$ satisfying
\[
 |U|=|V|=k,\qquad \prod U=\prod V,
\]
and put $\kappa(A)=\infty$ if no such relation exists.  Then
\[
 P_r(A)\quad\Longleftrightarrow\quad
 \kappa(A)>\min(r,m-r).
\]

Proof.  A collision between two $r$-subsets cancels their intersection and
leaves disjoint equal-product $k$-subsets.  Their union with the common part
has size $r+k\le m$, so $k\le\min(r,m-r)$.  Conversely, if such a disjoint
relation has $k\le r$ and $k\le m-r$, choose $r-k$ common elements outside
$U\cup V$ and pad both sides.  A rank-one relation cannot occur in a set of
distinct integers.  ∎

Consequences include:

- Complement duality:
  \[
  P_r(A)\Longleftrightarrow P_{m-r}(A).
  \]
- More strongly, with $s=\min(r,m-r)$,
  \[
  P_r(A)\Longleftrightarrow\bigwedge_{j=1}^{s}P_j(A).
  \]
- If $1\le s\le r$ and $m\ge r+s$, then $P_r(A)\Rightarrow P_s(A)$.
  In particular, $P_r(A)$ and $m\ge r+2$ imply pair admissibility.
- $P_r(A)$ is automatic for $m<r$, $m=r$, and $m=r+1$; hence
  $F_r(n)=n$ for $n\le r+1$.
- Fixed-r injectivity has no unconditional monotonicity in $r$:
  $\{1,2,3,6\}$ has $P_3$ but not $P_2$, while
  $\{1,2,6,7,15,35\}$ has $P_2$ but not $P_3$ because
  $1\cdot6\cdot35=2\cdot7\cdot15$.

In valuation language, if $M$ has columns $v(a)$, then $P_r(A)$ says that
$M$ is injective on $\{0,1\}$-vectors of Hamming weight $r$.  Equivalently,
there is no nonzero $z\in\{-1,0,1\}^m$ with $Mz=0$ and equal positive and
negative support sizes at most $\min(r,m-r)$.

For a semiprime graph, an $r$-fold product is its selected edges' vertex-degree
vector.  Thus the obstruction is an edge-disjoint red/blue configuration with
equal red and blue degrees and at most $r$ edges of each color.  Even cycles
provide such trades, but forbidding short even cycles alone is not sufficient:
for $r=3$, two triangles sharing one vertex support a balanced $3$-versus-$3$
trade without containing an even cycle.

## 6. Boundary facts

- $F_r(n)\le F_r(n+1)\le F_r(n)+1$, by inheritance and deletion of $n+1$.
- $\{1\}\cup\{p:p\le n\text{ prime}\}$ has $P_r$ for every $r$, so
  $F_r(n)\ge\pi(n)+1$.
- Direct checking gives
  \[
  \begin{array}{c|ccccccccc}
  n&1&2&3&4&5&6&7&8&9\\ \hline
  F(n)&1&2&3&4&5&5&6&6&7.
  \end{array}
  \]
  These values are normalization checks, not evidence for an asymptotic.

## 7. Current open obligations

1. Decide whether the explicit coupled four-part \(C_4\)-free packing can
   beat the proved Bellman coefficient; ordinary two-path inequalities do not
   decide it.
2. Close the critical-band cross-kernel upper lemma after applying canonical
   roughness, colored rectangles, exchange charging, and the proved tail
   bounds.
3. Determine whether the weighted semiprime optimum has a limit and prove
   that higher-composite layers cannot improve the resulting constant.
4. For fixed \(r\), prove the remaining smooth-core estimate after the
   large-largest-prime reduction, or construct a counterexample.
