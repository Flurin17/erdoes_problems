# Notes for Erdős Problem #881

## Definitions

Throughout, \(\mathbb N\) is interpreted as the positive integers unless
explicitly stated otherwise. The asymptotic convention is the one used by
the formalized statement linked from the problem page.

For \(A\subseteq\mathbb N\) and \(h\ge 1\), write
\[
hA=\{a_1+\cdots+a_h:\ a_i\in A\}
\]
with repetitions allowed.

An **asymptotic additive basis of order \(h\)** is a set
\(A\subseteq\mathbb N\) for which there is \(N_0\) such that every
\(n\ge N_0\) lies in \(hA\). Equivalently, \([N_0,\infty)\subseteq hA\).

The problem's **minimal under infinite deletions** hypothesis is:
\[
\forall B\subseteq A,\quad B\text{ infinite}\implies
A\setminus B\text{ is not an asymptotic basis of order }k.
\]
This is weaker than ordinary minimality under one-point deletions only in
wording: ordinary minimality implies it by monotonicity, but the hypothesis
does not require every one-point deletion to destroy order \(k\).

The desired conclusion is the existence of an infinite \(B\subseteq A\)
such that \(A\setminus B\) is an asymptotic additive basis of order \(k+1\):
\[
\exists N_1\ \forall n\ge N_1\quad
n\in (k+1)(A\setminus B).
\]

### Minimality is not extra leverage

If \(C\) is an asymptotic basis of order \(h\), then \(C\) is also an
asymptotic basis of order \(h+1\): fix \(c_0=\min C\), and write
\[
n=c_0+(n-c_0)
\]
once \(n-c_0\in hC\). Thus order is monotone upward.

Therefore any order-\(k\) basis \(A\) with no infinite deletion remaining an
order-\((k+1)\) basis is automatically minimal under infinite deletions at
order \(k\). Problem 881 is equivalent to the broader deletion theorem:
every asymptotic order-\(k\) basis should have some infinite deletion that
remains an order-\((k+1)\) basis. Equivalently, every order-\(k\) basis
should contain a co-infinite order-\((k+1)\) subbasis. A negative
construction need not separately verify the stated minimality; it follows
from blocking order \(k+1\).

There is one immediate positive split. If \(A\) contains a co-infinite
order-\(k\) subbasis \(P\), then choose any infinite
\[
B\subset A\setminus P.
\]
The complement \(A\setminus B\) contains \(P\), hence remains an order-\(k\)
basis and therefore is an order-\((k+1)\) basis by monotonicity. Thus the
only hard case of the broader theorem is exactly the original
infinite-deletion-minimal case: every co-infinite order-\(k\) subbasis has
already been ruled out.

The equivalent threshold form is: there should be an increasing sequence
\[
b_1<b_2<\cdots
\]
in \(A\) such that every prefix \(F_j=\{b_1,\ldots,b_j\}\) leaves
\(A\setminus F_j\) an order-\((k+1)\) basis with threshold \(<b_j\). Any
good infinite deletion gives such a sequence after discarding finitely many
small deleted elements, and such a sequence gives the deletion by the usual
interval argument \(b_j\le n<b_{j+1}\).

A fixed infinite deletion has an even cleaner exact test. Lemma 3.1d says
that \(A\setminus X\) is an order-\((k+1)\) basis if and only if all finite
deletions \(F\subset X\) share one common eventual threshold. The prefix
criterion above is a practical way to force such a uniform threshold by
making the next deleted element outrun the threshold of the current finite
prefix.

The late finite-deletion reservoir criterion in `PROOF.md` is exact. A good
infinite deletion with threshold \(T\) yields a reservoir
\[
R=B\cap(T,\infty)
\]
such that every finite \(F\subset R\) has arbitrarily late successors
\(b\) for which \(A\setminus(F\cup\{b\})\) is a basis of the desired order
with threshold \(<b\). Conversely, such a reservoir gives a good infinite
deletion by the prefix interval argument. Therefore the remaining positive
problem can be phrased as ruling out barriers of late-bad successors in
every infinite tail.

So a counterexample to the equivalent broader theorem must make finite
late-bad sets unavoidable in every infinite subset of \(A\). By the
terminal-gap lemmas below, genuine late-bad holes must delete all retained
\(A\)-points in a long terminal window below the witness. The plausible
negative shape is therefore an unbounded finite-barrier construction, not
ordinary essential elements or a few sparse gaps.

Lemma 10.3b packages this as a normal form: in any counterexample, for every
finite protected core \(E\), every infinite tail \(X\subset A\setminus E\),
and every bound \(L\), there is an inclusion-minimal finite
\[
F\subset X
\]
and \(w>L\) with \(w\notin(k+1)(A\setminus F)\). Every \(f\in F\) is active
with positive multiplicity in a repair after the other elements of \(F\) are
restored, and
\(A\setminus F\) has the terminal gap forced by Lemma 10.3. This is the
current precise target for a negative construction.

Warning 10.3c explains why a purely compactness, Zorn, or random-deletion
proof is unlikely to work without arithmetic input. An abstract Schreier
barrier representation model has arbitrarily long good finite deletion
prefixes and finite deletions are eventually harmless, but every infinite
deletion contains infinitely many finite barriers and therefore fails. The
missing step is to prove that such a representation model cannot be
arithmetized inside a genuine asymptotic basis, or to realize it by a staged
construction.

Finite-core finite-deletion stability is a useful but insufficient target:
there might be a finite \(E\subset A\) such that every finite
\[
F\subset A\setminus E
\]
leaves an order-\((k+1)\) basis. No current example refutes this statement,
but it would not by itself solve the problem, because Lemma 3.1d requires
one common threshold for all finite \(F\subset X\) inside the eventual
infinite deletion. The examples \(\{1\}\cup2\mathbb N\) and Warning 3.0
show how finite deletions can be harmless while their thresholds drift.
Lemma 3.1e records the resulting normal form: if finite-core stability
holds but no infinite deletion works, then every infinite tail contains a
finite delayed barrier \(F\) such that \(A\setminus F\) is eventually an
order-\((k+1)\) basis, but every threshold is at least \(\max F\); the same
terminal-gap and activity conclusions still hold for the delayed witness.
Corollary 3.1e' sharpens this to an inclusion-minimal delayed-barrier
normal form: \(F\) may be chosen late-bad while every proper subset is not,
and also inclusion-minimal for one witness \(w\ge\max F-1\). For \(k=2\),
after enlarging the protected core by finitely many singleton exceptions,
all remaining delayed barriers have size at least two.
The diagnostic `delayed_collective_barrier_search.py` finds small finite
models of this checklist, including the pair delayed barrier
\[
S=\{1,2,3,5,6,7\},\quad F=\{5,7\},
\]
whose proper singleton deletions have finite three-sum tail from \(3\), but
whose full deletion has minimal holes at \(16,17\) and tail only from \(18\).
Thus collective delay is a genuine local phenomenon, not an artefact of the
abstract barrier formulation.
However `certificate_free_stats.py` gives \(\alpha_{\rm cert}=2\) and
\(|S|/\alpha_{\rm cert}=3\) for this same window, so it cannot be scaled as
a fixed rank-2 large-excess obstruction without triggering Lemma 8.6g. A
true counterexample would need either unbounded ranks or much stronger
certificate-free arithmetic.
Corollary 10.3d records the complementary genuine-failure case: if no
finite core gives finite-deletion stability, then after every finite core
there are active finite barriers whose terminal windows are actual long
gaps of \(A\), not just gaps after deleting \(F\). Thus any refutation of
finite-core stability must live in the sparse regime and place its
finite-barrier witnesses immediately after genuine long \(A\)-gaps.
The diagnostic script `actual_gap_barrier_search.py` finds a small local
model:
\[
S=\{1,2,4,5,6\},\quad F=\{4,5\},\quad w=11,
\]
where \(2S\) covers through \(12\), \(w\notin3(S\setminus F)\) minimally,
and the terminal window \((6,9]\) is an actual \(S\)-gap.
Lemma 10.3e adds the corresponding coverage burden: any genuine \(A\)-gap
\((G,H]\) below the order-\((k+1)\) witness must still be covered by
\(k(A\cap[1,G])\). Hence finite-core failure requires long gaps that are
already filled by prefix sumsets, together with nearby finite barriers that
block the shifted repairs.
Lemma 10.3f sharpens this to a finite-prefix gadget: once the deleted set
lies before the terminal gap, every active repair and every shifted
representation dominated by the barrier uses only summands from the prefix
before the gap. Later elements are irrelevant to that local obstruction.
Proposition 10.3g shows this normal form is locally sharp: the interval
blocks
\[
I=[X+1,X+M],\qquad J=[X+2M,X+3M-1]\quad(M\ge X)
\]
with \(F\) the lower half of \(J\) have two-sum coverage through the
terminal gap, an inclusion-minimal three-sum hole, and an actual terminal
gap of length growing with \(M\). Thus the remaining problem is not local
existence of such barriers but cross-stage coding into an unbounded barrier.
The same interval block is not a cheap source of pair barriers. Lemma
10.3h classifies all coverage-compatible terminal-gap barriers in the
block. If the high coordinates are \(0,\ldots,M-1\) and
\(w_q=3X+5M+q\), then for \(-X\le q\le M-X\) the protected coordinate set
must be one of a lower prefix, an upper suffix, or for \(q\le0\) a forced
prefix-plus-suffix split:
\[
[0,\lfloor(M+q-1)/2\rfloor]\cup[M+q,M-1],
\]
\[
[\lceil q/2\rceil,M-1],
\]
or
\[
[0,\lfloor(M+q-1)/2\rfloor].
\]
Every such deletion has size at least \(\lceil M/2\rceil\). Thus the
interval gadget supplies only threshold-cut arithmetic, not arbitrary
finite-set coding. The diagnostic `interval_barrier_family.py` enumerates
these terminal-gap minimal holes and has a `--verify-classification` mode;
for \(5\le M\le12\), \(1\le X\le M\), it finds no coverage-compatible pair
deletions. Pair holes do appear after dropping coverage, but only far
beyond the two-sum coverage endpoint, so they do not satisfy Lemma 10.3e's
finite-core burden.
Disjoint copies of the interval gadget are insufficient: an infinite
deletion can take one protected point from each block and avoid containing
any whole block-level \(F\). A negative construction would still need a
Schreier-type or comparable unbounded barrier on the protected tail.
Warning 10.3i sharpens this: interval threshold cuts are local terminal-gap
objects, not deletion barriers by themselves. A genuine interval-gadget
counterexample would have to code arbitrary Schreier edges, or another
unbounded finite-set barrier, into arithmetic holes; a single block only
supports the rigid prefix/suffix cuts classified by Lemma 10.3h.

Proposition 3.1f proves both finite-core stability and the desired infinite
deletion under a tail-syndetic subset hypothesis. This blocks all
eventually periodic or finite-accelerator counterexample attempts whose
large background set has bounded gaps: finite fatal deletions would force
terminal retained gaps longer than the syndetic gap bound.
Consequently, any counterexample to the broad deletion theorem must have no
tail-syndetic subset. Equivalently, every infinite subset of \(A\) has
arbitrarily long tail gaps; in particular, \(A\) itself has arbitrarily
long gaps.
Lemma 8.2e adds a fixed-core delayed-singleton diagnostic for \(k=2\). If a
finite core \(D\) plus one moving deleted point \(b\) keeps producing
order-3 holes, then either the excess \(w-b\) is unbounded and gives
reflected centers directly, or the excess is bounded and a test set above
that bound prevents \(b\) from coloring the shifted rows. In both regimes,
one finite test set with no large certificate-free subset forces a recurrent
certificate triple and hence a good deletion. Thus fixed-core singleton
delay has the same certificate-free escape as fixed-rank barriers.
Lemma 8.6j-6 closes the simplest Sidon-copy escape: if a quotient order-2
basis \(S\) has bounded two-sum multiplicity, then there is an infinite
\(T\subset S\) with \(2(S\setminus T)+S\) cofinite. Therefore the
certificate-free two-color construction from Warning 8.6j'' would need
large shifted representation spikes, not merely Sidon sparsity.
Lemma 3.4b' is the general shifted version: bounded \(k\)-term
representation multiplicity in an order-\(k\) basis \(S\) gives an infinite
\(T\subset S\) with \(k(S\setminus T)+S\) cofinite. This is weaker than a
full good deletion for \(S\) itself but useful when the last summand lives
in a retained companion class.
Lemma 8.6j-7 gives the one-color version: for a certificate-free color
\(C\), either the graphs for \(C+C+A\) have unbounded matchings and one can
delete an infinite \(T\subset C\) while keeping \(2(C\setminus T)+A\)
cofinite, or bounded moving transversals force large mixed degrees
\(C+(A\setminus C)\) through a few moving vertices.
Warning 8.6j-8 records why cross-color reflected packets do not immediately
feed Corollary 2.3c: two reflected \(C\)-points create a certificate triple,
but the certificate value is the mirror \(m-e\), which is exactly the
natural element deleted by the fixed-certificate construction.
Warning 8.6j-9 adds the algebraic reason: if one deletes mirrors
\(m_i-t\), then any two-deleted repair using one mirror from each of two
centers requires a fixed value \(y_1+y_2-t\in A\). Thus a
certificate-free reflected packet cannot run the balanced repair recursion.
Lemma 8.2a' supplies the alternative bridge repair found from this failure:
with a fixed padder \(t\), moving anchors \(e_j\), and deleted elements
\(b_j\), the identities \(t+b_j=e_j+q_j\) and \(e_j+b_i\in2C\) for
\(i\le j\) imply \(A\setminus\{b_j\}\) is an order-3 basis. For cross
packets this asks for the extra bridge value \(q_j=t+m_j-2e_j\in C\).
The diagnostic `bridge_repair_search.py` finds this bridge in the finite
delayed pair window \(S=\{1,2,3,5,6,7\},F=\{5,7\}\), but not in the
rank-three delayed window or in the alternating pair-hole window, even when
all deletion orderings are tried. Other rank-three windows do have bridge
data, so the failure is geometric rather than a rank-only obstruction.
The same negative result holds for the current Schreier test windows: the
first seed pair \(\{1,4\}\), first seed triple \(\{2,3,4\}\), tail P5 pair
\(\{10,30\}\), and P6 pair-edge escape \(\{10,38\}\) have no moving-anchor
bridge data in their displayed finite row sets, even after reordering the
deletion. This rules out using Lemma 8.2a' as the local repair mechanism
for the surviving Schreier/P6 finite obstruction.
Corollary 3.4r explains the likely bottleneck: in a counterexample the
large reflected packets can be forced to have only bounded representation
counts in the translated rows \(s+d\), exactly the rows a bridge repair
would need to use coherently.

## Trivial and Boundary Cases

### \(k=1\)

If \(A\) is an asymptotic basis of order \(1\), then \(A\) is cofinite.
Every infinite deletion destroys order \(1\), so the minimality hypothesis
is automatic. The desired conclusion is true: choose any infinite
\(B\subset A\) with \(B(x)=o(x)\), for example a sufficiently sparse
subsequence of \(A\). Then \(A\setminus B\) is an order-2 basis. A complete
proof is written in `PROOF.md`.

### Residue-padding examples for every \(k\)

For \(k\ge2\), the set
\[
A_k=\{1\}\cup k\mathbb N
\]
is an order-\(k\) basis and is strongly minimal under infinite deletions at
order \(k\). If \(B\subset A_k\) is infinite, then \(B\) contains infinitely
many multiples \(b\) of \(k\). The number \(b+k-1\) has residue \(k-1\), so
any \(k\)-term representation uses exactly \(k-1\) copies of \(1\) and one
multiple of \(k\), forced to be \(b\). Thus deleting \(b\) removes this
witness.

