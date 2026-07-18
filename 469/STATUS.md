# Status: Erdős #469

## Goal

Determine whether
\[
 A=\{n\geq1:n\text{ is a sum of distinct positive proper divisors, and no }m\mid n,
 \ m<n,\text{ is such a sum}\}
\]
has convergent reciprocal sum.  The decisive target is either a proof that
\(\sum_{n\in A}1/n<\infty\), with a summable bound covering every member of
\(A\), or an explicit infinite subfamily of \(A\) whose reciprocal sum
diverges.

## Context

- `PROBLEM.md` is the authoritative statement; no other problem folders or
  repository history have been searched for a solution.
- A number is called **semiperfect** here if it is exactly a sum of a finite,
  nonempty set of distinct positive divisors smaller than itself.
- Divisibility-minimal means semiperfect, while every positive divisor
  \(m\mid n\) with \(m<n\) is not semiperfect.  Thus the test includes
  \(m=1\).  This case is vacuous because 1 has no positive proper divisor.
- The displayed expression \(d_1+\cdots+d_k\) is read with \(k\geq1\).
  Allowing the empty set would not represent any positive \(n\), and a
  one-term representation is impossible because the summand is proper.
- Semiperfectness is distinct from abundance, primitive abundance, and
  weirdness; no equivalence among these notions is assumed.
- The initial analytic reduction to establish is a counting estimate for
  \(A(x)=|A\cap[1,x]|\); for example \(A(x)\ll x/(\log x)^{1+\epsilon}\)
  would imply convergence by dyadic summation.

## Constraints

- No web search, browser, erdosproblems.com query, external literature lookup,
  or Git-history/repository search for a hidden solution.
- Use only the named local files and standard mathematical knowledge; label
  any remembered theorem whose exact hypotheses are uncertain.
- Keep all quantifiers, distinctness, positivity, and proper-divisor
  conditions explicit.  Numerical evidence and agent agreement are not proof.
- Any finite computation must be reproducible, independently checked in small
  cases, and used only as evidence unless it exhausts a provably finite domain.
- Subagents must not run Git commands.  Only the coordinating root agent may
  commit and push, and unrelated work must be preserved.

## Deliverables

- `NOTES.md` containing normalized definitions, equivalent formulations, and
  fully proved structural lemmas.
- Route-specific drafts in `attempts/`, including exact failure points for
  eliminated approaches.
- Deterministic enumeration in `computational/`, with command, range,
  invariants, runtime, and interpreted output.
- A dependency graph for the strongest route and `PROOF.md` containing only
  the strongest coherent self-contained argument.
- A maintained research ledger here, followed by coherent commits and pushes.

## Done when

For a complete solution: every quantifier and endpoint in `PROBLEM.md` is
covered by a dependency-complete convergence proof or divergent construction;
all computational certificates are reproducible; two fresh adversarial agents
find no valid objection; all objections are repaired or recorded; and the
accurate `STATUS.md`/`PROOF.md` state is committed and pushed.  For an honest
partial stopping point: at least one named structural/counting lemma is fully
proved or a route is rigorously eliminated, a reproducible computation and
precise current bottleneck are recorded, and that coherent advance is
committed and pushed.

## State

Phase 0 is complete and a 27-route constructive wave has been run.  The main
claim remains open locally.  The reciprocal subseries is proved convergent
for every fixed value of \(\omega(n)\), and the primitive-nondeficient branch
is summable.  The unsummed branch is localized to minimal semiperfect
extensions of primitive weird cores.

## Ambiguities and conventions

1. The source says “all \(n\)” without explicitly saying positive integers.
   Standard divisor terminology is taken to mean \(n\in\mathbb Z_{>0}\).
2. The source does not state \(k\geq1\), but the written sum
   \(d_1+\cdots+d_k=n>0\) forces a nonempty witness under the usual convention.
3. “This is not true for any \(m\mid n\)” is read literally as the same exact
   subset-sum property for every positive proper divisor, not merely abundant
   divisors and not merely divisors using inherited summands.

## Research ledger

### Proved facts

- Semiperfectness lifts to every multiple; membership in \(A\) can be checked
  on the covers \(n/p\).
- A semiperfect \(n\) is in \(A\) exactly when every witness has gcd 1,
  equivalently every reciprocal-divisor identity has lcm \(n\).
- If \(p^a\Vert n\in A\), every witness uses at least two terms from the
  maximal \(p\)-face and \(p\leq\sigma(n/p^a)\).
