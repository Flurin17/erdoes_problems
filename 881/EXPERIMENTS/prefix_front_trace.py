#!/usr/bin/env python3
"""Finite checks for the prefix-front conversion in Lemmas 3.1c.1--3.1c.2."""

from itertools import combinations


def subsets(seq):
    for r in range(1, len(seq) + 1):
        yield from combinations(seq, r)


def prefix_front(seq, barrier):
    barrier = {frozenset(edge) for edge in barrier}
    front = []
    for s_tuple in subsets(seq):
        s = frozenset(s_tuple)
        initial = frozenset(s_tuple[:-1])
        if any(edge <= s for edge in barrier) and not any(edge <= initial for edge in barrier):
            front.append(s_tuple)
    return front


def first_completion_max_property(front, barrier):
    barrier = {frozenset(edge) for edge in barrier}
    failures = []
    for s_tuple in front:
        s = frozenset(s_tuple)
        top = s_tuple[-1]
        for edge in barrier:
            if edge <= s and top not in edge:
                failures.append((s_tuple, tuple(sorted(edge))))
    return failures


def omitted_top_shrink_failures(front, barrier):
    barrier = {frozenset(edge) for edge in barrier}
    failures = []
    for s_tuple in front:
        top = s_tuple[-1]
        proper_prefix = set(s_tuple[:-1])
        for edge in barrier:
            if edge <= proper_prefix:
                failures.append((s_tuple, tuple(sorted(edge)), top))
    return failures


def second_element_edges(seq):
    edges = []
    for s_tuple in subsets(seq):
        if len(s_tuple) >= 2 and len(s_tuple) == s_tuple[1]:
            edges.append(s_tuple)
    return edges


def main():
    seq = tuple(range(2, 10))
    examples = {
        "second-element front": second_element_edges(seq),
        "non-prefix weak family": [(2, 5), (3, 4), (6, 8, 9)],
    }

    print("prefix-front trace diagnostic")
    print("sequence=", seq)
    for name, barrier in examples.items():
        front = prefix_front(seq, barrier)
        max_failures = first_completion_max_property(front, barrier)
        shrink_failures = omitted_top_shrink_failures(front, barrier)
        print()
        print(name)
        print("barrier edges=", barrier[:8], "..." if len(barrier) > 8 else "")
        print("prefix-front size=", len(front))
        print("first prefix-front edges=", front[:8])
        print("contained-edge-without-top failures=", max_failures or "none")
        print("omitted-top shrink already in barrier=", shrink_failures or "none")


if __name__ == "__main__":
    main()
