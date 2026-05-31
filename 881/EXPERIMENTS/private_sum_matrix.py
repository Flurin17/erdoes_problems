#!/usr/bin/env python3
"""Finite diagnostics for Lemma 8.4c.

For a finite window S, deleted set F, and hole w, print the retained
padders e for which w-e is in the covered two-sum range and the deleted
elements f such that e+f is private relative to C=S\\F.
"""

from __future__ import annotations


def sums2(s: set[int]) -> set[int]:
    return {a + b for a in s for b in s}


def sums3(s: set[int]) -> set[int]:
    return {a + b + c for a in s for b in s for c in s}


def representation_edges(s: set[int], target: int, forbidden: int) -> list[frozenset[int]]:
    edges: list[frozenset[int]] = []
    for a in sorted(s):
        b = target - a
        if b < a or b not in s:
            continue
        edge = frozenset({a, b})
        if forbidden not in edge:
            edges.append(edge)
    return edges


def max_disjoint_reps(s: set[int], target: int, forbidden: int) -> int:
    edges = representation_edges(s, target, forbidden)

    def search(i: int, used: frozenset[int]) -> int:
        if i == len(edges):
            return 0
        best = search(i + 1, used)
        edge = edges[i]
        if used.isdisjoint(edge):
            best = max(best, 1 + search(i + 1, used | edge))
        return best

    return search(0, frozenset())


def analyze(name: str, s_list: list[int], f_list: list[int], w: int, threshold: int) -> None:
    s = set(s_list)
    f_set = set(f_list)
    c = s - f_set
    two_c = sums2(c)
    print(f"\n{name}")
    print(f"S={sorted(s)}")
    print(f"F={sorted(f_set)} C={sorted(c)} w={w} threshold={threshold}")
    print(f"w in 3C? {w in sums3(c)}")
    print("e : w-e status ; exact colors f(nu_f(e+f))")
    for e in sorted(c):
        if w - e < threshold:
            continue
        status = []
        if w - e in two_c:
            status.append("BAD:w-e in 2C")
        if w - e in sums2(f_set):
            status.append("w-e in F+F")
        private = [
            f"{f}({max_disjoint_reps(s, e + f, f)})"
            for f in sorted(f_set)
            if w - e - f in c and e + f not in two_c
        ]
        print(f"{e:>3}: {w-e:>3} {' '.join(status) or '-':<16} ; {private}")


def main() -> None:
    analyze(
        "Alternating-deletion collective hole",
        [1, 2, 3, 6, 7, 8],
        [6, 8],
        14,
        2,
    )
    analyze(
        "Schreier P6 pair-edge escape",
        [1, 2, 4, 5, 8, 10, 15, 18, 19, 30, 38, 40, 43, 44],
        [10, 38],
        58,
        2,
    )
    analyze(
        "First Schreier seed edge",
        [1, 2, 3, 4, 8],
        [1, 4],
        10,
        2,
    )


if __name__ == "__main__":
    main()
