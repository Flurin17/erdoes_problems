#!/usr/bin/env python3
"""Fixed residue-slot modular partitions.

For the first dyadic lift, the flexible four-part conjecture asks only that
each color class have some internal degree residue modulo 4.  This script
tests the stronger aligned-slot version: can one prescribe the available
residues, e.g. slots 0,1,2,3?
"""

from __future__ import annotations

import argparse
import random
from functools import lru_cache

import modular_partition
import regular_induced as ri


def find_slot_partition(
    n: int,
    graph_mask: int,
    modulus: int,
    slots: tuple[int, ...],
    residue_one_matching: bool = False,
) -> list[int] | None:
    slots = tuple(sorted(slots))
    pc = ri.precompute(n)
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    full = (1 << n) - 1
    residues: dict[int, int] = {}
    by_residue: dict[int, list[int]] = {residue: [] for residue in set(slots)}
    by_residue_pivot: dict[int, list[list[int]]] = {
        residue: [[] for _ in range(n)] for residue in set(slots)
    }
    for subset in range(1, 1 << n):
        residue = modular_partition.residue_on(graph_mask, subset, modulus, pc)
        if residue is not None and residue in by_residue:
            if residue_one_matching and modulus == 4 and residue == 1:
                if any(
                    (graph_mask & pc.incident[subset][vertex]).bit_count() != 1
                    for vertex in pc.vertices[subset]
                ):
                    continue
            residues[subset] = residue
            by_residue[residue].append(subset)
            rest = subset
            while rest:
                bit = rest & -rest
                by_residue_pivot[residue][bit.bit_length() - 1].append(subset)
                rest ^= bit

    for residue in by_residue:
        by_residue[residue].sort(key=lambda subset: (subset.bit_count(), subset), reverse=True)
        for choices in by_residue_pivot[residue]:
            choices.sort(key=lambda subset: (subset.bit_count(), subset), reverse=True)

    choice: dict[tuple[int, tuple[int, ...]], tuple[int, int]] = {}

    def remove_slot(state: tuple[int, ...], residue: int) -> tuple[int, ...] | None:
        out = list(state)
        try:
            out.remove(residue)
        except ValueError:
            return None
        return tuple(out)

    @lru_cache(maxsize=None)
    def rec(remaining: int, state: tuple[int, ...]) -> bool:
        if remaining == 0:
            return True
        if not state:
            return False

        pivot = remaining & -remaining
        for residue in sorted(set(state)):
            next_state = remove_slot(state, residue)
            assert next_state is not None
            for subset in by_residue_pivot[residue][pivot.bit_length() - 1]:
                if subset & ~remaining == 0:
                    if rec(remaining ^ subset, next_state):
                        choice[(remaining, state)] = (subset, residue)
                        return True
        return False

    if not rec(full, slots):
        return None

    assignment = [-1] * n
    remaining = full
    state = slots
    color = 0
    while remaining:
        subset, residue = choice[(remaining, state)]
        for vertex in range(n):
            if (subset >> vertex) & 1:
                assignment[vertex] = color
        next_state = remove_slot(state, residue)
        assert next_state is not None
        state = next_state
        remaining ^= subset
        color += 1
    assert remaining == 0
    return assignment


def find_self_labelled_partition(
    n: int,
    graph_mask: int,
    modulus: int,
) -> list[int] | None:
    slots = tuple(range(modulus))
    assignment = find_slot_partition(n, graph_mask, modulus, slots)
    if assignment is None:
        return None
    stats = modular_partition.assignment_stats(n, graph_mask, assignment, modulus)
    color_to_residue = {color: residue for color, _size, residue in stats}
    return [color_to_residue[color] for color in assignment]


