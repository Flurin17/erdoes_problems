# Exact modal computation for finite additive levels

## Scope and outcome

This route treats the repetition-allowed finite problem.  The script
`computational/modal_exact.py` deterministically computes

\[
 M(N)=\max_{(w_p)\in\mathbb Q^{\pi(N)}}
 \left|\left\{2\leq n\leq N:\sum_{p\leq N}v_p(n)w_p=1\right\}\right|.
\]

By the finite grading theorem in `NOTES.md`, this is exactly the maximum size
of a repetition-allowed PLR subset of \([1,N]\).  The computation is exact,
not a floating-point optimization.  It finds the following complete table for
\(2\leq N\leq50\):

```text
N       2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
M(N)    1  2  2  3  3  4  4  5  5  6  7  8  9  9  9 10 10

N      19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
M(N)   11 12 12 13 14 15 15 16 16 17 18 18 19 19 19 20

N      35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
M(N)   20 20 21 22 23 24 25 26 27 28 29 30 31 31 31 31
```

A separate exact run gives \(M(60)=39\).  These bounded results do not decide
the asymptotic question.

## Exact reduction

Put \(B=\lfloor\sqrt N\rfloor\), and call primes at most \(B\) small.  Every
integer at most \(N\) contains at most one prime \(q>B\), and that prime has
exponent one.  Hence \([2,N]\) is the disjoint union of

1. the small-prime-smooth integers \(S\), and
2. the fibers \(C_q=\{qm:1\leq m\leq\lfloor N/q\rfloor\}\), one for each
   prime \(q>B\).

Fix the small-prime weights \(x=(w_p)_{p\leq B}\), and write
\(g_x(m)=\sum_{p\leq B}v_p(m)w_p\).  The weight \(w_q\) occurs only in
\(C_q\).  It can therefore be chosen independently as \(1-t\), where \(t\)
is a modal value of \(g_x(m)\) on \(1\leq m\leq N/q\).  Consequently

