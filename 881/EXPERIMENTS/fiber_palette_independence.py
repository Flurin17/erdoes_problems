#!/usr/bin/env python3
"""Finite checks for unique-gate and shifted-fiber independence.

These are small diagnostics for Lemmas 8.5a.7i--8.5a.7l in PROOF.md.
They do not search for infinite structure; they verify the finite graph
conditions forced by unique two-sum gates and retained shifted overlaps.
"""

from __future__ import annotations

from itertools import combinations


def three_sums(elements: set[int]) -> set[int]:
    ordered = sorted(elements)
    sums: set[int] = set()
    for i, a in enumerate(ordered):
        for j, b in enumerate(ordered[i:], start=i):
            for c in ordered[j:]:
                sums.add(a + b + c)
    return sums


def two_sums(elements: set[int]) -> set[int]:
    ordered = sorted(elements)
    return {a + b for i, a in enumerate(ordered) for b in ordered[i:]}


def rep_count(ambient: set[int], target: int) -> int:
    ordered = sorted(ambient)
    return sum(
        1
        for i, a in enumerate(ordered)
        for b in ordered[i:]
        if a + b == target
    )


def is_certificate_free(subset: set[int], ambient: set[int]) -> bool:
    for e in subset:
        for y1 in subset:
            if y1 == e:
                continue
            for y2 in subset:
                if y2 == e:
                    continue
                if y1 + y2 - e in ambient:
                    return False
    return True


def gate_independent(subset: set[int], ambient: set[int], gate: int) -> bool:
    for u in subset:
        for v in subset:
            if u == v:
                continue
            if u + gate - v in ambient:
                return False
    return True


def shift_independent(subset: set[int], shift: int) -> bool:
    return all(u + shift not in subset for u in subset)


def all_subsets(elements: set[int]):
    ordered = sorted(elements)
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            yield set(combo)


def max_gate_free(elements: set[int], ambient: set[int], gate: int) -> int:
    return max(
        len(subset)
        for subset in all_subsets(elements)
        if is_certificate_free(subset, ambient)
        and gate_independent(subset, ambient, gate)
    )


def max_shift_free(elements: set[int], ambient: set[int], shift: int) -> int:
    return max(
        len(subset)
        for subset in all_subsets(elements)
        if is_certificate_free(subset, ambient)
        and shift_independent(subset, shift)
        and all(u + shift in ambient for u in subset)
    )


def moving_unique_gate_packet() -> dict[str, object]:
    test = (1, 2, 4, 8, 16)
    n = 260
    w = 10 * n
    f = n
    g = 2 * n
    t = 3 * n
    q_g = 5 * n
    mirrors = {u: 9 * n - u for u in test}
    deleted = {f, g}
    retained = set(test) | set(mirrors.values()) | {t, q_g}
    ambient = retained | deleted
    private_rows = [
        (u, mirrors[u], mirrors[u] in retained, u + f not in two_sums(retained))
        for u in test
    ]
    unique_rows = [(u, rep_count(ambient, u + f)) for u in test]
    return {
        "U": test,
        "N": n,
        "w": w,
        "m": w - f,
        "F": tuple(sorted(deleted)),
        "w_notin_3C": w not in three_sums(retained),
        "repairs": {
            "restore_f": all(w == f + u + mirrors[u] for u in test),
            "restore_g": w == g + t + q_g,
        },
        "private_rows": private_rows,
        "unique_rows": unique_rows,
        "gate_independent": gate_independent(set(test), ambient, f),
        "certificate_free_U": is_certificate_free(set(test), ambient),
    }


def main() -> None:
    ambient = {8, 9, 11, 13, 15, 16}
    gate = 16
    reflected_center = 24
    rows = {s for s in ambient if s != gate and reflected_center - s in ambient}
    unique_rows = {s for s in rows if rep_count(ambient, s + gate) == 1}

    print("unique-gate window")
    print(f"ambient={tuple(sorted(ambient))}")
    print(f"gate={gate}")
    print(f"reflected_center={reflected_center}")
    print(f"rows={tuple(sorted(rows))}")
    print(f"unique_rows={tuple(sorted(unique_rows))}")
    print(f"gate_independent={gate_independent(unique_rows, ambient, gate)}")
    print(f"max_gate_certificate_free={max_gate_free(rows, ambient, gate)}")

    shifted_ambient = {1, 2, 3, 10}
    shift = 1
    shifted_rows = {1, 2}
    print()
    print("shifted-overlap window")
    print(f"ambient={tuple(sorted(shifted_ambient))}")
    print(f"shift={shift}")
    print(f"rows={tuple(sorted(shifted_rows))}")
    print(
        "rows_plus_shift_in_ambient="
        f"{all(u + shift in shifted_ambient for u in shifted_rows)}"
    )
    print(f"shift_independent={shift_independent(shifted_rows, shift)}")
    print(f"certificate_free={is_certificate_free(shifted_rows, shifted_ambient)}")
    print(f"max_shift_certificate_free={max_shift_free(shifted_rows, shifted_ambient, shift)}")

    packet = moving_unique_gate_packet()
    print()
    print("moving unique-gate packet check")
    for key, value in packet.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
