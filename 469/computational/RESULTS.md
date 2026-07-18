# Recorded exact runs

## Initial cross-check

Command:

```sh
python3 computational/enumerate_a.py --limit 10000 --cross-check 1000
```

Environment date: 2026-07-17 UTC.  Script-reported runtime: 0.27083 seconds
(host scheduling time excluded).  Every assertion passed, including the
independent divisor-scan/meet-in-the-middle checker through 1,000.

- Members through 10,000: 128.
- Largest member: 9,928.
- Counts by \(\omega\): 30 with \(\omega=2\), 38 with \(\omega=3\), and 60
  with \(\omega=4\).
- Squarefree members: 47.
- Across all cover quotients \(n/p\): 381 were deficient and 33 were abundant
  nonsemiperfect; none was perfect or semiperfect.
- SHA-256 of the comma-separated full member list followed by a newline:
  `1b23aa6342a81dc5108fc88c0ec2b88fa3ef61b3a34ce699a1eaa1292212e179`.

The observed dyadic reciprocal masses are not treated as asymptotic evidence.
This run is a correctness fixture and a source of conjectures only.

## Verification rerun

The same command was rerun on 2026-07-18 UTC after the reporting changes.
Every assertion again passed, the count remained 128, and the member-list
hash was unchanged.  Script-reported runtime was 0.134493 seconds.
