#!/usr/bin/env python3
"""Finite diagnostics for Lemma 8.4c and Corollaries 3.4h/3.4s.

For a finite window S, deleted set F, and hole w, print the retained
padders e for which w-e is in the covered two-sum range and the deleted
elements f such that e+f is private relative to C=S\\F.  Also print the
star-gate repair rows, their full two-sum counts r2(row+d), and whether
they are unique for the gate or overlap through another deleted element.
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


def rep_count(s: set[int], target: int) -> int:
    count = 0
    for a in sorted(s):
        b = target - a
        if b < a or b not in s:
            continue
        count += 1
    return count


def row_branch(s: set[int], f_set: set[int], d: int, row: int) -> str:
    target = row + d
    overlaps = [
        f
        for f in sorted(f_set - {d})
        if target - f in s
    ]
    count = rep_count(s, target)
    if count == 1:
        return "unique"
    if overlaps:
        return "overlap:" + ",".join(str(f) for f in overlaps)
    return "other"


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
    print("star gates d : retained repairs w-d=a+b ; rows row(r2,branch)")
    for d in sorted(f_set):
        repairs: list[tuple[int, int]] = []
        bounded_rows: dict[int, int] = {}
        for a in sorted(c):
            b = w - d - a
            if b < a or b not in c:
                continue
            repairs.append((a, b))
            for row in {a, b}:
                if row + d not in two_c:
                    bounded_rows[row] = rep_count(s, row + d)
        rows = [
            f"{row}({bounded_rows[row]},{row_branch(s, f_set, d, row)})"
            for row in sorted(bounded_rows)
        ]
        print(f"{d:>3}: repairs={repairs} rows={rows}")
        unique = [row for row in bounded_rows if row_branch(s, f_set, d, row) == "unique"]
        overlap_summary = {
            f: sorted(row for row in bounded_rows if row + d - f in s)
            for f in sorted(f_set - {d})
        }
        overlap_summary = {f: rows for f, rows in overlap_summary.items() if rows}
        print(f"     branch unique={sorted(unique)} overlaps={overlap_summary}")


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
