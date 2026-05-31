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
import math
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import cmp_to_key
from itertools import product
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import RefinedGamma2AlphaSurvivor, refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_endpoint_automaton import trail_possible  # noqa: E402
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
    pinch_labels: CounterTuple = ()
    pinch_cyclic_labels: CounterTuple = ()
    pinch_residual_sectors: int = 0
    pinch_unfillable_sectors: int = 0
    pinch_sector_signatures: CounterTuple = ()
    split_options: int = 0
    split_component_pass_options: int = 0
    split_failure_reasons: CounterTuple = ()
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


def canonical_segment(start: exact.KPoint, end: exact.KPoint) -> exact.KSegment:
    return exact.ksegment_key(start, end)


def graph_profile(segments: list[exact.KSegment]) -> GraphProfile:
    graph, components = graph_data(segments)
    degrees = Counter(len(neighbors) for neighbors in graph.values())
    return len(segments), len(graph), components, tuple(sorted(degrees.items()))


def residual_label_profile(residual_labels: dict[exact.KSegment, str]) -> CounterTuple:
    return tuple(sorted(Counter(residual_labels.values()).items()))


def pinch_label_profile(residual_labels: dict[exact.KSegment, str]) -> CounterTuple:
    incidences: dict[exact.KPoint, list[str]] = defaultdict(list)
    for (start, end), label in residual_labels.items():
        incidences[start].append(label)
        incidences[end].append(label)
    profiles = Counter("".join(sorted(labels)) for labels in incidences.values() if len(labels) != 2)
    return tuple(sorted(profiles.items()))


def vector_half_plane(vector: exact.KPoint) -> int:
    y_sign = exact.ksign(vector[1])
    x_sign = exact.ksign(vector[0])
    return 0 if y_sign > 0 or (y_sign == 0 and x_sign >= 0) else 1


def compare_incident_half_edges(
    left: tuple[str, exact.KPoint],
    right: tuple[str, exact.KPoint],
) -> int:
    left_half = vector_half_plane(left[1])
    right_half = vector_half_plane(right[1])
    if left_half != right_half:
        return left_half - right_half
    cross = exact.ksign(exact.kcross(left[1], right[1]))
    if cross != 0:
        return -cross
    return (left[0] > right[0]) - (left[0] < right[0])


def canonical_cyclic_word(labels: tuple[str, ...]) -> str:
    if not labels:
        return ""
    rotations = ["".join(labels[index:] + labels[:index]) for index in range(len(labels))]
    reverse = tuple(reversed(labels))
    rotations.extend("".join(reverse[index:] + reverse[:index]) for index in range(len(reverse)))
    return min(rotations)


def pinch_cyclic_label_profile(residual_labels: dict[exact.KSegment, str]) -> CounterTuple:
    incidences: dict[exact.KPoint, list[tuple[str, exact.KPoint]]] = defaultdict(list)
    for (start, end), label in residual_labels.items():
        incidences[start].append((label, exact.kpsub(end, start)))
        incidences[end].append((label, exact.kpsub(start, end)))
    profiles = Counter()
    for half_edges in incidences.values():
        if len(half_edges) == 2:
            continue
        ordered = tuple(label for label, _vector in sorted(half_edges, key=cmp_to_key(compare_incident_half_edges)))
        profiles[canonical_cyclic_word(ordered)] += 1
    return tuple(sorted(profiles.items()))


def kquad_float(value: exact.KQuad) -> float:
    return float(value[0]) + float(value[1]) * math.sqrt(exact.RADICAND)


def kpoint_float(point: exact.KPoint) -> tuple[float, float]:
    return kquad_float(point[0]), kquad_float(point[1])


def angle_values(sides: tuple[int, int, int]) -> dict[str, float]:
    a, b, c = sides
    return {
        "alpha": math.acos((b * b + c * c - a * a) / (2 * b * c)),
        "beta": math.acos((a * a + c * c - b * b) / (2 * a * c)),
        "gamma": math.acos((a * a + b * b - c * c) / (2 * a * b)),
    }


