#!/usr/bin/env python3
"""Finite selector-cover diagnostics for cross-packet barriers.

Corollary 8.5a.7r says that, in a remaining counterexample, every selector
choosing one deleted color from each fresh packet must contain arbitrarily
late bad edges spanning multiple packets. This script checks the finite
combinatorial shadow: whether a family of cross-block edges covers every
selector in a finite product of blocks.
"""

from __future__ import annotations

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


def main() -> None:
    blocks = (
        ("a0", "a1"),
        ("b0", "b1"),
        ("c0", "c1"),
    )

    local_edges = [frozenset(block) for block in blocks]
    print("local block cuts")
    print(f"uncovered_selectors={uncovered_selectors(blocks, local_edges)}")

    complete_cross_edges = [
        frozenset((a, b))
        for a in blocks[0]
        for b in blocks[1]
    ]
    print()
    print("complete cross-packet wiring")
    print(f"uncovered_selectors={uncovered_selectors(blocks, complete_cross_edges)}")

    sparse_cross_edges = [
        frozenset(("a0", "b0")),
        frozenset(("b1", "c1")),
    ]
    print()
    print("sparse cross-packet wiring")
    print(f"uncovered_selectors={uncovered_selectors(blocks, sparse_cross_edges)}")


if __name__ == "__main__":
    main()
