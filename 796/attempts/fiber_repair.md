# Route: repair nonrepeatable large-prime fibers

Distinct large-prime fibers are cross-compatible, but an individual fiber
need not be strong multiplicative Sidon.  Discarding every nonstrong fiber
is too expensive: large nonstrong fibers can be pairwise compatible.

The successful repair acts on witnesses.  A witness in \(B\) is a pair of
distinct unordered multiset factorizations of one product, diagonals allowed.
The same witness cannot occur in two cross-compatible fibers, because it
would create three or four ordered cross solutions.  Deleting one supported
element for every witness makes every fiber self-compatible.

The ambient number of witnesses in \([N]\) is at most
\[
\#\{(a,b,c,d)\in[N]^4:ab=cd\}\ll N^2\log N.
\]
Indeed, with \(a=gr,c=gs,(r,s)=1\), one has \(b=sh,d=rh\) and
\(g,h\leq N/\max(r,s)\).

Apply this in dyadic capacity blocks \(K\leq\lfloor n/p\rfloor<2K\).
For \(K\leq\sqrt n/\log^2n\), the geometric sum of repair costs is
\(O(n/\log^3n)\).  Above this cutoff, the standard weak
multiplication-table theorem gives each inherited admissible fiber size
\[
O(K/(\log K)^a)
\]
for some \(a>0\), so deleting all remaining blocks costs
\(o(n/\log n)\).

After repair, choose the largest fiber in every capacity stratum and repeat
it.  Pairwise compatibility and self-compatibility make this replacement
valid, yielding precisely the weighted profile problem in PROOF.md.

The exact obstruction that killed the earlier route was expecting a
power-saving size bound for each pair of cross-compatible fibers.  Disjoint
prime-support semiprime grids give two simultaneously large counterexamples.
Charging edit distance to disjoint witnesses is the required repair.
