#!/usr/bin/env python3
"""Cross-check independent solvers and reject a forged certificate."""

import json
import tempfile
from pathlib import Path

from compute_451 import direct_scan, solve as jump_solve
from segmented_451 import solve as segmented_solve
from verify_451 import verify


for k in range(1, 51):
    n, _ = jump_solve(k)
    if direct_scan(k, n) != n or segmented_solve(k) != n:
        raise RuntimeError(f"solver disagreement at k={k}")

forged = {
    "problem": 451,
    "k": 2,
    "n": 9,
    "chain": [
        {"start": 5, "end": 6, "p": 3, "q": 4 / 3},
        {"start": 7, "end": 8, "p": 3, "q": 2},
    ],
}
with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "forged.json"
    path.write_text(json.dumps(forged))
    try:
        verify(path)
    except ValueError:
        pass
    else:
        raise RuntimeError("forged fractional-q certificate was accepted")

print("independent solvers agree through k=50; forged certificate rejected")
