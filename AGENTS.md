# Mission

Solve the Erdős problems in this repository. The primary objective is to discover a correct proof, counterexample, construction, or sharp asymptotic—not merely to review known attempts. Treat each selected problem as tractable and keep searching while mathematically distinct routes remain.

# Non-negotiable constraints

- Do not use web search, browsers, search engines, social media, or external solution lookup.
- Do not query erdosproblems.com during a solving run. The `Verbatim statement` section of the fetched `PROBLEM.md` is the authoritative task input; commentary and initial goals may not alter it.
- Do not search the repository or Git history for a hidden solution before doing independent work. Files explicitly named in `PROBLEM.md` or `STATUS.md` are allowed context.
- Standard mathematical knowledge may be used from memory. Clearly label any theorem whose exact statement is uncertain.
- Never turn numerical evidence, agent consensus, or confidence into a claimed proof.
- Do not weaken, reinterpret, or silently repair the statement. Record ambiguities in `STATUS.md` and analyze each plausible reading.
- Preserve failed approaches. A precise obstruction is progress.
- Commit and push coherent progress regularly. Never overwrite unrelated user work.

# Default task contract

Every solving run must begin by writing or updating these five fields in the problem's `STATUS.md`.

## Goal

State the exact theorem, construction, counterexample, estimate, or reduction sought in the current run. Prefer one decisive target over “make progress.”

## Context

List the local files and already established lemmas that matter. State definitions and quantifiers explicitly.

## Constraints

Record forbidden assumptions, permitted background results, relevant parameter ranges, and the no-web-search rule.

## Deliverables

Name the artifacts the run must leave behind: proved lemmas, construction, computation, counterexample search, proof draft, or formalization.

## Done when

Give checkable completion criteria. For a full solution this means a dependency-complete proof or counterexample matching every quantifier. For a partial run it means a named lemma proved, a route rigorously eliminated, or a reproducible computation committed.

# Bias toward solving

Spend most effort producing new mathematics.

- At least 70% of agents in early and middle phases must be constructors, lemma-provers, reducers, or experimentalists.
- At most 30% should be critics until a concrete candidate exists.
- A critic may not merely say a route fails. It must identify the first invalid inference and, when possible, propose the weakest repair lemma.
- Do not start a large referee swarm on an informal idea. First force the idea into explicit lemmas.
- Prefer proving a useful special case or structural lemma over writing another broad strategy memo.
- When stuck, change representation: graph, poset, hypergraph, valuation vector, incidence matrix, residue system, optimization problem, probabilistic model, or computational search.
- Maintain several incompatible routes until evidence eliminates them. Cross-pollinate only after each route has an explicit mechanism.

# Multi-agent protocol

Use subagents whenever tasks can be separated. The root agent owns the statement, global ledger, synthesis, and final correctness.

## Phase 0: normalize the problem

Spawn 3–6 independent agents to:

1. parse every quantifier and convention;
2. test boundary and degenerate cases;
3. derive equivalent formulations;
4. identify source typos or ambiguities without silently fixing them;
5. isolate known-trivial parameter ranges.

The root agent consolidates this into `NOTES.md` and `STATUS.md`.

## Phase 1: broad constructive search

Run 16–48 explicitly different assignments in batches that respect the available concurrency cap. Do not give all agents the generic prompt “solve the problem.” Suitable roles include:

- extremal or minimal-counterexample argument;
- greedy or gap-greedy construction;
- prime-focused or valuation-vector construction;
- probabilistic construction;
- graph or hypergraph translation;
- additive/multiplicative energy and Sidon methods;
- sieve or density increment;
- dyadic decomposition;
- spectral, polynomial, or linear-algebraic method;
- entropy or information argument;
- generating function or Dirichlet-series method;
- explicit finite model and computational conjecture generation;
- reverse engineering the claimed asymptotic constant;
- proving a strategically chosen special case;
- searching for a counterexample to the statement.

Each explorer must return:

1. the proposed mechanism in one paragraph;
2. a chain of precise intermediate lemmas;
3. at least one lemma it can prove completely now;
4. the weakest unsupported step;
5. a concrete falsification test;
6. the next action if the route survives.

