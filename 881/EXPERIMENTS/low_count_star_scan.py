#!/usr/bin/env python3
"""Scan finite windows for reflected low-count stars.

For a finite set S, protected core E, and count bound Q, this checks triples
(w,d,a) with d,a,w-d-a in S\\E and r2_S(a+d) <= Q.  It is a toy diagnostic
for Corollary 3.4n, not a proof of any infinite statement.
"""

from __future__ import annotations


def rep_count(s: set[int], target: int) -> int:
    count = 0
    for a in s:
        b = target - a
        if b < a or b not in s:
            continue
        count += 1
    return count


def best_stars(
    name: str,
    s_list: list[int],
    protected: list[int],
    q: int,
    w_max: int,
    limit: int = 8,
) -> None:
    s = set(s_list)
    e = set(protected)
    c = s - e
    rows: list[tuple[int, int, int, list[int]]] = []
    for w in range(1, w_max + 1):
        for d in sorted(c):
            witnesses: list[int] = []
            for a in sorted(c):
                b = w - d - a
                if b in c and rep_count(s, a + d) <= q:
                    witnesses.append(a)
            if witnesses:
                rows.append((len(witnesses), w, d, witnesses))
    rows.sort(reverse=True)
    print(f"\n{name}: Q={q} protected={sorted(e)}")
    if not rows:
        print("  none")
        return
    for count, w, d, witnesses in rows[:limit]:
        print(f"  count={count:>2} w={w:>3} d={d:>3} rows={witnesses}")


def main() -> None:
    even_pin = [1] + list(range(2, 42, 2))
    best_stars("{1} plus evens, pin unprotected", even_pin, [], 1, 45)
    best_stars("{1} plus evens, pin protected", even_pin, [1], 1, 45)
    best_stars(
        "Schreier P6 pair-edge escape",
        [1, 2, 4, 5, 8, 10, 15, 18, 19, 30, 38, 40, 43, 44],
        [],
        2,
        70,
    )
    best_stars(
        "Schreier P6 pair-edge escape, old core protected",
        [1, 2, 4, 5, 8, 10, 15, 18, 19, 30, 38, 40, 43, 44],
        [1, 2, 4, 5, 8, 10, 15, 18, 19, 30],
        2,
        70,
    )


if __name__ == "__main__":
    main()
