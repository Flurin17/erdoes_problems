#!/usr/bin/env python3
"""Verify the binary Raikov-Stoehr deletion from Attempt 12.

Let A0 contain numbers whose binary support is in even positions and A1
contain numbers whose support is in odd positions. Delete the even-support
elements of A0. The proof in PROOF.md says the remaining set is an
asymptotic three-fold basis; this script checks the claim on a finite
initial interval.
"""

from __future__ import annotations


def support(n: int) -> list[int]:
    return [i for i in range(n.bit_length()) if (n >> i) & 1]


def in_a0(n: int) -> bool:
    return n > 0 and all(i % 2 == 0 for i in support(n))


def in_a1(n: int) -> bool:
    return n > 0 and all(i % 2 == 1 for i in support(n))


def retained(n: int) -> bool:
    if in_a1(n):
        return True
    if in_a0(n):
        return len(support(n)) % 2 == 1
    return False


def main(cap: int = 20_000) -> None:
    values = [n for n in range(1, cap + 1) if retained(n)]
    two_sums: set[int] = set()
    for i, a in enumerate(values):
        for b in values[i:]:
            total = a + b
            if total <= cap:
                two_sums.add(total)

    three_sums: set[int] = set()
    for total in two_sums:
        for c in values:
            value = total + c
            if value <= cap:
                three_sums.add(value)

    missing = [n for n in range(1, cap + 1) if n not in three_sums]
    print("binary digital retained set check")
    print("cap=", cap)
    print("missing=", missing)


if __name__ == "__main__":
    main()
