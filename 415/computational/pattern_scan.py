#!/usr/bin/env python3
"""Exact finite scan of strict ordering patterns of consecutive totients.

The permutation is the list of one-based positions in increasing totient order.
A window containing a tie realizes no permutation.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from pathlib import Path


def totient_sieve(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    if limit >= 1:
        phi[1] = 1
    for p in range(2, limit + 1):
        if phi[p] == p:
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def totient_naive(n: int) -> int:
    return sum(math.gcd(a, n) == 1 for a in range(1, n + 1))


def strict_pattern(values: list[int]) -> tuple[int, ...] | None:
    if len(set(values)) != len(values):
        return None
    return tuple(sorted(range(1, len(values) + 1), key=lambda i: values[i - 1]))


def natural_extensions(phi: list[int], k: int) -> list[tuple[int, ...]]:
    blocks: dict[int, list[int]] = {}
    for i in range(1, k + 1):
        blocks.setdefault(phi[i], []).append(i)
    ordered_blocks = [blocks[v] for v in sorted(blocks)]
    extensions: list[tuple[int, ...]] = []
    for choices in itertools.product(*(itertools.permutations(b) for b in ordered_blocks)):
        extensions.append(tuple(i for block in choices for i in block))
    return extensions


def scan(
    phi: list[int],
    limit: int,
    k: int,
    include_counts: bool,
    include_pattern_lists: bool,
) -> dict[str, object]:
    first: dict[tuple[int, ...], int] = {}
    counts: dict[tuple[int, ...], int] = {}
    tied = 0
    for m in range(0, limit - k + 1):
        pattern = strict_pattern(phi[m + 1 : m + k + 1])
        if pattern is None:
            tied += 1
            continue
        counts[pattern] = counts.get(pattern, 0) + 1
        first.setdefault(pattern, m + k)

    total_windows = limit - k + 1
    assert sum(counts.values()) + tied == total_windows
    all_patterns = list(itertools.permutations(range(1, k + 1)))
    missing = [p for p in all_patterns if p not in first]
    ordered_first = sorted(first.items(), key=lambda item: item[1])
    decreasing = tuple(range(k, 0, -1))
    decreasing_endpoint = first.get(decreasing)
    observed_after_decreasing = bool(
        decreasing_endpoint is not None
        and any(endpoint > decreasing_endpoint for endpoint in first.values())
    )
    if observed_after_decreasing:
        decreasing_is_last: bool | None = False
    elif not missing and ordered_first[-1][0] == decreasing:
        decreasing_is_last = True
    else:
        decreasing_is_last = None
    extensions = natural_extensions(phi, k)
    stable = tuple(sorted(range(1, k + 1), key=lambda i: (phi[i], i)))

    result: dict[str, object] = {
        "k": k,
        "windows": total_windows,
        "tied_windows": tied,
        "patterns_seen": len(first),
        "patterns_total": math.factorial(k),
        "missing_count": len(missing),
        "last_observed_endpoint": ordered_first[-1][1],
        "last_pattern": list(ordered_first[-1][0]) if not missing else None,
        "M_k": ordered_first[-1][1] if not missing else None,
        "decreasing_pattern": list(decreasing),
        "decreasing_first_endpoint": decreasing_endpoint,
        "decreasing_is_last": decreasing_is_last,
        "stable_natural_refinement": list(stable),
        "natural_extensions": [list(p) for p in extensions],
        "natural_aggregate_count": sum(counts.get(p, 0) for p in extensions),
    }
    if include_counts:
        result["counts"] = [
            {"pattern": list(p), "count": counts.get(p, 0)} for p in all_patterns
        ]
    if include_pattern_lists or k <= 4:
        result["missing_patterns"] = [list(p) for p in missing]
        result["first_occurrences"] = [
            {"pattern": list(p), "endpoint": endpoint}
            for p, endpoint in ordered_first
        ]
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--max-k", type=int, default=6)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--include-counts", action="store_true")
    parser.add_argument("--include-pattern-lists", action="store_true")
    args = parser.parse_args()
    if args.limit < 6 or args.max_k < 1 or args.max_k > args.limit:
        parser.error("require limit >= 6 and 1 <= max-k <= limit")

    started = time.perf_counter()
    phi = totient_sieve(args.limit)
    for n in range(1, min(args.limit, 500) + 1):
        assert phi[n] == totient_naive(n), (n, phi[n], totient_naive(n))
    assert phi[1:7] == [1, 1, 2, 2, 4, 2]

    results = [
        scan(
            phi,
            args.limit,
            k,
            args.include_counts,
            args.include_pattern_lists,
        )
        for k in range(1, args.max_k + 1)
    ]
    by_k = {row["k"]: row for row in results}
    assert by_k[2]["M_k"] == 6
    assert by_k[2]["last_pattern"] == [2, 1]

    payload = {
        "command_template": "python3 computational/pattern_scan.py --limit N --max-k K --output FILE",
        "algorithm": "Euler totient sieve, followed by exhaustive overlapping-window scan",
        "permutation_convention": "one-based positions sorted by strictly increasing totient",
        "tie_convention": "a tied window realizes no permutation",
        "limit": args.limit,
        "max_k": args.max_k,
        "runtime_seconds": round(time.perf_counter() - started, 6),
        "independent_check": "sieve values checked against gcd-count definition for n <= 500",
        "results": results,
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
