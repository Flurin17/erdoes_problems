#!/usr/bin/env python3
"""Audit the case bounds used in Lemma 28N for the parity pair."""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import sys
from collections import defaultdict


def load_symbolic_module():
    path = pathlib.Path(__file__).with_name("parity_pair_symbolic.py")
    spec = importlib.util.spec_from_file_location("parity_pair_symbolic", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load parity_pair_symbolic.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["parity_pair_symbolic"] = module
    spec.loader.exec_module(module)
    return module


def classify(c) -> str:
    y_parities = int(c.ye > 0) + int(c.yo > 0)
    if y_parities == 0:
        return "no_core"
    if y_parities == 1:
        return "one_core"
    return "two_core"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-h", type=int, default=7)
    parser.add_argument("--max-h", type=int, default=80)
    args = parser.parse_args()

    pps = load_symbolic_module()
    print("h max_total max_pure max_zero max_no_core max_one_core max_two_core")
    for h in range(args.min_h, args.max_h + 1):
        maxima: dict[str, int] = defaultdict(int)
        max_total = 0
        for c in pps.all_counts(h):
            if not pps.is_regular_with_degree(h, c):
                continue
            degree = pps.degrees(h, c)[0][1]
            max_total = max(max_total, c.total)
            if c.a_total == 0 or c.b_total == 0:
                maxima["pure"] = max(maxima["pure"], c.total)
                if c.total > h - 1:
                    raise AssertionError((h, "pure", c))
                continue
            if degree == 0:
                maxima["zero"] = max(maxima["zero"], c.total)
                if c.total > h - 1:
                    raise AssertionError((h, "zero", c))
                continue
            case = classify(c)
            maxima[case] = max(maxima[case], c.total)
            if case == "no_core" and c.total > 3:
                raise AssertionError((h, "no_core", c))
            if case == "one_core":
                y = c.ye + c.yo
                if c.total > max(5, y + 3) or c.total > h - 1:
                    raise AssertionError((h, "one_core", c))
            if case == "two_core" and c.total > 6:
                raise AssertionError((h, "two_core", c))
        if max_total >= h:
            raise AssertionError((h, "large_regular", max_total))
        print(
            h,
            max_total,
            maxima["pure"],
            maxima["zero"],
            maxima["no_core"],
            maxima["one_core"],
            maxima["two_core"],
        )


if __name__ == "__main__":
    main()
