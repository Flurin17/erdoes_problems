#!/usr/bin/env python3
"""Chunked exact residual census for `gamma=2alpha` boundary shells.

This runner is intentionally simple: it streams the deterministic capped shell
space, optionally skips shells hit by the default local-overlap cover, and
classifies only a generated-shell slice.  It is for long exact passes that need
to be resumed across turns without changing the enumeration order.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import refined_survivors_for_n, viable_free_x_representations, viable_x_representations  # noqa: E402
from gamma_2alpha_overlap_cover import DEFAULT_PAIR_TEXT, parse_pair, side_tile_polygon, valid_pairs_for_lengths  # noqa: E402
from gamma_2alpha_residual_capped_census import (  # noqa: E402
    LocalCoverChecker,
    classify_shell,
    iter_capped_demands,
)


def classify(
    survivor,
    demand,
    radicand: int,
    *,
    mode: str,
) -> str:
    if mode == "coarse":
        return exact.classify_quadratic_shell(survivor, demand, radicand).status
    if mode == "refined":
        return classify_shell(survivor, demand, radicand).status
    raise ValueError(mode)


class LazyLocalCoverChecker:
    def __init__(self, survivor, radicand: int) -> None:
        self.survivor = survivor
        self.radicand = radicand
        pairs = tuple(parse_pair(text) for text in DEFAULT_PAIR_TEXT)
        x_reps = viable_x_representations(survivor.candidate) + viable_free_x_representations(survivor.candidate)
        base_reps = survivor.y_representations
        max_x_len = max(sum(rep) for rep in x_reps)
        max_base_len = max(sum(rep) for rep in base_reps)
        self.active_pairs = valid_pairs_for_lengths(pairs, max_x_len, max_base_len)
        self.polygon_cache = {}
        self.overlap_cache = {}

    def polygon(self, side_name: str, path, position: int):
        key = (side_name, position, path)
        cached = self.polygon_cache.get(key)
        if cached is not None:
            return cached
        exact.RADICAND = self.radicand
        polygon = side_tile_polygon(
            self.survivor,
            side_name=side_name,
            path=path,
            position=position,
            radicand=self.radicand,
        )
        self.polygon_cache[key] = polygon
        return polygon

    def overlaps(self, left, right) -> bool:
        if exact.qbbox_disjoint(exact.qbbox(left), exact.qbbox(right)):
            return False
        if exact.qsame_triangle(left, right):
            return False
        return exact.qpositive_overlap(left, right)

    def first_overlap(self, demand) -> tuple[str, str] | None:
        exact.RADICAND = self.radicand
        for pair in self.active_pairs:
            side_path = demand.left_path if pair.side == "L" else demand.right_path
            key = (pair.side, pair.side_position, pair.base_position, side_path, demand.base_path)
            cached = self.overlap_cache.get(key)
            if cached is None:
                side_polygon = self.polygon(pair.side, side_path, pair.side_position)
                base_polygon = self.polygon("B", demand.base_path, pair.base_position)
                cached = self.overlaps(side_polygon, base_polygon)
                self.overlap_cache[key] = cached
            if cached:
                return f"{pair.side}{pair.side_position}", f"B{pair.base_position}"
        return None


def make_local_checker(survivor, radicand: int, mode: str):
    if mode == "eager":
        return LocalCoverChecker(survivor, radicand)
    if mode == "lazy":
        return LazyLocalCoverChecker(survivor, radicand)
    raise ValueError(mode)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--min-total-mixed", type=int, default=6)
    parser.add_argument("--max-total-mixed", type=int, default=6)
    parser.add_argument("--outside-local-cover", action="store_true")
    parser.add_argument("--local-cover-mode", choices=("eager", "lazy"), default="eager")
    parser.add_argument("--mode", choices=("coarse", "refined"), default="coarse")
    parser.add_argument("--skip-generated", type=int, default=0)
    parser.add_argument("--max-generated", type=int, default=10000)
    parser.add_argument("--progress-every", type=int, default=1000)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    if args.skip_generated < 0:
        raise SystemExit("--skip-generated must be nonnegative")
    if args.max_generated <= 0:
        raise SystemExit("--max-generated must be positive")

    survivors = refined_survivors_for_n(args.n)
    if len(survivors) != 1:
        raise SystemExit(f"expected one survivor for N={args.n}, got {len(survivors)}")
    survivor = survivors[0]
    radicand = exact.field_radicand(survivor)
    if radicand is None:
        raise SystemExit("exact quadratic classifier unavailable")

    local_checker = make_local_checker(survivor, radicand, args.local_cover_mode) if args.outside_local_cover else None
    generated_seen = 0
    generated_processed = 0
    covered = 0
    diagnosed = 0
    counts: Counter[str] = Counter()
    started = time.monotonic()

    for demand in iter_capped_demands(
        survivor,
        min_total_mixed=args.min_total_mixed,
        max_total_mixed=args.max_total_mixed,
        dedupe=True,
    ):
        generated_seen += 1
        if generated_seen <= args.skip_generated:
            continue
        if generated_processed >= args.max_generated:
            break
        generated_processed += 1

        if local_checker is not None and local_checker.first_overlap(demand) is not None:
            covered += 1
            continue

        status = classify(survivor, demand, radicand, mode=args.mode)
        counts[status] += 1
        diagnosed += 1

        if args.progress_every and generated_processed % args.progress_every == 0:
            elapsed = time.monotonic() - started
            rate = generated_processed / elapsed if elapsed else 0.0
            print(
                f"  progress generated_seen={generated_seen} "
                f"processed={generated_processed} covered={covered} "
                f"diagnosed={diagnosed} rate={rate:.1f}/s",
                flush=True,
            )

    result = {
        "n": args.n,
        "tile": survivor.candidate.tile,
        "radicand": radicand,
        "min_total_mixed": args.min_total_mixed,
        "max_total_mixed": args.max_total_mixed,
        "outside_local_cover": args.outside_local_cover,
        "local_cover_mode": args.local_cover_mode if args.outside_local_cover else None,
        "mode": args.mode,
        "skip_generated": args.skip_generated,
        "max_generated": args.max_generated,
        "generated_seen": generated_seen,
        "generated_processed": generated_processed,
        "covered": covered,
        "diagnosed": diagnosed,
        "status_counts": dict(sorted(counts.items())),
    }
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    if args.json_out is not None:
        args.json_out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
