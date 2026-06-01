#!/usr/bin/env python3
"""Exhaustively classify selected fixed side-label word triples.

The word-quotient census suggests that, for the remaining `gamma=2alpha`
mixed-6 shells, the refined residual obstruction status may depend only on the
side-label words `(L,R,B)` and not on the oriented angle endpoints realizing
those words.  This probe attacks that claim directly for selected word triples
by enumerating every matching oriented boundary demand in the capped shell
space and classifying all demands outside the local-overlap cover.
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
from gamma_2alpha_boundary import refined_survivors_for_n  # noqa: E402
from gamma_2alpha_overlap_remainder_inventory import label_word  # noqa: E402
from gamma_2alpha_residual_capped_census import classify_shell, iter_capped_demands  # noqa: E402
from gamma_2alpha_residual_chunked_census import LazyLocalCoverChecker  # noqa: E402


WordTriple = tuple[str, str, str]


def parse_word(text: str) -> WordTriple:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("word must have form LWORD,RWORD,BWORD")
    return parts[0], parts[1], parts[2]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--word", action="append", type=parse_word, required=True)
    parser.add_argument("--min-total-mixed", type=int, default=6)
    parser.add_argument("--max-total-mixed", type=int, default=6)
    parser.add_argument("--stop-when-seen", type=int, default=0)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    if args.max_total_mixed < args.min_total_mixed:
        raise SystemExit("--max-total-mixed must be at least --min-total-mixed")
    if args.stop_when_seen < 0:
        raise SystemExit("--stop-when-seen must be nonnegative")

    survivors = refined_survivors_for_n(args.n)
    if len(survivors) != 1:
        raise SystemExit(f"expected one survivor for N={args.n}, got {len(survivors)}")
    survivor = survivors[0]
    radicand = exact.field_radicand(survivor)
    if radicand is None:
        raise SystemExit("quadratic field unavailable")
    local_checker = LazyLocalCoverChecker(survivor, radicand)
    targets = tuple(args.word)
    target_set = set(targets)

    status_counts = {target: Counter() for target in targets}
    covered_counts: Counter[WordTriple] = Counter()
    outside_counts: Counter[WordTriple] = Counter()
    generated = 0
    started = time.monotonic()

    for demand in iter_capped_demands(
        survivor,
        min_total_mixed=args.min_total_mixed,
        max_total_mixed=args.max_total_mixed,
        dedupe=True,
    ):
        generated += 1
        word = (
            label_word(demand.left_path),
            label_word(demand.right_path),
            label_word(demand.base_path),
        )
        if word not in target_set:
            continue
        if local_checker.first_overlap(demand) is not None:
            covered_counts[word] += 1
            continue
        detail = classify_shell(survivor, demand, radicand)
        status_counts[word][detail.status] += 1
        outside_counts[word] += 1
        if args.stop_when_seen and all(outside_counts[target] >= args.stop_when_seen for target in targets):
            break

    result = {
        "n": args.n,
        "tile": survivor.candidate.tile,
        "radicand": radicand,
        "min_total_mixed": args.min_total_mixed,
        "max_total_mixed": args.max_total_mixed,
        "generated_until_stop": generated,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "targets": [
            {
                "word": {"L": target[0], "R": target[1], "B": target[2]},
                "covered_target": covered_counts[target],
                "outside_cover_seen": outside_counts[target],
                "status_counts": dict(sorted(status_counts[target].items())),
            }
            for target in targets
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    if args.json_out is not None:
        args.json_out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
