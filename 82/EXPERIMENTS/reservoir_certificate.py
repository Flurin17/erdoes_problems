#!/usr/bin/env python3
"""Search for the binary reservoir certificate from PROOF.md.

Given a vector and a modulus q, choose one coordinate as reservoir, delete
tail units by specials, and try to represent the residual tail by lifted
binary-bit rectangles.  This is a sufficient condition for the full
complete-multipartite bin cover, not an exact solver.
"""

from __future__ import annotations

import argparse


def parse_vector(text: str) -> tuple[int, ...]:
    return tuple(int(item) for item in text.split(",") if item)


def active_bits(values: tuple[int, ...]) -> tuple[int, ...]:
    bits: set[int] = set()
    for value in values:
        bit = 1
        while bit <= value:
            if value & bit:
                bits.add(bit)
            bit <<= 1
    return tuple(sorted(bits))


def bit_supports(values: tuple[int, ...], bits: tuple[int, ...]) -> dict[int, int]:
    return {bit: sum(1 for value in values if value & bit) for bit in bits}


def certificate(
    vector: tuple[int, ...],
    q: int,
    reservoir_index: int,
) -> dict[str, object] | None:
    cap = q + 2
    x = vector[reservoir_index]
    tail = vector[:reservoir_index] + vector[reservoir_index + 1 :]
    tail_total = sum(tail)
    delta = q * q - x - tail_total
    if delta < 0:
        return None

    best: dict[str, object] | None = None
    residual = [0] * len(tail)

    def visit(index: int, residual_total: int) -> None:
        nonlocal best
        if best is not None:
            return
        if index == len(tail):
            z = tuple(residual)
            bits = active_bits(z)
            supports = bit_supports(z, bits)
            if any(bit * (supports[bit] + 1) > cap for bit in bits):
                return
            s = tail_total - residual_total
            r = len(bits)
            h = sum(bits)
            if s + r > q:
                return
            if x < s * (q + 1) + h:
                return
            if residual_total + h < (r - 2) * q + 2 * r - delta:
                return
            best = {
                "reservoir": reservoir_index,
                "x": x,
                "tail": tail,
                "residual": z,
                "deleted": s,
                "bits": bits,
                "supports": supports,
                "H": h,
                "B": residual_total,
                "delta": delta,
            }
            return

        # Prefer larger residuals; dense residuals are more likely to satisfy
        # the slack inequality.
        for value in range(tail[index], -1, -1):
            residual[index] = value
            visit(index + 1, residual_total + value)
            if best is not None:
                return

    visit(0, 0)
    return best


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--vector", required=True)
    parser.add_argument("--reservoir-index", type=int)
    args = parser.parse_args()

    vector = parse_vector(args.vector)
    indices = (
        [args.reservoir_index]
        if args.reservoir_index is not None
        else list(range(len(vector)))
    )
    for index in indices:
        result = certificate(vector, args.q, index)
        if result is not None:
            print("certificate=found")
            for key, value in result.items():
                if isinstance(value, tuple):
                    print(f"{key}=" + ",".join(map(str, value)))
                elif isinstance(value, dict):
                    items = ",".join(f"{bit}:{count}" for bit, count in value.items())
                    print(f"{key}={items}")
                else:
                    print(f"{key}={value}")
            return
    print("certificate=none")


if __name__ == "__main__":
    main()
