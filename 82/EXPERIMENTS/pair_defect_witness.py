#!/usr/bin/env python3
"""Check pair-role equations for two-defect near-regular witnesses."""

from __future__ import annotations

import argparse
from itertools import combinations


def build_adjacency(n: int, mask: int) -> list[int]:
    adj = [0] * n
    edge_index = 0
    for u, v in combinations(range(n), 2):
        if mask & (1 << edge_index):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        edge_index += 1
    return adj


def vertices_from_csv(text: str) -> list[int]:
    return [int(part) for part in text.split(",") if part]


def role(adj: list[int], u: int, v: int, x: int) -> tuple[str, int]:
    ux = bool(adj[u] & (1 << x))
    vx = bool(adj[v] & (1 << x))
    if ux and not vx:
        return "X", 1
    if vx and not ux:
        return "Y", 1
    if ux and vx:
        return "Z", 2
    return "W", 0


def induced_degree(adj: list[int], vertex: int, mask: int) -> int:
    return (adj[vertex] & mask).bit_count()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--witness", required=True)
    parser.add_argument("--pair", required=True, help="u,v")
    args = parser.parse_args()

    adj = build_adjacency(args.n, args.mask)
    witness = vertices_from_csv(args.witness)
    pair = vertices_from_csv(args.pair)
    if len(pair) != 2:
        parser.error("--pair must be u,v")
    u, v = pair
    if u not in witness or v not in witness or u == v:
        parser.error("pair vertices must be distinct and lie in the witness")

    witness_set = set(witness)
    middle = sorted(witness_set - {u, v})
    witness_mask = sum(1 << x for x in witness)
    middle_mask = sum(1 << x for x in middle)
    roles: dict[str, list[int]] = {"X": [], "Y": [], "Z": [], "W": []}
    offsets: dict[int, int] = {}
    for x in middle:
        label, offset = role(adj, u, v, x)
        roles[label].append(x)
        offsets[x] = offset

    endpoint_degrees = [induced_degree(adj, u, witness_mask), induced_degree(adj, v, witness_mask)]
    middle_degrees = [induced_degree(adj, x, witness_mask) for x in middle]
    middle_degree_set = sorted(set(middle_degrees))
    common_middle_degree = middle_degree_set[0] if len(middle_degree_set) == 1 else None
    endpoint_defect = None
    if endpoint_degrees[0] == endpoint_degrees[1] and common_middle_degree is not None:
        endpoint_defect = endpoint_degrees[0] - common_middle_degree

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print("witness=" + ",".join(map(str, witness)))
    print(f"pair={u},{v}")
    print(f"pair_edge={bool(adj[u] & (1 << v))}")
    print("endpoint_degrees=" + ",".join(map(str, endpoint_degrees)))
    print("middle_degrees=" + ",".join(map(str, middle_degrees)))
    print(f"endpoint_minus_middle={endpoint_defect}")
    print(f"balanced_one_sided_roles={len(roles['X']) == len(roles['Y'])}")
    for label in ("X", "Y", "Z", "W"):
        print(f"{label}=" + ",".join(map(str, roles[label])))

    if common_middle_degree is None:
        print("defect_equations_ok=False")
        return

    equations = []
    ok = endpoint_degrees[0] == endpoint_degrees[1] and len(roles["X"]) == len(roles["Y"])
    for x in middle:
        internal = induced_degree(adj, x, middle_mask)
        total = internal + offsets[x]
        equations.append(f"{x}:{internal}+{offsets[x]}={total}")
        if total != common_middle_degree:
            ok = False
    print(f"middle_target_degree={common_middle_degree}")
    print("middle_profiles=" + ",".join(equations))
    print(f"defect_equations_ok={ok}")


if __name__ == "__main__":
    main()