## Phase 2: route tournament

Cluster duplicates and retain 4–10 genuinely different routes. Assign each surviving route a small team:

- one lead constructor;
- one lemma specialist;
- one computational experimentalist when applicable;
- one repair-oriented skeptic.

Require teams to write into separate files under `attempts/`. They must not edit the same proof file concurrently. The root agent records the comparison in `STATUS.md`.

## Phase 3: lemma closure

Turn the best route into a dependency graph. Every node must be one of:

- proved locally;
- a precisely stated standard theorem;
- reduced to an explicit finite computation;
- open and assigned to an agent.

Spawn agents on the open nodes, not on the whole problem. Prefer multiple independent attempts at the bottleneck lemma. If a bottleneck fails, preserve the counterexample and revisit the dependency graph.

## Phase 4: adversarial audit

Only after a complete candidate exists, spawn fresh agents to attack:

- quantifiers and uniformity;
- endpoint and small-parameter cases;
- implicit distinctness or multiplicity assumptions;
- asymptotic error terms and dependence of constants;
- injectivity/surjectivity of constructions;
- illegal interchange of limits or sums;
- circular dependencies;
- mismatch between computation and theorem;
- mismatch with the verbatim source statement.

Every objection must cite the exact proof step. Repair the proof rather than arguing by plausibility.

## Phase 5: formalization and finalization

When feasible, formalize the finite/combinatorial core in Lean. Otherwise add executable exhaustive checks for bounded claims. Formalization supplements but does not replace the readable proof.

The final `PROOF.md` must be self-contained, state its dependencies, and distinguish a complete solution from conditional or partial results.

# Persistent files

Each problem folder uses:

- `PROBLEM.md`: verbatim fetched statement, source metadata, and initial target.
- `STATUS.md`: current task contract, result ledger, route ranking, and next actions.
- `NOTES.md`: definitions, equivalent formulations, calculations, and proved lemmas.
- `PROOF.md`: only the strongest coherent proof/counterexample draft.
- `attempts/`: route-specific drafts; one file per route.
- `computational/`: scripts, fixtures, output summaries, and reproduction commands.
- `lean/`: formalization when applicable.

Create missing files as work begins. Do not dump raw agent transcripts into the repository; preserve distilled mathematical content.

# Computation standards

- Use computation to discover structure, falsify lemmas, and certify explicitly finite claims.
- Make searches reproducible with deterministic seeds where possible.
- Record the exact command, parameter range, runtime, and interpretation.
- Add assertions for invariants and independently check small instances.
- A search that finds no counterexample is not a proof unless the remaining domain is provably exhausted.

# Research ledger

After each substantial wave, update `STATUS.md` with:

- new proved facts;
- counterexamples found;
- surviving routes ranked by promise;
- dead routes and exact failure points;
- the current bottleneck lemma;
- next agent assignments;
- whether the main claim remains open, partial, conditional, or complete locally.

# Git workflow

- Inspect `git status` before editing and preserve unrelated changes.
- Only the root/coordinating agent may commit or push. Subagents edit only their assigned files and report milestones to the root.
- The root commits after each coherent milestone: intake, computational result, proved lemma, candidate proof, audit repair, or formalization.
- The root pushes successful commits regularly.
- Use descriptive commit messages naming the problem number and mathematical advance.
- Never claim completion merely because files were generated or agents agreed.

# Completion standard

A problem is locally solved only when all of the following hold:

1. every quantifier and case in `PROBLEM.md` is addressed;
2. the proof or counterexample is dependency-complete;
3. all computations used as certificates are reproducible;
4. at least two fresh adversarial agents fail to find a valid objection;
5. every earlier objection is explicitly resolved or incorporated;
6. `STATUS.md` and `PROOF.md` accurately describe the result without overclaiming;
7. the final state is committed and pushed.

Work with high confidence and persistence: assume a decisive idea can be found, actively invent it, and keep converting intuition into lemmas until the proof closes or a precise obstruction forces a new route.
