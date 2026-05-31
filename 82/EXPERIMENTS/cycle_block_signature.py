#!/usr/bin/env python3
"""Finite signatures for cycle blocks in self-labelled mod-4 cactus tests.

Marked vertices represent articulation vertices whose labels are fixed by the
rest of a cactus.  A signature records, for the marked vertices in cyclic
order, their labels and the same-labelled degree contribution coming from
this cycle block.  All unmarked vertices must already satisfy the
self-labelled mod-4 condition inside the cycle.
"""

from __future__ import annotations

import argparse
from itertools import product


def signatures(n: int, marked: tuple[int, ...]) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    marked_set = set(marked)
    internal = [v for v in range(n) if v not in marked_set]
    out: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for marked_labels in product(range(4), repeat=len(marked)):
        labels = [0] * n
        for vertex, label in zip(marked, marked_labels):
            labels[vertex] = label
        for internal_labels in product(range(4), repeat=len(internal)):
            for vertex, label in zip(internal, internal_labels):
                labels[vertex] = label
            ok = True
            for vertex in internal:
                degree = sum(
                    1
                    for neighbor in ((vertex - 1) % n, (vertex + 1) % n)
                    if labels[neighbor] == labels[vertex]
                )
                if degree % 4 != labels[vertex]:
                    ok = False
                    break
            if not ok:
                continue
            contribution = tuple(
                sum(
                    1
                    for neighbor in ((vertex - 1) % n, (vertex + 1) % n)
                    if labels[neighbor] == labels[vertex]
                )
                for vertex in marked
            )
            out.add((marked_labels, contribution))
    return out


def summarize(n: int, marked: tuple[int, ...]) -> None:
    sigs = signatures(n, marked)
    print(f"cycle_length={n}")
    print("marked=" + ",".join(map(str, marked)))
    print(f"signature_count={len(sigs)}")
    by_label: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for labels, contribution in sigs:
        by_label.setdefault(labels, set()).add(contribution)
    print(f"label_patterns={len(by_label)}")
    for labels in sorted(by_label):
        contributions = sorted(by_label[labels])
        print(
            "  labels="
            + ",".join(map(str, labels))
            + " contributions="
            + " ".join(",".join(map(str, item)) for item in contributions)
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--marked", required=True)
    args = parser.parse_args()
    marked = tuple(int(item) for item in args.marked.split(",") if item)
    summarize(args.n, marked)


if __name__ == "__main__":
    main()
