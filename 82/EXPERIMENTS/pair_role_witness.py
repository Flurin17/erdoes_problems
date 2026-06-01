#!/usr/bin/env python3
"""Print the pair-role profile equations for a regular witness."""

from __future__ import annotations

import argparse
from itertools import combinations


def build_adjacency(n: int, mask: int) -> list[int]:
    adj = [0] * n
    index = 0
    for u, v in combinations(range(n), 2):
        if mask & (1 << index):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        index += 1
    return adj


def vertices_from_csv(text: str) -> list[int]:
    return [int(part) for part in text.split(",") if part]


def role(adj: list[int], u: int, v: int, x: int) -> tuple[str, int]:
    ux = bool(adj[u] & (1 << x))
    vx = bool(adj[v] & (1 << x))
    if ux and not vx:
        return "A", 1
    if vx and not ux:
        return "B", 1
    if ux and vx:
        return "C", 2
    return "E", 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--witness", required=True, help="comma-separated witness vertices")
    parser.add_argument("--pair", help="optional pair u,v from the witness")
    args = parser.parse_args()

    adj = build_adjacency(args.n, args.mask)
    witness = vertices_from_csv(args.witness)
    witness_set = set(witness)
    if args.pair:
        pair_values = vertices_from_csv(args.pair)
        if len(pair_values) != 2:
            parser.error("--pair must be u,v")
        pairs = [tuple(pair_values)]
    else:
        pairs = list(combinations(witness, 2))

    witness_mask = sum(1 << v for v in witness)
    witness_degrees = [(adj[v] & witness_mask).bit_count() for v in witness]
    regular = len(set(witness_degrees)) == 1

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print("witness=" + ",".join(map(str, witness)))
    print(f"witness_regular={regular}")
    if regular:
        print(f"witness_degree={witness_degrees[0]}")

    for u, v in pairs:
        if u not in witness_set or v not in witness_set or u == v:
            parser.error("pair vertices must be distinct and lie in the witness")
        delta = 1 if adj[u] & (1 << v) else 0
        middle = sorted(witness_set - {u, v})
        middle_mask = sum(1 << x for x in middle)
        roles: dict[str, list[int]] = {"A": [], "B": [], "C": [], "E": []}
        offsets: dict[int, int] = {}
        for x in middle:
            label, offset = role(adj, u, v, x)
            roles[label].append(x)
            offsets[x] = offset
        d_pair = delta + len(roles["A"]) + len(roles["C"])
        balanced = len(roles["A"]) == len(roles["B"])
        equations = []
        ok = balanced
        for x in middle:
            internal = (adj[x] & middle_mask).bit_count()
            total = internal + offsets[x]
            equations.append(f"{x}:{internal}+{offsets[x]}={total}")
            if total != d_pair:
                ok = False

        print(f"pair={u},{v}")
        print(f"pair_edge={bool(delta)}")
        print(f"pair_degree_target={d_pair}")
        print(f"balanced_one_sided_roles={balanced}")
        for label in ("A", "B", "C", "E"):
            print(f"{label}=" + ",".join(map(str, roles[label])))
        print("middle_profiles=" + ",".join(equations))
        print(f"pair_role_equations_ok={ok}")


if __name__ == "__main__":
    main()
