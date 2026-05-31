#!/usr/bin/env python3
"""Cycle-cactus DP for ordinary residue-flexible modular partitions.

This is the analogue of `cactus_signature_dp.py` for ordinary color
partitions.  For a fixed number of colors and a global residue assigned to
each color, a cycle-block signature records the colors of articulation
vertices and the same-color degree contribution supplied by the cycle.  The
DP patches signatures across the block-cut tree.
"""

from __future__ import annotations

import argparse
import random
from functools import lru_cache
from itertools import product

import cactus_signature_dp


Cycle = tuple[int, ...]


@lru_cache(maxsize=None)
def block_signatures(
    cycle_len: int,
    marked_positions: tuple[int, ...],
    colors: int,
    residues: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    marked_set = set(marked_positions)
    internal = [v for v in range(cycle_len) if v not in marked_set]
    out: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for marked_colors in product(range(colors), repeat=len(marked_positions)):
        color = [0] * cycle_len
        for vertex, value in zip(marked_positions, marked_colors):
            color[vertex] = value
        for internal_colors in product(range(colors), repeat=len(internal)):
            for vertex, value in zip(internal, internal_colors):
                color[vertex] = value
            ok = True
            for vertex in internal:
                degree = sum(
                    1
                    for neighbor in ((vertex - 1) % cycle_len, (vertex + 1) % cycle_len)
                    if color[neighbor] == color[vertex]
                )
                if degree % 4 != residues[color[vertex]]:
                    ok = False
                    break
            if not ok:
                continue
            contribution = tuple(
                sum(
                    1
                    for neighbor in ((vertex - 1) % cycle_len, (vertex + 1) % cycle_len)
                    if color[neighbor] == color[vertex]
                )
                for vertex in marked_positions
            )
            out.add((marked_colors, contribution))
    return tuple(sorted(out))


def cycle_signatures(
    cycle: Cycle,
    articulations: set[int],
    colors: int,
    residues: tuple[int, ...],
) -> list[tuple[dict[int, int], dict[int, int]]]:
    marked_positions = tuple(i for i, vertex in enumerate(cycle) if vertex in articulations)
    raw = block_signatures(len(cycle), marked_positions, colors, residues)
    if not marked_positions:
        return [({}, {})] if raw else []
    marked_vertices = tuple(cycle[i] for i in marked_positions)
    out: list[tuple[dict[int, int], dict[int, int]]] = []
    for marked_colors, contributions in raw:
        out.append((dict(zip(marked_vertices, marked_colors)), dict(zip(marked_vertices, contributions))))
    return out


def solve_with_residues(
    cycles: list[Cycle],
    colors: int,
    residues: tuple[int, ...],
) -> tuple[bool, list[int] | None]:
    articulations = cactus_signature_dp.articulation_vertices(cycles)
    signatures = [cycle_signatures(cycle, articulations, colors, residues) for cycle in cycles]
    if any(not sigs for sigs in signatures):
        return False, None
    order = sorted(range(len(cycles)), key=lambda i: len(signatures[i]))
    contribution = {vertex: 0 for vertex in articulations}
    color: dict[int, int] = {}
    chosen: list[int | None] = [None] * len(cycles)

    remaining_touch: list[set[int]] = []
    seen: set[int] = set()
    for idx in reversed(order):
        seen.update(v for v in cycles[idx] if v in articulations)
        remaining_touch.append(set(seen))
    remaining_touch = list(reversed(remaining_touch))

    failed: set[tuple[int, tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]] = set()

    def dfs(pos: int) -> bool:
        key = (
            pos,
            tuple(sorted(color.items())),
            tuple(sorted((v, contribution[v] % 4) for v in articulations if v in color)),
        )
        if key in failed:
            return False
        if pos == len(order):
            return all(contribution[v] % 4 == residues[color[v]] for v in articulations)

        idx = order[pos]
        future = remaining_touch[pos + 1] if pos + 1 < len(order) else set()
        for sig_index, (colors_at, contribs) in enumerate(signatures[idx]):
            changed_colors: list[int] = []
            ok = True
            for vertex, value in colors_at.items():
                if vertex in color:
                    if color[vertex] != value:
                        ok = False
                        break
                else:
                    color[vertex] = value
                    changed_colors.append(vertex)
            if not ok:
                for vertex in changed_colors:
                    del color[vertex]
                continue

            for vertex, value in contribs.items():
                contribution[vertex] = (contribution[vertex] + value) % 4

            for vertex in colors_at:
                if vertex not in future and contribution[vertex] % 4 != residues[color[vertex]]:
                    ok = False
                    break

            if ok:
                chosen[idx] = sig_index
                if dfs(pos + 1):
                    return True
                chosen[idx] = None

            for vertex, value in contribs.items():
                contribution[vertex] = (contribution[vertex] - value) % 4
            for vertex in changed_colors:
                del color[vertex]

        failed.add(key)
        return False

    ok = dfs(0)
    return ok, [item if item is not None else -1 for item in chosen] if ok else None


def solve(cycles: list[Cycle], colors: int) -> tuple[bool, tuple[int, ...] | None, list[int] | None]:
    for residues in product(range(4), repeat=colors):
        ok, chosen = solve_with_residues(cycles, colors, residues)
        if ok:
            return True, residues, chosen
    return False, None, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycles", help="semicolon-separated cycles, e.g. 0,1,2;0,3,4")
    parser.add_argument("--colors", type=int, default=3)
    parser.add_argument("--random", type=int, default=0)
    parser.add_argument("--blocks", type=int, default=8)
    parser.add_argument("--min-len", type=int, default=3)
    parser.add_argument("--max-len", type=int, default=8)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.cycles:
        cycles = cactus_signature_dp.parse_cycles(args.cycles)
        ok, residues, chosen = solve(cycles, args.colors)
        print("cycles=" + ";".join(",".join(map(str, cycle)) for cycle in cycles))
        print(f"articulations={sorted(cactus_signature_dp.articulation_vertices(cycles))}")
        print(f"colors={args.colors}")
        print(f"modular_dp={'yes' if ok else 'no'}")
        if residues is not None:
            print("residues=" + ",".join(map(str, residues)))
        if chosen is not None:
            print("chosen=" + ",".join(map(str, chosen)))
        return

    rng = random.Random(args.seed)
    for trial in range(args.random):
        cycles = cactus_signature_dp.random_cycle_cactus(
            args.blocks,
            args.min_len,
            args.max_len,
            rng.randrange(1 << 30),
        )
        ok, residues, _chosen = solve(cycles, args.colors)
        print(
            f"trial={trial} blocks={args.blocks} vertices={1 + sum(len(cycle)-1 for cycle in cycles)} "
            f"ok={ok} residues={residues}"
        )
        if not ok:
            print("cycles=" + ";".join(",".join(map(str, cycle)) for cycle in cycles))
            return
    print("no_counterexample_seen")


if __name__ == "__main__":
    main()
