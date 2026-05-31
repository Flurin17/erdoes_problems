#!/usr/bin/env python3
"""Check the one-defect sufficient condition for slots (0,0,1,2).

For an even graph G, a set D is a residue-2 defect if:

* every vertex of D has degree 2 mod 4 inside D;
* every vertex outside D has its degree into D congruent to its full degree
  modulo 4.

Then D is the residue-2 slot and V\\D is a zero-residue slot.  This is much
stronger than the full (0,0,1,2) fixed-slot conjecture.
"""

from __future__ import annotations

import argparse
import random

import modular_partition
import regular_induced as ri


def find_defect_set(n: int, graph_mask: int) -> int | None:
    pc = ri.precompute(n)
    full = (1 << n) - 1
    full_residues = [
        (graph_mask & pc.incident[full][vertex]).bit_count() % 4
        for vertex in range(n)
    ]
    for defect in range(1 << n):
        ok = True
        for vertex in range(n):
            degree_to_defect = (
                graph_mask & pc.incident[defect][vertex]
            ).bit_count() % 4
            if (defect >> vertex) & 1:
                if degree_to_defect != 2:
                    ok = False
                    break
            elif degree_to_defect != full_residues[vertex]:
                ok = False
                break
        if ok:
            return defect
    return None


def sample_even(n: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    failures = 0
    checked = 0
    first_failure: int | None = None
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        if graph_mask is None:
            continue
        checked += 1
        if find_defect_set(n, graph_mask) is None:
            failures += 1
            if first_failure is None:
                first_failure = graph_mask
    print(f"n={n}")
    print(f"sample_even_checked={checked}")
    print(f"failures={failures}")
    if first_failure is not None:
        print(f"first_failure_mask={first_failure}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    if args.sample_even:
        sample_even(args.n, args.sample_even, args.seed)
        return
    if args.mask is None:
        raise SystemExit("--mask is required unless --sample-even is used")
    defect = find_defect_set(args.n, args.mask)
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    if defect is None:
        print("defect_set=no")
    else:
        print("defect_set=yes")
        print(f"defect_mask={defect}")
        print(f"defect_size={defect.bit_count()}")


if __name__ == "__main__":
    main()
