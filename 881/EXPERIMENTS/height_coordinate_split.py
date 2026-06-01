#!/usr/bin/env python3
"""Finite checks for the geometric-height coordinate split.

Corollary 16.128 uses only the inequality

    chi <= 7M

when q, b, m, S, and K are all at most M.  This script exhausts a small
integer box and samples weighted packet families to verify the corresponding
set inclusion behind the pigeonhole step.

It also checks the finite inequality behind Corollary 16.129: with rank and
linear-core density margin bounded, the pre-asymptotic constant K is bounded.
Finally, it checks the finite decompositions behind Corollary 16.131:
bounded start and length bound the tested interval endpoint, while bounded
auxiliary count and location bound the auxiliary endpoint sum.
"""

from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass(frozen=True)
class Label:
    q: int
    a: int
    b: int
    m: int
    s_aux: int
    k_const: int

    @property
    def n(self) -> int:
        return self.b - self.a + 1

    @property
    def chi(self) -> int:
        return self.q + self.a + self.b + self.n + self.m + self.s_aux + self.k_const


def labels(limit: int) -> list[Label]:
    out: list[Label] = []
    for q in range(1, limit + 1):
        for a in range(1, limit + 1):
            for b in range(a, limit + 1):
                for m in range(1, limit + 1):
                    for s_aux in range(m, 2 * limit + 1):
                        for k_const in range(0, limit + 1):
                            out.append(Label(q, a, b, m, s_aux, k_const))
    return out


def check_inclusion(limit: int = 7) -> int:
    checked = 0
    for label in labels(limit):
        for threshold in range(1, limit + 1):
            all_components_small = (
                label.q <= threshold
                and label.b <= threshold
                and label.m <= threshold
                and label.s_aux <= threshold
                and label.k_const <= threshold
            )
            if all_components_small:
                assert label.chi <= 7 * threshold, (label, threshold)
            if label.chi > 7 * threshold:
                assert not all_components_small, (label, threshold)
            checked += 1
    return checked


def check_weighted_packet_shadow(trials: int = 2000) -> int:
    rng = Random(16128)
    universe = labels(6)
    checked = 0
    for _ in range(trials):
        threshold = rng.randint(1, 6)
        packet_count = rng.randint(2, 8)
        left_mass = 0.0
        right_mass = 0.0
        for _packet in range(packet_count):
            packet_size = rng.randint(2, 12)
            active = [rng.choice(universe) for _ in range(rng.randint(0, packet_size))]
            left = [label for label in active if label.chi > 7 * threshold]
            right = [
                label
                for label in active
                if label.q > threshold
                or label.b > threshold
                or label.m > threshold
                or label.s_aux > threshold
                or label.k_const > threshold
            ]
            assert set(left).issubset(set(right))
            left_mass += len(left) / packet_size
            right_mass += len(right) / packet_size
        assert left_mass <= right_mass + 1e-12
        checked += 1
    return checked


def gamma(rank: int, margin_height: int) -> float:
    """Smallest gamma when ceil(1 / (2 delta - 1)) <= margin_height."""
    if rank == 1:
        return 1.0 / margin_height
    return 1.0 / (2 * margin_height)


def d_constant(rank: int) -> int:
    """Toy positive D(r) for the finite check."""
    return rank * rank + 3


def check_constant_margin_split(limit: int = 12) -> int:
    checked = 0
    for rank_bound in range(1, limit + 1):
        for margin_bound in range(1, limit + 1):
            d_star = max(d_constant(rank) for rank in range(1, rank_bound + 1))
            k_star = int(4 * margin_bound * d_star + 1)
            for rank in range(1, rank_bound + 1):
                for margin in range(1, margin_bound + 1):
                    k_const = int(2 * d_constant(rank) / gamma(rank, margin) + 1)
                    assert k_const <= k_star, (
                        rank_bound,
                        margin_bound,
                        rank,
                        margin,
                        k_const,
                        k_star,
                    )
                    checked += 1
    return checked


def check_height_decompositions(limit: int = 20) -> int:
    checked = 0
    for a_bound in range(1, limit + 1):
        for n_bound in range(1, limit + 1):
            for a_start in range(1, 2 * limit + 1):
                for n_len in range(1, 2 * limit + 1):
                    b_end = a_start + n_len - 1
                    if b_end > a_bound + n_bound - 1:
                        assert a_start > a_bound or n_len > n_bound
                    checked += 1
    for count_bound in range(1, limit + 1):
        for endpoint_bound in range(1, limit + 1):
            for count in range(1, 2 * limit + 1):
                for endpoint in range(1, 2 * limit + 1):
                    s_aux = 2 * count * endpoint
                    if s_aux > 2 * count_bound * endpoint_bound:
                        assert count > count_bound or endpoint > endpoint_bound
                    checked += 1
    return checked


def main() -> None:
    inclusion_checked = check_inclusion()
    packet_checked = check_weighted_packet_shadow()
    constant_margin_checked = check_constant_margin_split()
    height_decomposition_checked = check_height_decompositions()
    print("height coordinate split checks passed")
    print(f"inclusion_checked={inclusion_checked}")
    print(f"packet_shadow_checked={packet_checked}")
    print(f"constant_margin_checked={constant_margin_checked}")
    print(f"height_decomposition_checked={height_decomposition_checked}")


if __name__ == "__main__":
    main()
