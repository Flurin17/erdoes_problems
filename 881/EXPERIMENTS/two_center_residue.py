#!/usr/bin/env python3
"""Verify residue-level multi-center pair-barrier obstructions.

The set S={0,1,2,4} in Z/7Z is a finite model for the remaining k=2
finitely-bad obstruction:

  * 2S is the whole group;
  * deleting any singleton leaves a 3-basis;
  * deleting {0,1} creates a 3-sum hole at residue 2;
  * the reflected cover uses two centers and cannot be reduced to one.

This is not an integer counterexample; thick residue lifts lose
single-integer privacy as explained by Lemma 6.1 in PROOF.md.

The script also checks the complete pair-barrier warning from Example 8.7b
and the Z/5Z finite-center incoherence example from Example 8.8 in
PROOF.md.
"""

from __future__ import annotations


def hsum(values: set[int], h: int, mod: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {(x + y) % mod for x in out for y in values}
    return out


def check_two_center_cover() -> None:
    mod = 7
    s_set = {0, 1, 2, 4}
    group = set(range(mod))
    print("S=", sorted(s_set), "mod", mod)
    print("2S whole group:", hsum(s_set, 2, mod) == group)
    print(
        "all singleton deletions are 3-bases:",
        all(hsum(s_set - {s}, 3, mod) == group for s in s_set),
    )
    pair = {0, 1}
    print("3(S\\{0,1})=", sorted(hsum(s_set - pair, 3, mod)))
    print("2 is pair-deletion hole:", 2 not in hsum(s_set - pair, 3, mod))

    two_center_cover = all(
        ((2 - e) % mod in s_set) or ((1 - e) % mod in s_set)
        for e in s_set
    )
    print("two-center reflected cover:", two_center_cover)

    one_centers = [
        c
        for c in group
        if all((c - e) % mod in s_set for e in s_set)
    ]
    print("one reflected centers:", one_centers)


def check_finite_center_incoherence() -> None:
    mod = 5
    s_set = {0, 1, 2, 3}
    deleted = {0, 3}
    retained = s_set - deleted
    group = set(range(mod))

    print("T=", sorted(s_set), "mod", mod)
    print("2T whole group:", hsum(s_set, 2, mod) == group)
    print(
        "singleton deletions are 3-bases:",
        hsum(s_set - {0}, 3, mod) == group
        and hsum(s_set - {3}, 3, mod) == group,
    )
    print("3C=", sorted(hsum(retained, 3, mod)))
    print("2 is pair-deletion hole:", 2 not in hsum(retained, 3, mod))

    two_retained = hsum(retained, 2, mod)
    three_retained = hsum(retained, 3, mod)
    pattern_repairs = {
        "0+2 in 2C": (0 + 2) % mod in two_retained,
        "3+1 in 2C": (3 + 1) % mod in two_retained,
        "0+0+1 in 3C": (0 + 0 + 1) % mod in three_retained,
        "0+3+1 in 3C": (0 + 3 + 1) % mod in three_retained,
        "0+3+2 in 3C": (0 + 3 + 2) % mod in three_retained,
        "3+3+2 in 3C": (3 + 3 + 2) % mod in three_retained,
    }
    print("pattern repairs:", pattern_repairs)
    for center in sorted(retained):
        singleton_ok = all((d + center) % mod in two_retained for d in deleted)
        pair_ok = all(
            (a + b + center) % mod in three_retained
            for a in deleted
            for b in deleted
        )
        print(
            f"single center {center} works:",
            singleton_ok and pair_ok,
        )


def check_complete_pair_barrier() -> None:
    mod = 5
    s_set = {0, 1, 2, 3}
    group = set(range(mod))
    bad_pairs: list[tuple[int, int, list[int]]] = []

    for x in sorted(s_set):
        for y in sorted(t for t in s_set if t > x):
            retained = s_set - {x, y}
            holes = sorted(group - hsum(retained, 3, mod))
            if holes:
                bad_pairs.append((x, y, holes))

    print("complete pair barrier S=", sorted(s_set), "mod", mod)
    print("2S whole group:", hsum(s_set, 2, mod) == group)
    print(
        "all singleton deletions are 3-bases:",
        all(hsum(s_set - {s}, 3, mod) == group for s in s_set),
    )
    print("bad pair holes:", bad_pairs)

    pair = {0, 1}
    hole = 0
    centers = [(hole - x) % mod for x in sorted(pair)]
    for center in centers:
        reflected = {(center - s) % mod for s in s_set}
        print(
            "center",
            center,
            "reflects all S:",
            reflected <= s_set,
            "reflected=",
            sorted(reflected),
        )
    print(
        "two centers cover S:",
        all(any((center - s) % mod in s_set for center in centers) for s in s_set),
    )


def main() -> None:
    check_two_center_cover()
    check_complete_pair_barrier()
    check_finite_center_incoherence()


if __name__ == "__main__":
    main()
