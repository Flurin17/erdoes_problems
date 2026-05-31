#!/usr/bin/env python3
"""Backtracking checker for the `(0,0,1,2)` first-lift matching target.

Colors 0 and 1 are residue-0 modulo 4, color 2 is required to be exactly
1-regular, and color 3 is residue-2 modulo 4.
"""

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
    masks = [0, 0, 0, 0]
    for vertex, color in enumerate(assignment):
        masks[color] |= 1 << vertex
    for vertex, color in enumerate(assignment):
        same = (adj[vertex] & masks[color]).bit_count()
        if color in (0, 1):
            if same % 4 != 0:
                return False
        elif color == 2:
            if same != 1:
                return False
        elif color == 3:
            if same % 4 != 2:
                return False
    return True


def find_assignment(
    n: int,
    graph_mask: int,
    pc: ri.Precomp | None = None,
    node_limit: int | None = None,
    forced_colors: dict[int, int] | None = None,
    good_edge: tuple[int, int] | None = None,
) -> tuple[list[int] | None, int, bool]:
    if pc is None:
        pc = ri.precompute(n)
    adj = adjacency(n, graph_mask, pc)
    if forced_colors is None:
        forced_colors = {}
    order = list(forced_colors) + [
        vertex
        for vertex in sorted(range(n), key=lambda vertex: adj[vertex].bit_count(), reverse=True)
        if vertex not in forced_colors
    ]
    assignment = [-1] * n
    color_masks = [0, 0, 0, 0]
    nodes = 0

    def can_place(vertex: int, color: int) -> bool:
        if color != 2:
            return True
        assigned_c_neighbors = (adj[vertex] & color_masks[2]).bit_count()
        if assigned_c_neighbors > 1:
            return False
        neighbors = adj[vertex] & color_masks[2]
        while neighbors:
            bit = neighbors & -neighbors
            other = bit.bit_length() - 1
            if (adj[other] & color_masks[2]).bit_count() >= 1:
                return False
            neighbors ^= bit
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
        if color == 2:
            return same_assigned <= 1 <= same_assigned + unassigned_neighbors
        target = 0 if color in (0, 1) else 2
        return any(
            same_assigned <= value <= same_assigned + unassigned_neighbors
            for value in range(target, same_assigned + unassigned_neighbors + 1, 4)
        )

    def rec(position: int) -> bool:
        nonlocal nodes
        nodes += 1
        if node_limit is not None and nodes > node_limit:
            raise TimeoutError
        if position == n:
            if good_edge is not None:
                first, second = good_edge
                c1, c2 = assignment[first], assignment[second]
                good = (c1 == c2 == 3) or (c1 != c2 and {c1, c2} != {0, 1})
                if not good:
                    return False
            return verify_assignment(adj, assignment)
        vertex = order[position]
        colors = (forced_colors[vertex],) if vertex in forced_colors else (0, 3, 1, 2)
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

    try:
        return (assignment if rec(0) else None), nodes, False
    except TimeoutError:
        return None, nodes, True


def print_certificate(assignment: list[int]) -> None:
    names = ["A", "B", "C", "D"]
    for color, name in enumerate(names):
        vertices = [vertex for vertex, value in enumerate(assignment) if value == color]
        print(f"{name}=" + ",".join(map(str, vertices)))


def check_mask(
    n: int,
    graph_mask: int,
    node_limit: int | None,
    forced_colors: dict[int, int] | None,
    good_edge: tuple[int, int] | None,
) -> None:
    assignment, nodes, limited = find_assignment(
        n,
        graph_mask,
        node_limit=node_limit,
        forced_colors=forced_colors,
        good_edge=good_edge,
    )
    print(f"n={n}")
    print(f"mask={graph_mask}")
    if good_edge is not None:
        print(f"good_edge={good_edge[0]}:{good_edge[1]}")
    print(f"nodes={nodes}")
    if limited:
        print("matching_slot=unknown")
        return
    if assignment is None:
        print("matching_slot=no")
        return
    print("matching_slot=yes")
    print("assignment=" + ",".join(map(str, assignment)))
    print_certificate(assignment)