def angle_counter_text(counter: Counter[str]) -> str:
    parts: list[str] = []
    for name in ("alpha", "beta", "gamma"):
        count = counter[name]
        if count == 1:
            parts.append(name)
        elif count > 1:
            parts.append(f"{count}{name}")
    return "+".join(parts) if parts else "0"


def sector_angle_combos(value: float, sides: tuple[int, int, int]) -> tuple[Counter[str], ...]:
    angles = angle_values(sides)
    out: list[Counter[str]] = []
    for alpha_count in range(7):
        for beta_count in range(4):
            for gamma_count in range(4):
                if alpha_count + beta_count + gamma_count == 0:
                    continue
                total = (
                    alpha_count * angles["alpha"]
                    + beta_count * angles["beta"]
                    + gamma_count * angles["gamma"]
                )
                if abs(total - value) < 1e-6:
                    out.append(Counter({"alpha": alpha_count, "beta": beta_count, "gamma": gamma_count}))
    return tuple(out)


def sector_fillable(left_label: str, right_label: str, combos: tuple[Counter[str], ...]) -> bool:
    return any(trail_possible(combo, left_label, right_label) for combo in combos)


def ccw_sector_angle(left_vector: exact.KPoint, right_vector: exact.KPoint) -> float:
    left_x, left_y = kpoint_float(left_vector)
    right_x, right_y = kpoint_float(right_vector)
    left_angle = math.atan2(left_y, left_x)
    right_angle = math.atan2(right_y, right_x)
    if right_angle <= left_angle:
        right_angle += 2 * math.pi
    return right_angle - left_angle


def kpoint_add(left: exact.KPoint, right: exact.KPoint) -> exact.KPoint:
    return exact.kadd(left[0], right[0]), exact.kadd(left[1], right[1])


def direction_sector_index(
    direction: exact.KPoint,
    ordered_half_edges: tuple[tuple[str, exact.KPoint], ...],
) -> int | None:
    for index, (_left_label, left_vector) in enumerate(ordered_half_edges):
        _right_label, right_vector = ordered_half_edges[(index + 1) % len(ordered_half_edges)]
        left_cmp = compare_incident_half_edges(("", left_vector), ("", direction))
        right_cmp = compare_incident_half_edges(("", direction), ("", right_vector))
        if index + 1 < len(ordered_half_edges):
            if left_cmp < 0 and right_cmp < 0:
                return index
        elif left_cmp < 0 or right_cmp < 0:
            return index
    return None


def occupied_sector_indices(
    vertex: exact.KPoint,
    ordered_half_edges: tuple[tuple[str, exact.KPoint], ...],
    unique: tuple[exact.IntegerQuadraticTile, ...],
) -> set[int]:
    occupied: set[int] = set()
    for tile in unique:
        polygon = tile.polygon
        for index, point in enumerate(polygon):
            if point == vertex:
                previous_vector = exact.kpsub(polygon[index - 1], vertex)
                next_vector = exact.kpsub(polygon[(index + 1) % 3], vertex)
                interior_direction = kpoint_add(previous_vector, next_vector)
                sector_index = direction_sector_index(interior_direction, ordered_half_edges)
                if sector_index is not None:
                    occupied.add(sector_index)
        for index in range(3):
            start = polygon[index]
            end = polygon[(index + 1) % 3]
            if vertex == start or vertex == end:
                continue
            if exact.kpoint_on_segment(vertex, start, end):
                opposite = polygon[(index + 2) % 3]
                interior_direction = exact.kpsub(opposite, vertex)
                sector_index = direction_sector_index(interior_direction, ordered_half_edges)
                if sector_index is not None:
                    occupied.add(sector_index)
    return occupied


