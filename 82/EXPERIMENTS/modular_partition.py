#!/usr/bin/env python3
"""Brute-force modular induced partition checks for fixed graph masks."""

from __future__ import annotations

import argparse
import random
from functools import lru_cache

import modular_lift
import regular_induced as ri


class SearchLimitExceeded(RuntimeError):
    pass


def residue_on(graph_mask: int, subset: int, modulus: int, pc: ri.Precomp) -> int | None:
    if subset == 0:
        return 0
    vertices = pc.vertices[subset]
    residue = (graph_mask & pc.incident[subset][vertices[0]]).bit_count() % modulus
    if all(
        (graph_mask & pc.incident[subset][vertex]).bit_count() % modulus == residue
        for vertex in vertices[1:]
    ):
        return residue
    return None


def find_partition(
    n: int,
    graph_mask: int,
    modulus: int,
    colors: int,
    required_residue: int | None = None,
    min_part_size: int = 0,
    max_part_size: int | None = None,
    node_limit: int | None = None,
) -> list[int] | None:
    pc = ri.precompute(n)
    full = (1 << n) - 1
    modular = [False] * (1 << n)
    modular[0] = True
    indexed_choices = max_part_size is not None
    by_pivot: list[list[int]] | None = [[] for _ in range(n)] if indexed_choices else None
    for subset in range(1, 1 << n):
        residue = residue_on(graph_mask, subset, modulus, pc)
        size = subset.bit_count()
        modular[subset] = residue is not None and (
            required_residue is None or residue == required_residue
        ) and (
            size >= min_part_size
        ) and (
            max_part_size is None or size <= max_part_size
        )
        if modular[subset] and by_pivot is not None:
            rest = subset
            while rest:
                bit = rest & -rest
                by_pivot[bit.bit_length() - 1].append(subset)
                rest ^= bit
    if by_pivot is not None:
        for choices_for_pivot in by_pivot:
            choices_for_pivot.sort(key=lambda item: (item.bit_count(), item), reverse=True)

    choices: dict[tuple[int, int], int] = {}
    nodes = 0
    branches = 0

    @lru_cache(maxsize=None)
    def rec(remaining: int, colors_left: int) -> bool:
        nonlocal branches, nodes
        nodes += 1
        if node_limit is not None and nodes + branches > node_limit:
            raise SearchLimitExceeded
        if remaining == 0:
            return True
        if colors_left == 0:
            return False

        pivot = remaining & -remaining
        pivot_index = pivot.bit_length() - 1
        if by_pivot is not None:
            candidate_iterable = by_pivot[pivot_index]
        else:
            candidate_iterable = None

        if candidate_iterable is not None:
            for sub in candidate_iterable:
                branches += 1
                if node_limit is not None and nodes + branches > node_limit:
                    raise SearchLimitExceeded
                if sub & ~remaining:
                    continue
                if rec(remaining ^ sub, colors_left - 1):
                    choices[(remaining, colors_left)] = sub
                    return True
        else:
            sub = remaining
            while sub:
                branches += 1
                if node_limit is not None and nodes + branches > node_limit:
                    raise SearchLimitExceeded
                if (sub & pivot) and modular[sub] and rec(remaining ^ sub, colors_left - 1):
                    choices[(remaining, colors_left)] = sub
                    return True
                sub = (sub - 1) & remaining
        return False

    if not rec(full, colors):
        return None

    assignment = [-1] * n
    remaining = full
    colors_left = colors
    color = 0
    while remaining:
        sub = choices[(remaining, colors_left)]
        for vertex in range(n):
            if (sub >> vertex) & 1:
                assignment[vertex] = color
        remaining ^= sub
        colors_left -= 1
        color += 1

    return assignment


