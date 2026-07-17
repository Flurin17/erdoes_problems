# Status: Erdős #1005

## Goal

Let \(F_n=(a_i/b_i)_{i=0}^{N}\) be the increasing Farey sequence of order \(n\), including \(0/1\) and \(1/1\). Determine, under the intended existential-block interpretation, the maximum index span
\[
f_{\rm span}(n)=\max\{r:\exists s,\ 0\le s\le s+r\le N,\ (a_i-a_j)(b_i-b_j)\ge0\ \forall s\le i<j\le s+r\},
\]
and hence the maximum block cardinality \(f_{\rm card}(n)=f_{\rm span}(n)+1\). Prove matching bounds \(f_{\rm span}(n)=(c+o(1))n\), if true, and determine \(c\). Separately determine the consequence of the literal universal-in-starting-index reading.

## Context

- Authoritative input: `PROBLEM.md`, especially its Verbatim statement and Source ambiguity.
- Standard Farey convention used for normalization: reduced fractions in \([0,1]\) with denominator at most \(n\), ordered increasingly, including \(0/1\) and \(1/1\); alternative endpoint conventions will be compared.
- For \(i<j\), incompatibility is exactly \(a_i<a_j\) together with \(b_i>b_j\). Thus admissible blocks are exactly angularly consecutive sets of primitive points \((a_i,b_i)\) forming a chain in the coordinatewise product order. They need not have monotone numerator or denominator sequences; the initially suggested denominator-only reduction is false.
- Consecutive Farey neighbors satisfy \(a_{i+1}b_i-a_i b_{i+1}=1\) and the denominator recurrence \(b_{i+1}=\lfloor(n+b_{i-1})/b_i\rfloor b_i-b_{i-1}\).
- All facts used in the current partial theorem are proved in `NOTES.md` or `PROOF.md`; unclosed variational/localization steps remain in `attempts/` and are not promoted as theorems.

## Constraints

- No web search, browser, erdosproblems.com query, external literature lookup, or Git-history/repository search for a hidden solution.
- Use only `PROBLEM.md`, `STATUS.md`, artifacts created during this run, and standard mathematical knowledge from memory; label any remembered theorem with uncertain hypotheses.
- Preserve the verbatim quantifiers and analyze ambiguity rather than silently repairing it.
- Numerical evidence is conjecture-generation only unless a finite domain is provably exhausted.
- Parameters: \(n\ge4\); all endpoint, equality, starting-index, and span/cardinality conventions must be handled.
- Only the coordinating root agent may run Git commands, commit, or push.

## Deliverables

- `NOTES.md`: normalized definitions, equivalent formulations, proved local lemmas, and ambiguity analysis.
- `computational/`: two independent exact implementations, invariant checks, all maximizers for recorded ranges, deterministic commands, runtimes, and summaries.
- `attempts/`: distinct route files after clustering the constructive search.
- `PROOF.md`: strongest dependency-complete coherent argument, explicitly labeled complete, conditional, or partial.
- `STATUS.md`: research ledger with proved facts, failed routes, route ranking, bottleneck, assignments, and honest state.
- If a complete candidate is obtained, fresh adversarial audits and finite formal/executable checks where feasible.

## Done when

Full completion requires: (1) every quantifier and convention in the verbatim statement is resolved; (2) an explicit construction gives \((c-o(1))n\) span and a universal argument gives \((c+o(1))n\) under the same convention; (3) span/cardinality and endpoint variants are translated exactly; (4) any computation is reproducible and independently checked; (5) a self-contained dependency-complete `PROOF.md` survives at least two fresh adversarial audits; and (6) the accurate final state is committed and pushed. If full closure is not reached in this run, acceptable partial completion is a named rigorous lemma or eliminated route plus reproducible computation and a precise remaining bottleneck, committed and pushed without overclaiming.

## Quantifier and convention ledger

- **Intended reading:** the displayed condition is required for all pairs inside at least one block, and \(f(n)\) is the largest admissible span. This makes the source's \(l\le k+f(n)\) consistent with span, not cardinality.
- **Literal universal reading:** if the free \(k\) is understood universally, every consecutive window of span \(f(n)\) must work; this defines a different extremum and will be evaluated separately.
- **Endpoints:** primary convention includes \(0/1,1/1\). Each endpoint is compatible with every fraction. For \(n\ge4\), deleting either or both endpoints changes the intended maximum span by at most one and leaves the literal-universal value unchanged.
- **Equality:** equality of either coordinate makes a pair admissible. Repeated numerators and repeated denominators both occur in the interior.
- **Anchor-only reading:** merely inserting \(\exists k\) while checking only pairs \((k,l)\) does not express an all-pairs block and is trivial with \(0/1\): the full sequence works. It is recorded and rejected as the intended reading.

