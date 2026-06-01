# Formalization Notes

No Lean project is initialized in this repository.  The external
`formal-conjectures` project contains a Lean statement for Erdos Problem 82.

Definitions to formalize locally if a Lean workspace is added:

- `RegularOn G S`: all vertices in `S` have equal degree in `G.induce S`.
- `reg G`: maximum cardinality of a finite vertex set `S` such that
  `RegularOn G S`.
- `F n`: minimum of `reg G` over simple graphs on `Fin n`.
- `QModularOn q G S`: all induced degrees in `G.induce S` are congruent modulo
  `q`.

Finite lemmas suitable for formalization:

- Complement preservation: `RegularOn G S -> RegularOn Gᶜ S`.
- Cycle and anticycle lemma: induced cycles and their complements are regular.
- Modular terminal criterion: if `|S| <= q` and `QModularOn q G S`, then
  `RegularOn G S`.
- `q+2` modular extraction: if `|S| <= q+2` and `QModularOn q G S`, then
  either `G.induce S` is regular or, in the only nonregular cases, deleting
  one exceptional vertex leaves a clique or an independent set on `q+1`
  vertices.  A formal proof can split on the common degree residue `r`; only
  residues `0` and `1` allow two degree values in `[0,q+1]`.
- Deletion-face criterion: for `|S| >= 2`, `RegularOn G S` iff the edge counts
  of all one-vertex deletions `S \ {v}` are equal.
- Induced matching exclusion: an induced matching of size `r` gives a
  `1`-regular induced subgraph on `2r` vertices; its complement gives a
  `(2r-2)`-regular induced subgraph.
- Dyadic bit polynomial: for `q = 2^s`, Lucas's theorem gives
  `Nat.choose h q % 2` equal to the `s`th binary digit of `h`; this underlies
  the modular-lift polynomial formulation.
- Binary parity-split equation: in an even graph, same-color degree parity for
  a two-coloring `x` is `A*x` over `F_2`; parity constant on both sides iff
  `A*x = a*1 + b*x`.
- Low-rank row-class certificates: if the adjacency matrix has rank `r` over
  a field, then there are at most `2^r` distinct `0`-`1` rows, and one row
  class is an independent set; if `A+I` has rank `r`, one shifted-row class is
  a clique.  The hereditary version applies to every induced subgraph of a
  counterexample.
- Hierarchical-lift obstruction example: the recorded `n=14` mask has a
  `4`-part first lift but no lift obtained by first taking a binary
  parity-pattern split and then splitting each side into two `4`-modular
  parts.
- Clique obstruction to zero-residue lifting: `K_q` is `q`-modular, but any
  induced part with all degrees `0 mod 2q` is a singleton.
- Pairwise merge criterion: two modular induced parts merge iff the
  cross-degree residues on both sides are constant and have the same shifted
  residue.
- Odd-cycle merge obstruction: for `n >= 5` odd and not divisible by `3`, the
  whole cycle `C_n` is `4`-modular but cannot be obtained by repeated pairwise
  merges of proper `4`-modular induced parts.