def random_parity_mask(
    n: int,
    odd: bool,
    rng: random.Random,
    pc: ri.Precomp | None = None,
    edge_index: dict[tuple[int, int], int] | None = None,
) -> int | None:
    if odd and n % 2:
        return None
    if pc is None:
        pc = ri.precompute(n)
    if edge_index is None:
        edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    free_edges = [(i, j) for i in range(n - 1) for j in range(i + 1, n - 1)]
    target = 1 if odd else 0
    mask = 0
    parities = [0] * n
    for i, j in free_edges:
        if rng.randrange(2):
            idx = edge_index[(i, j)]
            mask |= 1 << idx
            parities[i] ^= 1
            parities[j] ^= 1
    for i in range(n - 1):
        if parities[i] != target:
            idx = edge_index[(i, n - 1)]
            mask |= 1 << idx
            parities[i] ^= 1
            parities[n - 1] ^= 1
    if parities[n - 1] != target:
        return None
    return mask


def random_full_modular_candidate(
    n: int,
    full_modulus: int,
    edge_count: int,
    rng: random.Random,
    pc: ri.Precomp | None = None,
    edge_index: dict[tuple[int, int], int] | None = None,
) -> int | None:
    if full_modulus > 4 and full_modulus & (full_modulus - 1) == 0:
        return random_full_modular_candidate(
            n, full_modulus // 2, edge_count, rng, pc, edge_index
        )
    if full_modulus == 4:
        odd = bool(rng.randrange(2))
        graph_mask = random_parity_mask(n, odd, rng, pc, edge_index)
        if graph_mask is not None:
            return graph_mask
        return random_parity_mask(n, False, rng, pc, edge_index)
    return rng.getrandbits(edge_count)


def is_connected_graph(n: int, graph_mask: int, pc: ri.Precomp) -> bool:
    if n <= 1:
        return True
    adj = [0] * n
    for index, (u, v) in enumerate(pc.edges):
        if (graph_mask >> index) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    seen = 1
    stack = [0]
    while stack:
        vertex = stack.pop()
        unseen_neighbors = adj[vertex] & ~seen
        while unseen_neighbors:
            bit = unseen_neighbors & -unseen_neighbors
            other = bit.bit_length() - 1
            seen |= bit
            stack.append(other)
            unseen_neighbors ^= bit
    return seen == (1 << n) - 1