def print_cut_0012_diagnostics(n: int, graph_mask: int, assignment: list[int]) -> None:
    pc = ri.precompute(n)
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    stats = modular_partition.assignment_stats(n, graph_mask, assignment, 4)
    color_to_residue = {color: residue for color, _size, residue in stats}
    zero_colors = [color for color, residue in color_to_residue.items() if residue == 0]
    one_colors = [color for color, residue in color_to_residue.items() if residue == 1]
    two_colors = [color for color, residue in color_to_residue.items() if residue == 2]
    if len(zero_colors) > 2 or len(one_colors) > 1 or len(two_colors) > 1:
        print("cut_0012_diagnostics=not_applicable")
        return

    names = {zero_colors[0]: "A"} if zero_colors else {}
    if len(zero_colors) == 2:
        names[zero_colors[1]] = "B"
    if one_colors:
        names[one_colors[0]] = "C"
    if two_colors:
        names[two_colors[0]] = "D"

    sets: dict[str, list[int]] = {"A": [], "B": [], "C": [], "D": []}
    for vertex, color in enumerate(assignment):
        sets[names[color]].append(vertex)
    for name in ("A", "B", "C", "D"):
        print(f"{name}=" + ",".join(map(str, sets[name])))

    residual = set(sets["A"]) | set(sets["B"])
    color_of_vertex = {vertex: "A" for vertex in sets["A"]}
    color_of_vertex.update({vertex: "B" for vertex in sets["B"]})
    ok = True
    rows = []
    for vertex in sorted(residual):
        deg_h = 0
        opposite = 0
        for other in residual:
            if other == vertex:
                continue
            edge = (min(vertex, other), max(vertex, other))
            if (graph_mask >> edge_index[edge]) & 1:
                deg_h += 1
                if color_of_vertex[other] != color_of_vertex[vertex]:
                    opposite += 1
        if opposite % 4 != deg_h % 4:
            ok = False
        rows.append((vertex, deg_h % 4, opposite % 4))
    print(f"cut_congruence_ok={ok}")
    print("cut_rows=vertex,deg_H_mod4,opposite_mod4")
    for vertex, deg_h, opposite in rows:
        print(f"  {vertex},{deg_h},{opposite}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--slots", type=str, default="0,1,2,3")
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--sample-random", type=int, default=0)
    parser.add_argument("--exhaustive-even", action="store_true")
    parser.add_argument("--self-labelled", action="store_true")
    parser.add_argument("--diagnostics", action="store_true")
    parser.add_argument(
        "--residue-one-matching",
        action="store_true",
        help="for modulus 4, require every residue-1 part to be exactly 1-regular",
    )
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    slots = (
        tuple(range(args.modulus))
        if args.self_labelled
        else tuple(int(item) % args.modulus for item in args.slots.split(",") if item)
    )
    if args.exhaustive_even:
        pc = ri.precompute(args.n)
        edge_index = {edge: i for i, edge in enumerate(pc.edges)}
        free_edges = [
            (i, j)
            for i in range(args.n - 1)
            for j in range(i + 1, args.n - 1)
        ]
        checked = 0
        bad: int | None = None
        for bits in range(1 << len(free_edges)):
            graph_mask = 0
            parities = [0] * args.n
            for k, (i, j) in enumerate(free_edges):
                if (bits >> k) & 1:
                    idx = edge_index[(i, j)]
                    graph_mask |= 1 << idx
                    parities[i] ^= 1
                    parities[j] ^= 1
            for i in range(args.n - 1):
                if parities[i]:
                    idx = edge_index[(i, args.n - 1)]
                    graph_mask |= 1 << idx
                    parities[i] ^= 1
                    parities[args.n - 1] ^= 1
            if parities[args.n - 1]:
                continue
            checked += 1
            if args.self_labelled:
                assignment = find_self_labelled_partition(args.n, graph_mask, args.modulus)
            else:
                assignment = find_slot_partition(
                    args.n,
                    graph_mask,
                    args.modulus,
                    slots,
                    args.residue_one_matching,
                )
            if assignment is None:
                bad = graph_mask
                break
        print(f"n={args.n}")
        print(f"modulus={args.modulus}")
        print("slots=" + ",".join(map(str, slots)))
        if args.residue_one_matching:
            print("residue_one_matching=True")
        print(f"exhaustive_even_checked={checked}")
        if bad is None:
            print("no_counterexample_seen")
        else:
            print(f"counterexample_mask={bad}")
        return

    if args.sample_even or args.sample_random:
        rng = random.Random(args.seed)
        pc = ri.precompute(args.n)
        edge_index = {edge: i for i, edge in enumerate(pc.edges)}
        sample_count = args.sample_even or args.sample_random
        failures: list[int] = []
        for _ in range(sample_count):
            if args.sample_even:
                graph_mask = modular_partition.random_parity_mask(
                    args.n, False, rng, pc, edge_index
                )
                if graph_mask is None:
                    continue
            else:
                graph_mask = rng.getrandbits(len(pc.edges))
            if args.self_labelled:
                assignment = find_self_labelled_partition(args.n, graph_mask, args.modulus)
            else:
                assignment = find_slot_partition(
                    args.n,
                    graph_mask,
                    args.modulus,
                    slots,
                    args.residue_one_matching,
                )
            if assignment is None:
                failures.append(graph_mask)
                break
        print(f"n={args.n}")
        print(f"modulus={args.modulus}")
        print("slots=" + ",".join(map(str, slots)))
        if args.residue_one_matching:
            print("residue_one_matching=True")
        if args.sample_even:
            print(f"sample_even={args.sample_even}")
        else:
            print(f"sample_random={args.sample_random}")
        print(f"seed={args.seed}")
        print(f"failures={len(failures)}")
        if failures:
            print(f"failure_mask={failures[0]}")
        else:
            print("no_counterexample_seen")
        return

    if args.mask is None:
        raise SystemExit("--mask is required unless --sample-even is used")
    if args.self_labelled:
        assignment = find_self_labelled_partition(args.n, args.mask, args.modulus)
    else:
        assignment = find_slot_partition(
            args.n,
            args.mask,
            args.modulus,
            slots,
            args.residue_one_matching,
        )
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"modulus={args.modulus}")
    print("slots=" + ",".join(map(str, slots)))
    if args.residue_one_matching:
        print("residue_one_matching=True")
    if assignment is None:
        print("slot_partition=no")
        return
    print("slot_partition=yes")
    print("assignment=" + ",".join(map(str, assignment)))
    stats = modular_partition.assignment_stats(args.n, args.mask, assignment, args.modulus)
    print("stats=color,size,residue")
    for color, size, residue in stats:
        print(f"  {color},{size},{residue}")
    if args.diagnostics and not args.self_labelled and sorted(slots) == [0, 0, 1, 2]:
        print_cut_0012_diagnostics(args.n, args.mask, assignment)


if __name__ == "__main__":
    main()
