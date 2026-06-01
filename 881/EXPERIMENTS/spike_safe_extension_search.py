#!/usr/bin/env python3
"""Try to extend safe spike fillers toward a frozen witness.

Starting from the safe filler profile, greedily adds retained fillers so that
the full set A=C union F has a longer initial two-sum interval, while the
protected witness stays outside 3C.  This is a finite diagnostic for the
stage obstruction after Corollary 8.5a.7z.12d, not a construction.
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


def add_retained(
    state: State,
    deleted: set[int],
    candidate: int,
    cap: int,
) -> State:
    retained = set(state.retained)
    full = retained | deleted
    new_retained_pairs = set(state.retained_pair_sums)
    new_full_pairs = set(state.full_pair_sums)

    for old in retained:
        total = old + candidate
        if total <= cap:
            new_retained_pairs.add(total)
            new_full_pairs.add(total)
    double = 2 * candidate
    if double <= cap:
        new_retained_pairs.add(double)
        new_full_pairs.add(double)
    for old in deleted:
        total = old + candidate
        if total <= cap:
            new_full_pairs.add(total)

    retained.add(candidate)
    new_cover = cover_end(new_full_pairs, 2, cap)
    return State(
        retained=frozenset(retained),
        full_pair_sums=frozenset(new_full_pairs),
        retained_pair_sums=frozenset(new_retained_pairs),
        cover_end=new_cover,
        added=state.added + (candidate,),
    )


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
    extensions.sort(key=lambda item: (item.cover_end, -len(item.retained)), reverse=True)
    return extensions[:max_candidates]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=int, default=100)
    parser.add_argument("--target", type=int, default=None)
    parser.add_argument("--cap", type=int, default=None)
    parser.add_argument("--beam", type=int, default=8)
    parser.add_argument("--steps", type=int, default=400)
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
                    item, deleted, witness, cap, max(args.beam * 2, 1)
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

    if any(witness - retained in best.retained_pair_sums for retained in best.retained):
        raise AssertionError("witness repaired in retained three-sum")


if __name__ == "__main__":
    main()
