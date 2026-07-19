# Sharp shell obstructions to endpoint rounding

## Status

The results here do not refute a universal bounded-weight deletion theorem.
They prove that two simpler versions are false:

1. contradictory endpoint cycles need not force superlinear scale growth;
2. the repair cost in one multiplicative shell can be of the full order
   $1/\log N$.

Throughout, equal rounded labels may be collapsed. Only proper divisibility
between distinct selected integers is treated as a conflict. This is enough
for the target series because adjacent labels have multiplicity at most two.

## 1. A fixed seven-point linear-span contradiction

For an integer $t\ge34$, let $G_t$ consist of the seven half-integers whose
floors are
\[
t,\quad 2t-1,\quad 2t+2,\quad 3t-1,\quad 3t+3,
\quad 6t-3,\quad 6t+8.                                  \tag{1}
\]

**Proposition 1.** The set $G_t$ is admissible and has no primitive
floor/ceiling labeling. Its exact minimum deletion cost is the weight of its
largest point,
\[
f(6t+17/2).                                               \tag{2}
\]

**Proof.** Doubling the points gives the odd integers
\[
2t+1,\ 4t-1,\ 4t+5,\ 6t-1,\ 6t+7,\ 12t-5,\ 12t+17.
\]
For two half-integers $P/2<Q/2$, admissibility is equivalent to
\[
\min_{k\ge1}|kP-Q|\ge2.                                  \tag{3}
\]
For the $21$ pairs above, the upper-triangular table of these minima is
\[
\begin{array}{c|rrrrrr}
0&3&3&4&4&11&11\\
1&&6&2t-1&2t-9&2&20\\
2&&&2t-6&2t+2&20&2\\
3&&&&8&3&19\\
4&&&&&19&3\\
5&&&&&&22
\end{array}                                               \tag{4}
\]
and every entry is at least $2$.

Let a bit choose floor or ceiling. The following eight proper divisibilities
occur:
\[
\begin{gathered}
t\mid2t,\qquad t+1\mid2t+2,\qquad
t\mid3t,\qquad t+1\mid3t+3,\\
2t-1\mid6t-3,\qquad 3t-1\mid6t-2,\\
2t+3\mid6t+9,\qquad 3t+4\mid6t+8.                       \tag{5}
\end{gathered}
\]
If the first point is rounded down, the first and third relations force the
$2t-1$ and $3t-1$ points down. The next two relevant relations then force
the $6t-3$ point both up and down. If the first point is rounded up, the
second and fourth relations force the $2t+2$ and $3t+3$ points up, after
which the last two relations force the $6t+8$ point both down and up.

For $t\ge34$, a direct comparison of the linear endpoint forms shows that
(5) is the complete list of proper endpoint divisibilities. Deleting the
largest point and choosing states
\[
(\text{up},\text{up},\text{up},\text{up},\text{up},
  \text{down})
\]
on the remaining six points avoids all eight conflicts. At least one point
must be deleted, and the largest has the least $f$-weight, proving (2).
$\square$

This proposition disproves any assertion that every contradictory endpoint
cycle contains a point quadratic in the least point. The double-clause local
lemma remains true: two different endpoint conflicts on one variable pair
force the larger floor to be at least $m^2-1$. The cycle in (5) evades it by
using one clause per pair and balancing upward and downward multipliers.

## 2. Linear packing of the seven-point cores

The fixed cores themselves can be packed throughout one shell. Take all
integers of one parity in
\[
T\le t\le1.01T,
\]
with $T$ sufficiently large, and form their union $\mathcal G_T$.

For a doubled point write
\[
P_i(t)=a_it+b_i,
\quad
a=(2,4,4,6,6,12,12),
\quad
b=(1,-1,5,-1,7,-5,17).                                  \tag{6}
\]
If a cross-copy pair violated admissibility, then
\[
|kP_i(t)-P_j(s)|\le1                                    \tag{7}
\]
for some $k\le6$. If $ka_i\ne a_j$, then
\[
|kP_i(t)-P_j(s)|
\ge (2-0.84)T-119>1.                                    \tag{8}
\]
If $ka_i=a_j$, the same-parity condition makes $t-s$ a nonzero even integer.
The nine possible slope matches have respective minimum absolute gaps
\[
4,5,8,13,2,4,4,5,2,                                    \tag{9}
\]
so (7) is again impossible. Thus $\mathcal G_T$ is admissible.

It contains $\Theta(T)$ disjoint copies of Proposition 1, all inside
$[T,7T]$. Every repair must delete one point from every copy, while deleting
the whole block costs $O(1/\log T)$. Hence its optimum deletion weight obeys
\[
\tau_f(\mathcal G_T)=\Theta(1/\log T).                  \tag{10}
\]

## 3. A simpler mixed-block obstruction without injectivity

The order in (10) already follows from a more elementary family. For
$N\ge2$, put
\[
M=\left\lfloor\frac{3N-2}{2}\right\rfloor
\]
and
\[
A_N=\{p+1/2:N\le p\le M\}
\ \cup\ \{2r:N\le r\le M+1\}.                          \tag{11}
\]