- Every perfect number is in \(A\), but \(A\) is not the primitive-abundant
  class: \(350,770\in A\) have the weird proper divisor 70.
- The complete \(\omega\leq2\) classification is \(n=2^ap\) with
  \(2^a<p<2^{a+1}\); its reciprocal sum converges.
- For every fixed \(k\), the reciprocal sum over
  \(A\cap\{\omega(n)=k\}\) converges.  The key cut bound is
  \(P^-(v)\leq2\omega(v)\sigma(u)\) for coprime \(n=uv\in A\).
- New-prime extensions obey an exact subset-sum-defect recurrence; above the
  activation threshold, \(\delta(mp)=p\delta(m)-\sigma(m)\).
- Carry paths for \(p^am\in A\) are shortest paths, yielding
  \(a(p-1)<\sigma(m)\).
- With standard Chebyshev/Mertens/Brun--Titchmarsh inputs, nondeficient \(n\)
  whose largest-prime coatom is deficient have convergent reciprocal sum.
- Exact computation through 10,000 found 128 members and passed an independent
  checker through 1,000; 33 cover quotients were abundant nonsemiperfect.

### Counterexamples

- \(70\) is primitive abundant but not semiperfect.
- \(350\in A\) although 70 is an abundant proper divisor.
- \(770=70\cdot11\in A\), so a weird-core transition may be coprime.
- \(70\cdot149\cdot1489\in A\), giving a two-step chain of abundant
  nonsemiperfect proper divisors.
- Ordinary antichainness, entropy, witness multiplicity, and first subset-sum
  gaps alone are insufficient; the infinite \(2^ap\) family may have unique
  witnesses.

### Route ranking

1. **Defect extension tree:** exact and constructive; needs a uniform
   contraction surviving failed-hit resets.
2. **Carry automaton / valuation faces:** gives prime and exponent bounds;
   needs a global count of shortest accepting paths.
3. **Primitive-core charge:** the primitive-nondeficient branch is closed;
   coprime extensions of saturated weird cores remain.
4. **Fixed-support / prime-chain methods:** every fixed \(\omega\) is closed,
   but constants grow too quickly with \(\omega\).
5. **Near-perfect coatom sieve:** closes the deficient-coatom class while
   leaving abundant nonsemiperfect coatoms.
6. **Explicit construction:** produces multi-layer families, but all proved
   branching mechanisms currently have contracting mass.

### Dead routes and exact failure points

- Replacing “nonsemiperfect proper divisor” by “deficient proper divisor”
  fails at 350.
- Charging to all weird numbers fails because \(70p\) is weird for every
  prime \(p>144\), so the reciprocal sum over weird numbers diverges.
- A bare bound \(p\leq\sigma(m)\), ordinary antichainness, or
  \(A(x)\ll x/\log x\) is not summable.
- Fixed-\(\omega\) bounds cannot presently be summed over \(\omega\).
- Fourier/entropy multiplicity bounds miss infinite unique-witness families.

### Current bottleneck

- Prove a uniform weighted bound for terminal nodes in the exact extension
  tree above each primitive weird core.  It must control thin-shell products
  and failed hits \(p\leq Q(m)=\sigma(m)/\delta(m)\), including resets such as
  \(70\to70\cdot149\to70\cdot149\cdot1489\).  Alternatively, turn such reset
  chains into a divergent explicit family.

### Proof dependency graph

- **D0 (proved):** exact definitions, lifting, cover test, and lcm-full witness
  characterization.
- **D1 (proved):** every fixed-\(\omega\) slice has finite reciprocal mass.
- **D2 (proved, standard analytic inputs):** members with deficient
  largest-prime coatom have finite reciprocal mass.
- **D3 (proved):** same-support extensions of a primitive weird core and
  extensions using any fixed number of new prime supports have finite mass.
- **D4 (proved in several subregimes):** no-carry, repeated-largest-prime,
  and large-gap weird extensions are summable.
- **D5 (open):** a uniform weighted bound for arbitrarily long chains of
  dense failed activations above changing weird cores.
- **Global convergence** follows from D0--D5.  All dependencies except D5 are
  locally closed.  A divergence proof instead needs a branching construction
  inside D5 with verified minimality and a noncontracting reciprocal mass.

### Next assignments

- Complete and audit the route-tournament files in `attempts/`.
- Seek reciprocal contraction in the defect tree, separately for safe primes
  and failed hits.
- Audit the analytic primitive/nondeficient theorem and carry automaton.
- Extend computation while recording defects, failed hits, and parent types.
