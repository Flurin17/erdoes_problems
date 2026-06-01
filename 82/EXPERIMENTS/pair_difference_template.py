#!/usr/bin/env python3
r"""Search pair-difference amplification templates.

For a pair u,v, put A=N(u)\N(v) and B=N(v)\N(u).  If uv is an edge, then
independent X subset A and Y subset B with all cross edges present give a
regular induced subgraph on {u,v} union X union Y.  If uv is a nonedge, then
clique X,Y with no cross edges give the complementary template.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations

import regular_induced as ri


def edge_index(pc: ri.Precomp) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(pc.edges)}


def has_edge(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> bool:
    if u > v:
        u, v = v, u
    return bool(mask & (1 << index[(u, v)]))


def homogeneous(
    mask: int, vertices: tuple[int, ...], value: bool, index: dict[tuple[int, int], int]
) -> bool:
    return all(has_edge(mask, u, v, index) == value for u, v in combinations(vertices, 2))


def cross_homogeneous(
    mask: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    value: bool,
    index: dict[tuple[int, int], int],
) -> bool:
    return all(has_edge(mask, u, v, index) == value for u in left for v in right)


def max_template(mask: int, pc: ri.Precomp) -> tuple[int, tuple[int, ...]]:
    index = edge_index(pc)
    best: tuple[int, tuple[int, ...]] = (0, ())

    for u, v in combinations(range(pc.n), 2):
        uv = has_edge(mask, u, v, index)
        a_side = tuple(
            w
            for w in range(pc.n)
            if w not in (u, v)
            and has_edge(mask, u, w, index)
            and not has_edge(mask, v, w, index)
        )
        b_side = tuple(
            w
            for w in range(pc.n)
            if w not in (u, v)
            and has_edge(mask, v, w, index)
            and not has_edge(mask, u, w, index)
        )
        want_inside = not uv
        want_cross = uv
        for r in range(min(len(a_side), len(b_side)), 0, -1):
            if 2 * r + 2 <= best[0]:
                break
            left_candidates = [
                left
                for left in combinations(a_side, r)
                if homogeneous(mask, left, want_inside, index)
            ]
            if not left_candidates:
                continue
            right_candidates = [
                right
                for right in combinations(b_side, r)
                if homogeneous(mask, right, want_inside, index)
            ]
            for left in left_candidates:
                for right in right_candidates:
                    if cross_homogeneous(mask, left, right, want_cross, index):
                        subset = tuple(sorted((u, v) + left + right))
                        best = (len(subset), subset)
                        break
                if best[0] == 2 * r + 2:
                    break
            if best[0] == 2 * r + 2:
                break
    return best


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    pc = ri.precompute(args.n)
    rng = random.Random(args.seed)
    masks: list[int]
    if args.mask is not None:
        masks = [args.mask]
    else:
        count = args.sample or 1
        masks = [rng.getrandbits(len(pc.edges)) for _ in range(count)]

    best = (0, 0, ())
    for mask in masks:
        size, subset = max_template(mask, pc)
        if size > best[0]:
            best = (size, mask, subset)

    size, mask, subset = best
    print(f"n={args.n}")
    print(f"graphs_checked={len(masks)}")
    print(f"best_template_order={size}")
    print(f"best_mask={mask}")
    print("best_subset=" + ",".join(map(str, subset)))
    if subset:
        subset_mask = sum(1 << v for v in subset)
        print(f"verified_regular={ri.is_regular_on(mask, subset_mask, pc)}")
        print(f"max_regular_order={ri.max_regular_order(mask, pc)}")


if __name__ == "__main__":
    main()
