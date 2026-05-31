#!/usr/bin/env python3
"""Deterministic residual-failure census for capped `gamma=2alpha` shells.

The randomized residual sampler is useful for discovering obstruction types,
but the `N=63` and `N=99` proof gap needs exact counts.  This script streams
the same finite boundary-shell demand space used by
`gamma_2alpha_low_mixed_shell_census.py`, optionally discards shells covered by
the default local-overlap cover, and then applies the exact residual diagnostic
from `gamma_2alpha_residual_failure_causes.py`.
"""

from __future__ import annotations

import argparse
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import (  # noqa: E402
    RefinedGamma2AlphaSurvivor,
    refined_survivors_for_n,
    viable_free_x_representations,
    viable_x_representations,
)
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_endpoint_automaton import PlacedEdge, alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_low_mixed_shell_census import paths_by_endpoint_and_mixed  # noqa: E402
from gamma_2alpha_mixed_growth import count_by_cap  # noqa: E402
from gamma_2alpha_overlap_cover import (  # noqa: E402
    DEFAULT_PAIR_TEXT,
    KPolygon,
    parse_pair,
    qdenominator_scale,
    side_tile_polygon,
    valid_pairs_for_lengths,
)
from gamma_2alpha_random_shell_search import all_path_options  # noqa: E402
from gamma_2alpha_residual_failure_causes import ShellDiagnostic, diagnose_shell  # noqa: E402


Triple = tuple[int, int, int]
Path = tuple[PlacedEdge, ...]
EndpointMixed = tuple[PlacedEdge, PlacedEdge, int]
PathIndex = dict[EndpointMixed, tuple[Path, ...]]
DemandKey = tuple[tuple[tuple[str, str, str], ...], ...]


class LocalCoverChecker:
    def __init__(self, survivor: RefinedGamma2AlphaSurvivor, radicand: int) -> None:
        exact.RADICAND = radicand
        pairs = tuple(parse_pair(text) for text in DEFAULT_PAIR_TEXT)
        candidate = survivor.candidate
        x_reps = set(viable_x_representations(candidate) + viable_free_x_representations(candidate))
        base_reps = set(survivor.y_representations)
        x_paths = tuple(path for rep in x_reps for path in all_path_options(rep))
        base_paths = tuple(path for rep in base_reps for path in all_path_options(rep))
        max_x_len = max((len(path) for path in x_paths), default=0)
        max_base_len = max((len(path) for path in base_paths), default=0)
        self.active_pairs = valid_pairs_for_lengths(pairs, max_x_len, max_base_len)
        needed_positions = {
            "L": sorted({pair.side_position for pair in self.active_pairs if pair.side == "L"}),
            "R": sorted({pair.side_position for pair in self.active_pairs if pair.side == "R"}),
            "B": sorted({pair.base_position for pair in self.active_pairs}),
        }

        q_polygons: dict[tuple[str, int, Path], exact.QPolygon] = {}
        all_polygons: list[exact.QPolygon] = []
        for side_name, paths in (("L", x_paths), ("R", x_paths), ("B", base_paths)):
            for position in needed_positions[side_name]:
                for path in paths:
                    if position > len(path):
                        continue
                    polygon = side_tile_polygon(
                        survivor,
                        side_name=side_name,
                        path=path,
                        position=position,
                        radicand=radicand,
                    )
                    q_polygons[(side_name, position, path)] = polygon
                    all_polygons.append(polygon)
        scale = qdenominator_scale(all_polygons) if all_polygons else 1
        self.polygons = {key: self.kscale_polygon(polygon, scale) for key, polygon in q_polygons.items()}
        self.overlap_cache: dict[tuple[KPolygon, KPolygon], bool] = {}

    @staticmethod
    def kscale_polygon(polygon: exact.QPolygon, scale: int) -> KPolygon:
        return tuple(exact.kscale_point(point, scale) for point in polygon)

    def overlaps(self, left: KPolygon, right: KPolygon) -> bool:
        key = (left, right)
        value = self.overlap_cache.get(key)
        if value is None:
            value = (
                not exact.kbbox_disjoint(exact.kbbox(left), exact.kbbox(right))
                and not exact.ksame_triangle(left, right)
                and exact.kpositive_overlap(left, right)
            )
            self.overlap_cache[key] = value
        return value

    def first_overlap(self, demand: BoundaryDemand) -> tuple[str, str] | None:
        for pair in self.active_pairs:
            side_path = demand.left_path if pair.side == "L" else demand.right_path
            side_key = (pair.side, pair.side_position, side_path)
            base_key = ("B", pair.base_position, demand.base_path)
            side_polygon = self.polygons.get(side_key)
            base_polygon = self.polygons.get(base_key)
            if side_polygon is None or base_polygon is None:
                continue
            if self.overlaps(side_polygon, base_polygon):
                return f"{pair.side}{pair.side_position}", f"B{pair.base_position}"
        return None