The desired deletion exists: delete \(B_0=\{k2^i:i\ge1\}\). Since
\(\mathbb N\setminus\{2^i:i\ge1\}\) is an asymptotic basis of every order
\(L\ge2\), the remaining set \(\{1\}\cup k(\mathbb N\setminus\{2^i\})\) is
an order-\((k+1)\) basis. The proof is written as Example 11 in `PROOF.md`.
Proposition 11.1 generalizes this: for a finite accelerator \(F\) over a
cofinite lattice component \(dD\), a sparse deletion from \(dD\) works
whenever every residue has a \((k+1)\)-term residue representation using at
least two lattice terms. Thus a finite-accelerator counterexample over a
cofinite component would need a residue class whose \((k+1)\)-term residue
repairs all use at most one lattice term.
Corollary 11.1a removes even that caveat when \(F\cup dD\) is already an
order-\(k\) basis: the order-\(k\) residue representation uses at least one
lattice term for large targets, and the order-\((k+1)\) repair can use one
more. Hence finite accelerators over cofinite lattice components are always
positive.

### A genuine \(k=2\) model where the desired deletion exists

Fix \(a\equiv3\pmod5\), and let
\[
C=\{n\ge N_0:n\equiv0\text{ or }1\pmod5\},\qquad A=C\cup\{a\}.
\]
Then \(A\) is an asymptotic basis of order \(2\): the residues
\[
C+C:\{0,1,2\},\qquad a+C:\{3,4\}
\]
cover all classes modulo \(5\), and each required progression is eventually
covered because \(C\) is cofinite inside its two progressions.

It is strongly minimal under infinite deletions at order \(2\). If an
infinite \(B\subseteq A\) contains infinitely many \(b\in C\), then the
numbers \(a+b\) are unbounded and have no two-term representation from
A\setminus B\): residue classes force a representation of \(a+b\) to be
\(a+c\) with \(c\equiv b\pmod5\), and equality forces \(c=b\), while
\(C+C\) has only residues \(0,1,2\). If \(B\) contains \(a\), then deleting
the remaining infinite part of \(B\cap C\) only makes this worse; deleting
\(a\) itself also leaves only residues \(0,1,2\) at order \(2\).

