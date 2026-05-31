#!/usr/bin/env python3
"""Verify the certificate propagation in Theorem 2.3 on A=N.

Theorem 2.3 is an abstract construction. This script instantiates it in the
maximally recurrent model A=N, builds a few deleted elements and protected
certificate entries, then checks that every deleted multiset of size <= k
has the repair required by Lemma 2.2.

This is a sanity check for the algebra/indexing, not a proof of the theorem.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations_with_replacement


def multiset_sum(values: tuple[int, ...]) -> int:
    return sum(values)


def build_empty_certificates(k: int, e: int) -> dict[tuple[tuple[int, ...], int], tuple[tuple[int, ...], tuple[int, ...]]]:
    """Return certificates keyed by (deleted multiset S, d).

    Each value is (Y, X), where
      sum(S)+sum(Y) = (d-1)e + sum(X).
    """
    certs: dict[tuple[tuple[int, ...], int], tuple[tuple[int, ...], tuple[int, ...]]] = {}
    y_values = [2]
    x = 2
    certs[((), 1)] = ((2,), (2,))
    next_center = 10
    for d in range(1, k):
        m = next_center
        next_center += 10
        x_next = m - e
        y_next = m - x
        y_values.append(y_next)
        x = x_next
        certs[((), d + 1)] = (tuple(y_values), (x,))
    return certs


def verify_certificate(
    certs: dict[tuple[tuple[int, ...], int], tuple[tuple[int, ...], tuple[int, ...]]],
    key: tuple[tuple[int, ...], int],
    e: int,
) -> bool:
    deleted, d = key
    y_tuple, x_tuple = certs[key]
    return sum(deleted) + sum(y_tuple) == (d - 1) * e + sum(x_tuple)


def protected_sum_contains(protected: set[int], target: int, length: int) -> bool:
    for combo in combinations_with_replacement(sorted(protected), length):
        if sum(combo) == target:
            return True
    return False


def main() -> None:
    k = 4
    steps = 4
    e = 1
    certs = build_empty_certificates(k, e)
    protected = {e}
    for _, x_tuple in certs.values():
        protected.update(x_tuple)
    deleted: list[int] = []

    for step in range(steps):
        y_entries = {
            y
            for y_tuple, _ in certs.values()
            for y in y_tuple
        }
        m = 100 * (step + 1)
        while m - e in protected or m - e in deleted:
            m += 1
        b = m - e
        deleted.append(b)

        for y in y_entries:
            if y != e:
                protected.add(m - y)

        old_certs = dict(certs)
        old_deleted_multisets = sorted({key[0] for key in old_certs})
        for old in old_deleted_multisets:
            q = len(old)
            for ell in range(1, k - q + 1):
                if (old, ell) not in old_certs:
                    continue
                y_tuple, x_tuple = old_certs[(old, ell)]
                repair_terms = tuple(m - y for y in y_tuple) + x_tuple
                target = e + sum(old) + ell * b
                assert sum(repair_terms) == target
                assert all(term in protected for term in repair_terms)

                new_deleted = tuple(sorted(old + (b,) * ell))
                if len(new_deleted) < k:
                    for d in range(1, k - len(new_deleted) + 1):
                        source_key = (old, ell + d)
                        if source_key not in old_certs:
                            continue
                        source_y, source_x = old_certs[source_key]
                        new_y = source_y[:d]
                        new_x = source_x + tuple(m - y for y in source_y[d : d + ell])
                        certs[(new_deleted, d)] = (new_y, new_x)
                        protected.update(new_x)

        for key in certs:
            assert verify_certificate(certs, key, e), key

    for r in range(1, k + 1):
        for combo in combinations_with_replacement(deleted, r):
            target = e + sum(combo)
            assert protected_sum_contains(protected, target, r + 1), (combo, target)

    print(
        f"verified k={k} steps={steps} deleted={deleted} "
        f"certificates={len(certs)} protected={len(protected)}"
    )


if __name__ == "__main__":
    main()