def pinch_sector_profile(
    residual_labels: dict[exact.KSegment, str],
    unique: tuple[exact.IntegerQuadraticTile, ...],
    sides: tuple[int, int, int],
) -> tuple[int, int, CounterTuple]:
    incidences: dict[exact.KPoint, list[tuple[str, exact.KPoint]]] = defaultdict(list)
    for (start, end), label in residual_labels.items():
        incidences[start].append((label, exact.kpsub(end, start)))
        incidences[end].append((label, exact.kpsub(start, end)))
    signatures: Counter[str] = Counter()
    residual_sectors = 0
    unfillable = 0
    for vertex, half_edges in incidences.items():
        if len(half_edges) == 2:
            continue
        ordered = tuple(sorted(half_edges, key=cmp_to_key(compare_incident_half_edges)))
        occupied = occupied_sector_indices(vertex, ordered, unique)
        for index, (left_label, left_vector) in enumerate(ordered):
            right_label, right_vector = ordered[(index + 1) % len(ordered)]
            if index in occupied:
                continue
            residual_sectors += 1
            sector_angle = ccw_sector_angle(left_vector, right_vector)
            combos = sector_angle_combos(sector_angle, sides)
            fillable = sector_fillable(left_label, right_label, combos)
            if not fillable:
                unfillable += 1
            combo_text = "/".join(angle_counter_text(combo) for combo in combos) if combos else "unclassified"
            status = "ok" if fillable else "bad"
            signatures[f"{left_label}{right_label}:{combo_text}:{status}"] += 1
    return residual_sectors, unfillable, tuple(sorted(signatures.items()))


def kneg(value: exact.KQuad) -> exact.KQuad:
    return -value[0], -value[1]


def kabs(value: exact.KQuad) -> exact.KQuad:
    return kneg(value) if exact.ksign(value) < 0 else value


def kquad_ratio(left: exact.KQuad, right: exact.KQuad) -> tuple[Fraction, Fraction] | None:
    denominator = right[0] * right[0] - right[1] * right[1] * exact.RADICAND
    if denominator == 0:
        return None
    rational = Fraction(left[0] * right[0] - left[1] * right[1] * exact.RADICAND, denominator)
    radical = Fraction(left[1] * right[0] - left[0] * right[1], denominator)
    return rational, radical


def possible_vertex_pairings(
    vertex: exact.KPoint,
    neighbors: list[tuple[exact.KPoint, str]],
) -> tuple[dict[exact.KPoint, exact.KPoint], ...]:
    if len(neighbors) == 2:
        first = neighbors[0][0]
        second = neighbors[1][0]
        return ({first: second, second: first},)
    if len(neighbors) != 4:
        return ()
    half_edges = tuple((label, exact.kpsub(neighbor, vertex), neighbor) for neighbor, label in neighbors)
    ordered = tuple(sorted(half_edges, key=cmp_to_key(lambda left, right: compare_incident_half_edges((left[0], left[1]), (right[0], right[1])))))
    cyclic_neighbors = tuple(neighbor for _label, _vector, neighbor in ordered)
    first = {
        cyclic_neighbors[0]: cyclic_neighbors[1],
        cyclic_neighbors[1]: cyclic_neighbors[0],
        cyclic_neighbors[2]: cyclic_neighbors[3],
        cyclic_neighbors[3]: cyclic_neighbors[2],
    }
    second = {
        cyclic_neighbors[1]: cyclic_neighbors[2],
        cyclic_neighbors[2]: cyclic_neighbors[1],
        cyclic_neighbors[3]: cyclic_neighbors[0],
        cyclic_neighbors[0]: cyclic_neighbors[3],
    }
    return first, second


def split_cycles_for_pairing(
    residual_labels: dict[exact.KSegment, str],
    pairing: dict[exact.KPoint, dict[exact.KPoint, exact.KPoint]],
) -> tuple[tuple[list[exact.KPoint], list[exact.KSegment]], ...] | None:
    unused = set(residual_labels)
    cycles: list[tuple[list[exact.KPoint], list[exact.KSegment]]] = []
    while unused:
        start_segment = next(iter(unused))
        start, current = start_segment
        previous = start
        vertices = [start]
        segments: list[exact.KSegment] = []
        seen_in_cycle: set[exact.KSegment] = set()
        while True:
            segment = canonical_segment(previous, current)
            if segment not in residual_labels:
                return None
            if segment in seen_in_cycle:
                return None
            seen_in_cycle.add(segment)
            segments.append(segment)
            vertices.append(current)
            next_vertex = pairing.get(current, {}).get(previous)
            if next_vertex is None:
                return None
            previous, current = current, next_vertex
            if previous == start and current == vertices[1]:
                break
            if len(segments) > len(residual_labels):
                return None
        for segment in seen_in_cycle:
            unused.discard(segment)
        cycles.append((vertices[:-1], segments))
    return tuple(cycles)