def demand_key(demand: BoundaryDemand) -> DemandKey:
    return (
        tuple((edge.side, edge.start, edge.end) for edge in demand.left_path),
        tuple((edge.side, edge.start, edge.end) for edge in demand.right_path),
        tuple((edge.side, edge.start, edge.end) for edge in demand.base_path),
    )


def iter_orientation_demands(
    *,
    short_side: str,
    left_rep: Triple,
    right_rep: Triple,
    base_rep: Triple,
    left_index: PathIndex,
    right_index: PathIndex,
    base_index: PathIndex,
    max_total_mixed: int,
) -> Iterable[BoundaryDemand]:
    for (left_first, left_last, left_mixed), left_paths in left_index.items():
        for (right_first, right_last, right_mixed), right_paths in right_index.items():
            if left_mixed + right_mixed > max_total_mixed - 1:
                continue
            if not apex_corner(left_last, right_first):
                continue
            for (base_first, base_last, base_mixed), base_paths in base_index.items():
                total_mixed = left_mixed + right_mixed + base_mixed
                if total_mixed > max_total_mixed:
                    continue
                if not alpha_corner(right_last, base_first):
                    continue
                if not alpha_corner(base_last, left_first):
                    continue
                for left_path in left_paths:
                    for right_path in right_paths:
                        for base_path in base_paths:
                            yield BoundaryDemand(
                                short_side=short_side,
                                left_rep=left_rep,
                                right_rep=right_rep,
                                base_rep=base_rep,
                                mixed_transitions=total_mixed,
                                left_path=left_path,
                                right_path=right_path,
                                base_path=base_path,
                            )


def iter_capped_demands(
    survivor: RefinedGamma2AlphaSurvivor,
    *,
    max_total_mixed: int,
    min_total_mixed: int,
    dedupe: bool,
) -> Iterable[BoundaryDemand]:
    candidate = survivor.candidate
    bounded_reps = viable_x_representations(candidate)
    free_reps = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations

    indexes = {
        rep: paths_by_endpoint_and_mixed(rep)
        for rep in set(bounded_reps + free_reps + base_reps)
    }
    seen: set[DemandKey] = set()

    def yield_orientation(
        short_side: str,
        left_reps: tuple[Triple, ...],
        right_reps: tuple[Triple, ...],
    ) -> Iterable[BoundaryDemand]:
        for left_rep in left_reps:
            for right_rep in right_reps:
                for base_rep in base_reps:
                    yield from iter_orientation_demands(
                        short_side=short_side,
                        left_rep=left_rep,
                        right_rep=right_rep,
                        base_rep=base_rep,
                        left_index=indexes[left_rep],
                        right_index=indexes[right_rep],
                        base_index=indexes[base_rep],
                        max_total_mixed=max_total_mixed,
                    )

    orientations = [("left", bounded_reps, free_reps)]
    if bounded_reps != free_reps:
        orientations.append(("right", free_reps, bounded_reps))

    for short_side, left_reps, right_reps in orientations:
        for demand in yield_orientation(short_side, left_reps, right_reps):
            if demand.mixed_transitions < min_total_mixed:
                continue
            if dedupe:
                key = demand_key(demand)
                if key in seen:
                    continue
                seen.add(key)
            yield demand


def format_counter(counter: Counter[str]) -> str:
    return "{" + ", ".join(f"{key}: {value}" for key, value in sorted(counter.items())) + "}"


def print_example(status: str, demand: BoundaryDemand, detail: ShellDiagnostic) -> None:
    print(
        f"    {status}: L={path_labels(demand.left_path)} "
        f"R={path_labels(demand.right_path)} "
        f"B={path_labels(demand.base_path)} "
        f"mixed={demand.mixed_transitions} "
        f"forced={detail.forced_corners} violations={detail.label_violations}"
    )


def classify_shell(
    survivor: RefinedGamma2AlphaSurvivor,
    demand: BoundaryDemand,
    radicand: int,
) -> ShellDiagnostic:
    coarse = exact.classify_quadratic_shell(survivor, demand, radicand)
    if coarse.status == "not-simple-cycle":
        return diagnose_shell(survivor, demand, radicand)
    return ShellDiagnostic(
        coarse.status,
        forced_corners=coarse.forced_corners,
        label_violations=coarse.label_violations,
    )


def expected_count(
    survivor: RefinedGamma2AlphaSurvivor,
    *,
    min_total_mixed: int,
    max_total_mixed: int,
) -> int:
    lower = count_by_cap(survivor, min_total_mixed - 1) if min_total_mixed > 0 else 0
    return count_by_cap(survivor, max_total_mixed) - lower


