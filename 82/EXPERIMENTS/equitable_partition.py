#!/usr/bin/env python3
"""Compute color-refinement/equitable partition certificates."""

from __future__ import annotations

import argparse
import random

import regular_induced as ri


def neighbor_count(graph_mask: int, edge_index: dict[tuple[int, int], int], v: int, cell: tuple[int, ...]) -> int:
    total = 0
    for w in cell:
        if v == w:
            continue
        a, b = sorted((v, w))
        total += (graph_mask >> edge_index[(a, b)]) & 1
    return total


def equitable_cells(graph_mask: int, pc: ri.Precomp) -> list[tuple[int, ...]]:
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    full = (1 << pc.n) - 1
    degrees = [
        (graph_mask & pc.incident[full][v]).bit_count()
        for v in range(pc.n)
    ]
    classes: dict[int, list[int]] = {}
    for v, degree in enumerate(degrees):
        classes.setdefault(degree, []).append(v)
    cells = [tuple(vs) for _, vs in sorted(classes.items())]

    changed = True
    while changed:
        changed = False
        new_cells: list[tuple[int, ...]] = []
        for cell in cells:
            buckets: dict[tuple[int, ...], list[int]] = {}
            for v in cell:
                signature = tuple(neighbor_count(graph_mask, edge_index, v, other) for other in cells)
                buckets.setdefault(signature, []).append(v)
            if len(buckets) > 1:
                changed = True
            new_cells.extend(tuple(vs) for _, vs in sorted(buckets.items()))
        cells = new_cells
    return cells


def sample(n: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    m = len(pc.edges)
    records: list[tuple[int, int, int]] = []
    for _ in range(trials):
        mask = rng.getrandbits(m)
        cells = equitable_cells(mask, pc)
        records.append((ri.max_regular_order(mask, pc), len(cells), max(len(c) for c in cells)))

    print(f"n={n}")
    print(f"trials={trials}")
    print("records=regular,num_cells,max_cell")
    for row in records[: min(30, len(records))]:
        print(f"  {row[0]},{row[1]},{row[2]}")
    print(f"min_regular={min(r for r, _, _ in records)}")
    print(f"max_num_cells={max(c for _, c, _ in records)}")
    print(f"min_max_cell={min(s for _, _, s in records)}")


def inspect(n: int, mask: int) -> None:
    pc = ri.precompute(n)
    cells = equitable_cells(mask, pc)
    regular = ri.max_regular_order(mask, pc)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"num_cells={len(cells)}")
    print(f"max_cell={max(len(cell) for cell in cells)}")
    print(f"max_regular={regular}")
    for cell in sorted(cells, key=lambda c: (-len(c), c)):
        print("cell size={} vertices={}".format(len(cell), ",".join(map(str, cell))))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--sample", type=int, default=100)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    if args.mask is not None:
        inspect(args.n, args.mask)
    else:
        sample(args.n, args.sample, args.seed)


if __name__ == "__main__":
    main()