def component_area_tiles(
    vertices: list[exact.KPoint],
    tile_area2: exact.KQuad,
) -> Fraction | None:
    area2 = kabs(exact.ksigned_area2(tuple(vertices)))
    ratio = kquad_ratio(area2, tile_area2)
    if ratio is None:
        return None
    rational, radical = ratio
    if radical != 0:
        return None
    return rational


def split_component_profile(
    residual_labels: dict[exact.KSegment, str],
    unique: tuple[exact.IntegerQuadraticTile, ...],
) -> tuple[int, int, CounterTuple]:
    graph: dict[exact.KPoint, list[tuple[exact.KPoint, str]]] = defaultdict(list)
    for (start, end), label in residual_labels.items():
        graph[start].append((end, label))
        graph[end].append((start, label))

    vertex_options: list[tuple[exact.KPoint, tuple[dict[exact.KPoint, exact.KPoint], ...]]] = []
    for vertex, neighbors in graph.items():
        options = possible_vertex_pairings(vertex, neighbors)
        if not options:
            return 0, 0, (("unsupported-degree", 1),)
        vertex_options.append((vertex, options))

    tile_area2 = kabs(exact.ksigned_area2(unique[0].polygon))
    total_options = 0
    pass_options = 0
    failures: Counter[str] = Counter()
    for choices in product(*(options for _vertex, options in vertex_options)):
        total_options += 1
        pairing = {vertex: choice for (vertex, _options), choice in zip(vertex_options, choices)}
        cycles = split_cycles_for_pairing(residual_labels, pairing)
        if cycles is None:
            failures["bad-cycle-split"] += 1
            continue
        option_ok = True
        for vertices, segments in cycles:
            area_tiles = component_area_tiles(vertices, tile_area2)
            if area_tiles is None or area_tiles.denominator != 1 or area_tiles <= 0:
                failures["nonintegral-area"] += 1
                option_ok = False
                break
            tile_count = area_tiles.numerator
            label_counts = Counter(residual_labels[segment] for segment in segments)
            if any(label_counts[label] > tile_count for label in ("a", "b", "c")):
                failures["too-many-boundary-sides"] += 1
                option_ok = False
                break
            if any(label_counts[label] % 2 != tile_count % 2 for label in ("a", "b", "c")):
                failures["side-parity"] += 1
                option_ok = False
                break
        if option_ok:
            pass_options += 1
    return total_options, pass_options, tuple(sorted(failures.items()))