## Research ledger

### Proved facts

- Exact compatibility/product-chain equivalence, Farey neighbor criterion and recurrence, endpoint universality, span/cardinality conversion, literal-universal first-bad-gap formula, and adjacent/distance-two compatibility are proved in `NOTES.md`.
- For \(F_4\), the intended span is \(4\) and literal-universal span is \(2\).
- The interval \([(m-1)/m,(3m-2)/(3m-1)]\), where \(m=\lceil n/5\rceil\), is admissible and has exact cardinality \(n+2\lfloor(n+1)/2\rfloor-\lfloor n/3\rfloor-3\lceil n/5\rceil\) for \(n\ge16\). Hence \(E_n\ge(16/15)n+O(1)\).
- Every product-chain block has span at most \(2n-2\), by the strictly increasing integer rank \(a+b\). Thus \(E_n=\Theta(n)\) unconditionally.

### Candidate constants and counterexamples

- The denominator-monotonicity reduction is false. Example: the consecutive \(F_5\) block \(2/5,1/2,3/5,2/3\) is admissible while both coordinate sequences are nonmonotone.
- Exact small cases \(n=1,\ldots,6\) give intended spans \(1,2,4,4,6,6\) and literal-universal spans \(1,2,4,2,3,3\); these are finite checks, not asymptotic evidence yet.
- Two independent implementations agree through their exhaustive-oracle ranges. Implementation A records all maximizers for \(4\le n\le500\); selected orders through \(n=5000\) converge to the four-defect shape. This motivated, but is not used to prove, the candidate \(c=16/15\).
- At \(n=5000\), the exact maximizing block runs from \(999/1000\) to \(2998/2999\), with span \(5333\).

### Surviving routes

Ranked after a 24-assignment constructive wave:

1. **Defect-layer/cusp envelope:** proves the \(16/15\) construction and reduces the sharp upper bound to a growing-layer/minimum-denominator cusp envelope.
2. **General rational cusp via \(SL_2(\mathbb Z)\):** controls fixed bounded-denominator cusps and suggests a finite envelope after choosing a minimum-denominator point.
3. **Quantitative sieve/geometry:** closes substantial sublinear defect scales and exposes the nonuniform interior linear scale.
4. **Coupled Farey recurrence:** gives exact sign/digit restrictions but no sharp global charge yet.
5. **Exact computation:** independently verified conjecture generation and falsification support.

Distilled routes are under `attempts/`; reproducible searches are under `computational/`.

### Dead routes

- **Denominator-only monotonicity:** first inference fails because increasing fraction value permits simultaneous numerator and denominator decrease, e.g. \(2/5<1/2\).
- **Naive fixed-row CRT uniformization:** periodic witnesses for fixed defect pairs are not uniform when defect indices grow.
- **Complement symmetry:** \(x\mapsto1-x\) does not preserve product-order compatibility.
- **Rank \(a+b\) alone for sharpness:** it yields constant \(2\), not \(16/15\).
- **Naive minimum-denominator localization:** the claim that a side with growing Stern--Brocot parent denominator has \(o(n)\) points is false. For \(n=q^2\), the admissible fan between \((2q-3)/(2q-1)\) and \((q-1)/q\) has \(\Theta(n)\) points while its relevant parent denominator is \(q-1\to\infty\).

### Current bottleneck

Prove the uniform global cusp-envelope lemma: a compatible block with growing defect/transverse scale has at most \((16/15+o(1))n\) terms. The bounded-defect model and explicit lower construction are closed. The hard regimes are interior linear-scale strips and growing-denominator Stern--Brocot fans; the simplest minimum-denominator localization shortcut has an explicit counterexample.

### Next assignments

1. Bound growing-denominator Stern--Brocot fans uniformly, using their exact two-parameter row model.
2. Certify the bounded \((r,s,J)\) cusp-envelope optimization exactly and combine it with the growing-fan estimate.
3. After a complete upper proof exists, launch fresh adversarial audits on quantifiers, endpoints, parity, uniform errors, and the verbatim statement.

## State

Partial locally. The rigorous global theorem currently proved is \((16/15)n+O(1)\le E_n\le2n-2\). The candidate sharp asymptotic \(E_n=(16/15+o(1))n\) remains unproved globally. No completion audit has been launched because the cusp-envelope dependency remains open.
