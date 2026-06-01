#!/usr/bin/env python3
"""Search the balanced pair-difference extension from Lemma 27A."""

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


def mask_from_vertices(vertices: list[int]) -> int:
    out = 0
    for vertex in vertices:
        out |= 1 << vertex
    return out


def masks_of_size(vertices: list[int], size: int) -> list[int]:
    return [mask_from_vertices(list(choice)) for choice in combinations(vertices, size)]


def is_regular_with_degree(adj: list[int], subset: int, degree: int) -> bool:
    remaining = subset
    while remaining:
        bit = remaining & -remaining
        vertex = bit.bit_length() - 1
        if (adj[vertex] & subset).bit_count() != degree:
            return False
        remaining ^= bit
    return True


def edge_exists(adj: list[int], u: int, v: int) -> bool:
    return bool(adj[u] & (1 << v))


def vertices(mask: int) -> list[int]:
    out: list[int] = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def pair_candidates(n: int, pair_text: str | None) -> list[tuple[int, int]]:
    if pair_text is None:
        return list(combinations(range(n), 2))
    parts = [int(part) for part in pair_text.split(",")]
    if len(parts) != 2 or parts[0] == parts[1]:
        raise ValueError("--pair must have the form u,v with u != v")
    u, v = sorted(parts)
    if not (0 <= u < n and 0 <= v < n):
        raise ValueError("--pair vertices out of range")
    return [(u, v)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--pair", help="optional pair u,v to inspect")
    parser.add_argument("--min-r", type=int, default=1)
    args = parser.parse_args()

    adj = build_adjacency(args.n, args.mask)
    best: tuple[int, int, int, int, int, int, int] | None = None

    for u, v in pair_candidates(args.n, args.pair):
        u_bit = 1 << u
        v_bit = 1 << v
        delta = 1 if edge_exists(adj, u, v) else 0
        a_vertices = [
            w
            for w in range(args.n)
            if w not in (u, v) and (adj[u] & (1 << w)) and not (adj[v] & (1 << w))
        ]
        b_vertices = [
            w
            for w in range(args.n)
            if w not in (u, v) and (adj[v] & (1 << w)) and not (adj[u] & (1 << w))
        ]
        max_r = min(len(a_vertices), len(b_vertices))
        for r in range(max_r, args.min_r - 1, -1):
            target = r - 1 + delta
            if target < 0:
                continue
            a_masks = masks_of_size(a_vertices, r)
            b_masks = masks_of_size(b_vertices, r)
            found = False
            for x_mask in a_masks:
                for y_mask in b_masks:
                    middle = x_mask | y_mask
                    if is_regular_with_degree(adj, middle, target):
                        extension = middle | u_bit | v_bit
                        degree = r + delta
                        if not is_regular_with_degree(adj, extension, degree):
                            raise AssertionError("extension failed verification")
                        order = 2 * r + 2
                        candidate = (order, r, degree, u, v, x_mask, y_mask)
                        if best is None or candidate > best:
                            best = candidate
                        found = True
                        break
                if found:
                    break
            if found:
                break

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    if args.pair:
        print(f"pair_filter={args.pair}")
    if best is None:
        print("best_extension_order=0")
        return

    order, r, degree, u, v, x_mask, y_mask = best
    delta = 1 if edge_exists(adj, u, v) else 0
    middle_degree = r - 1 + delta
    print(f"best_extension_order={order}")
    print(f"pair={u},{v}")
    print(f"pair_edge={bool(delta)}")
    print(f"balanced_side_size={r}")
    print(f"middle_regular_degree={middle_degree}")
    print(f"extension_regular_degree={degree}")
    print("X=" + ",".join(map(str, vertices(x_mask))))
    print("Y=" + ",".join(map(str, vertices(y_mask))))
    print("extension=" + ",".join(map(str, vertices(x_mask | y_mask | (1 << u) | (1 << v)))))


if __name__ == "__main__":
    main()
