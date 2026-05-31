#!/usr/bin/env python3
"""Run and aggregate residue-class scans for Erdos problem 647.

The C++ search program scans values of

    N = variable_mod * X + variable_rem.

This driver launches one job per residue class, computes exact per-residue
X-ranges for a half-open N interval, and aggregates the summary lines emitted
by prime_tuple_search or prime_tuple_search128.
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import subprocess
import sys
import time
from pathlib import Path


DEFAULT_RESIDUES = (
    0,
    858,
    1287,
    1716,
    2431,
    2574,
    4862,
    5291,
    6149,
    8151,
    9009,
    9867,
    10582,
    12155,
    12584,
    13013,
    13442,
    16302,
    17017,
    17160,
    18733,
    19877,
    20306,
    20735,
    21164,
    24310,
    24453,
    25168,
    27170,
    28028,
    28457,
    29315,
    29601,
    31603,
    32032,
    32461,
    35321,
    36608,
    37752,
    38896,
    44187,
)


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parse_residues(text: str | None) -> list[int]:
    if text is None:
        return list(DEFAULT_RESIDUES)
    values: list[int] = []
    for part in text.replace("\n", ",").split(","):
        stripped = part.strip()
        if stripped:
            values.append(int(stripped))
    return values


def x_range_for_residue(n_start: int, n_stop: int, modulus: int, residue: int) -> tuple[int, int]:
    start = max(0, ceil_div(n_start - residue, modulus))
    stop = max(start, ceil_div(n_stop - residue, modulus))
    return start, stop - start


def parse_summary(path: Path) -> dict[str, object]:
    result: dict[str, object] = {
        "prime_tuples": 0,
        "quick_pass": 0,
        "branches": collections.Counter(),
        "fails": collections.Counter(),
        "best": (0, None, None, None),
        "survive": [],
        "quick": [],
    }
    if not path.exists():
        return result

    done_re = re.compile(r"DONE .* prime_tuples=(\d+) quick_pass=(\d+)")
    branch_re = re.compile(r"BRANCH_COUNTS A=(\d+) B=(\d+)")
    best_re = re.compile(r"BEST_FIRST_FAIL k=(\d+) N=(\d+) n=(\d+) tau=(\d+)")

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("SURVIVE"):
            result["survive"].append(line)  # type: ignore[index, union-attr]
        if line.startswith("QUICK_PASS") or line.startswith("CANDIDATE"):
            result["quick"].append(line)  # type: ignore[index, union-attr]

        match = done_re.match(line)
        if match:
            result["prime_tuples"] = int(result["prime_tuples"]) + int(match.group(1))
            result["quick_pass"] = int(result["quick_pass"]) + int(match.group(2))
            continue

        match = branch_re.match(line)
        if match:
            branches = result["branches"]
            assert isinstance(branches, collections.Counter)
            branches["A"] += int(match.group(1))
            branches["B"] += int(match.group(2))
            continue

        match = best_re.match(line)
        if match:
            k = int(match.group(1))
            tau = int(match.group(4))
            current = result["best"]
            assert isinstance(current, tuple)
            if k > current[0] or (k == current[0] and (current[3] is None or tau < current[3])):
                result["best"] = (k, int(match.group(2)), int(match.group(3)), tau)
            continue

        if line.startswith("FIRST_FAIL_COUNTS"):
            fails = result["fails"]
            assert isinstance(fails, collections.Counter)
            for part in line.split()[1:]:
                k, value = part.split(":")
                fails[int(k)] += int(value)
    return result


def merge_summaries(paths: list[Path]) -> dict[str, object]:
    aggregate: dict[str, object] = {
        "prime_tuples": 0,
        "quick_pass": 0,
        "branches": collections.Counter(),
        "fails": collections.Counter(),
        "best": (0, None, None, None),
        "survive": [],
        "quick": [],
    }
    for path in paths:
        item = parse_summary(path)
        aggregate["prime_tuples"] = int(aggregate["prime_tuples"]) + int(item["prime_tuples"])
        aggregate["quick_pass"] = int(aggregate["quick_pass"]) + int(item["quick_pass"])
        aggregate_branches = aggregate["branches"]
        item_branches = item["branches"]
        aggregate_fails = aggregate["fails"]
        item_fails = item["fails"]
        assert isinstance(aggregate_branches, collections.Counter)
        assert isinstance(item_branches, collections.Counter)
        assert isinstance(aggregate_fails, collections.Counter)
        assert isinstance(item_fails, collections.Counter)
        aggregate_branches.update(item_branches)
        aggregate_fails.update(item_fails)
        aggregate["survive"].extend(item["survive"])  # type: ignore[index, union-attr]
        aggregate["quick"].extend(item["quick"])  # type: ignore[index, union-attr]

        best = aggregate["best"]
        candidate = item["best"]
        assert isinstance(best, tuple)
        assert isinstance(candidate, tuple)
        if candidate[0] > best[0] or (
            candidate[0] == best[0] and candidate[3] is not None and (best[3] is None or candidate[3] < best[3])
        ):
            aggregate["best"] = candidate
    return aggregate


def print_summary(summary: dict[str, object], elapsed: float | None = None) -> None:
    if elapsed is not None:
        print(f"AGG elapsed={elapsed:.1f}")
    print(f"AGG prime_tuples={summary['prime_tuples']} quick_pass={summary['quick_pass']}")
    branches = summary["branches"]
    fails = summary["fails"]
    assert isinstance(branches, collections.Counter)
    assert isinstance(fails, collections.Counter)
    print(f"AGG BRANCH_COUNTS A={branches['A']} B={branches['B']}")
    best = summary["best"]
    assert isinstance(best, tuple)
    print(f"AGG BEST_FIRST_FAIL k={best[0]} N={best[1]} n={best[2]} tau={best[3]}")
    fail_parts = " ".join(f"{k}:{fails[k]}" for k in sorted(fails))
    print(f"AGG FIRST_FAIL_COUNTS {fail_parts}".rstrip())
    survive = summary["survive"]
    quick = summary["quick"]
    assert isinstance(survive, list)
    assert isinstance(quick, list)
    print(f"AGG survive_count={len(survive)}")
    for line in survive:
        print(line)
    print(f"AGG quick_count={len(quick)}")
    for line in quick:
        print(line)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", required=True, help="prime_tuple_search binary to run")
    parser.add_argument("--n-start", type=int, required=True, help="inclusive lower N bound")
    parser.add_argument("--n-stop", type=int, required=True, help="exclusive upper N bound")
    parser.add_argument("--modulus", type=int, default=46189)
    parser.add_argument("--residues", help="comma-separated residue list; default is the 41-class list")
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=max(1, os.cpu_count() or 1))
    parser.add_argument("--segment", type=int, default=10_000_000)
    parser.add_argument("--sieve-limit", type=int, default=10_000)
    parser.add_argument("--quick-shift", type=int, default=5000)
    parser.add_argument("--report-survive", type=int, default=15)
    parser.add_argument("--extra-arg", action="append", default=[], help="extra argument passed through verbatim")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--aggregate-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.n_stop <= args.n_start:
        raise SystemExit("--n-stop must be greater than --n-start")
    if args.workers < 1:
        raise SystemExit("--workers must be positive")

    residues = parse_residues(args.residues)
    jobs = []
    for residue in residues:
        start, count = x_range_for_residue(args.n_start, args.n_stop, args.modulus, residue)
        jobs.append((residue, start, count, args.outdir / f"res_{residue}.log"))

    print(
        f"RANGE n_start={args.n_start} n_stop={args.n_stop} modulus={args.modulus} "
        f"jobs={len(jobs)} total_x={sum(count for _, _, count, _ in jobs)} outdir={args.outdir}"
    )
    if args.dry_run:
        for residue, start, count, _ in jobs:
            print(f"JOB residue={residue} start={start} count={count}")
        return 0

    args.outdir.mkdir(parents=True, exist_ok=True)

    if args.aggregate_only:
        print_summary(merge_summaries([path for _, _, _, path in jobs]))
        return 0

    active = []
    completed: list[Path] = []
    next_index = 0
    started = time.time()
    failed = False

    while next_index < len(jobs) or active:
        while not failed and next_index < len(jobs) and len(active) < args.workers:
            residue, start, count, path = jobs[next_index]
            next_index += 1
            command = [
                args.binary,
                "--variable-mod",
                str(args.modulus),
                "--variable-rem",
                str(residue),
                "--start",
                str(start),
                "--count",
                str(count),
                "--segment",
                str(args.segment),
                "--sieve-limit",
                str(args.sieve_limit),
                "--quick-shift",
                str(args.quick_shift),
                "--report-survive",
                str(args.report_survive),
                "--stats",
                *args.extra_arg,
            ]
            handle = path.open("w", encoding="utf-8")
            process = subprocess.Popen(command, stdout=handle, stderr=subprocess.STDOUT)
            active.append((process, handle, residue, path, time.time()))
            print(f"START residue={residue} start={start} count={count}", flush=True)

        time.sleep(2)
        still_active = []
        for process, handle, residue, path, job_start in active:
            returncode = process.poll()
            if returncode is None:
                still_active.append((process, handle, residue, path, job_start))
                continue
            handle.close()
            completed.append(path)
            elapsed = time.time() - job_start
            print(f"DONE residue={residue} rc={returncode} elapsed={elapsed:.1f}", flush=True)
            if returncode != 0:
                failed = True
        active = still_active

    summary = merge_summaries([path for _, _, _, path in jobs])
    print_summary(summary, time.time() - started)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
