#!/usr/bin/env python3
"""Try one-step staggered protection for the first interval-marker debt block."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def load_followup_helper():
    helper_path = Path(__file__).with_name("prepared_marker_followup_search.py")
    spec = importlib.util.spec_from_file_location("prepared_marker_followup_search", helper_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {helper_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    helper = load_followup_helper()
    stage = {1, 2, 3, 4, 8, 19, 25, 26, 39, 43, 44}
    previous_endpoint = 95
    print("stage=", sorted(stage))
    print("previous_endpoint=", previous_endpoint)
    for target in (25, 26, 43, 44):
        print("target", target, "ordinary")
        print(
            helper.find_protection(
                stage,
                base=3,
                previous_endpoint=previous_endpoint,
                target=target,
                max_new_size=2,
                max_candidate=150,
                slack=80,
                strict_high_excess=False,
            )
        )
        print("target", target, "strict_high_excess")
        print(
            helper.find_protection(
                stage,
                base=3,
                previous_endpoint=previous_endpoint,
                target=target,
                max_new_size=2,
                max_candidate=150,
                slack=80,
                strict_high_excess=True,
            )
        )


if __name__ == "__main__":
    main()
