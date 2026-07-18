# Exact enumeration

Run from the problem directory with

```sh
python3 computational/enumerate_a.py --limit 100000 --cross-check 1000
```

The optimized ascending enumerator uses exact integer bitsets and the
complementary excess target \(\sigma(n)-2n\).  The initial range is checked by
an independent divisor scan, meet-in-the-middle subset sums, and direct tests
of every proper divisor.  Assertions also verify factorization, divisor sums,
upward closure, antichainness, and hand fixtures.

The output is experimental evidence only.  An empty finite search region or
an apparent density trend is not used as an asymptotic proof.

Add `--include-members` to print the complete list.  By default the output
contains its SHA-256 digest and the first and last 25 entries.
