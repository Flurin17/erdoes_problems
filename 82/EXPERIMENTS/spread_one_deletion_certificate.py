#!/usr/bin/env python3
"""Inspect deletion certificates for regular witnesses in spread-one graphs."""

from __future__ import annotations

import argparse
from itertools import combinations

import regular_bitset


def vertices_from_csv(text: str) -> list[int]:
    return [int(part) for part in text.split(",") if part]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--witness", help="regular witness vertices; otherwise search maximum")
    args = parser.parse_args()

    adj = regular_bitset.build_adjacency(args.n, args.mask)
    full = (1 << args.n) - 1
    degrees = [(adj[v] & full).bit_count() for v in range(args.n)]
    low = min(degrees)
    high = max(degrees)
    if high - low != 1:
        raise SystemExit(f"degree spread is {high-low}, not 1")

    if args.witness:
        witness = tuple(vertices_from_csv(args.witness))
        witness_mask = sum(1 << v for v in witness)
        degree = regular_bitset.regular_degree(adj, witness_mask, witness)
        if degree is None:
            raise SystemExit("provided witness is not regular")
    else:
        witness = ()
        degree = None
        for order in range(args.n, 0, -1):
            found, found_degree, _checks = regular_bitset.find_regular_order(
                adj, args.n, order, max_checks=None
            )
            if found is not None:
                witness = found
                degree = found_degree
                break
        if degree is None:
            raise AssertionError("every nonempty graph has a one-vertex regular witness")

    witness_mask = sum(1 << v for v in witness)
    deleted_mask = full ^ witness_mask
    offsets = {v: degrees[v] - low for v in range(args.n)}
    certificate_values = [
        (adj[v] & deleted_mask).bit_count() - offsets[v] for v in witness
    ]

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"low_degree={low}")
    print(f"high_degree={high}")
    print("degree_sequence=" + ",".join(map(str, sorted(degrees))))
    print("witness=" + ",".join(map(str, witness)))
    print(f"witness_order={len(witness)}")
    print(f"witness_degree={degree}")
    print("deleted=" + ",".join(str(v) for v in range(args.n) if deleted_mask & (1 << v)))
    print(
        "trace_minus_offset="
        + ",".join(f"{v}:{value}" for v, value in zip(witness, certificate_values))
    )
    print(f"certificate_constant={len(set(certificate_values)) == 1}")

    deleted_vertices = [v for v in range(args.n) if deleted_mask & (1 << v)]
    print("deleted_trace_counts")
    for v in witness:
        trace = [u for u in deleted_vertices if adj[v] & (1 << u)]
        print(f"{v}:offset={offsets[v]} trace_size={len(trace)} trace={','.join(map(str, trace))}")


if __name__ == "__main__":
    main()
