#!/usr/bin/env python3
"""Summarize exhaustive word-quotient interval artifacts."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def load_interval(path: Path) -> dict:
    data = json.loads(path.read_text())
    required = (
        "first_classified_word_index",
        "last_classified_word_index",
        "classified_words",
        "classified_weight",
        "mixed_status_words",
        "status_weight_counts",
        "word_count_mismatches",
    )
    missing = [key for key in required if key not in data]
    if missing:
        raise SystemExit(f"{path}: missing fields {missing}")
    if data.get("classification_mode") != "exhaustive":
        raise SystemExit(f"{path}: not an exhaustive interval artifact")
    return data


def summarize(paths: list[Path]) -> dict:
    intervals = []
    status_weights: Counter[str] = Counter()
    mixed_status_words = 0
    word_count_mismatches: list[dict] = []
    classified_weight = 0
    classified_words = 0
    n_values = set()
    tile_values = set()
    quotient_groups = set()
    outside_cover_shells = set()

    for path in paths:
        data = load_interval(path)
        first = data["first_classified_word_index"]
        last = data["last_classified_word_index"]
        if first is None or last is None:
            raise SystemExit(f"{path}: empty interval")
        expected_count = last - first + 1
        if expected_count != data["classified_words"]:
            raise SystemExit(
                f"{path}: interval length {expected_count} != classified_words {data['classified_words']}"
            )
        intervals.append((first, last, path.name))
        status_weights.update(data["status_weight_counts"])
        mixed_status_words += data["mixed_status_words"]
        word_count_mismatches.extend(data["word_count_mismatches"])
        classified_weight += data["classified_weight"]
        classified_words += data["classified_words"]
        n_values.add(data.get("n"))
        tile_values.add(tuple(data.get("tile", ())))
        quotient_groups.add(data.get("quotient_groups"))
        outside_cover_shells.add(data.get("outside_cover_shells"))

    intervals.sort()
    gaps = []
    overlaps = []
    for (left_first, left_last, _left_name), (right_first, right_last, _right_name) in zip(
        intervals,
        intervals[1:],
    ):
        if right_first <= left_last:
            overlaps.append((right_first, min(left_last, right_last)))
        elif right_first > left_last + 1:
            gaps.append((left_last + 1, right_first - 1))

    covered_first = intervals[0][0] if intervals else None
    covered_last = intervals[-1][1] if intervals else None
    contiguous_prefix = bool(intervals and covered_first == 1 and not gaps and not overlaps)
    def shared_value(values: set):
        non_null = {value for value in values if value is not None}
        if len(non_null) == 1:
            return next(iter(non_null))
        return sorted(values, key=lambda value: (value is None, repr(value)))

    return {
        "files": [path.name for path in paths],
        "intervals": [
            {"first": first, "last": last, "file": name}
            for first, last, name in intervals
        ],
        "n": next(iter(n_values)) if len(n_values) == 1 else sorted(n_values),
        "tile": list(next(iter(tile_values))) if len(tile_values) == 1 else sorted(map(list, tile_values)),
        "quotient_groups": shared_value(quotient_groups),
        "outside_cover_shells": (
            shared_value(outside_cover_shells)
        ),
        "covered_first": covered_first,
        "covered_last": covered_last,
        "classified_words": classified_words,
        "classified_weight": classified_weight,
        "status_weight_counts": dict(sorted(status_weights.items())),
        "mixed_status_words": mixed_status_words,
        "word_count_mismatches": word_count_mismatches,
        "gaps": gaps,
        "overlaps": overlaps,
        "contiguous_prefix": contiguous_prefix,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    result = summarize(args.files)
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.json_out is not None:
        args.json_out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
