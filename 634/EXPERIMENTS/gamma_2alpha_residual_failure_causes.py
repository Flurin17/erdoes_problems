#!/usr/bin/env python3
"""Exact residual-failure sampler for `gamma=2alpha` boundary shells.

The local overlap cover removes most high-mixed boundary shells for the
remaining `N=63` and `N=99` benchmark rows.  This diagnostic focuses on the
sampled shells that avoid that cover and records why the exact residual
classifier still rejects them: non-simple residual graph structure or forced
single-corner side-label mismatches.
"""

from __future__ import annotations

import argparse
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import RefinedGamma2AlphaSurvivor, refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_overlap_causes import local_cover_overlap  # noqa: E402
from gamma_2alpha_random_shell_search import mixed_transitions, weighted_valid_demands  # noqa: E402


GraphProfile = tuple[int, int, int, tuple[tuple[int, int], ...]]
CounterTuple = tuple[tuple[str, int], ...]
ViolationTuple = tuple[tuple[str, str, int], ...]


@dataclass(frozen=True)
class ShellDiagnostic:
    status: str
    remaining_tiles: int = 0
    residual_edges: int = 0
    residual_vertices: int = 0
    graph_components: int = 0
    degree_profile: tuple[tuple[int, int], ...] = ()
    residual_labels: CounterTuple = ()
    non_full_atoms: int = 0
    wrong_full_label_atoms: int = 0
    parity_mismatches: str = ""
    forced_corners: int = 0
    label_violations: int = 0
    forced_angles: CounterTuple = ()
    violation_types: ViolationTuple = ()


def graph_data(segments: list[exact.KSegment]) -> tuple[dict[exact.KPoint, list[exact.KPoint]], int]:
    graph: dict[exact.KPoint, list[exact.KPoint]] = {}
    for start, end in segments:
        graph.setdefault(start, []).append(end)
        graph.setdefault(end, []).append(start)

    seen: set[exact.KPoint] = set()
    components = 0
    for start in graph:
        if start in seen:
            continue
        components += 1
        stack = [start]
        seen.add(start)
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
    return graph, components


def graph_profile(segments: list[exact.KSegment]) -> GraphProfile:
    graph, components = graph_data(segments)
    degrees = Counter(len(neighbors) for neighbors in graph.values())
    return len(segments), len(graph), components, tuple(sorted(degrees.items()))


def residual_label_profile(residual_labels: dict[exact.KSegment, str]) -> CounterTuple:
    return tuple(sorted(Counter(residual_labels.values()).items()))


def segment_length(segment: exact.KSegment, scale: int):
    length_sq = exact.knorm_sq(exact.kpsub(segment[1], segment[0]))
    if length_sq[1] != 0:
        return None
    return exact.sqrt_fraction(exact.Fraction(length_sq[0], scale * scale))


def full_atom_failures(
    residual_labels: dict[exact.KSegment, str],
    sides: tuple[int, int, int],
    scale: int,
) -> tuple[int, int]:
    side_lengths = {"a": sides[0], "b": sides[1], "c": sides[2]}
    length_values = set(side_lengths.values())
    non_full = 0
    wrong_label = 0
    for segment, label in residual_labels.items():
        length = segment_length(segment, scale)
        if length not in length_values:
            non_full += 1
        elif length != side_lengths[label]:
            wrong_label += 1
    return non_full, wrong_label


def parity_mismatches(label_profile: CounterTuple, remaining_tiles: int) -> str:
    parity = remaining_tiles % 2
    mismatches = tuple(label for label, count in label_profile if count % 2 != parity)
    return "".join(mismatches)