**Proposition 2.** The set $A_N$ is admissible. Any deletion permitting a
primitive adjacent labeling has weight at least
\[
\frac{M-N+1}{2}\,f(3N)\gg\frac1{\log N}.               \tag{12}
\]
Conversely, a deletion of weight $O(1/\log N)$ suffices.

**Proof.** The half-integer and integer parts separately lie in intervals of
ratio below $2$. For $x=p+1/2$ and $y=2r$, the multiplier-$2$ gap is a
nonzero odd integer. Moreover
\[
3(N+1/2)-2(M+1)\ge3/2,
\]
so all multipliers $k\ge3$ are also safe; $k=1$ is immediate. Thus (11) is
admissible.

Let $L=M-N+1$ be the number of half-integers. After a repair, let $d$ of
them be deleted and let $Q_0$ be the set of distinct integer labels chosen
for the remaining half-integers. Every $q\in Q_0$ lies in $[N,M+1]$, and
the point $2q$ occurs in (11). It must therefore be deleted, since
$q\mid2q$ properly. One label can serve at most two of the consecutive
half-integers, so
\[
L-d\le2|Q_0|\le2|D\cap2\mathbb Z|.
\]
It follows that $|D|\ge L/2$. All points in (11) are at most $3N$, giving
(12).

For the reverse bound, delete $2(N+1),\ldots,2(M+1)$, round every
half-integer up, and retain $2N$. The chosen labels
$N+1,\ldots,M+1$ lie in an interval of ratio below $2$, and none divides
$2N$. They therefore form a primitive set with $2N$. The deleted weight is
$O(1/\log N)$. $\square$

## 4. A sharp threshold for the stricter injective model

This section records a separate obstruction in which equal rounded labels
are forbidden. It does **not** apply after equal labels are collapsed as in
the main reduction above, because consecutive-label equalities are essential
to its implication chain.

Let $H$ be an admissible set of half-integers $n+1/2$ whose distinct floors
lie in $[N,3N]$. Rounding every point up gives distinct labels, and those
labels are primitive. Indeed, a proper divisibility would have the form

\[
m+1=k(n+1),\qquad n<m.
\]

The case $k=2$ would give
$|2(n+1/2)-(m+1/2)|=1/2$, contrary to admissibility, while $k\ge3$ gives
$m\ge3N+2$. Thus injective primitive rounding always succeeds through
aspect ratio $3$.

This constant is sharp. For every even $a\ge10$, set
\[
z=\frac{3a+4}{2},\quad u=z+1,\quad B=3a+3,\quad D=3a+8,
\]
\[
E=\{a,a+1,a+2,a+3\}\cup[2a+8,3a-1],\qquad
S_a=E\cup\{z,u,B,D\},                                  \tag{13}
\]
where the interval denotes its integer points, and take the half-integers
\[
H_a=\{n+1/2:n\in S_a\}.
\]

For floors $n<m<4n$, the two half-integers fail admissibility exactly when
\[
m\in\{2n,2n+1,3n+1\}.                                  \tag{14}
\]
To see this, put $P=2n+1$ and $Q=2m+1$. Failure means
$|kP-Q|\le1$ for some integer $k\ge1$; parity and $P<Q<4P$ leave precisely
the three possibilities in (14).

All floors in (13) lie below $4a$. For $n=a,a+1,a+2,a+3$, the bad doubles
in (14) fill $[2a,2a+7]$ and the bad triples are
$3a+1,3a+4,3a+7,3a+10$, none of which lies in $S_a$. For $n=z,u$, the bad
doubles fill $[3a+4,3a+7]$, again missing $S_a$; for $n\ge2a+8$, every bad
value exceeds $D$. Hence $H_a$ is admissible.

Write $\varepsilon_n\in\{0,1\}$ for the floor/ceiling choice. Injectivity on
consecutive floors gives $\varepsilon_n\le\varepsilon_{n+1}$. These
implications run through both intervals in $E$; the relations
\[
2a+8=2(a+4),\qquad 3a=3a
\]
close the chain and force all bits on $E$ equal. Since
\[
B=3(a+1),\qquad D+1=3(a+3),
\]
one of the two adjacent copies of $a+1$ always forces
$\varepsilon_B=1$, while one of the two adjacent copies of $a+3$ always
forces $\varepsilon_D=0$. Finally,
\[
B+1=2z,qquad u=z+1,qquad D=2(u+1)
\]
gives
\[
\varepsilon_B=1\Longrightarrow\varepsilon_z=1
\Longrightarrow\varepsilon_u=1\Longrightarrow\varepsilon_D=1,
\]
a contradiction. Thus $H_a$ has no injective primitive adjacent labeling,
and its floor aspect ratio is $3+8/a$. For every fixed $C>3$, sufficiently
large windows $[N,CN]$ therefore contain such a counterexample.

## 5. Consequence

No proof can assign a summably smaller budget to each shell merely because
an endpoint formula is contradictory: the optimal repair itself can cost
the full shell order $1/\log N$. A universal bounded deletion theorem, if
true, must prove that such critical shells cannot recur with divergent total
weight under all cross-scale admissibility constraints. Constructing a
cross-admissible sequence of critical shells would instead give a negative
solution to Problem 143.
