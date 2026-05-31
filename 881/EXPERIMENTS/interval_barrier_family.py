#!/usr/bin/env python3
"""Probe how many barriers one interval block can support.

This diagnostic is for Proposition 10.3g in PROOF.md.  The proposition
builds

    I = [X + 1, X + M],  J = [X + 2M, X + 3M - 1],  S = I union J

and deletes the lower half of J to create an inclusion-minimal three-sum
hole with an actual terminal S-gap.  This script enumerates other
subsets F of J and asks whether they have any witness w satisfying the
same local finite conditions:

* w is not in 3(S \\ F);
* w is repaired by restoring each single f in F;
* the terminal interval (w - min(F) - m0, w - threshold] has no S-points;
* optionally, 2S covers up to w - threshold.

The point is not to prove anything by search.  It is to find the finite
shape of possible block-level multi-edge barriers before trying to code
them into an infinite construction.
"""

from __future__ import annotations

import argparse
from itertools import combinations
from typing import Iterable


def interval(lo: int, hi: int) -> list[int]:
    return list(range(lo, hi + 1))


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def reps_with_count(
    elements: set[int], target: int, marked: int
) -> set[tuple[int, tuple[int, ...]]]:
    """Return compressed three-term representations of target.

    Each item is (count_of_marked, other_terms).  Terms are nondecreasing;
    repetitions are allowed, as usual for additive bases.
    """

    ordered = sorted(elements)
    out: set[tuple[int, tuple[int, ...]]] = set()
    for a in ordered:
        for b in ordered:
            if b < a:
                continue
            c = target - a - b
            if c < b or c not in elements:
                continue
            terms = (a, b, c)
            count = terms.count(marked)
            if count:
                out.add((count, tuple(t for t in terms if t != marked)))
    return out


def cover_end(elements: set[int], start: int, cap: int) -> int:
    sums = hsum(elements, 2, cap)
    x = start
    while x <= cap and x in sums:
        x += 1
    return x - 1


def minimal_hole(elements: set[int], deletion: tuple[int, ...], witness: int) -> bool:
    removed = set(deletion)
    if witness in hsum(elements - removed, 3, witness):
        return False
    return all(
        witness in hsum(elements - (removed - {f}), 3, witness)
        for f in removed
    )


def terminal_gap(
    elements: set[int],
    deletion: tuple[int, ...],
    witness: int,
    m0: int,
    threshold: int,
    min_gap: int,
) -> tuple[bool, tuple[int, int]]:
    left = witness - min(deletion) - m0
    right = witness - threshold
    if right - left < min_gap:
        return False, (left, right)
    return not any(left < x <= right for x in elements), (left, right)


def is_interval(values: Iterable[int]) -> bool:
    vals = sorted(values)
    return vals == list(range(vals[0], vals[-1] + 1))