def diagnose_shell(
    survivor: RefinedGamma2AlphaSurvivor,
    demand: BoundaryDemand,
    radicand: int,
) -> ShellDiagnostic:
    exact.RADICAND = radicand
    shell = exact.place_boundary_shell(survivor, demand, radicand)
    outer = exact.outer_vertices(survivor, radicand)
    if shell is None or outer is None:
        return ShellDiagnostic("not-quadratic")

    integer_shell, integer_outer, scale = exact.kscale_shell(shell, outer)
    unique_or_status = exact.kunique_tiles_or_overlap(integer_shell)
    if unique_or_status == "proper-overlap":
        return ShellDiagnostic("proper-overlap")
    unique = unique_or_status
    assert isinstance(unique, tuple)
    remaining_tiles = survivor.candidate.n - len(unique)

    residual_labels = exact.kresidual_segments_with_labels(unique, integer_outer)
    residual_segments = list(residual_labels)
    edges, vertices, components, degree_counts = graph_profile(residual_segments)
    label_profile = residual_label_profile(residual_labels)
    non_full_atoms, wrong_full_label_atoms = full_atom_failures(residual_labels, survivor.candidate.tile, scale)
    parity_bad = (
        parity_mismatches(label_profile, remaining_tiles)
        if non_full_atoms == 0 and wrong_full_label_atoms == 0
        else ""
    )
    cycle = exact.ksimple_cycle(residual_segments)
    if cycle is None:
        return ShellDiagnostic(
            "not-simple-cycle",
            remaining_tiles=remaining_tiles,
            residual_edges=edges,
            residual_vertices=vertices,
            graph_components=components,
            degree_profile=degree_counts,
            residual_labels=label_profile,
            non_full_atoms=non_full_atoms,
            wrong_full_label_atoms=wrong_full_label_atoms,
            parity_mismatches=parity_bad,
        )

    if any(exact.kside_decomposable(segment, survivor.candidate.tile, scale) for segment in residual_labels):
        return ShellDiagnostic(
            "decomposable-residual-atom",
            remaining_tiles=remaining_tiles,
            residual_edges=edges,
            residual_vertices=vertices,
            graph_components=components,
            degree_profile=degree_counts,
            residual_labels=label_profile,
            non_full_atoms=non_full_atoms,
            wrong_full_label_atoms=wrong_full_label_atoms,
            parity_mismatches=parity_bad,
        )

    forced_angles: Counter[str] = Counter()
    violation_types: Counter[tuple[str, str]] = Counter()
    forced = 0
    violations = 0
    for index in range(len(cycle)):
        angle_name = exact.ksingle_angle_name(cycle, index, survivor.candidate.tile, scale)
        if angle_name is None:
            continue
        forced += 1
        forced_angles[angle_name] += 1
        previous_label = residual_labels[exact.kcycle_edge_key(cycle, index - 1)]
        next_label = residual_labels[exact.kcycle_edge_key(cycle, index)]
        label_pair = tuple(sorted((previous_label, next_label)))
        if frozenset(label_pair) != exact.ANGLE_SIDES[angle_name]:
            violations += 1
            violation_types[(angle_name, "".join(label_pair))] += 1

    status = "corner-label-violation" if violations else "passes-corner-label-check"
    return ShellDiagnostic(
        status,
        remaining_tiles=remaining_tiles,
        residual_edges=edges,
        residual_vertices=vertices,
        graph_components=components,
        degree_profile=degree_counts,
        residual_labels=label_profile,
        non_full_atoms=non_full_atoms,
        wrong_full_label_atoms=wrong_full_label_atoms,
        parity_mismatches=parity_bad,
        forced_corners=forced,
        label_violations=violations,
        forced_angles=tuple(sorted(forced_angles.items())),
        violation_types=tuple((angle, labels, count) for (angle, labels), count in sorted(violation_types.items())),
    )


def profile_text(profile: GraphProfile) -> str:
    edges, vertices, components, degree_counts = profile
    degree_text = ",".join(f"{degree}:{count}" for degree, count in degree_counts)
    return f"edges={edges}, vertices={vertices}, components={components}, degree={degree_text}"


def counter_tuple_text(items: CounterTuple) -> str:
    return ",".join(f"{key}:{value}" for key, value in items) if items else "-"


