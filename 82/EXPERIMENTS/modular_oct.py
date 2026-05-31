#!/usr/bin/env python3
"""Check modular odd-cycle-transversal certificates in even graphs."""

from __future__ import annotations

import argparse
import random

import modular_lift
import modular_partition
import regular_induced as ri


def adjacency(n: int, graph_mask: int, pc: ri.Precomp) -> list[int]:
    out = [0] * n
    for index, (u, v) in enumerate(pc.edges):
        if (graph_mask >> index) & 1:
            out[u] |= 1 << v
            out[v] |= 1 << u
    return out


def verify_assignment(adj: list[int], assignment: list[int]) -> bool:
    """Colors 0/1 are residual bipartition, 2 is residue 1, 3 is residue 2."""
    masks = [0, 0, 0, 0]
    for vertex, color in enumerate(assignment):
        masks[color] |= 1 << vertex
    for vertex, color in enumerate(assignment):
        same = (adj[vertex] & masks[color]).bit_count()
        if color in (0, 1):
            if same:
                return False
        elif color == 2:
            if same % 4 != 1:
                return False
        elif color == 3:
            if same % 4 != 2:
                return False
    return True


def find_assignment(
    n: int,
    graph_mask: int,
    pc: ri.Precomp | None = None,
    forced_residual: set[int] | None = None,
    exact_low_degree: bool = False,
) -> list[int] | None:
    if pc is None:
        pc = ri.precompute(n)
    if forced_residual is None:
        forced_residual = set()
    adj = adjacency(n, graph_mask, pc)
    order = list(forced_residual) + [
        vertex
        for vertex in sorted(range(n), key=lambda item: adj[item].bit_count(), reverse=True)
        if vertex not in forced_residual
    ]
    assignment = [-1] * n
    color_masks = [0, 0, 0, 0]

    def can_place(vertex: int, color: int) -> bool:
        if color in (0, 1) and adj[vertex] & color_masks[color]:
            return False
        return True

    def partial_possible(vertex: int) -> bool:
        color = assignment[vertex]
        if color < 0:
            return True
        same_assigned = (adj[vertex] & color_masks[color]).bit_count()
        unassigned_neighbors = 0
        unseen = adj[vertex]
        while unseen:
            bit = unseen & -unseen
            other = bit.bit_length() - 1
            if assignment[other] < 0:
                unassigned_neighbors += 1
            unseen ^= bit
        if color in (0, 1):
            return same_assigned == 0
        target = 1 if color == 2 else 2
        if exact_low_degree:
            return same_assigned <= target <= same_assigned + unassigned_neighbors
        return any(
            same_assigned <= value <= same_assigned + unassigned_neighbors
            for value in range(target, same_assigned + unassigned_neighbors + 1, 4)
        )

    def rec(position: int) -> bool:
        if position == n:
            return verify_assignment(adj, assignment)
        vertex = order[position]
        colors = (0, 1) if vertex in forced_residual else range(4)
        for color in colors:
            if not can_place(vertex, color):
                continue
            assignment[vertex] = color
            color_masks[color] |= 1 << vertex
            ok = True
            closed = adj[vertex] | (1 << vertex)
            while closed:
                bit = closed & -closed
                other = bit.bit_length() - 1
                if not partial_possible(other):
                    ok = False
                    break
                closed ^= bit
            if ok and rec(position + 1):
                return True
            color_masks[color] ^= 1 << vertex
            assignment[vertex] = -1
        return False

    return assignment if rec(0) else None


def print_certificate(n: int, assignment: list[int]) -> None:
    names = ["A", "B", "C", "D"]
    for color, name in enumerate(names):
        vertices = [vertex for vertex in range(n) if assignment[vertex] == color]
        print(f"{name}=" + ",".join(map(str, vertices)))


def check_mask(
    n: int,
    graph_mask: int,
    root: int | None,
    all_roots: bool,
    exact_low_degree: bool,
) -> None:
    forced = set() if root is None else {root}
    assignment = find_assignment(
        n, graph_mask, forced_residual=forced, exact_low_degree=exact_low_degree
    )
    print(f"n={n}")
    print(f"mask={graph_mask}")
    if root is not None:
        print(f"root={root}")
    if exact_low_degree:
        print("exact_low_degree=True")
    if assignment is None:
        print("modular_oct=no")
        return
    print("modular_oct=yes")
    print("assignment=" + ",".join(map(str, assignment)))
    print_certificate(n, assignment)
    if all_roots:
        pc = ri.precompute(n)
        bad = [
            vertex
            for vertex in range(n)
            if find_assignment(n, graph_mask, pc, {vertex}, exact_low_degree) is None
        ]
        print("all_roots_residual=" + ("yes" if not bad else "no"))
        if bad:
            print("bad_roots=" + ",".join(map(str, bad)))


def exhaustive_even(n: int, limit: int | None, exact_low_degree: bool) -> None:
    pc = ri.precompute(n)
    checked = 0
    for graph_mask in modular_lift.parity_graphs(n, odd=False):
        checked += 1
        if find_assignment(n, graph_mask, pc, exact_low_degree=exact_low_degree) is None:
            print(f"n={n}")
            print(f"checked_before_counterexample={checked}")
            print(f"counterexample_mask={graph_mask}")
            return
        if limit is not None and checked >= limit:
            break
    print(f"n={n}")
    if exact_low_degree:
        print("exact_low_degree=True")
    print(f"checked={checked}")
    print("no_counterexample_seen")


def sample_even(n: int, trials: int, seed: int, exact_low_degree: bool) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    checked = 0
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        if graph_mask is None:
            continue
        checked += 1
        if find_assignment(n, graph_mask, pc, exact_low_degree=exact_low_degree) is None:
            print(f"n={n}")
            print(f"sample_even={trials}")
            print(f"seed={seed}")
            if exact_low_degree:
                print("exact_low_degree=True")
            print(f"checked_before_counterexample={checked}")
            print(f"counterexample_mask={graph_mask}")
            return
    print(f"n={n}")
    print(f"sample_even={trials}")
    print(f"seed={seed}")
    if exact_low_degree:
        print("exact_low_degree=True")
    print(f"checked={checked}")
    print("no_counterexample_seen")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--exhaustive-even", action="store_true")
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--root", type=int)
    parser.add_argument("--all-roots", action="store_true")
    parser.add_argument(
        "--exact-low-degree",
        action="store_true",
        help="require C to be exactly 1-regular and D exactly 2-regular",
    )
    args = parser.parse_args()
    if args.mask is not None:
        check_mask(args.n, args.mask, args.root, args.all_roots, args.exact_low_degree)
    elif args.exhaustive_even:
        exhaustive_even(args.n, args.limit, args.exact_low_degree)
    elif args.sample_even:
        sample_even(args.n, args.sample_even, args.seed, args.exact_low_degree)
    else:
        raise SystemExit("use --mask, --exhaustive-even, or --sample-even")


if __name__ == "__main__":
    main()
