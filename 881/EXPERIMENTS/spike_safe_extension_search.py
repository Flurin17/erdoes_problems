#!/usr/bin/env python3
"""Try to extend safe spike fillers toward a frozen witness.

Starting from the safe filler profile, greedily adds retained fillers or
optional two-point retained batches so that the full set A=C union F has a
longer initial two-sum interval, while the protected witness stays outside
3C.  This is a finite diagnostic for the stage obstruction after Corollary
8.5a.7z.12d, not a construction.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    retained: frozenset[int]
    full_pair_sums: frozenset[int]
    retained_pair_sums: frozenset[int]
    cover_end: int
    added: tuple[int, ...]


def pair_sums(elements: set[int], cap: int) -> set[int]:
    values = sorted(elements)
    out: set[int] = set()
    for i, first in enumerate(values):
        for second in values[i:]:
            total = first + second
            if total > cap:
                break
            out.add(total)
    return out


def cover_end(sums: set[int] | frozenset[int], start: int, cap: int) -> int:
    point = start
    while point <= cap and point in sums:
        point += 1
    return point - 1


def safe_to_add(
    retained: frozenset[int],
    retained_pair_sums: frozenset[int],
    candidate: int,
    witness: int,
) -> bool:
    if candidate in retained:
        return False
    if witness - candidate in retained_pair_sums:
        return False
    if witness - 2 * candidate in retained:
        return False
    if 3 * candidate == witness:
        return False
    return True


def unsafe_reasons(
    retained: frozenset[int],
    retained_pair_sums: frozenset[int],
    candidate: int,
    witness: int,
) -> list[str]:
    reasons: list[str] = []
    if witness - candidate in retained_pair_sums:
        reasons.append("candidate_plus_retained_pair")
    if witness - 2 * candidate in retained:
        reasons.append("double_candidate_plus_retained")
    if 3 * candidate == witness:
        reasons.append("triple_candidate")
    return reasons


def safe_batch(
    retained: frozenset[int],
    retained_pair_sums: frozenset[int],
    batch: tuple[int, ...],
    witness: int,
) -> bool:
    if len(set(batch)) != len(batch):
        return False
    if any(not safe_to_add(retained, retained_pair_sums, item, witness) for item in batch):
        return False
    retained_set = set(retained)
    for i, first in enumerate(batch):
        for second in batch[i:]:
            if witness - first - second in retained_set:
                return False
    for i, first in enumerate(batch):
        for j in range(i, len(batch)):
            second = batch[j]
            for third in batch[j:]:
                if first + second + third == witness:
                    return False
    return True


def safe_two_point_gap_batches(
    state: State,
    deleted: set[int],
    witness: int,
    gap: int,
    limit: int,
) -> list[tuple[int, int]]:
    full = set(state.retained) | deleted
    batches: list[tuple[int, int]] = []
    for first in range(1, gap // 2 + 1):
        second = gap - first
        if first in full or second in full:
            continue
        if first == second:
            continue
        batch = (first, second)
        if safe_batch(state.retained, state.retained_pair_sums, batch, witness):
            batches.append(batch)
            if len(batches) >= limit:
                break
    return batches


def count_safe_two_point_gap_batches(
    state: State,
    deleted: set[int],
    witness: int,
    gap: int,
) -> int:
    full = set(state.retained) | deleted
    count = 0
    for first in range(1, gap // 2 + 1):
        second = gap - first
        if first in full or second in full:
            continue
        if first == second:
            continue
        if safe_batch(state.retained, state.retained_pair_sums, (first, second), witness):
            count += 1
    return count


def count_safe_one_point_gap_extensions(
    state: State,
    deleted: set[int],
    witness: int,
    gap: int,
) -> int:
    full = set(state.retained) | deleted
    raw_candidates = {gap - old for old in full if gap - old > 0}
    if gap % 2 == 0:
        raw_candidates.add(gap // 2)
    raw_candidates -= full
    return sum(
        1
        for candidate in raw_candidates
        if safe_to_add(state.retained, state.retained_pair_sums, candidate, witness)
    )


def reflected_next_gap_blocker(
    state: State,
    deleted: set[int],
    witness: int,
    gap: int,
) -> dict[str, object]:
    full = set(state.retained) | deleted
    defect = witness - gap
    one_point_candidates: list[tuple[int, int]] = []
    unblocked: list[tuple[int, int, int]] = []
    for old in sorted(full):
        candidate = gap - old
        if candidate <= 0 or candidate in full:
            continue
        one_point_candidates.append((old, candidate))
        reflected_target = defect + old
        if reflected_target not in state.retained_pair_sums:
            unblocked.append((old, candidate, reflected_target))
    return {
        "defect": defect,
        "defect_retained": defect in state.retained,
        "deleted_gate_reflections": {
            gate: defect + gate in state.retained_pair_sums for gate in sorted(deleted)
        },
        "one_point_candidate_count": len(one_point_candidates),
        "one_point_reflected_blocked_count": (
            len(one_point_candidates) - len(unblocked)
        ),
        "one_point_unblocked_examples": unblocked[:20],
        "two_new_pairs_blocked_by_defect": defect in state.retained,
    }


def has_reflected_next_gap_blocker(
    state: State,
    deleted: set[int],
    witness: int,
) -> bool:
    gap = state.cover_end + 1
    certificate = reflected_next_gap_blocker(state, deleted, witness, gap)
    return (
        bool(certificate["defect_retained"])
        and certificate["one_point_candidate_count"]
        == certificate["one_point_reflected_blocked_count"]
    )


def one_sided_pair_saturation_blocker(
    state: State,
    deleted: set[int],
    witness: int,
    gap: int,
) -> dict[str, object]:
    full = set(state.retained) | deleted
    one_point_candidates = {gap - old for old in full if gap - old > 0}
    if gap % 2 == 0:
        one_point_candidates.add(gap // 2)
    one_point_candidates -= full
    one_point_unsaturated = sorted(
        candidate
        for candidate in one_point_candidates
        if witness - candidate not in state.retained_pair_sums
    )

    split_count = 0
    split_saturated_count = 0
    split_unsaturated: list[tuple[int, int]] = []
    for first in range(1, gap // 2 + 1):
        second = gap - first
        if first == second:
            continue
        if first in full or second in full:
            continue
        split_count += 1
        if (
            witness - first in state.retained_pair_sums
            or witness - second in state.retained_pair_sums
        ):
            split_saturated_count += 1
        else:
            split_unsaturated.append((first, second))

    return {
        "one_point_candidate_count": len(one_point_candidates),
        "one_point_saturated_count": (
            len(one_point_candidates) - len(one_point_unsaturated)
        ),
        "one_point_unsaturated_examples": one_point_unsaturated[:20],
        "two_point_split_count": split_count,
        "two_point_split_saturated_count": split_saturated_count,
        "two_point_unsaturated_examples": split_unsaturated[:20],
        "blocks_all_one_and_two_point_repairs": (
            not one_point_unsaturated
            and split_count == split_saturated_count
        ),
    }


def shadow_translation_summary(
    state: State,
    deleted: set[int],
    witness: int,
    gap: int,
) -> dict[str, object]:
    full = set(state.retained) | deleted
    defect = witness - gap
    deleted_retained_reps = [
        (gate, defect - gate)
        for gate in sorted(deleted)
        if defect - gate in state.retained
    ]
    deleted_deleted_reps = [
        (first, second)
        for first in sorted(deleted)
        for second in sorted(deleted)
        if first <= second and first + second == defect
    ]
    rows: list[int] = []
    for old in sorted(full):
        candidate = gap - old
        if (
            candidate > 0
            and candidate not in full
            and witness - candidate in state.retained_pair_sums
        ):
            rows.append(old)
    retained_rows = [row for row in rows if row in state.retained]
    deleted_rows = [row for row in rows if row in deleted]
    return {
        "defect": defect,
        "defect_in_retained": defect in state.retained,
        "defect_in_deleted": defect in deleted,
        "defect_in_2retained": defect in state.retained_pair_sums,
        "defect_deleted_retained_reps": deleted_retained_reps[:20],
        "defect_deleted_deleted_reps": deleted_deleted_reps,
        "saturated_old_row_count": len(rows),
        "saturated_retained_row_count": len(retained_rows),
        "saturated_deleted_row_count": len(deleted_rows),
        "saturated_row_examples": rows[:20],
        "saturated_row_tail": rows[-20:],
    }


def shadow_escape_set_summary(
    state: State,
    deleted: set[int],
    witness: int,
    gap: int,
) -> dict[str, object]:
    full = set(state.retained) | deleted
    defect = witness - gap
    old_row_escapes = []
    for old in sorted(full):
        candidate = gap - old
        if (
            candidate > 0
            and candidate not in full
            and defect + old not in state.retained_pair_sums
        ):
            old_row_escapes.append((old, candidate))

    split_escape_set = [
        item
        for item in range(1, gap)
        if item not in full and defect + item not in state.retained_pair_sums
    ]
    split_escape_lookup = set(split_escape_set)
    complementary_pairs = [
        (first, gap - first)
        for first in split_escape_set
        if first < gap - first and gap - first in split_escape_lookup
    ]
    low_split_escapes = [item for item in split_escape_set if 2 * item < gap]
    low_complement_in_full = [
        item for item in low_split_escapes if gap - item in full
    ]
    low_complement_absorbed = [
        item
        for item in low_split_escapes
        if gap - item not in full and gap - item not in split_escape_lookup
    ]
    half_candidate = gap % 2 == 0 and gap // 2 not in full
    return {
        "defect": defect,
        "old_row_escape_count": len(old_row_escapes),
        "old_row_escape_examples": old_row_escapes[:20],
        "split_escape_set_count": len(split_escape_set),
        "low_split_escape_count": len(low_split_escapes),
        "low_complement_in_full_count": len(low_complement_in_full),
        "low_complement_absorbed_count": len(low_complement_absorbed),
        "low_split_escape_examples": low_split_escapes[:20],
        "split_escape_examples": split_escape_set[:20],
        "split_escape_tail": split_escape_set[-20:],
        "complementary_escape_pair_count": len(complementary_pairs),
        "complementary_escape_pair_examples": complementary_pairs[:20],
        "half_candidate": half_candidate,
        "half_candidate_saturated": (
            half_candidate and defect + gap // 2 in state.retained_pair_sums
        ),
        "half_candidate_double_defect_retained": (
            half_candidate and defect in state.retained
        ),
    }


def add_retained_batch(
    state: State,
    deleted: set[int],
    batch: tuple[int, ...],
    cap: int,
) -> State:
    retained = set(state.retained)
    new_retained_pairs = set(state.retained_pair_sums)
    new_full_pairs = set(state.full_pair_sums)

    for candidate in batch:
        for old in retained:
            total = old + candidate
            if total <= cap:
                new_retained_pairs.add(total)
                new_full_pairs.add(total)
        for old in deleted:
            total = old + candidate
            if total <= cap:
                new_full_pairs.add(total)

    for index, first in enumerate(batch):
        for second in batch[index:]:
            total = first + second
            if total <= cap:
                new_retained_pairs.add(total)
                new_full_pairs.add(total)

    retained.update(batch)
    new_cover = cover_end(new_full_pairs, 2, cap)
    return State(
        retained=frozenset(retained),
        full_pair_sums=frozenset(new_full_pairs),
        retained_pair_sums=frozenset(new_retained_pairs),
        cover_end=new_cover,
        added=state.added + batch,
    )


def add_retained(
    state: State,
    deleted: set[int],
    candidate: int,
    cap: int,
) -> State:
    return add_retained_batch(state, deleted, (candidate,), cap)


def seed_state(
    cap: int,
    scale: int,
    upper_stop: int | None = None,
    upper_policy: str = "interval",
) -> tuple[State, set[int], int, dict[str, object]]:
    shift = 7
    rows = {1, 4, 9, 16, 25, 36}
    witness = 100 * scale
    f = 10 * scale + shift
    g = 10 * scale
    k = 20 * scale
    deleted = {f, g, k}

    mirrors = {90 * scale - shift - row for row in rows}
    shifted = {row + shift for row in rows}
    repairs = {37 * scale, 43 * scale}
    base_retained = rows | shifted | mirrors | repairs

    private_sums = {f + row for row in rows}
    low_radius = (min(private_sums) - 1) // 2
    low_band = set(range(1, low_radius + 1))
    upper_start = max(private_sums) + 1
    if upper_stop is None:
        upper_stop = 15 * scale
    dangerous_middle_complement = witness - 2 * 43 * scale
    upper_candidates = [
        item for item in range(upper_start, upper_stop + 1) if item not in deleted
    ]
    if upper_policy == "interval":
        upper_band = set(upper_candidates)
        upper_band.discard(dangerous_middle_complement)
    elif upper_policy == "greedy-safe":
        upper_band = set()
        retained_so_far = set(base_retained | low_band)
        retained_pairs_so_far = pair_sums(retained_so_far, witness)
        for candidate in upper_candidates:
            if candidate == dangerous_middle_complement:
                continue
            if safe_to_add(
                frozenset(retained_so_far),
                frozenset(retained_pairs_so_far),
                candidate,
                witness,
            ):
                upper_band.add(candidate)
                for old in retained_so_far:
                    total = old + candidate
                    if total <= witness:
                        retained_pairs_so_far.add(total)
                double = candidate + candidate
                if double <= witness:
                    retained_pairs_so_far.add(double)
                retained_so_far.add(candidate)
    else:
        raise ValueError(f"unknown upper_policy: {upper_policy}")

    retained = base_retained | low_band | upper_band
    full = retained | deleted
    full_pairs = pair_sums(full, cap)
    retained_pairs = pair_sums(retained, witness)
    state = State(
        retained=frozenset(retained),
        full_pair_sums=frozenset(full_pairs),
        retained_pair_sums=frozenset(retained_pairs),
        cover_end=cover_end(full_pairs, 2, cap),
        added=(),
    )
    metadata = {
        "scale": scale,
        "shift": shift,
        "rows": sorted(rows),
        "private_sums": sorted(private_sums),
        "low_band": (1, low_radius),
        "upper_band": (upper_start, upper_stop),
        "upper_policy": upper_policy,
        "upper_band_size": len(upper_band),
        "removed_from_upper_band": dangerous_middle_complement,
    }
    return state, deleted, witness, metadata


def candidate_extensions(
    state: State,
    deleted: set[int],
    witness: int,
    cap: int,
    max_candidates: int,
    allow_pairs: bool,
) -> list[State]:
    full = set(state.retained) | deleted
    gap = state.cover_end + 1
    raw_candidates = {gap - old for old in full if gap - old > 0}
    if gap % 2 == 0:
        raw_candidates.add(gap // 2)
    raw_candidates -= full
    safe = [
        candidate
        for candidate in raw_candidates
        if safe_to_add(state.retained, state.retained_pair_sums, candidate, witness)
    ]
    extensions = [add_retained(state, deleted, candidate, cap) for candidate in safe]
    if allow_pairs:
        gap_batches = safe_two_point_gap_batches(
            state, deleted, witness, gap, limit=max_candidates
        )
        extensions.extend(
            add_retained_batch(state, deleted, batch, cap)
            for batch in gap_batches
        )
    extensions.sort(key=lambda item: (item.cover_end, -len(item.retained)), reverse=True)
    return extensions[:max_candidates]


def run_beam_search(
    state: State,
    deleted: set[int],
    witness: int,
    cap: int,
    target: int,
    beam_size: int,
    steps: int,
    allow_pairs: bool,
    avoid_reflected_blockers: bool,
) -> tuple[State, int | None, int, int]:
    beam = [state]
    best = state
    stalled_at: int | None = None
    last_raw_extension_count = 0
    last_filtered_extension_count = 0

    for step in range(1, steps + 1):
        next_beam: list[State] = []
        for item in beam:
            raw_extensions = candidate_extensions(
                item,
                deleted,
                witness,
                cap,
                max(beam_size * 2, 1),
                allow_pairs,
            )
            last_raw_extension_count += len(raw_extensions)
            if avoid_reflected_blockers:
                raw_extensions = [
                    extension
                    for extension in raw_extensions
                    if not has_reflected_next_gap_blocker(
                        extension, deleted, witness
                    )
                ]
            last_filtered_extension_count += len(raw_extensions)
            next_beam.extend(raw_extensions)
        if not next_beam:
            stalled_at = step
            break
        last_raw_extension_count = 0
        last_filtered_extension_count = 0
        dedup: dict[tuple[int, tuple[int, ...]], State] = {}
        for item in next_beam:
            key = (item.cover_end, item.added[-8:])
            if key not in dedup or len(item.added) < len(dedup[key].added):
                dedup[key] = item
        beam = sorted(
            dedup.values(),
            key=lambda item: (item.cover_end, -len(item.added)),
            reverse=True,
        )[:beam_size]
        if beam[0].cover_end > best.cover_end:
            best = beam[0]
        if best.cover_end >= target:
            break

    return best, stalled_at, last_raw_extension_count, last_filtered_extension_count


def print_upper_stop_sweep(args: argparse.Namespace, cap: int, target: int) -> None:
    print(
        "upper_stop\tinitial\tbest\tgap\tstalled\td_retained\t"
        "reflected\tone_sided\tsplits\tsafe_one\tsafe_two"
    )
    for upper_stop in args.sweep_upper_stops:
        state, deleted, witness, _metadata = seed_state(
            cap, args.scale, upper_stop, args.upper_policy
        )
        best, stalled_at, _raw_count, _filtered_count = run_beam_search(
            state,
            deleted,
            witness,
            cap,
            target,
            args.beam,
            args.steps,
            args.allow_pairs,
            args.avoid_reflected_blockers,
        )
        gap = best.cover_end + 1
        reflected = reflected_next_gap_blocker(best, deleted, witness, gap)
        saturated = one_sided_pair_saturation_blocker(best, deleted, witness, gap)
        safe_one_count = count_safe_one_point_gap_extensions(
            best, deleted, witness, gap
        )
        safe_two_count = count_safe_two_point_gap_batches(
            best, deleted, witness, gap
        )
        reflected_ratio = (
            f"{reflected['one_point_reflected_blocked_count']}/"
            f"{reflected['one_point_candidate_count']}"
        )
        split_ratio = (
            f"{saturated['two_point_split_saturated_count']}/"
            f"{saturated['two_point_split_count']}"
        )
        print(
            "\t".join(
                str(item)
                for item in (
                    upper_stop,
                    state.cover_end,
                    best.cover_end,
                    gap,
                    stalled_at,
                    reflected["defect_retained"],
                    reflected_ratio,
                    saturated["blocks_all_one_and_two_point_repairs"],
                    split_ratio,
                    safe_one_count,
                    safe_two_count,
                )
            )
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=int, default=100)
    parser.add_argument("--target", type=int, default=None)
    parser.add_argument("--cap", type=int, default=None)
    parser.add_argument("--beam", type=int, default=8)
    parser.add_argument("--steps", type=int, default=400)
    parser.add_argument("--allow-pairs", action="store_true")
    parser.add_argument("--avoid-reflected-blockers", action="store_true")
    parser.add_argument("--upper-stop", type=int, default=None)
    parser.add_argument(
        "--upper-policy",
        choices=("interval", "greedy-safe"),
        default="interval",
    )
    parser.add_argument("--sweep-upper-stops", type=int, nargs="+")
    args = parser.parse_args()

    cap = args.cap if args.cap is not None else 100 * args.scale
    target = args.target if args.target is not None else 100 * args.scale
    if args.sweep_upper_stops:
        print_upper_stop_sweep(args, cap, target)
        return

    state, deleted, witness, metadata = seed_state(
        cap, args.scale, args.upper_stop, args.upper_policy
    )
    best, stalled_at, last_raw_extension_count, last_filtered_extension_count = (
        run_beam_search(
            state,
            deleted,
            witness,
            cap,
            target,
            args.beam,
            args.steps,
            args.allow_pairs,
            args.avoid_reflected_blockers,
        )
    )

    final_gap = best.cover_end + 1
    final_defect = witness - final_gap
    full = set(best.retained) | deleted
    blockers = sorted(
        candidate
        for candidate in {final_gap - old for old in full if final_gap - old > 0}
        if candidate not in full
        and not safe_to_add(best.retained, best.retained_pair_sums, candidate, witness)
    )
    reason_counts: dict[str, int] = {}
    blocker_examples: list[tuple[int, list[str]]] = []
    for blocker in blockers:
        reasons = unsafe_reasons(best.retained, best.retained_pair_sums, blocker, witness)
        blocker_examples.append((blocker, reasons))
        for reason in reasons:
            reason_counts[reason] = reason_counts.get(reason, 0) + 1

    print("spike safe extension search")
    print(f"metadata={metadata}")
    print(f"deleted={sorted(deleted)}")
    print(f"witness={witness}")
    print(f"target={target} cap={cap} beam={args.beam} steps={args.steps}")
    print(f"allow_pairs={args.allow_pairs}")
    print(f"avoid_reflected_blockers={args.avoid_reflected_blockers}")
    print(f"initial_cover={state.cover_end}")
    print(f"best_cover={best.cover_end}")
    print(f"reached_target={best.cover_end >= target}")
    print(f"stalled_at_step={stalled_at}")
    print(f"last_raw_extension_count={last_raw_extension_count}")
    print(f"last_filtered_extension_count={last_filtered_extension_count}")
    print(f"added_count={len(best.added)}")
    print(f"added_tail={best.added[-30:]}")
    print(f"next_gap={final_gap}")
    if final_defect in state.retained:
        final_defect_origin = "initial_retained"
    elif final_defect in best.added:
        final_defect_origin = f"added_at_{best.added.index(final_defect) + 1}"
    else:
        final_defect_origin = "not_retained"
    print(f"final_defect={final_defect}")
    print(f"final_defect_origin={final_defect_origin}")
    print(f"unsafe_blockers_for_next_gap={blockers[:30]}")
    print(f"unsafe_blocker_count={len(blockers)}")
    print(f"unsafe_reason_counts={reason_counts}")
    print(f"unsafe_blocker_examples={blocker_examples[:20]}")
    two_batches = safe_two_point_gap_batches(
        best, deleted, witness, final_gap, limit=20
    )
    safe_one_count = count_safe_one_point_gap_extensions(
        best, deleted, witness, final_gap
    )
    safe_two_count = count_safe_two_point_gap_batches(
        best, deleted, witness, final_gap
    )
    no_finite_batch = safe_one_count == 0 and safe_two_count == 0
    print(f"safe_one_point_extension_count={safe_one_count}")
    print(f"safe_two_point_batch_count={safe_two_count}")
    print(f"safe_two_point_batches_for_next_gap={two_batches}")
    print(f"safe_two_point_batch_count_reported={len(two_batches)}")
    print(f"no_finite_batch_by_12e_prime={no_finite_batch}")
    print(
        "reflected_next_gap_blocker="
        f"{reflected_next_gap_blocker(best, deleted, witness, final_gap)}"
    )
    print(
        "one_sided_pair_saturation_blocker="
        f"{one_sided_pair_saturation_blocker(best, deleted, witness, final_gap)}"
    )
    print(
        "shadow_translation_summary="
        f"{shadow_translation_summary(best, deleted, witness, final_gap)}"
    )
    print(
        "shadow_escape_set_summary="
        f"{shadow_escape_set_summary(best, deleted, witness, final_gap)}"
    )

    if any(witness - retained in best.retained_pair_sums for retained in best.retained):
        raise AssertionError("witness repaired in retained three-sum")


if __name__ == "__main__":
    main()