def exhaustive_even(
    n: int,
    limit: int | None,
    node_limit: int | None,
    forced_colors: dict[int, int] | None,
    good_edge: tuple[int, int] | None,
) -> None:
    pc = ri.precompute(n)
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    checked = 0
    limited = 0
    for graph_mask in modular_lift.parity_graphs(n, odd=False):
        if good_edge is not None:
            edge = tuple(sorted(good_edge))
            if ((graph_mask >> edge_index[edge]) & 1) == 0:
                continue
        assignment, _nodes, hit_limit = find_assignment(
            n, graph_mask, pc, node_limit, forced_colors, good_edge
        )
        if hit_limit:
            limited += 1
            continue
        checked += 1
        if assignment is None:
            print(f"n={n}")
            print(f"checked_before_counterexample={checked}")
            print(f"limited={limited}")
            print(f"counterexample_mask={graph_mask}")
            return
        if limit is not None and checked >= limit:
            break
    print(f"n={n}")
    if good_edge is not None:
        print(f"good_edge={good_edge[0]}:{good_edge[1]}")
    print(f"checked={checked}")
    print(f"limited={limited}")
    print("no_counterexample_seen")


def sample_even(
    n: int,
    trials: int,
    seed: int,
    node_limit: int | None,
    forced_colors: dict[int, int] | None,
    good_edge: tuple[int, int] | None,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    checked = 0
    limited = 0
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        if graph_mask is None:
            continue
        if good_edge is not None:
            edge = tuple(sorted(good_edge))
            if ((graph_mask >> edge_index[edge]) & 1) == 0:
                continue
        assignment, _nodes, hit_limit = find_assignment(
            n, graph_mask, pc, node_limit, forced_colors, good_edge
        )
        if hit_limit:
            limited += 1
            continue
        checked += 1
        if assignment is None:
            print(f"n={n}")
            print(f"sample_even={trials}")
            print(f"seed={seed}")
            if good_edge is not None:
                print(f"good_edge={good_edge[0]}:{good_edge[1]}")
            print(f"checked_before_counterexample={checked}")
            print(f"limited={limited}")
            print(f"counterexample_mask={graph_mask}")
            return
    print(f"n={n}")
    print(f"sample_even={trials}")
    print(f"seed={seed}")
    if good_edge is not None:
        print(f"good_edge={good_edge[0]}:{good_edge[1]}")
    print(f"checked={checked}")
    print(f"limited={limited}")
    print("no_counterexample_seen")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--exhaustive-even", action="store_true")
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--node-limit", type=int)
    parser.add_argument(
        "--force-color",
        action="append",
        default=[],
        help="force a vertex color as vertex:color; colors 0,1 are zero slots",
    )
    parser.add_argument(
        "--good-edge",
        help="require endpoints u:v to be in a degree-2-suppression-good pattern",
    )
    args = parser.parse_args()
    forced_colors: dict[int, int] = {}
    for item in args.force_color:
        vertex_text, color_text = item.split(":", 1)
        forced_colors[int(vertex_text)] = int(color_text)
    good_edge = None
    if args.good_edge is not None:
        first_text, second_text = args.good_edge.split(":", 1)
        good_edge = (int(first_text), int(second_text))
    if args.mask is not None:
        check_mask(args.n, args.mask, args.node_limit, forced_colors, good_edge)
    elif args.exhaustive_even:
        exhaustive_even(args.n, args.limit, args.node_limit, forced_colors, good_edge)
    elif args.sample_even:
        sample_even(
            args.n, args.sample_even, args.seed, args.node_limit, forced_colors, good_edge
        )
    else:
        raise SystemExit("use --mask, --exhaustive-even, or --sample-even")


if __name__ == "__main__":
    main()