def census_survivor(
    survivor: RefinedGamma2AlphaSurvivor,
    *,
    min_total_mixed: int,
    max_total_mixed: int,
    outside_local_cover: bool,
    limit: int | None,
    progress_every: int,
    show_examples: bool,
    top: int,
) -> None:
    radicand = exact.field_radicand(survivor)
    if radicand is None:
        print("  exact quadratic classifier unavailable for this survivor", flush=True)
        return

    expected = expected_count(
        survivor,
        min_total_mixed=min_total_mixed,
        max_total_mixed=max_total_mixed,
    )
    print(
        f"  Q(sqrt({radicand})) shells with {min_total_mixed} <= mixed <= {max_total_mixed}: "
        f"expected {expected}",
        flush=True,
    )
    local_checker = LocalCoverChecker(survivor, radicand) if outside_local_cover else None

    status_counts: Counter[str] = Counter()
    mixed_counts: dict[int, Counter[str]] = defaultdict(Counter)
    local_cover_counts: Counter[tuple[str, str]] = Counter()
    split_failure_counts: Counter[str] = Counter()
    examples: dict[str, tuple[BoundaryDemand, ShellDiagnostic]] = {}

    generated = 0
    kept = 0
    covered = 0
    started = time.monotonic()

    for demand in iter_capped_demands(
        survivor,
        max_total_mixed=max_total_mixed,
        min_total_mixed=min_total_mixed,
        dedupe=True,
    ):
        generated += 1
        if limit is not None and generated > limit:
            generated -= 1
            break
        if outside_local_cover:
            assert local_checker is not None
            local_cover = local_checker.first_overlap(demand)
            if local_cover is not None:
                covered += 1
                local_cover_counts[local_cover] += 1
                continue

        kept += 1
        detail = classify_shell(survivor, demand, radicand)
        status_counts[detail.status] += 1
        mixed_counts[demand.mixed_transitions][detail.status] += 1
        examples.setdefault(detail.status, (demand, detail))
        for reason, count in detail.split_failure_reasons:
            split_failure_counts[reason] += count

        if progress_every and generated % progress_every == 0:
            elapsed = time.monotonic() - started
            rate = generated / elapsed if elapsed > 0 else 0.0
            print(
                f"    progress generated={generated} kept={kept} covered={covered} "
                f"rate={rate:.1f}/s",
                flush=True,
            )

    suffix = " (limited)" if limit is not None and generated < expected else ""
    cover_text = f"; local-cover hits={covered}" if outside_local_cover else ""
    print(f"  processed={generated}/{expected}{suffix}; diagnosed={kept}{cover_text}", flush=True)
    print(f"  status counts={format_counter(status_counts)}", flush=True)
    print("  status by mixed:", flush=True)
    for mixed, counts in sorted(mixed_counts.items()):
        print(f"    mixed={mixed}: {format_counter(counts)}", flush=True)
    if outside_local_cover:
        print("  top local-cover pairs:", flush=True)
        for (left, right), count in local_cover_counts.most_common(top):
            print(f"    {left} with {right}: {count}", flush=True)
    if split_failure_counts:
        print("  top split failure reasons:", flush=True)
        for reason, count in split_failure_counts.most_common(top):
            print(f"    {reason}: {count}", flush=True)
    if show_examples:
        print("  examples:", flush=True)
        for status, (demand, detail) in sorted(examples.items()):
            print_example(status, demand, detail)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-total-mixed", type=int, default=4)
    parser.add_argument("--min-total-mixed", type=int, default=0)
    parser.add_argument(
        "--outside-local-cover",
        action="store_true",
        help="discard shells removed by the default exact local-overlap cover before diagnosing residual failures",
    )
    parser.add_argument("--limit", type=int, help="stop after LIMIT generated shell demands")
    parser.add_argument("--progress-every", type=int, default=0)
    parser.add_argument("--show-examples", action="store_true")
    parser.add_argument("--top", type=int, default=12)
    args = parser.parse_args()

    if args.min_total_mixed < 0:
        raise SystemExit("--min-total-mixed must be nonnegative")
    if args.max_total_mixed < args.min_total_mixed:
        raise SystemExit("--max-total-mixed must be at least --min-total-mixed")

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            print(f"  tile={survivor.candidate.tile} X={survivor.candidate.x} Y={survivor.candidate.y}")
            census_survivor(
                survivor,
                min_total_mixed=args.min_total_mixed,
                max_total_mixed=args.max_total_mixed,
                outside_local_cover=args.outside_local_cover,
                limit=args.limit,
                progress_every=args.progress_every,
                show_examples=args.show_examples,
                top=args.top,
            )


if __name__ == "__main__":
    main()
