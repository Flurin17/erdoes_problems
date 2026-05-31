#!/usr/bin/env python3
"""Signature-DP solver for self-labelled mod-4 colorings of cycle cacti."""

from __future__ import annotations

import argparse
import random
from functools import lru_cache

import cycle_block_signature


Cycle = tuple[int, ...]


def random_cycle_cactus(
    blocks: int,
    min_len: int,
    max_len: int,
    seed: int,
) -> list[Cycle]:
    rng = random.Random(seed)
    cycles: list[Cycle] = []
    vertex_count = 1
    for _ in range(blocks):
        length = rng.randint(min_len, max_len)
        root = rng.randrange(vertex_count)
        new_vertices = tuple(range(vertex_count, vertex_count + length - 1))
        vertex_count += length - 1
        cycles.append((root,) + new_vertices)
    return cycles


def articulation_vertices(cycles: list[Cycle]) -> set[int]:
    counts: dict[int, int] = {}
    for cycle in cycles:
        for vertex in cycle:
            counts[vertex] = counts.get(vertex, 0) + 1
    return {vertex for vertex, count in counts.items() if count > 1}


def cycle_signatures(cycle: Cycle, articulations: set[int]) -> list[tuple[dict[int, int], dict[int, int]]]:
    marked_positions = tuple(i for i, vertex in enumerate(cycle) if vertex in articulations)
    if not marked_positions:
        return [({}, {})]
    raw = cycle_block_signature.signatures(len(cycle), marked_positions)
    out: list[tuple[dict[int, int], dict[int, int]]] = []
    marked_vertices = tuple(cycle[i] for i in marked_positions)
    for labels, contributions in raw:
        out.append((dict(zip(marked_vertices, labels)), dict(zip(marked_vertices, contributions))))
    return out


def solve(cycles: list[Cycle]) -> tuple[bool, list[int] | None]:
    articulations = articulation_vertices(cycles)
    signatures = [cycle_signatures(cycle, articulations) for cycle in cycles]
    order = sorted(range(len(cycles)), key=lambda i: len(signatures[i]))
    contribution = {vertex: 0 for vertex in articulations}
    label: dict[int, int] = {}
    chosen: list[int | None] = [None] * len(cycles)

    # For pruning, remember which unprocessed cycles touch each articulation.
    remaining_touch: list[set[int]] = []
    seen: set[int] = set()
    for idx in reversed(order):
        seen.update(v for v in cycles[idx] if v in articulations)
        remaining_touch.append(set(seen))
    remaining_touch = list(reversed(remaining_touch))

    @lru_cache(maxsize=None)
    def impossible_cache(pos: int, label_items: tuple[tuple[int, int], ...], contrib_items: tuple[tuple[int, int], ...]) -> bool:
        # Cache key for failed states only; actual recursion mutates dictionaries.
        _ = (pos, label_items, contrib_items)
        return False

    def dfs(pos: int) -> bool:
        label_key = tuple(sorted(label.items()))
        contrib_key = tuple(sorted((v, contribution[v] % 4) for v in articulations if v in label))
        if impossible_cache(pos, label_key, contrib_key):
            return False

        if pos == len(order):
            return all(contribution[v] % 4 == label[v] for v in articulations)

        idx = order[pos]
        future = remaining_touch[pos + 1] if pos + 1 < len(order) else set()
        for sig_index, (labels, contribs) in enumerate(signatures[idx]):
            changed_labels: list[int] = []
            ok = True
            for vertex, value in labels.items():
                if vertex in label:
                    if label[vertex] != value:
                        ok = False
                        break
                else:
                    label[vertex] = value
                    changed_labels.append(vertex)
            if not ok:
                for vertex in changed_labels:
                    del label[vertex]
                continue

            for vertex, value in contribs.items():
                contribution[vertex] = (contribution[vertex] + value) % 4

            # If an articulation will not appear again, its congruence must
            # already be satisfied.
            for vertex in labels:
                if vertex not in future and contribution[vertex] % 4 != label[vertex]:
                    ok = False
                    break

            if ok:
                chosen[idx] = sig_index
                if dfs(pos + 1):
                    return True
                chosen[idx] = None

            for vertex, value in contribs.items():
                contribution[vertex] = (contribution[vertex] - value) % 4
            for vertex in changed_labels:
                del label[vertex]

        return False

    ok = dfs(0)
    return ok, [item if item is not None else -1 for item in chosen] if ok else None


def parse_cycles(text: str) -> list[Cycle]:
    cycles: list[Cycle] = []
    for block in text.split(";"):
        block = block.strip()
        if not block:
            continue
        cycles.append(tuple(int(item) for item in block.split(",") if item))
    return cycles


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycles", help="semicolon-separated cycles, e.g. 0,1,2;0,3,4")
    parser.add_argument("--random", type=int, default=0, help="number of random instances")
    parser.add_argument("--blocks", type=int, default=5)
    parser.add_argument("--min-len", type=int, default=3)
    parser.add_argument("--max-len", type=int, default=6)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.cycles:
        cycles = parse_cycles(args.cycles)
        ok, chosen = solve(cycles)
        print("cycles=" + ";".join(",".join(map(str, cycle)) for cycle in cycles))
        print(f"articulations={sorted(articulation_vertices(cycles))}")
        print(f"signature_dp={'yes' if ok else 'no'}")
        if chosen is not None:
            print("chosen=" + ",".join(map(str, chosen)))
        return

    rng = random.Random(args.seed)
    for trial in range(args.random):
        cycles = random_cycle_cactus(
            args.blocks,
            args.min_len,
            args.max_len,
            rng.randrange(1 << 30),
        )
        ok, _chosen = solve(cycles)
        print(
            f"trial={trial} blocks={args.blocks} vertices={1 + sum(len(cycle)-1 for cycle in cycles)} "
            f"ok={ok}"
        )
        if not ok:
            print("cycles=" + ";".join(",".join(map(str, cycle)) for cycle in cycles))
            return
    print("no_counterexample_seen")


if __name__ == "__main__":
    main()
