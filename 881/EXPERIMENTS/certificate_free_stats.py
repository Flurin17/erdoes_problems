#!/usr/bin/env python3
"""Certificate-free independence statistics for finite analogue sets.

For the k=2 fixed-triple criterion, a subset S of A is certificate-free if
there are no e,y1,y2 in S with y1,y2 != e and y1+y2-e in A. Lemma 8.6g in
PROOF.md says that fixed-rank large-excess barriers force a good deletion
unless every finite test set has a large certificate-free subset.
"""

from __future__ import annotations

from itertools import combinations


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


def max_certificate_free(ambient: set[int]) -> set[int]:
    best: set[int] = set()
    ordered = sorted(ambient)
    for size in range(len(ordered) + 1):
        for candidate in combinations(ordered, size):
            subset = set(candidate)
            if len(subset) > len(best) and is_certificate_free(subset, ambient):
                best = subset
    return best


def main() -> None:
    examples = [
        ("pair-window", {1, 2, 3, 6, 7, 8}),
        ("rank3-window", {1, 2, 3, 4, 5, 6, 8, 9}),
        ("rank4-window", {1, 2, 3, 4, 5, 6, 8, 9, 10, 11}),
        ("minimal-hole-toy", {1, 2, 3, 4, 5}),
    ]

    for name, ambient in examples:
        best = max_certificate_free(ambient)
        ratio = len(best) / len(ambient)
        gamma = len(ambient) / len(best) if best else float("inf")
        print(
            f"{name}: |A|={len(ambient)} "
            f"alpha_cert={len(best)} ratio={ratio:.3f} "
            f"gamma={gamma:.3f} "
            f"example={sorted(best)}"
        )


if __name__ == "__main__":
    main()
