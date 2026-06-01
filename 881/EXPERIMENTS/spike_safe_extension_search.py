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
        "one_point_candidate_count": len(one_point_candidates),
        "one_point_reflected_blocked_count": (
            len(one_point_candidates) - len(unblocked)
        ),
        "one_point_unblocked_examples": unblocked[:20],
        "two_new_pairs_blocked_by_defect": defect in state.retained,
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


def seed_state(cap: int, scale: int) -> tuple[State, set[int], int, dict[str, object]]:
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
    upper_stop = 15 * scale
    dangerous_middle_complement = witness - 2 * 43 * scale
    upper_band = set(range(upper_start, upper_stop + 1))
    upper_band.discard(dangerous_middle_complement)

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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=int, default=100)
    parser.add_argument("--target", type=int, default=None)
    parser.add_argument("--cap", type=int, default=None)
    parser.add_argument("--beam", type=int, default=8)
    parser.add_argument("--steps", type=int, default=400)
    parser.add_argument("--allow-pairs", action="store_true")
    args = parser.parse_args()

    cap = args.cap if args.cap is not None else 100 * args.scale
    target = args.target if args.target is not None else 100 * args.scale
    state, deleted, witness, metadata = seed_state(cap, args.scale)
    beam = [state]
    best = state
    stalled_at: int | None = None

    for step in range(1, args.steps + 1):
        next_beam: list[State] = []
        for item in beam:
            next_beam.extend(
                candidate_extensions(
                    item,
                    deleted,
                    witness,
                    cap,
                    max(args.beam * 2, 1),
                    args.allow_pairs,
                )
            )
        if not next_beam:
            stalled_at = step
            break
        dedup: dict[tuple[int, tuple[int, ...]], State] = {}
        for item in next_beam:
            key = (item.cover_end, item.added[-8:])
            if key not in dedup or len(item.added) < len(dedup[key].added):
                dedup[key] = item
        beam = sorted(
            dedup.values(),
            key=lambda item: (item.cover_end, -len(item.added)),
            reverse=True,
        )[: args.beam]
        if beam[0].cover_end > best.cover_end:
            best = beam[0]
        if best.cover_end >= target:
            break

    final_gap = best.cover_end + 1
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
    print(f"initial_cover={state.cover_end}")
    print(f"best_cover={best.cover_end}")
    print(f"reached_target={best.cover_end >= target}")
    print(f"stalled_at_step={stalled_at}")
    print(f"added_count={len(best.added)}")
    print(f"added_tail={best.added[-30:]}")
    print(f"next_gap={final_gap}")
    print(f"unsafe_blockers_for_next_gap={blockers[:30]}")
    print(f"unsafe_blocker_count={len(blockers)}")
    print(f"unsafe_reason_counts={reason_counts}")
    print(f"unsafe_blocker_examples={blocker_examples[:20]}")
    two_batches = safe_two_point_gap_batches(
        best, deleted, witness, final_gap, limit=20
    )
    print(f"safe_two_point_batches_for_next_gap={two_batches}")
    print(f"safe_two_point_batch_count_reported={len(two_batches)}")
    print(
        "reflected_next_gap_blocker="
        f"{reflected_next_gap_blocker(best, deleted, witness, final_gap)}"
    )

    if any(witness - retained in best.retained_pair_sums for retained in best.retained):
        raise AssertionError("witness repaired in retained three-sum")


if __name__ == "__main__":
    main()
