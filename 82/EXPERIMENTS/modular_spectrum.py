#!/usr/bin/env python3
"""Check exact-size spectra for modular induced subgraphs.

For a graph G and modulus q, the q-modular spectrum is the set of sizes s for
which G has a q-modular induced subgraph on exactly s vertices.  The dyadic
program would be much easier if spectra were usually initial intervals; this
script looks for small counterexamples.
"""

from __future__ import annotations

import argparse
import random

import regular_induced as ri


def spectrum(graph_mask: int, modulus: int, pc: ri.Precomp) -> set[int]:
    out: set[int] = set()
    for subset in range(1, 1 << pc.n):
        if ri.is_modular_on(graph_mask, subset, modulus, pc):
            out.add(len(pc.vertices[subset]))
    return out


def first_gap(spec: set[int]) -> int | None:
    if not spec:
        return 1
    maximum = max(spec)
    for size in range(1, maximum + 1):
        if size not in spec:
            return size
    return None


def exhaustive(n: int, modulus: int, require_full_modulus: int | None) -> None:
    pc = ri.precompute(n)
    total = 1 << len(pc.edges)
    full = (1 << n) - 1
    checked = 0
    gap_count = 0
    first_gap_mask = 0
    first_gap_size = None
    max_top = 0

    for graph_mask in range(total):
        if require_full_modulus is not None and not ri.is_modular_on(
            graph_mask, full, require_full_modulus, pc
        ):
            continue
        checked += 1
        spec = spectrum(graph_mask, modulus, pc)
        max_top = max(max_top, max(spec))
        gap = first_gap(spec)
        if gap is not None:
            gap_count += 1
            if first_gap_size is None:
                first_gap_mask = graph_mask
                first_gap_size = gap

    print(f"n={n}")
    print(f"modulus={modulus}")
    if require_full_modulus is not None:
        print(f"required_full_modulus={require_full_modulus}")
    print(f"checked={checked}")
    print(f"gap_count={gap_count}")
    print(f"max_spectrum_top={max_top}")
    if first_gap_size is not None:
        print(f"first_gap_size={first_gap_size}")
        print(f"first_gap_mask={first_gap_mask}")


def sample(n: int, modulus: int, trials: int, seed: int, require_full_modulus: int | None) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    full = (1 << n) - 1
    edge_count = len(pc.edges)
    checked = 0
    attempts = 0
    gap_count = 0
    first_gap_mask = 0
    first_gap_size = None

    while checked < trials:
        attempts += 1
        graph_mask = rng.getrandbits(edge_count)
        if require_full_modulus is not None and not ri.is_modular_on(
            graph_mask, full, require_full_modulus, pc
        ):
            continue
        checked += 1
        spec = spectrum(graph_mask, modulus, pc)
        gap = first_gap(spec)
        if gap is not None:
            gap_count += 1
            if first_gap_size is None:
                first_gap_mask = graph_mask
                first_gap_size = gap

    print(f"n={n}")
    print(f"modulus={modulus}")
    if require_full_modulus is not None:
        print(f"required_full_modulus={require_full_modulus}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"gap_count={gap_count}")
    if first_gap_size is not None:
        print(f"first_gap_size={first_gap_size}")
        print(f"first_gap_mask={first_gap_mask}")


def analyze_mask(n: int, modulus: int, graph_mask: int) -> None:
    pc = ri.precompute(n)
    spec = spectrum(graph_mask, modulus, pc)
    print(f"n={n}")
    print(f"modulus={modulus}")
    print(f"mask={graph_mask}")
    print("spectrum=" + ",".join(map(str, sorted(spec))))
    print(f"first_gap={first_gap(spec)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--require-full-modulus", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--mask", type=int)
    args = parser.parse_args()

    if args.mask is not None:
        analyze_mask(args.n, args.modulus, args.mask)
    elif args.sample:
        sample(args.n, args.modulus, args.sample, args.seed, args.require_full_modulus)
    else:
        exhaustive(args.n, args.modulus, args.require_full_modulus)


if __name__ == "__main__":
    main()
