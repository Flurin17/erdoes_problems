#!/usr/bin/env python3
"""Search finite windows for mobile-injective private-color patterns.

The remaining obstruction in PROOF.md is not just a large finite barrier,
but a large active trace whose private-color incidence can assign many
protected rows to distinct moving deleted colors. This script searches for
small finite analogues of that incidence.

For a finite set S, deletion F, retained set C=S\\F, and witness w, it
requires:

* w is a 3-sum hole of C;
* F is inclusion-minimal for that hole;
* rows e in C with w-e covered by 2S have private colors f in F satisfying
  w-e-f in C and e+f notin 2C.

It reports examples with large matchings in the row/color graph. This is a
diagnostic only; it is not an asymptotic construction.
"""

from __future__ import annotations

from itertools import combinations


def sums_k(values: tuple[int, ...], k: int, cap: int | None = None) -> set[int]:
    if k == 0:
        return {0}
    previous = sums_k(values, k - 1, cap)
    out: set[int] = set()
    for total in previous:
        for value in values:
            new_total = total + value
            if cap is None or new_total <= cap:
                out.add(new_total)
    return out


def is_interval_covered(two_sums: set[int], start: int, end: int) -> bool:
    return all(n in two_sums for n in range(start, end + 1))


def minimal_hole(S: tuple[int, ...], F: tuple[int, ...], w: int, three_C: set[int]) -> bool:
    if w in three_C:
        return False
    F_set = set(F)
    for f in F:
        retained = tuple(sorted(set(S) - (F_set - {f})))
        if w not in sums_k(retained, 3, w):
            return False
    return True


def private_color_graph(
    S: tuple[int, ...],
    F: tuple[int, ...],
    w: int,
    two_S: set[int],
    two_C: set[int],
) -> dict[int, set[int]]:
    F_set = set(F)
    C = tuple(x for x in S if x not in F_set)
    C_set = set(C)
    deleted_pair_sums = {a + b for a in F for b in F}
    graph: dict[int, set[int]] = {}
    for e in C:
        if w - e not in two_S or w - e in deleted_pair_sums:
            continue
        colors = {
            f
            for f in F
            if (w - e - f) in C_set and (e + f) not in two_C
        }
        if colors:
            graph[e] = colors
    return graph


def max_bipartite_matching(graph: dict[int, set[int]]) -> tuple[int, dict[int, int]]:
    match_color_to_row: dict[int, int] = {}

    def augment(row: int, seen: set[int]) -> bool:
        for color in sorted(graph[row]):
            if color in seen:
                continue
            seen.add(color)
            if color not in match_color_to_row or augment(match_color_to_row[color], seen):
                match_color_to_row[color] = row
                return True
        return False

    for row in sorted(graph, key=lambda r: len(graph[r])):
        augment(row, set())
    row_to_color = {row: color for color, row in match_color_to_row.items()}
    return len(row_to_color), row_to_color


def verify_range_packet(test: tuple[int, ...]) -> dict[str, object]:
    """Check the range-separated packet from Warning 8.5a.7c."""

    m = len(test)
    big_n = 4 * (max(test) + m) + 1
    w = 10 * big_n
    colors = tuple(big_n + i for i in range(1, m + 1))
    mirrors = tuple(9 * big_n - t - i for i, t in enumerate(test, start=1))
    C = tuple(sorted(test + mirrors))
    S = tuple(sorted(C + colors))
    two_C = sums_k(C, 2, 3 * w)
    three_C = sums_k(C, 3, w)
    fibers = {
        colors[i]: (test[i], mirrors[i])
        for i in range(m)
    }

    private_rows = []
    for i, color in enumerate(colors):
        t = test[i]
        q = mirrors[i]
        private_rows.append(
            (
                t,
                color,
                w - t - color,
                (t + color) not in two_C,
            )
        )
        private_rows.append(
            (
                q,
                color,
                w - q - color,
                (q + color) not in two_C,
            )
        )

    fiber_cert_free = True
    S_set = set(S)
    for t, q in fibers.values():
        if 2 * q - t in S_set or 2 * t - q in S_set:
            fiber_cert_free = False

    return {
        "test": test,
        "N": big_n,
        "w": w,
        "colors": colors,
        "mirrors": mirrors,
        "w_notin_3C": w not in three_C,
        "private_rows": private_rows,
        "fiber_cert_free": fiber_cert_free,
    }


def search(max_value: int, max_size: int, min_match: int, limit: int) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    universe = tuple(range(1, max_value + 1))
    for size in range(5, max_size + 1):
        for S in combinations(universe, size):
            two_S = sums_k(S, 2, 3 * max_value)
            if not is_interval_covered(two_S, 2 * min(S), max(S)):
                continue
            for rank in range(2, min(size, max_size // 2 + 2) + 1):
                for F in combinations(S, rank):
                    C = tuple(x for x in S if x not in set(F))
                    if len(C) < rank:
                        continue
                    two_C = sums_k(C, 2, 3 * max_value)
                    three_C = sums_k(C, 3, 3 * max_value)
                    for w in range(max(F) - 1, min(3 * max_value, 3 * max(S)) + 1):
                        if not minimal_hole(S, F, w, three_C):
                            continue
                        graph = private_color_graph(S, F, w, two_S, two_C)
                        matching_size, matching = max_bipartite_matching(graph)
                        if matching_size >= min_match:
                            results.append(
                                {
                                    "S": S,
                                    "F": F,
                                    "w": w,
                                    "rank": rank,
                                    "rows": sorted(graph),
                                    "matching_size": matching_size,
                                    "matching": dict(sorted(matching.items())),
                                }
                            )
                            if len(results) >= limit:
                                return results
    return results


def main() -> None:
    results = search(max_value=14, max_size=9, min_match=3, limit=8)
    print("mobile-injective private-color search")
    print("parameters: max_value=14 max_size=9 min_match=3")
    if not results:
        print("no examples found")
        return
    for idx, result in enumerate(results, start=1):
        print()
        print("example", idx)
        for key, value in result.items():
            print(f"{key}={value}")

    packet = verify_range_packet((2, 5, 9))
    print()
    print("range-separated packet check")
    for key, value in packet.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
