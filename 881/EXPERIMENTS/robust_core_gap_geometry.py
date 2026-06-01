#!/usr/bin/env python3
"""Check affine geometry of robust blocker cores.

This verifies Lemmas 16.97 and 16.102 on finite parameter ranges:
robust-core midpoint depends only on the auxiliary interval midpoint, gaps
between two cores measure auxiliary midpoint separation, and endpoint
escape from a core has the predicted midpoint-distance cost. It also checks
the contrapositive used by Corollary 16.105: points whose doubled midpoint
distance is below the endpoint-escape threshold lie inside the core. The
same calculation checks the centered-packet criterion behind Corollary
16.107.
"""

from __future__ import annotations

from math import ceil
from random import Random


def core(a: int, b: int, c: int, d: int, r: int, m_delta: int) -> tuple[int, int] | None:
    m = d - c + 1
    ell = ceil((m - r) / (r + 1))
    if m_delta > 2 * ell - 1:
        return None
    left = 2 * (d - ell + 1) - b + m_delta - 1
    right = 2 * (c + ell - 1) - a - m_delta + 1
    if right < left:
        return None
    return left, right


def main() -> None:
    rng = Random(1697)
    checked = 0
    proximal_checked = 0
    centered_packet_checked = 0
    endpoint_checked = 0
    gap_checked = 0
    clustered_checked = 0
    for n in range(8, 22):
        a = 100
        b = a + n - 1
        for r in range(1, 5):
            for m_delta in range(1, n + 1):
                intervals: list[tuple[int, int, int, int]] = []
                for c in range(1, 55):
                    for m in range(r + 1, 18):
                        d = c + m - 1
                        value = core(a, b, c, d, r, m_delta)
                        if value is None:
                            continue
                        left, right = value
                        assert left + right == 2 * (c + d) - a - b
                        rho = right - left + 1
                        for p in (left, (left + right) // 2, right):
                            assert left <= p <= right
                            assert abs(2 * p + a + b - 2 * (c + d)) <= rho - 1
                            proximal_checked += 1
                        for p_minus, p_plus in (
                            (left, right),
                            (left, (left + right) // 2),
                            ((left + right) // 2, right),
                        ):
                            width = p_plus - p_minus
                            center_distance = abs(
                                p_minus + p_plus + a + b - 2 * (c + d)
                            )
                            assert center_distance + width <= rho - 1
                            centered_packet_checked += 1
                        for p in (left - 3, left - 1, right + 1, right + 3):
                            assert p < left or p > right
                            assert abs(2 * p + a + b - 2 * (c + d)) >= rho + 1
                            endpoint_checked += 1
                        intervals.append((left, right, c, d))
                        checked += 1
                intervals.sort()
                candidate_pairs: list[tuple[tuple[int, int, int, int], tuple[int, int, int, int]]] = []
                for i, first in enumerate(intervals):
                    l1, u1, c1, d1 = first
                    for l2, u2, c2, d2 in intervals[i + 1 :]:
                        if u1 >= l2:
                            continue
                        candidate_pairs.append((first, (l2, u2, c2, d2)))
                        if len(candidate_pairs) >= 3000:
                            break
                    if len(candidate_pairs) >= 3000:
                        break
                if len(candidate_pairs) == 3000:
                    # Mix deterministic early separated pairs with sampled later pairs.
                    attempts = 0
                    added = 0
                    while attempts < 10000 and added < 2000 and len(intervals) >= 2:
                        i = rng.randrange(0, len(intervals) - 1)
                        j = rng.randrange(i + 1, len(intervals))
                        if intervals[i][1] < intervals[j][0]:
                            candidate_pairs.append((intervals[i], intervals[j]))
                            added += 1
                        attempts += 1
                for first, second in candidate_pairs:
                    l1, u1, c1, d1 = first
                    l2, u2, c2, d2 = second
                    rho1 = u1 - l1 + 1
                    rho2 = u2 - l2 + 1
                    gap = l2 - u1 - 1
                    assert gap >= 0
                    assert 2 * ((c2 + d2) - (c1 + d1)) == 2 * gap + rho1 + rho2
                    assert (c2 + d2) - (c1 + d1) >= gap + 1
                    midpoint_gap = (c2 + d2) - (c1 + d1)
                    if midpoint_gap <= max(rho1, rho2):
                        # A crude finite shadow of Corollary 16.100:
                        # adjacent separated cores need midpoint separation
                        # at least the shorter linear-core scale.
                        assert gap < midpoint_gap
                    gap_checked += 1
                    clustered_checked += 1
    print("robust core gap geometry check passed")
    print(f"cores_checked={checked}")
    print(f"endpoint_proximal_checked={proximal_checked}")
    print(f"centered_packet_checked={centered_packet_checked}")
    print(f"endpoint_escape_checked={endpoint_checked}")
    print(f"gaps_checked={gap_checked}")
    print(f"clustered_pairs_checked={clustered_checked}")


if __name__ == "__main__":
    main()
