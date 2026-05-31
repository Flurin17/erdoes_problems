#!/usr/bin/env python3
"""Compare homogeneous and regular induced subgraph sizes in samples."""

from __future__ import annotations

import argparse
import random

import regular_induced as ri


def max_clique_or_independent(graph_mask: int, pc: ri.Precomp) -> tuple[int, int]:
    best_clique = 1
    best_independent = 1
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    for subset in pc.subsets_by_size_desc:
        size = len(pc.vertices[subset])
        if size <= best_clique and size <= best_independent:
            break
        edge_count = 0
        vs = pc.vertices[subset]
        for i, v in enumerate(vs):
            for w in vs[i + 1 :]:
                a, b = sorted((v, w))
                edge_idx = edge_index[(a, b)]
                edge_count += (graph_mask >> edge_idx) & 1
        max_edges = size * (size - 1) // 2
        if edge_count == max_edges:
            best_clique = max(best_clique, size)
        if edge_count == 0:
            best_independent = max(best_independent, size)
    return best_clique, best_independent


def sample(n: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    m = len(pc.edges)
    records: list[tuple[int, int, int]] = []
    for _ in range(trials):
        mask = rng.getrandbits(m)
        reg = ri.max_regular_order(mask, pc)
        clique, indep = max_clique_or_independent(mask, pc)
        records.append((reg, clique, indep))

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"min_regular={min(r for r, _, _ in records)}")
    print(f"min_homogeneous={min(max(c, a) for _, c, a in records)}")
    print(f"max_regular_minus_homogeneous={max(r - max(c, a) for r, c, a in records)}")
    print("sample_records=regular,clique,independent")
    for row in records[: min(20, len(records))]:
        print(f"  {row[0]},{row[1]},{row[2]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--sample", type=int, default=100)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    sample(args.n, args.sample, args.seed)


if __name__ == "__main__":
    main()
