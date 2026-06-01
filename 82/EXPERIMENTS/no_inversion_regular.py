#!/usr/bin/env python3
"""Census and sampling for inversion-free ordered graphs.

An ordered graph is inversion-free when, for every i<j<k, the edge ij implies
the edge ik.  Equivalently, each vertex i has a later-neighborhood that is a
suffix of the later vertices.  This script represents such a graph by
thresholds t_i, with i adjacent to j>i exactly when j>=t_i.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from itertools import product
from math import exp, factorial, sqrt
from time import monotonic


@dataclass(frozen=True)
class Precomp:
    n: int
    subsets_by_size: list[tuple[int, list[tuple[int, tuple[int, ...]]]]]


def precompute(n: int) -> Precomp:
    by_size: list[tuple[int, list[tuple[int, tuple[int, ...]]]]] = []
    for size in range(n, 0, -1):
        entries = []
        for subset in range(1, 1 << n):
            if subset.bit_count() == size:
                vertices = tuple(v for v in range(n) if (subset >> v) & 1)
                entries.append((subset, vertices))
        by_size.append((size, entries))
    return Precomp(n=n, subsets_by_size=by_size)


def random_thresholds(n: int, rng: random.Random) -> tuple[int, ...]:
    return tuple(rng.randrange(i + 1, n + 1) for i in range(n - 1)) + (n,)


def threshold_ranges(n: int) -> list[range]:
    return [range(i + 1, n + 1) for i in range(n - 1)]


def build_adjacency(n: int, thresholds: tuple[int, ...]) -> list[int]:
    adj = [0] * n
    for i, threshold in enumerate(thresholds):
        for j in range(threshold, n):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def max_regular_order(adj: list[int], pc: Precomp) -> int:
    for size, entries in pc.subsets_by_size:
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                return size
    return 1


def regular_witness(adj: list[int], pc: Precomp) -> tuple[int, int, tuple[int, ...]]:
    for size, entries in pc.subsets_by_size:
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                return size, degree, vertices
    return 1, 0, (0,)


def max_homogeneous_order(adj: list[int], pc: Precomp) -> int:
    for size, entries in pc.subsets_by_size:
        clique_degree = size - 1
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if degree not in (0, clique_degree):
                continue
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                return size
    return 1


def homogeneous_witness(adj: list[int], pc: Precomp) -> tuple[int, str, tuple[int, ...]]:
    for size, entries in pc.subsets_by_size:
        clique_degree = size - 1
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if degree not in (0, clique_degree):
                continue
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                kind = "independent" if degree == 0 else "clique"
                return size, kind, vertices
    return 1, "single", (0,)


def evaluate(n: int, thresholds: tuple[int, ...], pc: Precomp) -> tuple[int, int]:
    adj = build_adjacency(n, thresholds)
    return max_regular_order(adj, pc), max_homogeneous_order(adj, pc)


def parse_thresholds(text: str, n: int) -> tuple[int, ...]:
    values = tuple(int(part) for part in text.replace(" ", "").split(",") if part)
    if len(values) != n:
        raise SystemExit(f"expected {n} thresholds, got {len(values)}")
    for index, value in enumerate(values[:-1]):
        if not index + 1 <= value <= n:
            raise SystemExit(
                f"threshold {index} must lie in [{index + 1}, {n}], got {value}"
            )
    if values[-1] != n:
        raise SystemExit(f"last threshold must be {n}")
    return values


def mutate_thresholds(
    n: int, thresholds: tuple[int, ...], rng: random.Random
) -> tuple[int, ...]:
    index = rng.randrange(n - 1)
    values = list(thresholds)
    values[index] = rng.randrange(index + 1, n + 1)
    return tuple(values)


def score(value: tuple[int, int]) -> tuple[int, int]:
    regular, homogeneous = value
    return regular, homogeneous


def exact(n: int, progress: int) -> None:
    pc = precompute(n)
    ranges = threshold_ranges(n)
    total = factorial(n)
    best_regular = n
    best_homogeneous = n
    regular_hist: dict[int, int] = {}
    homogeneous_hist: dict[int, int] = {}
    examples: list[tuple[tuple[int, ...], int]] = []
    start = monotonic()

    for count, thresholds0 in enumerate(product(*ranges), start=1):
        thresholds = tuple(thresholds0) + (n,)
        regular, homogeneous = evaluate(n, thresholds, pc)
        regular_hist[regular] = regular_hist.get(regular, 0) + 1
        homogeneous_hist[homogeneous] = homogeneous_hist.get(homogeneous, 0) + 1

        if regular < best_regular:
            best_regular = regular
            examples = [(thresholds, homogeneous)]
            print(
                "new_best "
                f"count={count} max_regular={regular} "
                f"max_homogeneous={homogeneous} thresholds={thresholds}",
                flush=True,
            )
        elif regular == best_regular and len(examples) < 5:
            examples.append((thresholds, homogeneous))
        best_homogeneous = min(best_homogeneous, homogeneous)

        if progress and count % progress == 0:
            print(
                f"progress count={count}/{total} best={best_regular} "
                f"elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

    print(f"n={n}")
    print(f"threshold_graphs={total}")
    print(f"min_max_regular={best_regular}")
    print(f"min_max_homogeneous={best_homogeneous}")
    print(f"sqrt_n={sqrt(n):.6f}")
    print(f"regular_histogram={dict(sorted(regular_hist.items()))}")
    print(f"homogeneous_histogram={dict(sorted(homogeneous_hist.items()))}")
    for thresholds, homogeneous in examples:
        print(f"example thresholds={thresholds} max_homogeneous={homogeneous}")


def sample(n: int, samples: int, seed: int, progress: int) -> None:
    pc = precompute(n)
    rng = random.Random(seed)
    best_regular = n
    best_homogeneous = n
    regular_hist: dict[int, int] = {}
    homogeneous_hist: dict[int, int] = {}
    examples: list[tuple[tuple[int, ...], int]] = []
    start = monotonic()

    for count in range(1, samples + 1):
        thresholds = random_thresholds(n, rng)
        regular, homogeneous = evaluate(n, thresholds, pc)
        regular_hist[regular] = regular_hist.get(regular, 0) + 1
        homogeneous_hist[homogeneous] = homogeneous_hist.get(homogeneous, 0) + 1

        if regular < best_regular:
            best_regular = regular
            examples = [(thresholds, homogeneous)]
            print(
                "new_best "
                f"count={count} max_regular={regular} "
                f"max_homogeneous={homogeneous} thresholds={thresholds}",
                flush=True,
            )
        elif regular == best_regular and len(examples) < 5:
            examples.append((thresholds, homogeneous))
        best_homogeneous = min(best_homogeneous, homogeneous)

        if progress and count % progress == 0:
            print(
                f"progress count={count}/{samples} best={best_regular} "
                f"elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

    print(f"n={n}")
    print(f"samples={samples}")
    print(f"seed={seed}")
    print(f"min_seen_max_regular={best_regular}")
    print(f"min_seen_max_homogeneous={best_homogeneous}")
    print(f"sqrt_n={sqrt(n):.6f}")
    print(f"regular_histogram={dict(sorted(regular_hist.items()))}")
    print(f"homogeneous_histogram={dict(sorted(homogeneous_hist.items()))}")
    for thresholds, homogeneous in examples:
        print(f"example thresholds={thresholds} max_homogeneous={homogeneous}")


def fixed(n: int, thresholds: tuple[int, ...]) -> None:
    pc = precompute(n)
    adj = build_adjacency(n, thresholds)
    regular_size, regular_degree, regular_vertices = regular_witness(adj, pc)
    homogeneous_size, homogeneous_kind, homogeneous_vertices = homogeneous_witness(adj, pc)
    print(f"n={n}")
    print(f"thresholds={thresholds}")
    print(f"max_regular_order={regular_size}")
    print(f"regular_degree={regular_degree}")
    print("regular_vertices=" + ",".join(map(str, regular_vertices)))
    print(f"max_homogeneous_order={homogeneous_size}")
    print(f"homogeneous_kind={homogeneous_kind}")
    print("homogeneous_vertices=" + ",".join(map(str, homogeneous_vertices)))


def hill_climb(
    n: int,
    restarts: int,
    steps: int,
    seed: int,
    progress: int,
    temperature: float,
) -> None:
    pc = precompute(n)
    rng = random.Random(seed)
    best_value = (n, n)
    best_thresholds: tuple[int, ...] | None = None
    start = monotonic()
    evaluations = 0

    for restart in range(1, restarts + 1):
        current = random_thresholds(n, rng)
        current_value = evaluate(n, current, pc)
        evaluations += 1

        if score(current_value) < score(best_value):
            best_value = current_value
            best_thresholds = current
            print(
                "new_best "
                f"restart={restart} step=0 max_regular={best_value[0]} "
                f"max_homogeneous={best_value[1]} thresholds={best_thresholds}",
                flush=True,
            )

        for step in range(1, steps + 1):
            candidate = mutate_thresholds(n, current, rng)
            candidate_value = evaluate(n, candidate, pc)
            evaluations += 1

            accept = score(candidate_value) <= score(current_value)
            if not accept and temperature > 0:
                delta = candidate_value[0] - current_value[0]
                accept = rng.random() < exp(-delta / temperature)

            if accept:
                current = candidate
                current_value = candidate_value

            if score(candidate_value) < score(best_value):
                best_value = candidate_value
                best_thresholds = candidate
                print(
                    "new_best "
                    f"restart={restart} step={step} "
                    f"max_regular={best_value[0]} "
                    f"max_homogeneous={best_value[1]} "
                    f"thresholds={best_thresholds}",
                    flush=True,
                )

            if progress and step % progress == 0:
                print(
                    f"progress restart={restart}/{restarts} step={step}/{steps} "
                    f"best_regular={best_value[0]} "
                    f"elapsed={monotonic() - start:.1f}s",
                    flush=True,
                )

    print(f"n={n}")
    print(f"restarts={restarts}")
    print(f"steps={steps}")
    print(f"evaluations={evaluations}")
    print(f"seed={seed}")
    print(f"temperature={temperature}")
    print(f"best_max_regular={best_value[0]}")
    print(f"best_max_homogeneous={best_value[1]}")
    print(f"sqrt_n={sqrt(n):.6f}")
    print(f"best_thresholds={best_thresholds}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--exact", action="store_true")
    parser.add_argument("--thresholds")
    parser.add_argument("--samples", type=int, default=0)
    parser.add_argument("--hill-climb", type=int, default=0, metavar="STEPS")
    parser.add_argument("--restarts", type=int, default=1)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--progress", type=int, default=0)
    parser.add_argument("--temperature", type=float, default=0.0)
    args = parser.parse_args()

    if args.thresholds is not None:
        fixed(args.n, parse_thresholds(args.thresholds, args.n))
    elif args.exact:
        exact(args.n, args.progress)
    elif args.samples > 0:
        sample(args.n, args.samples, args.seed, args.progress)
    elif args.hill_climb > 0:
        hill_climb(
            args.n,
            args.restarts,
            args.hill_climb,
            args.seed,
            args.progress,
            args.temperature,
        )
    else:
        raise SystemExit(
            "choose --exact, --thresholds CSV, --samples N, or --hill-climb STEPS"
        )


if __name__ == "__main__":
    main()