\[
 M(N)=\max_{x\in\mathbb Q^{\pi(B)}}\left(
 \sum_{n\in S}{\bf1}_{g_x(n)=1}
 +\sum_{q>B}\max_t\#\{m\leq N/q:g_x(m)=t\}\right). \tag{1}
\]

The objective in (1) is determined entirely by the truth values of the
rational affine hyperplanes

\[
 g_x(n)=1\quad(n\in S),                                      \tag{2}
\]

and the rational homogeneous hyperplanes

\[
 g_x(a)=g_x(b)\quad
 (1\leq a<b\leq \max_{q>B}\lfloor N/q\rfloor).              \tag{3}
\]

This gives a much smaller exact problem: at \(N=60\), for example, there are
only the four variables \(w_2,w_3,w_5,w_7\).

## Prime-weight candidate recursion and completeness

At every node the program stores each remaining event (2)--(3) as a
primitive integral affine form after all previous exact substitutions.  It
chooses a small-prime variable \(w_p\).  Every rational assignment belongs to
one of the following branches:

- **Generic branch.** None of the remaining forms with nonzero
  \(w_p\)-coefficient vanishes.  All of those events are false and are
  discarded.
- **Candidate branches.** At least one such form vanishes.  Choosing one
  vanishing form solves \(w_p\) as an exact rational affine function of the
  other weights; the program substitutes it into every event.  Proportional
  candidates are canonically merged.

These cases are exhaustive.  The generic branch is realizable because a
finite union of proper rational hyperplanes cannot cover a rational affine
space; the implementation constructs a rational point by a deterministic
integer moment-curve specialization and checks every avoided form exactly.
Repeating the dichotomy eliminates all small-prime weights.  Thus every event
stratum, and hence every possible value of (1), is visited.

The branch-and-bound score records events already forced true and events still
undecided.  Its upper bound declares every undecided event true.  This is
valid: adding a target event can only add a smooth integer, while adding an
equality event only merges cofactor value classes and cannot decrease their
largest class.  States are memoized after canonical primitive-integral
normalization.

All form normalization, substitution, reconstructed weights, additive values,
and modal comparisons use Python integers and `fractions.Fraction`.  No
numerical tolerance occurs.

## Independent exact checks

For every reported optimizer the program reconstructs all prime weights,
forms its exact level set \(A\), and independently performs rational Gaussian
elimination on the valuation rows.  It asserts

\[
 \operatorname{rank}_{\mathbb Q}V_A
 =\operatorname{rank}_{\mathbb Q}[V_A\mid\mathbf1].          \tag{4}
\]

The `--self-check-through 14` mode is a second algorithm: it enumerates every
subset of \(\{2,\ldots,N\}\), tests (4), and compares the resulting maximum
with the prime-weight recursion.  All thirteen cases agree.

Two illustrative exact witnesses are:

- \(N=9\): \(w_2=w_3=1/2\) and \(w_5=w_7=1\), giving
  \(A=\{4,5,6,7,9\}\) and exact ranks \(4=4\).  This shows the search is not
  confined to zero-one thresholds.
- \(N=60\): weights zero at \(2,3\) and one at every prime from \(5\) onward
  give
  \[
  \begin{split}
  A=\{&5,7,10,11,13,14,15,17,19,20,21,22,23,26,28,29,30,31,\\
      &33,34,37,38,39,40,41,42,43,44,45,46,47,51,52,53,56,57,
        58,59,60\},
  \end{split}
  \]
  of size \(39\), with exact ranks \(17=17\).

## Reproduction log

Environment: CPython 3.12.3.  Timings are one run on the current workspace
host and are not performance guarantees.

Small independent exhaustive check:

```bash
/usr/bin/time -f 'wall=%e user=%U maxrss_kb=%M' \
  python3 786/computational/modal_exact.py --self-check-through 14
```

Output summary: agreement for every \(2\leq N\leq14\);
`wall=1.39 user=1.37 maxrss_kb=16956`.

Complete exact range:

```bash
/usr/bin/time -f 'wall=%e user=%U maxrss_kb=%M' \
  python3 786/computational/modal_exact.py --range 2 50
```

Output summary: the table above; every row passed (4);
`wall=16.19 user=16.14 maxrss_kb=30008`.  For \(N=50\) the search visited
9975 canonical recursion nodes, with 3946 bound prunes and 5024 duplicate
prunes; the returned ranks were \(15=15\).

Larger selected instance with the full exact witness:

```bash
/usr/bin/time -f 'wall=%e user=%U maxrss_kb=%M' \
  python3 786/computational/modal_exact.py --N 60 --json
```

Output summary: \(M(60)=39\), 16878 nodes, 6125 bound prunes, 9205 duplicate
prunes, exact ranks \(17=17\);
`wall=8.43 user=8.42 maxrss_kb=22032`.

## Route assessment

**Mechanism.** Eliminate every prime above \(\sqrt N\) by an exact modal
choice, then exhaust the finite rational hyperplane arrangement in the
remaining prime weights by candidate/generic recursion.

**Proved intermediate lemmas.** The large-prime fiber decomposition, modal
elimination identity (1), finite event description (2)--(3), exhaustive
candidate/generic dichotomy, and monotone branch bound are proved above.

**Weakest step for future usefulness.** The algorithm is exponential in the
number and arrangement complexity of the small-prime events.  Nothing in the
finite data supplies a uniform-in-\(N\) anti-concentration bound or a dense
construction.

**Concrete falsification test.** Run the exhaustive subset/rank oracle farther
than \(N=14\), or independently enumerate all flats of (2)--(3); any mismatch
in \(M(N)\) falsifies the recursion or its implementation.  Within the current
range, deleting a candidate branch, using approximate equality, or omitting a
cofactor-pair event is also detected by the built-in rank oracle on small
instances.

**Next action.** Add structural upper bounds for modal class sizes before
attempting larger \(N\), and inspect whether all large optimizers are equivalent
to prime thresholds.  The exact \(N=9\) half-weight optimizer warns that a
zero-one restriction is not valid in general.

## Coordinator rerun

The coordinator reran the exact range \(2\leq N\leq50\) and reproduced every
table entry and exact rank check. Observed resource summary:
\[
\text{wall}=17.28\text{s},\quad
\text{user}=17.25\text{s},\quad
\text{maxrss}=29328\text{ KB}.
\]
