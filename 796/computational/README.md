# Computational checks for Erdős #796

All programs use only the Python standard library and deterministic tie
breaking.

## Exact values

Command run on 2026-07-16:

    python3 796/computational/exact_g3.py \
      --min-n 1 --max-n 30 --bruteforce-through 14

Runtime reported by the program: 1.698147 seconds.

The exact values obtained were

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\
\hline
g_3(n)&1&2&3&4&5&6&7&8&9&10&11&11&12&13&14
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
n&16&17&18&19&20&21&22&23&24&25&26&27&28&29&30\\
\hline
g_3(n)&15&16&16&17&17&18&19&20&21&22&23&24&24&25&25.
\end{array}
\]

The branch solver represents every forbidden configuration by its six-bit
vertex mask and branches on a contained hyperedge.  Every independent set
must omit a vertex of that edge, so the branches exhaust all possibilities.
It asserts that every equal-product triple uses six distinct vertices and
directly checks the returned set.  A separate all-subsets implementation
reproduced every answer through \(n=14\).

The computation is an exact certificate for the displayed finite range; it
is not used to prove the asymptotic.

## Compatible coefficient profiles

Command run on 2026-07-16:

    python3 796/computational/profile_search.py \
      --max-k 8 --mode both --bruteforce-k 5

Runtime reported by the program: 2.581849 seconds.

Results:

- all 188 repeatable profiles in \([8]\) were enumerated;
- both the canonical-tail-anchored and truncated optima equal \(176/105\);
- the gain over the canonical \(\{1\}\cup\mathbb P\) profile through
  \(K=8\) is \(1/18\);
- direct lifted-product enumeration had maximum multiplicity \(2\);
- independent Cartesian-product enumeration reproduced the optima through
  \(K=5\);
- the finite cores of the explicit \(C_0,C_1,C_2\) infinite profile in
  PROOF.md have cross multiplicity at most \(2\), and its extra weight is
  exactly \(19/60\).

The optimizer uses exact rational weights, an independently implemented
compatibility checker, and a direct lift check.  Its finite optima support
the variational formula; the proof that the limiting constant exists is
analytic and does not rely on the search.