def print_example(status: str, demand: BoundaryDemand, detail: ShellDiagnostic) -> None:
    print(
        f"    {status}: L={path_labels(demand.left_path)} "
        f"R={path_labels(demand.right_path)} "
        f"B={path_labels(demand.base_path)} "
        f"mixed={mixed_transitions(demand.left_path) + mixed_transitions(demand.right_path) + mixed_transitions(demand.base_path)} "
        f"forced={detail.forced_corners} violations={detail.label_violations}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--samples", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=634)
    parser.add_argument("--max-total-mixed", type=int)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--show-examples", action="store_true")
    parser.add_argument(
        "--outside-local-cover",
        action="store_true",
        help="discard shells removed by the default local overlap cover before diagnosing residual failures",
    )
    args = parser.parse_args()

    rng = random.Random(args.seed)
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            radicand = exact.field_radicand(survivor)
            if radicand is None:
                print("  exact quadratic classifier unavailable", flush=True)
                continue
            demands = weighted_valid_demands(
                survivor,
                rng=rng,
                samples=args.samples,
                max_total_mixed=args.max_total_mixed,
            )
            status_counts: Counter[str] = Counter()
            mixed_counts: dict[int, Counter[str]] = defaultdict(Counter)
            graph_profiles: Counter[GraphProfile] = Counter()
            residual_label_profiles: Counter[CounterTuple] = Counter()
            forced_angle_profiles: Counter[CounterTuple] = Counter()
            violation_counts: Counter[tuple[str, str]] = Counter()
            violations_per_shell: Counter[int] = Counter()
            atom_counts: Counter[int] = Counter()
            full_atom_profiles: Counter[tuple[int, int, str]] = Counter()
            examples: dict[str, tuple[BoundaryDemand, ShellDiagnostic]] = {}
            kept = 0
            covered = 0

            for demand in demands:
                if args.outside_local_cover and local_cover_overlap(survivor, demand, radicand) is not None:
                    covered += 1
                    continue
                kept += 1
                detail = diagnose_shell(survivor, demand, radicand)
                status_counts[detail.status] += 1
                mixed_counts[demand.mixed_transitions][detail.status] += 1
                atom_counts[detail.residual_edges] += 1
                residual_label_profiles[detail.residual_labels] += 1
                full_atom_profiles[
                    (
                        detail.non_full_atoms,
                        detail.wrong_full_label_atoms,
                        detail.parity_mismatches or "-",
                    )
                ] += 1
                examples.setdefault(detail.status, (demand, detail))

                if detail.status == "not-simple-cycle":
                    graph_profiles[
                        (
                            detail.residual_edges,
                            detail.residual_vertices,
                            detail.graph_components,
                            detail.degree_profile,
                        )
                    ] += 1
                if detail.status == "corner-label-violation":
                    forced_angle_profiles[detail.forced_angles] += 1
                    violations_per_shell[detail.label_violations] += 1
                    for angle, labels, count in detail.violation_types:
                        violation_counts[(angle, labels)] += count

            mode = " outside local cover" if args.outside_local_cover else ""
            print(
                f"  valid-weighted samples{mode}={kept} from {len(demands)} valid samples/{args.samples} attempts"
                + (f"; local-cover hits discarded={covered}" if args.outside_local_cover else ""),
                flush=True,
            )
            print(f"  status counts={dict(sorted(status_counts.items()))}")
            print("  status by mixed:")
            for mixed, counts in sorted(mixed_counts.items()):
                print(f"    mixed={mixed}: {dict(sorted(counts.items()))}")
            print("  residual atom-count histogram:")
            for atom_count, count in atom_counts.most_common(args.top):
                print(f"    {atom_count}: {count}")
            print("  top residual label histograms:")
            for profile, count in residual_label_profiles.most_common(args.top):
                print(f"    {counter_tuple_text(profile)}: {count}")
            print("  full-side atom/parity profiles:")
            for (non_full, wrong_label, parity_bad), count in full_atom_profiles.most_common(args.top):
                print(f"    non_full={non_full}, wrong_label={wrong_label}, parity_bad={parity_bad}: {count}")
            print("  top non-simple graph profiles:")
            for profile, count in graph_profiles.most_common(args.top):
                print(f"    {profile_text(profile)}: {count}")
            print("  top forced-angle profiles among corner violations:")
            for profile, count in forced_angle_profiles.most_common(args.top):
                print(f"    {counter_tuple_text(profile)}: {count}")
            print("  corner violations per shell:")
            for violations, count in sorted(violations_per_shell.items()):
                print(f"    {violations}: {count}")
            print("  top corner violation types:")
            for (angle, labels), count in violation_counts.most_common(args.top):
                print(f"    {angle} with labels {labels}: {count}")
            if args.show_examples:
                for status, (demand, detail) in sorted(examples.items()):
                    print_example(status, demand, detail)


if __name__ == "__main__":
    main()
