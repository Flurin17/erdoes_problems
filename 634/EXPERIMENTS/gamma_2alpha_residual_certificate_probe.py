#!/usr/bin/env python3
"""Probe exact residual obstruction certificates for capped `gamma=2alpha` shells."""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import refined_survivors_for_n  # noqa: E402
from gamma_2alpha_residual_capped_census import LocalCoverChecker, iter_capped_demands  # noqa: E402
from gamma_2alpha_residual_failure_causes import (  # noqa: E402
    ShellDiagnostic,
    counter_tuple_text,
    diagnose_shell,
)


def certificate_key(detail: ShellDiagnostic) -> str:
    if detail.status == "corner-label-violation":
        return (
            f"{detail.status}|forced={counter_tuple_text(detail.forced_angles)}"
            f"|viol={counter_tuple_text(tuple((f'{angle}:{labels}', count) for angle, labels, count in detail.violation_types))}"
        )
    if detail.status in (
        "pinch-sector-obstruction",
        "split-component-obstruction",
        "split-corner-label-obstruction",
        "not-simple-cycle",
    ):
        return (
            f"{detail.status}|degree={detail.degree_profile}"
            f"|labels={counter_tuple_text(detail.residual_labels)}"
            f"|pinch={counter_tuple_text(detail.pinch_cyclic_labels)}"
            f"|sectors={counter_tuple_text(detail.pinch_sector_signatures)}"
            f"|split={detail.split_options}/{detail.split_component_pass_options}/{detail.split_corner_pass_options}"
            f"|fail={counter_tuple_text(detail.split_failure_reasons)}"
        )
    return detail.status


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--min-total-mixed", type=int, default=6)
    parser.add_argument("--max-total-mixed", type=int, default=6)
    parser.add_argument("--outside-local-cover", action="store_true")
    parser.add_argument("--limit", type=int, default=500)
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            radicand = exact.field_radicand(survivor)
            if radicand is None:
                print("  exact quadratic classifier unavailable", flush=True)
                continue
            local_checker = LocalCoverChecker(survivor, radicand) if args.outside_local_cover else None
            generated = 0
            covered = 0
            diagnosed = 0
            status_counts: Counter[str] = Counter()
            certificate_counts: Counter[str] = Counter()
            certificates_by_status: dict[str, Counter[str]] = defaultdict(Counter)

            for demand in iter_capped_demands(
                survivor,
                min_total_mixed=args.min_total_mixed,
                max_total_mixed=args.max_total_mixed,
                dedupe=True,
            ):
                generated += 1
                if local_checker is not None and local_checker.first_overlap(demand) is not None:
                    covered += 1
                    continue
                if diagnosed >= args.limit:
                    break
                detail = diagnose_shell(survivor, demand, radicand)
                diagnosed += 1
                key = certificate_key(detail)
                status_counts[detail.status] += 1
                certificate_counts[key] += 1
                certificates_by_status[detail.status][key] += 1

            cover_text = f" covered={covered}" if args.outside_local_cover else ""
            print(
                f"  generated={generated}{cover_text} diagnosed={diagnosed} "
                f"statuses={dict(sorted(status_counts.items()))} certificates={len(certificate_counts)}",
                flush=True,
            )
            for status, counts in sorted(certificates_by_status.items()):
                print(f"  top certificates for {status}:", flush=True)
                for key, count in counts.most_common(args.top):
                    print(f"    {count}: {key}", flush=True)


if __name__ == "__main__":
    main()
