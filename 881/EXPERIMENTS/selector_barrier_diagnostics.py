#!/usr/bin/env python3
"""Finite selector-cover diagnostics for cross-packet barriers.

Corollary 8.5a.7r says that, in a remaining counterexample, every selector
choosing one deleted color from each fresh packet must contain arbitrarily
late bad edges spanning multiple packets. This script checks the finite
combinatorial shadow: whether a family of cross-block edges covers every
selector in a finite product of blocks.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Iterable


Block = tuple[str, ...]
Edge = frozenset[str]


def vertex_blocks(blocks: tuple[Block, ...]) -> dict[str, int]:
    owner: dict[str, int] = {}
    for index, block in enumerate(blocks):
        for vertex in block:
            if vertex in owner:
                raise ValueError(f"vertex appears in two blocks: {vertex}")
            owner[vertex] = index
    return owner


def selector_relevant_edges(blocks: tuple[Block, ...], edges: Iterable[Edge]) -> list[Edge]:
    owner = vertex_blocks(blocks)
    relevant: list[Edge] = []
    for edge in edges:
        if any(vertex not in owner for vertex in edge):
            continue
        seen: set[int] = set()
        ok = True
        for vertex in edge:
            block_index = owner[vertex]
            if block_index in seen:
                ok = False
                break
            seen.add(block_index)
        if ok:
            relevant.append(edge)
    return relevant


def edge_support(blocks: tuple[Block, ...], edge: Edge) -> frozenset[int]:
    owner = vertex_blocks(blocks)
    return frozenset(owner[vertex] for vertex in edge)


def cover_weight(blocks: tuple[Block, ...], edges: Iterable[Edge]) -> Fraction:
    relevant = selector_relevant_edges(blocks, edges)
    block_sizes = tuple(len(block) for block in blocks)
    total = Fraction(0, 1)
    for edge in relevant:
        denominator = 1
        for block_index in edge_support(blocks, edge):
            denominator *= block_sizes[block_index]
        total += Fraction(1, denominator)
    return total


def support_sizes(blocks: tuple[Block, ...], edges: Iterable[Edge]) -> list[int]:
    relevant = selector_relevant_edges(blocks, edges)
    return sorted(len(edge_support(blocks, edge)) for edge in relevant)


def uncovered_selectors(
    blocks: tuple[Block, ...],
    edges: Iterable[Edge],
    limit: int = 8,
) -> list[tuple[str, ...]]:
    relevant = selector_relevant_edges(blocks, edges)
    failures: list[tuple[str, ...]] = []
    for selector in product(*blocks):
        selected = frozenset(selector)
        if not any(edge <= selected for edge in relevant):
            failures.append(selector)
            if len(failures) >= limit:
                break
    return failures


def first_covered_prefix(blocks: tuple[Block, ...], edges: Iterable[Edge]) -> int | None:
    edge_tuple = tuple(edges)
    for size in range(1, len(blocks) + 1):
        if not uncovered_selectors(blocks[:size], edge_tuple, limit=1):
            return size
    return None


def report(name: str, blocks: tuple[Block, ...], edges: Iterable[Edge]) -> None:
    edge_tuple = tuple(edges)
    print(name)
    print(f"first_covered_prefix={first_covered_prefix(blocks, edge_tuple)}")
    print(f"cover_weight={cover_weight(blocks, edge_tuple)}")
    print(f"support_sizes={support_sizes(blocks, edge_tuple)}")
    print(f"uncovered_selectors={uncovered_selectors(blocks, edge_tuple)}")


def main() -> None:
    blocks = (
        ("a0", "a1"),
        ("b0", "b1"),
        ("c0", "c1"),
    )

    local_edges = [frozenset(block) for block in blocks]
    report("local block cuts", blocks, local_edges)

    complete_cross_edges = [
        frozenset((a, b))
        for a in blocks[0]
        for b in blocks[1]
    ]
    print()
    report("complete cross-packet wiring", blocks, complete_cross_edges)

    complete_rank3_edges = [
        frozenset((a, b, c))
        for a in blocks[0]
        for b in blocks[1]
        for c in blocks[2]
    ]
    print()
    report("complete rank-3 product wiring", blocks, complete_rank3_edges)

    sparse_cross_edges = [
        frozenset(("a0", "b0")),
        frozenset(("b1", "c1")),
    ]
    print()
    report("sparse cross-packet wiring", blocks, sparse_cross_edges)


if __name__ == "__main__":
    main()
