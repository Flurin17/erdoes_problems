#!/usr/bin/env python3
"""Probe exact residual obstruction certificates for capped `gamma=2alpha` shells."""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import refined_survivors_for_n  # noqa: E402
from gamma_2alpha_residual_capped_census import LocalCoverChecker, iter_capped_demands  # noqa: E402
from gamma_2alpha_residual_chunked_census import LazyLocalCoverChecker  # noqa: E402
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


def make_local_checker(survivor, radicand: int, mode: str):
    if mode == "eager":
        return LocalCoverChecker(survivor, radicand)
    if mode == "lazy":
        return LazyLocalCoverChecker(survivor, radicand)
    raise ValueError(mode)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--min-total-mixed", type=int, default=6)
    parser.add_argument("--max-total-mixed", type=int, default=6)
    parser.add_argument("--outside-local-cover", action="store_true")
    parser.add_argument("--local-cover-mode", choices=("eager", "lazy"), default="eager")
    parser.add_argument("--skip-generated", type=int, default=0)
    parser.add_argument("--max-generated", type=int)
    parser.add_argument("--limit", type=int, default=500)
    parser.add_argument("--progress-every", type=int, default=0)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    if args.skip_generated < 0:
        raise SystemExit("--skip-generated must be nonnegative")
    if args.max_generated is not None and args.max_generated <= 0:
        raise SystemExit("--max-generated must be positive")
    if args.limit <= 0:
        raise SystemExit("--limit must be positive")

    results = []
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            radicand = exact.field_radicand(survivor)
            if radicand is None:
                print("  exact quadratic classifier unavailable", flush=True)
                continue
            local_checker = (
                make_local_checker(survivor, radicand, args.local_cover_mode)
                if args.outside_local_cover
                else None
            )
            generated = 0
            processed = 0
            covered = 0
            diagnosed = 0
            status_counts: Counter[str] = Counter()
            certificate_counts: Counter[str] = Counter()
            certificates_by_status: dict[str, Counter[str]] = defaultdict(Counter)
            started = time.monotonic()

            for demand in iter_capped_demands(
                survivor,
                min_total_mixed=args.min_total_mixed,
                max_total_mixed=args.max_total_mixed,
                dedupe=True,
            ):
                generated += 1
                if generated <= args.skip_generated:
                    continue
                if args.max_generated is not None and processed >= args.max_generated:
                    break
                processed += 1
                if local_checker is not None and local_checker.first_overlap(demand) is not None:
                    covered += 1
                elif diagnosed < args.limit:
                    detail = diagnose_shell(survivor, demand, radicand)
                    diagnosed += 1
                    key = certificate_key(detail)
                    status_counts[detail.status] += 1
                    certificate_counts[key] += 1
                    certificates_by_status[detail.status][key] += 1
                if args.progress_every and processed % args.progress_every == 0:
                    elapsed = time.monotonic() - started
                    rate = processed / elapsed if elapsed else 0.0
                    print(
                        f"  progress generated={generated} processed={processed} "
                        f"covered={covered} diagnosed={diagnosed} rate={rate:.1f}/s",
                        flush=True,
                    )
                if diagnosed >= args.limit:
                    break

            cover_text = f" covered={covered}" if args.outside_local_cover else ""
            print(
                f"  generated={generated} processed={processed}{cover_text} diagnosed={diagnosed} "
                f"statuses={dict(sorted(status_counts.items()))} certificates={len(certificate_counts)}",
                flush=True,
            )
            result = {
                "n": n,
                "tile": survivor.candidate.tile,
                "radicand": radicand,
                "min_total_mixed": args.min_total_mixed,
                "max_total_mixed": args.max_total_mixed,
                "outside_local_cover": args.outside_local_cover,
                "local_cover_mode": args.local_cover_mode if args.outside_local_cover else None,
                "skip_generated": args.skip_generated,
                "max_generated": args.max_generated,
                "limit": args.limit,
                "generated": generated,
                "processed": processed,
                "covered": covered,
                "diagnosed": diagnosed,
                "status_counts": dict(sorted(status_counts.items())),
                "certificate_counts": dict(sorted(certificate_counts.items())),
            }
            results.append(result)
            for status, counts in sorted(certificates_by_status.items()):
                print(f"  top certificates for {status}:", flush=True)
                for key, count in counts.most_common(args.top):
                    print(f"    {count}: {key}", flush=True)
    if args.json_out is not None:
        payload = results[0] if len(results) == 1 else results
        args.json_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