Nevertheless the desired conclusion holds. Delete a sparse infinite
\(B\subset C\) with zero relative density in each of the two progressions
\(0,1\pmod5\), and put \(C'=C\setminus B\), \(A'=A\setminus B\). Then sums
of two elements of \(C'\) still cover all sufficiently large integers in
the residue classes \(0,1,2\pmod5\), by the same counting argument as the
\(k=1\) case inside arithmetic progressions. Hence
\[
3C':\{0,1,2,3\},\quad
a+2C':\{3,4,0\},\quad
2a+C':\{1,2\}
\]
cover all residue classes modulo \(5\) for all sufficiently large integers.
Thus \(A'\) is an order-3 basis.

### Eventually periodic bases

Proposition 7.1 in `PROOF.md` proves a more general fact: every eventually
periodic asymptotic basis of order \(k\) satisfies the desired conclusion,
without using the minimality hypothesis. The proof must account for finite
exceptional accelerators: if \(A\) is eventually the union of residue
classes \(S\pmod m\), it need not be true that
\(kS=\mathbb Z/m\mathbb Z\). Proposition 3.1f gives the cleaner reason:
the nonempty eventual periodic tail is syndetic, and terminal gaps from
finite order-\((k+1)\) holes cannot avoid a syndetic retained subset. The
same argument proves finite-core finite-deletion stability for eventually
periodic bases.

Corollary 7.1b extends this to any basis containing an eventually periodic
order-\(k\) subbasis \(P\). Delete the infinite sparse set inside \(P\)
given by Proposition 7.1; the remaining \(A\setminus B\) contains
\(P\setminus B\), so it is also order \(k+1\). Hence any counterexample to
the broad deletion theorem must avoid even a structured eventually periodic
subbasis of the original order, and eventually periodic examples cannot
refute the finite-core stability target.

However, Example 7.2 shows that arbitrary finite deletion is not stable at
order \(k+1\). A finite accelerator can lower the order of an eventually
periodic basis from \(m-1\) to about \(m/2\), so deleting that single
accelerator raises the order by an arbitrarily large amount. This is why
the late-deletion and matching criteria are formulated with threshold
control and carefully chosen deletions, not arbitrary finite deletions.

## Candidate Positive Lemmas

### Strong minimality as finite barriers

Lemma 2.1 in `PROOF.md` gives the most direct reformulation of the
hypothesis. The condition that every infinite \(B\subset A\) destroys
order \(k\) is equivalent to:

for every infinite \(B\subset A\) and every \(N\), there is some
\(n\ge N\) and finite \(F\subset B\) such that every \(k\)-term
representation of \(n\) from \(A\) uses an element of \(F\).

So the given minimality is an unavoidable finite-barrier property at order
\(k\). The problem asks whether one can choose an infinite \(B\) whose
order-\(k\) barriers can all be bypassed with one extra summand.

### One-hit absorption lemma

Let \(A\) be an order-\(k\) basis, \(B\subseteq A\), \(C=A\setminus B\).
Suppose there is \(t\in C\) such that:

1. every sufficiently large integer has a \(k\)-term representation from
   \(A\) using at most one element of \(B\);
2. for every \(b\in B\), \(b+t\in 2C\).

Then \(C\) is an order-\(k+1\) basis.

Proof idea: write \(n-t\) as a \(k\)-sum with at most one deleted element.
If none appears, add \(t\). If one deleted element \(b\) appears, replace
\(b+t\) by two elements of \(C\).

Gap: sparse choice of \(B\) does not by itself guarantee condition 1 for
thin or nearly unique bases, and condition 2 is an additive-repair condition
that can fail in Sidon-like constructions.

Lemma 2.2 gives the full repair version. If a fixed retained element
\(t\in C\) can absorb every multiset of \(r\le k\) deleted elements,
\[
t+b_1+\cdots+b_r\in(r+1)C,
\]
then \(C\) is automatically order \(k+1\). This is the general form of the
repair criterion later used for \(k=2\) in Lemma 8.2a.

Theorem 2.3 resolves the corresponding certificate problem under finite
reflection-recurrence. It constructs a protected reservoir and a finite
family of balanced certificates so that the repair condition in Lemma 2.2
holds for every deleted multiset of size at most \(k\). Thus if an
asymptotic order-\(k\) basis is finitely reflection-recurrent, it has the
desired infinite deletion for order \(k+1\).

Lemma 2.3b isolates the fixed-data form of that argument. It is enough to
find one recurrent certificate tuple
\[
e,y_1,\ldots,y_k\in A
\]
such that
\[
y_1+\cdots+y_d=(d-1)e+x_d,\qquad x_d\in A,\quad 1\le d\le k.
\]
For \(k=2\), this reduces to finding recurrent \(e,y_1,y_2\) with
\[
y_1+y_2-e\in A.
\]
Thus large recurrent clusters from Lemma 8.6c would finish the bounded-width
large-excess branch if one of them necessarily contained this certificate
pattern. The remaining obstruction can be phrased as certificate-free
recurrent clusters.
Corollary 2.3c writes the \(k=2\) case directly via Lemma 8.2a: choosing
deleted elements \(b_j=m_j-e\) from recurrent centers for
\(\{e,y_1,y_2\}\), the identities
\[
b_j+e\in2C,\qquad 2b_j+e\in3C,\qquad b_i+b_j+e\in3C
\]
come from the protected mirrors \(m_j-y_1,m_j-y_2\) and
\(x=y_1+y_2-e\).

Lemma 2.4 shows that the same conclusion follows from reflection-recurrence
on a tail \(A\cap(D,\infty)\). The certificate construction can initialize
the fixed padder and all \(Y\)-entries above \(D\), and later stages only
reflect that fixed finite tail set.

### Late finite-deletion reservoir lemma

Let \(h=k+1\). Suppose there is an infinite \(R\subseteq A\) such that for
every finite \(F\subset R\) and every \(L\), one can find
\(b\in R\setminus F\), \(b>L\), for which \(A\setminus(F\cup\{b\})\) is an
order-\(h\) basis with threshold \(<b\). Then there is an infinite
\(B\subset R\) such that \(A\setminus B\) is an order-\(h\) basis.

Proof idea: delete \(b_1<b_2<\cdots\) recursively, always choosing the next
deleted element beyond the current threshold. Future deletions are too large
to affect already protected integers.

Gap: no general proof yet that such an infinite reservoir must exist under
the hypotheses of the problem.

### Finite-deletion independence is insufficient

Warning 3.0 in `PROOF.md` records a failed diagonal: it is not enough to
find an infinite \(B_0\subseteq A\) such that every finite
\(F\subset B_0\) is deletable at order \(k+1\). After deleting a finite
prefix \(F_j\), its threshold \(N_j\) may lie beyond the last deleted
element \(b_j\), leaving a gap \([b_j,N_j)\) that future choices cannot
repair. This is why Lemma 3 requires the stronger condition \(N_j<b_j\) at
each deletion stage.

This suggests a possible no-answer mechanism not covered by permanent
private witnesses: every finite deletion could be harmless at order \(k+1\),
but only after a threshold far beyond the deleted elements. Then an infinite
deletion might create infinitely many delayed gaps. A counterexample of this
type would need blocks whose loss is eventually compensated by later blocks,
while infinitely many losses leave unbounded uncovered intervals.

This mechanism is not sufficient by itself. For \(k=2\), a delayed finite
gap after deleting a finite prefix \(F\) may disappear after later retained
elements are considered: if \(n-c\in2(A\setminus D)\) for some retained
\(c\), then \(n\in3(A\setminus D)\). A genuine counterexample needs delayed
gaps that are immune to all retained translates \(c+2(A\setminus D)\), not
merely gaps for finite prefixes.

Warning 3.0b gives a concrete check on this issue. The set
\(\{1\}\cup h\mathbb N\) is an order-\(h\) basis with no infinite deletion
remaining order \(h\), but no finite deletion gives a terminal minimal
order-\(h\) subbasis. Thus a finite-deletion tree argument without the
late-threshold condition is false. This example is not a counterexample to
Problem 881 for \(h=k+1\), because it is not an order-\(k\) basis.

Corollary 3.1b gives the exact finite-prefix language. A finite
\(F\subset A\) is late-bad if \(A\setminus F\) is not order \(k+1\), or its
order-\((k+1)\) threshold is at least \(\max F\). If some infinite
increasing sequence has no late-bad finite prefix, then deleting that
sequence preserves order \(k+1\). Hence any counterexample must make the
late-bad finite sets form a barrier: every infinite increasing sequence in
\(A\) has a late-bad initial segment.

This finite-prefix strategy is equivalent to the original question. If an
infinite deletion \(B\) leaves an order-\((k+1)\) basis with threshold
\(N\), then any tail of \(B\) above \(N\), enumerated increasingly, has no
late-bad prefix. Thus proving that some sparse sequence avoids late-bad
prefixes is not a separate easier theorem; it is exactly the desired
positive result in threshold language.

Corollary 3.1c strengthens this from initial segments to arbitrary infinite
subsets: in a counterexample, every infinite \(X\subset A\) contains some
finite late-bad \(F\subset X\). Thus a no-answer construction must build a
finite-set barrier of delayed or genuine order-\((k+1)\) failures.

The affine finite-booster construction linked from the 2026-05-03 page
comment is currently classified as an unverified attempt, not a solution.
Its local hyperplane-avoidance step does not prove the shifted domination
forced by existing order-\(k\) coverage: if \(p\) is an order-\((k+1)\) hole
after deleting \(c\), then every retained padder \(e\) with \(p-e\) in the
covered range requires all \(k\)-representations of \(p-e\) to use \(c\).
For \(k=2\), such singleton private witnesses for infinitely many elements
would contradict Theorem 8.2, which constructs a good infinite deletion from
the resulting reflection recurrence.

### Protected matching criterion

Lemma 3.2 in `PROOF.md` gives a broader sufficient condition. If there is a
finite protected core \(E\subset A\) such that every sufficiently large
\(n\) has arbitrarily many \((k+1)\)-representations whose summand sets are
pairwise disjoint outside \(E\), then one can delete an infinite sparse
subset of \(A\setminus E\) and preserve order \(k+1\). The recursive proof
chooses the next deleted element beyond the threshold for one more disjoint
representation; among \(r+1\) disjoint representations, only \(r\) can be
hit by the first \(r\) deleted elements.

Thus a counterexample must produce bounded moving transversals for
\((k+1)\)-representations of infinitely many large integers, even after
protecting any finite exceptional core.

Corollary 3.3 makes the contrapositive precise. If no infinite deletion
preserves order \(k+1\), then for every finite protected \(E\subset A\)
there are arbitrarily large \(n\) for which all \((k+1)\)-representations of
\(n\) are hit by a bounded set \(D_n\subset A\setminus E\). The bound may
depend on \(E\), but not on \(n\) along the bad sequence.

Corollary 3.3b combines this with the terminal-gap lemma: after protecting
any finite core, a counterexample has arbitrarily large genuine
order-\((k+1)\) holes caused by bounded-size deletions outside that core,
and each such hole forces a terminal retained gap below the witness. The
bound can grow with the protected core, which is exactly the loophole used
by Schreier-type barriers.

Proposition 3.4 gives a countable criterion for ruling this out. Let
\(\mathcal H_E(n)\) be the hypergraph of \((k+1)\)-representations of \(n\)
outside a finite protected core \(E\). If
\[
|\mathcal H_E(n)|/\Delta_E(n)\to\infty
\]
uniformly along large \(n\), where \(\Delta_E(n)\) is maximum vertex degree,
then greedy matching plus Lemma 3.2 gives the desired infinite deletion.
Thus any counterexample must have bounded-transversal structure, not merely
few representations.

Corollary 3.4b gives an important positive class: if the original
order-\(k\) representation function of \(A\) is uniformly bounded, then the
desired infinite deletion exists. The proof pads each \(k\)-term
representation of \(n-e\) by \(e\). This gives \(\gg |A\cap[1,n]|\)
order-\((k+1)\) representations of \(n\), while a fixed vertex \(x\) can
occur in only \(O(1)\) of them because removing \(x\) leaves a bounded
number of \(k\)-term representations of \(n-x\). Hence the edge/degree
ratio tends to infinity. For \(k=2\), this rules out Sidon-type or
unique-representation thin bases as counterexamples; any remaining sparse
counterexample must have unbounded two-sum multiplicity somewhere.

Corollary 3.4c strengthens the same argument. Let
\[
R_k(X)=\max_{m\le X} r_{k,A}(m).
\]
If \(R_k(X)=o(A(X))\), then the edge/degree ratio of the padded
order-\((k+1)\) representation hypergraphs still tends to infinity, so a
good deletion exists. Hence a counterexample needs representation spikes
with \(R_k(X)\) comparable to \(A(X)\) along an unbounded sequence. For
\(k=2\), the remaining sparse obstruction is not just near-critical
density; it must combine near-critical density with large two-sum
multiplicity spikes and the private-color barrier normal form.

Corollary 3.4d localizes the spike requirement. In a counterexample, after
any finite core \(E\) is protected, there are arbitrarily large
\((k+1)\)-targets \(n\) and unprotected summands \(x\in A\setminus E\)
such that
\[
r_{k,A}(n-x)\gg_E A(n).
\]
This follows because bounded matching number plus the padded lower bound
for \(|\mathcal H_E(n)|\) forces a high-degree vertex, and each edge
through that vertex gives a \(k\)-term representation of the shifted target.
For \(k=2\), the large spikes are large reflected clusters
\[
A\cap(n-x-A).
\]
Lemma 3.4f records the only direct recurrence consequence currently
available from such spikes: if the reflected clusters \(U_n=A\cap(n-A)\)
hit one finite certificate-dense test set \(T_0\) in more than
\(\alpha_A(T_0)\) points for arbitrarily many \(n\), then one certificate
triple in \(T_0\) recurs and Corollary 2.3c gives a good deletion. Without
stable overlap, spikes can escape to fresh blocks: finite models with
paired blocks \(P_j\) and \(n_j-P_j\) have huge reflected clusters at
\(n_j\) but eventually miss every fixed finite test set.

Corollary 3.4g gives the \(k=2\) bounded-transversal form of the same
phenomenon. In any counterexample, after protecting a finite core \(E\),
there are arbitrarily large holes \(w\notin3(A\setminus D)\) with
\(|D|\le q_E\), and one deleted element \(d\in D\) gates
\[
\gg_E A(w)
\]
retained two-sum repairs \(w-d=a+b\), \(a,b\in A\setminus D\). Thus the
remaining obstruction is not just a finite gate; it is a moving star gate
with linearly many retained repairs. If the same gate or a certificate-rich
part of those repairs could be made recurrent, the positive recurrence
theorems would apply.
Corollary 3.4h ties this back to the private-color obstruction: for a
star-gated hole, almost every retained summand \(a\) in a repair
\[
w-d=a+b
\]
satisfies \(a+d\notin2(A\setminus D)\). In fact the direct star equation
gives the stronger bound
\[
r_{2,A}(a+d)\le |D|
\]
for the full unordered two-sum representation count, with no \(N_0\)
threshold condition and no deleted-pair exceptions. Thus a moving-star
counterexample must carry a large reflected set of bounded-count translate
rows for the same moving gate.
Corollary 3.4i strengthens the star-gate normal form in the remaining
\(k=2\) case. After the finite singleton-exceptional set is protected, the
bounded deletion set can be shrunk to an inclusion-minimal collective hole
\[
w\notin3(A\setminus F),\qquad 2\le |F|\le q_E,
\]
while preserving a gate \(d\in F\) with \(\gg_E A(w)\) retained repairs.
Thus the moving star is not merely a maximal-matching artifact: it lives
inside a minimal collective barrier whose every deleted element is active
and individually order-3-good. Since \(w>d\) for every retained repair, the
singleton deletion \(A\setminus\{d\}\) represents \(w\); every such
singleton repair must use another element of \(F\setminus\{d\}\).
Corollary 3.4j packages the same conclusion without mentioning the hole:
for every finite protected core \(E\), a counterexample has arbitrarily
large \(w\) and a moving \(d\in A\setminus E\) such that a positive
proportion of the reflected slice
\[
A\cap(w-d-A)
\]
lands under translation by \(d\) in values \(s\) with
\(r_{2,A}(s)\le Q_E\). Proving a reflected low-count translate exclusion
for order-2 bases would close this branch.
Warning 3.4k shows that such an exclusion is false if it uses only
order-2 basishood. In the benign basis \(A=\{1\}\cup2\mathbb N\), taking
\(d=1\) and \(w=2M+1\) gives \(M-1\) even rows \(a\) with
\[
w-d-a\in A,\qquad r_{2,A}(a+d)=1,
\]
a proportion tending to \(1\) of \(A(w)\). The escape is that all these
rows are pinned by the single element \(1\).
Lemma 3.4l records the useful conditional form: if all large low-count
two-sums are forced to use one of finitely many pins \(P\), then after
protecting \(P\) no reflected low-count translate slice can have positive
density in \(A(w)\). Thus a remaining counterexample needs genuinely
unpinned bounded-count translate rows outside every finite protected core,
in addition to terminal gaps, active repairs, and occurrence inside every
infinite deletion tail.
Corollary 3.4m turns this into a positive theorem for \(k=2\): any order-2
basis with one finite pin set controlling all bounded-count large two-sums
satisfies the desired order-3 deletion conclusion. The leftover sparse
case must therefore have both large representation spikes and unpinned
bounded-count rows after every finite core is protected.
Corollary 3.4n makes this unpinned requirement explicit: outside every
finite protected core, a counterexample must have a fresh gate \(d\) and
\(\gg_E A(w)\) fresh reflected neighbours \(a\), all avoiding the core,
with \(w-d-a\in A\) and bounded full count \(r_{2,A}(a+d)\). This is a
low-count star in the graph of bounded-representation two-sums, coupled to
the reflected slice at \(w-d\).
Corollary 3.4o is the corresponding positive criterion: if some finite core
uniformly excludes such fresh low-count reflected stars, then the desired
order-3 deletion exists. Warning 3.4p shows why this criterion is global:
for any fixed finite core one can build a finite star gadget outside it,
then add a later cofinite tail to get a harmless order-2 basis without
destroying the low-count rows. A proof must use recurrence across every
infinite tail or the minimal collective-hole structure, not only local
order-2 coverage.
Corollary 3.4q gives a simpler sufficient condition: if after protecting
one finite core, every bounded-count translate graph has initial-segment
degree \(o(A(X))\) uniformly in the center \(d\), then a good deletion
exists. Therefore a counterexample must have low-count graph stars of
positive \(A(X)\)-density outside every finite core, even before imposing
the reflected partner \(w-d-a\in A\).
Corollary 3.4r adds the additive-combinatorial shape of such a star. The
fresh neighbours form a large reflected packet \(S\) with \(t-S\subset A\),
but the shifted equation
\[
x+y=s+d,\qquad x,y,s\in S,
\]
has only \(O(|S|)\) unordered solutions. So the remaining obstruction is a
large reflected packet that is sparse for a translated Schur equation.
Corollary 3.4s splits the rows of a star-gated minimal hole: each row
\(a+d\) is either uniquely represented by the gate pair \(\{a,d\}\), or
some other deleted element \(f\) gives a shifted overlap
\[
a+d-f\in A.
\]
With bounded \(|F|\), a positive proportion of the rows fall into one of
these two alternatives. This isolates the next branches: unpinned unique
rows versus moving shifted-overlap packets.
Corollary 3.4t packages this as an either-or normal form in every remaining
counterexample. Outside every finite core, arbitrarily far out, either
there is a large reflected packet \(S\) whose rows \(s+d\) are uniquely
represented by \(\{s,d\}\), or there is a large packet with both
\[
t-S\subset A,\qquad S+(d-f)\subset A
\]
for two fresh deleted elements \(d\ne f\). The latter branch produces many
three-point patterns \(s,s+d-f,t-s\) in \(A\).

Lemma 3.5 sharpens this obstruction. A bounded transversal \(D\) for
\((k+1)\)-representations of \(n\) is a finite order-\(k\) barrier for all
shifted targets \(n-c\), as \(c\) ranges through retained elements of \(A\).
This explains why the matching route cannot be forced from order-\(k\)
coverage alone: a local one-gate gadget realizes such a bounded
transversal. What remains hard is embedding those moving gates into a global
asymptotic basis with threshold control.

Lemma 3.5a strengthens this slightly: the same domination also applies to
protected shifts \(c\in E\), as long as \(n-c\) is too large to be represented
entirely inside the finite protected core. Thus one may put a finite test
pattern \(T\) into \(E\) and still conclude that every representation of
\(n-t\), \(t\in T\), uses the moving transversal \(D\). The unresolved
uniformity issue is that the allowed bound on \(D\) may grow with \(E=T\),
so this does not force a single reflection center by pigeonhole.

## Counterexample Target

A strong counterexample for \(k\ge 2\) would follow from a set \(A\) and
unbounded witnesses \(t_a\), for all but finitely many \(a\in A\), such that
\[
t_a\in kA,\qquad
t_a\notin (k+1)(A\setminus\{a\}).
\]
Then every infinite \(B\subseteq A\) removes infinitely many protected
elements \(a\), and the corresponding unbounded witnesses \(t_a\) are absent
from \((k+1)(A\setminus B)\).

This condition is stronger than ordinary minimality at order \(k\). Standard
minimal-basis constructions usually provide only
\[
t_a\in kA,\qquad t_a\notin k(A\setminus\{a\}),
\]
which is not enough because the extra summand may repair the deleted
element.

### Even stronger target: order \(k\), minimal at order \(k+1\)

An ordinary minimal basis of order \(k+1\) that is also a basis of order
\(k\) would immediately disprove the problem. Indeed, if every one-point
deletion \(A\setminus\{a\}\) is not an order-\((k+1)\) basis, then every
infinite deletion also fails at order \(k+1\), and hence fails at order
\(k\).

Finite cyclic residue analogues of this phenomenon exist. For example,
there are sets \(S\subset\mathbb Z/m\mathbb Z\) with \(2S=G\) but
\(3(S\setminus\{s\})\ne G\) for every \(s\in S\), in small moduli such as
\(m=5,8,9,13\). The hard part is lifting this to integers: deleting one
integer leaves many other integers in the same residue class, so residue
minimality does not produce element-level private witnesses.

Lemma 6.1 makes this obstruction precise for thick residue blocks
\[
T_L=\{s+mq:s\in S,\ 0\le q\le L\}.
\]
A modular hole \(\rho\notin3(S\setminus\{s_0\})\) has, by Lemma 6, a
three-term residue representation using \(s_0\). Central integer lifts
\(\rho+mQ\) then have \(\gg L^2\) lifted representations, while deleting a
single copy \(s_0+mq_0\) removes only \(O(L)\) of them. Single-integer
privacy can survive only near endpoint quotients, which is exactly the
fragile pattern in Example 13.2.

### Barrier target

A counterexample need not assign a private witness to each single deleted
element. It would be enough to find an infinite core \(P\subset A\) and a
family of finite nonempty sets \(F\subset P\) with witnesses \(w_F\) such that
\[
w_F\notin (k+1)(A\setminus F).
\]
The family must be an **unbounded barrier**: every infinite deletion
\(B\subset A\) must contain such finite sets \(F\subset B\) with
arbitrarily large \(w_F\). It is not enough that every infinite \(B\)
contain one protected finite set, because one finite missing value does not
destroy an asymptotic basis.

Lemma 10.1 shows what this requires: for every retained padder \(e\), the
finite set \(F\) must hit every \(k\)-term representation of \(w_F-e\).
For \(k=2\) and \(q=2\), this means all relevant two-sum graphs must have
the pair \(F\) as a vertex cover. This is a much stronger demand than
ordinary pairwise uniqueness.

More generally, one needs a hypergraph \(\mathcal F\) with finite nonempty
edges on an infinite core \(P\), together with a witness map
\(F\mapsto w_F\), such that
for every infinite \(X\subset P\) and every \(L\) there is
\[
F\in\mathcal F,\qquad F\subset X,\qquad w_F>L.
\]
Equivalently, for each \(L\), the subhypergraph of edges with \(w_F>L\)
has no infinite independent set.
Taking \(\mathcal F=[P]^q\) for a fixed \(q\) is a strong bounded-rank
version, but not necessary. Schreier-type barriers may have unbounded edge
size. This unbounded-barrier condition is the correct combinatorial form of
a finite-barrier counterexample.

## Finite Gadget Observations

Finite analogues search for sets \(T\subset[0,D]\) such that \(T+T\) covers
a long interval and each \(t\in T\) participates in some private two-sum
not produced without \(t\). Small examples exist:

* \(D=4\): \(T=\{0,1,3,4\}\), with \(T+T=[0,8]\).
* \(D=8\): \(T=\{0,1,2,4,5,7,8\}\), with \(T+T=[0,16]\).

These finite gadgets are encouraging for counterexample attempts, but they
do not yet solve the infinite problem. A block construction must also stop
three-term repairs involving earlier or later blocks.

### Product construction for finite gadgets

If \(T\subset[0,D]\) and \(S\subset[0,E]\) both have full two-sum intervals
and every element has a private two-sum, then
\[
U=T+(2D+1)S=\{t+(2D+1)s:t\in T,\ s\in S\}
\]
has the same properties. Indeed, the choice of base \(2D+1\) prevents
carries: a sum in \(U+U\) is uniquely decomposed into a low coordinate from
\([0,2D]\) and a high-coordinate sum from \(S+S\). Fullness and private
sums therefore tensor.

Starting from \(T_0=\{0,1,3,4\}\), this gives arbitrarily large finite
gadgets. The first diameters are \(4,40,364,3280,\ldots\), with sizes
\(4,16,64,256,\ldots\).

### Obstruction to using interval blocks as counterexamples

Suppose a shifted block \(M+T\) has
\[
(M+T)+(M+T)=[2M,2M+2D].
\]
Let \(e\) be a fixed earlier retained element. If a proposed private witness
has the form \(2M+u\) with \(u\ge e\), then
\[
2M+u = (2M+(u-e))+e.
\]
Since \(u-e\in[0,2D]\), the full-interval property gives
\(2M+(u-e)\in (M+T)+(M+T)\). Thus the witness is repaired by two current
block elements plus the earlier element \(e\), unless every such
representation uses the deleted element in the current block.

This is the central obstruction to converting full finite two-sum gadgets
into a \(k=2\) counterexample: only the first \(e-1\) coordinates of a large
block are automatically safe from the smallest earlier element, but a large
block has many elements to protect.

Finite searches show that one can avoid this obstruction locally by not
asking \(T+T\) to be a full interval. For example
\[
T=\{0,4,8,10,13,15,20\}
\]
has \(T+T\) containing the interval \([12,21]\), and each element of \(T\)
has a unique two-sum \(u\) using it with \(u-1\notin T+T\). This is a local
model for safety against a retained earlier element \(1\). It is still far
from an infinite counterexample, because an actual block construction must
avoid repairs by all earlier one- and two-sums and must place the covered
intervals consecutively.

### Safe markers: local privacy is easy, efficiency is hard

For any finite set \(E\) of earlier shifts and any \(L\), one can build a
finite \(T\) such that \(T+T\supset[0,2L]\) and every element has a private
two-sum \(u\) with \(u-E\) disjoint from \(T+T\). The construction starts
with the coverage core \(C=[0,L]\) and gives every \(c\in C\) a very large
marker \(p_c\); the private sums are \(c+p_c\) for \(c\), and \(2p_c\) for
the marker \(p_c\). Choosing markers recursively and very far apart avoids
all finitely many unwanted equalities.

This proves that the counterexample obstruction is not local privacy
against finitely many old elements. The hard part is **coverage efficiency**:
the marker gadget has diameter much larger than its covered interval, while
an infinite order-2 basis needs the covered intervals to bridge all gaps
before the next block can be placed above the current private witnesses.

## Failed Counterexample Route: finite accelerators

Tempting plan for \(k=2\): take a minimal order-3 basis \(C\), add one
finite "accelerator" \(f\), and arrange that \(A=C\cup\{f\}\) is order 2.
Then hope that deleting any infinite subset of \(C\) still destroys order 3
even with \(f\) present.

At the residue-class level this cannot protect private witnesses from the
accelerator. In an abelian group \(G\), write \(S\) for the residue set of
\(C\) and translate so that \(f=0\). If \(S\cup\{0\}\) is a 2-basis of
residues, then
\[
2(S\cup\{0\})=2S\cup S\cup\{0\}=G.
\]
But the right side is exactly the set of residues represented by a 3-term
sum from \(S\cup\{0\}\) that uses at least one copy of the accelerator
\(0\). Thus every residue already has an order-3 representation involving
the accelerator.

For general \(k\), the same translation gives
\[
k(S\cup\{0\})=G
\]
and every residue in this set is represented at order \(k+1\) with at least
one accelerator by appending another \(0\). Therefore finite accelerators
cannot give modularly protected order-\((k+1)\) private witnesses. Any such
counterexample would have to rely on size/uniqueness constraints, not merely
residue classes.

## Failed Counterexample Route: direct-sum digits

The formal direct-sum version of a Raikov-Stöhr construction also fails as a
counterexample. In the monoid \(M=X\oplus Y\), the set \(A=X\cup Y\) is
strongly minimal at order \(2\): deleting infinitely many elements from
\(X\), for instance, leaves unbounded unique mixed witnesses \(x+y\).

But it has the desired infinite deletion. Delete the positive even-weight
elements of \(X\). Every \(x\in X\) is either retained, or splits as
\[
x=e+(x-e)
\]
with both summands of odd weight. Hence every \(x+y\in M\) becomes a
three-sum from the remainder. Thus the clean carry-free model supports the
positive side rather than a counterexample.

A faithful additive embedding of this free commutative monoid into
\((\mathbb N,+)\) is impossible in rank at least two: if independent
generators \(u,v\) have images \(a,b\), then
\[
\phi(bu)=ba=ab=\phi(av),
\]
although \(bu\ne av\). Integer digit systems therefore must introduce
carries or coefficient identifications, exactly where the formal private
witness argument breaks.

## Staged Block Counterexample Requirements

A plausible counterexample for \(k=2\) would be built in stages. At a stage,
with all old elements below a cutoff, add a finite block \(S\) such that:

1. old elements together with \(S\) extend \(2A\)-coverage through a long
   interval beyond the previous cutoff;
2. every new element \(s\in S\) has an unbounded protected witness
   \(w_s\in2A\) with \(w_s\notin3(A\setminus\{s\})\);
3. all future blocks start above the current witnesses, so the witnesses
   remain protected.

The persistent difficulty is the ordering of coverage and witnesses. Marker
gadgets can protect every element against a fixed finite old set, but their
witnesses lie far beyond the interval that their two-sums cover. If future
blocks must start above those witnesses, the construction creates uncovered
gaps before the next block can contribute. Efficient-block searches have so
far found only degenerate local blocks under even small old-shift constraints.

Lemma 9 explains the obstruction: a witness \(w=a+p\) forces a gap
\[
A\cap(p,\ a+p-N_0]\subseteq\{a\}.
\]
Thus protecting many elements tends to create many long gaps exactly where
an order-2 basis needs enough density to cover the next interval.

For pair barriers \(F=\{x,y\}\), Lemma 10.1 specializes to a reflected-cover
condition. If \(A\) is an order-2 basis with threshold \(N_0\) and
\[
n\notin3(A\setminus F),
\]
then for every retained \(a\in A\setminus F\) with \(n-a\ge N_0\), every
two-sum representation of \(n-a\) uses \(x\) or \(y\). In particular,
\[
A\cap[1,n-N_0]\setminus F
\subseteq (n-x-A)\cup(n-y-A).
\]
Thus a pair-barrier counterexample needs infinitely many witnesses whose
large initial retained set is covered by two reflected copies of \(A\). This
is a strong rigidity demand, not just pairwise uniqueness.

### Failed marker-after-coverage scheme

A natural attempt is:

1. suppose \(2A_s\) covers \([0,N_s]\);
2. add a marker \(p_s=N_s+1\);
3. use witnesses \(p_s+a\) to protect old elements \(a\in A_s\);
4. start the next stage above all \(p_s+a\).

This would satisfy Lemma 9's domination gap if no new elements are placed in
\((p_s,p_s+\max A_s]\). The problem is coverage: adding \(p_s\) only gives
sums \(p_s+A_s\), not the whole interval \([p_s,p_s+N_s]\), unless \(A_s\)
itself contains \([0,N_s]\). If one adds dense intervals to repair this,
then those dense intervals create elements in the forbidden domination gaps
for many private witnesses.

This captures the recurring coverage/privacy conflict in the block route:
coverage wants interval-like additive structure, while order-3 privacy wants
large empty intervals after witness partners.

Proposition 13.1 in `PROOF.md` gives the precise finite-stage criterion.
It is enough to build increasing finite stages \(A_s\) covering successive
intervals \([N_{s-1}+1,N_s]\) by two-sums, while every new element
\(a\in A_s\setminus A_{s-1}\) has a witness
\[
w_{s,a}\le N_s,\qquad
w_{s,a}\notin3(A_s\setminus\{a\}).
\]
Future stages start above \(N_s\), so these witnesses remain permanently
private. Any infinite deletion hits infinitely many finite stages and hence
misses infinitely many such witnesses at order 3.

Proposition 13.1b records the correct weaker version. Singleton protection
can be replaced by a finite-edge stage-barrier system, with no uniform bound
on edge size, but it must be unbounded: every infinite deletion must contain
protected finite sets with arbitrarily large witnesses. This weaker version
proves failure at order 3; strong minimality at order 2 then has to be
proved separately unless the protected finite sets are singletons for all
but finitely many elements.

No suitable infinite sequence of stages is known. Example 13.2 shows that
isolated stages do exist: for even \(a\),
\[
A_{s-1}=\{1,3,\ldots,a-1\},\qquad P_s=\{a\}
\]
covers \([a,2a]\) at order \(2\), and \(2a\) is not a three-sum after
deleting \(a\) because the retained set is odd. The obstruction is
iteration: the witness is exactly the coverage endpoint, so the stage leaves
no buffer for the next stage's first required integer.

The script `stage_buffer_search.py` searches for stages that do leave such a
buffer, now filtering out the lowest padding artefacts by requiring
\(w-\min(A_{\rm old})\) to lie in the old two-sum coverage window. Its first
small hit is `old={1,2,3,9}`, add `6`, declare endpoint `10`, with two-sum
coverage continuing to `12`. This remains a finite-window artefact and has
not extended to a second stage in the same bounded search.

Thus current finite searches find only window artefacts. Lemmas 5.1 and 9
explain why dense interval or marker implementations fail.

Lemma 5.1 in `PROOF.md` formalizes the repair mechanism: deleting \(m\)
points from a dense interval \([r,r+L]\) still leaves the central two-sum
interval
\[
[2r+2m,\ 2r+2L-2m].
\]
Therefore markers placed near a dense coverage interval are repaired by
central old two-sums for all but endpoint elements. Markers placed far away
avoid this repair but fail to bridge the next coverage gap.

Attempt 13 now records the sharper interval version: if
\[
w=p+a,\qquad a\in I=[r,r+L],
\]
and some retained \(e\in I\setminus\{a\}\) makes
\[
p+a-e\in[2r+2,2r+2L-2],
\]
then \(w\in3(A_s\setminus\{a\})\). Thus a private marker witness must avoid
the whole central two-sum interval after subtracting every retained point of
the dense block, which is incompatible with using nearby marker sums for
coverage except at endpoints.

## Structural Obstruction for \(k=2\)

If \(A\) is an order-2 basis and \(a\in A\), put \(S=A\setminus\{a\}\).
If \(S\) is not an order-3 basis, then \(S\) must contain arbitrarily large
translates of every finite subset of itself:
\[
\forall T\subset S\text{ finite}\quad
\exists\text{ arbitrarily large }m\quad m-T\subset S.
\]
This is Lemma 8 in `PROOF.md`.

Interpretation: order-3 essentiality of a point in an order-2 basis is very
expensive. The remaining set cannot have even one finite pattern whose
backward translates eventually disappear. A positive proof for \(k=2\)
could try to show that infinitely many elements fail this translate-thick
condition, then diagonalize their deletion using Lemma 3.

If infinitely many elements \(a\) have \(A\setminus\{a\}\) not order 3, then
Corollary 8.1 gives the stronger global conclusion:
\[
\forall T\subset A\text{ finite}\quad
\exists\text{ arbitrarily large }m\quad m-T\subset A.
\]
Theorem 8.2 now proves that this recurrence is strong enough to construct a
good infinite deletion. The construction fixes a retained element \(e\),
chooses deleted elements \(b_j=m_j-e\), and protects enough reflected
mirrors to repair every possible occurrence of one or two deleted summands
in a two-term representation of \(n-e\). Consequently \(A\setminus B\) is
an order-3 basis.

Lemma 8.2a isolates the exact repair target. To prove that
\(C=A\setminus B\) is order 3, it is enough to find a retained \(e\in C\)
such that every deleted element satisfies \(b+e\in2C\) and every pair of
deleted elements satisfies \(b+b'+e\in3C\). The unresolved cases can be
viewed as attempts to construct such a repairable infinite deletion.
Equivalently, one may build a protected reservoir \(P\subset C\) containing
\(e\) that already contains all these repairs.

Therefore the \(k=2\) positive route now splits as follows:

1. infinitely many one-point order-3 failures, which is resolved by
   Corollary 8.3;
2. infinitely many one-point deletions that are order-3 bases but have no
   threshold below the deleted element, which is resolved by Lemma 8.3a;
3. the remaining collective case, where all but finitely many singleton
   deletions are order-3 bases with a threshold below the deleted element.

The remaining \(k=2\) obstruction is thus the **finitely-bad case**: all but
finitely many one-point deletions \(A\setminus\{a\}\) are order-3 bases
with a threshold \(<a\), but it is not yet known in this workspace how to
choose an infinite deletion whose finite-prefix thresholds remain
controlled.

Corollary 8.3b makes this barrier-theoretic: after discarding a finite
exceptional set, no singleton is late-bad. Hence every infinite subset of
the remaining elements must contain a late-bad finite subset of size at
least two. The remaining obstruction is genuinely collective from its first
possible finite prefix.

Lemma 8.4b records the useful normal form for this collective case. Given
a witness \(w\) and a finite deletion \(F\), shrink \(F\) inclusion-minimally
while preserving \(w\notin3(A\setminus F)\). For every surviving
\(f\in F\), one then has
\[
w=q_f f+c_{f,1}+\cdots+c_{f,3-q_f},
\qquad q_f\in\{1,2,3\},\quad c_{f,i}\in A\setminus F,
\]
so every deleted element is genuinely used when the other deleted elements
are restored. Also \(f\le w\), and the reflected-cover domination from
Lemma 8.4 still holds. After Corollary 8.3b this minimal hole has size at
least two, once witnesses are chosen above the fixed low threshold.
The multiplicity matters: \(q_f=1\) recovers the stronger old estimate
\(f\le w-2\min A\), while \(q_f\ge2\) forces the restored element to lie at
most about halfway up to the witness.

This normal form does not reduce the problem to pair barriers. The finite
toy model
\[
A_0=\{1,2,3,4,5\},\quad F=\{1,2,3\},\quad w=9
\]
has \(9\notin3(A_0\setminus F)\), but restoring any single element of
\(F\) repairs the hole. Thus a genuinely collective minimal hole may have
no bad pair subhole.

Lemma 8.4a strengthens the obstruction produced by a finite hole. If
\(w\notin3(A\setminus F)\), \(f_0=\min F\), and \(m_0=\min A\), then
\[
(A\setminus F)\cap(w-f_0-m_0,\ w-N_0]=\varnothing.
\]
So a bounded-size barrier sequence with \(\min F\to\infty\) must have
\(w-\min F\to\infty\). In particular, bounded-size late-bad barriers cannot
have both bounded internal diameter and bounded witness excess.

Terminal gaps do not by themselves give a sparse-prefix proof. In the
finite model
\[
A_0=\{1,f-1,f,g-1,g\},\qquad F=\{f,g\},\qquad w=f+g
\]
with \(4\le f<g\) and \(g>2f\), one has
\[
w\notin3(A_0\setminus F),
\]
but restoring either \(f\) or \(g\) repairs the hole:
\[
w=f+1+(g-1)=g+1+(f-1).
\]
The terminal interval from Lemma 8.4a contains only the later deleted point
\(g\). Thus a rapidly growing candidate deletion can still have pair holes
whose terminal gaps are just ordinary sparse gaps of \(A\). Any proof must
use the shifted two-sum cover/private-color structure, not terminal gaps
alone.

Example 3.0a shows why the threshold issue is real. In the benign basis
\[
A=\{1\}\cup2\mathbb N,
\]
which does have a good infinite deletion, the finite prefixes
\[
F_M=\{2,4,\ldots,2M\}
\]
are late-bad at order \(3\): \(A\setminus F_M\) is order-3, but its least
threshold is \(4M+4>\max F_M\). Thus strong minimality at order \(2\) and
good singleton deletions do not control arbitrary finite-prefix thresholds.
The positive deletion must be chosen sparsely.

The script `collective_barrier_search.py` gives finite-window evidence that
this obstruction is genuinely collective. It finds, for instance,
\[
A=\{1,2,3,6,7,8\}
\]
on the window \([8,18]\): every singleton deletion still covers the window
at order \(3\), but several pair deletions create holes. This is only a
finite-threshold artefact, yet it shows why controlling one-point deletions
alone cannot settle the finitely-bad case.

Warning 8.5 rules out a tempting simplification: even if the finite
barriers needed in Lemma 8.4 have bounded size, they need not reduce to one
fixed uniformity. A finite union of non-barrier families can be a barrier.
Thus a proof in the finitely-bad case must either use arithmetic structure
beyond abstract barrier combinatorics or handle mixed-size finite barriers
directly.

Warning 8.5 also records a Schreier-type example showing that a barrier
need not have bounded width on any infinite tail. So a proof cannot first
thin the problem to pair barriers or bounded-size barriers by combinatorics
alone; any such reduction must use the additive gap and reflected-cover
constraints.
Warning 8.5a.1 adds that the first Schreier barrier is not universal. A
second-order Schreier front, built as a Schreier number of consecutive
first-Schreier blocks, is still a barrier on every infinite tail but has no
two-element edges. Hence no tail contains the complete first-prefix pair
links from Lemma 13.1j. Closing the enumerated-Schreier route does not
automatically close arbitrary variable-rank fronts.
The side-agent front check adds an even simpler example:
\[
\mathcal B_2=\{\{x_1<\cdots<x_m\}\subset\{2,3,\ldots\}:m=x_2\}.
\]
Every infinite set contains its first \(x_2\) elements as an edge, but the
second point controls the rank, so fixing the first point does not give
complete first-prefix links. The right remaining combinatorial target is a
recursive section analysis of fronts, not a direct reduction to the first
Schreier barrier.
Lemma 8.5a.2 records the basic section fact: if \(\mathcal F\) is a front
and \(s\) is a proper node, then the section
\(\mathcal F_s=\{G:s\cup G\in\mathcal F\}\) is again a front on the tail.
The missing arithmetic step is to make the private-incidence and terminal
gap normal forms descend through these sections.
Lemma 8.5a.3 adds the first arithmetic section tool. If a fixed node
\(\Delta\) and the first \(j\) moving endpoints of a section always carry
witnesses within bounded excess of the \(j\)-th moving endpoint, then a
\((|\Delta|+j)^{-1}\)-fraction of every finite test set is reflected by one
center. A finite test set with no such large certificate-free subset then
gives a good deletion. Hence a surviving front section must have unbounded
excess past every bounded moving depth, or it must keep large fractional
certificate-free subsets at every such depth.
Corollary 8.5a.4 rules out the coherent list-color version of that escape:
if all finite tests can be split into certificate-free fibers indexed only
by the fixed node and the first \(j-1\) moving endpoints, compactness gives
finitely many recurrent Sidon colors, impossible by Lemma 8.6g''''.2.
Thus a surviving front must make the endpoint palette escape to unbounded
section depth, not merely use many tests with bounded-depth colors.

There is a positive Ramsey reduction once bounded width is supplied by
arithmetic. Lemma 8.5a says that if every infinite subset contains a
late-bad set of size between \(2\) and a fixed \(q\), then after passing to
an infinite tail and a fixed \(r\le q\), all sufficiently far \(r\)-subsets
are late-bad with arbitrarily large witnesses. Thus bounded-width
collective barriers may be studied one uniformity at a time.

Lemma 8.5b gives a new restriction on that uniform case. A complete
\(r\)-uniform barrier on a cofinite tail cannot have bounded top excess:
if every sufficiently late \(F\in[P]^r\) had a witness
\[
\max F\le w_F\le\max F+D,
\]
then Lemma 8.4a would force every interval
\([x,2x+m_0-D-1]\) to contain only \(O_{r,D,N_0}(1)\) points of \(P\).
Since \(P\) is cofinite in \(A\), this would imply \(A(X)=O(\log X)\),
contradicting the \(A(X)\gg\sqrt X\) lower bound for an order-2 basis.
Thus a fixed-rank complete-barrier counterexample must live in the
large-top-excess branch, or use growing edge sizes.

Lemma 8.6 adds a second distinction. If such bounded-width barriers can be
chosen with witness excess \(w-\max F\) arbitrarily large, then every finite
pattern in \(A\) has arbitrarily large reflected subpatterns of size at
least a \(1/q\) fraction. For \(q=1\), this is full reflection-recurrence
and Theorem 8.2 resolves the case. Therefore a remaining counterexample
must either use barriers of growing size, or keep bounded-width witness
excesses under control in a delayed-threshold fashion.

Lemma 8.6c sharpens the large-excess conclusion: a uniform \(1/q\)
fractional recurrence property implies that for every \(M\) there is an
\(M\)-element set \(S\subset A\) with arbitrarily large centers
\(m-S\subset A\). This cannot be compacted into an infinite fully recurrent
core from combinatorics alone: the hereditary family
\(\{S:|S|\le\min S\}\) has the same \(1/2\)-fractional property, but no
infinite set all of whose finite subsets belong to it. The remaining gap is
not just recurrence density but certificate compatibility. The deletion
construction needs recurrent entries that also satisfy the finite affine
repair identities, e.g. for \(k=2\), recurrent \(e,y_1,y_2\) with
\(y_1+y_2=e+x\in e+A\), and it later needs recurrence for mirrors generated
during the construction.
Warning 8.6c' shows that this gap is real even inside order-2 bases. Start
with the thick residue basis \(U=\{n:n\equiv0,1\pmod3\}\), then insert very
sparse finite clusters \(S_M\subset2+3\mathbb N\) and infinitely many
reflected copies \(m_{M,q}-S_M\). A sparse affine-avoidance induction can
make each \(S_M\) recurrent while ensuring no nontrivial
\(y_1+y_2-e\), \(e,y_i\in S_M\), belongs to the enlarged set. The basis
property comes from \(U\), so large recurrent clusters alone cannot force
Corollary 2.3c.

Example 8.6d shows that the bounded second-excess hypothesis in Lemma 8.6a
is not a local consequence of the other known constraints. In the benign
strongly minimal basis \(A=\{1\}\cup2\mathbb N\), the sets
\[
F_M=\{2M+2,2M+4,\ldots,4M\}
\]
are inclusion-minimal order-3 holes for \(w_M=4M+3\), every deleted element
is essential after the others are restored, and reflected-cover domination
holds. But \(w_M-f_2=2M-1\to\infty\). Therefore the proof must use the
global barrier requirement over every infinite \(X\), not just the local
minimal-hole normal form.

Warning 8.6e records a related failed sparse-gap route. Lemma 8.4a says a
finite hole forces a terminal \(A\)-gap covered by the deleted set, but
choosing \(B\) to avoid all such finite terminal gaps is an independent-set
problem in interval hypergraphs. Order-2 basishood alone does not rule out
long intervals of the relevant length whose \(A\)-content is a prescribed
single far-tail point. So any proof using retained gaps needs an additional
arithmetic thickness lemma, not just sparsity.

Warning 8.6f makes this sharper in the no-tail-syndetic case left by
Proposition 3.1f. If \(A\) has arbitrarily long gaps, then for any late
finite \(F\) with \(f_0=\min F\) and any \(L\), ordinary gaps alone produce
some \(w>L\) with
\[
(A\setminus F)\cap(w-f_0-m_0,\ w-N_0]=\varnothing.
\]
Thus the remaining obstruction is not the existence of terminal gaps; it is
the shifted two-sum vertex-cover condition attached to genuine
nonrepresentations.

Lemma 8.6g gives a conditional way to exploit that vertex-cover condition.
If fixed-rank large-excess barriers exist and some finite test set \(T_0\)
has no large certificate-free subset, then a pigeonhole over the barrier
vertices reflects a certificate triple \(e,y_1,y_2\) with
\(y_1+y_2-e\in A\). Corollary 2.3c then gives a good order-3 deletion.
Therefore a fixed-rank large-excess counterexample must satisfy a strong
opposite property: every finite \(T\subset A\) has a subset of size at
least \(|T|/r\) containing no such certificate triple. For pair barriers,
that means every finite test set has a certificate-free half-subset.

Lemma 8.6h supplies the finite test set whenever \(A\) contains a long
arithmetic progression. An \(L\)-term progression has certificate-free
subsets of size at most \(2\): for two selected indices \(i<j\), avoiding
the certificates \(2j-i\) and \(2i-j\) forces \(j\ge L/2\) and \(j<2i\);
three selected indices are impossible. Hence fixed-rank large-excess
barriers cannot persist in bases with progressions longer than \(2r\).
Warning 8.6i records that this is not a residue-level consequence of
\(2A=G\): in \(\mathbb Z/(2r+1)\mathbb Z\), the set
\(\{1,\ldots,r+1\}\) is a 2-basis but can be partitioned into \(r\)
certificate-free classes.
Warning 8.6j adds that each certificate-free class is Sidon, so a finite
certificate-free coloring only implies \(A(X)=O_r(\sqrt X)\). This rules
out dense bases but not thin order-2 bases, whose necessary lower bound is
also of order \(\sqrt X\). Finite integer windows such as
\(\{1,2,7,8,10,11\}\), with \(2A\) covering \([8,22]\), can already be
2-colored into certificate-free classes.

Lemma 8.6a closes a broader delayed-barrier branch. If every infinite tail
contains finite barriers \(F=\{f_1<\cdots<f_r\}\) whose witness lies within
a bounded distance of the second-smallest element \(f_2\), then all test
elements above that bound are forced to reflect through \(f_1\). This gives
tail reflection-recurrence, and Lemma 2.4 upgrades tail recurrence to the
usual protected-reservoir deletion. Corollary 8.6b is the pair case:
persistent pair barriers must have unbounded top excess \(w-y\), or give
way to barriers of size at least three.

Example 8.7 warns that even pair barriers cannot be collapsed to one-center
recurrence by pigeonhole alone. The residue set
\[
S=\{0,1,2,4\}\subset\mathbb Z/7\mathbb Z
\]
has \(2S=G\), all singleton deletions remain 3-bases, but deleting
\(\{0,1\}\) creates a 3-sum hole. The resulting reflected cover of \(S\)
uses two centers and no single reflected copy covers \(S\). This is not an
integer counterexample, but it identifies a real local obstruction that a
proof of the finitely-bad case must overcome.

Example 8.7b strengthens the finite warning. In
\(\mathbb Z/5\mathbb Z\), \(S=\{0,1,2,3\}\) has \(2S=G\), every singleton
deletion remains a 3-basis, and every pair deletion has a 3-sum hole. The
hole for \(\{0,1\}\) is covered by the two reflected centers \(0\) and
\(4\), neither of which covers all of \(S\). Thus even a complete finite
pair-barrier graph can remain genuinely two-centered.

Warning 8.7c gives a coherent infinite cover-level obstruction. In a model
inside \(\mathbb Z\times\mathbb Z/8\mathbb Z\), every pair from an infinite
tail supplies arbitrarily far two-center reflected covers of every finite
test set, but a fixed four-point test set is never reflected by one center.
So Ramsey coherence of the covers from Lemma 10.1 is still insufficient;
the proof must exploit actual two-sum representation hypergraphs or genuine
holes, not just set-cover data.

Example 8.7d shows that even one genuine integer pair hole plus actual
order-2 tail coverage is insufficient locally. With tail residue classes
\(R=\{0,1,4\}\pmod8\) and two exceptional elements \(x\equiv2\),
\(y\equiv6\), every large \(w\equiv7\pmod8\) is absent from
\(3(A\setminus\{x,y\})\), the top excess \(w-y\) is unbounded, and the
two reflected centers split the three tail residue classes. A finite
three-residue test set has no one-center reflection. Thus a positive proof
must use global barrier/minimality over all infinite deletions, not just
local pair-hole structure.

Example 8.7e adds that active minimal pair holes do not force certificate
triples. In \(\mathbb Z/13\mathbb Z\),
\[
A_0=\{0,1,3,7,8,9\}
\]
has \(2A_0=G\), the subset \(P=\{0,1,3\}\) is certificate-free
\((y_1+y_2-e\notin A_0)\), yet every pair in \(P\) is an
inclusion-minimal 3-fold hole after deletion. Thus Lemma 8.4b's activity
normal form is still locally compatible with the certificate-free
alternative in Lemma 8.6g.

Example 8.8 gives a second finite warning: even if every deleted singleton
or pair pattern is repairable by one of finitely many retained centers, the
repairs may be incoherent. Lemma 8.2a needs one fixed center compatible with
the representation of \(n-e\); covering different deleted patterns by
different centers does not imply an order-3 basis after deletion.

Proposition 13.1c gives a concrete counterexample target for this
obstruction: build finite stages where every old-new pair has a local
order-3-private witness below the new endpoint. Any infinite deletion then
contains cross-stage pairs with unbounded witnesses. The script
`cross_stage_pair_search.py` finds the initial chain
\[
\{1,2\}\to\{1,2,3\}\to\{1,2,3,5\}
\]
but the default bounded greedy search stalls at the next stage. This is
finite evidence only; the stage criterion remains open. Also, the script
imposes the extra local condition \(N_s\ge\max P_s\). Proposition 13.1c
does not formally require this, because elements above \(N_s\) are dormant
for witnesses below \(N_s\); however, if a witness lies below \(b\in P_s\),
then deleting \(b\) is irrelevant to that witness, so the pair condition
collapses to singleton privacy for the old element. Thus the script is
testing the genuinely pair-dependent version of the criterion.

The older singleton stage criterion, Proposition 13.1, is now only a
diagnostic. Corollary 8.3 rules it out for \(k=2\): infinitely many robust
one-point order-3 witnesses would force reflection-recurrence and hence a
good deletion. For pair-stage systems, Corollary 8.6b says bounded top-excess
witnesses \(w-b\) are also impossible in a genuine counterexample; any
surviving pair construction must place its witnesses far above the larger
deleted element.

Proposition 13.1b-Schreier records the remaining unbounded-rank target. One
would build a cofinite tail \(P=\{p_i\}\) and protect the Schreier barrier
\[
\{F\subset P:|F|=\operatorname{index}(\min F)+1\}.
\]
Every newly completed Schreier edge must get a frozen witness below a lock
ceiling \(R_s\), while the stage still covers a later interval up to
\(C_s\) with \(R_s+\min A\le C_s\), and these witnesses must be unbounded
inside every infinite tail. The local holes should also be inclusion-minimal
and satisfy the shifted two-sum domination from Lemma 10.1. This criterion
is not ruled out by the fixed-rank lemmas, because edge sizes go to
infinity on tails; the open burden is finite-gadget existence with coverage,
frozen witnesses, unboundedness, and domination all at once.
The numerical order on \(P\) is only one version of this target. Variant
13.1b-enum in `PROOF.md` allows an arbitrary enumeration of a cofinite
protected set, as long as witnesses are unbounded in every infinite set of
enumeration indices. This keeps open a delayed-promotion route for repair
fillers: a filler with small numerical value need not become an early
Schreier vertex immediately. When it is eventually promoted, Corollary
13.1h.1 still forces shifted two-sum gaps against all old retained
endpoints.

The Schreier diagnostics now have several exact finite tests. Lemma 13.1f
gives the terminal forbidden windows. Lemma 13.1g says an inclusion-minimal
hole must also lie in
\[
\bigcap_{f\in F}\bigl((f+2C)\cup(2f+C)\cup\{3f\}\bigr),
\]
where \(C=S\setminus F\). Lemma 13.1h records the retained-endpoint poison
interval: if \(p\in C\) and \([q-p,R-p]\subset2C\), then every candidate
for the pair edge \(\{a,q\}\) in \([q,R]\) already lies in \(3C\). For
promoted fillers, Corollary 13.1h.1 gives the pointwise version: any
witness for \(\{a,q\}\) must avoid \(p+2C\) for every retained old endpoint
\(p\). For low-excess pair holes, Lemma 13.1i makes the private-color closure explicit:
each active row is colored by one endpoint, and the lower endpoint can force
new mirrors above the moving endpoint. These tests explain the P6 search
stall without proving a global obstruction; a surviving construction would
have to route the forced mirrors around the poisoned intervals while keeping
the two-sum coverage buffer.
The latest P6 diagnostic sharpens the first protected-filler failure. In
the pair-edge escape \((p,w)=(38,58)\), the fillers are
\(\{40,43,44\}\). Once they are treated as protected, each
\(q\in\{40,43,44\}\) has
\[
[q,63]\subseteq3(A\setminus\{10,q\}).
\]
Thus the whole current candidate range for the pair edge \(\{10,q\}\) is
poisoned. The retained endpoint \(38\) accounts for many, but not all, of
these candidates; the full old retained window fills the remaining shifted
two-sum gaps.
The `--p6-order-diagnostic` mode tests the first delayed-enumeration
loophole on this exact finite set: keep the fillers present but not among
the first six protected vertices, and try all orders of
\(\{10,15,18,19,30,38\}\). No order works; the best orders still have
three failed edges, all involving the newly added \(38\). Thus delaying the
fillers alone does not rescue the P6 escape. The prefix constraints are
already decisive: the good-pair graph forces \(10\) to be first, and after
that no second vertex has all rank-three Schreier edges against the
remaining tail.
The bounded `--p6-enum-search` mode broadens this slightly: for
\(p_6\le80\) and at most one delayed filler through \(120\), no arbitrary
enumeration order extends the P5 seed. Only \(p_6\le38\) survive the
coverage filter in that range.
Lemma 13.1j abstracts the ordering test: an enumerated Schreier stage
requires complete prefix links in the good-subset hypergraphs. In the P6
escape, the pair link forces \(10\) to be first, and the triple link then
has no possible second vertex.
With lazy prefix-link pruning, the same search checks \(14912\) candidates
for \(p_6\le55\) with up to two delayed fillers through \(95\), again
finding no arbitrary-order P6 extension.
A broader delayed-filler run with
`--max-p6 45 --max-extra 3 --max-extra-value 75` checks \(89702\)
coverage-passing candidates and again finds no arbitrary-order P6
extension; after \(p_6=38\), no later candidate passes the coverage filter
within those bounds.

Lemma 8.2c' closes one fixed-prefix loophole: if a fixed lower endpoint
\(d\) has genuinely pair-private witnesses
\[
w\notin3(A\setminus\{d,b\}),\qquad b\le w\le b+D,
\]
with the finite-test uniformity needed to avoid arbitrary retained test
sets, then \(w-d\) reflects the whole tail above \(\max\{D,d\}\). Indeed,
for a test point \(t>D\), the moving endpoint \(b\) cannot occur in a
two-sum representation of \(w-t\), so the fixed endpoint \(d\) must occur.
Lemma 2.4 then gives a good deletion. Corollary 13.1k translates this to
the enumerated Schreier route, and Corollary 13.1l removes the apparent
finite-test caveat: if a fixed prefix \(d\) has low-excess pair witnesses
for infinitely many later vertices, any finite test can be avoided by
taking a later witness. Hence, in a counterexample, for each fixed \(D\)
only finitely many later pair links may have \(w-p\le D\). Any viable
Schreier lift must make first-prefix pair excess diverge on every infinite
tail, or move into genuinely higher-rank prefix obstructions.
Lemma 8.2c'' and Corollary 13.1l.1 extend this beyond pairs. If a fixed
prefix vertex \(d\) is deleted together with a finite moving set \(H\), and
the witness stays within \(D\) of \(\min H\), then none of the moving
vertices can occur in the shifted rows \(w-t\) for \(t>D\); the fixed
vertex \(d\) reflects the whole tail. Hence every Schreier prefix level
\(u_i\) must have divergent witness excess above the first later endpoint
on every infinite later tail.
Lemma 8.2c''' records the intermediate version: if the witness is close to
the \(j\)-th moving endpoint, then only the fixed endpoint and the first
\(j-1\) moving endpoints can color shifted rows, giving \(1/j\)-fractional
recurrence. Unless a finite test set forces a certificate in every such
large fraction, this again falls into the certificate-free branch.
For the first pair level, Corollary 13.1l.2 combines this with the
endpoint-list lemma 8.6g': unless a good deletion already exists, every
finite test set in the later tail can be split by the shifted endpoint
lists into two certificate-free fibers. Compactness then gives a
two-coloring of the tail into certificate-free sets that are separately
reflection-recurrent in \(A\). This is now the canonical high-excess
first-prefix obstruction.
Corollary 13.1l.3 specializes this to the enumerated-Schreier target:
the later tail after the first protected vertex must be a union of two
recurrent Sidon-like colors. Since that tail is cofinite in \(A\), the
construction is forced to the critical density scale \(A(X)=O(\sqrt X)\)
and must have mixed two-sum spikes of size not \(o(A(X))\).
The finite `bipartite_sidon_window_search.py` diagnostic shows this shape
is still locally compatible: for example
\[
C=\{11,15,16\},\quad D=\{8,9,13\}
\]
are certificate-free colors, \(2(C\cup D)\) covers \([16,32]\), and
\(24=11+13=15+9=16+8\) is a mixed spike. The remaining contradiction, if
true, must use infinite recurrence, cofinite coverage, or threshold
control. The enhanced diagnostic also reports cross-residual matching
minima, and the top interval examples have minimum \((0,0)\); mixed spikes
alone are much weaker than the matching condition that would give a sparse
deletion from one color.
Sorting the same finite search by matching strength (`--sort matching`) on
`--max-value 20 --size 8` still gives per-color minima \((0,0)\), though
the best-color minimum is \(1\). Locally, coverage can alternate which
color supplies a cross-residual edge, avoiding the one-color matching
criterion.

The new `--pair-edge-search` diagnostic confirms that high-excess first
pair starts are locally possible but expensive. Starting from the P5 seed,
it finds \(p=37,w=69\) with fillers
\[
\{40,41,44,51,54,55,58\},
\]
and \(p=37,w=80\) with a larger filler set. Both give a local pair-private
hole for \(\{10,37\}\), but even delaying the fillers does not make the
six core vertices \(\{10,15,18,19,30,37\}\) support a Schreier order. The
same higher-rank edges fail:
\[
\{15,18,37\},\quad \{15,19,37\},\quad
\{15,30,37\},\quad \{18,19,30,37\}.
\]
The first three are fully poisoned in the covered interval after deleting
the edge; the rank-four edge has candidates but lacks inclusion-minimal
repair for some deleted vertex.
Treating the fillers as protected adds pair-link failures from \(10\) to
the fillers. Thus high excess shifts the obstruction upward rather than
removing it.

The latest private-color normal form is Proposition 8.4f in `PROOF.md`.
After the finite singleton-exceptional set is removed, every remaining
\(k=2\) counterexample must have, inside every infinite tail, an
inclusion-minimal collective hole \(w\notin3(A\setminus F)\) such that:

* \(A\setminus F\) has the terminal retained gap below \(w\);
* every deleted element of \(F\) is active in a repair after the other
  elements are restored;
* every finite test row \(t\) below the witness is either an exceptional
  deleted-pair row \(w-t\in F+F\), or has a private color
  \(f\in F\) with
  \[
  w-t-f\in A\setminus F,\qquad t+f\notin2(A\setminus F).
  \]

Lemma 8.4d further says that such a color can occur only when \(t+f\) has
fewer than \(|F|\) two-sum representations avoiding \(f\). For two-term
sums this is ordinary representation count, not a separate matching
notion. Warning 8.4e shows the limitation: in the eventually periodic
order-2 basis
\[
A=m\mathbb N\cup\{1,\ldots,m-1\},
\]
the low-count rows are cofinite in the infinite progression \(m\mathbb N\)
simultaneously for any prescribed finite set of small colors. Thus no
generic Sidon or energy bound on low-count rows follows from order-2
basishood alone. The obstruction must use either non-sparse redundancy,
certificate structure, or the recursive closure of private fillers.

There is also a more local witness obstruction. If \(w=a+p\in2A\) is meant
to remain outside \(3(A\setminus\{a\})\), then
\[
A\cap(p,\ a+p-N_0]\subseteq\{a\}.
\]
Indeed any \(e\) in that interval lets one write \(w-e\in2A\), and if the
two-sum avoids \(a\), then \(w\in3(A\setminus\{a\})\); if it uses \(a\),
then the complementary summand is negative because \(e>p\). This is Lemma 9.
It rules out dense interval-block/private-witness constructions for \(k=2\).

## General One-Point Failure Pattern

Lemma 10 generalizes the \(k=2\) translate-thickness obstruction. If
\(A\) is an order-\(k\) basis, \(C=A\setminus\{a\}\), and \(C\) is not an
order-\((k+1)\) basis, then every finite \(T\subset C\) has a large subset
\(U\) for which some reflected translate lands in a lower sumset:
\[
n-ra-U\subseteq (k-r)C
\]
for some \(1\le r\le k-1\). The subset \(U\) has size at least
\(\lceil |T|/(k-1)\rceil\).

Thus any counterexample in general order must force substantial finite
patterns of \(A\setminus\{a\}\) to recur inside lower sumsets after
reflection about arbitrarily large integers.

Corollary 10.2 is the global version: infinitely many bad one-point
deletions force this fractional lower-sumset recurrence for every finite
pattern in \(A\). For \(k=2\), the lower sumset is just \(A\) and the
fraction is all of \(T\), giving the reflection-recurrence used in Theorem
8.2. For \(k>2\), this is weaker than the finite reflection-recurrence
needed by Theorem 2.3.

Lemma 10.2b gives the matching delayed-threshold version. If infinitely
many one-point deletions are eventually order-\((k+1)\) bases but have no
threshold below the deleted element, then the shifted centers
\[
d_b=w_b-b
\]
are unbounded and every finite \(T\subset A\) has arbitrarily large
translates
\[
d_b-T\subseteq(k-1)A.
\]
For \(k=2\) this is genuine reflection-recurrence and closes by Theorem
8.2. For \(k>2\) it lands in a lower sumset, so delayed finite-core
stability still leaves the same budget mismatch as the bad-one-point
case.

For \(k=3\), the split is explicit: bad one-point deletions reflect a
half-sized subset either into \(A\) or into \(2A\). The first case can feed
Lemma 2.3b if the reflected half contains a fixed order-3 certificate tuple;
the second case has mirrors that cost two retained summands each, so the
existing balanced repair recursion overruns the order-4 budget. This is the
specific gap behind the stalled adjacent-order minimality route. The finite
booster window
\[
\{1,3,5,20,21,30,31\}
\]
shows the issue locally: for the one-point witness \(37\) after deleting
\(30\), the shifts \(37-30-\{1,3,5\}=\{6,4,2\}\) lie in \(2A\) but not in
\(A\).

For finite deletions, Lemma 10.1 gives the collective analogue. If
\(C=A\setminus F\) misses \(w\) at order \(k+1\), then for every retained
padder \(e\) with \(w-e\) above the order-\(k\) threshold, the finite set
\(F\) must hit every \(k\)-term representation of \(w-e\). In graph terms
for \(k=2\), \(F\) is a vertex cover for all relevant two-sum representation
graphs. This shows that collective-hole counterexamples still require a
strong domination mechanism, not just private witnesses for individual
deleted elements.

## Digital Minimal Bases

A Raikov-Stöhr-type digital construction was a natural candidate, but the
clean direct-sum model is now understood not to be a counterexample. In the
formal monoid \(M=X\oplus Y\), \(A=X\cup Y\) is strongly minimal at order
2, yet deleting the positive even-weight elements of \(X\) leaves an
order-3 basis because every deleted \(X\)-element splits into two retained
odd-weight elements.

Adding a finite residue layer does not by itself stop this repair. If
residue sets \(R_1,\ldots,R_k\) cover every target residue by one term from
each digit class, then after prescribing any residue \(r\in R_i\), the
remaining target \(\rho-r\) is again covered by one term from each class.
Thus \(\rho\) has a \((k+1)\)-term residue representation with an extra
class-\(i\) term. The residue layer therefore cannot force a repair to use
exactly one term from the deleted element's digit class.

The obstruction to turning the formal model into an integer counterexample
is structural: a faithful additive embedding of a free commutative monoid
of rank at least two into \((\mathbb N,+)\) is impossible. Integer digit
systems must introduce carries or coefficient identifications, and those
extra representations are exactly what the private-witness argument cannot
control.

The binary Raikov-Stöhr model also does not support the finite
certificate-free coloring escape from Lemma 8.6g. Writing
\[
X=\{\sum_{j\in F}4^j:\varnothing\ne F\subset\mathbb N\text{ finite}\},
\qquad Y=2X,\qquad A=X\cup Y,
\]
any finite coloring of \(X\) has, by Hindman's finite-unions theorem,
disjoint nonempty \(U,V\) with
\[
x_U,\ x_V,\ x_{U\cup V}
\]
monochromatic. Then
\[
e=x_U,\quad y_1=x_{U\cup V},\quad y_2=x_V
\]
gives
\[
y_1+y_2-e=2x_V\in Y\subset A,
\]
so this is a monochromatic certificate. Thus standard digital bases have
finite certificate tests; a certificate-free obstruction would have to be a
different thin bipartite/Sidon complementing construction.

Any such construction has an additional separation constraint. If
\(C\subset A\) is certificate-free, then
\[
(C+C)\cap(C+(A\setminus C))=\varnothing.
\]
Otherwise \(c_1+c_2=c+a\) with \(c,c_1,c_2\in C\) and
\(a\in A\setminus C\) would give the forbidden certificate
\[
a=c_1+c_2-c\in A.
\]
So a two-color certificate-free order-2 basis would need mixed sums
separated from both same-color sumsets, in addition to the Sidon-type
sparsity of each color. The two same-color sumsets need not be disjoint
from each other: \(\{1,6\}\cup\{2,5\}\) has certificate-free colors but
\(1+6=2+5\). Thus the usable separation is mixed-versus-same, not a full
three-way partition of \(2A\).

This also forces any certificate-free counterexample to have mixed-color
representation spikes. If
\[
A=C_1\cup\cdots\cup C_r
\]
is certificate-free colored and every mixed count
\[
|\{(c_i,c_j):c_i+c_j=n\}|
\]
is \(o(A(X))\) uniformly for \(n\le X\), then same-color sums contribute
only \(O_r(1)\) because the colors are Sidon, and Corollary 3.4c gives a
good deletion.
For two colors, a mixed spike at \(m\) is equivalently a reflected packet
\[
P_m=\{c\in C:m-c\in D\},
\]
and it carries the difference translate
\[
m+(P_m-P_m)\subset C+D.
\]
Thus any surviving spike is a large Sidon packet with its difference set
embedded in the mixed support.
The mixed support cannot be cofinite when one color is infinite, because it
is disjoint from that color's unbounded same-color sumset. Hence a
certificate-free order-2 basis must interleave same-color Sidon supports
with mixed reflected-difference spikes; it cannot rely on mixed sums alone
for all sufficiently large integers.

For large-excess pair barriers, the precise certificate obstruction is
list-valued. Given a pair hole \(\{x,y\}\) at \(w\), with endpoint centers
\(w-x\) and \(w-y\) arbitrarily large, and a finite test set \(T\), each
\[
t\in T
\]
has an endpoint list
\[
L_w(t)=\{z\in\{x,y\}:w-t-z\in A\}.
\]
If no admissible choice of endpoints splits \(T\) into two certificate-free
fibers, then one fiber contains a fixed certificate triple, reflected by
\(w-x\) or \(w-y\), and Corollary 2.3c gives a good deletion. Thus a
persistent pair-barrier obstruction needs coherent certificate-free
endpoint list-colorings, not just abstract certificate-free halfsets.
Moreover, if such list-colorable large-excess pair barriers exist for every
finite \(T\), a compactness argument produces a global coloring
\[
A=C_0\cup C_1
\]
such that both colors are certificate-free and each color is separately
reflection-recurrent in \(A\). Thus the remaining pair obstruction must
look like two recurrent Sidon-like layers, not just isolated finite
colorings. Since Corollary 8.6j-3 handles certificate-free colorings whose
mixed sums have sublinear multiplicity, these two recurrent layers would
also need mixed two-sum spikes comparable to \(A(X)\) along an unbounded
sequence of scales.
The same-color Sidon property also forces almost-cross-color recurrence:
if \(U\) lies in one color and \(m>2\max U\), at most one mirror \(m-u\)
can lie in that same color, otherwise \(u+(m-u)=v+(m-v)\) is a nontrivial
same-color collision. Hence each recurrent color must reflect finite
patterns almost entirely into the other color. The key new observation is
Lemma 8.6g'''': two different recurrence centers for the same three-point
test set then force a Sidon collision in the opposite color. Thus an
infinite integer basis cannot have a cofinite two-color certificate-free
tail with both colors reflection-recurrent. This closes the
enumerated-Schreier first-tail route in Corollary 13.1l.3a.
Corollary 8.6g''''.1 gives the packet version: if \(S\subset C\),
\(t-S\subset D\), and \(D\) is recurrent, then \(|S|\le2\). A recurrence
center for \(t-S\) shifts all but one element of \(S\) by a fixed nonzero
\(h\) inside \(C\), which a Sidon set cannot do twice.
Lemma 8.6g''''.2 gives the finite-color version: in a \(q\)-color Sidon
partition up to a finite exceptional set, any recurrent color has at most
\(q\) elements. Thus no finite certificate-free coloring of a cofinite
tail can have all colors recurrent. This is the likely replacement for the
old rank-sensitive certificate-free-color escape in fixed-rank barriers.
Corollary 8.6g.1 packages the fixed-rank list version: if every finite test
could be colored by \(r\) moving endpoints so that each endpoint fiber is
certificate-free and has an unbounded reflected center, compactness would
produce \(r\) recurrent Sidon colors, contradicting Lemma 8.6g''''.2.
For variable rank this gives only a quantitative necessary condition. If a
coherent \(q\)-color recurrent Sidon compactification covers a finite test
set \(T\), Lemma 8.6g''''.2 gives \(|T|\le q^2\). Hence ranks
\(q=o(\sqrt{|T|})\) cannot work, but Schreier-scale barriers with
\(q\approx |T|\) can keep splitting the active prefix into singleton or
bounded fibers and avoid any fixed recurrent color with many points. The
next obstruction must force color reuse in such variable-rank barriers.
Warning 8.6g.2 records the construction-side trap. For a hole
\(w\notin3(A\setminus F)\), every active retained row \(e\) has its whole
retained-complement coverage neighborhood
\[
N_e=\{f\in A:w-e-f\in A\setminus F\}
\]
inside \(F\). Deleting the union of these neighborhoods can make rank huge
and fibers tiny, but then any proper subedge that leaves one neighborhood
element retained repairs the witness. Such full neighborhood cuts are
avoidable by an infinite selector unless additional cross-block coding
turns them into a genuine barrier.
The abstract \(\mathcal B_2\) front shows what that coding would have to
look like: full neighborhood cuts whose ranks are controlled by a later
selected point. Locally one can assign singleton neighborhoods
\(N_{e_f}=\{f\}\) and mirrors \(q_f=w-e_f-f\), but order-2 coverage must
then be reserved so no retained element outside \(F\) covers any shifted
row \(w-e_f\). Promoted mirrors create the same demand recursively.
The shape is still finite-quotient compatible:
in \(\mathbb Z/6\mathbb Z\), \(A=\{0,1,2,3\}\) splits into
\(\{0,2\}\cup\{1,3\}\), both colors are certificate-free, \(2A\) is the
whole group, and the center \(3\) swaps the two colors by reflection.
The quotient example has only a one-center/two-point shadow; it does not
survive the integer recurrence demand for arbitrarily many centers on a
three-point test.
Lemma 8.6j-7a records the matching route that would close one color:
if the graphs of representations \(n=c_1+c_2+d\), with
\(c_i\in C\) and \(d\in D\cup E\), have arbitrarily large matchings
eventually, then a sparse deletion from \(C\) leaves an order-3 basis. A
counterexample must therefore keep these cross-residual graphs star-like
or bounded-transversal on infinitely many targets.
Lemma 8.6j-7b identifies those stars with the earlier low-count-star
normal form: in a two-color certificate-free tail, same-color sums have
uniformly bounded two-sum multiplicity, because same-color representations
are Sidon, mixed representations are separated, and only finitely many
exceptional summands remain. Thus a star \(n=p+c+d\) with fixed
\(p,c\in C\) and \(d\in D\cup E\) is exactly a reflected low-count star
with gate \(p\).
Warning 8.6j-7c explains why separate recurrence does not upgrade this to
large matchings: if \(m-U\subset D\) and \(n=m+p\), then the edges
\(\{p,u\}\) form a large star in the cross-residual graph, and
certificate-freeness forbids non-star same-color pairs from using the same
residual rows.
Lemma 8.6j-7d closes one tempting escape inside this two-color setting:
there is an absolute bound on a packet \(S\) with
\[
S+h\subset A,\qquad t-S\subset A,\qquad h\ne0,
\]
after the finite exceptional set is protected. Translation and reflection
each flip colors except for \(O(1)\) elements; then \(s+h\) and \(t-s\)
land in the same color and all sum to \(t+h\), violating Sidon if this
happens for many \(s\). Thus the shifted-overlap branch from Corollary
3.4t cannot be the surviving obstruction in a cofinite two-color
certificate-free tail. The remaining two-color branch is unique-gate:
large reflected packets whose rows \(s+d\) are uniquely represented by the
gate pair.
Corollary 13.1l.5 applies this directly to the enumerated-Schreier
reduction. Once the first tail is cofinally two-colored, the
shifted-overlap branch from Corollary 3.4t is bounded after discarding the
finite exceptional set. Therefore every surviving low-count star in that
route must be a unique-gate packet:
\[
t-S\subset A,\qquad r_{2,A}(s+d)=1\quad(s\in S),
\]
with \(|S|\gg A(w)\) outside every protected finite core.
Hooke's two-color private-incidence check is now Lemma 8.6j-7e. For a
finite deleted set \(F\), a fixed \(c\in F\), and one color \(C_i\), there
is at most one \(a\in F\cap C_i\) for which the \(F+F\)-exception row
\[
w-a-c
\]
is a retained element of the same color \(C_i\). Two such rows would give
a forbidden certificate
\[
b+(w-b-c)-a=w-a-c.
\]
Thus same-color exception incidences are only \(O(|F|)\). This is a real
sharpening of Corollary 8.4c.1, but it still leaves color-flipping
star-like exception windows, so it does not close the private-incidence
obstruction by itself.
Hubble's construction-side check is recorded as Warning 13.1n. A mirrored
packet can meet Lemma 8.4c locally by coloring each retained padder
\(e\) with a deleted element \(\chi(e)\in F\) and adding
\[
q_e=w-e-\chi(e).
\]
Surjectivity of \(\chi\) gives inclusion-minimal repairs after restoring
single deleted vertices. The nonlocal debt is promotion: each \(q_e\)
eventually becomes part of the protected tail, and Lemma 13.1h can poison
all bounded witness ranges for pairs involving \(q_e\) through old retained
endpoints. Therefore a viable mirrored-packet construction must build a
hierarchy of fresh buffers; one self-contained block cannot protect its own
mirrors indefinitely.
The bipartite window diagnostic now reports the largest local unique-gate
packet as `unique_star=(count,d,t,rows)`. In the same top window
\[
A=\{8,9,11,13,15,16\}
\]
it finds
\[
d=16,\quad t=24,\quad S=\{9,11,13,15,16\},
\]
with \(24-S\subset A\) and every \(s+16\) uniquely represented in \(2A\).
Thus Corollary 13.1l.5 narrows the infinite obstruction to unique-gate
packets under the now-impossible cofinite two-color tail; as a finite
diagnostic, that branch remains locally compatible.
Corollary 13.1l.6 splits that remaining branch by color. Since reflection
through \(t\) flips colors except for \(O(1)\) Sidon exceptions, a large
unique-gate packet has a positive subpacket in one of two forms:
same-color unique rows \(s+d\) with \(s,d\) in one color and \(t-s\) in the
other, or mixed degree-one rows \(s+d\) with \(s\) opposite \(d\). Lemma
8.6g'''' rules out this entire cofinite recurrent two-color setting before
those subbranches can become an infinite construction.

This route reaches the Sidon-basis frontier. If \(S\) were a Sidon
asymptotic basis of order \(2\), then
\[
A=(3S+1)\cup(3S+2)
\]
would be an order-2 basis split into two certificate-free classes: residues
modulo \(3\) separate mixed and same-color sums, and a same-color certificate
would be a nontrivial Sidon collision in \(S\). Thus proving that every
order-2 basis has arbitrarily large finite certificate-density would also
rule out Sidon asymptotic bases of order \(2\), a much deeper-looking
statement than the local finite-window checks.

This hypothetical \(A\) would still not be a counterexample to #881:
Sidonicity keeps the two-sum representation multiplicity of \(A\) bounded,
so Corollary 3.4b would produce a good infinite deletion. The lesson is only
that the certificate-density method is too strong as a universal route.

More concretely, deleting \(3T+1\) from the first copy leaves an order-3
basis exactly when
\[
2(S\setminus T)+S
\]
is cofinite. The residue \(1\pmod3\) class must use two retained elements
from \(3(S\setminus T)+1\) and one element from \(3S+2\). Thus ordinary
strong minimality of \(S\), which only makes \(2(S\setminus T)\) fail
cofiniteness, is not enough; a counterexample would need shifted robust
minimality against the extra summand \(S\).

## Robust Residue Boosters

The finite residue obstruction becomes more promising in order \(k=3\).
The script `robust_booster_residue.py` finds
\[
S=\{0,1,3\}\subset\mathbb Z/10\mathbb Z,\qquad f=5.
\]
Here \(4S=\mathbb Z/10\mathbb Z\) and \(3(S\cup\{f\})=\mathbb Z/10\mathbb Z\).
Deleting any residue in \(S\) still leaves a four-sum hole even with the
booster retained: deleting \(0\) leaves only odd summands \(1,3,5\), so
four-fold sums are even; deleting \(1\) misses \(7\); deleting \(3\) misses
\(9\).

This is the right residue-level shape for a negative answer at \(k=3\), but
it is not an integer construction. A thick lift gives whole-residue-class
privacy, not single-integer privacy. The unresolved lifting problem is to
force an individual representative of residue \(0,1\), or \(3\) to be used
in a witness while preserving order-3 coverage with the booster and the
positive-summand buffer from Lemma 13.1d.

The stage search has one nontrivial finite lift:
\[
C_0=\{1,3,20,21\},\quad f=5,\quad C_1=C_0\cup\{30,31\}.
\]
For \(A_1=C_1\cup\{5\}\), three-sums cover through \(47\), and
\[
37\notin4(A_1\setminus\{30\}),\qquad
38\notin4(A_1\setminus\{31\}).
\]
The search then stalls on the next greedy stage, so this is evidence of
local traction rather than an infinite construction.

The cross-stage pair version is more promising locally. Starting from the
same \(C_0\), the pair-stage search first adds \(23\), then adds \(30,31\),
and every old-new pair has a robust four-sum witness below the declared
endpoint. The extended search still finds no third stage. This points to
the same conclusion as the \(k=2\) pair-barrier work: pair barriers are the
right finite shape, but simultaneous domination of all old elements becomes
rapidly expensive.
Diagnostic 16.1 makes the third-stage stall explicit. After
\[
C=\{1,3,20,21,23,30,31\},\qquad f=5,\qquad N=40,
\]
the only singleton candidates extending coverage in the prescribed residue
classes are \(41\) and \(43\), and both fail pair witnesses against
\[
1,\ 3,\ 21,\ 23,\ 31.
\]
So the robust-booster lift is blocked first by simultaneous domination
against many old elements, not by lack of three-fold coverage.

Propositions 13.1b-general and 13.1e now record the exact infinite
criterion behind these searches. For any order \(k\), an iterable
cross-stage pair construction would give an order-\(k\) basis \(A\) such
that every infinite deletion fails at order \(k+1\), and hence fails at
order \(k\) by padding. Thus the robust \(k=3\) booster-pair search is not
just a local curiosity: it is a finite attempt at a complete negative
answer.

## Current Mobile-Fiber Reduction for \(k=2\)

The active-trace branch has now been narrowed past the purely injective
mobile-color model. Lemma 8.5a.7e shows that, after passing to a sufficiently
sparse deletion set, no late-bad finite edge can have all private-color
fibers bounded by a fixed constant. The functional variant Lemma 8.5a.7e'
strengthens this to any prescribed rank function \(\Phi(|F|)\).

Consequently, a surviving \(k=2\) counterexample must force arbitrarily
large one-color private reflected fibers
\[
m-U\subset A\setminus F,\qquad U+f\cap2(A\setminus F)=\varnothing
\]
outside every finite core. Corollary 8.5a.7f.1 splits such fibers into two
rank-free branches:

1. **unique-gate:** \(r_{2,A}(u+f)=1\) for all \(u\in U\);
2. **retained shifted-overlap:** for some fixed \(g\in F\setminus\{f\}\),
   \[
   U+f-g\subset A\setminus F.
   \]

Lemma 8.5a.7i adds a finite-test constraint on the shifted-overlap branch.
Writing \(h=f-g\), any shifted fiber \(U\) that remains certificate-free
relative to \(A\) must be \(h\)-independent:
\[
U\cap(U-h)=\varnothing.
\]
Indeed, \(u,u+h\in U\) and \(U+h\subset A\) would give the certificate
\[
e=u,\qquad y_1=y_2=u+h,\qquad y_1+y_2-e=u+2h\in A.
\]

Lemma 8.5a.7j gives the unique-gate analogue. If \(r_{2,A}(u+f)=1\) for
all \(u\in U\), then \(U\) is independent in the gate-difference graph:
\[
(U+f-U)\cap A\subset\{f\}.
\]
Otherwise \(u+f=v+(u+f-v)\) would be a second two-term representation of
\(u+f\).

Corollaries 8.5a.7k--8.5a.7l package these as finite-palette no-go
criteria. Recurring reflected fibers over a fixed finite gate palette or a
fixed finite shift palette either stay inside the corresponding
certificate-free independence numbers, or they contain a certificate triple
that recurs by reflection and triggers Corollary 2.3c.

Example 8.5a.7m shows why this still does not close the unique-gate branch
locally. For any finite Sidon \(U\), a range-separated packet can choose a
fresh gate \(f=N\), mirrors \(q_u=9N-u\), and a second repair color
\(g=2N\) so that \(w=10N\) is a local collective hole, restoring \(f\)
repairs through every \(u\in U\), and every sum \(u+f\) has the unique full
representation \(u+f\). The moving gate makes gate-independence automatic.

Corollary 8.5a.7n turns the finite-palette criteria into a bounded-center
constraint for actual counterexamples. Fix a finite test \(T_0\). If
oversized unique-gate fibers over a finite gate palette, or oversized
shifted-overlap fibers over a finite shift palette, recur with unbounded
reflection centers \(m\), then a certificate triple in \(T_0\) recurs and
Corollary 2.3c gives a good deletion. Hence every surviving recurrence
over a fixed finite test must either keep the center bounded, move the
gate/shift out of every finite palette, or stay inside the appropriate
certificate-free independence number.

Corollary 8.5a.7o gives the cofinal palette-avoidance version. In the
counterexample extraction, the sparse deletion set \(B\) can be chosen not
only outside a finite core \(E\), but outside any prescribed finite gate
palette \(P\), and with
\[
(B-B)\cap H=\varnothing
\]
for any prescribed finite shift palette \(H\subset\mathbb Z\setminus\{0\}\).
The resulting finite bad edge \(F\subset B\) inherits these exclusions, so
the unique gate avoids \(P\), and any shifted-overlap difference \(f-g\)
avoids \(H\). Thus moving gates and moving shifts are not merely possible;
they are cofinally forced by the remaining counterexample hypothesis.

Corollary 8.5a.7p closes a small quantifier gap in the phrase "outside
every finite core." The large fiber \(U\) itself can also be forced outside
any prescribed finite row core: ask first for \(M+|E_{\rm row}|\) rows and
discard the finitely many that land in \(E_{\rm row}\). Thus both the
deleted active colors and the retained private rows can be made fresh.

Corollary 8.5a.7q makes the whole private packet fresh. Since the map
\[
u\mapsto m-u
\]
is injective, one can also ask for \(|E_{\rm mir}|\) extra rows and discard
the rows whose mirrors \(m-u\) land in a prescribed finite mirror core.
Thus the deleted colors \(F\), retained rows \(U\), and retained mirrors
\(m-U\) can all be chosen outside the current finite stage.

Corollary 8.5a.7r records the resulting promoted-edge debt. Build disjoint
fresh packets and choose one deleted color from each packet. The selected
colors form an infinite subset of the singleton-free tail, so Lemma 8.4
forces arbitrarily late finite bad subsets inside this selector. Since the
selector has at most one color from each packet, every such bad subset is a
cross-packet edge. Thus a counterexample cannot be a disjoint union of
fresh private packets; it must wire selected colors from different packets
into new late-bad edges.

Corollary 8.5a.7s packages this as a product-selector barrier. For each
witness threshold \(L\), the realized selector edges project to a
non-singleton weak barrier on the packet indices, but the arithmetic demand
is stronger than the index shadow: every product selector must contain an
actual realized bad edge, not merely have an index set belonging to an
abstract front.

Corollary 8.5a.7t gives the finite compactness form of this demand. In
every infinite packet tail and for every \(L\), some finite packet window is
already completely product-covered: every choice of one deleted color from
each packet in that finite window contains a realized late-bad edge with
witness \(>L\). This is now the finite combinatorial target for any
negative construction.

Lemma 8.5a.7u adds the selector-cylinder count for those finite windows.
If a family of partial selector edges covers
\[
\prod_{j\in J}F_j,
\]
then
\[
\sum_G\prod_{j\in\sigma(G)}|F_j|^{-1}\ge1.
\]
Thus, when every packet has at least \(m\) choices, avoiding all supports
below rank \(q\) costs at least \(m^q\) realized bad edges in the same
finite window. In particular, finite product covers must either expose
low-rank arithmetic edges or pay a large high-rank edge count.

Corollary 8.5a.7v closes the strongest low-rank subcase: pair edges cannot
themselves form a product-selector subcover on every packet tail. If every
selector through the fresh packets contained an arbitrarily late bad pair,
then the pair-barrier machinery from Corollary 8.6b and Lemmas
8.6g'--8.6g'''' would either give bounded-excess tail recurrence or
compact high-excess endpoint lists into two recurrent certificate-free
colors, both of which are impossible in a counterexample. Thus the
remaining product-cover debt must be genuinely high-rank on some selector
tail.

Corollary 8.5a.7w makes this cofinal: for arbitrarily large \(L\), there is
an infinite packet selector containing no bad pair with witness \(>L\), but
the full product-selector barrier still forces a bad edge inside that same
selector. Such an edge must have rank at least \(3\). The remaining
obstruction is therefore a rank-\(\ge3\) product-cover problem on
pair-avoiding selectors.

Corollary 8.5a.7x also removes bounded second-excess from those pair-free
selector tails. If all high-rank edges in a pair-free selector had witnesses
bounded by their second-smallest deleted color plus \(D\), Lemma 8.6a would
give tail reflection-recurrence from that selector reservoir. Therefore,
for every \(D\), the counterexample must produce a rank-\(\ge3\) edge
\(\{g_1<g_2<\cdots\}\) with witness \(v>g_2+D\).

This is still only a global obstruction. Proposition 10.3g and Lemma 10.3h
show that interval half-cuts locally realize exactly this large-spread
high-rank profile: no coverage-compatible pair deletions, rank at least
\(\lceil M/2\rceil\), and second excess on the order of \(M\). The missing
ingredient is not a finite-window contradiction but a way to prevent such
cuts from being wired into a cross-packet selector barrier.

Corollary 8.5a.7y packages the surviving edge in its final local normal
form. After shrinking for its witness, it is still rank at least \(3\)
because the selector is pair-free and the tail is singleton-free. It is
inclusion-minimal, active at every deleted color, has the terminal retained
gap
\[
(A\setminus F)\cap(v-f_1-m_0,\ v-N_0]=\varnothing,
\]
and every shifted two-sum representation of \(v-e\) for retained \(e\) must
meet \(F\). This is the current object to rule out globally.

Example 8.5a.7z adds a small full product-window warning. The finite set
\[
A_0=\{1,3,4,5,8,10,11,12\}
\]
has \(2A_0\) covering \([4,24]\), every singleton and pair deletion remains
three-fold covered on \([14,23]\), but the packets
\[
\{4,10\},\quad \{5,11\},\quad \{8,12\}
\]
form a complete rank-three product cover by inclusion-minimal terminal-gap
holes with witnesses at most \(23\). The extra covered point \(24\) supplies
the one-point buffer required by Lemma 13.1d for a \(k=2\) staged window.
Thus no purely local argument can rule out pair-free rank-three product
covers; the obstruction must be global.

Warning 8.5a.7z.1 records the first global restriction on this local model.
Disjoint copies of such rank-three product windows are not a selector
barrier: an infinite packet set can take at most two indices from each
finite window and avoid every rank-\(\ge3\) support. Therefore any negative
construction has to wire these terminal-cut supports across windows into a
true weak barrier/front on packet indices.

The first bounded extension search is negative. The script
`product_rank3_extension_search.py --max-value 30 --max-fillers 2` starts
from Example 8.5a.7z, tries to add a fourth two-point packet plus at most
two fillers, and asks every three of the four packets to support a complete
rank-three terminal product window while all singleton and pair deletions
remain harmless. It checks \(20961\) candidates and finds no extension.
This is finite evidence only, but it points to the simultaneous
cross-window closure burden.

Lemma 8.5a.7z.3 gives a rigorous reason common witness layers are too
rigid. If one witness \(v\) works for every selector through three
two-point packets \(P_1,P_2,P_3\), then any retained outside point \(e\)
with \(v-e\) above the order-2 threshold must satisfy
\[
v-e\in\{P_1\text{-sum},P_2\text{-sum},P_3\text{-sum}\}.
\]
So at most three outside retained padders can coexist with such a common
witness. Any iterable product construction must therefore use highly
selector-specific witnesses.

Lemma 8.5a.7z.4 records the general version. If one witness \(v\) works for
a family \(\mathcal C\) of selector deletions, then every shifted two-sum
support representing \(v-e\), with \(e\) retained outside the selectors, is
a transversal of \(\mathcal C\) of size at most two. When there is no
singleton transversal, the possible shifted sums \(v-e\) are confined to
the finite set of two-transversal sums inside \(\bigcup\mathcal C\). Thus,
outside the degenerate common-point case, witness-sharing becomes a finite
hypergraph-transversal question.

The diagnostic `product_rank3_terminal_cover.py` now checks this directly
on Example 8.5a.7z. In its only shared witness class without a singleton
transversal, \(v=22\), the outside shifts \(19,21\) have two-sum supports
\((8,11)\) and \((10,11)\), exactly two-transversals of the three selector
edges sharing that witness.

Lemma 8.5a.7z.5 handles the singleton-transversal exception. For a shared
witness family with common core \(K\), every old retained outside padder is
either accounted for by a two-transversal avoiding \(K\), or it creates a
two-sum representation of \(v-c\) for some common deleted point \(c\in K\).
Thus many old padders below one shared witness force a representation spike
at one of the common colors, up to the finite non-common two-transversal
sum set.

Corollary 8.5a.7z.6 packages this as a capacity inequality for a shared
witness class:
\[
|A\cap[1,v-N_0]\setminus U|
\le |\Sigma_2^0(\mathcal C)|
   +2|K|\max_{c\in K}r_{2,A}(v-c).
\]
So witness reuse must either spend many non-common two-transversal sums or
create a large shifted two-sum spike at a common deleted color. Warning
8.5a.7z.7 then records the negative side: these transversal constraints do
not alone produce an escaping selector, because an abstract rank-three
product front can assign essentially selector-specific witness classes.
Target 8.5a.7z.8 isolates the remaining counterexample skeleton as a
selector-specific reflected front: each front edge and selector receives a
nearly private witness, and every old padder is either a deleted-pair
exception from \(F+F\) or is assigned to a deleted gate and retained mirror.
The retained gate/mirror data must avoid all finite recurrent palettes
while preserving pair-harmlessness, and the \(F+F\) exceptions are bounded
only by the rank-sensitive mass from Lemma 8.4c.
The terminal-cover diagnostic now prints the finite gate-option maps
\(e\mapsto\{f\in F:v-e-f\in A\setminus F\}\), along with deleted-pair
exceptions, for the small rank-three product window, so this bookkeeping is
checked on the local model.
The new `selector_reflected_front_search.py` makes the stricter retained
mirror requirement explicit: on Example 8.5a.7z the ordinary terminal cover
still covers all eight selector triples, but `--require-retained-mirrors`
leaves only four candidates, and `--require-all-gates-active` leaves only
three. Thus a genuine reflected-front counterexample needs more than the
local terminal product cover; it must control the \(F+F\) exception rows.
Lemma 8.5a.7z.10 then compresses any large retained-mirror row set on one
edge: after discarding \(F+F\) rows, a large fiber at one deleted gate gives
either a unique-gate packet or a shifted-overlap packet through a fixed
second deleted gate. The remaining missing promotion is to turn those
one-/two-gate spike supports into recurrent certificates or genuine
late-bad pair debt.
The reflected-front script now reports these branches explicitly for each
candidate by listing usable rows, unique rows, and fixed shifted-overlap
rows for every retained gate.
It also tests same-witness promotion of those supports. In the strict seed
run, all singleton and pair promotion flags are false, confirming that
compression to low-rank spike supports is weaker than producing bad
singleton or pair deletions.
With `--promotion-radius 5`, the strict retained-mirror/all-gates-active
seed still has no nearby low-rank holes; the broader unfiltered seed has
nearby pair holes only in later \((10,11,12)\) selector cases, not at the
original terminal witnesses.
The companion `selector_pair_promotion_scan.py` aggregates these branches:
the strict run has \(6\) directed shifted-overlap branches and no pair holes
at the original witnesses or within radius \(5\); the broader run has
\(34\) directed branches, no holes on \([14,23]\), and nearby holes only at
\(26,27,28\) in the later \((10,11,12)\) selector cases. It also prints the
repair triples, confirming that the original pair deletions are repaired by
the remaining active selector color.
The script `spike_no_promotion_gadget.py` isolates the same point without
the product-window clutter: a rank-three witness can contain a large
shifted-overlap spike on a pair \(\{f,g\}\), but deleting \(\{f,g\}\) still
leaves a third active color \(k\) that repairs the witness. Local spike
support does not imply pair debt.
Example 8.5a.7z.12a generalizes this diagnostic: for arbitrarily large
finite row sets \(U\), a range-separated rank-three terminal hole can carry
a shifted-overlap spike \(U+f-g\subset A\) while every pair deletion inside
\(\{f,g,k\}\) is harmless at the same witness.
But it also has a macroscopic two-sum coverage gap: if \(B=\max U+h\), then
no element below \(9N\) lies outside \([1,B]\), so \(2A_0\) misses
\((2B,10N)\). It is a local obstruction to promotion, not a stage gadget.
The companion script `spike_interval_filler_pressure.py` checks the most
direct filler route: adding a retained low interval \([1,R]\). In the
minimal-repair default gadget, \(R=5003\) is still harmless, while
\(R=5004\) repairs the witness by \(5004+5004+89992=100000\), exactly when
the interval two-sum first covers \(f+\min U\). Thus a stage cannot simply
bridge the low two-sum gap with a long retained interval reaching the
private spike sums.
The script `spike_safe_filler_profile.py` adds the maximal harmless low band
\([1,5003]\) and a second band \([10044,15000]\setminus\{14000\}\). The
full set then has two-sum coverage through \(30000\), all private spike
sums remain absent from the retained two-sumset, and the witness \(100000\)
is still not in the retained three-sumset. So the first coverage gap is not
by itself fatal; the hard stage burden is to continue coverage up to a
declared endpoint beyond the witness, where every retained filler below the
witness creates a shifted terminal-cover obligation.
Corollary 8.5a.7z.12d packages that obligation: any large retained filler
block below a frozen witness and outside the \(F+F\) exception rows is
automatically a row set for Lemma 8.5a.7z.10, hence compresses to a
unique-gate or shifted-overlap spike.
True one-gate terminal barriers are already closed in the \(k=2\) reduction
by Corollaries 8.3 and 8.3b; the only surviving one-gate-looking objects
are unique-gate fibers inside larger active edges, where another active
color repairs the singleton deletion.
Lemma 8.5a.7z.12e records the exact one-step safe filler criterion:
a filler that covers a current two-sum gap \(p\) must be of the form
\(p-a\), but it preserves \(w\notin3C\) only if it avoids
\(w-2C\), \( (w-C)/2\), and \(w/3\). The new
`spike_safe_extension_search.py` applies this to the safe spike profile.
At scale \(100\), beam \(8\) extends full two-sum coverage from \(3000\) to
\(6488\) and stalls at \(6489\); beam \(32\) reaches only \(6501\). The
next-gap candidates are all unsafe because they lie in \(w-2C\), with a
few also hitting \(w-2x\in C\). The script also tests two-point batches
\(x+y=p\) for the stalled gap and finds none at scales \(100\) and \(200\).
Scale \(200\) gives the same ratio, reaching \(12947<20000\). This is
evidence that greedy safe bands hit complement-pair saturation well below
the witness.
With `--allow-pairs`, safe two-point batches can be used earlier in the
beam. They help only slightly: scale \(100\), beam \(32\), reaches \(6578\),
and scale \(200\), beam \(8\), reaches \(12980\), with the same final
no-safe-one/two-point gap obstruction.
Lemma 8.5a.7z.12e' explains why the two-point check is enough for that
final gap: any finite batch that covers a new two-sum gap contains either a
one-new-point representation or a two-new-point representation of the gap,
and adding more retained points cannot remove a three-sum repair of the
witness.
Lemma 8.5a.7z.12e'' identifies the exact certificate behind the stall:
if \(d=w-p\in C\) and \(d+a\in2C\) for every old summand \(a\) that could
pair with a new point to cover \(p\), then every one-new or two-new gap
repair also repairs \(w\). The scale-\(100\), beam-\(8\), pair-batch run
prints this certificate with \(d=3494\) and all \(1034\) one-point
candidates reflected into \(2C\). Coarse coverage past a fixed fraction of
\(w\) is not enough by itself; the blocker is the reflected condition.
Corollary 8.5a.7z.12e''' simplifies the check in the current retained/deleted
split: once \(d=w-p\) is retained, every retained old summand reflects
automatically as \(d+a\in C+C\), so only the deleted gates need separate
checking. The default terminal state has
\[
d+\{1000,1007,2000\}\subset2C.
\]
Corollary 8.5a.7z.12g then limits how far this exact wall can persist at
fixed rank: if \(T\) is a set of retained defects \(d\) with
\(w-\max T\ge N_0\) and \(T+F\subset2C\), then
\[
|T|\le |F+F|.
\]
So a fixed deleted packet can create only finitely many retained-complement
blockers above the order-2 threshold; a global obstruction must either keep
moving the packet \(F\), grow its rank, or use the private-incidence escape
\(w-d=f+c\) with \(d+f\notin2C\).
The script now prints `no_finite_batch_by_12e_prime=True` for that terminal
state, making the Lemma 8.5a.7z.12e' certificate explicit.
The seed-geometry scan in the same script varies the upper retained band.
At scale \(100\), interval upper endpoints \(1200,1400,1600,1800\) still
stall in reflected blockers, with best cover endpoints \(6465,6506,6200\),
and \(6550\). A greedy-safe upper band with endpoint \(2500\) reaches
\(6898\), while endpoints \(3200\) and \(5000\) already have initial
coverage \(6899\) and immediately stall at \(6900\); the blocker has
\(d=3100\) and the same deleted-gate reflection condition.
The adjacent greedy-safe endpoint \(3000\) also starts with coverage
\(6899\) and stalls at \(6900\), but \(d=3100\notin C\). It still has no
safe one-point or two-point batch. Lemma 8.5a.7z.12h packages this as a
one-sided saturation blocker: the run has \(2312\) saturated one-point
candidates and \(1138/1138\) saturated two-point splits. Thus the finite
pair-saturation obstruction is broader than the clean retained-defect
certificate.
With `--avoid-reflected-blockers`, the same scale-\(100\), beam-\(8\) run
still reaches only \(6503\). At the stopping step, the script reports
\(128\) raw extensions and \(0\) surviving after the reflected-blocker
filter. So the finite profile does not merely end at a bad reflected state;
the available local safe moves all enter one.
Corollary 8.5a.7z.13 records the stable case that is already closed: if
the compressed unique-gate or shifted-overlap packets recur inside one
finite row test with gates or shifts in fixed finite palettes and exceed
the corresponding independence thresholds, Corollaries 8.5a.7k--8.5a.7l
produce a recurrent certificate and a good deletion.
Target 8.5a.7z.14 is now the live form: a surviving construction must have
a true cross-window selector front of moving compressed spikes, no pair
promotion, no stable finite row/gate/shift palettes, and enough coverage
fillers to bridge the two-sum gaps without repairing the protected
witnesses.

Thus the live \(k=2\) obstruction is no longer just "unbounded moving
colors." It must produce large private fibers that either have genuinely
unique full two-sum gates while keeping the gate moving or gate-independent
inside every finite test, or have retained shifted overlaps while keeping
the shift moving or shift-independent inside every finite test. It must do
this cofinally outside every finite palette and finite row/mirror core while
also preventing unbounded reflection centers on any fixed finite-palette
violation. A proof must turn one of these finite product-cover patterns into
a recurrent certificate triple; a counterexample must stage these escaping
fibers while preserving the late-bad barrier for every infinite deletion.
