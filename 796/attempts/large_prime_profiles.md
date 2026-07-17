# Route: compatible large-prime profiles

## Mechanism

For each prime \(p>\sqrt n\), write selected elements as \(pd\), where
\(d\leq\lfloor n/p\rfloor\).  If
\[
\mu_{U,V}(t)=\#\{(u,v)\in U\times V:uv=t\},
\]
then two distinct prime labels \(p,q\) turn coefficient solutions into
representations of \(pqt\).  Thus a family of profiles \(D_k\subseteq[k]\)
with \(\mu_{D_i,D_j}\leq2\) for every \(i,j\) lifts to an admissible set.

The asymptotic weight of coordinate \(k\) is \(1/[k(k+1)]\).  This leads to
\[
M_K=\max\sum_{k\leq K}\frac{|D_k|}{k(k+1)}
\]
over pairwise compatible profiles and to the exact constant
\[
c=B_1+C_*,
\qquad
C_*=\lim_{K\to\infty}
\left(M_K-\sum_{k\leq K}\frac{\pi(k)}{k(k+1)}\right).
\]
The existence of the limit and the matching global upper bound are proved
in PROOF.md.

## Explicit profitable profile

Put
\[
\begin{aligned}
C_0&=\{1\}\cup\mathbb P,\\
C_1&=\{1,3,4,5,6\}\cup\{p\ge7:p\text{ prime}\},\\
C_2&=\{1,2,5,7,8,9,11,12,13,15\}
      \cup\{p\ge17:p\text{ prime}\}.
\end{aligned}
\]
All six ordered cross-products \(C_i\times C_j\), including \(i=j\),
have multiplicity at most two.  A prime at least \(17\) is forced
identically across any equality, reducing the check to the finite cores.
Apart from ordinary swapped pairs, the duplicate products are:

\[
\begin{array}{c|l}
(C_0,C_1)&1\cdot6=2\cdot3,\quad2\cdot6=3\cdot4,\\
(C_0,C_2)&1\cdot15=3\cdot5,\quad2\cdot12=3\cdot8,\quad
3\cdot15=5\cdot9,\\
(C_1,C_2)&3\cdot2=6\cdot1,\quad1\cdot8=4\cdot2,\quad
1\cdot12=6\cdot2,\\
&1\cdot15=3\cdot5,\quad3\cdot12=4\cdot9,\quad
3\cdot15=5\cdot9,\\
&4\cdot12=6\cdot8,\quad4\cdot15=5\cdot12.
\end{array}
\]

Use \(C_0\cap[k]\) through \(k=5\), \(C_1\cap[k]\) for \(6\leq k\leq11\),
and \(C_2\cap[k]\) thereafter.  Its gain over \(C_0\) is
\[
\left(\frac16-\frac1{12}\right)
+2\left(\frac1{12}-\frac1{15}\right)+\frac3{15}
=\frac{19}{60}.
\]
Since \(C_0\) itself contributes one beyond the prime-only profile,
\[
C_*\geq\frac{79}{60}.
\]

The finite core, exact weight, and direct lifted representation bound are
checked by computational/profile_search.py.

## Failed simplification

The profiles cannot in general be truncations of one common strong
multiplicative-Sidon set.  Exact finite optimization through \(K=10\)
already gives a larger score for nonnested profiles.  The upper proof must
therefore retain a compatible sequence, not collapse it to a single set.
