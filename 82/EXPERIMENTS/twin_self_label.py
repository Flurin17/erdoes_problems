#!/usr/bin/env python3
"""Self-labelled modular colorings in a twin-class quotient.

Class i has size sizes[i].  If loops[i]=1 it is a clique, otherwise an
independent set; between classes, edges are complete or empty.  The script
searches for counts x[i][r] of vertices in class i assigned residue r such
that every used residue r in class i has same-label degree congruent to r.
"""

from __future__ import annotations

import argparse


def compositions(total: int, parts: int) -> list[tuple[int, ...]]:
    if parts == 1:
        return [(total,)]
    out: list[tuple[int, ...]] = []
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            out.append((first,) + rest)
    out.sort(key=lambda item: (sum(1 for value in item if value), item))
    return out


def edge_bit(edges: int, classes: int, i: int, j: int) -> int:
    if i > j:
        i, j = j, i
    index = 0
    for a in range(classes):
        for b in range(a + 1, classes):
            if a == i and b == j:
                return (edges >> index) & 1
            index += 1
    raise IndexError((classes, i, j))


def check(
    counts: list[tuple[int, ...]],
    loops: int,
    edges: int,
    modulus: int,
) -> bool:
    classes = len(counts)
    for i in range(classes):
        for residue in range(modulus):
            if counts[i][residue] == 0:
                continue
            degree = 0
            if (loops >> i) & 1:
                degree += counts[i][residue] - 1
            for j in range(classes):
                if i != j and edge_bit(edges, classes, i, j):
                    degree += counts[j][residue]
            if degree % modulus != residue:
                return False
    return True


def search(
    sizes: tuple[int, ...],
    loops: int,
    edges: int,
    modulus: int,
    max_nodes: int | None,
) -> tuple[list[tuple[int, ...]] | None, int, bool]:
    choices = [compositions(size, modulus) for size in sizes]
    counts: list[tuple[int, ...]] = []
    nodes = 0
    complete = True

    def dfs(index: int) -> list[tuple[int, ...]] | None:
        nonlocal nodes, complete
        nodes += 1
        if max_nodes is not None and nodes > max_nodes:
            complete = False
            return None
        if index == len(sizes):
            return counts.copy() if check(counts, loops, edges, modulus) else None
        for choice in choices[index]:
            counts.append(choice)
            result = dfs(index + 1)
            counts.pop()
            if result is not None:
                return result
            if not complete:
                return None
        return None

    return dfs(0), nodes, complete


def tree_122_edges() -> int:
    classes = 6
    edge_pairs = {(0, 1), (0, 2), (0, 5), (1, 4), (2, 3)}
    out = 0
    index = 0
    for i in range(classes):
        for j in range(i + 1, classes):
            if (i, j) in edge_pairs:
                out |= 1 << index
            index += 1
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", default="2,2,2,2,2,2")
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--loops", type=int, default=0)
    parser.add_argument("--edges", type=int)
    parser.add_argument("--tree-122", action="store_true")
    parser.add_argument("--max-nodes", type=int, default=100000)
    args = parser.parse_args()
    sizes = tuple(int(item) for item in args.sizes.split(",") if item)
    edges = tree_122_edges() if args.tree_122 else (args.edges or 0)
    result, nodes, complete = search(sizes, args.loops, edges, args.modulus, args.max_nodes)
    print("sizes=" + ",".join(map(str, sizes)))
    print(f"modulus={args.modulus}")
    print(f"loops={args.loops}")
    print(f"edges={edges}")
    print(f"nodes={nodes}")
    print(f"complete={complete}")
    if result is None:
        print("self_labelled=no")
    else:
        print("self_labelled=yes")
        for index, counts in enumerate(result):
            print(f"  class{index}=" + ",".join(map(str, counts)))


if __name__ == "__main__":
    main()
