#!/usr/bin/env python3
"""Brute-force module diagnostics for small fixed graph masks."""

from __future__ import annotations

import argparse

import regular_bitset


def is_module(adj: list[int], subset: int, n: int) -> bool:
    for v in range(n):
        if (subset >> v) & 1:
            continue
        hits = (adj[v] & subset).bit_count()
        if hits not in (0, subset.bit_count()):
            return False
    return True


def vertices(mask: int) -> str:
    out = []
    while mask:
        bit = mask & -mask
        out.append(str(bit.bit_length() - 1))
        mask ^= bit
    return ",".join(out)


def inspect(n: int, mask: int) -> None:
    adj = regular_bitset.build_adjacency(n, mask)
    full = (1 << n) - 1
    proper_modules: list[int] = []
    for subset in range(1, full):
        size = subset.bit_count()
        if size == 1:
            continue
        if is_module(adj, subset, n):
            proper_modules.append(subset)

    proper_modules.sort(key=lambda item: (-item.bit_count(), item))
    maximal_modules = []
    for module in proper_modules:
        if not any(module != other and module | other == other for other in proper_modules):
            maximal_modules.append(module)

    print(f"n={n}")
    print(f"mask={mask}")
    print(f"proper_module_count={len(proper_modules)}")
    print(f"is_prime={'yes' if not proper_modules else 'no'}")
    if proper_modules:
        largest = proper_modules[0]
        print(f"largest_module_size={largest.bit_count()}")
        print(f"largest_module_vertices={vertices(largest)}")
    else:
        print("largest_module_size=1")
        print("largest_module_vertices=")
    print(f"maximal_module_count={len(maximal_modules)}")
    for module in maximal_modules[:20]:
        print(f"maximal_module size={module.bit_count()} vertices={vertices(module)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    args = parser.parse_args()
    inspect(args.n, args.mask)


if __name__ == "__main__":
    main()
