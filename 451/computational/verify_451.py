#!/usr/bin/env python3
"""Independent checker for modular-jump certificates for problem 451."""

import argparse
import json
from pathlib import Path


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return n == d
        d += 1 if d == 2 else 2
    return True


def forbidden_primes(k: int) -> list[int]:
    return [p for p in range(k + 1, 2 * k) if is_prime(p)]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def verify(path: Path) -> None:
    data = json.loads(path.read_text())
    require(type(data) is dict, f"{path}: top level must be an object")
    require(data.get("problem") == 451, f"{path}: wrong problem number")
    k, n = data["k"], data["n"]
    require(type(k) is int and k >= 1, f"{path}: invalid k")
    require(type(n) is int and n > 2 * k, f"{path}: invalid n")
    require(type(data.get("chain")) is list, f"{path}: chain must be a list")
    ps = forbidden_primes(k)
    cursor = 2 * k + 1
    for index, row in enumerate(data["chain"]):
        require(type(row) is dict, f"{path}: row {index} must be an object")
        try:
            start, end, p, q = (row[x] for x in ("start", "end", "p", "q"))
        except KeyError as exc:
            raise ValueError(f"{path}: row {index} lacks {exc.args[0]}") from exc
        require(
            all(type(x) is int for x in (start, end, p, q)),
            f"{path}: row {index} has a non-integer field",
        )
        require(start == cursor, f"{path}: coverage gap before row {index}")
        require(p in ps and q >= 1, f"{path}: invalid witness in row {index}")
        require(
            q * p + 1 <= start <= q * p + k,
            f"{path}: row {index} does not cover its start",
        )
        require(end == q * p + k, f"{path}: wrong endpoint in row {index}")
        cursor = end + 1
    require(cursor == n, f"{path}: chain does not end immediately before n")
    require(
        all(n % p == 0 or n % p > k for p in ps),
        f"{path}: terminal n is not admissible",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    count = 0
    for item in args.paths:
        paths = sorted(item.glob("*.json")) if item.is_dir() else [item]
        for path in paths:
            verify(path)
            count += 1
    print(f"verified {count} certificates")


if __name__ == "__main__":
    main()