def classified_coordinate_deletions(
    x_value: int, m_value: int
) -> set[tuple[int, tuple[int, ...]]]:
    """Predicted covered terminal-gap barriers from Lemma 10.3h.

    The returned pairs are (q, D), where the witness is
    w_q = 3X + 5M + q and D is a tuple of high-block coordinates.
    """

    out: set[tuple[int, tuple[int, ...]]] = set()
    for q in range(-x_value, m_value - x_value + 1):
        if q <= 0:
            prefix_end = (m_value + q - 1) // 2
            deletion = set(range(0, prefix_end + 1))
            deletion.update(range(m_value + q, m_value))
            out.add((q, tuple(sorted(deletion))))
            continue

        suffix = tuple(range((q + 1) // 2, m_value))
        out.add((q, suffix))

        if q <= m_value - 2:
            prefix = tuple(range(0, (m_value + q - 1) // 2 + 1))
            out.add((q, prefix))
    return out


def verify_classification(
    x_value: int,
    m_value: int,
    elements: set[int],
    high: list[int],
    coverage: int,
    m0: int,
    threshold: int,
) -> None:
    actual: set[tuple[int, tuple[int, ...]]] = set()
    coord_by_value = {value: idx for idx, value in enumerate(high)}

    for rank in range(1, len(high) + 1):
        for deletion in combinations(high, rank):
            for q in range(-x_value, m_value - x_value + 1):
                witness = 3 * x_value + 5 * m_value + q
                if witness - threshold > coverage:
                    continue
                if not minimal_hole(elements, deletion, witness):
                    continue
                ok_gap, _ = terminal_gap(
                    elements,
                    deletion,
                    witness,
                    m0,
                    threshold,
                    min_gap=1,
                )
                if ok_gap:
                    coords = tuple(coord_by_value[value] for value in deletion)
                    actual.add((q, coords))

    expected = classified_coordinate_deletions(x_value, m_value)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        print(f"classification mismatch for X={x_value} M={m_value}")
        if missing:
            print("missing:")
            for item in missing[:20]:
                print("  ", item)
        if extra:
            print("extra:")
            for item in extra[:20]:
                print("  ", item)
        raise SystemExit(1)

    print(
        f"classification verified for X={x_value} M={m_value}: "
        f"{len(actual)} covered terminal-gap patterns"
    )


def max_clique(vertices: list[int], edges: set[tuple[int, int]]) -> tuple[int, tuple[int, ...]]:
    best: tuple[int, ...] = ()
    n = len(vertices)
    edge_set = {tuple(sorted(edge)) for edge in edges}
    for size in range(1, n + 1):
        found: tuple[int, ...] | None = None
        for combo in combinations(vertices, size):
            if all(tuple(sorted((a, b))) in edge_set for a, b in combinations(combo, 2)):
                found = combo
        if found is not None:
            best = found
    return len(best), best


def describe_repairs(
    elements: set[int], deletion: tuple[int, ...], witness: int
) -> dict[int, list[str]]:
    removed = set(deletion)
    out: dict[int, list[str]] = {}
    for f in deletion:
        repaired = elements - (removed - {f})
        descriptions: list[str] = []
        for count, others in sorted(reps_with_count(repaired, witness, f)):
            descriptions.append(f"{count}*{f}+{others}")
        out[f] = descriptions
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--X", type=int, default=3)
    parser.add_argument("--M", type=int, default=8)
    parser.add_argument("--max-rank", type=int, default=4)
    parser.add_argument("--m0", type=int, default=1)
    parser.add_argument("--threshold", type=int, default=2)
    parser.add_argument("--min-gap", type=int, default=1)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument(
        "--witness-cap",
        type=int,
        default=None,
        help="largest witness to inspect; defaults to coverage+threshold",
    )
    parser.add_argument(
        "--no-coverage",
        action="store_true",
        help="do not require the full 2S interval coverage up to w-threshold",
    )
    parser.add_argument(
        "--verify-classification",
        action="store_true",
        help="exhaustively verify the Lemma 10.3h classification for this X,M",
    )
    args = parser.parse_args()

    if args.M < args.X:
        raise SystemExit("this diagnostic follows Proposition 10.3g and needs M >= X")

    low = interval(args.X + 1, args.X + args.M)
    high = interval(args.X + 2 * args.M, args.X + 3 * args.M - 1)
    elements = set(low + high)
    start = 2 * (args.X + 1)
    cap = 3 * max(elements)
    coverage = cover_end(elements, start, cap)
    max_witness = args.witness_cap
    if max_witness is None:
        max_witness = coverage + args.threshold

    print(f"X={args.X} M={args.M}")
    print(f"I={low}")
    print(f"J={high}")
    print(f"2S coverage=({start}, {coverage})")
    print(f"search witnesses <= {max_witness}")

    if args.verify_classification:
        verify_classification(
            args.X,
            args.M,
            elements,
            high,
            coverage,
            args.m0,
            args.threshold,
        )
        return

    supported: dict[tuple[int, ...], list[tuple[int, tuple[int, int]]]] = {}
    samples: list[tuple[tuple[int, ...], int, tuple[int, int]]] = []

    max_rank = min(args.max_rank, len(high))
    for rank in range(1, max_rank + 1):
        for deletion in combinations(high, rank):
            for witness in range(max(deletion) + 1, max_witness + 1):
                if not args.no_coverage and witness - args.threshold > coverage:
                    continue
                if not minimal_hole(elements, deletion, witness):
                    continue
                ok_gap, gap = terminal_gap(
                    elements,
                    deletion,
                    witness,
                    args.m0,
                    args.threshold,
                    args.min_gap,
                )
                if not ok_gap:
                    continue
                supported.setdefault(deletion, []).append((witness, gap))
                if len(samples) < args.limit:
                    samples.append((deletion, witness, gap))

    for rank in range(1, max_rank + 1):
        deletions = [deletion for deletion in supported if len(deletion) == rank]
        intervals = [deletion for deletion in deletions if is_interval(deletion)]
        print(
            f"rank {rank}: {len(deletions)} supported deletions, "
            f"{len(intervals)} contiguous intervals"
        )

    lower_start = high[0]
    print("initial high-segment checks:")
    for r in range(0, min(max_rank, len(high))):
        deletion = tuple(range(lower_start, lower_start + r + 1))
        witnesses = supported.get(deletion, [])
        print(f"  {deletion}: {witnesses[:5]}")

    if max_rank >= 2:
        pair_edges = {
            tuple(sorted(deletion))
            for deletion in supported
            if len(deletion) == 2
        }
        clique_size, clique = max_clique(high, pair_edges)
        print(f"pair graph: {len(pair_edges)} supported edges")
        print(f"pair graph max clique: size {clique_size}, clique {clique}")
        missing_pair = next(
            (
                pair
                for pair in combinations(high, 2)
                if tuple(sorted(pair)) not in pair_edges
            ),
            None,
        )
        if missing_pair is not None:
            print(f"first unsupported pair: {missing_pair}")

    print("sample supported deletions:")
    for deletion, witness, gap in samples:
        print(f"  F={deletion} w={witness} gap={gap}")
        repairs = describe_repairs(elements, deletion, witness)
        for f, desc in repairs.items():
            preview = "; ".join(desc[:4])
            if len(desc) > 4:
                preview += "; ..."
            print(f"    repair {f}: {preview}")

    non_interval = [deletion for deletion in supported if len(deletion) >= 2 and not is_interval(deletion)]
    if non_interval:
        deletion = min(non_interval, key=lambda item: (len(item), item))
        print(f"first non-contiguous supported deletion: {deletion}, {supported[deletion][:5]}")
    else:
        print("no non-contiguous supported deletion found in searched ranks")


if __name__ == "__main__":
    main()