def segment_length(segment: exact.KSegment, scale: int):
    length_sq = exact.knorm_sq(exact.kpsub(segment[1], segment[0]))
    if length_sq[1] != 0:
        return None
    return exact.sqrt_fraction(Fraction(length_sq[0], scale * scale))


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
    pinch_profile = pinch_label_profile(residual_labels)
    cyclic_pinch_profile = pinch_cyclic_label_profile(residual_labels)
    residual_sector_count, unfillable_sector_count, sector_profile = pinch_sector_profile(
        residual_labels,
        unique,
        survivor.candidate.tile,
    )
    split_options, split_pass_options, split_failures = split_component_profile(residual_labels, unique)
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
            pinch_labels=pinch_profile,
            pinch_cyclic_labels=cyclic_pinch_profile,
            pinch_residual_sectors=residual_sector_count,
            pinch_unfillable_sectors=unfillable_sector_count,
            pinch_sector_signatures=sector_profile,
            split_options=split_options,
            split_component_pass_options=split_pass_options,
            split_failure_reasons=split_failures,
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
            pinch_labels=pinch_profile,
            pinch_cyclic_labels=cyclic_pinch_profile,
            pinch_residual_sectors=residual_sector_count,
            pinch_unfillable_sectors=unfillable_sector_count,
            pinch_sector_signatures=sector_profile,
            split_options=split_options,
            split_component_pass_options=split_pass_options,
            split_failure_reasons=split_failures,
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
        pinch_labels=pinch_profile,
        pinch_cyclic_labels=cyclic_pinch_profile,
        pinch_residual_sectors=residual_sector_count,
        pinch_unfillable_sectors=unfillable_sector_count,
        pinch_sector_signatures=sector_profile,
        split_options=split_options,
        split_component_pass_options=split_pass_options,
        split_failure_reasons=split_failures,
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
            pinch_label_counts: Counter[str] = Counter()
            pinch_shell_profiles: Counter[CounterTuple] = Counter()
            cyclic_pinch_label_counts: Counter[str] = Counter()
            cyclic_pinch_shell_profiles: Counter[CounterTuple] = Counter()
            pinch_sector_counts: Counter[str] = Counter()
            pinch_sector_shell_profiles: Counter[CounterTuple] = Counter()
            unfillable_sector_counts: Counter[tuple[int, int]] = Counter()
            split_pass_counts: Counter[tuple[int, int]] = Counter()
            split_failure_counts: Counter[str] = Counter()
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
                    pinch_shell_profiles[detail.pinch_labels] += 1
                    for labels, count in detail.pinch_labels:
                        pinch_label_counts[labels] += count
                    cyclic_pinch_shell_profiles[detail.pinch_cyclic_labels] += 1
                    for labels, count in detail.pinch_cyclic_labels:
                        cyclic_pinch_label_counts[labels] += count
                    pinch_sector_shell_profiles[detail.pinch_sector_signatures] += 1
                    unfillable_sector_counts[(detail.pinch_residual_sectors, detail.pinch_unfillable_sectors)] += 1
                    for signature, count in detail.pinch_sector_signatures:
                        pinch_sector_counts[signature] += count
                    split_pass_counts[(detail.split_options, detail.split_component_pass_options)] += 1
                    for reason, count in detail.split_failure_reasons:
                        split_failure_counts[reason] += count
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
            print("  top non-simple pinch label profiles:")
            for profile, count in pinch_shell_profiles.most_common(args.top):
                print(f"    {counter_tuple_text(profile)}: {count}")
            print("  top non-2-degree vertex incident labels:")
            for labels, count in pinch_label_counts.most_common(args.top):
                print(f"    {labels}: {count}")
            print("  top non-simple cyclic pinch label profiles:")
            for profile, count in cyclic_pinch_shell_profiles.most_common(args.top):
                print(f"    {counter_tuple_text(profile)}: {count}")
            print("  top non-2-degree vertex cyclic incident labels:")
            for labels, count in cyclic_pinch_label_counts.most_common(args.top):
                print(f"    {labels}: {count}")
            print("  non-simple residual-sector fillability counts:")
            for (sectors, bad), count in sorted(unfillable_sector_counts.items()):
                print(f"    residual_sectors={sectors}, unfillable={bad}: {count}")
            print("  top non-simple pinch sector profiles:")
            for profile, count in pinch_sector_shell_profiles.most_common(args.top):
                print(f"    {counter_tuple_text(profile)}: {count}")
            print("  top non-simple pinch sector signatures:")
            for signature, count in pinch_sector_counts.most_common(args.top):
                print(f"    {signature}: {count}")
            print("  non-simple split component pass counts:")
            for (options, pass_options), count in sorted(split_pass_counts.items()):
                print(f"    options={options}, pass={pass_options}: {count}")
            print("  non-simple split component failure reasons:")
            for reason, count in split_failure_counts.most_common(args.top):
                print(f"    {reason}: {count}")
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
