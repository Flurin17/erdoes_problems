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
from gamma_2alpha_boundary import refined_survivors_for_n, viable_free_x_representations, viable_x_representations  # noqa: E402
from gamma_2alpha_boundary_transition_demand import BoundaryDemand  # noqa: E402
from gamma_2alpha_endpoint_automaton import alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_overlap_remainder_inventory import label_word  # noqa: E402
from gamma_2alpha_random_shell_search import all_path_options, mixed_transitions  # noqa: E402
from gamma_2alpha_residual_capped_census import classify_shell, demand_key  # noqa: E402
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
    candidate = survivor.candidate
    bounded_reps = viable_x_representations(candidate)
    free_reps = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations
    paths_by_rep_and_word = {}
    for rep in set(bounded_reps + free_reps + base_reps):
        by_word = {}
        for path in all_path_options(rep):
            by_word.setdefault(label_word(path), []).append(path)
        paths_by_rep_and_word[rep] = {word: tuple(paths) for word, paths in by_word.items()}

    status_counts = {target: Counter() for target in targets}
    covered_counts: Counter[WordTriple] = Counter()
    outside_counts: Counter[WordTriple] = Counter()
    generated = 0
    seen_demands = set()
    started = time.monotonic()

    orientations = [("left", bounded_reps, free_reps)]
    if bounded_reps != free_reps:
        orientations.append(("right", free_reps, bounded_reps))

    for target in targets:
        left_word, right_word, base_word = target
        for short_side, left_reps, right_reps in orientations:
            for left_rep in left_reps:
                left_paths = paths_by_rep_and_word[left_rep].get(left_word, ())
                if not left_paths:
                    continue
                for right_rep in right_reps:
                    right_paths = paths_by_rep_and_word[right_rep].get(right_word, ())
                    if not right_paths:
                        continue
                    for base_rep in base_reps:
                        base_paths = paths_by_rep_and_word[base_rep].get(base_word, ())
                        if not base_paths:
                            continue
                        for left_path in left_paths:
                            left_mixed = mixed_transitions(left_path)
                            for right_path in right_paths:
                                if not apex_corner(left_path[-1], right_path[0]):
                                    continue
                                right_mixed = mixed_transitions(right_path)
                                for base_path in base_paths:
                                    total_mixed = left_mixed + right_mixed + mixed_transitions(base_path)
                                    if not args.min_total_mixed <= total_mixed <= args.max_total_mixed:
                                        continue
                                    if not alpha_corner(right_path[-1], base_path[0]):
                                        continue
                                    if not alpha_corner(base_path[-1], left_path[0]):
                                        continue
                                    demand = BoundaryDemand(
                                        short_side=short_side,
                                        left_rep=left_rep,
                                        right_rep=right_rep,
                                        base_rep=base_rep,
                                        mixed_transitions=total_mixed,
                                        left_path=left_path,
                                        right_path=right_path,
                                        base_path=base_path,
                                    )
                                    key = demand_key(demand)
                                    if key in seen_demands:
                                        continue
                                    seen_demands.add(key)
                                    generated += 1
                                    if local_checker.first_overlap(demand) is not None:
                                        covered_counts[target] += 1
                                        continue
                                    detail = classify_shell(survivor, demand, radicand)
                                    status_counts[target][detail.status] += 1
                                    outside_counts[target] += 1
                                    if args.stop_when_seen and outside_counts[target] >= args.stop_when_seen:
                                        break
                                if args.stop_when_seen and outside_counts[target] >= args.stop_when_seen:
                                    break
                            if args.stop_when_seen and outside_counts[target] >= args.stop_when_seen:
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