def sample_parity_partitions(
    n: int,
    odd: bool,
    modulus: int,
    colors: int,
    trials: int,
    seed: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
    node_limit: int | None,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    accepted = 0
    attempts = 0
    limited = 0
    while accepted < trials:
        attempts += 1
        graph_mask = random_parity_mask(n, odd, rng, pc, edge_index)
        if graph_mask is None:
            continue
        accepted += 1
        try:
            assignment = find_partition(
                n,
                graph_mask,
                modulus,
                colors,
                required_residue,
                min_part_size,
                max_part_size,
                node_limit,
            )
        except SearchLimitExceeded:
            limited += 1
            continue
        if assignment is None:
            print(f"n={n}")
            print(f"parity={'odd' if odd else 'even'}")
            print(f"modulus={modulus}")
            print(f"colors={colors}")
            if required_residue is not None:
                print(f"required_residue={required_residue}")
            if min_part_size:
                print(f"min_part_size={min_part_size}")
            if max_part_size is not None:
                print(f"max_part_size={max_part_size}")
            print(f"trials={trials}")
            print(f"attempts={attempts}")
            print(f"counterexample_at_trial={accepted}")
            print(f"counterexample_mask={graph_mask}")
            return
    print(f"n={n}")
    print(f"parity={'odd' if odd else 'even'}")
    print(f"modulus={modulus}")
    print(f"colors={colors}")
    if required_residue is not None:
        print(f"required_residue={required_residue}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    if node_limit is not None:
        print(f"node_limited={limited}")
    print("no_counterexample_seen")


def sample_full_modular_partitions(
    n: int,
    full_modulus: int,
    modulus: int,
    colors: int,
    trials: int,
    seed: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
    max_attempts: int,
    node_limit: int | None,
    connected_only: bool,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    full = (1 << n) - 1
    edge_count = len(pc.edges)
    accepted = 0
    attempts = 0
    limited = 0
    while accepted < trials and attempts < max_attempts:
        attempts += 1
        graph_mask = random_full_modular_candidate(
            n, full_modulus, edge_count, rng, pc, edge_index
        )
        if graph_mask is None:
            continue
        if not ri.is_modular_on(graph_mask, full, full_modulus, pc):
            continue
        if connected_only and not is_connected_graph(n, graph_mask, pc):
            continue
        accepted += 1
        try:
            assignment = find_partition(
                n,
                graph_mask,
                modulus,
                colors,
                required_residue,
                min_part_size,
                max_part_size,
                node_limit,
            )
        except SearchLimitExceeded:
            limited += 1
            continue
        if assignment is None:
            print(f"n={n}")
            print(f"full_modulus={full_modulus}")
            print(f"modulus={modulus}")
            print(f"colors={colors}")
            if required_residue is not None:
                print(f"required_residue={required_residue}")
            if min_part_size:
                print(f"min_part_size={min_part_size}")
            if max_part_size is not None:
                print(f"max_part_size={max_part_size}")
            if connected_only:
                print("connected_only=True")
            print(f"trials={trials}")
            print(f"attempts={attempts}")
            print(f"accepted_before_counterexample={accepted}")
            print(f"counterexample_mask={graph_mask}")
            return
    print(f"n={n}")
    print(f"full_modulus={full_modulus}")
    print(f"modulus={modulus}")
    print(f"colors={colors}")
    if required_residue is not None:
        print(f"required_residue={required_residue}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    if connected_only:
        print("connected_only=True")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"accepted={accepted}")
    if node_limit is not None:
        print(f"node_limited={limited}")
    print("no_counterexample_seen" if accepted == trials else "max_attempts_reached")


def sample_parity_min_colors(
    n: int,
    odd: bool,
    modulus: int,
    max_colors: int,
    trials: int,
    seed: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
    node_limit: int | None,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    histogram: dict[int | str, int] = {}
    worst_mask = 0
    worst_value = -1
    limited = 0
    for _ in range(trials):
        graph_mask = random_parity_mask(n, odd, rng, pc, edge_index)
        if graph_mask is None:
            continue
        try:
            result = find_min_colors(
                n,
                graph_mask,
                modulus,
                max_colors,
                required_residue,
                min_part_size,
                max_part_size,
                node_limit,
            )
        except SearchLimitExceeded:
            limited += 1
            continue
        value: int | str = result[0] if result is not None else "NA"
        histogram[value] = histogram.get(value, 0) + 1
        numeric = max_colors + 1 if result is None else result[0]
        if numeric > worst_value:
            worst_value = numeric
            worst_mask = graph_mask
    print(f"n={n}")
    print(f"parity={'odd' if odd else 'even'}")
    print(f"modulus={modulus}")
    print(f"max_colors={max_colors}")
    if required_residue is not None:
        print(f"required_residue={required_residue}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    print(f"trials={trials}")
    if node_limit is not None:
        print(f"node_limited={limited}")
    print(f"worst_value={worst_value if worst_value <= max_colors else 'NA'}")
    print(f"worst_mask={worst_mask}")
    print("histogram=min_colors:count")
    for key in sorted(histogram, key=lambda item: max_colors + 1 if item == "NA" else item):
        print(f"  {key}: {histogram[key]}")


def sample_full_modular_min_colors(
    n: int,
    full_modulus: int,
    modulus: int,
    max_colors: int,
    trials: int,
    seed: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
    max_attempts: int,
    node_limit: int | None,
    connected_only: bool,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    full = (1 << n) - 1
    edge_count = len(pc.edges)
    accepted = 0
    attempts = 0
    histogram: dict[int | str, int] = {}
    worst_mask = 0
    worst_value = -1
    limited = 0
    while accepted < trials and attempts < max_attempts:
        attempts += 1
        graph_mask = random_full_modular_candidate(
            n, full_modulus, edge_count, rng, pc, edge_index
        )
        if graph_mask is None:
            continue
        if not ri.is_modular_on(graph_mask, full, full_modulus, pc):
            continue
        if connected_only and not is_connected_graph(n, graph_mask, pc):
            continue
        accepted += 1
        try:
            result = find_min_colors(
                n,
                graph_mask,
                modulus,
                max_colors,
                required_residue,
                min_part_size,
                max_part_size,
                node_limit,
            )
        except SearchLimitExceeded:
            limited += 1
            continue
        value: int | str = result[0] if result is not None else "NA"
        histogram[value] = histogram.get(value, 0) + 1
        numeric = max_colors + 1 if result is None else result[0]
        if numeric > worst_value:
            worst_value = numeric
            worst_mask = graph_mask
    print(f"n={n}")
    print(f"full_modulus={full_modulus}")
    print(f"modulus={modulus}")
    print(f"max_colors={max_colors}")
    if required_residue is not None:
        print(f"required_residue={required_residue}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    if connected_only:
        print("connected_only=True")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"accepted={accepted}")
    if node_limit is not None:
        print(f"node_limited={limited}")
    print(f"worst_value={worst_value if worst_value <= max_colors else 'NA'}")
    print(f"worst_mask={worst_mask}")
    print("histogram=min_colors:count")
    for key in sorted(histogram, key=lambda item: max_colors + 1 if item == "NA" else item):
        print(f"  {key}: {histogram[key]}")


def exhaustive_full_modular_partitions(
    n: int,
    full_modulus: int,
    modulus: int,
    colors: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
    node_limit: int | None,
    limit: int | None,
) -> None:
    pc = ri.precompute(n)
    full = (1 << n) - 1
    total = 1 << len(pc.edges)
    checked = 0
    for graph_mask in range(total):
        if not ri.is_modular_on(graph_mask, full, full_modulus, pc):
            continue
        checked += 1
        if (
            find_partition(
                n,
                graph_mask,
                modulus,
                colors,
                required_residue,
                min_part_size,
                max_part_size,
                node_limit,
            )
            is None
        ):
            print(f"n={n}")
            print(f"full_modulus={full_modulus}")
            print(f"modulus={modulus}")
            print(f"colors={colors}")
            if required_residue is not None:
                print(f"required_residue={required_residue}")
            if min_part_size:
                print(f"min_part_size={min_part_size}")
            if max_part_size is not None:
                print(f"max_part_size={max_part_size}")
            print(f"checked_before_counterexample={checked}")
            print(f"counterexample_mask={graph_mask}")
            return
        if limit is not None and checked >= limit:
            print(f"n={n}")
            print(f"full_modulus={full_modulus}")
            print(f"modulus={modulus}")
            print(f"colors={colors}")
            if required_residue is not None:
                print(f"required_residue={required_residue}")
            if min_part_size:
                print(f"min_part_size={min_part_size}")
            if max_part_size is not None:
                print(f"max_part_size={max_part_size}")
            print(f"limit_reached={limit}")
            print("no_counterexample_seen")
            return
    print(f"n={n}")
    print(f"full_modulus={full_modulus}")
    print(f"modulus={modulus}")
    print(f"colors={colors}")
    if required_residue is not None:
        print(f"required_residue={required_residue}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    print(f"all_ok={checked}")


def assignment_stats(
    n: int, graph_mask: int, assignment: list[int], modulus: int
) -> list[tuple[int, int, int]]:
    pc = ri.precompute(n)
    out = []
    for color in sorted(set(assignment)):
        subset = 0
        for vertex, assigned in enumerate(assignment):
            if assigned == color:
                subset |= 1 << vertex
        if subset == 0:
            continue
        vertices = pc.vertices[subset]
        residues = {
            (graph_mask & pc.incident[subset][vertex]).bit_count() % modulus
            for vertex in vertices
        }
        residue = next(iter(residues)) if len(residues) == 1 else -1
        out.append((color, len(vertices), residue))
    return out


def print_assignment_diagnostics(
    n: int, graph_mask: int, assignment: list[int], modulus: int
) -> None:
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    colors = sorted(set(assignment))
    subsets: dict[int, int] = {}
    full = (1 << n) - 1
    total_degrees = [
        (graph_mask & pc.incident[full][vertex]).bit_count() for vertex in range(n)
    ]
    print(
        "total_degree_residues="
        + ",".join(str(total_degrees[v] % modulus) for v in range(n))
    )
    for color in colors:
        subset = 0
        for vertex, assigned in enumerate(assignment):
            if assigned == color:
                subset |= 1 << vertex
        subsets[color] = subset

    for color in colors:
        vertices = pc.vertices[subsets[color]]
        internal = [
            (graph_mask & pc.incident[subsets[color]][vertex]).bit_count() % modulus
            for vertex in vertices
        ]
        print(
            f"internal color{color}:"
            + ",".join(map(str, internal))
        )
        for other in colors:
            cross = []
            for vertex in vertices:
                count = 0
                other_subset = subsets[other]
                for w in pc.vertices[other_subset]:
                    if vertex == w:
                        continue
                    a, b = sorted((vertex, w))
                    edge_idx = edge_index[(a, b)]
                    count += (graph_mask >> edge_idx) & 1
                cross.append(count % modulus)
            print(f"cross color{color}->color{other}:" + ",".join(map(str, cross)))


def find_min_colors(
    n: int,
    graph_mask: int,
    modulus: int,
    max_colors: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
    node_limit: int | None = None,
) -> tuple[int, list[int]] | None:
    for colors in range(1, max_colors + 1):
        assignment = find_partition(
            n,
            graph_mask,
            modulus,
            colors,
            required_residue,
            min_part_size,
            max_part_size,
            node_limit,
        )
        if assignment is not None:
            return colors, assignment
    return None


def min_partition_count_from_allowed(n: int, allowed: list[bool], max_colors: int) -> int | None:
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def rec(remaining: int) -> int:
        if remaining == 0:
            return 0
        pivot = remaining & -remaining
        best = max_colors + 1
        sub = remaining
        while sub:
            if (sub & pivot) and allowed[sub]:
                value = 1 + rec(remaining ^ sub)
                if value < best:
                    best = value
            sub = (sub - 1) & remaining
        return best

    value = rec(full)
    return value if value <= max_colors else None


def exhaustive_parity_min_colors(
    n: int,
    odd: bool,
    modulus: int,
    max_colors: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
    limit: int | None,
    progress_every: int,
) -> None:
    pc = ri.precompute(n)
    histogram: dict[int | str, int] = {}
    worst_value = -1
    worst_mask = 0
    checked = 0
    for graph_mask in modular_lift.parity_graphs(n, odd):
        checked += 1
        allowed = [False] * (1 << n)
        allowed[0] = True
        for subset in range(1, 1 << n):
            size = subset.bit_count()
            if size < min_part_size:
                continue
            if max_part_size is not None and size > max_part_size:
                continue
            residue = residue_on(graph_mask, subset, modulus, pc)
            allowed[subset] = residue is not None and (
                required_residue is None or residue == required_residue
            )
        result = min_partition_count_from_allowed(n, allowed, max_colors)
        value: int | str = result if result is not None else "NA"
        histogram[value] = histogram.get(value, 0) + 1
        numeric = max_colors + 1 if result is None else result
        if numeric > worst_value:
            worst_value = numeric
            worst_mask = graph_mask
        if progress_every and checked % progress_every == 0:
            print(f"checked={checked}", flush=True)
        if limit is not None and checked >= limit:
            break

    print(f"n={n}")
    print(f"parity={'odd' if odd else 'even'}")
    print(f"modulus={modulus}")
    print(f"max_colors={max_colors}")
    if required_residue is not None:
        print(f"required_residue={required_residue}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    if limit is not None:
        print(f"limit={limit}")
    print(f"checked={checked}")
    print(f"worst_value={worst_value if worst_value <= max_colors else 'NA'}")
    print(f"worst_mask={worst_mask}")
    print("histogram=min_colors:count")
    for key in sorted(histogram, key=lambda item: max_colors + 1 if item == "NA" else item):
        print(f"  {key}: {histogram[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int, nargs="?")
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--colors", type=int, default=3)
    parser.add_argument("--exhaustive-parity", action="store_true")
    parser.add_argument("--exhaustive-full-modular", action="store_true")
    parser.add_argument("--odd", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--progress-every", type=int, default=0)
    parser.add_argument("--sample-parity", type=int, default=0)
    parser.add_argument("--sample-full-modular", type=int, default=0)
    parser.add_argument("--sample-parity-min-colors", type=int, default=0)
    parser.add_argument("--exhaustive-parity-min-colors", action="store_true")
    parser.add_argument("--sample-full-modular-min-colors", type=int, default=0)
    parser.add_argument("--full-modulus", type=int)
    parser.add_argument("--max-attempts", type=int, default=1000000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--required-residue", type=int)
    parser.add_argument("--min-part-size", type=int, default=0)
    parser.add_argument("--max-part-size", type=int)
    parser.add_argument("--balanced", action="store_true")
    parser.add_argument("--connected-only", action="store_true")
    parser.add_argument("--find-min-colors", type=int)
    parser.add_argument("--diagnostics", action="store_true")
    parser.add_argument("--node-limit", type=int)
    args = parser.parse_args()

    min_part_size = args.min_part_size
    max_part_size = args.max_part_size
    if args.balanced:
        min_part_size = args.n // args.colors
        max_part_size = (args.n + args.colors - 1) // args.colors

    if args.sample_parity:
        sample_parity_partitions(
            args.n,
            args.odd,
            args.modulus,
            args.colors,
            args.sample_parity,
            args.seed,
            args.required_residue,
            min_part_size,
            max_part_size,
            args.node_limit,
        )
        return

    if args.sample_parity_min_colors:
        sample_parity_min_colors(
            args.n,
            args.odd,
            args.modulus,
            args.colors,
            args.sample_parity_min_colors,
            args.seed,
            args.required_residue,
            min_part_size,
            max_part_size,
            args.node_limit,
        )
        return

    if args.exhaustive_parity_min_colors:
        exhaustive_parity_min_colors(
            args.n,
            args.odd,
            args.modulus,
            args.colors,
            args.required_residue,
            min_part_size,
            max_part_size,
            args.limit,
            args.progress_every,
        )
        return

    if args.sample_full_modular:
        if args.full_modulus is None:
            parser.error("--sample-full-modular requires --full-modulus")
        sample_full_modular_partitions(
            args.n,
            args.full_modulus,
            args.modulus,
            args.colors,
            args.sample_full_modular,
            args.seed,
            args.required_residue,
            min_part_size,
            max_part_size,
            args.max_attempts,
            args.node_limit,
            args.connected_only,
        )
        return

    if args.sample_full_modular_min_colors:
        if args.full_modulus is None:
            parser.error("--sample-full-modular-min-colors requires --full-modulus")
        sample_full_modular_min_colors(
            args.n,
            args.full_modulus,
            args.modulus,
            args.colors,
            args.sample_full_modular_min_colors,
            args.seed,
            args.required_residue,
            min_part_size,
            max_part_size,
            args.max_attempts,
            args.node_limit,
            args.connected_only,
        )
        return

    if args.exhaustive_full_modular:
        if args.full_modulus is None:
            parser.error("--exhaustive-full-modular requires --full-modulus")
        exhaustive_full_modular_partitions(
            args.n,
            args.full_modulus,
            args.modulus,
            args.colors,
            args.required_residue,
            min_part_size,
            max_part_size,
            args.node_limit,
            args.limit,
        )
        return

    if args.exhaustive_parity:
        checked = 0
        for graph_mask in modular_lift.parity_graphs(args.n, args.odd):
            checked += 1
            if args.progress_every and checked % args.progress_every == 0:
                print(f"checked={checked}", flush=True)
            if (
                find_partition(
                    args.n,
                    graph_mask,
                    args.modulus,
                    args.colors,
                    args.required_residue,
                    min_part_size,
                    max_part_size,
                )
                is None
            ):
                print(f"n={args.n}")
                print(f"parity={'odd' if args.odd else 'even'}")
                print(f"modulus={args.modulus}")
                print(f"colors={args.colors}")
                if args.required_residue is not None:
                    print(f"required_residue={args.required_residue}")
                if min_part_size:
                    print(f"min_part_size={min_part_size}")
                if max_part_size is not None:
                    print(f"max_part_size={max_part_size}")
                print(f"checked_before_counterexample={checked}")
                print(f"counterexample_mask={graph_mask}")
                return
            if args.limit is not None and checked >= args.limit:
                print(f"n={args.n}")
                print(f"parity={'odd' if args.odd else 'even'}")
                print(f"modulus={args.modulus}")
                print(f"colors={args.colors}")
                if args.required_residue is not None:
                    print(f"required_residue={args.required_residue}")
                if min_part_size:
                    print(f"min_part_size={min_part_size}")
                if max_part_size is not None:
                    print(f"max_part_size={max_part_size}")
                print(f"limit_reached={args.limit}")
                print("no_counterexample_seen")
                return
        print(f"n={args.n}")
        print(f"parity={'odd' if args.odd else 'even'}")
        print(f"modulus={args.modulus}")
        print(f"colors={args.colors}")
        if args.required_residue is not None:
            print(f"required_residue={args.required_residue}")
        if min_part_size:
            print(f"min_part_size={min_part_size}")
        if max_part_size is not None:
            print(f"max_part_size={max_part_size}")
        print(f"all_ok={checked}")
        return

    if args.mask is None:
        parser.error("mask is required unless --exhaustive-parity is used")

    if args.find_min_colors is not None:
        try:
            result = find_min_colors(
                args.n,
                args.mask,
                args.modulus,
                args.find_min_colors,
                args.required_residue,
                min_part_size,
                max_part_size,
                args.node_limit,
            )
        except SearchLimitExceeded:
            result = None
            limited = True
        else:
            limited = False
        print(f"n={args.n}")
        print(f"mask={args.mask}")
        print(f"modulus={args.modulus}")
        print(f"max_colors={args.find_min_colors}")
        if args.required_residue is not None:
            print(f"required_residue={args.required_residue}")
        if min_part_size:
            print(f"min_part_size={min_part_size}")
        if max_part_size is not None:
            print(f"max_part_size={max_part_size}")
        if limited:
            print("search_limited=True")
            return
        print(f"min_colors={result[0] if result is not None else 'NA'}")
        if result is not None:
            assignment = result[1]
            print("assignment=" + ",".join(map(str, assignment)))
            stats = assignment_stats(args.n, args.mask, assignment, args.modulus)
            print(
                "parts="
                + " ".join(
                    f"color{color}:size{size}:residue{residue}"
                    for color, size, residue in stats
                )
            )
            if args.diagnostics:
                print_assignment_diagnostics(args.n, args.mask, assignment, args.modulus)
        return

    try:
        assignment = find_partition(
            args.n,
            args.mask,
            args.modulus,
            args.colors,
            args.required_residue,
            min_part_size,
            max_part_size,
            args.node_limit,
        )
    except SearchLimitExceeded:
        assignment = None
        limited = True
    else:
        limited = False
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"modulus={args.modulus}")
    print(f"colors={args.colors}")
    if args.required_residue is not None:
        print(f"required_residue={args.required_residue}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    if limited:
        print("search_limited=True")
        return
    print(f"partition_exists={assignment is not None}")
    if assignment is not None:
        print("assignment=" + ",".join(map(str, assignment)))
        stats = assignment_stats(args.n, args.mask, assignment, args.modulus)
        print(
            "parts="
            + " ".join(
                f"color{color}:size{size}:residue{residue}"
                for color, size, residue in stats
            )
        )
        if args.diagnostics:
            print_assignment_diagnostics(args.n, args.mask, assignment, args.modulus)


if __name__ == "__main__":
    main()
